---
title: "14.20 Window Functions"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/window-functions.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

MySQL supports window functions that, for each row from a query, perform a calculation using rows related to that row. The following sections discuss how to use window functions, including descriptions of the `OVER` and `WINDOW` clauses. The first section provides descriptions of the nonaggregate window functions. For descriptions of the aggregate window functions, see [Section 14.19.1, “Aggregate Function Descriptions”](aggregate-functions.md).

For information about optimization and window functions, see [Section 10.2.1.21, “Window Function Optimization”](window-function-optimization.md).