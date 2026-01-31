---
title: "Python Tips and Tricks"
date: 2025-09-20
draft: false
description: "Useful Python tips I've learned over the years."
tags: ["python", "programming"]
---

Here are some Python tips that have been useful to me:

## List Compreh\`python
#ensions

\`\` Instead of:
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x)

# Use:
result = [x for x in range(10) if x % 2 == 0]
\`\`\`

## Dictionary Merge

\`\`\`python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
\`\`\`

These small tips can make your code more Pythonic.
