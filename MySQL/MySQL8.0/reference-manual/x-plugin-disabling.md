---
title: "22.5.2 Disabling X Plugin"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/x-plugin-disabling.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 22.5.2 Disabling X Plugin

The X Plugin can be disabled at startup by either setting [`mysqlx=0`](x-plugin-options-system-variables.md) in your MySQL configuration file, or by passing in either [`--mysqlx=0`](x-plugin-options-system-variables.md) or [`--skip-mysqlx`](x-plugin-options-system-variables.md) when starting the MySQL server.

Alternatively, use the [`-DWITH_MYSQLX=OFF`](source-configuration-options.md) CMake option to compile MySQL Server without X Plugin.