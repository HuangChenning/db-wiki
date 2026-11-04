---
title: "29.12.17 Performance Schema Firewall Tables"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/performance-schema-firewall-tables.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 29.12.17 Performance Schema Firewall Tables

Note

The Performance Schema tables described here are available as of MySQL 8.0.23. Prior to MySQL 8.0.23, use the corresponding `INFORMATION_SCHEMA` tables instead; see [MySQL Enterprise Firewall Tables](firewall-reference.md).

The following sections describe the Performance Schema tables associated with MySQL Enterprise Firewall (see [Section 8.4.7, “MySQL Enterprise Firewall”](firewall.md)). They provide information about firewall operation:

- [`firewall_groups`](performance-schema-firewall-groups-table.md): Information about firewall group profiles.
- [`firewall_group_allowlist`](performance-schema-firewall-group-allowlist-table.md): Allowlist rules of registered firewall group profiles.
- [`firewall_membership`](performance-schema-firewall-membership-table.md): Members (accounts) of registered firewall group profiles.