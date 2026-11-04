---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PART_KEY_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.4 ALL\_PART\_KEY\_COLUMNS

`ALL_PART_KEY_COLUMNS` describes the partitioning key columns for the partitioned objects accessible to the current user.

Related Views

- `DBA_PART_KEY_COLUMNS` describes the partitioning key columns for all partitioned objects in the database.
- `USER_PART_KEY_COLUMNS` describes the partitioning key columns for the partitioned objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the partitioned table or index |
| `NAME` | `VARCHAR2(128)` |  | Name of the partitioned table or index |
| `OBJECT_TYPE` | `CHAR(5)` |  | Object type:  - `TABLE` - `INDEX` |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column |
| `COLUMN_POSITION` | `NUMBER` |  | Position of the column within the partitioning key |
| `COLLATED_COLUMN_ID` | `NUMBER` |  | Internal sequence number of the column for which this column provides linguistic ordering |

See Also:

- " [DBA\_PART\_KEY\_COLUMNS](DBA_PART_KEY_COLUMNS.md) "
- " [USER\_PART\_KEY\_COLUMNS](USER_PART_KEY_COLUMNS.md) "