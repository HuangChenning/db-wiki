---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_HIER_HIER_ATTRIBUTES.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_HIER\_HIER\_ATTRIBUTES](DBA_HIER_HIER_ATTRIBUTES.md) "
- " [USER\_HIER\_HIER\_ATTRIBUTES](USER_HIER_HIER_ATTRIBUTES.md) "