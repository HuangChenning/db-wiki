---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_COL_PRIVS.html
tags:
  - oracle
  - 12c
  - reference
---

- Column object grants for which the current user is the object owner, grantor, or grantee
- Column object grants for which an enabled role or `PUBLIC` is the grantee

Related Views

- `DBA_COL_PRIVS` describes all column object grants in the database.
- `USER_COL_PRIVS` describes the column object grants for which the current user is the object owner, grantor, or grantee.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `GRANTOR` | `VARCHAR2(128)` |  | Name of the user who performed the grant |
| `GRANTEE` | `VARCHAR2(128)` |  | Name of the user or role to whom access was granted |
| `TABLE_SCHEMA` | `VARCHAR2(128)` |  | Schema of the object |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the column |
| `PRIVILEGE` | `VARCHAR2(40)` |  | Privilege on the column |
| `GRANTABLE` | `VARCHAR2(3)` |  | Indicates whether the privilege was granted with the `GRANT OPTION` (`YES`) or not (`NO`) |
| `COMMON` | `VARCHAR2(3)` |  | Indicates how the grant was made. Possible values:  - `YES` if the privilege was granted commonly (`CONTAINER=ALL` was used) - `NO` if the privilege was granted locally (`CONTAINER=ALL` was not used) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the privilege grant was inherited from another container (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_COL\_PRIVS](DBA_COL_PRIVS.md) "
- " [USER\_COL\_PRIVS](USER_COL_PRIVS.md) "