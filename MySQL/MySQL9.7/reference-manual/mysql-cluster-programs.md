---
title: "25.5 NDB Cluster Programs"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-cluster-programs.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

Using and managing an NDB Cluster requires several specialized programs, which we describe in this chapter. We discuss the purposes of these programs in an NDB Cluster, how to use the programs, and what startup options are available for each of them.

These programs include the NDB Cluster data, management, and SQL node processes ([**ndbd**](mysql-cluster-programs-ndbd.md), [**ndbmtd**](mysql-cluster-programs-ndbmtd.md), [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md), and [**mysqld**](mysqld.md)) and the management client ([**ndb\_mgm**](mysql-cluster-programs-ndb-mgm.md)).

For information about using [**mysqld**](mysqld.md) as an NDB Cluster process, see [Section 25.6.10, “MySQL Server Usage for NDB Cluster”](mysql-cluster-mysqld.md).

Other [`NDB`](mysql-cluster.md) utility, diagnostic, and example programs are included with the NDB Cluster distribution. These include [**ndb\_restore**](mysql-cluster-programs-ndb-restore.md), [**ndb\_show\_tables**](mysql-cluster-programs-ndb-show-tables.md), and [**ndb\_config**](mysql-cluster-programs-ndb-config.md). These programs are also covered in this section.