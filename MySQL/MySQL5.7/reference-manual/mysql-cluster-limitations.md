---
title: "21.2.7 Known Limitations of NDB Cluster"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-limitations.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.2.7 Known Limitations of NDB Cluster

In the sections that follow, we discuss known limitations in current releases of NDB Cluster as compared with the features available when using the `MyISAM` and `InnoDB` storage engines. If you check the “Cluster” category in the MySQL bugs database at [http://bugs.mysql.com](http://bugs.mysql.com/), you can find known bugs in the following categories under “MySQL Server:” in the MySQL bugs database at [http://bugs.mysql.com](http://bugs.mysql.com/), which we intend to correct in upcoming releases of NDB Cluster:

- NDB Cluster
- Cluster Direct API (NDBAPI)
- Cluster Disk Data
- Cluster Replication
- ClusterJ

This information is intended to be complete with respect to the conditions just set forth. You can report any discrepancies that you encounter to the MySQL bugs database using the instructions given in [Section 1.5, “How to Report Bugs or Problems”](bug-reports.md). Any problem which we do not plan to fix in NDB Cluster 7.5 is added to the list.

See [Previous NDB Cluster Issues Resolved in NDB Cluster 8.0](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-cluster-limitations-resolved.html) for a list of issues in earlier releases that have been resolved in NDB Cluster 7.5.

Note

Limitations and other issues specific to NDB Cluster Replication are described in [Section 21.7.3, “Known Issues in NDB Cluster Replication”](mysql-cluster-replication-issues.md).