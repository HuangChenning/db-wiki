---
title: "25.5.18 ndb_print_file — Print NDB Disk Data File Contents"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndb-print-file.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.18 ndb\_print\_file — Print NDB Disk Data File Contents

**ndb\_print\_file** obtains information from an NDB Cluster Disk Data file.

#### Usage

```
ndb_print_file [-v] [-q] file_name+
```

*`file_name`* is the name of an NDB Cluster Disk Data file. Multiple filenames are accepted, separated by spaces.

Like [**ndb\_print\_schema\_file**](mysql-cluster-programs-ndb-print-schema-file.md) and [**ndb\_print\_sys\_file**](mysql-cluster-programs-ndb-print-sys-file.md) (and unlike most of the other [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) **ndb\_print\_file** must be run on an NDB Cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.

#### Options

**Table 25.40 Command-line options used with the program ndb\_print\_file**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `--file-key=hex_data`,  `                  -K                 hex_data  ` | Supply encryption key using stdin, tty, or my.cnf file | ADDED: NDB 8.0.31 |
| `                  --file-key-from-stdin                  ` | Supply encryption key using stdin | ADDED: NDB 8.0.31 |
| `--help`,  `                  -?                  ` | Display help text and exit; same as --usage | (Supported in all NDB releases based on MySQL 8.0) |
| `--quiet`,  `                  -q                  ` | Reduce verbosity of output | (Supported in all NDB releases based on MySQL 8.0) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 8.0) |
| `--verbose`,  `                  -v                  ` | Increase verbosity of output | (Supported in all NDB releases based on MySQL 8.0) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 8.0) |

**ndb\_print\_file** supports the following options:

- `--file-key`, `-K`
	| Command-Line Format | `--file-key=hex_data` |
	| --- | --- |
	Supply file system encryption or decryption key from `stdin`, `tty`, or a `my.cnf` file.
- `--file-key-from-stdin`
	| Command-Line Format | `--file-key-from-stdin` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	| Valid Values | `TRUE` |
	Supply file system encryption or decryption key from `stdin`.
- `--help`, `-h`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Print help message and exit.
- `--quiet`, `-q`
	| Command-Line Format | `--quiet` |
	| --- | --- |
	Suppress output (quiet mode).
- `--usage`, `-?`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Print help message and exit.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Make output verbose.
- `--version`, `-v`
	| Command-Line Format | `--version` |
	| --- | --- |
	Print version information and exit.

For more information, see [Section 25.6.11, “NDB Cluster Disk Data Tables”](mysql-cluster-disk-data.md).