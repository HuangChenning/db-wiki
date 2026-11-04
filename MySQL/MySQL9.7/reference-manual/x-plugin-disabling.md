---
title: "22.5.2 Disabling X Plugin"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/x-plugin-disabling.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 22.5.2 Disabling X Plugin

The X Plugin can be disabled at startup by either setting [`mysqlx=0`](x-plugin-options-system-variables.md) in your MySQL configuration file, or by passing in either [`--mysqlx=0`](x-plugin-options-system-variables.md) or [`--skip-mysqlx`](x-plugin-options-system-variables.md) when starting the MySQL server.

Alternatively, use the [`-DWITH_MYSQLX=OFF`](source-configuration-options.md) CMake option to compile MySQL Server without X Plugin.