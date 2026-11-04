---
title: SQL_TRACE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams248.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | `true \| false` |

`SQL_TRACE` enables or disables the SQL trace facility. Setting this parameter to `true` provides information on tuning that you can use to improve performance.

Caution:

Using this initialization parameter to enable the SQL trace facility for the entire instance can have a severe performance impact. Enable the facility for specific sessions using the `ALTER SESSION` statement. If you must enable the facility on an entire production environment, then you can minimize performance impact by:

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information about performance diagnostic tools

Note:

The `SQL_TRACE` parameter is deprecated. Oracle recommends that you use the `DBMS_MONITOR` and `DBMS_SESSION` packages instead. `SQL_TRACE` is retained for backward compatibility only.