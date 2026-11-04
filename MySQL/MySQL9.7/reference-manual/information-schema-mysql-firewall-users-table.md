---
title: "28.7.2 The INFORMATION_SCHEMA MYSQL_FIREWALL_USERS Table"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-mysql-firewall-users-table.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.7.2 The INFORMATION\_SCHEMA MYSQL\_FIREWALL\_USERS Table

The `MYSQL_FIREWALL_USERS` table provides a view into the in-memory data cache for the MySQL Enterprise Firewall plugin. It lists names and operational modes of registered firewall account profiles. It is used in conjunction with the `mysql.firewall_users` system table that provides persistent storage of firewall data; see [MySQL Enterprise Firewall Tables](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/firewall-reference.html#firewall-tables).

The `MYSQL_FIREWALL_USERS` table has these columns:

- `USERHOST`
	The account profile name. Each account name has the format ``*`user_name`*@*`host_name`*``.
- `MODE`
	The current operational mode for the profile. Permitted mode values are `OFF`, `DETECTING`, `PROTECTING`, `RECORDING`, and `RESET`. For details about their meanings, see [Firewall Concepts](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/firewall-usage.html#firewall-concepts).

This table is deprecated and subject to removal in a future MySQL version. See [Migrating Account Profiles to Group Profiles](https://docs.oracle.com/cd/E17952_01/mysql-8.4-en/firewall-usage.html#firewall-account-profile-migration).