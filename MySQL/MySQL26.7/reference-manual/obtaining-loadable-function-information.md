---
title: "MySQL :: MySQL 26.7 Reference Manual :: 7.7.2 Obtaining Information About Loadable Functions"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/obtaining-loadable-function-information.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 7.7.2 Obtaining Information About Loadable Functions

The Performance Schema [`user_defined_functions`](performance-schema-user-defined-functions-table.md) table contains information about the currently installed loadable functions:

```sql
SELECT * FROM performance_schema.user_defined_functions;
```

The `mysql.func` system table also lists installed loadable functions, but only those installed using [`CREATE       FUNCTION`](create-function-loadable.md). The [`user_defined_functions`](performance-schema-user-defined-functions-table.md) table lists loadable functions installed using [`CREATE       FUNCTION`](create-function-loadable.md) as well as loadable functions installed automatically by components or plugins. This difference makes [`user_defined_functions`](performance-schema-user-defined-functions-table.md) preferable to `mysql.func` for checking which loadable functions are installed. See [Section 29.12.22.12, “The user\_defined\_functions Table”](performance-schema-user-defined-functions-table.md).