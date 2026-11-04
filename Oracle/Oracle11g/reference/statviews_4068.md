---
title: DBA_HIST_TOPLEVELCALL_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4068.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_TOPLEVELCALL_NAME` displays the mapping between Oracle top level calls and names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `TOP_LEVEL_CALL#` | `NUMBER` | `NOT NULL` | Oracle top level call number |
| `TOP_LEVEL_CALL_NAME` | `VARCHAR2(64)` |  | Oracle top level call name |