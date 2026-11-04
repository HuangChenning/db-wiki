---
title: "25.5.27 ndb_show_tables — Display List of NDB Tables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndb-show-tables.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.27 ndb\_show\_tables — Display List of NDB Tables

**ndb\_show\_tables** displays a list of all [`NDB`](mysql-cluster.md) database objects in the cluster. By default, this includes not only both user-created tables and [`NDB`](mysql-cluster.md) system tables, but [`NDB`](mysql-cluster.md) -specific indexes, internal triggers, and NDB Cluster Disk Data objects as well.

Options that can be used with **ndb\_show\_tables** are shown in the following table. Additional descriptions follow the table.

**Table 25.48 Command-line options used with the program ndb\_show\_tables**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | REMOVED: 8.0.31 |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 8.0) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --core-file                  ` | Write core file on error; used in debugging | REMOVED: 8.0.31 |
| `--database=name`,  `                  -d                 name  ` | Specifies database in which table is found; database name must be followed by table name | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 8.0) |
| `--loops=#`,  `  -l                 #  ` | Number of times to repeat output | (Supported in all NDB releases based on MySQL 8.0) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | REMOVED: 8.0.31 |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 8.0) |
| `--parsable`,  `                  -p                  ` | Return output suitable for MySQL LOAD DATA statement | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --show-temp-status                  ` | Show table temporary flag | (Supported in all NDB releases based on MySQL 8.0) |
| `--type=#`,  `  -t                 #  ` | Limit output to objects of this type | (Supported in all NDB releases based on MySQL 8.0) |
| `--unqualified`,  `                  -u                  ` | Do not qualify table names | (Supported in all NDB releases based on MySQL 8.0) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 8.0) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 8.0) |

#### Usage

```
ndb_show_tables [-c connection_string]
```

- `--character-sets-dir`
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
	Same as `--ndb-connectstring`.
- `--core-file`
	Write core file on error; used in debugging.
- `--database`, `-d`
	Specifies the name of the database in which the desired table is found. If this option is given, the name of a table must follow the database name.
	If this option has not been specified, and no tables are found in the `TEST_DB` database, **ndb\_show\_tables** issues a warning.
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
- `--loops`, `-l`
	Specifies the number of times the utility should execute. This is 1 when this option is not specified, but if you do use the option, you must supply an integer argument for it.
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
	Same as `--ndb-connectstring`.
- `--ndb-nodeid`
	| Command-Line Format | `--ndb-nodeid=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Set node ID for this node, overriding any ID set by `--ndb-connectstring`.
- `--ndb-optimized-node-selection`
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--parsable`, `-p`
	Using this option causes the output to be in a format suitable for use with [`LOAD             DATA`](load-data.md).
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--show-temp-status`
	If specified, this causes temporary tables to be displayed.
- `--type`, `-t`
	Can be used to restrict the output to one type of object, specified by an integer type code as shown here:
	- `1`: System table
	- `2`: User-created table
	- `3`: Unique hash index
	Any other value causes all [`NDB`](mysql-cluster.md) database objects to be listed (the default).
- `--unqualified`, `-u`
	If specified, this causes unqualified object names to be displayed.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

Note

Only user-created NDB Cluster tables may be accessed from MySQL; system tables such as `SYSTAB_0` are not visible to [**mysqld**](mysqld.md). However, you can examine the contents of system tables using [`NDB`](mysql-cluster.md) API applications such as [**ndb\_select\_all**](mysql-cluster-programs-ndb-select-all.md) (see [Section 25.5.25, “ndb\_select\_all — Print Rows from an NDB Table”](mysql-cluster-programs-ndb-select-all.md)).

Prior to NDB 8.0.20, this program printed ``NDBT_ProgramExit -         *`status`*`` upon completion of its run, due to an unnecessary dependency on the `NDBT` testing library. This dependency has been removed, eliminating the extraneous output.