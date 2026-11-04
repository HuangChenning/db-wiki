---
title: "24.7.3 The INFORMATION_SCHEMA MYSQL_FIREWALL_WHITELIST Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-mysql-firewall-whitelist-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.7.3 The INFORMATION\_SCHEMA MYSQL\_FIREWALL\_WHITELIST Table

The `MYSQL_FIREWALL_WHITELIST` table provides a view into the in-memory data cache for MySQL Enterprise Firewall. It lists allowlist rules of registered firewall account profiles. It is used in conjunction with the `mysql.firewall_whitelist` system table that provides persistent storage of firewall data; see [MySQL Enterprise Firewall Tables](firewall-reference.md).

The `MYSQL_FIREWALL_WHITELIST` table has these columns:

- `USERHOST`
	The account profile name. Each account name has the format ``*`user_name`*@*`host_name`*``.
- `RULE`
	A normalized statement indicating an acceptable statement pattern for the profile. A profile allowlist is the union of its rules.