---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MULTISHARD_QUERY_DATA_CONSISTENCY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.215 MULTISHARD\_QUERY\_DATA\_CONSISTENCY

`MULTISHARD_QUERY_DATA_CONSISTENCY` enables you to specify a data consistency setting for multi-shard queries.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MULTISHARD_QUERY_DATA_CONSISTENCY = { STRONG \| SHARD_LOCAL \|                                         DELAYED_STANDBY_ALLOWED \| STANDBY_ONLY \| STANDBY_PREFERRED                                         }` |
| Default value | `STRONG` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

You can use `MULTISHARD_QUERY_DATA_CONSISTENCY` to avoid the cost of SCN synchronization when executing multi-shard queries across shards, which can be globally distributed.

`MULTISHARD_QUERY_DATA_CONSISTENCY` can be set at the system level or the session level.

The values that can be set for `MULTISHARD_QUERY_DATA_CONSISTENCY` are:

- `STRONG`: SCN synchronization is performed across all shards, and data is consistent across all shards. This setting provides global consistent read capability. This is the default value.
- `SHARD_LOCAL`: SCN synchronization is not performed across all shards. Data is consistent within each shard. This setting provides the most current data.
- `DELAYED_STANDBY_ALLOWED`: SCN synchronization is not performed across all shards. Data is consistent within each shard. This setting allows data to be fetched from Data Guard standby databases when possible (for example, depending on load balancing), and may return stale data from standby databases.
- `STANDBY_ONLY`: SCN synchronization is not performed across all shards. Data is consistent within each shard. Data is fetched only from standbys. If there are multiple standbys, chunks are distributed equally among them. If no standbys exist or none are alive, an error is raised.
- `STANDBY_PREFERRED`: SCN synchronization is not performed across all shards. Data is consistent within each shard. Data is fetched from the standbys when they are available, that is, the primary shard is excluded. If there are multiple standbys, chunks are distributed equally among them. If there is no standby to serve the request, data is fetched from the primary shard.

See Also:

[Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SHARD-GUID-902C8750-EF4E-4551-AF75-AC4B95FC7D03) for more information about specifying consistency levels in a multi-shard query