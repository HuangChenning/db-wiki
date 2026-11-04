---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_MVREF_STATS_PARAMS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_MVREF_STATS_PARAMS` displays the refresh statistics properties associated with each materialized view. These properties can be modified with the `DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS` procedure.

Related View

`USER_MVREF_STATS_PARAMS` displays the refresh statistics properties associated with each materialized view accessible to the current user. These properties can be modified with the `DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `MV_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MV_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `COLLECTION_LEVEL` | `VARCHAR2(8)` |  | The collection level for the materialized view |
| `RETENTION_PERIOD` | `NUMBER` |  | The retention period for the materialize view |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [USER\_MVREF\_STATS\_PARAMS](USER_MVREF_STATS_PARAMS.md) "