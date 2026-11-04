---
title: "29.12.17 Performance Schema Firewall Tables"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/performance-schema-firewall-tables.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 29.12.17 Performance Schema Firewall Tables

The following sections describe the Performance Schema tables associated with MySQL Enterprise Firewall (see [Section 8.4.7, “MySQL Enterprise Firewall”](firewall.md)). They provide information about firewall operation:

- [`firewall_groups`](performance-schema-firewall-groups-table.md): Information about firewall group profiles.
- [`firewall_group_allowlist`](performance-schema-firewall-group-allowlist-table.md): Allowlist rules of registered firewall group profiles.
- [`firewall_membership`](performance-schema-firewall-membership-table.md): Members (accounts) of registered firewall group profiles.