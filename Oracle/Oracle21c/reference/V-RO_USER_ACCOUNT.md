---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RO_USER_ACCOUNT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.183 V$RO\_USER\_ACCOUNT

`V$RO_USER_ACCOUNT` is populated only on Oracle databases that are open in read-only mode. When a database is read-only, security data cannot be stored in normal catalogue tables. Instead, the security data is stored in an in-memory table that is queried through this view.

In an Oracle Data Guard environment, some of the security information for user accounts on the standby is inherited from the primary server. For example, if the account is locked out unlimited on the primary, then it will be locked on the standby database(s). The information stored on the standby is volatile information that user actions on the standby database(s) can affect, such as the number of failed logins, and the time the account was locked on the standby due to failed access attempts. Note that failed login attempts on standbys do not affect the account status on primaries.

If this view is queried from the root in a multitenent container database (CDB), then only common users and the `SYS` user are returned.

If this view is queried from a pluggable database (PDB), only rows that pertain to the current PDB are returned.

| Column | Datatype | Description |
| --- | --- | --- |
| `USERID` | `NUMBER` | User ID number |
| `PASSW_EXPIRED` | `NUMBER` | Indicates whether the password has expired (`1`) or not (`0`) |
| `PASSW_IN_GRACE` | `NUMBER` | Indicates whether the account is in grace (`1`) or not (`0`) |
| `PASSW_LOCKED` | `NUMBER` | Indicates whether the account is locked (`1`) or not (`0`) |
| `PASSW_LOCK_UNLIM` | `NUMBER` | Indicates whether the account is locked for an unlimited time (`1`) or not (`0`) |
| `FAILED_LOGINS` | `NUMBER` | The number of failed login attempts. The count is not cumulative; it is reset upon successful logon to the account |
| `EXPIRATION_AFTER_GRACE` | `TIMESTAMP(3)` | The expiration time after grace |
| `PASSW_LOCK_TIME` | `TIMESTAMP(3)` | The time the account was locked out |
| `CON_ID` | `NUMBER` | The ID of the container where the failed login occurred.  For users that are not common users, the `CON_ID` is the PDB ID where the failed login attempt occurred.  For common users, the `CON_ID` is `0`.  The login attempts that occurred on a PDB are not displayed when you query `V$RO_USER_ACCOUNT` from another PDB. You only see the failed login attempts of any users (that are not common users) if those failed login attempts occurred on the same PDB from which you are querying `V$RO_USER_ACCOUNT`.  The failed login attempts of common users (and of the `SYS` user) are only displayed when `V$RO_USER_ACCOUNT` is queried from the root of a CDB, not when it is queried from a PDB.  In a non-CDB, the value is always `0`. |
| `USERNAME` | `VARCHAR2(128)` | User name |