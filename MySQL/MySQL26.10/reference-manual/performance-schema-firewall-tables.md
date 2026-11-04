---
title: "MySQL :: MySQL 26.10 Reference Manual :: 29.12.17 Performance Schema Firewall Tables"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/performance-schema-firewall-tables.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 29.12.17 Performance Schema Firewall Tables

The following sections describe the Performance Schema tables associated with MySQL Enterprise Firewall (see [Section 8.4.9, “MySQL Enterprise Firewall”](firewall.md)). They provide information about firewall operation:

- [`firewall_groups`](performance-schema-firewall-groups-table.md): Information about firewall group profiles.
- [`firewall_group_allowlist`](performance-schema-firewall-group-allowlist-table.md): Allowlist rules of registered firewall group profiles.
- [`firewall_membership`](performance-schema-firewall-membership-table.md): Members (accounts) of registered firewall group profiles.

These tables are supported by both the firewall plugin (deprecated) and the MySQL Enterprise Firewall component.