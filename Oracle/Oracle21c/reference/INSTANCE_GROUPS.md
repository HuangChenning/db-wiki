---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INSTANCE_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.162 INSTANCE\_GROUPS

Used with the `PARALLEL_INSTANCE_GROUP` parameter, `INSTANCE_GROUPS` lets you restrict parallel query operations to a limited number of instances.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INSTANCE_GROUPS = ` `group_name` `  [,  ``group_name` ` ] ...` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | One or more instance group names, separated by commas |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

The `INSTANCE_GROUPS` parameter is deprecated. It is retained for backward compatibility only.

`INSTANCE_GROUPS` is an Oracle RAC parameter that you can specify only in parallel mode.

This parameter specifies one or more instance groups and assigns the current instance to those groups. If one of the specified groups is also specified in the `PARALLEL_INSTANCE_GROUP` parameter, then Oracle allocates query processes for a parallel operation from this instance.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD8273) for more information on parallel query execution in a Real Application Clusters environment
- " [PARALLEL\_INSTANCE\_GROUP](PARALLEL_INSTANCE_GROUP.md) "