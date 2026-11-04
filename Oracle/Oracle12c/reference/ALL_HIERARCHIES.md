---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_HIERARCHIES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_HIERARCHIES` describes the hierarchies accessible to the current user.

Related Views

- `DBA_HIERARCHIES` describes all hierarchies in the database.
- `USER_HIERARCHIES` describes the hierarchies owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the hierarchy |
| `HIER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the hierarchy |
| `DIMENSION_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the attribute dimension used by the hierarchy |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute dimension used by the hierarchy |
| `PARENT_ATTR` | `VARCHAR2` |  | Always `NULL` |
| `COMPILE_STATE` | `VARCHAR2(7)` |  | Compile status of the hierarchy:  - `VALID` - `INVALID` |
| `ORIGIN_CON_ID` | `NUMBER` |  | The ID of the container where the data originates. Possible values include:  - `0`: This value is used for rows in non-CDBs. This value is not used for CDBs. - n: This value is used for rows containing data that originate in the container with container ID n (n = 1 if the row originates in root). |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBA\_HIERARCHIES](DBA_HIERARCHIES.md) "
- " [USER\_HIERARCHIES](USER_HIERARCHIES.md) "