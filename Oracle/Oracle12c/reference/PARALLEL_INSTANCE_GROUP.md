---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PARALLEL_INSTANCE_GROUP.html
tags:
  - oracle
  - 12c
  - reference
---

Used in conjunction with services or with the `INSTANCE_GROUPS` parameter, `PARALLEL_INSTANCE_GROUP` lets you restrict parallel query operations to a limited number of instances.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_INSTANCE_GROUP = ` `service_name` `  \|  ` `group_name` |
| Default value | There is no default value; parallel execution is enabled across all currently active instances. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Any service name or any group name specified in the `INSTANCE_GROUPS` parameter of any active instance |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

`PARALLEL_INSTANCE_GROUP` is an Oracle RAC parameter that you can specify in parallel mode only. Note that the `INSTANCE_GROUPS` parameter has been deprecated.

This parameter identifies the parallel instance group Oracle will use for spawning parallel execution processes. If used in conjunction with services, then parallel operations will spawn parallel execution processes only on instances defined in the service. If used in conjunction with `INSTANCE_GROUPS`, then parallel operations will spawn parallel execution processes only on instances that specify a matching group in their `INSTANCE_GROUPS` parameter.

If the value assigned to `PARALLEL_INSTANCE_GROUP` is the name of a service or group that does not exist, then the operation runs serially. No parallelism is used.