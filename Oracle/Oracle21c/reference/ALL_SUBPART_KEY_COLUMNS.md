---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SUBPART_KEY_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.97 ALL\_SUBPART\_KEY\_COLUMNS

`ALL_SUBPART_KEY_COLUMNS` displays subpartitioning key columns for composite-partitioned tables (and local indexes on composite-partitioned tables) accessible to the current user.

Related Views

- `DBA_SUBPART_KEY_COLUMNS` displays this information for all subpartitions in the database.
- `USER_SUBPART_KEY_COLUMNS` displays this information for subpartitions of all partitioned objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the partitioned table or index |
| `NAME` | `VARCHAR2(128)` |  | Name of the partitioned table or index |
| `OBJECT_TYPE` | `CHAR(5)` |  | Object type:  - `TABLE` - `INDEX` |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column name |
| `COLUMN_POSITION` | `NUMBER` |  | Position of the column within the subpartitioning key |
| `COLLATED_COLUMN_ID` | `NUMBER` |  | Internal sequence number of the column for which this column provides linguistic ordering |

See Also:

- " [DBA\_SUBPART\_KEY\_COLUMNS](DBA_SUBPART_KEY_COLUMNS.md) "
- " [USER\_SUBPART\_KEY\_COLUMNS](USER_SUBPART_KEY_COLUMNS.md) "