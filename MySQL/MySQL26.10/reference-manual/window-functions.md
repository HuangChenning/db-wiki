---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.20 Window Functions"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/window-functions.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 14.20 Window Functions

MySQL supports window functions that, for each row from a query, perform a calculation using rows related to that row. The following sections discuss how to use window functions, including descriptions of the `OVER` and `WINDOW` clauses. The first section provides descriptions of the nonaggregate window functions. For descriptions of the aggregate window functions, see [Section 14.19.1, “Aggregate Function Descriptions”](aggregate-functions.md).

For information about optimization and window functions, see [Section 10.2.1.21, “Window Function Optimization”](window-function-optimization.md).