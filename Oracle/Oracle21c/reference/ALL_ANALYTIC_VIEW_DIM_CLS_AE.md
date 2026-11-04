---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ANALYTIC_VIEW_DIM_CLS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.36 ALL\_ANALYTIC\_VIEW\_DIM\_CLS\_AE

`ALL_ANALYTIC_VIEW_DIM_CLS_AE` describes the classifications of the attribute dimensions in the analytic views (across all editions) accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_DIM_CLS_AE` describes the classifications of the attribute dimensions in all analytic views (across all editions) in the database.
- `USER_ANALYTIC_VIEW_DIM_CLS_AE` describes the classifications of the attribute dimensions in the analytic views (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `DIMENSION_ALIAS` | `VARCHAR2(128)` |  | Alias of the attribute dimension in the analytic view |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the attribute dimension |
| `VALUE` | `CLOB` |  | Value of the classification or NULL if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | `NLS_LANGUAGE` value associated with the classification or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the attribute dimension |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the analytic view is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_ANALYTIC\_VIEW\_DIM\_CLS\_AE](DBA_ANALYTIC_VIEW_DIM_CLS_AE.md) "
- " [USER\_ANALYTIC\_VIEW\_DIM\_CLS\_AE](USER_ANALYTIC_VIEW_DIM_CLS_AE.md) "