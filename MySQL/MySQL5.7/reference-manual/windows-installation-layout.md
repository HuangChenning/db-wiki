---
title: "2.3.1 MySQL Installation Layout on Microsoft Windows"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/windows-installation-layout.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 2.3.1 MySQL Installation Layout on Microsoft Windows

For MySQL 5.7 on Windows, the default installation directory is `C:\Program Files\MySQL\MySQL Server       5.7` for installations performed with MySQL Installer. If you use the ZIP archive method to install MySQL, you may prefer to install in `C:\mysql`. However, the layout of the subdirectories remains the same.

All of the files are located within this parent directory, using the structure shown in the following table.

**Table 2.4 Default MySQL Installation Layout for Microsoft Windows**

| Directory | Contents of Directory | Notes |
| --- | --- | --- |
| `bin` | [**mysqld**](mysqld.md) server, client and utility programs |  |
| `%PROGRAMDATA%\MySQL\MySQL Server 5.7\` | Log files, databases | The Windows system variable `%PROGRAMDATA%` defaults to `C:\ProgramData`. |
| `docs` | Release documentation | With MySQL Installer, use the `Modify` operation to select this optional folder. |
| `include` | Include (header) files |  |
| `lib` | Libraries |  |
| `share` | Miscellaneous support files, including error messages, character set files, sample configuration files, SQL for database installation |  |