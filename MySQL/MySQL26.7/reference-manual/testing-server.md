---
title: "MySQL :: MySQL 26.7 Reference Manual :: 2.9.3 Testing the Server"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/testing-server.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 2.9.3 Testing the Server

After the data directory is initialized and you have started the server, perform some simple tests to make sure that it works satisfactorily. This section assumes that your current location is the MySQL installation directory and that it has a `bin` subdirectory containing the MySQL programs used here. If that is not true, adjust the command path names accordingly.

Alternatively, add the `bin` directory to your `PATH` environment variable setting. That enables your shell (command interpreter) to find MySQL programs properly, so that you can run a program by typing only its name, not its path name. See [Section 6.2.9, “Setting Environment Variables”](setting-environment-variables.md).

Use [**mysqladmin**](mysqladmin.md) to verify that the server is running. The following commands provide simple tests to check whether the server is up and responding to connections:

```svg
$> bin/mysqladmin version
$> bin/mysqladmin variables
```

If you cannot connect to the server, specify a `-u       root` option to connect as `root`. If you have assigned a password for the `root` account already, you'll also need to specify `-p` on the command line and enter the password when prompted. For example:

```svg
$> bin/mysqladmin -u root -p version
Enter password: (enter root password here)
```

The output from [**mysqladmin version**](mysqladmin.md) varies slightly depending on your platform and version of MySQL, but should be similar to that shown here:

```svg
$> bin/mysqladmin version
mysqladmin  Ver 14.12 Distrib 26.7.0, for pc-linux-gnu on i686
...

Server version          26.7.0
Protocol version        10
Connection              Localhost via UNIX socket
UNIX socket             /var/lib/mysql/mysql.sock
Uptime:                 14 days 5 hours 5 min 21 sec

Threads: 1  Questions: 366  Slow queries: 0
Opens: 0  Flush tables: 1  Open tables: 19
Queries per second avg: 0.000
```

To see what else you can do with [**mysqladmin**](mysqladmin.md), invoke it with the [`--help`](mysqladmin.md) option.

Verify that you can shut down the server (include a `-p` option if the `root` account has a password already):

```svg
$> bin/mysqladmin -u root shutdown
```

Verify that you can start the server again. Do this by using [**mysqld\_safe**](mysqld-safe.md) or by invoking [**mysqld**](mysqld.md) directly. For example:

```svg
$> bin/mysqld_safe --user=mysql &
```

If [**mysqld\_safe**](mysqld-safe.md) fails, see [Section 2.9.2.1, “Troubleshooting Problems Starting the MySQL Server”](starting-server-troubleshooting.md).

Run some simple tests to verify that you can retrieve information from the server. The output should be similar to that shown here.

Use [**mysqlshow**](mysqlshow.md) to see what databases exist:

```svg
$> bin/mysqlshow
+--------------------+
|     Databases      |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

The list of installed databases may vary, but always includes at least `mysql` and `information_schema`.

If you specify a database name, [**mysqlshow**](mysqlshow.md) displays a list of the tables within the database:

```svg
$> bin/mysqlshow mysql
Database: mysql
+---------------------------+
|          Tables           |
+---------------------------+
| columns_priv              |
| component                 |
| db                        |
| default_roles             |
| engine_cost               |
| func                      |
| general_log               |
| global_grants             |
| gtid_executed             |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| ndb_binlog_index          |
| password_history          |
| plugin                    |
| procs_priv                |
| proxies_priv              |
| role_edges                |
| server_cost               |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
```

Use the [**mysql**](mysql.md) program to select information from a table in the `mysql` schema:

```svg
$> bin/mysql -e "SELECT User, Host, plugin FROM mysql.user" mysql
+------+-----------+-----------------------+
| User | Host      | plugin                |
+------+-----------+-----------------------+
| root | localhost | caching_sha2_password |
+------+-----------+-----------------------+
```

At this point, your server is running and you can access it. To tighten security if you have not yet assigned a password to the initial account, follow the instructions in [Section 2.9.4, “Securing the Initial MySQL Account”](default-privileges.md).

For more information about [**mysql**](mysql.md), [**mysqladmin**](mysqladmin.md), and [**mysqlshow**](mysqlshow.md), see [Section 6.5.1, “mysql — The MySQL Command-Line Client”](mysql.md), [Section 6.5.2, “mysqladmin — A MySQL Server Administration Program”](mysqladmin.md), and [Section 6.5.6, “mysqlshow — Display Database, Table, and Column Information”](mysqlshow.md).