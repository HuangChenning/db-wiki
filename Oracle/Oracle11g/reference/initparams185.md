---
title: PARALLEL_IO_CAP_ENABLED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams185.htm
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
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

The `PARALLEL_IO_CAP_ENABLED` parameter is deprecated. It is retained for backward compatibility only. It is replaced by the `PARALLEL_DEGREE_LIMIT` parameter when set to `IO`.

`PARALLEL_IO_CAP_ENABLED` specifies whether or not Oracle caps the default degree of parallelism to no greater than what the I/O system can support. This new value is calculated based on the results of the resource manager's I/O calibration package.

If `PARALLEL_IO_CAP_ENABLED` is set to `true` and the database I/O capacity has been calibrated, then Oracle will reduce the default degree of parallelism if the I/O capacity cannot support the available number of CPUs. To calibrate the I/O capacity, use the `DBMS_RESOURCE_MANAGER.CALIBRATE_IO` procedure to measure the system's I/O capacity. Oracle then computes the degree of parallelism so as not to exceed the system's I/O capacity.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) for information on initializing and tuning parameters for parallel execution