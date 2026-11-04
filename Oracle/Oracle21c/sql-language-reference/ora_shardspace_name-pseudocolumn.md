---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/ora_shardspace_name-pseudocolumn.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## ORA\_SHARDSPACE\_NAME Pseudocolumn

You can use the `ORA_SHARDSPACE_NAME` pseudocolumn to run queries across shards instead of a sharding key.

Before you can run cross-shard queries from the catalog, you must create users in the catalog with shared DDL enabled. Then you must grant these users access to the privately sharded tables.

The queries referencing the privately sharded tables will run across the shards in the catalog using the pseudocolumn `ORA_SHARDSPACE_NAME` associated to them. To run a cross shard query on a given shard, you must filter the query with the predicate `ORA_SHARDSPACE_NAME = <shardspace_name_belonging_to_name>`.

Examples

```
SELECT CUST_NAME, CUST_ID FROM CUSTOMER WHERE ORA_SHARDSPACE_NAME = 'EUROPE'
```

This query will run on one of the shards belonging to the shardspace named Europe. The query will run on the primary shard of the sharspace Europe or on one of its standbys, depending on the value of the parameter `MULTISHARD_QUERY_DATA_CONSISTENCY`.

A query like:

```
SELECT CUST_NAME, CUST_ID FROM CUSTOMER
```

where the table `CUSTOMER` is marked as privately sharded, will run on all shards.