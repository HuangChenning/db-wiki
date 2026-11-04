---
title: "8.6.4 MySQL Enterprise Encryption Function Reference"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/enterprise-encryption-function-reference.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 8.6.4 MySQL Enterprise Encryption Function Reference

In releases from MySQL 8.0.30, MySQL Enterprise Encryption's functions are provided by the MySQL component `component_enterprise_encryption`. For their descriptions, see [Section 8.6.5, “MySQL Enterprise Encryption Component Function Descriptions”](enterprise-encryption-functions.md).

In releases before MySQL 8.0.30, MySQL Enterprise Encryption's functions are based on the `openssl_udf` shared library. The functions continue to be available in later releases if they have been installed, but they are deprecated. For their descriptions, see [Section 8.6.6, “MySQL Enterprise Encryption Legacy Function Descriptions”](enterprise-encryption-functions-legacy.md).

For information on upgrading to the new component functions provided by the MySQL component `component_enterprise_encryption`, and a list of the behavior differences between the legacy functions and the component functions, see [Upgrading MySQL Enterprise Encryption](enterprise-encryption-installation.md).