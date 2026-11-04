---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MULTISHARD_QUERY_DATA_CONSISTENCY.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.218 MULTISHARD\_QUERY\_DATA\_CONSISTENCY

`MULTISHARD_QUERY_DATA_CONSISTENCY` enables you to specify a data consistency setting for multi-shard queries.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `MULTISHARD_QUERY_DATA_CONSISTENCY = { STRONG \| SHARD_LOCAL \| DELAYED_STANDBY_ALLOWED }` |
| Default value | `STRONG` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The value of this parameter can be different on different Oracle RAC instances. |

You can use `MULTISHARD_QUERY_DATA_CONSISTENCY` to avoid the cost of SCN synchronization when executing multi-shard queries across shards, which can be globally distributed.

`MULTISHARD_QUERY_DATA_CONSISTENCY` can be set at the system level or the session level.

The values that can be set for `MULTISHARD_QUERY_DATA_CONSISTENCY` are:

- `STRONG`: With this setting, SCN synchronization is performed across all shards, and data is consistent across all shards. This setting provides global consistent read capability. This is the default value.
- `SHARD_LOCAL`: With this setting, SCN synchronization is not performed across all shards. Data is consistent within each shard. This setting provides the most current data.
- `DELAYED_STANDBY_ALLOWED`: With this setting, SCN synchronization is not performed across all shards. Data is consistent within each shard. This setting allows data to be fetched from Data Guard standby databases when possible (for example, depending on load balancing), and may return stale data from standby databases.

See Also:

[Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=SHARD-GUID-902C8750-EF4E-4551-AF75-AC4B95FC7D03) for more information about specifying consistency levels in a multi-shard query