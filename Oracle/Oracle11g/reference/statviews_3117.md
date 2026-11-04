---
title: DBA_COMPARISON_SCAN_VALUES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3117.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_COMPARISON_SCAN_VALUES` displays information about the values for all comparison scans in the database.

Related View

`USER_COMPARISON_SCAN_VALUES` displays information about the values for the comparison scans owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the comparison scan |
| `COMPARISON_SCAN` | `VARCHAR2(30)` | `NOT NULL` | Name of the comparison scan |
| `SCAN_ID` | `NUMBER` | `NOT NULL` | Scan ID |
| `COLUMN_POSITION` | `NUMBER` | `NOT NULL` | Column position, as in `DBA_COMPARISON_COLUMNS` |
| `MIN_VALUE` | `VARCHAR2(4000)` |  | Minimum value of the scan |
| `MAX_VALUE` | `VARCHAR2(4000)` |  | Maximum value of the scan |
| `LAST_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time that this row was last updated |