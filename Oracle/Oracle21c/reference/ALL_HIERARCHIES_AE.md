---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_HIERARCHIES_AE.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.221 ALL\_HIERARCHIES\_AE

`ALL_HIERARCHIES_AE` describes the hierarchies (across all editions) accessible to the current user.

Related Views

- `DBA_HIERARCHIES_AE` describes all hierarchies (across all editions) in the database.
- `USER_HIERARCHIES_AE` describes the hierarchies (across all editions) owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `DIMENSION_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension used by the hierarchy |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension used by the hierarchy |
| `PARENT_ATTR` | `VARCHAR2` |  | The value of this column is always NULL |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the hierarchy:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |
| `EDITION_NAME` | `VARCHAR2(128)` |  | Name of the application edition where the hierarchy is defined |

Note:

This view is available starting with Oracle Database 21c, Release Update 21.5.

See Also:

- " [DBA\_HIERARCHIES\_AE](DBA_HIERARCHIES_AE.md) "
- " [USER\_HIERARCHIES\_AE](USER_HIERARCHIES_AE.md) "