---
title: MAX_DISPATCHERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams138.htm
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
| Range of values | If `MAX_DISPATCHERS` is specified, then it should be greater than or equal to the number of dispatchers specified by the `DISPATCHERS` parameter and less than the number of processes specified by the `PROCESSES` parameter. |
| Basic | No |

`MAX_DISPATCHERS` specifies the maximum number of dispatcher processes allowed to be running simultaneously. It can be overridden by the `DISPATCHERS` parameter and is maintained for backward compatibility with older releases.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on setting this parameter
- Your operating system-specific Oracle documentation for the default value and range of values