---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USER_USERS.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the user |
| `USER_ID` | `NUMBER` | `NOT NULL` | ID number of the user |
| `ACCOUNT_STATUS` | `VARCHAR2(32)` | `NOT NULL` | Account status:  - `OPEN` 	The account is open. - `EXPIRED` 	The password for the account is expired, either because the `PASSWORD_LIFE_TIME` limit was reached or because the password was expired by the `ALTER` `USER`... `PASSWORD` `EXPIRE` command. The user can log in with the expired password, then change the password. - `EXPIRED(GRACE)` 	The password for the account is expired because the `PASSWORD_LIFE_TIME` limit was reached, but the password change grace period (`PASSWORD_GRACE_TIME`) has not yet elapsed. The user can log in with the expired password, but will receive an `ORA-28002` warning as a reminder that the password must soon be changed. If the `PASSWORD_GRACE_TIME` elapses, the user can log in with the expired password, then change the password. - `LOCKED` 	The account is locked, either by the `ALTER` `USER`... `ACCOUNT` `LOCK` command, or because the number of consecutive failed login attempts exceeded the `FAILED_LOGIN_ATTEMPTS` limit and the value of `PASSWORD_LOCK_TIME` is `UNLIMITED`. The account can be unlocked by the `ALTER` `USER`... `ACCOUNT` `UNLOCK` command. - `LOCKED(TIMED)` 	The account is locked because the number of consecutive failed login attempts exceeded the `FAILED_LOGIN_ATTEMPTS` limit and the `PASSWORD_LOCK_TIME` has not yet elapsed. The account can be unlocked either by the `ALTER` `USER`... `ACCOUNT` `UNLOCK` command or by waiting until the `PASSWORD_LOCK_TIME` has elapsed. - `EXPIRED & LOCKED` 	The password for the account is expired, as described for the `EXPIRED` account status, and the account is locked as described for the `LOCKED` account status. The account can first be unlocked as described for the `LOCKED` account status, then the password can be changed as described for the `EXPIRED` account status. - `EXPIRED(GRACE) & LOCKED` 	The password for the account is expired, as described for the `EXPIRED(GRACE)` account status, and the account is locked as described for the `LOCKED` account status. The account can first be unlocked as described for the `LOCKED` account status, then the password can be changed as described for the `EXPIRED(GRACE)` account status. - `EXPIRED & LOCKED(TIMED)` 	The password for the account is expired, as described for the `EXPIRED` account status, and the account is locked as described for the `LOCKED(TIMED)` account status. The account can first be unlocked as described for the `LOCKED(TIMED)` account status, then the password can be changed as described for the `EXPIRED` account status. - `EXPIRED(GRACE) & LOCKED(TIMED)` 	The password for the account is expired, as described for the `EXPIRED(GRACE)` account status, and the account is locked as described for the `LOCKED(TIMED)` account status. The account can first be unlocked as described for the `LOCKED(TIMED)` account status, then the password can be changed as described for the `EXPIRED(GRACE)` account status. |
| `LOCK_DATE` | `DATE` |  | Date the account was locked if account status was `LOCKED` |
| `EXPIRY_DATE` | `DATE` |  | Date of expiration of the account |
| `DEFAULT_TABLESPACE` | `VARCHAR2(30)` | `NOT NULL` | Default tablespace for data |
| `TEMPORARY_TABLESPACE` | `VARCHAR2(30)` | `NOT NULL` | Name of the default tablespace for temporary tables or the name of a tablespace group |
| `LOCAL_TEMP_TABLESPACE` | `VARCHAR2(30)` |  | Default local temporary tablespace for the user  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CREATED` | `DATE` | `NOT NULL` | User creation date |
| `INITIAL_RSRC_CONSUMER_GROUP` | `VARCHAR2(128)` |  | Initial resource consumer group for the user |
| `EXTERNAL_NAME` | `VARCHAR2(4000)` |  | User external name |
| `PROXY_ONLY_CONNECT` | `VARCHAR2(1)` |  | Indicates whether a user can connect directly (`N`) or whether the account can only be proxied (`Y`) by users who have proxy privileges for this account (that is, by users who have been granted the "connect through" privilege for this account).  For more information about creating proxy user accounts and authorizing users to connect through them, see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG99851). |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether a given user is common. Possible values  - `YES` if a user is common - `NO` if a user is local (not common) |
| `ORACLE_MAINTAINED` | `VARCHAR2(1)` |  | Denotes whether the user was created, and is maintained, by Oracle-supplied scripts (such as catalog.sql or catproc.sql). A user for which this column has the value `Y` must not be changed in any way except by running an Oracle-supplied script. |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the user definition was inherited from another container (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `DEFAULT_COLLATION` | `VARCHAR2(100)` |  | Default collation for the user’s schema  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `IMPLICIT` | `VARCHAR2(3)` |  | Indicates whether this user is a common user created by an implicit application (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `ALL_SHARD` | `VARCHAR2(3)` |  | In a sharded database, the value in this column indicates whether the user was created with shard DDL enabled. The possible values are:  - `YES`: The user was created with shard DDL enabled. The user exists on all shards and the shard catalog. - `NO`: The user was created without shard DDL enabled. The user exists only in the database in which the user was created.  In a non-sharded database, the value in this column is always `NO`.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_USERS](DBA_USERS.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN-GUID-DE8AF949-9F68-4C0C-9B5A-45401EF3C3D1) for more information about sharded database management