---
title: "15.1.33 DROP LOGFILE GROUP Statement"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/drop-logfile-group.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.1.33 DROP LOGFILE GROUP Statement

```
DROP LOGFILE GROUP logfile_group
    ENGINE [=] engine_name
```

This statement drops the log file group named *`logfile_group`*. The log file group must already exist or an error results. (For information on creating log file groups, see [Section 15.1.20, “CREATE LOGFILE GROUP Statement”](create-logfile-group.md).)

Important

Before dropping a log file group, you must drop all tablespaces that use that log file group for `UNDO` logging.

The required `ENGINE` clause provides the name of the storage engine used by the log file group to be dropped. The only permitted values for *`engine_name`* are [`NDB`](mysql-cluster.md) and [`NDBCLUSTER`](mysql-cluster.md).

`DROP LOGFILE GROUP` is useful only with Disk Data storage for NDB Cluster. See [Section 25.6.11, “NDB Cluster Disk Data Tables”](mysql-cluster-disk-data.md).