---
title: "25.5.5 ndb_mgm — The NDB Cluster Management Client"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-cluster-programs-ndb-mgm.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

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

- [`--backup-password-from-stdin[=TRUE|FALSE]`](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/mysql-cluster-programs-ndb-mgm.html#option_ndb_mgm_backup-password-from-stdin)
	| Command-Line Format | `--backup-password-from-stdin` |
	| --- | --- |
	This option enables input of the backup password from the system shell (`stdin`) when using `--execute "START BACKUP"` or similar to create a backup. Use of this option requires use of `--execute` as well.
- `--character-sets-dir`
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
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
	| Command-Line Format | `--core-file` |
	| --- | --- |
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
- `--no-login-paths`
	| Command-Line Format | `--no-login-paths` |
	| --- | --- |
	Skips reading options from the login path file.
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
- `--ndb-mgm-tls`
	| Command-Line Format | `--ndb-mgm-tls=level` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `relaxed` |
	| Valid Values | `relaxed`  `strict` |
	Sets the level of TLS support required to connect to the management server; one of `relaxed` or `strict`. `relaxed` (the default) means that a TLS connection is attempted, but success is not required; `strict` means that TLS is required to connect.
- `--ndb-mgmd-host`
	| Command-Line Format | `--ndb-mgmd-host=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Same as `--ndb-connectstring`.
- `--ndb-optimized-node-selection`
	| Command-Line Format | `--ndb-optimized-node-selection` |
	| --- | --- |
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--ndb-tls-search-path`
	| Command-Line Format | `--ndb-tls-search-path=list` |
	| --- | --- |
	| Type | Path name |
	| Default Value (Unix) | `$HOME/ndb-tls` |
	| Default Value (Windows) | `$HOMEDIR/ndb-tls` |
	Specify a list of directories to search for a CA file. On Unix platforms, the directory names are separated by colons (`:`); on Windows systems, the semicolon character (`;`) is used as the separator. A directory reference may be relative or absolute; it may contain one or more environment variables, each denoted by a prefixed dollar sign (`$`), and expanded prior to use.
	Searching begins with the leftmost named directory and proceeds from left to right until a file is found. An empty string denotes an empty search path, which causes all searches to fail. A string consisting of a single dot (`.`) indicates that the search path limited to the current working directory.
	If no search path is supplied, the compiled-in default value is used. This value depends on the platform used: On Windows, this is `\ndb-tls`; on other platforms (including Linux), it is `$HOME/ndb-tls`. This can be overridden by compiling NDB Cluster using [`-DWITH_NDB_TLS_SEARCH_PATH`](source-configuration-options.md).
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- `--test-tls`
	| Command-Line Format | `--test-tls` |
	| --- | --- |
	Connect using TLS, then exit. Output if successful is similar to what is shown here:
	```
	>$ ndb_mgm --test-tls
	Connected to Management Server at: sakila:1186
	>$
	```
	See [Section 25.6.19.5, “TLS Link Encryption for NDB Cluster”](mysql-cluster-tls.md), for more information.
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