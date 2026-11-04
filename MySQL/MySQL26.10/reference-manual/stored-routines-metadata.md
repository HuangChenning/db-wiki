---
title: "MySQL :: MySQL 26.10 Reference Manual :: 27.2.3 Stored Routine Metadata"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/stored-routines-metadata.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 27.2.3 Stored Routine Metadata

To obtain metadata about stored routines:

- Query the [`ROUTINES`](information-schema-routines-table.md) table of the `INFORMATION_SCHEMA` database. See [Section 28.3.36, “The INFORMATION\_SCHEMA ROUTINES Table”](information-schema-routines-table.md).
- Use the [`SHOW CREATE PROCEDURE`](show-create-procedure.md) and [`SHOW CREATE FUNCTION`](show-create-function.md) statements to see routine definitions. See [Section 15.7.7.12, “SHOW CREATE PROCEDURE Statement”](show-create-procedure.md).
- Use the [`SHOW PROCEDURE STATUS`](show-procedure-status.md) and [`SHOW FUNCTION STATUS`](show-function-status.md) statements to see routine characteristics. See [Section 15.7.7.32, “SHOW PROCEDURE STATUS Statement”](show-procedure-status.md).
- Use the [`SHOW PROCEDURE CODE`](show-procedure-code.md) and [`SHOW FUNCTION CODE`](show-function-code.md) statements to see a representation of the internal implementation of the routine. See [Section 15.7.7.31, “SHOW PROCEDURE CODE Statement”](show-procedure-code.md).