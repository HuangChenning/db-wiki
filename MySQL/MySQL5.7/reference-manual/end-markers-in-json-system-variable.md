---
title: "8.15.9 The end_markers_in_json System Variable"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/end-markers-in-json-system-variable.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.15.9 The end\_markers\_in\_json System Variable

When reading a very large JSON document, it can be difficult to pair its closing bracket and opening brackets; setting [`end_markers_in_json=ON`](server-system-variables.md) repeats the structure's key, if it has one, near the closing bracket. This variable affects both optimizer traces and the output of `EXPLAIN FORMAT=JSON`.

Note

If [`end_markers_in_json`](server-system-variables.md) is enabled, the repetition of the key means the result is not a valid JSON document, and causes JSON parsers to throw an error.