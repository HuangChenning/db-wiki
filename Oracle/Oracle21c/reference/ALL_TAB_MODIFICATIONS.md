---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_MODIFICATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.112 ALL\_TAB\_MODIFICATIONS

`ALL_TAB_MODIFICATIONS` describes tables accessible to the current user that have been modified since the last time statistics were gathered on the tables.

Related Views

- `DBA_TAB_MODIFICATIONS` describes such information for all tables in the database.
- `USER_TAB_MODIFICATIONS` describes such information for tables owned by the current user. This view does not display the `TABLE_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` |  | Owner of the modified table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the modified table |
| `PARTITION_NAME` | `VARCHAR2(128)` |  | Name of the modified partition |
| `SUBPARTITION_NAME` | `VARCHAR2(128)` |  | Name of the modified subpartition |
| `INSERTS` | `NUMBER` |  | Approximate number of inserts since the last time statistics were gathered |
| `UPDATES` | `NUMBER` |  | Approximate number of updates since the last time statistics were gathered |
| `DELETES` | `NUMBER` |  | Approximate number of deletes since the last time statistics were gathered |
| `TIMESTAMP` | `DATE` |  | Indicates the last time the table was modified |
| `TRUNCATED` | `VARCHAR2(3)` |  | Indicates whether the table has been truncated since the last analyze (`YES`) or not (`NO`) |
| `DROP_SEGMENTS` | `NUMBER` |  | Number of partition and subpartition segments dropped since the last analyze |

See Also:

- " [DBA\_TAB\_MODIFICATIONS](DBA_TAB_MODIFICATIONS.md) "
- " [USER\_TAB\_MODIFICATIONS](USER_TAB_MODIFICATIONS.md) "