---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/JAVA_POOL_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.169 JAVA\_POOL\_SIZE

`JAVA_POOL_SIZE` specifies (in bytes) the size of the Java pool, from which the Java memory manager allocates most Java state during run-time execution. This memory includes the shared in-memory representation of Java method and class definitions, as well as the Java objects that are migrated to the Java session space at end-of-call.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `JAVA_POOL_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | If `SGA_TARGET` is set: If the parameter is not specified, then the default is `0` (internally determined by the Oracle Database). If the parameter is specified, then the user-specified value indicates a minimum value for the memory pool.  If `SGA_TARGET` is not set: `24` MB, rounded up to the nearest granule size |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Minimum: `0` (values greater than zero are rounded up to the nearest granule size)  Maximum: operating system-dependent |
| Basic | No |