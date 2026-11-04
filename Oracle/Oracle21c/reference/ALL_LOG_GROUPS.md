---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_LOG_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.265 ALL\_LOG\_GROUPS

`ALL_LOG_GROUPS` describes the log group definitions on the tables accessible to the current user.

Related Views

- `DBA_LOG_GROUPS` describes the log group definitions on all tables in the database.
- `USER_LOG_GROUPS` describes the log group definitions on the tables owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the log group definition |
| `LOG_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the log group definition |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table on which the log group is defined |
| `LOG_GROUP_TYPE` | `VARCHAR2(28)` |  | Type of the log group:  - `ALL` `COLUMN` `LOGGING` - `FOREIGN` `KEY` `LOGGING` - `PRIMARY` `KEY` `LOGGING` - `UNIQUE` `KEY` `LOGGING` - `USER` `LOG` `GROUP` |
| `ALWAYS` | `VARCHAR2(11)` |  | Indicates whether the log group is an unconditional log group (`ALWAYS`) or a conditional log group (`CONDITIONAL`) |
| `GENERATED` | `VARCHAR2(14)` |  | Indicates whether the name of the supplemental log group was system generated (`GENERATED` `NAME`) or not (`USER` `NAME`) |

See Also:

- " [DBA\_LOG\_GROUPS](DBA_LOG_GROUPS.md) "
- " [USER\_LOG\_GROUPS](USER_LOG_GROUPS.md) "