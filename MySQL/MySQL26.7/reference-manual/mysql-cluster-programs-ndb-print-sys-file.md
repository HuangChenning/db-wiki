---
title: "MySQL :: MySQL 26.7 Reference Manual :: 25.5.21 ndb_print_sys_file — Print NDB System File Contents"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-cluster-programs-ndb-print-sys-file.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 25.5.21 ndb\_print\_sys\_file — Print NDB System File Contents

**ndb\_print\_sys\_file** obtains diagnostic information from an NDB Cluster system file.

#### Usage

```svg
ndb_print_sys_file file_name
```

*`file_name`* is the name of a cluster system file (sysfile). Cluster system files are located in a data node's data directory ([`DataDir`](mysql-cluster-ndbd-definition.md)); the path under this directory to system files matches the pattern ``ndb_*`#`*_fs/D*`#`*/DBDIH/P*`#`*.sysfile``. In each case, the *`#`* represents a number (not necessarily the same number). For more information, see [NDB Cluster Data Node File System Directory](https://dev.mysql.com/doc/ndb-internals/en/ndb-internals-ndbd-filesystemdir-files.html).

Like [**ndb\_print\_backup\_file**](mysql-cluster-programs-ndb-print-backup-file.md) and [**ndb\_print\_schema\_file**](mysql-cluster-programs-ndb-print-schema-file.md) (and unlike most of the other [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) [**ndb\_print\_backup\_file**](mysql-cluster-programs-ndb-print-backup-file.md) must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.

#### Additional Options

None.