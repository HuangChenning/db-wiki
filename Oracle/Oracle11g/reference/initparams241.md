---
title: SHARED_SERVER_SESSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams241.htm
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
| Range of values | If `SHARED_SERVER_SESSIONS` is specified, then it should be less than `SESSIONS`. If `SHARED_SERVER_SESSIONS` is not specified, then a shared server session may be created as long as there is a free session slot. |

`SHARED_SERVER_SESSIONS` specifies the total number of shared server sessions to allow. Setting this parameter enables you to reserve user sessions for dedicated servers.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information on sessions