---
title: "V$FIXED_VIEW_DEFINITION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1143.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FIXED_VIEW_DEFINITION` contains the definitions of all the fixed views (views beginning with `V$`). Use this table with caution. Oracle tries to keep the behavior of fixed views the same from release to release, but the definitions of the fixed views can change without notice. Use these definitions to optimize your queries by using indexed columns of the dynamic performance tables.

| Column | Datatype | Description |
| --- | --- | --- |
| `VIEW_NAME` | `VARCHAR2(30)` | Name of the fixed view |
| `VIEW_DEFINITION` | `VARCHAR2(4000)` | Definition of the fixed view |