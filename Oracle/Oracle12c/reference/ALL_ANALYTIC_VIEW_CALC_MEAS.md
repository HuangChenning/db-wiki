---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ANALYTIC_VIEW_CALC_MEAS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_ANALYTIC_VIEW_CALC_MEAS` describes the calculated measures in the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_CALC_MEAS` describes the calculated measures in all analytic views in the database.
- `USER_ANALYTIC_VIEW_CALC_MEAS` describes the calculated measures in the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `MEASURE_NAME` | `VARCHAR2(128)` |  | Name of the analytic view calculated measure |
| `MEAS_EXPRESSION` | `CLOB` |  | Text of the expression for the measure |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the calculated measure in the list of the measures in the analytic view |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_ANALYTIC\_VIEW\_CALC\_MEAS](DBA_ANALYTIC_VIEW_CALC_MEAS.md) "
- " [USER\_ANALYTIC\_VIEW\_CALC\_MEAS](USER_ANALYTIC_VIEW_CALC_MEAS.md) "