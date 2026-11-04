---
title: "15.1.28 DROP LOGFILE GROUP Statement"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/drop-logfile-group.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 15.1.28 DROP LOGFILE GROUP Statement

```
DROP LOGFILE GROUP logfile_group
    ENGINE [=] engine_name
```

This statement drops the log file group named *`logfile_group`*. The log file group must already exist or an error results. (For information on creating log file groups, see [Section 15.1.16, “CREATE LOGFILE GROUP Statement”](create-logfile-group.md).)

Important

Before dropping a log file group, you must drop all tablespaces that use that log file group for `UNDO` logging.

The required `ENGINE` clause provides the name of the storage engine used by the log file group to be dropped. Currently, the only permitted values for *`engine_name`* are [`NDB`](mysql-cluster.md) and [`NDBCLUSTER`](mysql-cluster.md).

`DROP LOGFILE GROUP` is useful only with Disk Data storage for NDB Cluster. See [Section 25.6.11, “NDB Cluster Disk Data Tables”](mysql-cluster-disk-data.md).