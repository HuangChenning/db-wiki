---
title: "7.6.8 MySQL Plugin Services"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/plugin-services.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 7.6.8 MySQL Plugin Services

MySQL server plugins have access to server “plugin services.” The plugin services interface complements the plugin API by exposing server functionality that plugins can call. For developer information about writing plugin services, see [MySQL Services for Plugins](https://dev.mysql.com/doc/extending-mysql/9.7/en/services-for-plugins.html). The following sections describe plugin services available at the SQL and C-language levels.