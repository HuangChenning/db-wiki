---
title: DBA_HIST_PLAN_OPERATION_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4024.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PLAN_OPERATION_NAME` displays historical information about SQL plan operation names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier |
| `OPERATION_ID` | `NUMBER` | `NOT NULL` | Plan operation identifier |
| `OPERATION_NAME` | `VARCHAR2(64)` |  | Plan operation name. This value also appears in the `SQL_PLAN_OPERATION` column of the `DBA_HIST_ACTIVE_SESS_HISTORY` view. |