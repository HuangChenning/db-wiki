---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_USERS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_USERS` lists all users of the database visible to the current user.

This view does not describe the users (see the related views).

Related Views

- `DBA_USERS` describes all users of the database, and contains more columns than `ALL_USERS`.
- `USER_USERS` describes the current user, and contains more columns than `ALL_USERS`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user |
| `USER_ID` | `NUMBER` | `NOT NULL` | ID number of the user |
| `CREATED` | `DATE` | `NOT NULL` | User creation date |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether a given user is common. Possible values:  - `YES` if a user is common - `NO` if a user is local (not common) |
| `ORACLE_MAINTAINED` | `VARCHAR2(1)` |  | Denotes whether the user was created, and is maintained, by Oracle-supplied scripts (such as catalog.sql or catproc.sql). A user for which this column has the value `Y` must not be changed in any way except by running an Oracle-supplied script. |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the user definition was inherited from another container (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `DEFAULT_COLLATION` | `VARCHAR2(100)` |  | Default collation for the user’s schema  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether this user is a common user created by an implicit application (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `ALL_SHARD` | `VARCHAR2(3)` |  | In a sharded database, the value in this column indicates whether the user was created with shard DDL enabled. The possible values are:  - `YES`: The user was created with shard DDL enabled. The user exists on all shards and the shard catalog. - `NO`: The user was created without shard DDL enabled. The user exists only in the database in which the user was created.  In a non-sharded database, the value in this column is always `NO`.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_USERS](DBA_USERS.md) "
- " [USER\_USERS](USER_USERS.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-DE8AF949-9F68-4C0C-9B5A-45401EF3C3D1) for more information about sharded database management