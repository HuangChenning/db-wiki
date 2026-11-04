---
title: "28.7.3 The INFORMATION_SCHEMA MYSQL_FIREWALL_WHITELIST Table"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-mysql-firewall-whitelist-table.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.7.3 The INFORMATION\_SCHEMA MYSQL\_FIREWALL\_WHITELIST Table

The `MYSQL_FIREWALL_WHITELIST` table provides a view into the in-memory data cache for the MySQL Enterprise Firewall plugin. It lists allowlist rules of registered firewall account profiles. It is used in conjunction with the `mysql.firewall_whitelist` system table that provides persistent storage of firewall data; see [MySQL Enterprise Firewall Tables](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/firewall-reference.html#firewall-tables).

The `MYSQL_FIREWALL_WHITELIST` table has these columns:

- `USERHOST`
	The account profile name. Each account name has the format ``*`user_name`*@*`host_name`*``.
- `RULE`
	A normalized statement indicating an acceptable statement pattern for the profile. A profile allowlist is the union of its rules.

This table is deprecated and subject to removal in a future MySQL version. See [Migrating Account Profiles to Group Profiles](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/firewall-usage.html#firewall-account-profile-migration).