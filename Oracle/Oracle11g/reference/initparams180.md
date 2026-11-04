---
title: PARALLEL_DEGREE_LIMIT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams180.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_DEGREE_LIMIT = { CPU \| IO \|` `integer` `}` |
| Default value | `CPU` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

With automatic degree of parallelism, Oracle automatically decides whether or not a statement should execute in parallel and what degree of parallelism the statement should use. The optimizer automatically determines the degree of parallelism for a statement based on the resource requirements of the statement. However, the optimizer will limit the degree of parallelism used to ensure parallel server processes do not flood the system. This limit is enforced by `PARALLEL_DEGREE_LIMIT`.

Values:

- `CPU`
	The maximum degree of parallelism is limited by the number of CPUs in the system. The formula used to calculate the limit is `PARALLEL_THREADS_PER_CPU` \* `CPU_COUNT` \* the number of instances available (by default, all the opened instances on the cluster but can be constrained using `PARALLEL_INSTANCE_GROUP` or service specification). This is the default.
- `IO`
	The maximum degree of parallelism the optimizer can use is limited by the I/O capacity of the system. The value is calculated by dividing the total system throughput by the maximum I/O bandwidth per process. You must run the `DBMS_RESOURCE_MANAGER.CALIBRATE_IO` procedure on the system in order to use the `IO` setting. This procedure will calculate the total system throughput and the maximum I/O bandwidth per process.
- `integer`
	A numeric value for this parameter specifies the maximum degree of parallelism the optimizer can choose for a SQL statement when automatic degree of parallelism is active. Automatic degree of parallelism is only enabled if `PARALLEL_DEGREE_POLICY` is set to `AUTO` or `LIMITED`.

See Also:

- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/toc.htm) for information about automatic degree of parallelism
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information on the `DBMS_RESOURCE_MANAGER.CALIBRATE_IO` procedure