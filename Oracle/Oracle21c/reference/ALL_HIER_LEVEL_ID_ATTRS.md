---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_LEVEL_ID_ATTRS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.216 ALL\_HIER\_LEVEL\_ID\_ATTRS

`ALL_HIER_LEVEL_ID_ATTRS` describes the attributes that uniquely identify members of the levels of the hierarchies accessible to the current user.

Related Views

- `DBA_HIER_LEVEL_ID_ATTRS` describes the attributes that uniquely identify members of the levels of all hierarchies in the database.
- `USER_HIER_LEVEL_ID_ATTRS` describes the attributes that uniquely identify members of the levels of the hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `LEVEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of hierarchy level |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the unique identifier attribute |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the level in the list of unique identifier attributes for the level |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_HIER\_LEVEL\_ID\_ATTRS](DBA_HIER_LEVEL_ID_ATTRS.md) "
- " [USER\_HIER\_LEVEL\_ID\_ATTRS](USER_HIER_LEVEL_ID_ATTRS.md) "