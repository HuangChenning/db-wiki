---
title: "24.3.10 The INFORMATION_SCHEMA GLOBAL_STATUS and SESSION_STATUS Tables"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-status-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.3.10 The INFORMATION\_SCHEMA GLOBAL\_STATUS and SESSION\_STATUS Tables

Note

The value of the [`show_compatibility_56`](server-system-variables.md) system variable affects the information available from the tables described here. For details, see the description of that variable in [Section 5.1.7, “Server System Variables”](server-system-variables.md).

Note

Information available from the tables described here is also available from the Performance Schema. The `INFORMATION_SCHEMA` tables are deprecated in preference to the Performance Schema tables and are removed in MySQL 8.0. For advice on migrating away from the `INFORMATION_SCHEMA` tables to the Performance Schema tables, see [Section 25.20, “Migrating to Performance Schema System and Status Variable Tables”](performance-schema-variable-table-migration.md).

The `GLOBAL_STATUS` and `SESSION_STATUS` tables provide information about server status variables. Their contents correspond to the information produced by the [`SHOW GLOBAL       STATUS`](show-status.md) and [`SHOW SESSION       STATUS`](show-status.md) statements (see [Section 13.7.5.35, “SHOW STATUS Statement”](show-status.md)).

#### Notes

- The `VARIABLE_VALUE` column for each of these tables is defined as `VARCHAR(1024)`.