---
title: "MySQL :: MySQL 26.7 Reference Manual :: 6.9 Environment Variables"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/environment-variables.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 6.9 Environment Variables

This section lists environment variables that are used directly or indirectly by MySQL. Most of these can also be found in other places in this manual.

Options on the command line take precedence over values specified in option files and environment variables, and values in option files take precedence over values in environment variables. In many cases, it is preferable to use an option file instead of environment variables to modify the behavior of MySQL. See [Section 6.2.2.2, “Using Option Files”](option-files.md).

| Variable | Description |
| --- | --- |
| `AUTHENTICATION_KERBEROS_CLIENT_LOG` | Kerberos authentication logging level. |
| `AUTHENTICATION_LDAP_CLIENT_LOG` | Client-side LDAP authentication logging level. |
| `AUTHENTICATION_PAM_LOG` | [PAM](pam-pluggable-authentication.md) authentication plugin debug logging settings. |
| `CC` | The name of your C compiler (for running **CMake**). |
| `CXX` | The name of your C++ compiler (for running **CMake**). |
| `CC` | The name of your C compiler (for running **CMake**). |
| `DBI_USER` | The default user name for Perl DBI. |
| `DBI_TRACE` | Trace options for Perl DBI. |
| `HOME` | The default path for the [**mysql**](mysql.md) history file is `$HOME/.mysql_history`. |
| `LD_RUN_PATH` | Used to specify the location of `libmysqlclient.so`. |
| `LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN` | Enable `mysql_clear_password` authentication plugin; see [Section 8.4.1.3, “Client-Side Cleartext Pluggable Authentication”](cleartext-pluggable-authentication.md). |
| `LIBMYSQL_PLUGIN_DIR` | Directory in which to look for client plugins. |
| `LIBMYSQL_PLUGINS` | Client plugins to preload. |
| `MYSQL_DEBUG` | Debug trace options when debugging. |
| `MYSQL_GROUP_SUFFIX` | Option group suffix value (like specifying [`--defaults-group-suffix`](option-file-options.md)). |
| `MYSQL_HISTFILE` | The path to the [**mysql**](mysql.md) history file. If this variable is set, its value overrides the default for `$HOME/.mysql_history`. |
| `MYSQL_HISTIGNORE` | Patterns specifying statements that [**mysql**](mysql.md) should not log to `$HOME/.mysql_history`, or `syslog` if [`--syslog`](mysql-command-options.md) is given. |
| `MYSQL_HOME` | The path to the directory in which the server-specific `my.cnf` file resides. |
| `MYSQL_HOST` | The default host name used by the [**mysql**](mysql.md) command-line client. |
| `MYSQL_PS1` | The command prompt to use in the [**mysql**](mysql.md) command-line client. |
| `MYSQL_PWD` | The default password when connecting to [**mysqld**](mysqld.md). Using this is insecure. See note following table. |
| `MYSQL_TCP_PORT` | The default TCP/IP port number. |
| `MYSQL_TEST_LOGIN_FILE` | The name of the `.mylogin.cnf` login path file. |
| `MYSQL_TEST_TRACE_CRASH` | Whether the test protocol trace plugin crashes clients. See note following table. |
| `MYSQL_TEST_TRACE_DEBUG` | Whether the test protocol trace plugin produces output. See note following table. |
| `MYSQL_UNIX_PORT` | The default Unix socket file name; used for connections to `localhost`. |
| `MYSQLX_TCP_PORT` | The X Plugin default TCP/IP port number. |
| `MYSQLX_UNIX_PORT` | The X Plugin default Unix socket file name; used for connections to `localhost`. |
| `NOTIFY_SOCKET` | Socket used by [**mysqld**](mysqld.md) to communicate with systemd. |
| `PATH` | Used by the shell to find MySQL programs. |
| `PKG_CONFIG_PATH` | Location of `mysqlclient.pc` **pkg-config** file. See note following table. |
| `TMPDIR` | The directory in which temporary files are created. |
| `TZ` | This should be set to your local time zone. See [Section B.3.3.7, “Time Zone Problems”](timezone-problems.md). |
| `UMASK` | The user-file creation mode when creating files. See note following table. |
| `UMASK_DIR` | The user-directory creation mode when creating directories. See note following table. |
| `USER` | The default user name on Windows when connecting to [**mysqld**](mysqld.md). |

For information about the [**mysql**](mysql.md) history file, see [Section 6.5.1.3, “mysql Client Logging”](mysql-logging.md).

Use of `MYSQL_PWD` to specify a MySQL password must be considered *extremely insecure* and should not be used. Some versions of **ps** include an option to display the environment of running processes. On some systems, if you set `MYSQL_PWD`, your password is exposed to any other user who runs **ps**. Even on systems without such a version of **ps**, it is unwise to assume that there are no other methods by which users can examine process environments.

`MYSQL_PWD` is deprecated as of MySQL 26.7; expect it to be removed in a future version of MySQL.

`MYSQL_TEST_LOGIN_FILE` is the path name of the login path file (the file created by [**mysql\_config\_editor**](mysql-config-editor.md)). If not set, the default value is `%APPDATA%\MySQL\.mylogin.cnf` directory on Windows and `$HOME/.mylogin.cnf` on non-Windows systems. See [Section 6.6.7, “mysql\_config\_editor — MySQL Configuration Utility”](mysql-config-editor.md).

The `MYSQL_TEST_TRACE_DEBUG` and `MYSQL_TEST_TRACE_CRASH` variables control the test protocol trace client plugin, if MySQL is built with that plugin enabled. For more information, see [Using the Test Protocol Trace Plugin](https://dev.mysql.com/doc/extending-mysql/26.7/en/test-protocol-trace-plugin.html).

The default `UMASK` and `UMASK_DIR` values are `0640` and `0750`, respectively. MySQL assumes that the value for `UMASK` or `UMASK_DIR` is in octal if it starts with a zero. For example, setting `UMASK=0600` is equivalent to `UMASK=384` because 0600 octal is 384 decimal.

The `UMASK` and `UMASK_DIR` variables, despite their names, are used as modes, not masks:

- If `UMASK` is set, [**mysqld**](mysqld.md) uses `($UMASK | 0600)` as the mode for file creation, so that newly created files have a mode in the range from 0600 to 0666 (all values octal).
- If `UMASK_DIR` is set, [**mysqld**](mysqld.md) uses `($UMASK_DIR |         0700)` as the base mode for directory creation, which then is AND-ed with `~(~$UMASK & 0666)`, so that newly created directories have a mode in the range from 0700 to 0777 (all values octal). The AND operation may remove read and write permissions from the directory mode, but not execute permissions.

See also [Section B.3.3.1, “Problems with File Permissions”](file-permissions.md).

It may be necessary to set `PKG_CONFIG_PATH` if you use **pkg-config** for building MySQL programs. See [Building C API Client Programs Using pkg-config](https://dev.mysql.com/doc/c-api/26.7/en/c-api-building-clients-pkg-config.html).