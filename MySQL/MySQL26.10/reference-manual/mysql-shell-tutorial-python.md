---
title: "MySQL :: MySQL 26.10 Reference Manual :: 22.4 Python Quick-Start Guide: MySQL Shell for Document Store"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/mysql-shell-tutorial-python.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.10 Reference Manual

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb

version 26.10

[26.7](https://dev.mysql.com/doc/refman/26.7/en/mysql-shell-tutorial-python.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/mysql-shell-tutorial-python.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/mysql-shell-tutorial-python.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-shell-tutorial-python.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/mysql-shell-tutorial-python.html)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / [Using MySQL as a Document Store](document-store.md) / Python Quick-Start Guide: MySQL Shell for Document Store

## 22.4 Python Quick-Start Guide: MySQL Shell for Document Store

This quick-start guide provides instructions to begin prototyping document store applications interactively with MySQL Shell. The guide includes the following topics:

- Introduction to MySQL functionality, MySQL Shell, and the `world_x` example schema.
- Operations to manage collections and documents.
- Operations to manage relational tables.
- Operations that apply to documents within tables.

To follow this quick-start guide you need a MySQL server with X Plugin installed, the default in 26.10, and MySQL Shell to use as the client. MySQL Shell includes X DevAPI, implemented in both JavaScript and Python, which enables you to connect to the MySQL server instance using X Protocol and use the server as a Document Store.

### Related Information

- [MySQL Shell 26.10](https://dev.mysql.com/doc/mysql-shell/26.10/en/) provides more in-depth information about MySQL Shell.
- See [Installing MySQL Shell](https://dev.mysql.com/doc/mysql-shell/26.10/en/mysql-shell-install.html) and [Section 22.5, “X Plugin”](x-plugin.md) for more information about the tools used in this quick-start guide.
- See [Supported Languages](https://dev.mysql.com/doc/mysql-shell/26.10/en/mysql-shell-features.html#shell-supported-languages) for more information about the languages MySQL Shell supports.
- [X DevAPI User Guide](https://dev.mysql.com/doc/x-devapi-userguide/en/) provides more examples of using X DevAPI to develop applications which use MySQL as a Document Store.
- A [JavaScript](mysql-shell-tutorial-javascript.md) quick-start guide is also available.

[PREV](mysql-shell-tutorial-javascript-documents-in-tables.md) [HOME](index.md) [UP](document-store.md) [NEXT](mysql-shell-tutorial-python-shell.md)

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb