---
title: "21.5.18 ndb_print_backup_file — Print NDB Backup File Contents"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-print-backup-file.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.18 ndb\_print\_backup\_file — Print NDB Backup File Contents

**ndb\_print\_backup\_file** obtains diagnostic information from a cluster backup file.

#### Usage

```
ndb_print_backup_file file_name
```

*`file_name`* is the name of a cluster backup file. This can be any of the files (`.Data`, `.ctl`, or `.log` file) found in a cluster backup directory. These files are found in the data node's backup directory under the subdirectory ``BACKUP-*`#`*``, where *`#`* is the sequence number for the backup. For more information about cluster backup files and their contents, see [Section 21.6.8.1, “NDB Cluster Backup Concepts”](mysql-cluster-backup-concepts.md).

Like [**ndb\_print\_schema\_file**](mysql-cluster-programs-ndb-print-schema-file.md) and [**ndb\_print\_sys\_file**](mysql-cluster-programs-ndb-print-sys-file.md) (and unlike most of the other [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) **ndb\_print\_backup\_file** must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.

#### Additional Options

None.