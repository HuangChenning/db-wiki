---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIER_JOIN_PATHS_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.215 ALL\_HIER\_JOIN\_PATHS\_AE

`ALL_HIER_JOIN_PATHS_AE` describes the join paths for the hierarchies (across all editions) accessible to the current user.

Related Views

- `DBA_HIER_JOIN_PATHS_AE` describes the join paths for all hierarchies (across all editions) in the database.
- `USER_HIER_JOIN_PATHS_AE` describes the join paths for the hierarchies (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `JOIN_PATH_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the join path |
| `ORDER_NUM` | `NUMBER` | `NOT NULL` | Order of the classification in the list of join paths associated with the hierarchy |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the hierarchy is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_HIER\_JOIN\_PATHS\_AE](DBA_HIER_JOIN_PATHS_AE.md) "
- " [USER\_HIER\_JOIN\_PATHS\_AE](USER_HIER_JOIN_PATHS_AE.md) "