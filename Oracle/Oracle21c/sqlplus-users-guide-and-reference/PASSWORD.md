---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/PASSWORD.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
PASSW[ORD] [username]
```

where username specifies the user. If omitted, username defaults to the current user.

Enables you to change a password without echoing it on an input device.

If the user's password profile contains a non-zero value for the `PASSWORD_ROLLOVER_TIME` parameter, then changing the password starts the password rollover period for the user account.

If you are a database user that is associated with a profile that enables gradual password rollover (a period of time where both the old and and new passwords are valid), then you can change your password through SQL\*Plus and have both the newly created password and the old password work during user authentication.

For more information, see [Gradual Database Password Rollover for Applications](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=DBSEG-GUID-ACBA8DAE-C5B4-4811-A31D-53B97C50249B) in Oracle Database Security Guide.

During the password rollover period, you can log in using either the old password (password1) or the new password (password2).

To change the password again during the rollover period, use either password1 or password2 as the old password. For example, use either one of the following statements to change the password to password3:

```
ALTER USER jones IDENTIFIED BY password3 REPLACE password1
```
```
ALTER USER jones IDENTIFIED BY password3 REPLACE password2
```

There is no limit to the number of times you can change the password during the password rollover period. However, note that the password rollover period is fixed starting from the time the password is changed the first time.

Usage

To change the password of another user, you must have been granted the appropriate privilege. See [CONNECT](CONNECT.md) for more information about changing your password.

Examples

If you want to change your current password, enter

```
PASSWORD
Changing password for your_password
Old password: your_password
New password: new_password
Retype new password: new_password
Password changed
```

If you are logged on as a DBA, and want to change the password for user johnw (currently identified by johnwpass) to johnwnewpass

```
PASSWORD johnw
Changing password for johnw
New password: johnwnewpass
Retype new password: johnwnewpass
Password changed
```

Passwords are not echoed to the screen, they are shown here for your convenience.