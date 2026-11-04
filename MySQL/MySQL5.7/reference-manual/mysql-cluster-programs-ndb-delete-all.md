---
title: "21.5.9 ndb_delete_all — Delete All Rows from an NDB Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-delete-all.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.9 ndb\_delete\_all — Delete All Rows from an NDB Table

**ndb\_delete\_all** deletes all rows from the given [`NDB`](mysql-cluster.md) table. In some cases, this can be much faster than [`DELETE`](delete.md) or even [`TRUNCATE TABLE`](truncate-table.md).

#### Usage

```
ndb_delete_all -c connection_string tbl_name -d db_name
```

This deletes all rows from the table named *`tbl_name`* in the database named *`db_name`*. It is exactly equivalent to executing ``TRUNCATE         *`db_name`*.*`tbl_name`*`` in MySQL.

Options that can be used with **ndb\_delete\_all** are shown in the following table. Additional descriptions follow the table.

**Table 21.28 Command-line options used with the program ndb\_delete\_all**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 5.7) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --core-file                  ` | Write core file on error; used in debugging | (Supported in all NDB releases based on MySQL 5.7) |
| `--database=name`,  `-d name` | Name of the database in which the table is found | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 5.7) |
| `--diskscan` | Perform disk scan | (Supported in all NDB releases based on MySQL 5.7) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `--transactional`,  `                  -t                  ` | Perform delete in one single transaction; possible to run out of operations when used | (Supported in all NDB releases based on MySQL 5.7) |
| `--tupscan` | Perform tuple scan | (Supported in all NDB releases based on MySQL 5.7) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 5.7) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 5.7) |

- `--character-sets-dir`
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
	Directory containing character sets.
- `--connect-retries`
	| Command-Line Format | `--connect-retries=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `12` |
	| Minimum Value | `0` |
	| Maximum Value | `12` |
	Number of times to retry connection before giving up.
- `--connect-retry-delay`
	| Command-Line Format | `--connect-retry-delay=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `5` |
	| Minimum Value | `0` |
	| Maximum Value | `5` |
	Number of seconds to wait between attempts to contact management server.
- `--connect-string`
	| Command-Line Format | `--connect-string=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as --ndb-connectstring.
- `--core-file`
	| Command-Line Format | `--core-file` |
	| --- | --- |
	Write core file on error; used in debugging.
- `--database`, `-d`
	| Command-Line Format | `--database=name` |
	| --- | --- |
	| Type | String |
	| Default Value | `TEST_DB` |
	Name of the database containing the table to delete from.
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
- `--diskscan`
	| Command-Line Format | `--diskscan` |
	| --- | --- |
	Run a disk scan.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--ndb-connectstring`
	| Command-Line Format | `--ndb-connectstring=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf.
- `--ndb-mgmd-host`
	| Command-Line Format | `--ndb-mgmd-host=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as --ndb-connectstring.
- `--ndb-nodeid`
	| Command-Line Format | `--ndb-nodeid=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Set node ID for this node, overriding any ID set by --ndb-connectstring.
- `--ndb-optimized-node-selection`
	| Command-Line Format | `--ndb-optimized-node-selection` |
	| --- | --- |
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--transactional`, `-t`
	Use of this option causes the delete operation to be performed as a single transaction.
	Warning
	With very large tables, using this option may cause the number of operations available to the cluster to be exceeded.
- `--tupscan`
	Run a tuple scan.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as --help.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.