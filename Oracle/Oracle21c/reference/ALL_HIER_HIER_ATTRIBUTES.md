---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_HIER_ATTRIBUTES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.212 ALL\_HIER\_HIER\_ATTRIBUTES

`ALL_HIER_HIER_ATTRIBUTES` describes the hierarchical attributes of the hierarchies accessible to the current user.

Related Views

- `DBA_HIER_HIER_ATTRIBUTES` describes the hierarchical attributes of all hierarchies in the database.
- `USER_HIER_HIER_ATTRIBUTES` describes the hierarchical attributes of the hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `HIER_ATTR_NAME` | `VARCHAR2(128)` |  | Name of the hierarchical attribute |
| `EXPRESSION` | `CLOB` |  | The expression defining the hierarchical attribute value |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the hierarchical attribute in the list of hierarchical attributes |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_HIER\_HIER\_ATTRIBUTES](DBA_HIER_HIER_ATTRIBUTES.md) "
- " [USER\_HIER\_HIER\_ATTRIBUTES](USER_HIER_HIER_ATTRIBUTES.md) "