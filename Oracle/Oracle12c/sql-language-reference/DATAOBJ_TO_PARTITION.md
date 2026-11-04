---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DATAOBJ_TO_PARTITION.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![dataobj_to_partition](img/dataobj_to_partition.gif)

> ```
> DATAOBJ_TO_PARTITION( table, partition_id )
> ```


Purpose

`DATAOBJ_TO_PARTITION` is useful only to Data Cartridge developers who are performing data maintenance or query operations on system-partitioned tables that are used to store domain index data. The DML or query operations are triggered by corresponding operations on the base table of the domain index.

This function takes as arguments the name of the base table and the partition ID of the base table partition, both of which are passed to the function by the appropriate ODCIIndex method. The function returns the absolute partition number of the corresponding system-partitioned table, which can be used to perform the operation (DML or query) on that partition of the system-partitioned table.

Note:

If the base table is interval partitioned, then Oracle recommends that you instead use the `DATAOBJ_TO_MAT_PARTITION` function. Refer to [DATAOBJ\_TO\_MAT\_PARTITION](DATAOBJ_TO_MAT_PARTITION.md) for more information.

See Also:

[Oracle Database Data Cartridge Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=ADDCI290) for information on the use of the `DATAOBJ_TO_PARTITION` function, including examples