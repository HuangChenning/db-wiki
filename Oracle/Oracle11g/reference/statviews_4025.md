---
title: DBA_HIST_PLAN_OPTION_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4025.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PLAN_OPTION_NAME` displays historical information about SQL plan option names.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier |
| `OPTION_ID` | `NUMBER` | `NOT NULL` | Plan option identifier |
| `OPTION_NAME` | `VARCHAR2(64)` |  | Plan option name. This value also appears in the `SQL_PLAN_OPTIONS` column of the `DBA_HIST_ACTIVE_SESS_HISTORY` view. |