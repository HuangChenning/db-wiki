---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.41 DROP TRIGGER Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/drop-trigger.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.41 DROP TRIGGER Statement

```sql
DROP TRIGGER [IF EXISTS] [schema_name.]trigger_name
```

This statement drops a trigger. The schema (database) name is optional. If the schema is omitted, the trigger is dropped from the default schema. `DROP TRIGGER` requires the [`TRIGGER`](privileges-provided.md) privilege for the table associated with the trigger.

Use `IF EXISTS` to prevent an error from occurring for a trigger that does not exist. A `NOTE` is generated for a nonexistent trigger when using `IF EXISTS`. See [Section 15.7.7.44, “SHOW WARNINGS Statement”](show-warnings.md).

Triggers for a table are also dropped if you drop the table.