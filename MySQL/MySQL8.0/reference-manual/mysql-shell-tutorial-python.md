---
title: "22.4 Python Quick-Start Guide: MySQL Shell for Document Store"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/mysql-shell-tutorial-python.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

Skip to Main Content

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

This quick-start guide provides instructions to begin prototyping document store applications interactively with MySQL Shell. The guide includes the following topics:

- Introduction to MySQL functionality, MySQL Shell, and the `world_x` example schema.
- Operations to manage collections and documents.
- Operations to manage relational tables.
- Operations that apply to documents within tables.

To follow this quick-start guide you need a MySQL server with X Plugin installed, the default in 8.0, and MySQL Shell to use as the client. MySQL Shell includes X DevAPI, implemented in both JavaScript and Python, which enables you to connect to the MySQL server instance using X Protocol and use the server as a Document Store.

### Related Information

- [MySQL Shell 8.0](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/) provides more in-depth information about MySQL Shell.
- See [Installing MySQL Shell](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-install.html) and [Section 22.5, “X Plugin”](x-plugin.md) for more information about the tools used in this quick-start guide.
- See [Supported Languages](https://docs.oracle.com/cd/E17952_01/mysql-shell-8.0-en/mysql-shell-features.html#shell-supported-languages) for more information about the languages MySQL Shell supports.
- [X DevAPI User Guide](https://docs.oracle.com/cd/E17952_01/x-devapi-userguide-en/) provides more examples of using X DevAPI to develop applications which use MySQL as a Document Store.
- A [JavaScript](mysql-shell-tutorial-javascript.md) quick-start guide is also available.

[MySQL Documentation Library](https://docs.oracle.com/cd/E17952_01/index.html "Go to MySQL Doc Library")