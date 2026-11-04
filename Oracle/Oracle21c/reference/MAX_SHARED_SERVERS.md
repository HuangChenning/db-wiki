---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAX_SHARED_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.209 MAX\_SHARED\_SERVERS

Setting this parameter enables you to reserve process slots for other processes, such as dedicated servers.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | If `MAX_SHARED_SERVERS` is specified, then it should be greater than or equal to `SHARED_SERVERS` and less than `PROCESSES`. |
| Basic | No |

When you want to reduce the range of shared servers, you can reduce `MAX_SHARED_SERVERS` before reducing `SHARED_SERVERS`. If `MAX_SHARED_SERVERS` is lower than `SHARED_SERVERS`, then the number of shared servers will not vary but will remain at the constant level specified by `SHARED_SERVERS`. If `MAX_SHARED_SERVERS` is not specified, then a shared server process may be spawned as long as the number of free process slots is greater than 1 / 8 the maximum number of processes, or 2 if `PROCESSES` is less than 24.

See Also:

- " [SHARED\_SERVERS](SHARED_SERVERS.md) "
- " [PROCESSES](PROCESSES.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11173) for more information on setting this parameter
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT901) for information on processes
- Your operating system-specific Oracle documentation for the default value and range of values