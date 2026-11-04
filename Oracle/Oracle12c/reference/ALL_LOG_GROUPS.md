---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_LOG_GROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_LOG_GROUPS` describes the log group definitions on the tables accessible to the current user.

Related Views

- `DBA_LOG_GROUPS` describes the log group definitions on all tables in the database.
- `USER_LOG_GROUPS` describes the log group definitions on the tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the log group definition |
| `LOG_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the log group definition |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table on which the log group is defined |
| `LOG_GROUP_TYPE` | `VARCHAR2(28)` |  | Type of the log group:  - `PRIMARY KEY LOGGING` - `UNIQUE KEY LOGGING` - `FOREIGN KEY LOGGING` - `ALL COLUMN LOGGING` - `USER LOG GROUP` |
| `ALWAYS` | `VARCHAR2(11)` |  | `Y` indicates the log group is logged any time a row is updated; `N` indicates the log group is logged any time a member column is updated |
| `GENERATED` | `VARCHAR2(14)` |  | Indicates whether the name of the supplemental log group was system generated (`GENERATED NAME`) or not (`USER NAME`) |

See Also:

- " [DBA\_LOG\_GROUPS](DBA_LOG_GROUPS.md) "
- " [USER\_LOG\_GROUPS](USER_LOG_GROUPS.md) "