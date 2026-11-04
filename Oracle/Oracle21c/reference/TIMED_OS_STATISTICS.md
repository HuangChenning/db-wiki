---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TIMED_OS_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.364 TIMED\_OS\_STATISTICS

`TIMED_OS_STATISTICS` specifies (in seconds) the interval at which Oracle collects operating system statistics when a request is made from the client to the server or when a request completes.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If `STATISTICS_LEVEL` is set to `ALL`, then `60`  If `STATISTICS_LEVEL` is set to `BASIC` or `TYPICAL`, then `0` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Unlimited |
| Basic | No |

On dedicated servers, Oracle collects operating system statistics at user logon and after each subsequent client invocation through the OCI into the Oracle server as a remote procedure call message.

On shared servers, Oracle collects statistics when client calls to Oracle are processed.

A value of zero specifies that operating system statistics are not gathered. To collect statistics, set a value meaningful for your application and site needs.

Note:

Gathering operating system statistics is very expensive. Oracle recommends that you set this parameter in an `ALTER SYSTEM` statement rather than in the initialization parameter file, and that you reset the value to zero as soon as the needed statistics have been gathered.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA153) for more information about this parameter