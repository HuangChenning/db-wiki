---
title: "5.5.2 Obtaining Server Plugin Information"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/obtaining-plugin-information.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.5.2 Obtaining Server Plugin Information

There are several ways to determine which plugins are installed in the server:

- The Information Schema [`PLUGINS`](information-schema-plugins-table.md) table contains a row for each loaded plugin. Any that have a `PLUGIN_LIBRARY` value of `NULL` are built in and cannot be unloaded.
	```
	mysql> SELECT * FROM INFORMATION_SCHEMA.PLUGINS\G
	*************************** 1. row ***************************
	           PLUGIN_NAME: binlog
	        PLUGIN_VERSION: 1.0
	         PLUGIN_STATUS: ACTIVE
	           PLUGIN_TYPE: STORAGE ENGINE
	   PLUGIN_TYPE_VERSION: 50158.0
	        PLUGIN_LIBRARY: NULL
	PLUGIN_LIBRARY_VERSION: NULL
	         PLUGIN_AUTHOR: MySQL AB
	    PLUGIN_DESCRIPTION: This is a pseudo storage engine to represent the binlog in a transaction
	        PLUGIN_LICENSE: GPL
	           LOAD_OPTION: FORCE
	...
	*************************** 10. row ***************************
	           PLUGIN_NAME: InnoDB
	        PLUGIN_VERSION: 1.0
	         PLUGIN_STATUS: ACTIVE
	           PLUGIN_TYPE: STORAGE ENGINE
	   PLUGIN_TYPE_VERSION: 50158.0
	        PLUGIN_LIBRARY: ha_innodb_plugin.so
	PLUGIN_LIBRARY_VERSION: 1.0
	         PLUGIN_AUTHOR: Innobase Oy
	    PLUGIN_DESCRIPTION: Supports transactions, row-level locking,
	                        and foreign keys
	        PLUGIN_LICENSE: GPL
	           LOAD_OPTION: ON
	...
	```
- The [`SHOW PLUGINS`](show-plugins.md) statement displays a row for each loaded plugin. Any that have a `Library` value of `NULL` are built in and cannot be unloaded.
	```
	mysql> SHOW PLUGINS\G
	*************************** 1. row ***************************
	   Name: binlog
	 Status: ACTIVE
	   Type: STORAGE ENGINE
	Library: NULL
	License: GPL
	...
	*************************** 10. row ***************************
	   Name: InnoDB
	 Status: ACTIVE
	   Type: STORAGE ENGINE
	Library: ha_innodb_plugin.so
	License: GPL
	...
	```
- The `mysql.plugin` table shows which plugins have been registered with [`INSTALL           PLUGIN`](install-plugin.md). The table contains only plugin names and library file names, so it does not provide as much information as the [`PLUGINS`](information-schema-plugins-table.md) table or the [`SHOW PLUGINS`](show-plugins.md) statement.