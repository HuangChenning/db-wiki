---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_SHARD.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.64 V$SQL\_SHARD

`V$SQL_SHARD` displays the shard information for a shard query's previous execution. This view uniquely maps a shard SQL fragment of a cross shard query to the target shard database.

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of a cross shard query on the coordinator |
| `CHILD_NUMBER` | `NUMBER` | Cursor child number of a cross shard query on the coordinator |
| `OPERATION_ID` | `NUMBER` | Operation ID of a remote node for a shard SQL fragment of a cross shard query |
| `SHARD_SQL_ID` | `VARCHAR2(13)` | SQL ID of the SQL segment associated with a remote operation identified by the operation ID in the `OPERATION_ID` column |
| `SHARD_ID` | `NUMBER` | IDs of shards where the shard SQL fragment was executed |
| `SHARD_CHILD_NUMBER` | `NUMBER` | Cursor child number of a shard SQL fragment on a shard. The default value is `0`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Using Oracle Sharding](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SHARD-GUID-51377035-217B-4624-88CD-A5D5DE125606) for more information about the `V$SQL_SHARD` view