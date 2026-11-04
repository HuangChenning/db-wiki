---
title: "2.10.8 Upgrading MySQL on Windows"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/windows-upgrading.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 2.10.8 Upgrading MySQL on Windows

There are two approaches for upgrading MySQL on Windows:

The approach you select depends on how the existing installation was performed. Before proceeding, review [Section 2.10, “Upgrading MySQL”](upgrading.md) for additional information on upgrading MySQL that is not specific to Windows.

Note

Whichever approach you choose, always back up your current MySQL installation before performing an upgrade. See [Section 7.2, “Database Backup Methods”](backup-methods.md).

Upgrades between milestone releases (or from a milestone release to a GA release) are not supported. Significant development changes take place in milestone releases and you may encounter compatibility issues or problems starting the server. For instructions on how to perform a logical upgrade with a milestone release, see [Logical Upgrade](upgrade-binary-package.md).

Note

MySQL Installer does not support upgrades between *Community* releases and *Commercial* releases. If you require this type of upgrade, perform it using the ZIP archive approach.

#### Upgrading MySQL with MySQL Installer

Performing an upgrade with MySQL Installer is the best approach when the current server installation was performed with it and the upgrade is within the current release series. MySQL Installer does not support upgrades between release series, such as from 5.6 to 5.7, and it does not provide an upgrade indicator to prompt you to upgrade. For instructions on upgrading between release series, see Upgrading MySQL Using the Windows ZIP Distribution.

To perform an upgrade using MySQL Installer:

1. Start MySQL Installer.
2. From the dashboard, click Catalog to download the latest changes to the catalog. The installed server can be upgraded only if the dashboard displays an arrow next to the version number of the server.
3. Click Upgrade. All products that have a newer version now appear in a list.
	Note
	MySQL Installer deselects the server upgrade option for milestone releases (Pre-Release) in the same release series. In addition, it displays a warning to indicate that the upgrade is not supported, identifies the risks of continuing, and provides a summary of the steps to perform a logical upgrade manually. You can reselect server upgrade and proceed at your own risk.
4. Deselect all but the MySQL server product, unless you intend to upgrade other products at this time, and click Next.
5. Click Execute to start the download. When the download finishes, click Next to begin the upgrade operation.
6. Configure the server.

#### Upgrading MySQL Using the Windows ZIP Distribution

To perform an upgrade using the Windows ZIP archive distribution:

1. Download the latest Windows ZIP Archive distribution of MySQL from [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/).
2. If the server is running, stop it. If the server is installed as a service, stop the service with the following command from the command prompt:
	```
	C:\> SC STOP mysqld_service_name
	```
	Alternatively, use **NET STOP *`mysqld_service_name`***.
	If you are not running the MySQL server as a service, use [**mysqladmin**](mysqladmin.md) to stop it. For example, before upgrading from MySQL 5.6 to 5.7, use [**mysqladmin**](mysqladmin.md) from MySQL 5.6 as follows:
	```
	C:\> "C:\Program Files\MySQL\MySQL Server 5.6\bin\mysqladmin" -u root shutdown
	```
	Note
	If the MySQL `root` user account has a password, invoke [**mysqladmin**](mysqladmin.md) with the `-p` option and enter the password when prompted.
3. Extract the ZIP archive. You may either overwrite your existing MySQL installation (usually located at `C:\mysql`), or install it into a different directory, such as `C:\mysql5`. Overwriting the existing installation is recommended.
4. Restart the server. For example, use the **SC START *`mysqld_service_name`*** or **NET START *`mysqld_service_name`*** command if you run MySQL as a service, or invoke [**mysqld**](mysqld.md) directly otherwise.
5. As Administrator, run [**mysql\_upgrade**](mysql-upgrade.md) to check your tables, attempt to repair them if necessary, and update your grant tables if they have changed so that you can take advantage of any new capabilities. See [Section 4.4.7, “mysql\_upgrade — Check and Upgrade MySQL Tables”](mysql-upgrade.md).
6. If you encounter errors, see [Section 2.3.5, “Troubleshooting a Microsoft Windows MySQL Server Installation”](windows-troubleshooting.md).