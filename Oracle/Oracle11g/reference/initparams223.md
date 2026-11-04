---
title: RESUMABLE_TIMEOUT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams223.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` (seconds) |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | `0` to 2 <sup>31</sup> - 1 (in seconds) |
| Oracle RAC | Multiple instances can have different values. |

`RESUMABLE_TIMEOUT` enables or disables resumable statements and specifies resumable timeout at the system level.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about enabling resumable space allocation, what conditions are correctable, and what statements can be made resumable