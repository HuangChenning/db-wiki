---
title: "5.6.2 Obtaining Information About Loadable Functions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/obtaining-loadable-function-information.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 5.6.2 Obtaining Information About Loadable Functions

The `mysql.func` system table shows which loadable functions have been registered using [`CREATE FUNCTION`](create-function.md):

```
SELECT * FROM mysql.func;
```

The `func` table has these columns:

- `name`
	The function name as referred to in SQL statements.
- `ret`
	The function return value type. Permitted values are 0 (`STRING`), 1 (`REAL`), 2 (`INTEGER`), 3 (`ROW`), or 4 (`DECIMAL`).
- `dl`
	The name of the function library file containing the executable function code. The file is located in the directory named by the [`plugin_dir`](server-system-variables.md) system variable.
- `type`
	The function type, either `function` (scalar) or `aggregate`.