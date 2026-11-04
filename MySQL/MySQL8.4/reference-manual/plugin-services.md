---
title: "7.6.9 MySQL Plugin Services"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/plugin-services.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 7.6.9 MySQL Plugin Services

MySQL server plugins have access to server “plugin services.” The plugin services interface complements the plugin API by exposing server functionality that plugins can call. For developer information about writing plugin services, see [MySQL Services for Plugins](https://dev.mysql.com/doc/extending-mysql/8.4/en/services-for-plugins.html). The following sections describe plugin services available at the SQL and C-language levels.