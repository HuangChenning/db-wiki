---
title: "V$RESULT_CACHE_DEPENDENCY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2138.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RESULT_CACHE_DEPENDENCY` displays the depends-on relationship between cached results and dependencies.

| Column | Datatype | Description |
| --- | --- | --- |
| `RESULT_ID` | `NUMBER` | Cached result |
| `DEPEND_ID` | `NUMBER` | Dependency object |
| `OBJECT_NO` | `NUMBER` | Dictionary object number of the dependency object |