---
title: "25.5.22 ndb_redo_log_reader — Check and Print Content of Cluster Redo Log"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-cluster-programs-ndb-redo-log-reader.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 25.5.22 ndb\_redo\_log\_reader — Check and Print Content of Cluster Redo Log

Reads a redo log file, checking it for errors, printing its contents in a human-readable format, or both. **ndb\_redo\_log\_reader** is intended for use primarily by NDB Cluster developers and Support personnel in debugging and diagnosing problems.

This utility remains under development, and its syntax and behavior are subject to change in future NDB Cluster releases.

The C++ source files for **ndb\_redo\_log\_reader** can be found in the directory `/storage/ndb/src/kernel/blocks/dblqh/redoLogReader`.

Options that can be used with **ndb\_redo\_log\_reader** are shown in the following table. Additional descriptions follow the table.

#### Usage

```
ndb_redo_log_reader file_name [options]
```

*`file_name`* is the name of a cluster redo log file. redo log files are located in the numbered directories under the data node's data directory ([`DataDir`](mysql-cluster-ndbd-definition.md)); the path under this directory to the redo log files matches the pattern ``ndb_*`nodeid`*_fs/D*`#`*/DBLQH/S*`#`*.FragLog``. *`nodeid`* is the data node's node ID. The two instances of *`#`* each represent a number (not necessarily the same number); the number following `D` is in the range 8-39 inclusive; the range of the number following `S` varies according to the value of the [`NoOfFragmentLogFiles`](mysql-cluster-ndbd-definition.md) configuration parameter, whose default value is 16; thus, the default range of the number in the file name is 0-15 inclusive. For more information, see [NDB Cluster Data Node File System Directory](https://dev.mysql.com/doc/ndb-internals/en/ndb-internals-ndbd-filesystemdir-files.html).

The name of the file to be read may be followed by one or more of the options listed here:

- `-dump`
	| Command-Line Format | `-dump` |
	| --- | --- |
	Print dump info.
- `--file-key`, `-K`
	| Command-Line Format | `--file-key=key` |
	| --- | --- |
	Supply file decryption key using `stdin`, `tty`, or a `my.cnf` file.
- `--file-key-from-stdin`
	| Command-Line Format | `--file-key-from-stdin` |
	| --- | --- |
	Supply file decryption key using `stdin`.
- | Command-Line Format | `-filedescriptors` |
	| --- | --- |
	`-filedescriptors`: Print file descriptors only.
- | Command-Line Format | `--help` |
	| --- | --- |
	`--help`: Print usage information.
- `-lap`
	| Command-Line Format | `-lap` |
	| --- | --- |
	Provide lap info, with max GCI started and completed.
- | Command-Line Format | `-mbyte #` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `15` |
	``-mbyte             *`#`*``: Starting megabyte.
	*`#`* is an integer in the range 0 to 15, inclusive.
- | Command-Line Format | `-mbyteheaders` |
	| --- | --- |
	`-mbyteheaders`: Show only the first page header of every megabyte in the file.
- | Command-Line Format | `-noprint` |
	| --- | --- |
	`-noprint`: Do not print the contents of the log file.
- | Command-Line Format | `-nocheck` |
	| --- | --- |
	`-nocheck`: Do not check the log file for errors.
- | Command-Line Format | `-page #` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `31` |
	``-page             *`#`*``: Start at this page.
	*`#`* is an integer in the range 0 to 31, inclusive.
- | Command-Line Format | `-pageheaders` |
	| --- | --- |
	`-pageheaders`: Show page headers only.
- | Command-Line Format | `-pageindex #` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `12` |
	| Minimum Value | `12` |
	| Maximum Value | `8191` |
	``-pageindex             *`#`*``: Start at this page index.
	*`#`* is an integer between 12 and 8191, inclusive.
- `-twiddle`
	| Command-Line Format | `-twiddle` |
	| --- | --- |
	Bit-shifted dump.

Like [**ndb\_print\_backup\_file**](mysql-cluster-programs-ndb-print-backup-file.md) and [**ndb\_print\_schema\_file**](mysql-cluster-programs-ndb-print-schema-file.md) (and unlike most of the [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) **ndb\_redo\_log\_reader** must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.