---
title: "27.2.3 Stored Routine Metadata"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/stored-routines-metadata.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 27.2.3 Stored Routine Metadata

To obtain metadata about stored routines:

- Query the [`ROUTINES`](information-schema-routines-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 28.3.30, “The INFORMATION\_SCHEMA ROUTINES Table”](information-schema-routines-table.md).
- Use the [`SHOW CREATE PROCEDURE`](show-create-procedure.md) and [`SHOW CREATE FUNCTION`](show-create-function.md) statements to see routine definitions. See [Section 15.7.7.9, “SHOW CREATE PROCEDURE Statement”](show-create-procedure.md).
- Use the [`SHOW PROCEDURE STATUS`](show-procedure-status.md) and [`SHOW FUNCTION STATUS`](show-function-status.md) statements to see routine characteristics. See [Section 15.7.7.28, “SHOW PROCEDURE STATUS Statement”](show-procedure-status.md).
- Use the [`SHOW PROCEDURE CODE`](show-procedure-code.md) and [`SHOW FUNCTION CODE`](show-function-code.md) statements to see a representation of the internal implementation of the routine. See [Section 15.7.7.27, “SHOW PROCEDURE CODE Statement”](show-procedure-code.md).