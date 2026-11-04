---
title: "25.2.4 What is New in MySQL NDB Cluster 9.7"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-cluster-what-is-new.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 25.2.4 What is New in MySQL NDB Cluster 9.7

The following sections describe changes in the implementation of MySQL NDB Cluster in NDB Cluster 9.7.0, as compared to earlier release series. NDB Cluster 9.7 is available as a Development release for preview and testing of new features currently under development. For production, please use NDB 8.4; for more information, see [MySQL NDB Cluster 8.4](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysql-cluster.html). NDB Cluster 8.0 and 7.6 are previous GA releases which are still supported in production, although we recommend that new deployments for production use MySQL NDB Cluster 8.4.

#### What is New in NDB Cluster 9.7

Major changes and new features in NDB Cluster 9.7 which are likely to be of interest are listed here:

- **Ndb.cfg support removed.** Use of an `Ndb.cfg` configuration file in an [`NDB`](mysql-cluster.md) executable's startup directory was deprecated in MySQL 9.1, and is no longer supported as of NDB 9.5.0; such files are no longer read by any NDB Cluster executable.
	See [Section 25.4.3.3, “NDB Cluster Connection Strings”](mysql-cluster-connection-strings.md), for more information.

MySQL Cluster Manager has an advanced command-line interface that can simplify many complex NDB Cluster management tasks. See [MySQL Cluster Manager 9.7.0 User Manual](https://docs.oracle.com/cd/E17952_01/mysql-cluster-manager-9.7-en/), for more information.