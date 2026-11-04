---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PWFILE_USERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.142 V$PWFILE\_USERS

`V$PWFILE_USERS` lists all users in the password file, and indicates whether the user has been granted the `SYSDBA`, `SYSOPER`, `SYSASM`, `SYSBACKUP`, `SYSDG`, and `SYSKM` privileges.

| Column | Datatype | Description |
| --- | --- | --- |
| `USERNAME` | `VARCHAR2(128)` | Name of the user that is contained in the password file |
| `SYSDBA` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSDBA` privileges (`TRUE`) or not (`FALSE`) |
| `SYSOPER` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSOPER` privileges (`TRUE`) or not (`FALSE`) |
| `SYSASM` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSASM` privileges (`TRUE`) or not (`FALSE`) |
| `SYSBACKUP` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSBACKUP` privileges (`TRUE`) or not (`FALSE`) |
| `SYSDG` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSDG` privileges (`TRUE`) or not (`FALSE`) |
| `SYSKM` | `VARCHAR2(5)` | Indicates whether the user can connect with `SYSKM` privileges (`TRUE`) or not (`FALSE`) |
| `ACCOUNT_STATUS` | `VARCHAR2(30)` | Account status:  - `OPEN` - `EXPIRED` - `EXPIRED (GRACE)` - `LOCKED (TIMED)` - `LOCKED` - `EXPIRED & LOCKED (TIMED)` - `EXPIRED & LOCKED` - `EXPIRED (GRACE) & LOCKED` |
| `PASSWORD_PROFILE` | `VARCHAR2(128)` | Password profile name |
| `LAST_LOGIN` | `TIMESTAMP(9) WITH TIME ZONE` | The time of the last user login  This column is not populated when a user connects to the database with administrative privileges, that is, `AS` `{` `SYSASM` `\|` `SYSBACKUP` `\|` `SYSDBA` `\|` `SYSDG` `\|` `SYSOPER` `\|` `SYSRAC` `\|` `SYSKM` `}`. The exception is as follows: If a user connects to the database with administrative privileges from a remote session, and the database password file format is 12.2 (`V$PASSWORDFILE_INFO.FORMAT` = `12.2`), then this column is populated. |
| `LOCK_DATE` | `DATE` | Date the account was locked if account status was `LOCKED` |
| `EXPIRY_DATE` | `DATE` | Date of expiration of the account |
| `EXTERNAL_NAME` | `VARCHAR2(1024)` | Shows Certificate DN or Principal Name of externally authenticated users |
| `AUTHENTICATION_TYPE` | `VARCHAR2(8)` | Indicates the authentication mechanism for the user:  - `EXTERNAL` - `CREATE` `USER` `user1` `IDENTIFIED` `EXTERNALLY;` - `GLOBAL` - `CREATE` `USER` `user2` `IDENTIFIED` `GLOBALLY;` - `PASSWORD` - `CREATE` `USER` `user3` `IDENTIFIED` `BY` `password``;` |
| `COMMON` | `VARCHAR2(3)` | This column has a value of `YES` if an administrative privilege (for example, `SYSDBA`) was granted with `CONTAINER=ALL`. Otherwise, the column has a value of `NO`. |
| `PASSWORD_VERSIONS` <sup>Foot 1</sup> | `VARCHAR2(12)` | Shows the list of versions of the password hashes (also known as "verifiers") existing for the account.  The values for this column can include:  - `10G`: If an old case-insensitive ORCL hash exists - `11G`: If a SHA-1 hash exists - `12C`: If a de-optimized PBKDF2-based hash exists  For more information about the 12C verifier, see [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG801).  Note that any combination of these verifiers can exist for any given account. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.