---
title: "16.4.1 Replication Features and Issues"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/replication-features.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 16.4.1 Replication Features and Issues

The following sections provide information about what is supported and what is not in MySQL replication, and about specific issues and situations that may occur when replicating certain statements.

Statement-based replication depends on compatibility at the SQL level between the source and replica. In other words, successful statement-based replication requires that any SQL features used be supported by both the source and the replica servers. If you use a feature on the source server that is available only in the current version of MySQL, you cannot replicate to a replica that uses an earlier version of MySQL. Such incompatibilities can also occur within a release series as well as between versions.

If you are planning to use statement-based replication between MySQL 5.7 and a previous MySQL release series, it is a good idea to consult the edition of the *MySQL Reference Manual* corresponding to the earlier release series for information regarding the replication characteristics of that series.

With MySQL's statement-based replication, there may be issues with replicating stored routines or triggers. You can avoid these issues by using MySQL's row-based replication instead. For a detailed list of issues, see [Section 23.7, “Stored Program Binary Logging”](stored-programs-logging.md). For more information about row-based logging and row-based replication, see [Section 5.4.4.1, “Binary Logging Formats”](binary-log-formats.md), and [Section 16.2.1, “Replication Formats”](replication-formats.md).

For additional information specific to replication and `InnoDB`, see [Section 14.20, “InnoDB and MySQL Replication”](innodb-and-mysql-replication.md). For information relating to replication with NDB Cluster, see [Section 21.7, “NDB Cluster Replication”](mysql-cluster-replication.md).