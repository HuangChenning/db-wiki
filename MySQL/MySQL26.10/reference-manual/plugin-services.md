---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.6.8 MySQL Plugin Services"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/plugin-services.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.6.8 MySQL Plugin Services

MySQL server plugins have access to server “plugin services.” The plugin services interface complements the plugin API by exposing server functionality that plugins can call. For developer information about writing plugin services, see [MySQL Services for Plugins](https://dev.mysql.com/doc/extending-mysql/26.10/en/services-for-plugins.html). The following sections describe plugin services available at the SQL and C-language levels.