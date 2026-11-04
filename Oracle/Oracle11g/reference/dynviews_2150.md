---
title: "V$RO_USER_ACCOUNT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2150.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RO_USER_ACCOUNT` is populated only on Oracle databases that are open in read-only mode. When a database is read-only, security data cannot be stored in normal catalogue tables. Instead, the security data is stored in an in-memory table that is queried through this view.

In an Oracle Data Guard environment, some of the security information for user accounts on the standby is inherited from the primary server. For example, if the account is locked out unlimited on the primary, then it will be locked on the standby database(s). The information stored on the standby is volatile information that user actions on the standby database(s) can affect, such as the number of failed logins, and the time the account was locked on the standby due to failed access attempts. Note that failed login attempts on standbys do not affect the account status on primaries.

| Column | Datatype | Description |
| --- | --- | --- |
| `USERID` | `NUMBER` | User ID number |
| `PASSW_EXPIRED` | `NUMBER` | Indicates whether the password has expired (`1`) or not (`0`) |
| `PASSW_IN_GRACE` | `NUMBER` | Indicates whether the account is in grace (`1`) or not (`0`) |
| `PASSW_LOCKED` | `NUMBER` | Indicates whether the account is locked (`1`) or not (`0`) |
| `PASSW_LOCK_UNLIM` | `NUMBER` | Indicates whether the account is locked for an unlimited time (`1`) or not (`0`) |
| `FAILED_LOGINS` | `NUMBER` | The number of failed login attempts. The count is not cumulative; it is reset upon successful logon to the account |
| `EXPIRATION_AFTER_GRACE` | `TIMESTAMP(3)` | The expiration time after grace |
| `PASSW_LOCK_TIME` | `TIMESTAMP(3)` | The time the account was locked out, if the account was locked for a limited time |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).