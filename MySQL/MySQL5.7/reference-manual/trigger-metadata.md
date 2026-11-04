---
title: "23.3.2 Trigger Metadata"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/trigger-metadata.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 23.3.2 Trigger Metadata

To obtain metadata about triggers:

- Query the [`TRIGGERS`](information-schema-triggers-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 24.3.29, “The INFORMATION\_SCHEMA TRIGGERS Table”](information-schema-triggers-table.md).
- Use the [`SHOW CREATE TRIGGER`](show-create-trigger.md) statement. See [Section 13.7.5.11, “SHOW CREATE TRIGGER Statement”](show-create-trigger.md).
- Use the [`SHOW TRIGGERS`](show-triggers.md) statement. See [Section 13.7.5.38, “SHOW TRIGGERS Statement”](show-triggers.md).