---
title: "27.3.2 Trigger Metadata"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/trigger-metadata.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 27.3.2 Trigger Metadata

To obtain metadata about triggers:

- Query the [`TRIGGERS`](information-schema-triggers-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 28.3.44, “The INFORMATION\_SCHEMA TRIGGERS Table”](information-schema-triggers-table.md).
- Use the [`SHOW CREATE TRIGGER`](show-create-trigger.md) statement. See [Section 15.7.7.12, “SHOW CREATE TRIGGER Statement”](show-create-trigger.md).
- Use the [`SHOW TRIGGERS`](show-triggers.md) statement. See [Section 15.7.7.40, “SHOW TRIGGERS Statement”](show-triggers.md).