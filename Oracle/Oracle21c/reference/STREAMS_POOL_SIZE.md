---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STREAMS_POOL_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.356 STREAMS\_POOL\_SIZE

The `STREAMS_POOL_SIZE` value helps determine the size of the Streams pool.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `STREAMS_POOL_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Minimum: `0` (values greater than zero are rounded up to the nearest granule size)  Maximum: operating system-dependent |
| Basic | No |

Oracle's Automatic Shared Memory Management feature manages the size of the Streams pool when the `SGA_TARGET` initialization parameter is set to a nonzero value. If the `STREAMS_POOL_SIZE` initialization parameter also is set to a nonzero value, then Automatic Shared Memory Management uses this value as a minimum for the Streams pool.

If `SGA_TARGET` is set to a nonzero value and `STREAMS_POOL_SIZE` is not specified or is set to a null value, Automatic Shared Memory Management uses 0 (zero) bytes as a minimum for the Streams pool.

If the `STREAMS_POOL_SIZE` initialization parameter is set to a nonzero value, and the `SGA_TARGET` parameter is set to 0 (zero), then the Streams pool size is the value specified by the `STREAMS_POOL_SIZE` parameter, in bytes.

If both the `STREAMS_POOL_SIZE` and the `SGA_TARGET` initialization parameters are set to 0 (zero), then, by default, on the first request for Streams pool memory in a database, an amount of memory equal to 10% of the shared pool is transferred from the buffer cache to the Streams pool. Products and features that use the Streams pool include Oracle GoldenGate, XStream, Oracle Advanced Queuing, and Oracle Data Pump.

The Streams pool is a shared resource, and the amount of memory a process can use from the Streams pool is determined by the application. The capture or apply parameter `MAX_SGA_SIZE` can be controlled for Oracle GoldenGate or XStream. For Oracle Advanced Queuing, use the procedures in the `dbms_aqadm` package to control the amount of Streams Pool needed.

See Also:

- [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=XSTRM1560) for information on configuring the Streams pool for an XStream Out configuration
- [Oracle Database XStream Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=XSTRM1566) for information on configuring the Streams pool for an XStream In configuration
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS005) for more information about the `dbms_aqadm` package