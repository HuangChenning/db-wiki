---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TAB_COL_STAT_MODELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.104 ALL\_TAB\_COL\_STAT\_MODELS

`ALL_TAB_COL_STAT_MODELS` describes real-time statistics models for all tables accessible to the current user.

Real-time statistics models use machine learning algorithms to predict the number of distinct values (NDV) for table columns.

Related Views

- `DBA_TAB_COL_STAT_MODELS` describes real-time statistics models for all tables in the database.
- `USER_TAB_COL_STAT_MODELS` describes real-time statistics models for all tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table column to which the model applies |
| `STATS_TYPE` | `VARCHAR2(7)` |  | Statistics type  The value of this column is always `NDV`. |
| `MODEL_NAME` | `VARCHAR2(200)` | `NOT NULL` | Name of the model |
| `STATUS` | `VARCHAR2(8)` |  | Status of the model (`ENABLED` or `DISABLED`) |
| `CREATED` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the model was created |
| `LAST_USED` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the model was most recently used |

Note:

This view is available starting with Oracle Database 21c.

See Also:

- " [DBA\_TAB\_COL\_STAT\_MODELS](DBA_TAB_COL_STAT_MODELS.md) "
- " [USER\_TAB\_COL\_STAT\_MODELS](USER_TAB_COL_STAT_MODELS.md) "