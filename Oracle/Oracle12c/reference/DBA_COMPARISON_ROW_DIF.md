---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_COMPARISON_ROW_DIF.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_COMPARISON_ROW_DIF` displays information about the differing rows in all comparison scans in the database.

Related View

`USER_COMPARISON_ROW_DIF` displays information about the differing rows in the comparison scans owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the comparison |
| `COMPARISON_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the comparison |
| `SCAN_ID` | `NUMBER` | `NOT NULL` | Scan ID for the comparison scan |
| `LOCAL_ROWID` | `ROWID` |  | Local rowid of the differing row |
| `REMOTE_ROWID` | `ROWID` |  | Remote rowid of the differing row |
| `INDEX_VALUE` | `VARCHAR2(4000)` |  | Index column value of the differing row |
| `STATUS` | `VARCHAR2(3)` |  | Status of the differing row:  - `SUC` - `DIF` |
| `LAST_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time that this row was last updated |

See Also:

" [USER\_COMPARISON\_ROW\_DIF](USER_COMPARISON_ROW_DIF.md) "