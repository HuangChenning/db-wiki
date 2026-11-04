---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_ANALYTIC_VIEW_ATTR_CLASS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.18 ALL\_ANALYTIC\_VIEW\_ATTR\_CLASS

`ALL_ANALYTIC_VIEW_ATTR_CLASS` describes the attribute classifications of the analytic views accessible to the current user.

Related Views

- `DBA_ANALYTIC_VIEW_ATTR_CLASS` describes the attribute classifications of all analytic views in the database.
- `USER_ANALYTIC_VIEW_ATTR_CLASS` describes the attribute classifications of the analytic views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the analytic view |
| `ANALYTIC_VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of analytic view |
| `DIMENSION_ALIAS` | `VARCHAR2(128)` |  | Alias of the attribute dimension in the analytic view |
| `HIER_ALIAS` | `VARCHAR2(128)` |  | Alias of the hierarchy specified by an attribute dimension in the analytic view |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute within the analytic view |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Name of analytic view attribute classification |
| `VALUE` | `CLOB` |  | Value of attribute classification |
| `LANGUAGE` | `VARCHAR2(64)` |  | Language of attribute classification |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order number of the attribute classification |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_ANALYTIC\_VIEW\_ATTR\_CLASS](DBA_ANALYTIC_VIEW_ATTR_CLASS.md) "
- " [USER\_ANALYTIC\_VIEW\_ATTR\_CLASS](USER_ANALYTIC_VIEW_ATTR_CLASS.md) "