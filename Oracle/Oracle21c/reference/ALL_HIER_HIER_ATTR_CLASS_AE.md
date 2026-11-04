---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_HIER_ATTR_CLASS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.211 ALL\_HIER\_HIER\_ATTR\_CLASS\_AE

`ALL_HIER_HIER_ATTR_CLASS_AE` describes the classifications of the hierarchical attributes of the hierarchies (across all editions) accessible to the current user.

Related Views

- `DBA_HIER_HIER_ATTR_CLASS_AE` describes the classifications of the hierarchical attributes of all hierarchies (across all editions) in the database.
- `USER_HIER_HIER_ATTR_CLASS_AE` describes the classifications of the hierarchical attributes of the hierarchies (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `HIER_ATTR_NAME` | `VARCHAR2(128)` |  | Name of the hierarchical attribute |
| `CLASSIFICATION` | `VARCHAR2(128)` |  | Classification associated with the hierarchical attribute |
| `VALUE` | `CLOB` |  | Value associated with the classification or NULL if not specified |
| `LANGUAGE` | `VARCHAR2(64)` |  | `NLS_LANGUAGE` value associated with the classification or NULL if not specified |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of classifications associated with the hierarchical attribute |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the hierarchy is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_HIER\_HIER\_ATTR\_CLASS\_AE](DBA_HIER_HIER_ATTR_CLASS_AE.md) "
- " [USER\_HIER\_HIER\_ATTR\_CLASS\_AE](USER_HIER_HIER_ATTR_CLASS_AE.md) "