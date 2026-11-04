---
title: "21.5.21 ndb_print_schema_file — Print NDB Schema File Contents"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-print-schema-file.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.21 ndb\_print\_schema\_file — Print NDB Schema File Contents

**ndb\_print\_schema\_file** obtains diagnostic information from a cluster schema file.

#### Usage

```
ndb_print_schema_file file_name
```

*`file_name`* is the name of a cluster schema file. For more information about cluster schema files, see [NDB Cluster Data Node File System Directory](https://dev.mysql.com/doc/ndb-internals/en/ndb-internals-ndbd-filesystemdir-files.html).

Like [**ndb\_print\_backup\_file**](mysql-cluster-programs-ndb-print-backup-file.md) and [**ndb\_print\_sys\_file**](mysql-cluster-programs-ndb-print-sys-file.md) (and unlike most of the other [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) **ndb\_print\_schema\_file** must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.

#### Additional Options

None.