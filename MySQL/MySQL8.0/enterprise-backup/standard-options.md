---
title: "20.1 General Options"
book: "MySQL Enterprise Backup User's Guide (Version 8.0.46)"
version: "8.0"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/8.0/en/standard-options.html"
tags:
  - mysql
  - mysql-8.0
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 8.0.46)

The general options are options of a general nature, or options that are not classified under any other specific option group:

- The following general options also exist for the **mysql** command. Full descriptions for these options can be found in the MySQL reference manual, for example in [Server Option, System Variable, and Status Variable Reference](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/server-option-variable-reference.html). *These options must be specified ahead of any other **mysqlbackup** options, including the rest of the general options*:
	- [`--print-defaults`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_print-defaults): Print the program argument list and exit.
	- [`--no-defaults`](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_no-defaults): Don't read default options from any option file.
	- [``--defaults-file=*`PATH`*``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-file): Only read default options from the given file. It has to be the first option to be specified, if used.
	- [``--defaults-extra-file=*`PATH`*``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-extra-file): Read this file after the global files are read.
	- [``--defaults-group-suffix=*`str`*``](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/option-file-options.html#option_general_defaults-group-suffix): Also read option groups with the usual names and a suffix of *`str`*.
- The following options are also common between **mysqlbackup** and **mysql**, and full descriptions for them can be found in the MySQL reference manual, accessible through, e.g., [Server Option, System Variable, and Status Variable Reference](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/server-option-variable-reference.html). However, **mysqlbackup** does not accept any short forms for these options as **mysql** does (for example, you must use `--help` instead of `-h` for **mysqlbackup**):
	- `--help`: Display help.
	- `--version`: Display version information.
- More general options are available for **mysqlbackup**:
	- `--verbose`: Print more verbose information.
		*For release 8.0.27 and later:* `--verbose` is synonymous with `--trace=1`.
	- `--debug` = *`STRING`*: Print additional debug information.
		*For release 8.0.26 and earlier:* The option accepts one or more of the following arguments:
		- `all`: Print additional debug information for all operations
		- `sbt`: Print additional debug information for [operations using the System Backup to Tape (SBT)](meb-mms.md) interface
		- null: When a null string or no argument at all is specified for the option, **mysqlbackup** behaves as if the `--verbose` option is used.
		*For release 8.0.27 and later:* The option accepts one or more of the following arguments (multiple values should be separated by semicolons (;)):
		- `all`: Print additional debug information for all operations
		- `sbt`: Print additional debug information for [operations using the System Backup to Tape (SBT)](meb-mms.md) interface
		- `page_validation`: Print debug information for validation operations.
		- `hole_punch`: Print debug information for transparent page compression for backups.
		- `tablespace_flags`: Print flags read from tablespaces.
		- `io_file`: Print debug information for reading and writing files.
		- `keyring_migration_tool`: Print debug information on keyring migration operations.
	- `--force`: *For release 8.0.27 and earlier only (deprecated and ignored since release 8.0.28):* By default, some of the operations halt rather than overwrite any user data or log files when told to write to existing files. `--force` allows the following:
		Warning
		For any restore operations, do NOT attempt to restore data to a non-empty data directory using the `--force` option; doing so may cause data corruption and other unexpected behaviors. Do not use the `--force` option with a [`copy-back`](backup-commands-restore.md) or a [`copy-back-and-apply-log`](backup-commands-restore.md) operation.
		- Overwriting of InnoDB data and log files during the `apply-log` and `apply-incremental-backup` operations.
		- Replacing of an image file during an `backup-to-image` or `backup-dir-to-image` operation.
	- `--trace` = *`level`*
		| Command-Line Format | `--trace=LEVEL` |
		| --- | --- |
		| Type | Enumeration |
		| Default Value | `0` |
		| Valid Values | `0`  `1`  `2`  `3` |
		Trace level of **mysqlbackup** messages. The permissible levels, in the order of increasing fineness, are:
		- 0 - INFO (information, warnings, errors)
		- 1 - FINE (more information given than at trace level 0)
		- 2 - FINER (finer level of information given than at trace level 1)
		- 3 - FINEST (finest level of information that can be given)
	- `--error-code` = *`CODE`*
		| Command-Line Format | `--error-code` |
		| --- | --- |
		| Type | Numeric |
		| Minimum Value | `0` |
		| Maximum Value | `19` |
		Specifies the exit code for which the [`print-message`](backup-commands-other.md) command prints the corresponding exit message. See [Section 17.1, “Exit codes of MySQL Enterprise Backup”](meb-exitcodes.md) for details.
	- `--enable-cleartext-plugin`
		*For MySQL Enterprise Backup 8.0.22 and later:* Enables the [Client-Side Cleartext Pluggable Authentication](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/cleartext-pluggable-authentication.html). Required when using simple LDAP authentication. See [Chapter 16, *Using LDAP for Server Authentication*](meb-ldap.md).
	- `--plugin-dir` = *`plugin-dir`*
		*For MySQL Enterprise Backup 8.0.22 and later:* Specifies the directory for the client-side plugins. Required when using SASL-based LDAP authentication *AND* the client-side plugin is not in the server's plugin directory. See [Chapter 16, *Using LDAP for Server Authentication*](meb-ldap.md) for details.