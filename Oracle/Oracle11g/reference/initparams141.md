---
title: MAX_SHARED_SERVERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams141.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Range of values | If `MAX_SHARED_SERVERS` is specified, then it should be greater than or equal to `SHARED_SERVERS` and less than `PROCESSES`. |
| Basic | No |

`MAX_SHARED_SERVERS` specifies the maximum number of shared server processes allowed to be running simultaneously. Setting this parameter enables you to reserve process slots for other processes, such as dedicated servers.

When you want to reduce the range of shared servers, you can reduce `MAX_SHARED_SERVERS` before reducing `SHARED_SERVERS`. If `MAX_SHARED_SERVERS` is lower than `SHARED_SERVERS`, then the number of shared servers will not vary but will remain at the constant level specified by `SHARED_SERVERS`. If `MAX_SHARED_SERVERS` is not specified, then a shared server process may be spawned as long as the number of free process slots is greater than 1 / 8 the maximum number of processes, or 2 if `PROCESSES` is less than 24.

See Also:

- ["SHARED\_SERVERS"](initparams242.md)
- ["PROCESSES"](initparams202.md)
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on setting this parameter
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for information on processes
- Your operating system-specific Oracle documentation for the default value and range of values