---
title: "6.4.1 Authentication Plugins"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/authentication-plugins.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 6.4.1 Authentication Plugins

The following sections describe pluggable authentication methods available in MySQL and the plugins that implement these methods. For general discussion of the authentication process, see [Section 6.2.13, “Pluggable Authentication”](pluggable-authentication.md).

The default plugin is indicated by the value of the [`default_authentication_plugin`](server-system-variables.md) system variable.