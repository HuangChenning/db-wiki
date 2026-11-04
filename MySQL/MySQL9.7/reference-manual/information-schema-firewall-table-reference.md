---
title: "28.7.1 INFORMATION_SCHEMA Firewall Plugin Table Reference"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-firewall-table-reference.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.7.1 INFORMATION\_SCHEMA Firewall Plugin Table Reference

The following table summarizes `INFORMATION_SCHEMA` tables used by the MySQL Enterprise Firewall plugin. For greater detail, see the individual table descriptions.

**Table 28.9 INFORMATION\_SCHEMA Firewall Tables**

| Table Name | Description | Deprecated |
| --- | --- | --- |
| [`MYSQL_FIREWALL_USERS`](information-schema-mysql-firewall-users-table.md) | Firewall in-memory data for account profiles | Yes |
| [`MYSQL_FIREWALL_WHITELIST`](information-schema-mysql-firewall-whitelist-table.md) | Firewall in-memory data for account profile allowlists | Yes |