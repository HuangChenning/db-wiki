---
title: "27.4.2 Trigger Metadata"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/trigger-metadata.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 27.4.2 Trigger Metadata

To obtain metadata about triggers:

- Query the [`TRIGGERS`](information-schema-triggers-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 28.3.50, “The INFORMATION\_SCHEMA TRIGGERS Table”](information-schema-triggers-table.md).
- Use the [`SHOW CREATE TRIGGER`](show-create-trigger.md) statement. See [Section 15.7.7.13, “SHOW CREATE TRIGGER Statement”](show-create-trigger.md).
- Use the [`SHOW TRIGGERS`](show-triggers.md) statement. See [Section 15.7.7.41, “SHOW TRIGGERS Statement”](show-triggers.md).