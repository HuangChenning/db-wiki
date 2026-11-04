---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_MVREF_STATS_PARAMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.201 DBA\_MVREF\_STATS\_PARAMS

`DBA_MVREF_STATS_PARAMS` displays the refresh statistics properties associated with each materialized view. These properties can be modified with the `DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS` procedure.

Related View

`USER_MVREF_STATS_PARAMS` displays the refresh statistics properties associated with each materialized view accessible to the current user. These properties can be modified with the `DBMS_MVIEW_STATS.SET_MVREF_STATS_PARAMS` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `MV_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MV_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `COLLECTION_LEVEL` | `VARCHAR2(8)` |  | The collection level for the materialized view |
| `RETENTION_PERIOD` | `NUMBER` |  | The retention period for the materialize view |

See Also:

" [USER\_MVREF\_STATS\_PARAMS](USER_MVREF_STATS_PARAMS.md) "