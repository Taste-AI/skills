#!/usr/bin/env python3
"""Local slop lookup — the retrievable anti-pattern rubric, no infra.

The creativity v2.1 pipeline queries a Qdrant collection of design-dimension
rubrics per section while composing ("slop k=2 per section keyword", generator
rule R4). This is the same discipline over the vendored catalog
(design-dimensions.json, 36 dimensions, slop/good/great tiers verbatim):
pure-stdlib TF-IDF, which is plenty at 34 documents.

Usage:
    python3 slop_lookup.py "generic purple gradient saas hero" [--k 2]

Prints JSON: the k most relevant dimensions with all three tier excerpts.
Cite the dimension_id in the facet sheet / verify record when a check fires.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import re

HERE = pathlib.Path(__file__).parent
CATALOG = HERE / "design-dimensions.json"

STOP = set(
    "a an and are as at be but by for from has have if in into is it its like "
    "no not of on or that the their there this to too very was what when with "
    "without you your looks look feel feels design designs".split()
)


def tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2 and t not in STOP]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--k", type=int, default=2)
    args = ap.parse_args()

    dims = json.loads(CATALOG.read_text())["dimensions"]
    docs = []
    for d in dims:
        # Name and question carry the dimension's identity; weight them up.
        body = tokens(" ".join((d["ai_slop"], d["good"], d["great"])))
        head = tokens(" ".join((d["name"], d["question"], d["section"]))) * 3
        docs.append(head + body)

    n = len(docs)
    df: dict[str, int] = {}
    for doc in docs:
        for t in set(doc):
            df[t] = df.get(t, 0) + 1

    q = tokens(args.query)
    scored = []
    for d, doc in zip(dims, docs):
        tf = {t: doc.count(t) for t in set(doc)}
        length = math.sqrt(len(doc)) or 1.0
        score = sum(
            (tf.get(t, 0) / length) * math.log(1 + n / df[t])
            for t in q
            if t in df
        )
        scored.append((score, d))
    scored.sort(key=lambda x: -x[0])

    top = [
        {
            "dimension_id": d["id"],
            "dimension_name": d["name"],
            "section": d["section"],
            "question": d["question"],
            "slop": d["ai_slop"],
            "good": d["good"],
            "great": d["great"],
            "score": round(s, 3),
        }
        for s, d in scored[: max(1, args.k)]
        if s > 0
    ]
    print(json.dumps({"query": args.query, "anti_patterns": top}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
