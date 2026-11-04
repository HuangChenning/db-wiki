---
title: PARALLEL_INSTANCE_GROUP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams184.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_INSTANCE_GROUP =` `service_name` `\|` `group_name` |
| Default value | There is no default value; parallel execution is enabled across all currently active instances. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | Any service name or any group name specified in the `INSTANCE_GROUPS` parameter of any active instance |
| Oracle RAC | Multiple instances can have different values. |

`PARALLEL_INSTANCE_GROUP` is an Oracle RAC parameter that you can specify in parallel mode only. Used in conjunction with services or with the `INSTANCE_GROUPS` parameter, it lets you restrict parallel query operations to a limited number of instances. Note that the `INSTANCE_GROUPS` parameter has been deprecated.

This parameter identifies the parallel instance group Oracle will use for spawning parallel execution processes. If used in conjunction with services, then parallel operations will spawn parallel execution processes only on instances defined in the service. If used in conjunction with `INSTANCE_GROUPS`, then parallel operations will spawn parallel execution processes only on instances that specify a matching group in their `INSTANCE_GROUPS` parameter.

If the value assigned to `PARALLEL_INSTANCE_GROUP` is the name of a service or group that does not exist, then the operation runs serially. No parallelism is used.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information on parallel query execution in a Real Application Clusters environment