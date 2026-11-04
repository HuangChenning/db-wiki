---
title: "21.2.6 MySQL Server Using InnoDB Compared with NDB Cluster"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-compared.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.2.6 MySQL Server Using InnoDB Compared with NDB Cluster

MySQL Server offers a number of choices in storage engines. Since both [`NDB`](mysql-cluster.md) and [`InnoDB`](innodb-storage-engine.md) can serve as transactional MySQL storage engines, users of MySQL Server sometimes become interested in NDB Cluster. They see [`NDB`](mysql-cluster.md) as a possible alternative or upgrade to the default [`InnoDB`](innodb-storage-engine.md) storage engine in MySQL 5.7. While [`NDB`](mysql-cluster.md) and [`InnoDB`](innodb-storage-engine.md) share common characteristics, there are differences in architecture and implementation, so that some existing MySQL Server applications and usage scenarios can be a good fit for NDB Cluster, but not all of them.

In this section, we discuss and compare some characteristics of the [`NDB`](mysql-cluster.md) storage engine used by NDB 7.5 with [`InnoDB`](innodb-storage-engine.md) used in MySQL 5.7. The next few sections provide a technical comparison. In many instances, decisions about when and where to use NDB Cluster must be made on a case-by-case basis, taking all factors into consideration. While it is beyond the scope of this documentation to provide specifics for every conceivable usage scenario, we also attempt to offer some very general guidance on the relative suitability of some common types of applications for [`NDB`](mysql-cluster.md) as opposed to [`InnoDB`](innodb-storage-engine.md) back ends.

NDB Cluster 7.5 uses a [**mysqld**](mysqld.md) based on MySQL 5.7, including support for [`InnoDB`](innodb-storage-engine.md) 1.1. While it is possible to use `InnoDB` tables with NDB Cluster, such tables are not clustered. It is also not possible to use programs or libraries from an NDB Cluster 7.5 distribution with MySQL Server 5.7, or the reverse.

While it is also true that some types of common business applications can be run either on NDB Cluster or on MySQL Server (most likely using the [`InnoDB`](innodb-storage-engine.md) storage engine), there are some important architectural and implementation differences. [Section 21.2.6.1, “Differences Between the NDB and InnoDB Storage Engines”](mysql-cluster-ndb-innodb-engines.md), provides a summary of the these differences. Due to the differences, some usage scenarios are clearly more suitable for one engine or the other; see [Section 21.2.6.2, “NDB and InnoDB Workloads”](mysql-cluster-ndb-innodb-workloads.md). This in turn has an impact on the types of applications that better suited for use with [`NDB`](mysql-cluster.md) or [`InnoDB`](innodb-storage-engine.md). See [Section 21.2.6.3, “NDB and InnoDB Feature Usage Summary”](mysql-cluster-ndb-innodb-usage.md), for a comparison of the relative suitability of each for use in common types of database applications.

For information about the relative characteristics of the [`NDB`](mysql-cluster.md) and [`MEMORY`](memory-storage-engine.md) storage engines, see [When to Use MEMORY or NDB Cluster](memory-storage-engine.md).

See [Chapter 15, *Alternative Storage Engines*](storage-engines.md), for additional information about MySQL storage engines.