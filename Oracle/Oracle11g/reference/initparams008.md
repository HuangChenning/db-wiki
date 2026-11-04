---
title: AQ_TM_PROCESSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams008.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | 1 |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `0` to `40` |
| Basic | No |

`AQ_TM_PROCESSES` controls time monitoring on queue messages and controls processing of messages with delay and expiration properties specified.You do not need to specify a value for this parameter because Oracle Database automatically determines the number of processes and autotunes them, as necessary. Therefore, Oracle highly recommends that you leave the `AQ_TM_PROCESSES` parameter unspecified and let the system autotune.

The default value for `AQ_TM_PROCESSES` is used if the client does not explicitly set a value for the parameter in the `init.ora` file or using the ALTER SYSTEM command.

Note:

If you want to disable the Queue Monitor Coordinator, then you must set `AQ_TM_PROCESSES` to 0 in your parameter file. Oracle strongly recommends that you do NOT set `AQ_TM_PROCESSES` to 0. If you are using Oracle Streams, then setting this parameter to zero (which Oracle Database respects no matter what) can cause serious problems.

See Also:

[Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for more information about this parameter and Advanced Queuing