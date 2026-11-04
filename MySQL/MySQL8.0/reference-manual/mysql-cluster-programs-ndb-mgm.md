---
title: "25.5.5 ndb_mgm — The NDB Cluster Management Client"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndb-mgm.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 25.5.5 ndb\_mgm — The NDB Cluster Management Client

The **ndb\_mgm** management client process is actually not needed to run the cluster. Its value lies in providing a set of commands for checking the cluster's status, starting backups, and performing other administrative functions. The management client accesses the management server using a C API. Advanced users can also employ this API for programming dedicated management processes to perform tasks similar to those performed by **ndb\_mgm**.

To start the management client, it is necessary to supply the host name and port number of the management server:

```
$> ndb_mgm [host_name [port_num]]
```

For example:

```
$> ndb_mgm ndb_mgmd.mysql.com 1186
```

The default host name and port number are `localhost` and 1186, respectively.

All options that can be used with **ndb\_mgm** are shown in the following table. Additional descriptions follow the table.

**Table 25.27 Command-line options used with the program ndb\_mgm**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --backup-password-from-stdin                  ` | Get decryption password in a secure fashion from STDIN; use together with --execute and ndb\_mgm START BACKUP command | ADDED: NDB 8.0.24 |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | REMOVED: 8.0.31 |
| `                  --connect-retries=#                  ` | Set number of times to retry connection before giving up; 0 means 1 attempt only (and no retries) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 8.0) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --core-file                  ` | Write core file on error; used in debugging | REMOVED: 8.0.31 |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --encrypt-backup                  ` | Cause START BACKUP to encrypt whenever making a backup, prompting for password if not supplied by user | ADDED: NDB 8.0.24 |
| `--execute=command`,  `  -e                 command  ` | Execute command and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `--help`,  `  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 8.0) |
| `--ndb-mgmd-host=connection_string`,  `  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | REMOVED: 8.0.31 |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 8.0) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 8.0) |
| `--try-reconnect=#`,  `  -t                 #  ` | Set number of times to retry connection before giving up; synonym for --connect-retries | (Supported in all NDB releases based on MySQL 8.0) |
| `--usage`,  `  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 8.0) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 8.0) |

- [`--backup-password-from-stdin[=TRUE|FALSE]`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/mysql-cluster-programs-ndb-mgm.html#option_ndb_mgm_backup-password-from-stdin)
	| Command-Line Format | `--backup-password-from-stdin` |
	| --- | --- |
	This option enables input of the backup password from the system shell (`stdin`) when using `--execute "START BACKUP"` or similar to create a backup. Use of this option requires use of `--execute` as well.
- `--character-sets-dir`
	Directory containing character sets.
- ``--connect-retries=*`#`*``
	| Command-Line Format | `--connect-retries=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `3` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	This option specifies the number of times following the first attempt to retry a connection before giving up (the client always tries the connection at least once). The length of time to wait per attempt is set using [`--connect-retry-delay`](mysql-cluster-programs-ndb-mgmd.md).
	This option is synonymous with the `--try-reconnect` option, which is now deprecated.
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
- `--encrypt-backup`
	| Command-Line Format | `--encrypt-backup` |
	| --- | --- |
	When used, this option causes all backups to be encrypted. To make this happen whenever **ndb\_mgm** is run, put the option in the `[ndb_mgm]` section of the `my.cnf` file.
- `` --execute=`command` ``, `` -e `command` ``
	| Command-Line Format | `--execute=command` |
	| --- | --- |
	This option can be used to send a command to the NDB Cluster management client from the system shell. For example, either of the following is equivalent to executing [`SHOW`](mysql-cluster-mgm-client-commands.md) in the management client:
	```
	$> ndb_mgm -e "SHOW"
	$> ndb_mgm --execute="SHOW"
	```
	This is analogous to how the [`--execute`](mysql-command-options.md) or `-e` option works with the [**mysql**](mysql.md) command-line client. See [Section 6.2.2.1, “Using Options on the Command Line”](command-line-options.md).
	Note
	If the management client command to be passed using this option contains any space characters, then the command *must* be enclosed in quotation marks. Either single or double quotation marks may be used. If the management client command contains no space characters, the quotation marks are optional.
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
	Set connect string for connecting to [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md). Syntax: \[``nodeid=*`id`*;``\]\[`host=`\] ``*`hostname`*`` \[``:*`port`*``\]. Overrides entries in `NDB_CONNECTSTRING` and `my.cnf`.
- `--ndb-nodeid`
	| Command-Line Format | `--ndb-nodeid=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Set node ID for this node, overriding any ID set by `--ndb-connectstring`.
- `--ndb-mgmd-host`
	| Command-Line Format | `--ndb-mgmd-host=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as `--ndb-connectstring`.
- `--ndb-optimized-node-selection`
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- ``--try-reconnect=*`number`*``
	| Command-Line Format | `--try-reconnect=#` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Numeric |
	| Type | Integer |
	| Default Value | `12` |
	| Default Value | `3` |
	| Minimum Value | `0` |
	| Maximum Value | `4294967295` |
	If the connection to the management server is broken, the node tries to reconnect to it every 5 seconds until it succeeds. By using this option, it is possible to limit the number of attempts to *`number`* before giving up and reporting an error instead.
	This option is deprecated and subject to removal in a future release. Use `--connect-retries`, instead.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.

Additional information about using **ndb\_mgm** can be found in [Section 25.6.1, “Commands in the NDB Cluster Management Client”](mysql-cluster-mgm-client-commands.md).