---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LICENSE_MAX_SESSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.175 LICENSE\_MAX\_SESSIONS

`LICENSE_MAX_SESSIONS` specifies the maximum number of concurrent user sessions allowed.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0 to number of session licenses |
| Basic | No |
| Oracle RAC | Multiple instances can have different values, but the total for all instances mounting a database should be less than or equal to the total number of sessions licensed for that database. |

Note:

Oracle no longer offers licensing by the number of concurrent sessions. Therefore the `LICENSE_MAX_SESSIONS` and `LICENSE_SESSIONS_WARNING` initialization parameters have been deprecated.

When the limit specified by `LICENSE_MAX_SESSIONS` is reached, only users with the `RESTRICTED SESSION` privilege can connect to the database. Users who are not able to connect receive a warning message indicating that the system has reached maximum capacity.

A zero value indicates that concurrent usage (session) licensing is not enforced. If you set this parameter to a nonzero number, you might also want to set `LICENSE_SESSIONS_WARNING` (see " [LICENSE\_SESSIONS\_WARNING](LICENSE_SESSIONS_WARNING.md) ").

Do not enable both concurrent usage licensing and user licensing. Set either `LICENSE_MAX_SESSIONS` or `LICENSE_MAX_USERS` to zero.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11113) for more information about this parameter