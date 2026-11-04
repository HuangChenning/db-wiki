---
title: "MySQL :: MySQL 26.7 Reference Manual :: 29.18 Performance Schema and Plugins"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/performance-schema-and-plugins.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

## 29.18 Performance Schema and Plugins

Removing a plugin with [`UNINSTALL       PLUGIN`](uninstall-plugin.md) does not affect information already collected for code in that plugin. Time spent executing the code while the plugin was loaded was still spent even if the plugin is unloaded later. The associated event information, including aggregate information, remains readable in `performance_schema` database tables. For additional information about the effect of plugin installation and removal, see [Section 29.7, “Performance Schema Status Monitoring”](performance-schema-status-monitoring.md).

A plugin implementor who instruments plugin code should document its instrumentation characteristics to enable those who load the plugin to account for its requirements. For example, a third-party storage engine should include in its documentation how much memory the engine needs for mutex and other instruments.