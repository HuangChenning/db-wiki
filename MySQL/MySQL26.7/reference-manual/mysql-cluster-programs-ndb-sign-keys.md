---
title: "MySQL :: MySQL 26.7 Reference Manual :: 25.5.28 ndb_sign_keys — Create, Sign, and Manage TLS Keys and Certificates for NDB\n        Cluster"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-cluster-programs-ndb-sign-keys.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 25.5.28 ndb\_sign\_keys — Create, Sign, and Manage TLS Keys and Certificates for NDB Cluster

Management of TLS keys and certificates in implemented in NDB Cluster as the executable utility program **ndb\_sign\_keys**, which can normally be found in the MySQL `bin` directory. The program performs such functions as creating, signing, and retiring keys and certificates, and normally works as follows:

1. **ndb\_sign\_keys** connects to [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md) and fetches the cluster' configuration.
2. For each cluster node that is configured to run on the local machine, **ndb\_sign\_keys** finds the node' private key and sign it, creating an active node certificate.

Some additional tasks that can be performed by **ndb\_sign\_keys** are listed here:

- Obtaining configuration information from a config.ini file rather than a running [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md)
- Creating the cluster' certificate authority (CA) if it does not yet exist
- Creating private keys
- Saving keys and certificates as pending rather than active
- Signing the key for a single node as specified using command-line options described later in this section
- Requesting a CA located on a remote host to sign a local key

Options that can be used with **ndb\_sign\_keys** are shown in the following table. Additional descriptions follow the table.

- `--bind-host`
	| Command-Line Format | `--bind-host=host` |
	| --- | --- |
	| Type | String |
	| Default Value | `mgmd, api` |
	Create a certificate bound to a hostname list of node types that should have certificate hostname bindings, from the set `(mgmd,db,api)`.
- `--bound-hostname`
	| Command-Line Format | `--bound-hostname=hostname` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Create a certificate bound to the hostname passed to this option.
- `--CA-cert`
	| Command-Line Format | `--CA-cert=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `NDB-Cluster-cert` |
	Use the name passed to this option for the CA Certificate file.
- `--CA-key`
	| Command-Line Format | `--CA-key=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `NDB-Cluster-private-key` |
	Use the name passed to this option for the CA private key file.
- `--CA-ordinal`
	| Command-Line Format | `--CA-ordinal=name` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	| Valid Values | `First`  `Second` |
	Set the ordinal CA name; defaults to `First` for `--create-CA` and `Second` for `--rotate-CA`. The Common Name in the CA certificate is “MySQL NDB Cluster *`ordinal`* Certificate”, where *`ordinal`* is the ordinal name passed to this option.
- `--CA-search-path`
	| Command-Line Format | `--CA-search-path=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `[none]` |
	Specify a list of directories to search for a CA file. On Unix platforms, the directory names are separated by colons (`:`); on Windows systems, the semicolon character (`;`) is used as the separator. A directory reference may be relative or absolute; it may contain one or more environment variables, each denoted by a prefixed dollar sign (`$`), and expanded prior to use.
	Searching begins with the leftmost named directory and proceeds from left to right until a file is found. An empty string denotes an empty search path, which causes all searches to fail. A string consisting of a single dot (`.`) indicates that the search path is limited to the current working directory.
	If no search path is supplied, the compiled-in default value is used. This value depends on the platform used: On Windows, this is `$HOMEPATH\ndb-tls`; on other platforms (including Linux), it is `$HOME/ndb-tls`. This default can be overridden by compiling NDB Cluster using [`-DWITH_NDB_TLS_SEARCH_PATH`](source-configuration-options.md).
- `--CA-tool`
	| Command-Line Format | `--CA-tool=name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `[none]` |
	Designate an executable helper tool, including the path.
- `--check`
	| Command-Line Format | `--check` |
	| --- | --- |
	Check certificate expiry dates.
- `--config-file`
	| Command-Line Format | `--config-file=file` |
	| --- | --- |
	| Disabled by | `no-config` |
	| Type | File name |
	| Default Value | `[none]` |
	Supply the path to the cluster configuration file (usually `config.ini`).
- `--connect-retries`
	| Command-Line Format | `--connect-retries=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `12` |
	| Minimum Value | `-1` |
	| Maximum Value | `12` |
	Set the number of times that **ndb\_sign\_keys** attempts to connect to the cluster. If you use `-1`, the program keeps trying to connect until it succeeds or is forced to stop.
- `--connect-retry-delay`
	| Command-Line Format | `--connect-retry-delay=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `5` |
	| Minimum Value | `0` |
	| Maximum Value | `5` |
	Set the number of seconds after a failed connection attempt which **ndb\_sign\_keys** waits before trying again, up to the number of times determined by `--connect-retries`.
- `--create-CA`
	| Command-Line Format | `--create-CA` |
	| --- | --- |
	Create the CA key and certificate.
- `--CA-days`
	| Command-Line Format | `--CA-days=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1461` |
	| Minimum Value | `-1` |
	| Maximum Value | `2147483647` |
	Set the lifetime of the certificate to this many days. The default is equivalent to 4 years plus 1 day. `-1` means the certificate never expires.
	This option was added in NDB 8.4.1.
- `--create-key`
	| Command-Line Format | `--create-key` |
	| --- | --- |
	Create or replace private keys.
- `--curve`
	| Command-Line Format | `--curve=name` |
	| --- | --- |
	| Type | String |
	| Default Value | `P-256` |
	Use the named curve for encrypting node keys.
- `--defaults-extra-file`
	| Command-Line Format | `--defaults-extra-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read this option file after the global files are read.
- `--defaults-file`
	| Command-Line Format | `--defaults-file=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read this option file only.
- `--defaults-group-suffix`
	| Command-Line Format | `--defaults-group-suffix=string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`string`*.
- `--duration`
	| Command-Line Format | `--duration=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `-500000` |
	| Maximum Value | `0` |
	| Unit | seconds |
	Set the lifetime of certificates or signing requests, in seconds.
- `--help`
	| Command-Line Format | `--help` |
	| --- | --- |
	Print help text and exit.
- `--keys-to-dir`
	| Command-Line Format | `--keys-to-dir=dirname` |
	| --- | --- |
	| Type | Directory name |
	| Default Value | `[none]` |
	Specify output directory for private keys (only); for this purpose, it overrides any value set for `--to-dir`.
- `--login-path`
	| Command-Line Format | `--login-path=path` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Read this path from the login file.
- `--ndb-connectstring`
	| Command-Line Format | `--ndb-connectstring=connection_string` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Set the connection string to use for connecting to [**ndb\_mgmd**](mysql-cluster-programs-ndb-mgmd.md), using the syntax ``[nodeid=*`id`*;][host=]*`hostname`*[:*`port`*]``. If this option is set, it overrides the value set for `NDB_CONNECTSTRING` (if any), as well as any value set in a `my.cnf`. file.
- `--ndb-mgm-tls`
	| Command-Line Format | `--ndb-mgm-tls=level` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `relaxed` |
	| Valid Values | `relaxed`  `strict` |
	Sets the level of TLS support required for the [**ndb\_mgm**](mysql-cluster-programs-ndb-mgm.md) client; one of `relaxed` or `strict`. `relaxed` (the default) means that a TLS connection is attempted, but success is not required; `strict` means that TLS is required to connect.
- `--ndb-tls-search-path`
	| Command-Line Format | `--ndb-tls-search-path=list` |
	| --- | --- |
	| Type | Path name |
	| Default Value (Unix) | `$HOME/ndb-tls` |
	| Default Value (Windows) | `$HOMEDIR/ndb-tls` |
	Specify a list of directories containing TLS keys and certificates.
	For syntax, see the description of the `--CA-search-path` option.
- `--no-config`
	| Command-Line Format | `--no-config` |
	| --- | --- |
	Do not obtain the cluster configuration; create a single certificate based on the options supplied (including defaults for those not specified).
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read default options from any option file other than the login file.
- `--no-login-paths`
	| Command-Line Format | `--no-login-paths` |
	| --- | --- |
	Do not read login paths from the login path file.
- `--passphrase`
	| Command-Line Format | `--passphrase=phrase` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Specify a CA key pass phrase.
- `--node-id`
	| Command-Line Format | `--node-id=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	| Minimum Value | `0` |
	| Maximum Value | `255` |
	Create or sign a key for the node having the specified node ID.
- `--node-type`
	| Command-Line Format | `--node-type=set` |
	| --- | --- |
	| Type | Set |
	| Default Value | `mgmd,db,api` |
	Create or sign keys for the specified type or types from the set `(mgmd,db,api)`.
- `--pending`
	| Command-Line Format | `--pending` |
	| --- | --- |
	Save keys and certificates as pending, rather than active.
- `--print-defaults`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Print the program argument list, then exit.
- `--promote`
	| Command-Line Format | `--promote` |
	| --- | --- |
	Promote pending files to active, then exit.
- `--remote-CA-host`
	| Command-Line Format | `--remote-CA-host=hostname` |
	| --- | --- |
	| Type | String |
	| Default Value | `[none]` |
	Specify the address or hostname of a remote CA host.
- `--remote-exec-path`
	| Command-Line Format | `--remote-exec-path` |
	| --- | --- |
	| Type | Path name |
	| Default Value | `[none]` |
	Provide the full path to an executable on the remote CA host specified with `--remote-CA-host`.
- `--remote-openssl`
	| Command-Line Format | `--remote-openssl` |
	| --- | --- |
	Use OpenSSL for signing of keys on the remote CA host specified with `--remote-CA-host`.
- `--replace-by`
	| Command-Line Format | `--replace-by=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `-10` |
	| Minimum Value | `-128` |
	| Maximum Value | `127` |
	Suggest a certificate replacement date for periodic checks, as a number of days after the CA expiration date. Use a negative number to indicate days before expiration.
- `--rotate-CA`
	| Command-Line Format | `--rotate-CA` |
	| --- | --- |
	Replace an older CA with a newer one. The new CA can be created using OpenSSL, or you can allow **ndb\_sign\_keys** to create the new one, in which case the new CA is created with an intermediate CA certificate, signed by the old CA.
- `--schedule`
	| Command-Line Format | `--schedule=list` |
	| --- | --- |
	| Type | String |
	| Default Value | `120,10,130,10,150,0` |
	Assign a schedule of expiration dates to certificates. The schedule is defined as a comma-delimited list of six integers, in the format shown here:
	```svg
	api_valid,api_extra,dn_valid,dn_extra,mgm_valid,mgm_extra
	```
	These values are defined as follows:
	- `api_valid`: A fixed number of days of validity for client certificates.
		`api_extra`: A number of extra days for client certificates.
		`dn_valid`: A fixed number of days of validity for client certificates for data node certificates.
		`dn_extra`: A number of extra days for data node certificates.
		`mgm_valid`: A fixed number of days of validity for management server certificates.
		`mgm_extra`: A number of extra days for management server certificates.
	In other words, for each node type (API node, data node, management node), certificates are created with a lifetime equal to a whole fixed number of days, plus some random amount of time less than or equal to the number of extra days. The default schedule is shown here:
	```svg
	--schedule=120,10,130,10,150,0
	```
	Following the default schedule, client certificates begin expiring on the 120 <sup>th</sup> day, and expire at random intervals over the next 10 days; data node certificates expire at random times between the 130 <sup>th</sup> and 140 <sup>th</sup> days; and management node certificates expire on the 150 <sup>th</sup> day (with no random interval following).
- `--sign`
	| Command-Line Format | `--sign` |
	| --- | --- |
	| Disabled by | `skip-sign` |
	Create signed certificates; enabled by default. Use `--skip-sign` to create certificate signing requests instead.
- `--skip-sign`
	| Command-Line Format | `--skip-sign` |
	| --- | --- |
	Create certificate signing requests instead of signed certificates.
- `--stdio`
	| Command-Line Format | `--stdio` |
	| --- | --- |
	Read certificate signing requests from `stdin`, and write X.509 to `stdout`.
- `--to-dir`
	| Command-Line Format | `--to-dir=dirname` |
	| --- | --- |
	| Type | Directory name |
	| Default Value | `[none]` |
	Specify the output directory for created files. For private key files, this can be overriden using `--keys-to-dir`.
- `--usage`
	| Command-Line Format | `--usage` |
	| --- | --- |
	Print help text, then exit (alias for `--help`).
- `--version`
	| Command-Line Format | `--version` |
	| --- | --- |
	Print version information, then exit.