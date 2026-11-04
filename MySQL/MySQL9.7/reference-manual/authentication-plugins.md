---
title: "8.4.1 Authentication Plugins"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/authentication-plugins.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 8.4.1 Authentication Plugins

Note

If you are looking for information about the `authentication_oci` plugin, it is MySQL HeatWave Service only. See [authentication\_oci plugin](https://docs.oracle.com/en-us/iaas/mysql-database/doc/connecting-db-system.html#MYAAS-GUID-232CA959-1FDD-4AA8-A77D-0A551C881C09), in the *MySQL HeatWave Service* manual.

The following sections describe pluggable authentication methods available in MySQL and the plugins that implement these methods. For general discussion of the authentication process, see [Section 8.2.17, “Pluggable Authentication”](pluggable-authentication.md).

The default authentication plugin is determined as described in [The Default Authentication Plugin](pluggable-authentication.md).