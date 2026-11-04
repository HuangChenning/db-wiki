---
title: "4.4.3 mysql_plugin — Configure MySQL Server Plugins"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-plugin.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 4.4.3 mysql\_plugin — Configure MySQL Server Plugins

Note

**mysql\_plugin** is deprecated as of MySQL 5.7.11 and removed in MySQL 8.0. Alternatives include loading plugins at server startup using the [`--plugin-load`](server-options.md) or [`--plugin-load-add`](server-options.md) option, or at runtime using the [`INSTALL           PLUGIN`](install-plugin.md) statement.

The **mysql\_plugin** utility enables MySQL administrators to manage which plugins a MySQL server loads. It provides an alternative to manually specifying the [`--plugin-load`](server-options.md) option at server startup or using the [`INSTALL         PLUGIN`](install-plugin.md) and [`UNINSTALL         PLUGIN`](uninstall-plugin.md) statements at runtime.

Depending on whether **mysql\_plugin** is invoked to enable or disable plugins, it inserts or deletes rows in the `mysql.plugin` table that serves as a plugin registry. (To perform this operation, **mysql\_plugin** invokes the MySQL server in bootstrap mode. This means that the server must not already be running.) For normal server startups, the server loads and enables plugins listed in `mysql.plugin` automatically. For additional control over plugin activation, use ``--*`plugin_name`*`` options named for specific plugins, as described in [Section 5.5.1, “Installing and Uninstalling Plugins”](plugin-loading.md).

Each invocation of **mysql\_plugin** reads a configuration file to determine how to configure the plugins contained in a single plugin library file. To invoke **mysql\_plugin**, use this syntax:

```
mysql_plugin [options] plugin {ENABLE|DISABLE}
```

*`plugin`* is the name of the plugin to configure. `ENABLE` or `DISABLE` (not case-sensitive) specify whether to enable or disable components of the plugin library named in the configuration file. The order of the *`plugin`* and `ENABLE` or `DISABLE` arguments does not matter.

For example, to configure components of a plugin library file named `myplugins.so` on Linux or `myplugins.dll` on Windows, specify a *`plugin`* value of `myplugins`. Suppose that this plugin library contains three plugins, `plugin1`, `plugin2`, and `plugin3`, all of which should be configured under **mysql\_plugin** control. By convention, configuration files have a suffix of `.ini` and the same base name as the plugin library, so the default configuration file name for this plugin library is `myplugins.ini`. The configuration file contents look like this:

```
myplugins
plugin1
plugin2
plugin3
```

The first line in the `myplugins.ini` file is the name of the library file, without any extension such as `.so` or `.dll`. The remaining lines are the names of the components to be enabled or disabled. Each value in the file should be on a separate line. Lines on which the first character is `'#'` are taken as comments and ignored.

To enable the plugins listed in the configuration file, invoke **mysql\_plugin** this way:

```
mysql_plugin myplugins ENABLE
```

To disable the plugins, use `DISABLE` rather than `ENABLE`.

An error occurs if **mysql\_plugin** cannot find the configuration file or plugin library file, or if **mysql\_plugin** cannot start the MySQL server.

**mysql\_plugin** supports the following options, which can be specified on the command line or in the `[mysqld]` group of any option file. For options specified in a `[mysqld]` group, **mysql\_plugin** recognizes the `--basedir`, `--datadir`, and `--plugin-dir` options and ignores others. For information about option files used by MySQL programs, see [Section 4.2.2.2, “Using Option Files”](option-files.md).

**Table 4.9 mysql\_plugin Options**

| Option Name | Description |
| --- | --- |
| \--basedir | The server base directory |
| \--datadir | The server data directory |
| \--help | Display help message and exit |
| \--my-print-defaults | Path to my\_print\_defaults |
| \--mysqld | Path to server |
| \--no-defaults | Do not read configuration file |
| \--plugin-dir | Directory where plugins are installed |
| \--plugin-ini | The plugin configuration file |
| \--print-defaults | Show configuration file defaults |
| \--verbose | Verbose mode |
| \--version | Display version information and exit |

- `--help`, `-?`
	| Command-Line Format | `--help` |
	| --- | --- |
	Display a help message and exit.
- ``--basedir=*`dir_name`*``, ``-b *`dir_name`*``
	| Command-Line Format | `--basedir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The server base directory.
- ``--datadir=*`dir_name`*``, ``-d *`dir_name`*``
	| Command-Line Format | `--datadir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The server data directory.
- ``--my-print-defaults=*`file_name`*``, ``-b *`file_name`*``
	| Command-Line Format | `--my-print-defaults=file_name` |
	| --- | --- |
	| Type | File name |
	The path to the [**my\_print\_defaults**](my-print-defaults.md) program.
- ``--mysqld=*`file_name`*``, ``-b *`file_name`*``
	| Command-Line Format | `--mysqld=file_name` |
	| --- | --- |
	| Type | File name |
	The path to the [**mysqld**](mysqld.md) server.
- `--no-defaults`, `-p`
	| Command-Line Format | `--no-defaults` |
	| --- | --- |
	Do not read values from the configuration file. This option enables an administrator to skip reading defaults from the configuration file.
	With **mysql\_plugin**, this option need not be given first on the command line, unlike most other MySQL programs that support `--no-defaults`.
- ``--plugin-dir=*`dir_name`*``, ``-p *`dir_name`*``
	| Command-Line Format | `--plugin-dir=dir_name` |
	| --- | --- |
	| Type | Directory name |
	The server plugin directory.
- ``--plugin-ini=*`file_name`*``, ``-i *`file_name`*``
	| Command-Line Format | `--plugin-ini=file_name` |
	| --- | --- |
	| Type | File name |
	The **mysql\_plugin** configuration file. Relative path names are interpreted relative to the current directory. If this option is not given, the default is ``*`plugin`*.ini`` in the plugin directory, where *`plugin`* is the *`plugin`* argument on the command line.
- `--print-defaults`, `-P`
	| Command-Line Format | `--print-defaults` |
	| --- | --- |
	Display the default values from the configuration file. This option causes **mysql\_plugin** to print the defaults for `--basedir`, `--datadir`, and `--plugin-dir` if they are found in the configuration file. If no value for a variable is found, nothing is shown.
	With **mysql\_plugin**, this option need not be given first on the command line, unlike most other MySQL programs that support `--print-defaults`.
- `--verbose`, `-v`
	| Command-Line Format | `--verbose` |
	| --- | --- |
	Verbose mode. Print more information about what the program does. This option can be used multiple times to increase the amount of information.
- `--version`, `-V`
	| Command-Line Format | `--version` |
	| --- | --- |
	Display version information and exit.