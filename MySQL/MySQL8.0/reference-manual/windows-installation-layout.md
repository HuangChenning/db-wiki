---
title: "2.3.1 MySQL Installation Layout on Microsoft Windows"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/windows-installation-layout.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 2.3.1 MySQL Installation Layout on Microsoft Windows

For MySQL 8.0 on Windows, the default installation directory is `C:\Program Files\MySQL\MySQL Server       8.0` for installations performed with MySQL Installer. If you use the ZIP archive method to install MySQL, you may prefer to install in `C:\mysql`. However, the layout of the subdirectories remains the same.

All of the files are located within this parent directory, using the structure shown in the following table.

**Table 2.4 Default MySQL Installation Layout for Microsoft Windows**

| Directory | Contents of Directory | Notes |
| --- | --- | --- |
| `bin` | [**mysqld**](mysqld.md) server, client and utility programs |  |
| `%PROGRAMDATA%\MySQL\MySQL Server 8.0\` | Log files, databases | The Windows system variable `%PROGRAMDATA%` defaults to `C:\ProgramData`. |
| `docs` | Release documentation | With MySQL Installer, use the `Modify` operation to select this optional folder. |
| `include` | Include (header) files |  |
| `lib` | Libraries |  |
| `share` | Miscellaneous support files, including error messages, character set files, sample configuration files, SQL for database installation |  |

#### Silent Installation Methods

Use MySQL Installer, see [Section 2.3.3.5, “MySQL Installer Console Reference”](MySQLInstallerConsole.md).