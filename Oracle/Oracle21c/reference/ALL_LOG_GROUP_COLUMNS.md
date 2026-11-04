---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_LOG_GROUP_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.264 ALL\_LOG\_GROUP\_COLUMNS

`ALL_LOG_GROUP_COLUMNS` describes columns that are accessible to the current user and that are specified in log groups.

Related Views

- `DBA_LOG_GROUP_COLUMNS` describes all columns in the database that are specified in log groups.
- `USER_LOG_GROUP_COLUMNS` describes columns that are owned by the current user and that are specified in log groups.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the log group definition |
| `LOG_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the log group definition |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table in which the log group is defined |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the column or attribute of the object type column specified in the log group definition |
| `POSITION` | `NUMBER` |  | Original position of the column or attribute in the definition of the object |
| `LOGGING_PROPERTY` | `VARCHAR2(6)` |  | Indicates whether the column or attribute would be supplementally logged (`LOG`) or not (`NO LOG`) |

See Also:

- " [DBA\_LOG\_GROUP\_COLUMNS](DBA_LOG_GROUP_COLUMNS.md) "
- " [USER\_LOG\_GROUP\_COLUMNS](USER_LOG_GROUP_COLUMNS.md) "