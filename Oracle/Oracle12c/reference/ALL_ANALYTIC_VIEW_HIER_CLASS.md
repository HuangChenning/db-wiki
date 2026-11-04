---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_ANALYTIC_VIEW_HIER_CLASS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_ANALYTIC_VIEW_HIER_CLASS` describes the classifications of the hierarchies in the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_HIER_CLASS` describes the classifications of the hierarchies in all analytic views in the database.
- `USER_ANALYTIC_VIEW_HIER_CLASS` describes the classifications of the hierarchies in the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the analytic view |
| `DIMENSION_ALIAS` | `VARCHAR2(128)` |  | Alias of the attribute dimension in the analytic view |
| `HIER_ALIAS` | `VARCHAR2(128)` |  | Alias of the hierarchy in the attribute dimension in the analytic view |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the hierarchy |
| `VALUE` | `CLOB` |  | Value of the classification, or `NULL` if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | NLS\_LANGUAGE value associated with the classification, or `NULL` if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the hierarchy |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_ANALYTIC\_VIEW\_HIER\_CLASS](DBA_ANALYTIC_VIEW_HIER_CLASS.md) "
- " [USER\_ANALYTIC\_VIEW\_HIER\_CLASS](USER_ANALYTIC_VIEW_HIER_CLASS.md) "