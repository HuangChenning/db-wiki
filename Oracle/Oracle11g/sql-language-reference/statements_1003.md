---
title: ALTER CLUSTER
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1003.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `ALTER` `CLUSTER` statement to redefine storage and parallelism characteristics of a cluster.

Note:

You cannot use this statement to change the number or the name of columns in the cluster key, and you cannot change the tablespace in which the cluster is stored.

See Also:

[CREATE CLUSTER](statements_5001.md) for information on creating a cluster, [DROP CLUSTER](statements_8007.md) and [DROP TABLE](statements_9003.md) for information on removing tables from a cluster, and [CREATE TABLE](statements_7002.md)... [physical\_properties](statements_7002.md) for information on adding a table to a cluster

Prerequisites

The cluster must be in your own schema or you must have the `ALTER` `ANY` `CLUSTER` system privilege.

Syntax

alter\_cluster::=

![alter_cluster](img/alter_cluster.gif)

> ```
> ALTER CLUSTER [ schema. ]cluster
>   { physical_attributes_clause
>   | SIZE size_clause
>   | allocate_extent_clause
>   | deallocate_unused_clause
>   | { CACHE | NOCACHE }
>   } ...
>   [ parallel_clause ] ;
> ```
  
  

(physical\_attributes\_clause::=, [size\_clause::=](clauses008.md), allocate\_extent\_clause::=, deallocate\_unused\_clause::=, parallel\_clause::=)

physical\_attributes\_clause::=

![physical_attributes_clause](img/physical_attributes_clause.gif)

> ```
> [ { PCTFREE integer
>   | PCTUSED integer
>   | INITRANS integer
>   | storage_clause
>   }...
> ]
> ```
  
  

([storage\_clause::=](clauses009.md))

allocate\_extent\_clause::=

![allocate_extent_clause](img/allocate_extent_clause.gif)

> ```
> ALLOCATE EXTENT
>   [ ( { SIZE size_clause
>       | DATAFILE 'filename'
>       | INSTANCE integer
>       } ...
>     )
>   ]
> ```
  
  

([size\_clause::=](clauses008.md))

deallocate\_unused\_clause::=

![deallocate_unused_clause](img/deallocate_unused_clause.gif)

> ```
> DEALLOCATE UNUSED [ KEEP size_clause ]
> ```
  
  

([size\_clause::=](clauses008.md))

parallel\_clause::=

![parallel_clause](img/parallel_clause.gif)

> ```
> { NOPARALLEL | PARALLEL [ integer ] }
> ```
  

Semantics

schema

Specify the schema containing the cluster. If you omit `schema`, then Oracle Database assumes the cluster is in your own schema.

cluster

Specify the name of the cluster to be altered.

physical\_attributes\_clause

Use this clause to change the values of the `PCTUSED`, `PCTFREE`, and `INITRANS` parameters of the cluster.

Use the `STORAGE` clause to change the storage characteristics of the cluster.

See Also:

- [physical\_attributes\_clause](clauses007.md) for information on the parameters
- [storage\_clause](clauses007.md) for a full description of that clause

Restriction on Physical Attributes You cannot change the values of the storage parameters `INITIAL` and `MINEXTENTS` for a cluster.

SIZE integer

Use the `SIZE` clause to specify the number of cluster keys that will be stored in data blocks allocated to the cluster.

Restriction on SIZE You can change the `SIZE` parameter only for an indexed cluster, not for a hash cluster.

See Also:

[CREATE CLUSTER](statements_5001.md) for a description of the `SIZE` parameter and "Modifying a Cluster: Example"

allocate\_extent\_clause

Specify the `allocate_extent_clause` to explicitly allocate a new extent for the cluster.

When you explicitly allocate an extent with this clause, Oracle Database does not evaluate the storage parameters of the cluster and determine a new size for the next extent to be allocated (as it does when you create a table). Therefore, specify `SIZE` if you do not want Oracle Database to use a default value.

See Also:

[allocate\_extent\_clause](clauses001.md) for a full description of this clause

deallocate\_unused\_clause

Use the `deallocate_unused_clause` to explicitly deallocate unused space at the end of the cluster and make the freed space available for other segments.

See Also:

[deallocate\_unused\_clause](clauses003.md) for a full description of this clause and "Deallocating Unused Space: Example"

CACHE | NOCACHE

This clause has the same behavior in `CREATE` `CLUSTER` and `ALTER` `CLUSTER` statements.

See Also:

["CACHE | NOCACHE"](statements_5001.md) for information on this clause.

parallel\_clause

Specify the `parallel_clause` to change the default degree of parallelism for queries on the cluster.

See Also:

[parallel\_clause](statements_7002.md) in the documentation on `CREATE` `TABLE` for complete information on this clause

Examples

The following examples modify the clusters that were created in the `CREATE` `CLUSTER` ["Examples"](statements_5001.md).

Modifying a Cluster: Example The next statement alters the `personnel` cluster:

```
ALTER CLUSTER personnel
   SIZE 1024 CACHE;
```

Oracle Database allocates 1024 bytes for each cluster key value and enables the cache attribute. Assuming a data block size of 2 kilobytes, future data blocks within this cluster contain 2 cluster keys in each data block, or 2 kilobytes divided by 1024 bytes.

Deallocating Unused Space: Example The following statement deallocates unused space from the `language` cluster, keeping 30 kilobytes of unused space for future use:

```
ALTER CLUSTER language 
   DEALLOCATE UNUSED KEEP 30 K;
```