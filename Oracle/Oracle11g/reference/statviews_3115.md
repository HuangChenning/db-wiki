---
title: DBA_COMPARISON_ROW_DIF
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3115.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_COMPARISON_ROW_DIF` displays information about the differing rows in all comparison scans in the database.

Related View

`USER_COMPARISON_ROW_DIF` displays information about the differing rows in the comparison scans owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the comparison |
| `COMPARISON_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the comparison |
| `SCAN_ID` | `NUMBER` | `NOT NULL` | Scan ID for the comparison scan |
| `LOCAL_ROWID` | `ROWID` |  | Local rowid of the differing row |
| `REMOTE_ROWID` | `ROWID` |  | Remote rowid of the differing row |
| `INDEX_VALUE` | `VARCHAR2(4000)` |  | Index column value of the differing row |
| `STATUS` | `VARCHAR2(3)` |  | Status of the differing row: |
| `LAST_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time that this row was last updated |