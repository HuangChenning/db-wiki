---
title: "7.6.2 Obtaining Server Plugin Information"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/obtaining-plugin-information.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 7.6.2 Obtaining Server Plugin Information

There are several ways to determine which plugins are installed in the server:

- The Information Schema [`PLUGINS`](information-schema-plugins-table.md) table contains a row for each loaded plugin. Any that have a `PLUGIN_LIBRARY` value of `NULL` are built in and cannot be unloaded.
	```
	mysql> TABLE INFORMATION_SCHEMA.PLUGINS\G
	*************************** 1. row ***************************
	           PLUGIN_NAME: binlog
	        PLUGIN_VERSION: 1.0
	         PLUGIN_STATUS: ACTIVE
	           PLUGIN_TYPE: STORAGE ENGINE
	   PLUGIN_TYPE_VERSION: 80100.0
	        PLUGIN_LIBRARY: NULL
	PLUGIN_LIBRARY_VERSION: NULL
	         PLUGIN_AUTHOR: Oracle Corporation
	    PLUGIN_DESCRIPTION: This is a pseudo storage engine to represent the binlog in a transaction
	        PLUGIN_LICENSE: GPL
	           LOAD_OPTION: FORCE
	*************************** 2. row ***************************
	           PLUGIN_NAME: mysql_native_password
	        PLUGIN_VERSION: 1.1
	         PLUGIN_STATUS: ACTIVE
	           PLUGIN_TYPE: AUTHENTICATION
	   PLUGIN_TYPE_VERSION: 2.1
	        PLUGIN_LIBRARY: NULL
	PLUGIN_LIBRARY_VERSION: NULL
	         PLUGIN_AUTHOR: Oracle Corporation
	    PLUGIN_DESCRIPTION: Native MySQL authentication
	        PLUGIN_LICENSE: GPL
	           LOAD_OPTION: FORCE
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
	*************************** 2. row ***************************
	   Name: mysql_native_password
	 Status: ACTIVE
	   Type: AUTHENTICATION
	Library: NULL
	License: GPL
	...
	```
- The `mysql.plugin` table shows which plugins have been registered with [`INSTALL           PLUGIN`](install-plugin.md). The table contains only plugin names and library file names, so it does not provide as much information as the [`PLUGINS`](information-schema-plugins-table.md) table or the [`SHOW PLUGINS`](show-plugins.md) statement.