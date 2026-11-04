---
title: ALTER CLUSTER
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-CLUSTER.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `ALTER` `CLUSTER` statement to redefine storage and parallelism characteristics of a cluster.

**Note:** You cannot use this statement to change the number or the name of columns in the cluster key, and you cannot change the tablespace in which the cluster is stored.

**See Also:** [CREATE CLUSTER](CREATE-CLUSTER.md) for information on creating a cluster, [DROP CLUSTER](DROP-CLUSTER.md) and [DROP TABLE](DROP-TABLE.md) for information on removing tables from a cluster, and [CREATE TABLE](CREATE-TABLE.md) … *[physical\_properties](CREATE-TABLE.md)* for information on adding a table to a cluster

## Prerequisites

The cluster must be in your own schema or you must have the `ALTER` `ANY` `CLUSTER` system privilege.

## Syntax

## alter\_cluster::=

[Description of the illustration alter\_cluster.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/alter_cluster.html)

(*physical\_attributes\_clause::*, *[size\_clause::=](size_clause.md)*, MODIFY PARTITION, *allocate\_extent\_clause::=*, *deallocate\_unused\_clause::=*, *parallel\_clause::=*)

## physical\_attributes\_clause::

[Description of the illustration physical\_attributes\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/physical_attributes_clause.html)

(*[storage\_clause::=](storage_clause.md)*)

## allocate\_extent\_clause::=

[Description of the illustration allocate\_extent\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/allocate_extent_clause.html)

(*[size\_clause::=](size_clause.md)*)

## deallocate\_unused\_clause::=

[Description of the illustration deallocate\_unused\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/deallocate_unused_clause.html)

(*[size\_clause::=](size_clause.md)*)

## parallel\_clause::=

[Description of the illustration parallel\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/parallel_clause.html)

## Semantics

## IF EXISTS

Specify `IF EXISTS` to alter an existing cluster.

**Note:** You can only use `IF EXISTS` from Release 19.28 and up.

## schema

Specify the schema containing the cluster. If you omit *schema*, then Oracle Database assumes the cluster is in your own schema.

## cluster

Specify the name of the cluster to be altered.

## physical\_attributes\_clause

Use this clause to change the values of the `PCTUSED`, `PCTFREE`, and `INITRANS` parameters of the cluster.

Use the `STORAGE` clause to change the storage characteristics of the cluster.

```md
<div class="infoboxnote" markdown="1">

**See Also:**

- *[physical_attributes_clause](physical_attributes_clause.html#GUID-A15063A9-3237-43D3-B0AE-D01F6E80B393)* for information on the parameters

- *[storage_clause](physical_attributes_clause.html#GUID-A15063A9-3237-43D3-B0AE-D01F6E80B393\_\_I1026834)* for a full description of that clause

</div>
```

**Restriction on Physical Attributes**

You cannot change the values of the storage parameters `INITIAL` and `MINEXTENTS` for a cluster.

## SIZE

***integer***

Use the `SIZE` clause to specify the number of cluster keys that will be stored in data blocks allocated to the cluster.

**Restriction on SIZE**

You can change the `SIZE` parameter only for an indexed cluster, not for a hash cluster.

**See Also:** [CREATE CLUSTER](CREATE-CLUSTER.md) for a description of the `SIZE` parameter and “ Modifying a Cluster: Example ”

## MODIFY PARTITION

Specify `MODIFY` `PARTITION` *partition* *allocate\_extent\_clause* to explicitly allocate a new extent for a cluster partition. This operation is valid only for range-partitioned hash clusters. For *partition*, specify the cluster partition name.

## allocate\_extent\_clause

Specify *allocate\_extent\_clause* to explicitly allocate a new extent for a cluster. This operation is valid only for indexed clusters and nonpartitioned hash clusters.

When you explicitly allocate an extent with the *allocate\_extent\_clause*, Oracle Database does not evaluate the storage parameters of the cluster and determine a new size for the next extent to be allocated (as it does when you create a table). Therefore, specify `SIZE` if you do not want Oracle Database to use a default value.

**See Also:** *[allocate\_extent\_clause](allocate_extent_clause.md)* for a full description of this clause

## deallocate\_unused\_clause

Use the *deallocate\_unused\_clause* to explicitly deallocate unused space at the end of the cluster and make the freed space available for other segments.

**See Also:** *[deallocate\_unused\_clause](deallocate_unused_clause.md)* for a full description of this clause and “ Deallocating Unused Space: Example ”

## parallel\_clause

Specify the *parallel\_clause* to change the default degree of parallelism for queries on the cluster.

**See Also:** *[parallel\_clause](CREATE-TABLE.md)* in the documentation on `CREATE` `TABLE` for complete information on this clause

## Examples

The following examples modify the clusters that were created in the `CREATE` `CLUSTER` “ [Examples](CREATE-CLUSTER.md) ”.

**Modifying a Cluster: Example**

The next statement alters the `personnel` cluster:

```md
ALTER CLUSTER personnel
   SIZE 1024 CACHE;
```

Oracle Database allocates 1024 bytes for each cluster key value and enables the cache attribute. Assuming a data block size of 2 kilobytes, future data blocks within this cluster contain 2 cluster keys in each data block, or 2 kilobytes divided by 1024 bytes.

**Deallocating Unused Space: Example**

The following statement deallocates unused space from the `language` cluster, keeping 30 kilobytes of unused space for future use:

```md
ALTER CLUSTER language
   DEALLOCATE UNUSED KEEP 30 K;
```

**Altering Clusters: Example**

The following statement creates a cluster with the default key size (600):

```md
CREATE CLUSTER EMP_DEPT (DEPTNO NUMBER(3))
   SIZE 600
   TABLESPACE USERS
   STORAGE (INITIAL 200K
      NEXT 300K
      MINEXTENTS 2
      PCTINCREASE 33);
```

The following statement queries `USER_CLUSTERS` to display the cluster metadata:

```md
SELECT CLUSTER_NAME, TABLESPACE_NAME, KEY_SIZE, CLUSTER_TYPE, AVG_BLOCKS_PER_KEY, MIN_EXTENTS, MAX_EXTENTS FROM USER_CLUSTERS;

CLUSTER_NAME    TABLESPACE_NAME                  KEY_SIZE CLUST AVG_BLOCKS_PER_KEY MIN_EXTENTS MAX_EXTENTS
--------------- ------------------------------ ---------- ----- ------------------ ----------- -----------
EMP_DEPT        USERS                                 600 INDEX                              1  2147483645
```

The following statement modifies the cluster key size:

```md
ALTER CLUSTER EMP_DEPT SIZE 1024;
```

The following statement displays the metadata of the modified cluster:

```md
SELECT CLUSTER_NAME, TABLESPACE_NAME, KEY_SIZE, CLUSTER_TYPE, AVG_BLOCKS_PER_KEY, MIN_EXTENTS, MAX_EXTENTS FROM USER_CLUSTERS;

CLUSTER_NAME    TABLESPACE_NAME                  KEY_SIZE CLUST AVG_BLOCKS_PER_KEY MIN_EXTENTS MAX_EXTENTS
--------------- ------------------------------ ---------- ----- ------------------ ----------- -----------
EMP_DEPT        USERS                                1024 INDEX                              1  2147483645
```

The following statement deallocates unused space from the `EMP_DEPT` cluster, keeping 30 kilobytes of unused space for future use:

```md
ALTER CLUSTER EMP_DEPT DEALLOCATE UNUSED KEEP 30 K;
```

The following statement displays the metadata of the modified cluster:

```md
SELECT CLUSTER_NAME, TABLESPACE_NAME, KEY_SIZE, CLUSTER_TYPE, AVG_BLOCKS_PER_KEY, MIN_EXTENTS, MAX_EXTENTS FROM USER_CLUSTERS;

CLUSTER_NAME    TABLESPACE_NAME                  KEY_SIZE CLUST AVG_BLOCKS_PER_KEY MIN_EXTENTS MAX_EXTENTS
--------------- ------------------------------ ---------- ----- ------------------ ----------- -----------
EMP_DEPT        USERS                                1024 INDEX                              1  2147483645
```