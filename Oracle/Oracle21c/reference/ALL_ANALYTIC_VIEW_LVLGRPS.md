---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ANALYTIC_VIEW_LVLGRPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.55 ALL\_ANALYTIC\_VIEW\_LVLGRPS

`ALL_ANALYTIC_VIEW_LVLGRPS` describes the analytic view measure and level groups of the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_LVLGRPS` describes the analytic view measure and level groups of all analytic views in the database.
- `USER_ANALYTIC_VIEW_LVLGRPS` describes the analytic view measure and level groups of the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` |  | Name of the analytic view |
| `CACHE_TYPE` | `VARCHAR2(128)` |  | Type of the materialized view; one of the following: - `DYNAMIC` - `MATERIALIZED` (the default value) |
| `DIMENSION_ALIAS` | `VARCHAR2(128)` |  | Alias of the attribute dimension in the group |
| `HIER_ALIAS` | `VARCHAR2(128)` |  | Alias of the hierarchy associated with the attribute dimension in the group |
| `LEVEL_NAME` | `VARCHAR2(128)` |  | Name of the level in the hierarchy in the group |
| `MEASURE_NAME` | `VARCHAR2(128)` |  | Names of the measures in the group |
| `MAT_TABLE_OWNER` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | If the schema for an aggregation table is specified for the analytic view, then the schema owner; otherwise NULL |
| `MAT_TABLE_NAME` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | If an aggregation table is specified for an analytic view, then the name of the materialized table; otherwise NULL |
| `AV_LVLGRP_ORDER` | `NUMBER` |  | Order of the groups in the analytic view |
| `LEVEL_MEAS_ORDER` | `NUMBER` |  | Order of the levels and measures in the group |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

- " [DBA\_ANALYTIC\_VIEW\_LVLGRPS](DBA_ANALYTIC_VIEW_LVLGRPS.md) "
- " [USER\_ANALYTIC\_VIEW\_LVLGRPS](USER_ANALYTIC_VIEW_LVLGRPS.md) "