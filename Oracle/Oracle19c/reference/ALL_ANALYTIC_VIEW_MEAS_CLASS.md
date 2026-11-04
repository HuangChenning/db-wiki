---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_ANALYTIC_VIEW_MEAS_CLASS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.46 ALL\_ANALYTIC\_VIEW\_MEAS\_CLASS

`ALL_ANALYTIC_VIEW_MEAS_CLASS` describes the classifications of the measures of the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_MEAS_CLASS` describes the classifications of the measures of all analytic views in the database.
- `USER_ANALYTIC_VIEW_MEAS_CLASS` describes the classifications of the measures of the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `MEASURE_NAME` | `VARCHAR2(128)` |  | Name of the measure associated with the classification |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the measure of the analytic view |
| `VALUE` | `CLOB` |  | Value of the classification, or NULL if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | `NLS_LANGUAGE` value associated with the classification, or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the measure |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ANALYTIC\_VIEW\_MEAS\_CLASS](DBA_ANALYTIC_VIEW_MEAS_CLASS.md) "
- " [USER\_ANALYTIC\_VIEW\_MEAS\_CLASS](USER_ANALYTIC_VIEW_MEAS_CLASS.md) "