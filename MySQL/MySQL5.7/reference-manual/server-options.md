---
title: "5.1.6 Server Command Options"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/server-options.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.1.6 Server Command Options

When you start the [**mysqld**](mysqld.md) server, you can specify program options using any of the methods described in [Section 4.2.2, “Specifying Program Options”](program-options.md). The most common methods are to provide options in an option file or on the command line. However, in most cases it is desirable to make sure that the server uses the same options each time it runs. The best way to ensure this is to list them in an option file. See [Section 4.2.2.2, “Using Option Files”](option-files.md). That section also describes option file format and syntax.

[**mysqld**](mysqld.md) reads options from the `[mysqld]` and `[server]` groups. [**mysqld\_safe**](mysqld-safe.md) reads options from the `[mysqld]`, `[server]`, `[mysqld_safe]`, and `[safe_mysqld]` groups. [**mysql.server**](mysql-server.md) reads options from the `[mysqld]` and `[mysql.server]` groups.

An embedded MySQL server usually reads options from the `[server]`, `[embedded]`, and ``[*`xxxxx`*_SERVER]`` groups, where *`xxxxx`* is the name of the application into which the server is embedded.

[**mysqld**](mysqld.md) accepts many command options. For a brief summary, execute this command:

```
mysqld --help
```

To see the full list, use this command:

```
mysqld --verbose --help
```

Some of the items in the list are actually system variables that can be set at server startup. These can be displayed at runtime using the [`SHOW VARIABLES`](show-variables.md) statement. Some items displayed by the preceding [**mysqld**](mysqld.md) command do not appear in [`SHOW       VARIABLES`](show-variables.md) output; this is because they are options only and not system variables.

The following list shows some of the most common server options. Additional options are described in other sections:

- Options that affect security: See [Section 6.1.4, “Security-Related mysqld Options and Variables”](security-options.md).
- SSL-related options: See [Command Options for Encrypted Connections](connection-options.md).
- Binary log control options: See [Section 5.4.4, “The Binary Log”](binary-log.md).
- Replication-related options: See [Section 16.1.6, “Replication and Binary Logging Options and Variables”](replication-options.md).
- Options for loading plugins such as pluggable storage engines: See [Section 5.5.1, “Installing and Uninstalling Plugins”](plugin-loading.md).
- Options specific to particular storage engines: See [Section 14.15, “InnoDB Startup Options and System Variables”](innodb-parameters.md) and [Section 15.2.1, “MyISAM Startup Options”](myisam-start.md).

Some options control the size of buffers or caches. For a given buffer, the server might need to allocate internal data structures. These structures typically are allocated from the total memory allocated to the buffer, and the amount of space required might be platform dependent. This means that when you assign a value to an option that controls a buffer size, the amount of space actually available might differ from the value assigned. In some cases, the amount might be less than the value assigned. It is also possible that the server adjusts a value upward. For example, if you assign a value of 0 to an option for which the minimal value is 1024, the server sets the value to 1024.

Values for buffer sizes, lengths, and stack sizes are given in bytes unless otherwise specified.

Some options take file name values. Unless otherwise specified, the default file location is the data directory if the value is a relative path name. To specify the location explicitly, use an absolute path name. Suppose that the data directory is `/var/mysql/data`. If a file-valued option is given as a relative path name, it is located under `/var/mysql/data`. If the value is an absolute path name, its location is as given by the path name.

You can also set the values of server system variables at server startup by using variable names as options. To assign a value to a server system variable, use an option of the form ``--*`var_name`*=*`value`*``. For example, [`--sort_buffer_size=384M`](server-system-variables.md) sets the [`sort_buffer_size`](server-system-variables.md) variable to a value of 384MB.

When you assign a value to a variable, MySQL might automatically correct the value to stay within a given range, or adjust the value to the closest permissible value if only certain values are permitted.

To restrict the maximum value to which a system variable can be set at runtime with the [`SET`](set-variable.md) statement, specify this maximum by using an option of the form ``--maximum-*`var_name`*=*`value`*`` at server startup.

You can change the values of most system variables at runtime with the [`SET`](set-variable.md) statement. See [Section 13.7.4.1, “SET Syntax for Variable Assignment”](set-variable.md).

[Section 5.1.7, “Server System Variables”](server-system-variables.md), provides a full description for all variables, and additional information for setting them at server startup and runtime. For information on changing system variables, see [Section 5.1.1, “Configuring the Server”](server-configuration.md).

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a short help message and exit. Use both the `--verbose` and `--help` options to see the full message.
- `--allow-suspicious-udfs`
	| Command-Line Format | `--allow-suspicious-udfs[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	This option controls whether loadable functions that have only an `xxx` symbol for the main function can be loaded. By default, the option is off and only loadable functions that have at least one auxiliary symbol can be loaded; this prevents attempts at loading functions from shared object files other than those containing legitimate functions. See [Loadable Function Security Precautions](https://dev.mysql.com/doc/extending-mysql/5.7/en/adding-loadable-function.html#loadable-function-security).
- `--ansi`
	| Command-Line Format | `--ansi` |
	| --- | --- |
	Use standard (ANSI) SQL syntax instead of MySQL syntax. For more precise control over the server SQL mode, use the `--sql-mode` option instead. See [Section 1.6, “MySQL Standards Compliance”](compatibility.md), and [Section 5.1.10, “Server SQL Modes”](sql-mode.md).
- [``--basedir=*`dir_name`*``](server-system-variables.md), [``-b           *`dir_name`*``](server-system-variables.md)
	| Command-Line Format | `--basedir=dir_name` |
	| --- | --- |
	| System Variable | `basedir` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Directory name |
	| Default Value | `configuration-dependent default` |
	The path to the MySQL installation directory. This option sets the [`basedir`](server-system-variables.md) system variable.
- `--bootstrap`
	| Command-Line Format | `--bootstrap` |
	| --- | --- |
	| Deprecated | Yes |
	This option is used by the [**mysql\_install\_db**](mysql-install-db.md) program to create the MySQL privilege tables without having to start a full MySQL server.
	Note
	[**mysql\_install\_db**](mysql-install-db.md) is deprecated because its functionality has been integrated into [**mysqld**](mysqld.md), the MySQL server. Consequently, the `--bootstrap` server option that [**mysql\_install\_db**](mysql-install-db.md) passes to [**mysqld**](mysqld.md) is also deprecated. To initialize a MySQL installation, invoke [**mysqld**](mysqld.md) with the `--initialize` or `--initialize-insecure` option. For more information, see [Section 2.9.1, “Initializing the Data Directory”](data-directory-initialization.md). Expect [**mysql\_install\_db**](mysql-install-db.md) and the `--bootstrap` server option to be removed in a future release of MySQL.
	`--bootstrap` is mutually exclusive with `--daemonize`, `--initialize`, and `--initialize-insecure`.
	Global transaction identifiers (GTIDs) are not disabled when `--bootstrap` is used. `--bootstrap` was used (Bug #20980271). See [Section 16.1.3, “Replication with Global Transaction Identifiers”](replication-gtids.md).
	When the server operates in bootstap mode, some functionality is unavailable that limits the statements permitted in any file named by the [`init_file`](server-system-variables.md) system variable. For more information, see the description of that variable. In addition, the [`disabled_storage_engines`](server-system-variables.md) system variable has no effect.
- `--character-set-client-handshake`
	| Command-Line Format | `--character-set-client-handshake[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `ON` |
	Do not ignore character set information sent by the client. To ignore client information and use the default server character set, use `--skip-character-set-client-handshake`; this makes MySQL behave like MySQL 4.0.
- ``--chroot=*`dir_name`*``, ``-r *`dir_name`*``
	| Command-Line Format | `--chroot=dir_name` |
	| --- | --- |
	| Type | Directory name |
	Put the [**mysqld**](mysqld.md) server in a closed environment during startup by using the `chroot()` system call. This is a recommended security measure. Use of this option somewhat limits [`LOAD DATA`](load-data.md) and [`SELECT ... INTO           OUTFILE`](select-into.md).
- `--console`
	| Command-Line Format | `--console` |
	| --- | --- |
	| Platform Specific | Windows |
	(Windows only.) Write the error log to `stderr` and `stdout` (the console). [**mysqld**](mysqld.md) does not close the console window if this option is used.
	`--console` takes precedence over `--log-error` if both are given. (In MySQL 5.5 and 5.6, this is reversed: `--log-error` takes precedence over `--console` if both are given.)
- `--core-file`
	| Command-Line Format | `--core-file` |
	| --- | --- |
	When this option is used, write a core file if [**mysqld**](mysqld.md) dies; no arguments are needed (or accepted). The name and location of the core file is system dependent. On Linux, a core file named ``core.*`pid`*`` is written to the current working directory of the process, which for [**mysqld**](mysqld.md) is the data directory. *`pid`* represents the process ID of the server process. On macOS, a core file named ``core.*`pid`*`` is written to the `/cores` directory. On Solaris, use the **coreadm** command to specify where to write the core file and how to name it.
	For some systems, to get a core file you must also specify the [`--core-file-size`](mysqld-safe.md) option to [**mysqld\_safe**](mysqld-safe.md). See [Section 4.3.2, “mysqld\_safe — MySQL Server Startup Script”](mysqld-safe.md). On some systems, such as Solaris, you do not get a core file if you are also using the `--user` option. There might be additional restrictions or limitations. For example, it might be necessary to execute **ulimit -c unlimited** before starting the server. Consult your system documentation.
- `--daemonize`
	| Command-Line Format | `--daemonize[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	This option causes the server to run as a traditional, forking daemon, permitting it to work with operating systems that use systemd for process control. For more information, see [Section 2.5.10, “Managing MySQL Server with systemd”](using-systemd.md).
	`--daemonize` is mutually exclusive with `--bootstrap`, `--initialize`, and `--initialize-insecure`.
- [``--datadir=*`dir_name`*``](server-system-variables.md), ``-h *`dir_name`*``
	| Command-Line Format | `--datadir=dir_name` |
	| --- | --- |
	| System Variable | `datadir` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Directory name |
	The path to the MySQL server data directory. This option sets the [`datadir`](server-system-variables.md) system variable. See the description of that variable.
- [``--debug[=*`debug_options`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_debug), ``-# [*`debug_options`*]``
	| Command-Line Format | `--debug[=debug_options]` |
	| --- | --- |
	| System Variable | `debug` |
	| Scope | Global, Session |
	| Dynamic | Yes |
	| Type | String |
	| Default Value (Unix) | `d:t:i:o,/tmp/mysqld.trace` |
	| Default Value (Windows) | `d:t:i:O,\mysqld.trace` |
	If MySQL is configured with the [`-DWITH_DEBUG=1`](source-configuration-options.md) **CMake** option, you can use this option to get a trace file of what [**mysqld**](mysqld.md) is doing. A typical *`debug_options`* string is ``d:t:o,*`file_name`*``. The default is `d:t:i:o,/tmp/mysqld.trace` on Unix and `d:t:i:O,\mysqld.trace` on Windows.
	Using [`-DWITH_DEBUG=1`](source-configuration-options.md) to configure MySQL with debugging support enables you to use the `--debug="d,parser_debug"` option when you start the server. This causes the Bison parser that is used to process SQL statements to dump a parser trace to the server's standard error output. Typically, this output is written to the error log.
	This option may be given multiple times. Values that begin with `+` or `-` are added to or subtracted from the previous value. For example, `--debug=T` `--debug=+P` sets the value to `P:T`.
	For more information, see [Section 5.8.3, “The DBUG Package”](dbug-package.md).
- [``--debug-sync-timeout[=*`N`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_debug-sync-timeout)
	| Command-Line Format | `--debug-sync-timeout[=#]` |
	| --- | --- |
	| Type | Integer |
	Controls whether the Debug Sync facility for testing and debugging is enabled. Use of Debug Sync requires that MySQL be configured with the [`-DWITH_DEBUG=ON`](source-configuration-options.md) **CMake** option (see [Section 2.8.7, “MySQL Source-Configuration Options”](source-configuration-options.md)). If Debug Sync is not compiled in, this option is not available. The option value is a timeout in seconds. The default value is 0, which disables Debug Sync. To enable it, specify a value greater than 0; this value also becomes the default timeout for individual synchronization points. If the option is given without a value, the timeout is set to 300 seconds.
	For a description of the Debug Sync facility and how to use synchronization points, see [MySQL Internals: Test Synchronization](https://dev.mysql.com/doc/internals/en/test-synchronization.html).
- ``--default-time-zone=*`timezone`*``
	| Command-Line Format | `--default-time-zone=name` |
	| --- | --- |
	| Type | String |
	Set the default server time zone. This option sets the global [`time_zone`](server-system-variables.md) system variable. If this option is not given, the default time zone is the same as the system time zone (given by the value of the [`system_time_zone`](server-system-variables.md) system variable.
	The [`system_time_zone`](server-system-variables.md) variable differs from [`time_zone`](server-system-variables.md). Although they might have the same value, the latter variable is used to initialize the time zone for each client that connects. See [Section 5.1.13, “MySQL Server Time Zone Support”](time-zone-support.md).
- ``--defaults-extra-file=*`file_name`*``
	Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory. This must be the first option on the command line if it is used.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-file=*`file_name`*``
	Read only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	Note
	This must be the first option on the command line if it is used, except that if the server is started with the `--defaults-file` and `--install` (or `--install-manual`) options, `--install` (or `--install-manual`) must be first.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-group-suffix=*`str`*``
	Read not only the usual option groups, but also groups with the usual names and a suffix of *`str`*. For example, [**mysqld**](mysqld.md) normally reads the `[mysqld]` group. If this option is given as `--defaults-group-suffix=_other`, [**mysqld**](mysqld.md) also reads the `[mysqld_other]` group.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--des-key-file=*`file_name`*``
	| Command-Line Format | `--des-key-file=file_name` |
	| --- | --- |
	| Deprecated | Yes |
	Read the default DES keys from this file. These keys are used by the [`DES_ENCRYPT()`](encryption-functions.md) and [`DES_DECRYPT()`](encryption-functions.md) functions.
	Note
	The [`DES_ENCRYPT()`](encryption-functions.md) and [`DES_DECRYPT()`](encryption-functions.md) functions are deprecated in MySQL 5.7, are removed in MySQL 8.0, and should no longer be used. Consequently, `--des-key-file` also is deprecated and is removed in MySQL 8.0.
- `--disable-partition-engine-check`
	| Command-Line Format | `--disable-partition-engine-check[={OFF\|ON}]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value | `ON` |
	Whether to disable the startup check for tables with nonnative partitioning.
	As of MySQL 5.7.17, the generic partitioning handler in the MySQL server is deprecated, and is removed in MySQL 8.0, when the storage engine used for a given table is expected to provide its own (“native”) partitioning handler. Currently, only the [`InnoDB`](innodb-storage-engine.md) and [`NDB`](mysql-cluster.md) storage engines do this.
	Use of tables with nonnative partitioning results in an [`ER_WARN_DEPRECATED_SYNTAX`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_warn_deprecated_syntax) warning. In MySQL 5.7.17 through 5.7.20, the server automatically performs a check at startup to identify tables that use nonnative partitioning; for any that are found, the server writes a message to its error log. To disable this check, use the `--disable-partition-engine-check` option. In MySQL 5.7.21 and later, this check is *not* performed; in these versions, you must start the server with `--disable-partition-engine-check=false`, if you wish for the server to check for tables using the generic partitioning handler (Bug #85830, Bug #25846957).
	Use of tables with nonnative partitioning results in an [`ER_WARN_DEPRECATED_SYNTAX`](https://docs.oracle.com/cd/E17952_01/mysql-errors-5.7-en/server-error-reference.html#error_er_warn_deprecated_syntax) warning. Also, the server performs a check at startup to identify tables that use nonnative partitioning; for any found, the server writes a message to its error log. To disable this check, use the `--disable-partition-engine-check` option.
	To prepare for migration to MySQL 8.0, any table with nonnative partitioning should be changed to use an engine that provides native partitioning, or be made nonpartitioned. For example, to change a table to `InnoDB`, execute this statement:
	```
	ALTER TABLE table_name ENGINE = INNODB;
	```
- ``--early-plugin-load=*`plugin_list`*``
	| Command-Line Format | `--early-plugin-load=plugin_list` |
	| --- | --- |
	| Type | String |
	| Default Value | `empty string` |
	This option tells the server which plugins to load before loading mandatory built-in plugins and before storage engine initialization. Early loading is supported only for plugins compiled with `PLUGIN_OPT_ALLOW_EARLY`. If multiple `--early-plugin-load` options are given, only the last one applies.
	The option value is a semicolon-separated list of *`plugin_library`* and *`name`* `=` *`plugin_library`* values. Each *`plugin_library`* is the name of a library file that contains plugin code, and each *`name`* is the name of a plugin to load. If a plugin library is named without any preceding plugin name, the server loads all plugins in the library. With a preceding plugin name, the server loads only the named plugin from the libary. The server looks for plugin library files in the directory named by the [`plugin_dir`](server-system-variables.md) system variable.
	For example, if plugins named `myplug1` and `myplug2` are contained in the plugin library files `myplug1.so` and `myplug2.so`, use this option to perform an early plugin load:
	```
	mysqld --early-plugin-load="myplug1=myplug1.so;myplug2=myplug2.so"
	```
	Quotes surround the argument value because otherwise some command interpreters interpret semicolon (`;`) as a special character. (For example, Unix shells treat it as a command terminator.)
	Each named plugin is loaded early for a single invocation of [**mysqld**](mysqld.md) only. After a restart, the plugin is not loaded early unless `--early-plugin-load` is used again.
	If the server is started using `--initialize` or `--initialize-insecure`, plugins specified by `--early-plugin-load` are not loaded.
	If the server is run with `--help`, plugins specified by `--early-plugin-load` are loaded but not initialized. This behavior ensures that plugin options are displayed in the help message.
	`InnoDB` tablespace encryption relies on the MySQL Keyring for encryption key management, and the keyring plugin to be used must be loaded prior to storage engine initialization to facilitate `InnoDB` recovery for encrypted tables. For example, administrators who want the `keyring_file` plugin loaded at startup should use `--early-plugin-load` with the appropriate option value (such as `keyring_file.so` on Unix and Unix-like systems or `keyring_file.dll` on Windows).
	Important
	In MySQL 5.7.11, the default `--early-plugin-load` value is the name of the `keyring_file` plugin library file, causing that plugin to be loaded by default. In MySQL 5.7.12 and higher, the default `--early-plugin-load` value is empty; to load the `keyring_file` plugin, you must explicitly specify the option with a value naming the `keyring_file` plugin library file.
	This change of default `--early-plugin-load` value introduces an incompatibility for `InnoDB` tablespace encryption for upgrades from 5.7.11 to 5.7.12 or higher. Administrators who have encrypted `InnoDB` tablespaces must take explicit action to ensure continued loading of the keyring plugin: Start the server with an `--early-plugin-load` option that names the plugin library file. For additional information, see [Section 6.4.4.1, “Keyring Plugin Installation”](keyring-plugin-installation.md).
	For information about `InnoDB` tablespace encryption, see [Section 14.14, “InnoDB Data-at-Rest Encryption”](innodb-data-encryption.md). For general information about plugin loading, see [Section 5.5.1, “Installing and Uninstalling Plugins”](plugin-loading.md).
- [``--exit-info[=*`flags`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_exit-info), ``-T [*`flags`*]``
	| Command-Line Format | `--exit-info[=flags]` |
	| --- | --- |
	| Type | Integer |
	This is a bitmask of different flags that you can use for debugging the [**mysqld**](mysqld.md) server. Do not use this option unless you know *exactly* what it does!
- `--external-locking`
	| Command-Line Format | `--external-locking[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Enable external locking (system locking), which is disabled by default. If you use this option on a system on which `lockd` does not fully work (such as Linux), it is easy for [**mysqld**](mysqld.md) to deadlock.
	To disable external locking explicitly, use `--skip-external-locking`.
	External locking affects only [`MyISAM`](myisam-storage-engine.md) table access. For more information, including conditions under which it can and cannot be used, see [Section 8.11.5, “External Locking”](external-locking.md).
- `--flush`
	| Command-Line Format | `--flush[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `flush` |
	| Scope | Global |
	| Dynamic | Yes |
	| Type | Boolean |
	| Default Value | `OFF` |
	Flush (synchronize) all changes to disk after each SQL statement. Normally, MySQL does a write of all changes to disk only after each SQL statement and lets the operating system handle the synchronizing to disk. See [Section B.3.3.3, “What to Do If MySQL Keeps Crashing”](crashing.md).
	Note
	If `--flush` is specified, the value of [`flush_time`](server-system-variables.md) does not matter and changes to [`flush_time`](server-system-variables.md) have no effect on flush behavior.
- `--gdb`
	| Command-Line Format | `--gdb[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Install an interrupt handler for `SIGINT` (needed to stop [**mysqld**](mysqld.md) with `^C` to set breakpoints) and disable stack tracing and core file handling. See [Section 5.8.1.4, “Debugging mysqld under gdb”](using-gdb-on-mysqld.md).
- ``--ignore-db-dir=*`dir_name`*``
	| Command-Line Format | `--ignore-db-dir=dir_name` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Directory name |
	This option tells the server to ignore the given directory name for purposes of the [`SHOW           DATABASES`](show-databases.md) statement or `INFORMATION_SCHEMA` tables. For example, if a MySQL configuration locates the data directory at the root of a file system on Unix, the system might create a `lost+found` directory there that the server should ignore. Starting the server with `--ignore-db-dir=lost+found` causes that name not to be listed as a database.
	To specify more than one name, use this option multiple times, once for each name. Specifying the option with an empty value (that is, as `--ignore-db-dir=`) resets the directory list to the empty list.
	Instances of this option given at server startup are used to set the [`ignore_db_dirs`](server-system-variables.md) system variable.
	This option is deprecated in MySQL 5.7. With the introduction of the data dictionary in MySQL 8.0, it became superfluous and was removed in that version.
- `--initialize`
	| Command-Line Format | `--initialize[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	This option is used to initialize a MySQL installation by creating the data directory and populating the tables in the `mysql` system database. For more information, see [Section 2.9.1, “Initializing the Data Directory”](data-directory-initialization.md).
	This option limits the effects of, or is not compatible with, a number of other startup options for the MySQL server. Some of the most common issues of this sort are noted here:
	- We strongly recommend, when initializing the data directory with `--initialize`, that you specify no additional options other than [`--datadir`](server-system-variables.md), other options used for setting directory locations such as [`--basedir`](server-system-variables.md), and possibly `--user`, if required. Options for the running MySQL server can be specified when starting it once initialization has been completed and [**mysqld**](mysqld.md) has shut down. This also applies when using `--initialize-insecure` instead of `--initialize`.
	- When the server is started with `--initialize`, some functionality is unavailable that limits the statements permitted in any file named by the [`init_file`](server-system-variables.md) system variable. For more information, see the description of that variable. In addition, the [`disabled_storage_engines`](server-system-variables.md) system variable has no effect.
	- The [`--ndbcluster`](mysql-cluster-options-variables.md) option is ignored when used together with `--initialize`.
	- `--initialize` is mutually exclusive with `--bootstrap` and `--daemonize`.
	The items in the preceding list also apply when initializing the server using the `--initialize-insecure` option.
- `--initialize-insecure`
	| Command-Line Format | `--initialize-insecure[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	This option is used to initialize a MySQL installation by creating the data directory and populating the tables in the `mysql` system database. This option implies `--initialize`, and the same restrictions and limitations apply; for more information, see the description of that option, and [Section 2.9.1, “Initializing the Data Directory”](data-directory-initialization.md).
	Warning
	This option creates a MySQL `root` user with an empty password, which is insecure. For this reason, do not use it in production without setting this password manually. See [Post-Initialization root Password Assignment](data-directory-initialization.md), for information about how to do this.
- ``--innodb-*`xxx`*``
	Set an option for the `InnoDB` storage engine. The `InnoDB` options are listed in [Section 14.15, “InnoDB Startup Options and System Variables”](innodb-parameters.md).
- [``--install           [*`service_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_install)
	| Command-Line Format | `--install [service_name]` |
	| --- | --- |
	| Platform Specific | Windows |
	(Windows only) Install the server as a Windows service that starts automatically during Windows startup. The default service name is `MySQL` if no *`service_name`* value is given. For more information, see [Section 2.3.4.8, “Starting MySQL as a Windows Service”](windows-start-service.md).
	Note
	If the server is started with the `--defaults-file` and `--install` options, `--install` must be first.
- [``--install-manual           [*`service_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_install-manual)
	| Command-Line Format | `--install-manual [service_name]` |
	| --- | --- |
	| Platform Specific | Windows |
	(Windows only) Install the server as a Windows service that must be started manually. It does not start automatically during Windows startup. The default service name is `MySQL` if no *`service_name`* value is given. For more information, see [Section 2.3.4.8, “Starting MySQL as a Windows Service”](windows-start-service.md).
	Note
	If the server is started with the [`--defaults-file`](option-file-options.md) and `--install-manual` options, `--install-manual` must be first.
- ``--language=*`lang_name`*,           -L *`lang_name`*``
	| Command-Line Format | `--language=name` |
	| --- | --- |
	| Deprecated | Yes; use `lc-messages-dir` instead |
	| System Variable | `language` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Directory name |
	| Default Value | `/usr/local/mysql/share/mysql/english/` |
	The language to use for error messages. *`lang_name`* can be given as the language name or as the full path name to the directory where the language files are installed. See [Section 10.12, “Setting the Error Message Language”](error-message-language.md).
	`--lc-messages-dir` and `--lc-messages` should be used rather than `--language`, which is deprecated (and handled as a synonym for `--lc-messages-dir`). You should expect the `--language` option to be removed in a future release of MySQL.
- `--large-pages`
	| Command-Line Format | `--large-pages[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `large_pages` |
	| Scope | Global |
	| Dynamic | No |
	| Platform Specific | Linux |
	| Type | Boolean |
	| Default Value | `OFF` |
	Some hardware/operating system architectures support memory pages greater than the default (usually 4KB). The actual implementation of this support depends on the underlying hardware and operating system. Applications that perform a lot of memory accesses may obtain performance improvements by using large pages due to reduced Translation Lookaside Buffer (TLB) misses.
	MySQL supports the Linux implementation of large page support (which is called HugeTLB in Linux). See [Section 8.12.4.3, “Enabling Large Page Support”](large-page-support.md). For Solaris support of large pages, see the description of the `--super-large-pages` option.
	`--large-pages` is disabled by default.
- ``--lc-messages=*`locale_name`*``
	| Command-Line Format | `--lc-messages=name` |
	| --- | --- |
	| System Variable | `lc_messages` |
	| Scope | Global, Session |
	| Dynamic | Yes |
	| Type | String |
	| Default Value | `en_US` |
	The locale to use for error messages. The default is `en_US`. The server converts the argument to a language name and combines it with the value of `--lc-messages-dir` to produce the location for the error message file. See [Section 10.12, “Setting the Error Message Language”](error-message-language.md).
- ``--lc-messages-dir=*`dir_name`*``
	| Command-Line Format | `--lc-messages-dir=dir_name` |
	| --- | --- |
	| System Variable | `lc_messages_dir` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Directory name |
	The directory where error messages are located. The server uses the value together with the value of `--lc-messages` to produce the location for the error message file. See [Section 10.12, “Setting the Error Message Language”](error-message-language.md).
- `--local-service`
	| Command-Line Format | `--local-service` |
	| --- | --- |
	(Windows only) A `--local-service` option following the service name causes the server to run using the `LocalService` Windows account that has limited system privileges. If both [`--defaults-file`](option-file-options.md) and `--local-service` are given following the service name, they can be in any order. See [Section 2.3.4.8, “Starting MySQL as a Windows Service”](windows-start-service.md).
- [``--log-error[=*`file_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_log-error)
	| Command-Line Format | `--log-error[=file_name]` |
	| --- | --- |
	| System Variable | `log_error` |
	| Scope | Global |
	| Dynamic | No |
	| Type | File name |
	Write the error log and startup messages to this file. See [Section 5.4.2, “The Error Log”](error-log.md).
	If the option names no file, the error log file name on Unix and Unix-like systems is ``*`host_name`*.err`` in the data directory. The file name on Windows is the same, unless the [`--pid-file`](server-system-variables.md) option is specified. In that case, the file name is the PID file base name with a suffix of `.err` in the data directory.
	If the option names a file, the error log file has that name (with an `.err` suffix added if the name has no suffix), located under the data directory unless an absolute path name is given to specify a different location.
	On Windows, `--console` takes precedence over `--log-error` if both are given. In this case, the server writes the error log to the console rather than to a file. (In MySQL 5.5 and 5.6, this is reversed: `--log-error` takes precedence over `--console` if both are given.)
- [``--log-isam[=*`file_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_log-isam)
	| Command-Line Format | `--log-isam[=file_name]` |
	| --- | --- |
	| Type | File name |
	Log all `MyISAM` changes to this file (used only when debugging `MyISAM`).
- `--log-raw`
	| Command-Line Format | `--log-raw[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Passwords in certain statements written to the general query log, slow query log, and binary log are rewritten by the server not to occur literally in plain text. Password rewriting can be suppressed for the general query log by starting the server with the `--log-raw` option. This option may be useful for diagnostic purposes, to see the exact text of statements as received by the server, but for security reasons is not recommended for production use.
	If a query rewrite plugin is installed, the `--log-raw` option affects statement logging as follows:
	- Without `--log-raw`, the server logs the statement returned by the query rewrite plugin. This may differ from the statement as received.
	- With `--log-raw`, the server logs the original statement as received.
	For more information, see [Section 6.1.2.3, “Passwords and Logging”](password-logging.md).
- `--log-short-format`
	| Command-Line Format | `--log-short-format[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Log less information to the slow query log, if it has been activated.
- ``--log-tc=*`file_name`*``
	| Command-Line Format | `--log-tc=file_name` |
	| --- | --- |
	| Type | File name |
	| Default Value | `tc.log` |
	The name of the memory-mapped transaction coordinator log file (for XA transactions that affect multiple storage engines when the binary log is disabled). The default name is `tc.log`. The file is created under the data directory if not given as a full path name. This option is unused.
- ``--log-tc-size=*`size`*``
	| Command-Line Format | `--log-tc-size=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `6 * page size` |
	| Minimum Value | `6 * page size` |
	| Maximum Value (64-bit platforms) | `18446744073709551615` |
	| Maximum Value (32-bit platforms) | `4294967295` |
	The size in bytes of the memory-mapped transaction coordinator log. The default and minimum values are 6 times the page size, and the value must be a multiple of the page size. (Before MySQL 5.7.21, the default size is 24KB.)
- [``--log-warnings[=*`level`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_log-warnings), ``-W [*`level`*]``
	| Command-Line Format | `--log-warnings[=#]` |
	| --- | --- |
	| Deprecated | Yes |
	| System Variable | `log_warnings` |
	| Scope | Global |
	| Dynamic | Yes |
	| Type | Integer |
	| Default Value | `2` |
	| Minimum Value | `0` |
	| Maximum Value (64-bit platforms) | `18446744073709551615` |
	| Maximum Value (32-bit platforms) | `4294967295` |
	Note
	The [`log_error_verbosity`](server-system-variables.md) system variable is preferred over, and should be used instead of, the `--log-warnings` option or [`log_warnings`](server-system-variables.md) system variable. For more information, see the descriptions of [`log_error_verbosity`](server-system-variables.md) and [`log_warnings`](server-system-variables.md). The `--log-warnings` command-line option and [`log_warnings`](server-system-variables.md) system variable are deprecated; expect them to be removed in a future release of MySQL.
	Whether to produce additional warning messages to the error log. This option is enabled by default. To disable it, use `--log-warnings=0`. Specifying the option without a *`level`* value increments the current value by 1. The server logs messages about statements that are unsafe for statement-based logging if the value is greater than 0. Aborted connections and access-denied errors for new connection attempts are logged if the value is greater than 1. See [Section B.3.2.9, “Communication Errors and Aborted Connections”](communication-errors.md).
- `--memlock`
	| Command-Line Format | `--memlock[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Lock the [**mysqld**](mysqld.md) process in memory. This option might help if you have a problem where the operating system is causing [**mysqld**](mysqld.md) to swap to disk.
	`--memlock` works on systems that support the `mlockall()` system call; this includes Solaris, most Linux distributions that use a 2.4 or higher kernel, and perhaps other Unix systems. On Linux systems, you can tell whether or not `mlockall()` (and thus this option) is supported by checking to see whether or not it is defined in the system `mman.h` file, like this:
	```
	$> grep mlockall /usr/include/sys/mman.h
	```
	If `mlockall()` is supported, you should see in the output of the previous command something like the following:
	```
	extern int mlockall (int __flags) __THROW;
	```
	Important
	Use of this option may require you to run the server as `root`, which, for reasons of security, is normally not a good idea. See [Section 6.1.5, “How to Run MySQL as a Normal User”](changing-mysql-user.md).
	On Linux and perhaps other systems, you can avoid the need to run the server as `root` by changing the `limits.conf` file. See the notes regarding the memlock limit in [Section 8.12.4.3, “Enabling Large Page Support”](large-page-support.md).
	You must not use this option on a system that does not support the `mlockall()` system call; if you do so, [**mysqld**](mysqld.md) is very likely to exit as soon as you try to start it.
- ``--myisam-block-size=*`N`*``
	| Command-Line Format | `--myisam-block-size=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `1024` |
	| Minimum Value | `1024` |
	| Maximum Value | `16384` |
	The block size to be used for `MyISAM` index pages.
- `--no-defaults`
	Do not read any option files. If program startup fails due to reading unknown options from an option file, `--no-defaults` can be used to prevent them from being read. This must be the first option on the command line if it is used.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- `--old-style-user-limits`
	| Command-Line Format | `--old-style-user-limits[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	Enable old-style user limits. (Before MySQL 5.0.3, account resource limits were counted separately for each host from which a user connected rather than per account row in the `user` table.) See [Section 6.2.16, “Setting Account Resource Limits”](user-resources.md).
- [``--partition[=*`value`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_partition)
	| Command-Line Format | `--partition[={OFF\|ON}]` |
	| --- | --- |
	| Deprecated | Yes |
	| Disabled by | `skip-partition` |
	| Type | Boolean |
	| Default Value | `ON` |
	Enables or disables user-defined partitioning support in the MySQL Server.
	This option is deprecated in MySQL 5.7.16, and is removed from MySQL 8.0 because in MySQL 8.0, the partitioning engine is replaced by native partitioning, which cannot be disabled.
- `--performance-schema-xxx`
	Configure a Performance Schema option. For details, see [Section 25.14, “Performance Schema Command Options”](performance-schema-options.md).
- ``--plugin-load=*`plugin_list`*``
	| Command-Line Format | `--plugin-load=plugin_list` |
	| --- | --- |
	| Type | String |
	This option tells the server to load the named plugins at startup. If multiple `--plugin-load` options are given, only the last one applies. Additional plugins to load may be specified using `--plugin-load-add` options.
	The option value is a semicolon-separated list of *`plugin_library`* and *`name`* `=` *`plugin_library`* values. Each *`plugin_library`* is the name of a library file that contains plugin code, and each *`name`* is the name of a plugin to load. If a plugin library is named without any preceding plugin name, the server loads all plugins in the library. With a preceding plugin name, the server loads only the named plugin from the libary. The server looks for plugin library files in the directory named by the [`plugin_dir`](server-system-variables.md) system variable.
	For example, if plugins named `myplug1` and `myplug2` are contained in the plugin library files `myplug1.so` and `myplug2.so`, use this option to perform an early plugin load:
	```
	mysqld --plugin-load="myplug1=myplug1.so;myplug2=myplug2.so"
	```
	Quotes surround the argument value because otherwise some command interpreters interpret semicolon (`;`) as a special character. (For example, Unix shells treat it as a command terminator.)
	Each named plugin is loaded for a single invocation of [**mysqld**](mysqld.md) only. After a restart, the plugin is not loaded unless `--plugin-load` is used again. This is in contrast to [`INSTALL PLUGIN`](install-plugin.md), which adds an entry to the `mysql.plugins` table to cause the plugin to be loaded for every normal server startup.
	During the normal startup sequence, the server determines which plugins to load by reading the `mysql.plugins` system table. If the server is started with the `--skip-grant-tables` option, plugins registered in the `mysql.plugins` table are not loaded and are unavailable. `--plugin-load` enables plugins to be loaded even when `--skip-grant-tables` is given. `--plugin-load` also enables plugins to be loaded at startup that cannot be loaded at runtime.
	This option does not set a corresponding system variable. The output of [`SHOW PLUGINS`](show-plugins.md) provides information about loaded plugins. More detailed information can be found in the Information Schema [`PLUGINS`](information-schema-plugins-table.md) table. See [Section 5.5.2, “Obtaining Server Plugin Information”](obtaining-plugin-information.md).
	For additional information about plugin loading, see [Section 5.5.1, “Installing and Uninstalling Plugins”](plugin-loading.md).
- ``--plugin-load-add=*`plugin_list`*``
	| Command-Line Format | `--plugin-load-add=plugin_list` |
	| --- | --- |
	| Type | String |
	This option complements the `--plugin-load` option. `--plugin-load-add` adds a plugin or plugins to the set of plugins to be loaded at startup. The argument format is the same as for `--plugin-load`. `--plugin-load-add` can be used to avoid specifying a large set of plugins as a single long unwieldy `--plugin-load` argument.
	`--plugin-load-add` can be given in the absence of `--plugin-load`, but any instance of `--plugin-load-add` that appears before `--plugin-load` has no effect because `--plugin-load` resets the set of plugins to load. In other words, these options:
	```
	--plugin-load=x --plugin-load-add=y
	```
	are equivalent to this option:
	```
	--plugin-load="x;y"
	```
	But these options:
	```
	--plugin-load-add=y --plugin-load=x
	```
	are equivalent to this option:
	```
	--plugin-load=x
	```
	This option does not set a corresponding system variable. The output of [`SHOW PLUGINS`](show-plugins.md) provides information about loaded plugins. More detailed information can be found in the Information Schema [`PLUGINS`](information-schema-plugins-table.md) table. See [Section 5.5.2, “Obtaining Server Plugin Information”](obtaining-plugin-information.md).
	For additional information about plugin loading, see [Section 5.5.1, “Installing and Uninstalling Plugins”](plugin-loading.md).
- ``--plugin-*`xxx`*``
	Specifies an option that pertains to a server plugin. For example, many storage engines can be built as plugins, and for such engines, options for them can be specified with a `--plugin` prefix. Thus, the [`--innodb-file-per-table`](innodb-parameters.md) option for `InnoDB` can be specified as [`--plugin-innodb-file-per-table`](innodb-parameters.md).
	For boolean options that can be enabled or disabled, the `--skip` prefix and other alternative formats are supported as well (see [Section 4.2.2.4, “Program Option Modifiers”](option-modifiers.md)). For example, [`--skip-plugin-innodb-file-per-table`](innodb-parameters.md) disables [`innodb-file-per-table`](innodb-parameters.md).
	The rationale for the `--plugin` prefix is that it enables plugin options to be specified unambiguously if there is a name conflict with a built-in server option. For example, were a plugin writer to name a plugin “sql” and implement a “mode” option, the option name might be `--sql-mode`, which would conflict with the built-in option of the same name. In such cases, references to the conflicting name are resolved in favor of the built-in option. To avoid the ambiguity, users can specify the plugin option as `--plugin-sql-mode`. Use of the `--plugin` prefix for plugin options is recommended to avoid any question of ambiguity.
- ``--port=*`port_num`*``, ``-P *`port_num`*``
	| Command-Line Format | `--port=port_num` |
	| --- | --- |
	| System Variable | `port` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Integer |
	| Default Value | `3306` |
	| Minimum Value | `0` |
	| Maximum Value | `65535` |
	The port number to use when listening for TCP/IP connections. On Unix and Unix-like systems, the port number must be 1024 or higher unless the server is started by the `root` operating system user. Setting this option to 0 causes the default value to be used.
- ``--port-open-timeout=*`num`*``
	| Command-Line Format | `--port-open-timeout=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `0` |
	On some systems, when the server is stopped, the TCP/IP port might not become available immediately. If the server is restarted quickly afterward, its attempt to reopen the port can fail. This option indicates how many seconds the server should wait for the TCP/IP port to become free if it cannot be opened. The default is not to wait.
- `--print-defaults`
	Print the program name and all options that it gets from option files. Password values are masked. This must be the first option on the command line if it is used, except that it may be used immediately after `--defaults-file` or `--defaults-extra-file`.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- [``--remove           [*`service_name`*]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_remove)
	| Command-Line Format | `--remove [service_name]` |
	| --- | --- |
	| Platform Specific | Windows |
	(Windows only) Remove a MySQL Windows service. The default service name is `MySQL` if no *`service_name`* value is given. For more information, see [Section 2.3.4.8, “Starting MySQL as a Windows Service”](windows-start-service.md).
- `--safe-user-create`
	| Command-Line Format | `--safe-user-create[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	If this option is enabled, a user cannot create new MySQL users by using the [`GRANT`](grant.md) statement unless the user has the [`INSERT`](privileges-provided.md) privilege for the `mysql.user` system table or any column in the table. If you want a user to have the ability to create new users that have those privileges that the user has the right to grant, you should grant the user the following privilege:
	```
	GRANT INSERT(user) ON mysql.user TO 'user_name'@'host_name';
	```
	This ensures that the user cannot change any privilege columns directly, but has to use the [`GRANT`](grant.md) statement to give privileges to other users.
- `--skip-grant-tables`
	| Command-Line Format | `--skip-grant-tables[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	This option affects the server startup sequence:
	- `--skip-grant-tables` causes the server not to read the grant tables in the `mysql` system database, and thus to start without using the privilege system at all. This gives anyone with access to the server *unrestricted access to all databases*.
		To cause a server started with `--skip-grant-tables` to load the grant tables at runtime, perform a privilege-flushing operation, which can be done in these ways:
		- Issue a MySQL [`FLUSH                   PRIVILEGES`](flush.md) statement after connecting to the server.
		- Execute a [**mysqladmin flush-privileges**](mysqladmin.md) or [**mysqladmin reload**](mysqladmin.md) command from the command line.
		Privilege flushing might also occur implicitly as a result of other actions performed after startup, thus causing the server to start using the grant tables. For example, [**mysql\_upgrade**](mysql-upgrade.md) flushes the privileges during the upgrade procedure.
	- `--skip-grant-tables` causes the server not to load certain other objects registered in the `mysql` system database:
		- Plugins installed using [`INSTALL                   PLUGIN`](install-plugin.md) and registered in the `mysql.plugin` system table.
			To cause plugins to be loaded even when using `--skip-grant-tables`, use the `--plugin-load` or `--plugin-load-add` option.
		- Scheduled events installed using [`CREATE EVENT`](create-event.md) and registered in the `mysql.event` system table.
		- Loadable functions installed using [`CREATE                   FUNCTION`](create-function-loadable.md) and registered in the `mysql.func` system table.
	- `--skip-grant-tables` causes the [`disabled_storage_engines`](server-system-variables.md) system variable to have no effect.
- `--skip-host-cache`
	| Command-Line Format | `--skip-host-cache` |
	| --- | --- |
	Disable use of the internal host cache for faster name-to-IP resolution. With the cache disabled, the server performs a DNS lookup every time a client connects.
	Use of `--skip-host-cache` is similar to setting the [`host_cache_size`](server-system-variables.md) system variable to 0, but [`host_cache_size`](server-system-variables.md) is more flexible because it can also be used to resize, enable, or disable the host cache at runtime, not just at server startup.
	Starting the server with `--skip-host-cache` does not prevent runtime changes to the value of [`host_cache_size`](server-system-variables.md), but such changes have no effect and the cache is not re-enabled even if [`host_cache_size`](server-system-variables.md) is set larger than 0.
	For more information about how the host cache works, see [Section 5.1.11.2, “DNS Lookups and the Host Cache”](host-cache.md).
- [`--skip-innodb`](innodb-parameters.md)
	Disable the `InnoDB` storage engine. In this case, because the default storage engine is [`InnoDB`](innodb-storage-engine.md), the server cannot start unless you also use [`--default-storage-engine`](server-system-variables.md) and [`--default-tmp-storage-engine`](server-system-variables.md) to set the default to some other engine for both permanent and `TEMPORARY` tables.
	The `InnoDB` storage engine cannot be disabled, and the [`--skip-innodb`](innodb-parameters.md) option is deprecated and has no effect. Its use results in a warning. Expect this option to be removed in a future release of MySQL.
- `--skip-new`
	| Command-Line Format | `--skip-new` |
	| --- | --- |
	This option disables (what used to be considered) new, possibly unsafe behaviors. It results in these settings: [`delay_key_write=OFF`](server-system-variables.md), [`concurrent_insert=NEVER`](server-system-variables.md), [`automatic_sp_privileges=OFF`](server-system-variables.md). It also causes [`OPTIMIZE TABLE`](optimize-table.md) to be mapped to [`ALTER TABLE`](alter-table.md) for storage engines for which [`OPTIMIZE           TABLE`](optimize-table.md) is not supported.
- `--skip-partition`
	| Command-Line Format | `--skip-partition`  `--disable-partition` |
	| --- | --- |
	| Deprecated | Yes |
	Disables user-defined partitioning. Partitioned tables can be seen using [`SHOW TABLES`](show-tables.md) or by querying the Information Schema [`TABLES`](information-schema-tables-table.md) table, but cannot be created or modified, nor can data in such tables be accessed. All partition-specific columns in the Information Schema [`PARTITIONS`](information-schema-partitions-table.md) table display `NULL`.
	Since [`DROP TABLE`](drop-table.md) removes table definition (`.frm`) files, this statement works on partitioned tables even when partitioning is disabled using the option. The statement, however, does not remove partition definitions associated with partitioned tables in such cases. For this reason, you should avoid dropping partitioned tables with partitioning disabled, or take action to remove orphaned `.par` files manually (if present).
	Note
	In MySQL 5.7, partition definition (`.par`) files are no longer created for partitioned `InnoDB` tables. Instead, partition definitions are stored in the `InnoDB` internal data dictionary. Partition definition (`.par`) files continue to be used for partitioned `MyISAM` tables.
	This option is deprecated in MySQL 5.7.16, and is removed from MySQL 8.0 because in MySQL 8.0, the partitioning engine is replaced by native partitioning, which cannot be disabled.
- `--skip-show-database`
	| Command-Line Format | `--skip-show-database` |
	| --- | --- |
	| System Variable | `skip_show_database` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Boolean |
	| Default Value | `OFF` |
	This option sets the [`skip_show_database`](server-system-variables.md) system variable that controls who is permitted to use the [`SHOW DATABASES`](show-databases.md) statement. See [Section 5.1.7, “Server System Variables”](server-system-variables.md).
- `--skip-stack-trace`
	| Command-Line Format | `--skip-stack-trace` |
	| --- | --- |
	Do not write stack traces. This option is useful when you are running [**mysqld**](mysqld.md) under a debugger. On some systems, you also must use this option to get a core file. See [Section 5.8, “Debugging MySQL”](debugging-mysql.md).
- ``--slow-start-timeout=*`timeout`*``
	| Command-Line Format | `--slow-start-timeout=#` |
	| --- | --- |
	| Type | Integer |
	| Default Value | `15000` |
	This option controls the Windows service control manager's service start timeout. The value is the maximum number of milliseconds that the service control manager waits before trying to kill the windows service during startup. The default value is 15000 (15 seconds). If the MySQL service takes too long to start, you may need to increase this value. A value of 0 means there is no timeout.
- ``--socket=*`path`*``
	| Command-Line Format | `--socket={file_name\|pipe_name}` |
	| --- | --- |
	| System Variable | `socket` |
	| Scope | Global |
	| Dynamic | No |
	| Type | String |
	| Default Value (Windows) | `MySQL` |
	| Default Value (Other) | `/tmp/mysql.sock` |
	On Unix, this option specifies the Unix socket file to use when listening for local connections. The default value is `/tmp/mysql.sock`. If this option is given, the server creates the file in the data directory unless an absolute path name is given to specify a different directory. On Windows, the option specifies the pipe name to use when listening for local connections that use a named pipe. The default value is `MySQL` (not case-sensitive).
- [``--sql-mode=*`value`*[,*`value`*[,*`value`*...]]``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_sql-mode)
	| Command-Line Format | `--sql-mode=name` |
	| --- | --- |
	| System Variable | `sql_mode` |
	| Scope | Global, Session |
	| Dynamic | Yes |
	| Type | Set |
	| Default Value | `ONLY_FULL_GROUP_BY STRICT_TRANS_TABLES NO_ZERO_IN_DATE NO_ZERO_DATE ERROR_FOR_DIVISION_BY_ZERO NO_AUTO_CREATE_USER NO_ENGINE_SUBSTITUTION` |
	| Valid Values | `ALLOW_INVALID_DATES`  `ANSI_QUOTES`  `ERROR_FOR_DIVISION_BY_ZERO`  `HIGH_NOT_PRECEDENCE`  `IGNORE_SPACE`  `NO_AUTO_CREATE_USER`  `NO_AUTO_VALUE_ON_ZERO`  `NO_BACKSLASH_ESCAPES`  `NO_DIR_IN_CREATE`  `NO_ENGINE_SUBSTITUTION`  `NO_FIELD_OPTIONS`  `NO_KEY_OPTIONS`  `NO_TABLE_OPTIONS`  `NO_UNSIGNED_SUBTRACTION`  `NO_ZERO_DATE`  `NO_ZERO_IN_DATE`  `ONLY_FULL_GROUP_BY`  `PAD_CHAR_TO_FULL_LENGTH`  `PIPES_AS_CONCAT`  `REAL_AS_FLOAT`  `STRICT_ALL_TABLES`  `STRICT_TRANS_TABLES` |
	Set the SQL mode. See [Section 5.1.10, “Server SQL Modes”](sql-mode.md).
	Note
	MySQL installation programs may configure the SQL mode during the installation process. If the SQL mode differs from the default or from what you expect, check for a setting in an option file that the server reads at startup.
- `--ssl`, `--skip-ssl`
	| Command-Line Format | `--ssl[={OFF\|ON}]` |
	| --- | --- |
	| Disabled by | `skip-ssl` |
	| Type | Boolean |
	| Default Value | `ON` |
	The `--ssl` option specifies that the server permits but does not require encrypted connections. This option is enabled by default.
	`--ssl` can be specified in negated form as `--skip-ssl` or a synonym (`--ssl=OFF`, `--disable-ssl`). In this case, the option specifies that the server does *not* permit encrypted connections, regardless of the settings of the ``tls_*`xxx`*`` and ``ssl_*`xxx`*`` system variables.
	For more information about configuring whether the server permits clients to connect using SSL and indicating where to find SSL keys and certificates, see [Section 6.3.1, “Configuring MySQL to Use Encrypted Connections”](using-encrypted-connections.md), which also describes server capabilities for certificate and key file autogeneration and autodiscovery. Consider setting at least the [`ssl_cert`](server-system-variables.md) and [`ssl_key`](server-system-variables.md) system variables on the server side and the [`--ssl-ca`](connection-options.md) (or [`--ssl-capath`](connection-options.md)) option on the client side.
- `--standalone`
	| Command-Line Format | `--standalone` |
	| --- | --- |
	| Platform Specific | Windows |
	Available on Windows only; instructs the MySQL server not to run as a service.
- `--super-large-pages`
	| Command-Line Format | `--super-large-pages[={OFF\|ON}]` |
	| --- | --- |
	| Platform Specific | Solaris |
	| Type | Boolean |
	| Default Value | `OFF` |
	Standard use of large pages in MySQL attempts to use the largest size supported, up to 4MB. Under Solaris, a “super large pages” feature enables uses of pages up to 256MB. This feature is available for recent SPARC platforms. It can be enabled or disabled by using the `--super-large-pages` or `--skip-super-large-pages` option.
- `--symbolic-links`, `--skip-symbolic-links`
	| Command-Line Format | `--symbolic-links[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `ON` |
	Enable or disable symbolic link support. On Unix, enabling symbolic links means that you can link a `MyISAM` index file or data file to another directory with the `INDEX DIRECTORY` or `DATA DIRECTORY` option of the [`CREATE TABLE`](create-table.md) statement. If you delete or rename the table, the files that its symbolic links point to also are deleted or renamed. See [Section 8.12.3.2, “Using Symbolic Links for MyISAM Tables on Unix”](symbolic-links-to-tables.md).
	This option has no meaning on Windows.
- `--sysdate-is-now`
	| Command-Line Format | `--sysdate-is-now[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `OFF` |
	[`SYSDATE()`](date-and-time-functions.md) by default returns the time at which it executes, not the time at which the statement in which it occurs begins executing. This differs from the behavior of [`NOW()`](date-and-time-functions.md). This option causes [`SYSDATE()`](date-and-time-functions.md) to be a synonym for [`NOW()`](date-and-time-functions.md). For information about the implications for binary logging and replication, see the description for [`SYSDATE()`](date-and-time-functions.md) in [Section 12.7, “Date and Time Functions”](date-and-time-functions.md) and for `SET           TIMESTAMP` in [Section 5.1.7, “Server System Variables”](server-system-variables.md).
- `--tc-heuristic-recover={COMMIT|ROLLBACK}`
	| Command-Line Format | `--tc-heuristic-recover=name` |
	| --- | --- |
	| Type | Enumeration |
	| Default Value | `OFF` |
	| Valid Values | `OFF`  `COMMIT`  `ROLLBACK` |
	The decision to use in a manual heuristic recovery.
	If a `--tc-heuristic-recover` option is specified, the server exits regardless of whether manual heuristic recovery is successful.
	On systems with more than one storage engine capable of two-phase commit, the `ROLLBACK` option is not safe and causes recovery to halt with the following error:
	```
	[ERROR] --tc-heuristic-recover rollback
	strategy is not safe on systems with more than one 2-phase-commit-capable
	storage engine. Aborting crash recovery.
	```
- `--temp-pool`
	| Command-Line Format | `--temp-pool[={OFF\|ON}]` |
	| --- | --- |
	| Deprecated | Yes |
	| Type | Boolean |
	| Default Value (Linux) | `ON` |
	| Default Value (Other) | `OFF` |
	This option is ignored except on Linux. On Linux, it causes most temporary files created by the server to use a small set of names, rather than a unique name for each new file. This works around a problem in the Linux kernel dealing with creating many new files with different names. With the old behavior, Linux seems to “leak” memory, because it is being allocated to the directory entry cache rather than to the disk cache.
	As of MySQL 5.7.18, this option is deprecated and is removed in MySQL 8.0.
- ``--transaction-isolation=*`level`*``
	| Command-Line Format | `--transaction-isolation=name` |
	| --- | --- |
	| System Variable | `transaction_isolation` |
	| Scope | Global, Session |
	| Dynamic | Yes |
	| Type | Enumeration |
	| Default Value | `REPEATABLE-READ` |
	| Valid Values | `READ-UNCOMMITTED`  `READ-COMMITTED`  `REPEATABLE-READ`  `SERIALIZABLE` |
	Sets the default transaction isolation level. The `level` value can be [`READ-UNCOMMITTED`](innodb-transaction-isolation-levels.md), [`READ-COMMITTED`](innodb-transaction-isolation-levels.md), [`REPEATABLE-READ`](innodb-transaction-isolation-levels.md), or [`SERIALIZABLE`](innodb-transaction-isolation-levels.md). See [Section 13.3.6, “SET TRANSACTION Statement”](set-transaction.md).
	The default transaction isolation level can also be set at runtime using the [`SET           TRANSACTION`](set-transaction.md) statement or by setting the [`tx_isolation`](server-system-variables.md) (or, as of MySQL 5.7.20, [`transaction_isolation`](server-system-variables.md)) system variable.
- `--transaction-read-only`
	| Command-Line Format | `--transaction-read-only[={OFF\|ON}]` |
	| --- | --- |
	| System Variable | `transaction_read_only` |
	| Scope | Global, Session |
	| Dynamic | Yes |
	| Type | Boolean |
	| Default Value | `OFF` |
	Sets the default transaction access mode. By default, read-only mode is disabled, so the mode is read/write.
	To set the default transaction access mode at runtime, use the [`SET TRANSACTION`](set-transaction.md) statement or set the [`tx_read_only`](server-system-variables.md) (or, as of MySQL 5.7.20, [`transaction_read_only`](server-system-variables.md)) system variable. See [Section 13.3.6, “SET TRANSACTION Statement”](set-transaction.md).
- ``--tmpdir=*`dir_name`*``, ``-t *`dir_name`*``
	| Command-Line Format | `--tmpdir=dir_name` |
	| --- | --- |
	| System Variable | `tmpdir` |
	| Scope | Global |
	| Dynamic | No |
	| Type | Directory name |
	The path of the directory to use for creating temporary files. It might be useful if your default `/tmp` directory resides on a partition that is too small to hold temporary tables. This option accepts several paths that are used in round-robin fashion. Paths should be separated by colon characters (`:`) on Unix and semicolon characters (`;`) on Windows.
	`--tmpdir` can be a non-permanent location, such as a directory on a memory-based file system or a directory that is cleared when the server host restarts. If the MySQL server is acting as a replica, and you are using a non-permanent location for `--tmpdir`, consider setting a different temporary directory for the replica using the [`slave_load_tmpdir`](replication-options-replica.md) system variable. For a replication replica, the temporary files used to replicate [`LOAD DATA`](load-data.md) statements are stored in this directory, so with a permanent location they can survive machine restarts, although replication can now continue after a restart if the temporary files have been removed.
	For more information about the storage location of temporary files, see [Section B.3.3.5, “Where MySQL Stores Temporary Files”](temporary-files.md).
- ``--user={*`user_name`*|*`user_id`*}``, ``-u           {*`user_name`*|*`user_id`*}``
	| Command-Line Format | `--user=name` |
	| --- | --- |
	| Type | String |
	Run the [**mysqld**](mysqld.md) server as the user having the name *`user_name`* or the numeric user ID *`user_id`*. (“User” in this context refers to a system login account, not a MySQL user listed in the grant tables.)
	This option is *mandatory* when starting [**mysqld**](mysqld.md) as `root`. The server changes its user ID during its startup sequence, causing it to run as that particular user rather than as `root`. See [Section 6.1.1, “Security Guidelines”](security-guidelines.md).
	To avoid a possible security hole where a user adds a `--user=root` option to a `my.cnf` file (thus causing the server to run as `root`), [**mysqld**](mysqld.md) uses only the first `--user` option specified and produces a warning if there are multiple `--user` options. Options in `/etc/my.cnf` and `$MYSQL_HOME/my.cnf` are processed before command-line options, so it is recommended that you put a `--user` option in `/etc/my.cnf` and specify a value other than `root`. The option in `/etc/my.cnf` is found before any other `--user` options, which ensures that the server runs as a user other than `root`, and that a warning results if any other `--user` option is found.
- [`--validate-user-plugins[={OFF|ON}]`](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/server-options.html#option_mysqld_validate-user-plugins)
	| Command-Line Format | `--validate-user-plugins[={OFF\|ON}]` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `ON` |
	If this option is enabled (the default), the server checks each user account and produces a warning if conditions are found that would make the account unusable:
	- The account requires an authentication plugin that is not loaded.
	- The account requires the `sha256_password` authentication plugin but the server was started with neither SSL nor RSA enabled as required by this plugin.
	Enabling `--validate-user-plugins` slows down server initialization and [`FLUSH           PRIVILEGES`](flush.md). If you do not require the additional checking, you can disable this option at startup to avoid the performance decrement.
- `--verbose`, `-v`
	Use this option with the `--help` option for detailed help.
- `--version`, `-V`
	Display version information and exit.