---
title: "4.4.2 mysql_install_db — Initialize MySQL Data Directory"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-install-db.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.4.2 mysql\_install\_db — Initialize MySQL Data Directory

Note

**mysql\_install\_db** is deprecated as of MySQL 5.7.6 because its functionality has been integrated into [**mysqld**](mysqld.md), the MySQL server. To initialize a MySQL installation, invoke [**mysqld**](mysqld.md) with the [`--initialize`](server-options.md) or [`--initialize-insecure`](server-options.md) option. For more information, see [Section 2.9.1, “Initializing the Data Directory”](data-directory-initialization.md). You should expect **mysql\_install\_db** to be removed in a future MySQL release.

**mysql\_install\_db** handles initialization tasks that must be performed before the MySQL server, [**mysqld**](mysqld.md), is ready to use:

- It initializes the MySQL data directory and creates the system tables that it contains.
- It initializes the [system tablespace](glossary.md) and related data structures needed to manage [`InnoDB`](innodb-storage-engine.md) tables.
- It loads the server-side help tables.
- It installs the `sys` schema.
- It creates an administrative account. Older versions of **mysql\_install\_db** may create anonymous-user accounts.

#### Secure-by-Default Deployment

Current versions of **mysql\_install\_db** produce a MySQL deployment that is secure by default, with these characteristics:

- A single administrative account named `'root'@'localhost'` is created with a randomly generated password, which is marked expired.
- No anonymous-user accounts are created.
- No `test` database accessible by all users is created.
- ``--admin-*`xxx`*`` options are available to control characteristics of the administrative account.
- The `--random-password-file` option is available to control where the random password is written.
- The `--insecure` option is available to suppress random password generation.

If **mysql\_install\_db** generates a random administative password, it writes the password to a file and displays the file name. The password entry includes a timestamp to indicate when it was written. By default, the file is `.mysql_secret` in the home directory of the effective user running the script. `.mysql_secret` is created with mode 600 to be accessible only to the operating system user for whom it is created.

Important

When **mysql\_install\_db** generates a random password for the administrative account, it is necessary after **mysql\_install\_db** has been run to start the server, connect using the administrative account with the password written to the `.mysql_secret` file, and specify a new administrative password. Until this is done, the administrative account cannot be used for anything else. To change the password, you can use the [`SET PASSWORD`](set-password.md) statement (for example, with the [**mysql**](mysql.md) or [**mysqladmin**](mysqladmin.md) client). After resetting the password, remove the `.mysql_secret` file; otherwise, if you run [**mysql\_secure\_installation**](mysql-secure-installation.md), that command may see the file and expire the `root` password again as part of ensuring secure deployment.

#### Invocation Syntax

Change location to the MySQL installation directory and use this invocation syntax:

```
bin/mysql_install_db --datadir=path/to/datadir [other_options]
```

The `--datadir` option is mandatory. **mysql\_install\_db** creates the data directory, which must not already exist:

- If the data directory does already exist, you are performing an upgrade operation (not an install operation) and should run [**mysql\_upgrade**](mysql-upgrade.md), not **mysql\_install\_db**. See [Section 4.4.7, “mysql\_upgrade — Check and Upgrade MySQL Tables”](mysql-upgrade.md).
- If the data directory does not exist but **mysql\_install\_db** fails, you must remove any partially created data directory before running **mysql\_install\_db** again.

Because the MySQL server, [**mysqld**](mysqld.md), must access the data directory when it runs later, you should either run **mysql\_install\_db** from the same system account used for running [**mysqld**](mysqld.md), or run it as `root` and specify the `--user` option to indicate the user name that [**mysqld**](mysqld.md) runs under. It might be necessary to specify other options such as `--basedir` if **mysql\_install\_db** does not use the correct location for the installation directory. For example:

```
bin/mysql_install_db --user=mysql \
    --basedir=/opt/mysql/mysql \
    --datadir=/opt/mysql/mysql/data
```

Note

After **mysql\_install\_db** sets up the `InnoDB` [system tablespace](glossary.md), changes to some tablespace characteristics require setting up a whole new [instance](glossary.md). This includes the file name of the first file in the system tablespace and the number of undo logs. If you do not want to use the default values, make sure that the settings for the [`innodb_data_file_path`](innodb-parameters.md) and [`innodb_log_file_size`](innodb-parameters.md) configuration parameters are in place in the MySQL [configuration file](glossary.md) before running **mysql\_install\_db**. Also make sure to specify as necessary other parameters that affect the creation and location of `InnoDB` files, such as [`innodb_data_home_dir`](innodb-parameters.md) and [`innodb_log_group_home_dir`](innodb-parameters.md).

If those options are in your configuration file but that file is not in a location that MySQL reads by default, specify the file location using the `--defaults-extra-file` option when you run **mysql\_install\_db**.

Note

If you have set a custom `TMPDIR` environment variable when performing the installation, and the specified directory is not accessible, **mysql\_install\_db** may fail. If so, unset `TMPDIR` or set `TMPDIR` to point to the system temporary directory (usually `/tmp`).

#### Administrative Account Creation

**mysql\_install\_db** creates an administrative account named `'root'@'localhost'` by default.

**mysql\_install\_db** provides options that enable you to control several aspects of the administrative account:

- To change the user or host parts of the account name, use `--login-path`, or `--admin-user` and `--admin-host`.
- `--insecure` suppresses generation of a random password.
- `--admin-auth-plugin` specifies the authentication plugin.
- `--admin-require-ssl` specifies whether the account must use SSL connections.

For more information, see the descriptions of those options.

**mysql\_install\_db** assigns `mysql.user` system table rows a nonempty `plugin` column value to set the authentication plugin. The default value is `mysql_native_password`. The value can be changed using the `--admin-auth-plugin` option.

#### Default my.cnf File

**mysql\_install\_db** creates no default `my.cnf` file.

Note

As of MySQL 5.7.18, `my-default.cnf` is no longer included in or installed by distribution packages.

With one exception, the settings in the default option file are commented and have no effect. The exception is that the file sets the [`sql_mode`](server-system-variables.md) system variable to `NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES`. This setting produces a server configuration that results in errors rather than warnings for bad data in operations that modify transactional tables. See [Section 5.1.10, “Server SQL Modes”](sql-mode.md).

#### Command Options

**mysql\_install\_db** supports the following options, which can be specified on the command line or in the `[mysql_install_db]` group of an option file. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.8 mysql\_install\_db Options**

| Option Name | Description |
| --- | --- |
| \--admin-auth-plugin | Administrative account authentication plugin |
| \--admin-host | Administrative account name host part |
| \--admin-require-ssl | Require SSL for administrative account |
| \--admin-user | Administrative account name user part |
| \--basedir | Path to base directory |
| \--builddir | Path to build directory (for out-of-source builds) |
| \--datadir | Path to data directory |
| \--defaults | Read default option files |
| \--defaults-extra-file | Read named option file in addition to usual option files |
| \--defaults-file | Read only named option file |
| \--extra-sql-file | Optional SQL file to execute during bootstrap |
| \--help | Display help message and exit |
| \--insecure | Do not generate administrative account random password |
| \--lc-messages | Locale for error messages |
| \--lc-messages-dir | Directory where error messages are installed |
| \--login-file | File to read for login path information |
| \--login-path | Read login path options from.mylogin.cnf |
| \--mysqld-file | Path to mysqld binary |
| \--no-defaults | Read no option files |
| \--random-password-file | File in which to write administrative account random password |
| \--skip-sys-schema | Do not install or upgrade the sys schema |
| \--srcdir | For internal use |
| \--user | Operating system user under which to execute mysqld |
| \--verbose | Verbose mode |
| \--version | Display version information and exit |

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- ``--admin-auth-plugin=*`plugin_name`*``
	| Command-Line Format | `--admin-auth-plugin=plugin_name` |
	| --- | --- |
	| Type | String |
	The authentication plugin to use for the administrative account. The default is `mysql_native_password`.
- ``--admin-host=*`host_name`*``
	| Command-Line Format | `--admin-host=host_name` |
	| --- | --- |
	| Type | String |
	The host part to use for the adminstrative account name. The default is `localhost`. This option is ignored if `--login-path` is also specified.
- `--admin-require-ssl`
	| Command-Line Format | `--admin-require-ssl` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Whether to require SSL for the administrative account. The default is not to require it. With this option enabled, the statement that **mysql\_install\_db** uses to create the account includes a `REQUIRE SSL` clause. As a result, the administrative account must use secure connections when connecting to the server.
- ``--admin-user=*`user_name`*``
	| Command-Line Format | `--admin-user=user_name` |
	| --- | --- |
	| Type | String |
	The user part to use for the adminstrative account name. The default is `root`. This option is ignored if `--login-path` is also specified.
- ``--basedir=*`dir_name`*``
	| Command-Line Format | `--basedir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The path to the MySQL installation directory.
- ``--builddir=*`dir_name`*``
	| Command-Line Format | `--builddir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	For use with `--srcdir` and out-of-source builds. Set this to the location of the directory where the built files reside.
- ``--datadir=*`dir_name`*``
	| Command-Line Format | `--datadir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The path to the MySQL data directory. Only the last component of the path name is created if it does not exist; the parent directory must already exist or an error occurs.
	Note
	The `--datadir` option is mandatory and the data directory must not already exist.
- `--defaults`
	| Command-Line Format | `--defaults` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	This option causes **mysql\_install\_db** to invoke [**mysqld**](mysqld.md) in such a way that it reads option files from the default locations. If given as `--no-defaults`, and `--defaults-file` or `--defaults-extra-file` is not also specified, **mysql\_install\_db** passes `--no-defaults` to [**mysqld**](mysqld.md), to prevent option files from being read. This may help if program startup fails due to reading unknown options from an option file.
- ``--defaults-extra-file=*`file_name`*``
	| Command-Line Format | `--defaults-extra-file=file_name` |
	| --- | --- |
	| Type | File name |
	Read this option file after the global option file but (on Unix) before the user option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	This option is passed by **mysql\_install\_db** to [**mysqld**](mysqld.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--defaults-file=*`file_name`*``
	| Command-Line Format | `--defaults-file=file_name` |
	| --- | --- |
	| Type | File name |
	Use only the given option file. If the file does not exist or is otherwise inaccessible, an error occurs. If *`file_name`* is not an absolute path name, it is interpreted relative to the current directory.
	This option is passed by **mysql\_install\_db** to [**mysqld**](mysqld.md).
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--extra-sql-file=*`file_name`*``, ``-f *`file_name`*``
	| Command-Line Format | `--extra-sql-file=file_name` |
	| --- | --- |
	| Type | File name |
	This option names a file containing additional SQL statements to be executed after the standard bootstrapping statements. Accepted statement syntax in the file is like that of the [**mysql**](mysql.md) command-line client, including support for multiple-line C-style comments and delimiter handling to enable definition of stored programs.
- `--insecure`
	| Command-Line Format | `--insecure` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	Do not generate a random password for the adminstrative account.
	If `--insecure` is *not* given, it is necessary after **mysql\_install\_db** has been run to start the server, connect using the administrative account with the password written to the `.mysql_secret` file, and specify a new administrative password. Until this is done, the administrative account cannot be used for anything else. To change the password, you can use the [`SET PASSWORD`](set-password.md) statement (for example, with the [**mysql**](mysql.md) or [**mysqladmin**](mysqladmin.md) client). After resetting the password, remove the `.mysql_secret` file; otherwise, if you run [**mysql\_secure\_installation**](mysql-secure-installation.md), that command may see the file and expire the `root` password again as part of ensuring secure deployment.
- `--lc-messages=name`
	| Command-Line Format | `--lc-messages=name` |
	| --- | --- |
	| Type | String |
	| Default Value | `en_US` |
	The locale to use for error messages. The default is `en_US`. The argument is converted to a language name and combined with the value of `--lc-messages-dir` to produce the location for the error message file. See [Section 10.12, “Setting the Error Message Language”](error-message-language.md).
- ``--lc-messages-dir=*`dir_name`*``
	| Command-Line Format | `--lc-messages-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The directory where error messages are located. The value is used together with the value of `--lc-messages` to produce the location for the error message file. See [Section 10.12, “Setting the Error Message Language”](error-message-language.md).
- ``--login-file=*`file_name`*``
	| Command-Line Format | `--login-file=file_name` |
	| --- | --- |
	| Type | File name |
	The file from which to read the login path if the ``--login-path=*`file_name`*`` option is specified. The default file is `.mylogin.cnf`.
- ``--login-path=*`name`*``
	| Command-Line Format | `--login-path=name` |
	| --- | --- |
	| Type | String |
	Read options from the named login path in the `.mylogin.cnf` login path file. The default login path is `client`. (To read a different file, use the ``--login-file=*`name`*`` option.) A “login path” is an option group containing options that specify which MySQL server to connect to and which account to authenticate as. To create or modify a login path file, use the [**mysql\_config\_editor**](mysql-config-editor.md) utility. See [Section 4.6.6, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).
	If the `--login-path` option is specified, the user, host, and password values are taken from the login path and used to create the administrative account. The password must be defined in the login path or an error occurs, unless the `--insecure` option is also specified. In addition, with `--login-path`, any `--admin-host` and `--admin-user` options are ignored.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--mysqld-file=*`file_name`*``
	| Command-Line Format | `--mysqld-file=file_name` |
	| --- | --- |
	| Type | File name |
	The path name of the [**mysqld**](mysqld.md) binary to execute. The option value must be an absolute path name or an error occurs.
	If this option is not given, **mysql\_install\_db** searches for [**mysqld**](mysqld.md) in these locations:
	- In the `bin` directory under the `--basedir` option value, if that option was given.
	- In the `bin` directory under the `--srcdir` option value, if that option was given.
	- In the `bin` directory under the `--builddir` option value, if that option was given.
	- In the local directory and in the `bin` and `sbin` directories under the local directory.
	- In `/usr/bin`, `/usr/sbin`, `/usr/local/bin`, `/usr/local/sbin`, `/opt/local/bin`, `/opt/local/sbin`.
- `--no-defaults`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	For behavior of this option, see the description of `--defaults`.
	For additional information about this and other option-file options, see [Section 4.2.2.3, “Command-Line Options that Affect Option-File Handling”](option-file-options.md).
- ``--random-password-file=*`file_name`*``
	| Command-Line Format | `--random-password-file=file_name` |
	| --- | --- |
	| Type | File name |
	The path name of the file in which to write the randomly generated password for the administrative account. The option value must be an absolute path name or an error occurs. The default is `$HOME/.mysql_secret`.
- `--skip-sys-schema`
	| Command-Line Format | `--skip-sys-schema` |
	| --- | --- |
	| Type | Boolean |
	| Default Value | `FALSE` |
	**mysql\_install\_db** installs the `sys` schema. The `--skip-sys-schema` option suppresses this behavior.
- ``--srcdir=*`dir_name`*``
	| Command-Line Format | `--srcdir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	For internal use. This option specifies the directory under which **mysql\_install\_db** looks for support files such as the error message file and the file for populating the help tables.
- ``--user=*`user_name`*``, ``-u *`user_name`*``
	| Command-Line Format | `--user=user_name` |
	| --- | --- |
	The system (login) user name to use for running [**mysqld**](mysqld.md). Files and directories created by [**mysqld**](mysqld.md) are owned by this user. You must be the system `root` user to use this option. By default, [**mysqld**](mysqld.md) runs using your current login name; files and directories that it creates are owned by you.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Print more information about what the program does. You can use this option to see the [**mysqld**](mysqld.md) command that **mysql\_install\_db** invokes to start the server in bootstrap mode.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.