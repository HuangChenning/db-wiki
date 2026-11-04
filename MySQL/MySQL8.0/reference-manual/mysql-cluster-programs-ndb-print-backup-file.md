---
title: "25.5.17 ndb_print_backup_file — Print NDB Backup File Contents"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndb-print-backup-file.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.17 ndb\_print\_backup\_file — Print NDB Backup File Contents

**ndb\_print\_backup\_file** obtains diagnostic information from a cluster backup file.

**Table 25.39 Command-line options used with the program ndb\_print\_backup\_file**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `--backup-key=key`,  `                  -K                 password  ` | Use this password to decrypt file | ADDED: NDB 8.0.31 |
| `                  --backup-key-from-stdin                  ` | Get decryption key in a secure fashion from STDIN | ADDED: NDB 8.0.31 |
| `--backup-password=password`,  `                  -P                 password  ` | Use this password to decrypt file | ADDED: NDB 8.0.22 |
| `                  --backup-password-from-stdin                  ` | Get decryption password in a secure fashion from STDIN | ADDED: NDB 8.0.24 |
| `--control-directory-number=#`,  `                  -c                 #  ` | Control directory number | ADDED: NDB 8.0.24 |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 8.0) |
| `--fragment-id=#`,  `                  -f                 #  ` | Fragment ID | ADDED: NDB 8.0.24 |
| `--help`,  `--usage`,  `-h`,  `                  -?                  ` | Print usage information | ADDED: NDB 8.0.24 |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 8.0) |
| `--no-print-rows`,  `                  -u                  ` | Do not print rows | ADDED: NDB 8.0.24 |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `--print-header-words`,  `                  -h                  ` | Print header words | ADDED: NDB 8.0.24 |
| `                  --print-restored-rows                  ` | Print restored rows | ADDED: NDB 8.0.24 |
| `--print-rows`,  `                  -U                  ` | Print rows. Enabled by default; disable with --no-print-rows | ADDED: NDB 8.0.24 |
| `                  --print-rows-per-page                  ` | Print rows per page | ADDED: NDB 8.0.24 |
| `--rowid-file=path`,  `                  -n                 path  ` | File containing row ID to check for | ADDED: NDB 8.0.24 |
| `--show-ignored-rows`,  `                  -i                  ` | Show ignored rows | ADDED: NDB 8.0.24 |
| `--table-id=#`,  `                  -t                 #  ` | Table ID; used with --print-restored rows | ADDED: NDB 8.0.24 |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 8.0) |
| `--verbose[=#]`,  `                  -v                  ` | Verbosity level | ADDED: NDB 8.0.24 |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 8.0) |

#### Usage

```
ndb_print_backup_file [-P password] file_name
```

*`file_name`* is the name of a cluster backup file. This can be any of the files (`.Data`, `.ctl`, or `.log` file) found in a cluster backup directory. These files are found in the data node's backup directory under the subdirectory ``BACKUP-*`#`*``, where *`#`* is the sequence number for the backup. For more information about cluster backup files and their contents, see [Section 25.6.8.1, “NDB Cluster Backup Concepts”](mysql-cluster-backup-concepts.md).

Like [**ndb\_print\_schema\_file**](mysql-cluster-programs-ndb-print-schema-file.md) and [**ndb\_print\_sys\_file**](mysql-cluster-programs-ndb-print-sys-file.md) (and unlike most of the other [`NDB`](mysql-cluster.md) utilities that are intended to be run on a management server host or to connect to a management server) **ndb\_print\_backup\_file** must be run on a cluster data node, since it accesses the data node file system directly. Because it does not make use of the management server, this utility can be used when the management server is not running, and even when the cluster has been completely shut down.

In NDB 8.0, this program can also be used to read undo log files.

#### Options

Prior to NDB 8.0.24, **ndb\_print\_backup\_file** supported only the `-P` option. Beginning with NDB 8.0.24, the program supports a number of options, which are described in the following list.

- `--backup-key`, `-K`
	| Command-Line Format | `--backup-key=key` |
	| --- | --- |
	Specify the key needed to decrypt an encrypted backup.
- `--backup-key-from-stdin`
	| Command-Line Format | `--backup-key-from-stdin` |
	| --- | --- |
	Allow input of the decryption key from standard input, similar to entering a password after invoking [**mysql**](mysql.md) [`--password`](mysql-command-options.md) with no password supplied.
- `--backup-password`
	| Command-Line Format | `--backup-password=password` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Specify the password needed to decrypt an encrypted backup.
	The long form of this option is available beginning with NDB 8.0.24.
- `--backup-password-from-stdin`
	| Command-Line Format | `--backup-password-from-stdin` |
	| --- | --- |
	Allow input of the password from standard input, similar to entering a password after invoking [**mysql**](mysql.md) [`--password`](mysql-command-options.md) with no password supplied.
- `--control-directory-number`
	| Command-Line Format | `--control-directory-number=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	Control file directory number. Used together with `--print-restored-rows`.
- `--defaults-extra-file`
	| Command-Line Format | `--defaults-extra-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given file after global files are read.
- `--defaults-file`
	| Command-Line Format | `--defaults-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read default options from given file only.
- `--defaults-group-suffix`
	| Command-Line Format | `--defaults-group-suffix=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Also read groups with concat(group, suffix).
- `--fragment-id`
	| Command-Line Format | `--fragment-id=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	Fragment ID. Used together with `--print-restored-rows`.
- `--help`
	| Command-Line Format | `--help`  `--usage` |
	| --- | --- |
	Print program usage information.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--no-print-rows`
	| Command-Line Format | `--no-print-rows` |
	| --- | --- |
	Do not include rows in output.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--print-header-words`
	| Command-Line Format | `--print-header-words` |
	| --- | --- |
	Include header words in output.
- `--print-restored-rows`
	| Command-Line Format | `--print-restored-rows` |
	| --- | --- |
	Include restored rows in output, using the file ``LCP/*`c`*/T*`t`*F*`f`*.ctl``, for which the values are set as follows:
	- *`c`* is the control file number set using `--control-directory-number`
	- *`t`* is the table ID set using `--table-id`
	- *`f`* is the fragment ID set using `--fragment-id`
- `--print-rows`
	| Command-Line Format | `--print-rows` |
	| --- | --- |
	Print rows. This option is enabled by default; to disable it, use `--no-print-rows`.
- `--print-rows-per-page`
	| Command-Line Format | `--print-rows-per-page` |
	| --- | --- |
	Print rows per page.
- `--rowid-file`
	| Command-Line Format | `--rowid-file=path` |
	| --- | --- |
	| Type | File name |
	| Default Value | `[none]` |
	File to check for row ID.
- `--show-ignored-rows`
	| Command-Line Format | `--show-ignored-rows` |
	| --- | --- |
	Show ignored rows.
- `--table-id`
	| Command-Line Format | `--table-id=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Table ID. Used together with `--print-restored-rows`.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--verbose`
	| Command-Line Format | `--verbose[=#]` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	Verbosity level of output. A greater value indicates increased verbosity.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.