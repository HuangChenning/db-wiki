---
title: DBA_HIST_IOSTAT_FUNCTION_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3235.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_IOSTAT_FUNCTION_NAME` displays historical I/O statistics by function names. This view contains snapshots of `V$IOSTAT_FUNCTION`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `FUNCTION_ID` | `NUMBER` | `NOT NULL` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Function name |