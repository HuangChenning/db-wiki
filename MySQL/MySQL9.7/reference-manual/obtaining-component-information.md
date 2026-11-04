---
title: "7.5.2 Obtaining Component Information"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/obtaining-component-information.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 7.5.2 Obtaining Component Information

The `mysql.component` system table contains information about currently loaded components and shows which components have been registered using [`INSTALL       COMPONENT`](install-component.md). Selecting from the table shows which components are installed. For example:

```
mysql> SELECT * FROM mysql.component;
+--------------+--------------------+------------------------------------+
| component_id | component_group_id | component_urn                      |
+--------------+--------------------+------------------------------------+
|            1 |                  1 | file://component_validate_password |
|            2 |                  2 | file://component_log_sink_json     |
+--------------+--------------------+------------------------------------+
```

The `component_id` and `component_group_id` values are for internal use. The `component_urn` is the URN used in [`INSTALL COMPONENT`](install-component.md) and [`UNINSTALL COMPONENT`](uninstall-component.md) statements to load and unload the component.