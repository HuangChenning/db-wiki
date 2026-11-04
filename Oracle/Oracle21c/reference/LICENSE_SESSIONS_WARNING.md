---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LICENSE_SESSIONS_WARNING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.177 LICENSE\_SESSIONS\_WARNING

`LICENSE_SESSIONS_WARNING` specifies a warning limit on the number of concurrent user sessions.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0 to value of `LICENSE_MAX_SESSIONS` parameter |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

Oracle no longer offers licensing by the number of concurrent sessions. Therefore the `LICENSE_MAX_SESSIONS` and `LICENSE_SESSIONS_WARNING` initialization parameters have been deprecated.

When this limit specified by `LICENSE_SESSIONS_WARNING` is reached, additional users can connect, but Oracle writes a message in the alert log for each new connection. Users with `RESTRICTED SESSION` privilege who connect after the limit is reached receive a warning message stating that the system is nearing its maximum capacity.

If this parameter is set to zero, no warning is given as you approach the concurrent usage (session) limit. If you set this parameter to a nonzero number, you should also set `LICENSE_MAX_SESSIONS` (see " [LICENSE\_MAX\_SESSIONS](LICENSE_MAX_SESSIONS.md) ").

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11113) for more information on setting this parameter