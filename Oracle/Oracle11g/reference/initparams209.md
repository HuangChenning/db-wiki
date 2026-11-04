---
title: REDO_TRANSPORT_USER
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams209.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REDO_TRANSPORT_USER =` `user_name` |
| Default value | There is no default value. |
| Range of values | Any character string that matches the name of a user who has been granted the `SYSDBA` or `SYSOPER` privilege |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |
| Oracle RAC | Every instance should use the same value |

`REDO_TRANSPORT_USER` specifies the name of the user whose password verifier is used when a remote login password file is used for redo transport authentication. This user must have the `SYSDBA` or `SYSOPER` privilege and must have the same password in the database that initiates the redo transport session and in the database that is the target of the redo transport session.

The value of this parameter is case sensitive and must exactly match the value of the `USERNAME` column of a row in the `V$PWFILE_USERS` view. The value of the `SYSDBA` or `SYSOPER` column of the row must also be `TRUE`.

If this parameter is not specified, then the password verifier of the `SYS` user will be used when a remote login password file is used for redo transport authentication.