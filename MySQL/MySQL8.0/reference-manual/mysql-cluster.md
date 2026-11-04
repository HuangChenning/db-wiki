---
title: "Chapter 25 MySQL NDB Cluster 8.0"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This chapter provides information about MySQL NDB Cluster, a high-availability, high-redundancy version of MySQL adapted for the distributed computing environment, using the `NDB` storage engine (also known as `NDBCLUSTER`) to enable running several computers with MySQL servers and other software in a cluster. NDB Cluster 8.0, now available as a General Availability (GA) release (beginning with version 8.0.19), incorporates version 8.0 of the `NDB` storage engine. This chapter also provides information specific to NDB Cluster 8.0, and covers releases through 8.0.43. NDB Cluster 8.4 (NDB 8.4.7), based on version 8.4 of the NDB storage engine, is also available as an LTS release. See [What is New in MySQL NDB Cluster 8.4](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysql-cluster-what-is-new.html) for information about differences in NDB 8.4 as compared to earlier releases. NDB Cluster 7.6 and NDB Cluster 7.5, still available as GA releases, use versions 7.6 and 7.5 of `NDB`, respectively. NDB Cluster 7.6 and 7.5 are previous GA releases still supported in production; for information about NDB Cluster 7.6, see [What is New in NDB Cluster 7.6](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysql-cluster-what-is-new-7-6.html). For similar information about NDB Cluster 7.5, see [What is New in NDB Cluster 7.5](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/mysql-cluster-what-is-new-7-5.html). Previous GA releases NDB Cluster 7.4 and NDB Cluster 7.3 incorporated `NDB` versions 7.4 and 7.3, respectively. *NDB 7.4 and older release series are no longer supported or maintained*. Both NDB 8.0 and NDB 8.4 are supported in production, and are recommended for new deployments.