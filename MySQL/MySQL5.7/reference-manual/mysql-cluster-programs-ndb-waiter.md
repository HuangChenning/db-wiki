---
title: "21.5.30 ndb_waiter — Wait for NDB Cluster to Reach a Given Status"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-waiter.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.30 ndb\_waiter — Wait for NDB Cluster to Reach a Given Status

**ndb\_waiter** repeatedly (each 100 milliseconds) prints out the status of all cluster data nodes until either the cluster reaches a given status or the `--timeout` limit is exceeded, then exits. By default, it waits for the cluster to achieve `STARTED` status, in which all nodes have started and connected to the cluster. This can be overridden using the `--no-contact` and `--not-started` options.

The node states reported by this utility are as follows:

- `NO_CONTACT`: The node cannot be contacted.
- `UNKNOWN`: The node can be contacted, but its status is not yet known. Usually, this means that the node has received a [`START`](mysql-cluster-mgm-client-commands.md) or [`RESTART`](mysql-cluster-mgm-client-commands.md) command from the management server, but has not yet acted on it.
- `NOT_STARTED`: The node has stopped, but remains in contact with the cluster. This is seen when restarting the node using the management client's `RESTART` command.
- `STARTING`: The node's [**ndbd**](mysql-cluster-programs-ndbd.md) process has started, but the node has not yet joined the cluster.
- `STARTED`: The node is operational, and has joined the cluster.
- `SHUTTING_DOWN`: The node is shutting down.
- `SINGLE USER MODE`: This is shown for all cluster data nodes when the cluster is in single user mode.

Options that can be used with **ndb\_waiter** are shown in the following table. Additional descriptions follow the table.

**Table 21.46 Command-line options used with the program ndb\_waiter**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 5.7) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --core-file                  ` | Write core file on error; used in debugging | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 5.7) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | (Supported in all NDB releases based on MySQL 5.7) |
| `--no-contact`,  `                  -n                  ` | Wait for cluster to reach NO CONTACT state | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --not-started                  ` | Wait for cluster to reach NOT STARTED state | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --nowait-nodes=list                  ` | List of nodes not to be waited for | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --single-user                  ` | Wait for cluster to enter single user mode | (Supported in all NDB releases based on MySQL 5.7) |
| `--timeout=#`,  `  -t                 #  ` | Wait this many seconds, then exit whether or not cluster has reached desired state | (Supported in all NDB releases based on MySQL 5.7) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 5.7) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `--wait-nodes=list`,  `  -w                 list  ` | List of nodes to be waited for | (Supported in all NDB releases based on MySQL 5.7) |

#### Usage

```
ndb_waiter [-c connection_string]
```

#### Additional Options

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
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
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
	Same as -- `ndb-connectstring`.
- `--ndb-nodeid`
	| Command-Line Format | `--ndb-nodeid=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Set node ID for this node, overriding any ID set by `--ndb-connectstring`.
- `--ndb-optimized-node-selection`
	| Command-Line Format | `--ndb-optimized-node-selection` |
	| --- | --- |
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--no-contact`, `-n`
	Instead of waiting for the `STARTED` state, **ndb\_waiter** continues running until the cluster reaches `NO_CONTACT` status before exiting.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- `--not-started`
	Instead of waiting for the `STARTED` state, **ndb\_waiter** continues running until the cluster reaches `NOT_STARTED` status before exiting.
- ``--nowait-nodes=*`list`*``
	When this option is used, **ndb\_waiter** does not wait for the nodes whose IDs are listed. The list is comma-delimited; ranges can be indicated by dashes, as shown here:
	```
	$> ndb_waiter --nowait-nodes=1,3,7-9
	```
	Important
	Do *not* use this option together with the `--wait-nodes` option.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- ``--timeout=*`seconds`*``, ``-t *`seconds`*``
	Time to wait. The program exits if the desired state is not achieved within this number of seconds. The default is 120 seconds (1200 reporting cycles).
- `--single-user`
	The program waits for the cluster to enter single user mode.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Display help text and exit; same as `--help`.
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.
- ``--wait-nodes=*`list`*``, ``-w *`list`*``
	When this option is used, **ndb\_waiter** waits only for the nodes whose IDs are listed. The list is comma-delimited; ranges can be indicated by dashes, as shown here:
	```
	$> ndb_waiter --wait-nodes=2,4-6,10
	```
	Important
	Do *not* use this option together with the `--nowait-nodes` option.

**Sample Output.** Shown here is the output from **ndb\_waiter** when run against a 4-node cluster in which two nodes have been shut down and then started again manually. Duplicate reports (indicated by `...`) are omitted.

```
$> ./ndb_waiter -c localhost

Connecting to mgmsrv at (localhost)
State node 1 STARTED
State node 2 NO_CONTACT
State node 3 STARTED
State node 4 NO_CONTACT
Waiting for cluster enter state STARTED

...

State node 1 STARTED
State node 2 UNKNOWN
State node 3 STARTED
State node 4 NO_CONTACT
Waiting for cluster enter state STARTED

...

State node 1 STARTED
State node 2 STARTING
State node 3 STARTED
State node 4 NO_CONTACT
Waiting for cluster enter state STARTED

...

State node 1 STARTED
State node 2 STARTING
State node 3 STARTED
State node 4 UNKNOWN
Waiting for cluster enter state STARTED

...

State node 1 STARTED
State node 2 STARTING
State node 3 STARTED
State node 4 STARTING
Waiting for cluster enter state STARTED

...

State node 1 STARTED
State node 2 STARTED
State node 3 STARTED
State node 4 STARTING
Waiting for cluster enter state STARTED

...

State node 1 STARTED
State node 2 STARTED
State node 3 STARTED
State node 4 STARTED
Waiting for cluster enter state STARTED
```

Note

If no connection string is specified, then **ndb\_waiter** tries to connect to a management on `localhost`, and reports `Connecting to mgmsrv at (null)`.

Prior to NDB 7.5.18 and 7.6.14, this program printed ``NDBT_ProgramExit -         *`status`*`` upon completion of its run, due to an unnecessary dependency on the `NDBT` testing library. This dependency is has now been removed, eliminating the extraneous output.