---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/REDO_TRANSPORT_USER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.302 REDO\_TRANSPORT\_USER

`REDO_TRANSPORT_USER` specifies the name of the user whose password verifier is used when a remote login password file is used for redo transport authentication. This user must have the `SYSOPER` privilege and must have the same password in the database that initiates the redo transport session and in the database that is the target of the redo transport session.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REDO_TRANSPORT_USER = ` `user_name` |
| Default value | There is no default value. |
| Range of values | Any character string that matches the name of a user who has been granted the `SYSOPER` privilege |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Every instance should use the same value |

The value of this parameter is case sensitive and must exactly match the value of the `USERNAME` column of a row in the `V$PWFILE_USERS` view. The value of the `SYSOPER` column of the row must also be `TRUE`.

If this parameter is not specified, then the password verifier of the `SYS` user will be used when a remote login password file is used for redo transport authentication.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB4748) for more information about this parameter