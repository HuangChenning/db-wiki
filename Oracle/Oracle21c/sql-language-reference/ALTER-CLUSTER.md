---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/ALTER-CLUSTER.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## ALTER CLUSTER

Purpose

Use the `ALTER` `CLUSTER` statement to redefine storage and parallelism characteristics of a cluster.

Note:

You cannot use this statement to change the number or the name of columns in the cluster key, and you cannot change the tablespace in which the cluster is stored.

See Also:

[CREATE CLUSTER](CREATE-CLUSTER.md) for information on creating a cluster, [DROP CLUSTER](DROP-CLUSTER.md) and [DROP TABLE](DROP-TABLE.md) for information on removing tables from a cluster, and [CREATE TABLE](CREATE-TABLE.md)... [physical\_properties](CREATE-TABLE.md) for information on adding a table to a cluster

Prerequisites

The cluster must be in your own schema or you must have the `ALTER` `ANY` `CLUSTER` system privilege.

Syntax

parallel\_clause::=

![parallel_clause](img/parallel_clause.gif)

> ```
> { NOPARALLEL | PARALLEL [ integer ] }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Semantics

schema

Specify the schema containing the cluster. If you omit `schema`, then Oracle Database assumes the cluster is in your own schema.

cluster

Specify the name of the cluster to be altered.

physical\_attributes\_clause

Use this clause to change the values of the `PCTUSED`, `PCTFREE`, and `INITRANS` parameters of the cluster.

Use the `STORAGE` clause to change the storage characteristics of the cluster.

See Also:

- [physical\_attributes\_clause](physical_attributes_clause.md) for information on the parameters
- [storage\_clause](physical_attributes_clause.md) for a full description of that clause

Restriction on Physical Attributes

You cannot change the values of the storage parameters `INITIAL` and `MINEXTENTS` for a cluster.

SIZE

integer

Use the `SIZE` clause to specify the number of cluster keys that will be stored in data blocks allocated to the cluster.

Restriction on SIZE

You can change the `SIZE` parameter only for an indexed cluster, not for a hash cluster.

See Also:

[CREATE CLUSTER](CREATE-CLUSTER.md) for a description of the `SIZE` parameter and " Modifying a Cluster: Example "

MODIFY PARTITION

Specify `MODIFY` `PARTITION` `partition` `allocate_extent_clause` to explicitly allocate a new extent for a cluster partition. This operation is valid only for range-partitioned hash clusters. For `partition`, specify the cluster partition name.

allocate\_extent\_clause

Specify `allocate_extent_clause` to explicitly allocate a new extent for a cluster. This operation is valid only for indexed clusters and nonpartitioned hash clusters.

When you explicitly allocate an extent with the `allocate_extent_clause`, Oracle Database does not evaluate the storage parameters of the cluster and determine a new size for the next extent to be allocated (as it does when you create a table). Therefore, specify `SIZE` if you do not want Oracle Database to use a default value.

See Also:

[allocate\_extent\_clause](allocate_extent_clause.md) for a full description of this clause

deallocate\_unused\_clause

Use the `deallocate_unused_clause` to explicitly deallocate unused space at the end of the cluster and make the freed space available for other segments.

See Also:

[deallocate\_unused\_clause](deallocate_unused_clause.md) for a full description of this clause and " Deallocating Unused Space: Example "

parallel\_clause

Specify the `parallel_clause` to change the default degree of parallelism for queries on the cluster.

See Also:

[parallel\_clause](CREATE-TABLE.md) in the documentation on `CREATE` `TABLE` for complete information on this clause

Examples

The following examples modify the clusters that were created in the `CREATE` `CLUSTER` " [Examples](CREATE-CLUSTER.md) ".

Modifying a Cluster: Example

The next statement alters the `personnel` cluster:

```
ALTER CLUSTER personnel
   SIZE 1024 CACHE;
```

Oracle Database allocates 1024 bytes for each cluster key value and enables the cache attribute. Assuming a data block size of 2 kilobytes, future data blocks within this cluster contain 2 cluster keys in each data block, or 2 kilobytes divided by 1024 bytes.

Deallocating Unused Space: Example

The following statement deallocates unused space from the `language` cluster, keeping 30 kilobytes of unused space for future use:

```
ALTER CLUSTER language 
   DEALLOCATE UNUSED KEEP 30 K;
```

Altering Clusters: Example

The following statement creates a cluster with the default key size (600):

```
CREATE CLUSTER EMP_DEPT (DEPTNO NUMBER(3))   
   SIZE 600   
   TABLESPACE USERS   
   STORAGE (INITIAL 200K   
      NEXT 300K   
      MINEXTENTS 2   
      PCTINCREASE 33);
```

The following statement queries `USER_CLUSTERS` to display the cluster metadata:

```
SELECT CLUSTER_NAME, TABLESPACE_NAME, KEY_SIZE, CLUSTER_TYPE, AVG_BLOCKS_PER_KEY, MIN_EXTENTS, MAX_EXTENTS FROM USER_CLUSTERS;

CLUSTER_NAME    TABLESPACE_NAME                  KEY_SIZE CLUST AVG_BLOCKS_PER_KEY MIN_EXTENTS MAX_EXTENTS
--------------- ------------------------------ ---------- ----- ------------------ ----------- -----------
EMP_DEPT        USERS                                 600 INDEX                              1  2147483645
```

The following statement modifies the cluster key size:

```
ALTER CLUSTER EMP_DEPT SIZE 1024;
```

The following statement displays the metadata of the modified cluster:

```
SELECT CLUSTER_NAME, TABLESPACE_NAME, KEY_SIZE, CLUSTER_TYPE, AVG_BLOCKS_PER_KEY, MIN_EXTENTS, MAX_EXTENTS FROM USER_CLUSTERS;

CLUSTER_NAME    TABLESPACE_NAME                  KEY_SIZE CLUST AVG_BLOCKS_PER_KEY MIN_EXTENTS MAX_EXTENTS
--------------- ------------------------------ ---------- ----- ------------------ ----------- -----------
EMP_DEPT        USERS                                1024 INDEX                              1  2147483645
```

The following statement deallocates unused space from the `EMP_DEPT` cluster, keeping 30 kilobytes of unused space for future use:

```
ALTER CLUSTER EMP_DEPT DEALLOCATE UNUSED KEEP 30 K;
```

The following statement displays the metadata of the modified cluster:

```
SELECT CLUSTER_NAME, TABLESPACE_NAME, KEY_SIZE, CLUSTER_TYPE, AVG_BLOCKS_PER_KEY, MIN_EXTENTS, MAX_EXTENTS FROM USER_CLUSTERS;

CLUSTER_NAME    TABLESPACE_NAME                  KEY_SIZE CLUST AVG_BLOCKS_PER_KEY MIN_EXTENTS MAX_EXTENTS
--------------- ------------------------------ ---------- ----- ------------------ ----------- -----------
EMP_DEPT        USERS                                1024 INDEX                              1  2147483645
```