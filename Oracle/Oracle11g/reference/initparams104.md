---
title: INSTANCE_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams104.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INSTANCE_GROUPS =` `group_name` `[,` `group_name` `] ...` |
| Default value | There is no default value. |
| Modifiable | No |
| Range of values | One or more instance group names, separated by commas |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

The `INSTANCE_GROUPS` parameter is deprecated. It is retained for backward compatibility only.

`INSTANCE_GROUPS` is an Oracle RAC parameter that you can specify only in parallel mode. Used in conjunction with the `PARALLEL_INSTANCE_GROUP` parameter, it lets you restrict parallel query operations to a limited number of instances.

This parameter specifies one or more instance groups and assigns the current instance to those groups. If one of the specified groups is also specified in the `PARALLEL_INSTANCE_GROUP` parameter, then Oracle allocates query processes for a parallel operation from this instance.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information on parallel query execution in a Real Application Clusters environment
- ["PARALLEL\_INSTANCE\_GROUP"](initparams184.md)