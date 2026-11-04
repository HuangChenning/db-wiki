---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_LEVELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.218 ALL\_HIER\_LEVELS

`ALL_HIER_LEVELS` describes the levels of the hierarchies accessible to the current user.

Related Views

- `DBA_HIER_LEVELS` describes the levels of all hierarchies in the database.
- `USER_HIER_LEVELS` describes the levels of the hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `LEVEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of hierarchy level |
| `ORDER_NUM` | `NUMBER` | ` NOT NULL` | Order of the level in the list of hierarchy levels |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

See Also:

- " [DBA\_HIER\_LEVELS](DBA_HIER_LEVELS.md) "
- " [USER\_HIER\_LEVELS](USER_HIER_LEVELS.md) "