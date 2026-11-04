---
title: THREAD
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams257.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | No |
| Range of values | 0 to the maximum number of enabled threads |
| Oracle RAC | If specified, multiple instances must have different values. |

`THREAD` has been superseded by the `INSTANCE_NAME` and `INSTANCE_NUMBER` parameters, and will be made obsolete in a future release of the Oracle Database.

See Also:

["INSTANCE\_NAME"](initparams105.md) and ["INSTANCE\_NUMBER"](initparams106.md)