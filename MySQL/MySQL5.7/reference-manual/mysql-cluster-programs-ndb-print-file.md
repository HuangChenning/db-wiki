---
title: "21.5.19 ndb_print_file — Print NDB Disk Data File Contents"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-print-file.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.19 ndb\_print\_file — Print NDB Disk Data File Contents

**ndb\_print\_file** obtains information from an NDB Cluster Disk Data file.

#### Usage

```
ndb_print_file [-v] [-q] file_name+
```

*`file_name`* is the name of an NDB Cluster Disk Data file. Multiple filenames are accepted, separated by spaces.

Like [**ndb\_print\_schema\_file**](mysql-cluster-programs-ndb-print-schema-file.md) and [**ndb\_print\_sys\_file**](mysql-cluster-programs-ndb-print-sys-file.md) (and unlike most of the other [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) **ndb\_print\_file** must be run on an NDB Cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.

#### Additional Options

**ndb\_print\_file** supports the following options:

- `-v`: Make output verbose.
- `-q`: Suppress output (quiet mode).
- `--help`, `-h`, `-?`: Print help message.

For more information, see [Section 21.6.11, “NDB Cluster Disk Data Tables”](mysql-cluster-disk-data.md).