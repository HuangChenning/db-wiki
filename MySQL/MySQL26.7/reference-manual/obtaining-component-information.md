---
title: "MySQL :: MySQL 26.7 Reference Manual :: 7.5.2 Obtaining Component Information"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/obtaining-component-information.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 7.5.2 Obtaining Component Information

The `mysql.component` system table contains information about currently loaded components and shows which components have been registered using [`INSTALL       COMPONENT`](install-component.md). Selecting from the table shows which components are installed. For example:

```sql
mysql> SELECT * FROM mysql.component;
+--------------+--------------------+------------------------------------+
| component_id | component_group_id | component_urn                      |
+--------------+--------------------+------------------------------------+
|            1 |                  1 | file://component_validate_password |
|            2 |                  2 | file://component_log_sink_json     |
+--------------+--------------------+------------------------------------+
```

The `component_id` and `component_group_id` values are for internal use. The `component_urn` is the URN used in [`INSTALL COMPONENT`](install-component.md) and [`UNINSTALL COMPONENT`](uninstall-component.md) statements to load and unload the component.