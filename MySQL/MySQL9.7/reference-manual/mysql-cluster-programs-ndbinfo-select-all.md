---
title: "25.5.2 ndbinfo_select_all — Select From ndbinfo Tables"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/mysql-cluster-programs-ndbinfo-select-all.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 25.5.2 ndbinfo\_select\_all — Select From ndbinfo Tables

**ndbinfo\_select\_all** is a client program that selects all rows and columns from one or more tables in the [`ndbinfo`](mysql-cluster-ndbinfo.md) database

Not all `ndbinfo` tables available in the [**mysql**](mysql.md) client can be read by this program (see later in this section). In addition, **ndbinfo\_select\_all** can show information about some tables internal to `ndbinfo` which cannot be accessed using SQL, including the `tables` and `columns` metadata tables.

To select from one or more `ndbinfo` tables using **ndbinfo\_select\_all**, it is necessary to supply the names of the tables when invoking the program as shown here:

```
$> ndbinfo_select_all table_name1  [table_name2] [...]
```

For example:

```
$> ndbinfo_select_all logbuffers logspaces
== logbuffers ==
node_id log_type        log_id  log_part        total   used    high
5       0       0       0       33554432        262144  0
6       0       0       0       33554432        262144  0
7       0       0       0       33554432        262144  0
8       0       0       0       33554432        262144  0
== logspaces ==
node_id log_type        log_id  log_part        total   used    high
5       0       0       0       268435456       0       0
5       0       0       1       268435456       0       0
5       0       0       2       268435456       0       0
5       0       0       3       268435456       0       0
6       0       0       0       268435456       0       0
6       0       0       1       268435456       0       0
6       0       0       2       268435456       0       0
6       0       0       3       268435456       0       0
7       0       0       0       268435456       0       0
7       0       0       1       268435456       0       0
7       0       0       2       268435456       0       0
7       0       0       3       268435456       0       0
8       0       0       0       268435456       0       0
8       0       0       1       268435456       0       0
8       0       0       2       268435456       0       0
8       0       0       3       268435456       0       0
$>
```

Options that can be used with **ndbinfo\_select\_all** are shown in the following table. Additional descriptions follow the table.

- `--character-sets-dir`
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
	Directory containing character sets.
- `--core-file`
	| Command-Line Format | `--core-file` |
	| --- | --- |
	Write core file on error; used in debugging.
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
	| Command-Line Format | `--connect-string=connection-string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as `--ndb-connectstring`.
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
- `` --delay=`seconds` ``
	| Command-Line Format | `--delay=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `5` |
	| Minimum Value | `0` |
	| Maximum Value | `MAX_INT` |
	This option sets the number of seconds to wait between executing loops. Has no effect if `--loops` is set to 0 or 1.
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
- `--no-login-paths`
	| Command-Line Format | `--no-login-paths` |
	| --- | --- |
	Skips reading options from the login path file.
- `` --loops=`number` ``, ``-l *`number`*``
	| Command-Line Format | `--loops=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `1` |
	| Minimum Value | `0` |
	| Maximum Value | `MAX_INT` |
	This option sets the number of times to execute the select. Use `--delay` to set the time between loops.
- `--ndb-connectstring`
	| Command-Line Format | `--ndb-connectstring=connection-string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Set connection string for connecting to [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md). Syntax: ``[nodeid=*`id`*;][host=]*`hostname`*[:*`port`*]``. Overrides entries in `NDB_CONNECTSTRING` and `my.cnf`.
- `--ndb-mgmd-host`
	| Command-Line Format | `--ndb-mgmd-host=connection-string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as `--ndb-connectstring`.
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
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as --help.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

**ndbinfo\_select\_all** is unable to read the following tables: