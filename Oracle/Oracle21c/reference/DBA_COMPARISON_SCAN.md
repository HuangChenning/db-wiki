---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_COMPARISON_SCAN.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.239 DBA\_COMPARISON\_SCAN

`DBA_COMPARISON_SCAN` displays information about all comparison scans in the database.

Related View

`USER_COMPARISON_SCAN` displays information about the comparison scans owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the comparison scan |
| `COMPARISON_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the comparison scan |
| `SCAN_ID` | `NUMBER` | `NOT NULL` | Scan ID |
| `PARENT_SCAN_ID` | `NUMBER` |  | Scan ID of the immediate parent scan |
| `ROOT_SCAN_ID` | `NUMBER` |  | Scan ID of the root (top-most) parent |
| `STATUS` | `VARCHAR2(16)` |  | Status of the scan:  - `SUC` - `BUCKET DIF` - `FINAL BUCKET DIF` - `ROW DIF` |
| `CURRENT_DIF_COUNT` | `NUMBER` |  | Current cumulative (including children) diff count of the scan |
| `INITIAL_DIF_COUNT` | `NUMBER` |  | Initial cumulative (including children) diff count of the scan |
| `COUNT_ROWS` | `NUMBER` |  | Number of rows in the scan |
| `SCAN_NULLS` | `VARCHAR2(1)` |  | Indicates whether NULLs are part of this scan (`Y`) or not (`N`) |
| `LAST_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time that this row was last updated |

See Also:

" [USER\_COMPARISON\_SCAN](USER_COMPARISON_SCAN.md) "