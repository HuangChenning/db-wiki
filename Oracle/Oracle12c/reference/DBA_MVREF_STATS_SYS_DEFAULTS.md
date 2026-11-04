---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_MVREF_STATS_SYS_DEFAULTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_MVREF_STATS_SYS_DEFAULTS` displays the system-wide defaults for the refresh history statistics properties for materialized views. These values can be altered with the `SET_SYSTEM_DEFAULTS` procedure by a database administrator.

Related View

This view contains exactly two rows corresponding to the collection-level and retention-period properties; their initial values are `TYPICAL` and `31` respectively.

`USER_MVREF_STATS_SYS_DEFAULTS` displays the system-wide defaults for the refresh history statistics properties for materialized views accessible to the current user. These values can be altered with the `SET_SYSTEM_DEFAULTS` procedure by a database administrator.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `CHAR(16)` |  | Value of the `parameter_name` parameter:  - `COLLECTION_LEVEL` - `RETENTION_PERIOD` |
| `VALUE` | `VARCHAR2(40)` |  | The system-wide default value for the parameter |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [USER\_MVREF\_STATS\_SYS\_DEFAULTS](USER_MVREF_STATS_SYS_DEFAULTS.md) "