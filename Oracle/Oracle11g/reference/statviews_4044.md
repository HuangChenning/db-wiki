---
title: DBA_HIST_SNAP_ERROR
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4044.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SNAP_ERROR` displays information about the snapshot error information in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table in which the error occurred |
| `ERROR_NUMBER` | `NUMBER` | `NOT NULL` | Error number for the error encountered |