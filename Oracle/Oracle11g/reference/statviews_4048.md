---
title: DBA_HIST_SQL_SUMMARY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4048.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SQL_SUMMARY` displays historical SQL summary information.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TOTAL_SQL` | `NUMBER` | `NOT NULL` | Total number of SQLs |
| `TOTAL_SQL_MEM` | `NUMBER` | `NOT NULL` | Total sharable memory in bytes for SQLs |
| `SINGLE_USE_SQL` | `NUMBER` | `NOT NULL` | Total number of single execution SQLs |
| `SINGLE_USE_SQL_MEM` | `NUMBER` | `NOT NULL` | Total sharable memory in bytes for single execution SQLs |