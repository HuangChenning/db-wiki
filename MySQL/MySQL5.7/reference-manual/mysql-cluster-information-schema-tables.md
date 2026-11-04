---
title: "21.6.16 INFORMATION_SCHEMA Tables for NDB Cluster"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-information-schema-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.6.16 INFORMATION\_SCHEMA Tables for NDB Cluster

Two [`INFORMATION_SCHEMA`](information-schema.md) tables provide information that is of particular use when managing an NDB Cluster. The [`FILES`](information-schema-files-table.md) table provides information about NDB Cluster Disk Data files. The [`ndb_transid_mysql_connection_map`](information-schema-ndb-transid-mysql-connection-map-table.md) table provides a mapping between transactions, transaction coordinators, and API nodes.

Additional statistical and other data about NDB Cluster transactions, operations, threads, blocks, and other aspects of performance can be obtained from the tables in the [`ndbinfo`](mysql-cluster-ndbinfo.md) database. For information about these tables, see [Section 21.6.15, “ndbinfo: The NDB Cluster Information Database”](mysql-cluster-ndbinfo.md).