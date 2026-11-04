---
title: "2.9.5 Starting and Stopping MySQL Automatically"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/automatic-start.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 2.9.5 Starting and Stopping MySQL Automatically

This section discusses methods for starting and stopping the MySQL server.

Generally, you start the [**mysqld**](mysqld.md) server in one of these ways:

- Invoke [**mysqld**](mysqld.md) directly. This works on any platform.
- On Windows, you can set up a MySQL service that runs automatically when Windows starts. See [Section 2.3.3.8, “Starting MySQL as a Windows Service”](windows-start-service.md).
- On Unix and Unix-like systems, you can invoke [**mysqld\_safe**](mysqld-safe.md), which tries to determine the proper options for [**mysqld**](mysqld.md) and then runs it with those options. See [Section 6.3.2, “mysqld\_safe — MySQL Server Startup Script”](mysqld-safe.md).
- On Linux systems that support systemd, you can use it to control the server. See [Section 2.5.9, “Managing MySQL Server with systemd”](using-systemd.md).
- On systems that use System V-style run directories (that is, `/etc/init.d` and run-level specific directories), invoke [**mysql.server**](mysql-server.md). This script is used primarily at system startup and shutdown. It usually is installed under the name `mysql`. The [**mysql.server**](mysql-server.md) script starts the server by invoking [**mysqld\_safe**](mysqld-safe.md). See [Section 6.3.3, “mysql.server — MySQL Server Startup Script”](mysql-server.md).
- On macOS, install a launchd daemon to enable automatic MySQL startup at system startup. The daemon starts the server by invoking [**mysqld\_safe**](mysqld-safe.md). For details, see [Section 2.4.3, “Installing and Using the MySQL Launch Daemon”](macos-installation-launchd.md). A MySQL Preference Pane also provides control for starting and stopping MySQL through the System Preferences. See [Section 2.4.4, “Installing and Using the MySQL Preference Pane”](macos-installation-prefpane.md).
- On Solaris, use the service management framework (SMF) system to initiate and control MySQL startup.

systemd, the [**mysqld\_safe**](mysqld-safe.md) and [**mysql.server**](mysql-server.md) scripts, Solaris SMF, and the macOS Startup Item (or MySQL Preference Pane) can be used to start the server manually, or automatically at system startup time. systemd, [**mysql.server**](mysql-server.md), and the Startup Item also can be used to stop the server.

The following table shows which option groups the server and startup scripts read from option files.

**Table 2.16 MySQL Startup Scripts and Supported Server Option Groups**

| Script | Option Groups |
| --- | --- |
| [**mysqld**](mysqld.md) | `[mysqld]`, `[server]`, ``[mysqld-*`major_version`*]`` |
| [**mysqld\_safe**](mysqld-safe.md) | `[mysqld]`, `[server]`, `[mysqld_safe]` |
| [**mysql.server**](mysql-server.md) | `[mysqld]`, `[mysql.server]`, `[server]` |

``[mysqld-*`major_version`*]`` means that groups with names like `[mysqld-9.6]` and `[mysqld-9.7]` are read by servers having versions 9.6.x, 9.7.x, and so forth. This feature can be used to specify options that can be read only by servers within a given release series.

For backward compatibility, [**mysql.server**](mysql-server.md) also reads the `[mysql_server]` group and [**mysqld\_safe**](mysqld-safe.md) also reads the `[safe_mysqld]` group. To be current, you should update your option files to use the `[mysql.server]` and `[mysqld_safe]` groups instead.

For more information on MySQL configuration files and their structure and contents, see [Section 6.2.2.2, “Using Option Files”](option-files.md).