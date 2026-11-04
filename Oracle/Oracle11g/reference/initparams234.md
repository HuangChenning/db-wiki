---
title: SESSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams234.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: (1.5 \* `PROCESSES`) + 22 |
| Modifiable | No |
| Range of values | 1 to 2 <sup>16</sup> (which is 1 to 65536) |
| Basic | Yes |

`SESSIONS` specifies the maximum number of sessions that can be created in the system. Because every login requires a session, this parameter effectively determines the maximum number of concurrent users in the system. You should always set this parameter explicitly to a value equivalent to your estimate of the maximum number of concurrent users, plus the number of background processes, plus approximately 10% for recursive sessions.

Oracle uses the default value of this parameter as its minimum. Values between 1 and the default do not trigger errors, but Oracle ignores them and uses the default instead.

The default values of the `ENQUEUE_RESOURCES` and `TRANSACTIONS` parameters are derived from `SESSIONS`. Therefore, if you increase the value of `SESSIONS`, you should consider whether to adjust the values of `ENQUEUE_RESOURCES` and `TRANSACTIONS` as well. (Note that `ENQUEUE_RESOURCES` is obsolete as of Oracle Database 10g release 2 (10.2).)

In a shared server environment, the value of `PROCESSES` can be quite small. Therefore, Oracle recommends that you adjust the value of `SESSIONS` to approximately 1.1 \* total number of connections.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for more information on memory structures and processes