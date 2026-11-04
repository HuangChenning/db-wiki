---
title: DBA_USERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5081.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_USERS` describes all users of the database.

Related View

`USER_USERS` describes the current user. This view does not display the `PASSWORD`, `PROFILE`, `PASSWORD_VERSIONS`, `EDITIONS_ENABLED`, or `AUTHENTICATION_TYPE` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the user |
| `USER_ID` | `NUMBER` | `NOT NULL` | ID number of the user |
| `PASSWORD` | `VARCHAR2(30)` |  | This column is deprecated in favor of the `AUTHENTICATION_TYPE` column |
| `ACCOUNT_STATUS` | `VARCHAR2(32)` | `NOT NULL` | Account status: - `OPEN` - `EXPIRED` - `EXPIRED(GRACE)` - `LOCKED(TIMED)` - `LOCKED` - `EXPIRED & LOCKED(TIMED)` - `EXPIRED(GRACE) & LOCKED(TIMED)` - `EXPIRED & LOCKED` - `EXPIRED(GRACE) & LOCKED` |
| `LOCK_DATE` | `DATE` |  | Date the account was locked if account status was `LOCKED` |
| `EXPIRY_DATE` | `DATE` |  | Date of expiration of the account |
| `DEFAULT_TABLESPACE` | `VARCHAR2(30)` | `NOT NULL` | Default tablespace for data |
| `TEMPORARY_TABLESPACE` | `VARCHAR2(30)` | `NOT NULL` | Name of the default tablespace for temporary tables or the name of a tablespace group |
| `CREATED` | `DATE` | `NOT NULL` | User creation date |
| `PROFILE` | `VARCHAR2(30)` | `NOT NULL` | User resource profile name |
| `INITIAL_RSRC_CONSUMER_GROUP` | `VARCHAR2(30)` |  | Initial resource consumer group for the user |
| `EXTERNAL_NAME` | `VARCHAR2(4000)` |  | User external name |
| `PASSWORD_VERSIONS` | `VARCHAR2(8)` |  | Shows the list of versions of the password hashes (also known as "verifiers") existing for the account.  The `PASSWORD_VERSIONS` column value includes `10G` if an old case-insensitive ORCL hash exists and `11G` if a SHA-1 hash exists.  Note that one or both of these verifiers can exist for any given account. |
| `EDITIONS_ENABLED` | `VARCHAR2(1)` |  | Indicates whether editions have been enabled for the corresponding user (`Y`) or not (`N`) |
| `AUTHENTICATION_TYPE` | `VARCHAR2(8)` |  | Indicates the authentication mechanism for the user: |

See Also:

["USER\_USERS"](statviews_5506.md)