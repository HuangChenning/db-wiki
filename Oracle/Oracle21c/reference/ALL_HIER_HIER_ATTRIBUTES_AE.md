---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_HIER_ATTRIBUTES_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.213 ALL\_HIER\_HIER\_ATTRIBUTES\_AE

`ALL_HIER_HIER_ATTRIBUTES_AE` describes the hierarchical attributes of the hierarchies (across all editions) accessible to the current user.

Related Views

- `DBA_HIER_HIER_ATTRIBUTES_AE` describes the hierarchical attributes of all hierarchies (across all editions) in the database.
- `USER_HIER_HIER_ATTRIBUTES_AE` describes the hierarchical attributes of the hierarchies (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `HIER_ATTR_NAME` | `VARCHAR2(128)` |  | Name of the hierarchical attribute |
| `EXPRESSION` | `CLOB` |  | The expression defining the hierarchical attribute value |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the hierarchical attribute in the list of hierarchical attributes |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the hierarchy is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.