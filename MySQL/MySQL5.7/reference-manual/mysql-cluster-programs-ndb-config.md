---
title: "21.5.7 ndb_config — Extract NDB Cluster Configuration Information"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-programs-ndb-config.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.5.7 ndb\_config — Extract NDB Cluster Configuration Information

This tool extracts current configuration information for data nodes, SQL nodes, and API nodes from one of a number of sources: an NDB Cluster management node, or its `config.ini` or `my.cnf` file. By default, the management node is the source for the configuration data; to override the default, execute ndb\_config with the `--config-file` or `--mycnf` option. It is also possible to use a data node as the source by specifying its node ID with ``--config_from_node=*`node_id`*``.

**ndb\_config** can also provide an offline dump of all configuration parameters which can be used, along with their default, maximum, and minimum values and other information. The dump can be produced in either text or XML format; for more information, see the discussion of the `--configinfo` and `--xml` options later in this section).

You can filter the results by section (`DB`, `SYSTEM`, or `CONNECTIONS`) using one of the options `--nodes`, `--system`, or `--connections`.

Options that can be used with **ndb\_config** are shown in the following table. Additional descriptions follow the table.

**Table 21.27 Command-line options used with the program ndb\_config**

| Format | Description | Added, Deprecated, or Removed |
| --- | --- | --- |
| `                  --character-sets-dir=path                  ` | Directory containing character sets | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --config-file=file_name                  ` | Set the path to config.ini file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --config-from-node=#                  ` | Obtain configuration data from the node having this ID (must be a data node) | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --configinfo                  ` | Dumps information about all NDB configuration parameters in text format with default, maximum, and minimum values. Use with --xml to obtain XML output | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connections                  ` | Print information only about connections specified in \[tcp\], \[tcp default\], \[sci\], \[sci default\], \[shm\], or \[shm default\] sections of cluster configuration file. Cannot be used with --system or --nodes | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retries=#                  ` | Number of times to retry connection before giving up | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --connect-retry-delay=#                  ` | Number of seconds to wait between attempts to contact management server | (Supported in all NDB releases based on MySQL 5.7) |
| `--connect-string=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --core-file                  ` | Write core file on error; used in debugging | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-extra-file=path                  ` | Read given file after global files are read | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-file=path                  ` | Read default options from given file only | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --defaults-group-suffix=string                  ` | Also read groups with concat(group, suffix) | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --diff-default                  ` | Print only configuration parameters that have non-default values | ADDED: NDB 7.5.7, NDB 7.6.3 |
| `--fields=string`,  `                  -f                  ` | Field separator | (Supported in all NDB releases based on MySQL 5.7) |
| `--help`,  `                  -?                  ` | Display help text and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --host=name                  ` | Specify host | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --login-path=path                  ` | Read given path from login file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --mycnf                  ` | Read configuration data from my.cnf file | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-connectstring=connection_string`,  `                  -c                 connection_string  ` | Set connect string for connecting to ndb\_mgmd. Syntax: "\[nodeid=id;\]\[host=\]hostname\[:port\]". Overrides entries in NDB\_CONNECTSTRING and my.cnf | (Supported in all NDB releases based on MySQL 5.7) |
| `--ndb-mgmd-host=connection_string`,  `                  -c                 connection_string  ` | Same as --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-nodeid=#                  ` | Set node ID for this node, overriding any ID set by --ndb-connectstring | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --ndb-optimized-node-selection                  ` | Enable optimizations for selection of nodes for transactions. Enabled by default; use --skip-ndb-optimized-node-selection to disable | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --no-defaults                  ` | Do not read default options from any option file other than login file | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --nodeid=#                  ` | Get configuration of node with this ID | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --nodes                  ` | Print node information (\[ndbd\] or \[ndbd default\] section of cluster configuration file) only. Cannot be used with --system or --connections | (Supported in all NDB releases based on MySQL 5.7) |
| `--query=string`,  `  -q                 string  ` | One or more query options (attributes) | (Supported in all NDB releases based on MySQL 5.7) |
| `--query-all`,  `                  -a                  ` | Dumps all parameters and values to a single comma-delimited string | ADDED: NDB 7.4.16, NDB 7.5.7 |
| `                  --print-defaults                  ` | Print program argument list and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `--rows=string`,  `  -r                 string  ` | Row separator | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --system                  ` | Print SYSTEM section information only (see ndb\_config --configinfo output). Cannot be used with --nodes or --connections | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --type=name                  ` | Specify node type | (Supported in all NDB releases based on MySQL 5.7) |
| `--usage`,  `                  -?                  ` | Display help text and exit; same as --help | (Supported in all NDB releases based on MySQL 5.7) |
| `--version`,  `                  -V                  ` | Display version information and exit | (Supported in all NDB releases based on MySQL 5.7) |
| `                  --configinfo                 --xml  ` | Use --xml with --configinfo to obtain a dump of all NDB configuration parameters in XML format with default, maximum, and minimum values | (Supported in all NDB releases based on MySQL 5.7) |

- `--character-sets-dir`
	| Command-Line Format | `--character-sets-dir=path` |
	| --- | --- |
	Directory containing character sets.
- `--configinfo`
	The `--configinfo` option causes **ndb\_config** to dump a list of each NDB Cluster configuration parameter supported by the NDB Cluster distribution of which **ndb\_config** is a part, including the following information:
	- A brief description of each parameter's purpose, effects, and usage
	- The section of the `config.ini` file where the parameter may be used
	- The parameter's data type or unit of measurement
	- Where applicable, the parameter's default, minimum, and maximum values
	- NDB Cluster release version and build information
	By default, this output is in text format. Part of this output is shown here:
	```
	$> ndb_config --configinfo
	****** SYSTEM ******
	Name (String)
	Name of system (NDB Cluster)
	MANDATORY
	PrimaryMGMNode (Non-negative Integer)
	Node id of Primary ndb_mgmd(MGM) node
	Default: 0 (Min: 0, Max: 4294967039)
	ConfigGenerationNumber (Non-negative Integer)
	Configuration generation number
	Default: 0 (Min: 0, Max: 4294967039)
	****** DB ******
	MaxNoOfSubscriptions (Non-negative Integer)
	Max no of subscriptions (default 0 == MaxNoOfTables)
	Default: 0 (Min: 0, Max: 4294967039)
	MaxNoOfSubscribers (Non-negative Integer)
	Max no of subscribers (default 0 == 2 * MaxNoOfTables)
	Default: 0 (Min: 0, Max: 4294967039)
	…
	```
	Use this option together with the `--xml` option to obtain output in XML format.
- ``--config-file=*`path-to-file`*``
	| Command-Line Format | `--config-file=file_name` |
	| --- | --- |
	| Type | File name |
	| Default Value |  |
	Gives the path to the management server's configuration file (`config.ini`). This may be a relative or absolute path. If the management node resides on a different host from the one on which **ndb\_config** is invoked, then an absolute path must be used.
- `--config_from_node=#`
	| Command-Line Format | `--config-from-node=#` |
	| --- | --- |
	| Type | Numeric |
	| Default Value | `none` |
	| Minimum Value | `1` |
	| Maximum Value | `48` |
	Obtain the cluster's configuration data from the data node that has this ID.
	If the node having this ID is not a data node, **ndb\_config** fails with an error. (To obtain configuration data from the management node instead, simply omit this option.)
- `--connections`
	| Command-Line Format | `--connections` |
	| --- | --- |
	Tells **ndb\_config** to print `CONNECTIONS` information only—that is, information about parameters found in the `[tcp]`, `[tcp default]`, `[shm]`, or `[shm             default]` sections of the cluster configuration file (see [Section 21.4.3.10, “NDB Cluster TCP/IP Connections”](mysql-cluster-tcp-definition.md), and [Section 21.4.3.12, “NDB Cluster Shared Memory Connections”](mysql-cluster-shm-definition.md), for more information).
	This option is mutually exclusive with `--nodes` and `--system`; only one of these 3 options can be used.
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
- `--diff-default`
	| Command-Line Format | `--diff-default` |
	| --- | --- |
	Print only configuration parameters that have non-default values.
- ``--fields=*`delimiter`*``, `-f` *`delimiter`*
	| Command-Line Format | `--fields=string` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Specifies a *`delimiter`* string used to separate the fields in the result. The default is `,` (the comma character).
	Note
	If the *`delimiter`* contains spaces or escapes (such as `\n` for the linefeed character), then it must be quoted.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display help text and exit.
- ``--host=*`hostname`*``
	| Command-Line Format | `--host=name` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Specifies the host name of the node for which configuration information is to be obtained.
	Note
	While the hostname `localhost` usually resolves to the IP address `127.0.0.1`, this may not necessarily be true for all operating platforms and configurations. This means that it is possible, when `localhost` is used in `config.ini`, for **ndb\_config `--host=localhost`** to fail if **ndb\_config** is run on a different host where `localhost` resolves to a different address (for example, on some versions of SUSE Linux, this is `127.0.0.2`). In general, for best results, you should use numeric IP addresses for all NDB Cluster configuration values relating to hosts, or verify that all NDB Cluster hosts handle `localhost` in the same fashion.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read given path from login file.
- `--mycnf`
	| Command-Line Format | `--mycnf` |
	| --- | --- |
	Read configuration data from the `my.cnf` file.
- ``--ndb-connectstring=*`connection_string`*``, ``-c             *`connection_string`*``
	| Command-Line Format | `--ndb-connectstring=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Specifies the connection string to use in connecting to the management server. The format for the connection string is the same as described in [Section 21.4.3.3, “NDB Cluster Connection Strings”](mysql-cluster-connection-strings.md), and defaults to `localhost:1186`.
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
	| Command-Line Format | `--ndb-optimized-node-selection` |
	| --- | --- |
	Enable optimizations for selection of nodes for transactions. Enabled by default; use `--skip-ndb-optimized-node-selection` to disable.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than login file.
- ``--nodeid=*`node_id`*``
	| Command-Line Format | `--ndb-nodeid=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `[none]` |
	Specify the node ID of the node for which configuration information is to be obtained. Formerly, `--id` could be used as a synonym for this option; in NDB 7.5 and later, the only form accepted is `--nodeid`.
- `--nodes`
	| Command-Line Format | `--nodes` |
	| --- | --- |
	Tells **ndb\_config** to print information relating only to parameters defined in an `[ndbd]` or `[ndbd             default]` section of the cluster configuration file (see [Section 21.4.3.6, “Defining NDB Cluster Data Nodes”](mysql-cluster-ndbd-definition.md)).
	This option is mutually exclusive with `--connections` and `--system`; only one of these 3 options can be used.
- ``--query=*`query-options`*``, `-q` *`query-options`*
	| Command-Line Format | `--query=string` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	This is a comma-delimited list of query options—that is, a list of one or more node attributes to be returned. These include `nodeid` (node ID), type (node type—that is, `ndbd`, `mysqld`, or `ndb_mgmd`), and any configuration parameters whose values are to be obtained.
	For example, `--query=nodeid,type,datamemory,datadir` returns the node ID, node type, [`DataMemory`](mysql-cluster-ndbd-definition.md), and [`DataDir`](mysql-cluster-ndbd-definition.md) for each node.
	Formerly, `id` was accepted as a synonym for `nodeid`, but has been removed in NDB 7.5 and later.
	Note
	If a given parameter is not applicable to a certain type of node, than an empty string is returned for the corresponding value. See the examples later in this section for more information.
- `--query-all`, `-a`
	| Command-Line Format | `--query-all` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Returns a comma-delimited list of all query options (node attributes; note that this list is a single string.
	This option was introduced in NDB 7.5.7 (Bug #60095, Bug #11766869).
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print program argument list and exit.
- ``--rows=*`separator`*``, `-r` *`separator`*
	| Command-Line Format | `--rows=string` |
	| --- | --- |
	| Type | String |
	| Default Value |  |
	Specifies a *`separator`* string used to separate the rows in the result. The default is a space character.
	Note
	If the *`separator`* contains spaces or escapes (such as `\n` for the linefeed character), then it must be quoted.
- `--system`
	| Command-Line Format | `--system` |
	| --- | --- |
	Tells **ndb\_config** to print `SYSTEM` information only. This consists of system variables that cannot be changed at run time; thus, there is no corresponding section of the cluster configuration file for them. They can be seen (prefixed with `****** SYSTEM ******`) in the output of **ndb\_config** `--configinfo`.
	This option is mutually exclusive with `--nodes` and `--connections`; only one of these 3 options can be used.
- ``--type=*`node_type`*``
	| Command-Line Format | `--type=name` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `[none]` |
	| Valid Values | `ndbd`  `mysqld`  `ndb_mgmd` |
	Filters results so that only configuration values applying to nodes of the specified *`node_type`* (`ndbd`, `mysqld`, or `ndb_mgmd`) are returned.
- `--usage`, `--help`, or `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Causes **ndb\_config** to print a list of available options, and then exit. Synonym for `--help`.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Causes **ndb\_config** to print a version information string, and then exit.
- `--configinfo` `--xml`
	| Command-Line Format | `--configinfo --xml` |
	| --- | --- |
	Cause **ndb\_config** `--configinfo` to provide output as XML by adding this option. A portion of such output is shown in this example:
	```
	$> ndb_config --configinfo --xml
	<configvariables protocolversion="1" ndbversionstring="5.7.44-ndb-7.5.36"
	                    ndbversion="460032" ndbversionmajor="7" ndbversionminor="5"
	                    ndbversionbuild="0">
	  <section name="SYSTEM">
	    <param name="Name" comment="Name of system (NDB Cluster)" type="string"
	              mandatory="true"/>
	    <param name="PrimaryMGMNode" comment="Node id of Primary ndb_mgmd(MGM) node"
	              type="unsigned" default="0" min="0" max="4294967039"/>
	    <param name="ConfigGenerationNumber" comment="Configuration generation number"
	              type="unsigned" default="0" min="0" max="4294967039"/>
	  </section>
	  <section name="MYSQLD" primarykeys="NodeId">
	    <param name="wan" comment="Use WAN TCP setting as default" type="bool"
	              default="false"/>
	    <param name="HostName" comment="Name of computer for this node"
	              type="string" default=""/>
	    <param name="Id" comment="NodeId" type="unsigned" mandatory="true"
	              min="1" max="255" deprecated="true"/>
	    <param name="NodeId" comment="Number identifying application node (mysqld(API))"
	              type="unsigned" mandatory="true" min="1" max="255"/>
	    <param name="ExecuteOnComputer" comment="HostName" type="string"
	              deprecated="true"/>
	    …
	  </section>
	  …
	</configvariables>
	```
	Note
	Normally, the XML output produced by **ndb\_config** `--configinfo` `--xml` is formatted using one line per element; we have added extra whitespace in the previous example, as well as the next one, for reasons of legibility. This should not make any difference to applications using this output, since most XML processors either ignore nonessential whitespace as a matter of course, or can be instructed to do so.
	The XML output also indicates when changing a given parameter requires that data nodes be restarted using the [`--initial`](mysql-cluster-programs-ndbd.md) option. This is shown by the presence of an `initial="true"` attribute in the corresponding `<param>` element. In addition, the restart type (`system` or `node`) is also shown; if a given parameter requires a system restart, this is indicated by the presence of a `restart="system"` attribute in the corresponding `<param>` element. For example, changing the value set for the [`Diskless`](mysql-cluster-ndbd-definition.md) parameter requires a system initial restart, as shown here (with the `restart` and `initial` attributes highlighted for visibility):
	```
	<param name="Diskless" comment="Run wo/ disk" type="bool" default="false"
	          restart="system" initial="true"/>
	```
	Currently, no `initial` attribute is included in the XML output for `<param>` elements corresponding to parameters which do not require initial restarts; in other words, `initial="false"` is the default, and the value `false` should be assumed if the attribute is not present. Similarly, the default restart type is `node` (that is, an online or “rolling” restart of the cluster), but the `restart` attribute is included only if the restart type is `system` (meaning that all cluster nodes must be shut down at the same time, then restarted).
	Deprecated parameters are indicated in the XML output by the `deprecated` attribute, as shown here:
	```
	<param name="NoOfDiskPagesToDiskAfterRestartACC" comment="DiskCheckpointSpeed"
	       type="unsigned" default="20" min="1" max="4294967039" deprecated="true"/>
	```
	In such cases, the `comment` refers to one or more parameters that supersede the deprecated parameter. Similarly to `initial`, the `deprecated` attribute is indicated only when the parameter is deprecated, with `deprecated="true"`, and does not appear at all for parameters which are not deprecated. (Bug #21127135)
	Beginning with NDB 7.5.0, parameters that are required are indicated with `mandatory="true"`, as shown here:
	```
	<param name="NodeId"
	          comment="Number identifying application node (mysqld(API))"
	          type="unsigned" mandatory="true" min="1" max="255"/>
	```
	In much the same way that the `initial` or `deprecated` attribute is displayed only for a parameter that requires an intial restart or that is deprecated, the `mandatory` attribute is included only if the given parameter is actually required.
	Important
	The `--xml` option can be used only with the `--configinfo` option. Using `--xml` without `--configinfo` fails with an error.
	Unlike the options used with this program to obtain current configuration data, `--configinfo` and `--xml` use information obtained from the NDB Cluster sources when **ndb\_config** was compiled. For this reason, no connection to a running NDB Cluster or access to a `config.ini` or `my.cnf` file is required for these two options.

Combining other **ndb\_config** options (such as `--query` or `--type`) with `--configinfo` (with or without the `--xml` option is not supported. Currently, if you attempt to do so, the usual result is that all other options besides `--configinfo` or `--xml` are simply ignored. *However, this behavior is not guaranteed and is subject to change at any time*. In addition, since **ndb\_config**, when used with the `--configinfo` option, does not access the NDB Cluster or read any files, trying to specify additional options such as `--ndb-connectstring` or `--config-file` with `--configinfo` serves no purpose.

#### Examples

1. To obtain the node ID and type of each node in the cluster:
	```
	$> ./ndb_config --query=nodeid,type --fields=':' --rows='\n'
	1:ndbd
	2:ndbd
	3:ndbd
	4:ndbd
	5:ndb_mgmd
	6:mysqld
	7:mysqld
	8:mysqld
	9:mysqld
	```
	In this example, we used the `--fields` options to separate the ID and type of each node with a colon character (`:`), and the `--rows` options to place the values for each node on a new line in the output.
2. To produce a connection string that can be used by data, SQL, and API nodes to connect to the management server:
	```
	$> ./ndb_config --config-file=usr/local/mysql/cluster-data/config.ini \
	--query=hostname,portnumber --fields=: --rows=, --type=ndb_mgmd
	198.51.100.179:1186
	```
3. This invocation of **ndb\_config** checks only data nodes (using the `--type` option), and shows the values for each node's ID and host name, as well as the values set for its [`DataMemory`](mysql-cluster-ndbd-definition.md) and [`DataDir`](mysql-cluster-ndbd-definition.md) parameters:
	```
	$> ./ndb_config --type=ndbd --query=nodeid,host,datamemory,datadir -f ' : ' -r '\n'
	1 : 198.51.100.193 : 83886080 : /usr/local/mysql/cluster-data
	2 : 198.51.100.112 : 83886080 : /usr/local/mysql/cluster-data
	3 : 198.51.100.176 : 83886080 : /usr/local/mysql/cluster-data
	4 : 198.51.100.119 : 83886080 : /usr/local/mysql/cluster-data
	```
	In this example, we used the short options `-f` and `-r` for setting the field delimiter and row separator, respectively, as well as the short option `-q` to pass a list of parameters to be obtained.
4. To exclude results from any host except one in particular, use the `--host` option:
	```
	$> ./ndb_config --host=198.51.100.176 -f : -r '\n' -q id,type
	3:ndbd
	5:ndb_mgmd
	```
	In this example, we also used the short form `-q` to determine the attributes to be queried.
	Similarly, you can limit results to a node with a specific ID using the `--nodeid` option.