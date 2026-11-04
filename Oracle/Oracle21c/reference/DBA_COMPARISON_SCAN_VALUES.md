---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_COMPARISON_SCAN_VALUES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.240 DBA\_COMPARISON\_SCAN\_VALUES

`DBA_COMPARISON_SCAN_VALUES` displays information about the values for all comparison scans in the database.

Related View

`USER_COMPARISON_SCAN_VALUES` displays information about the values for the comparison scans owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the comparison scan |
| `COMPARISON_SCAN` | `VARCHAR2(128)` | `NOT NULL` | Name of the comparison scan |
| `SCAN_ID` | `NUMBER` | `NOT NULL` | Scan ID |
| `COLUMN_POSITION` | `NUMBER` | `NOT NULL` | Column position, as in `DBA_COMPARISON_COLUMNS` |
| `MIN_VALUE` | `VARCHAR2(4000)` |  | Minimum value of the scan |
| `MAX_VALUE` | `VARCHAR2(4000)` |  | Maximum value of the scan |
| `LAST_UPDATE_TIME` | `TIMESTAMP(6)` |  | Time that this row was last updated |

See Also:

" [USER\_COMPARISON\_SCAN\_VALUES](USER_COMPARISON_SCAN_VALUES.md) "