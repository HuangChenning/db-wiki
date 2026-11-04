---
title: "15.6.7 Condition Handling"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/condition-handling.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 15.6.7 Condition Handling

Conditions may arise during stored program execution that require special handling, such as exiting the current program block or continuing execution. Handlers can be defined for general conditions such as warnings or exceptions, or for specific conditions such as a particular error code. Specific conditions can be assigned names and referred to that way in handlers.

To name a condition, use the [`DECLARE ...       CONDITION`](declare-condition.md) statement. To declare a handler, use the [`DECLARE ...       HANDLER`](declare-handler.md) statement. See [Section 15.6.7.1, “DECLARE... CONDITION Statement”](declare-condition.md), and [Section 15.6.7.2, “DECLARE... HANDLER Statement”](declare-handler.md). For information about how the server chooses handlers when a condition occurs, see [Section 15.6.7.6, “Scope Rules for Handlers”](handler-scope.md).

To raise a condition, use the [`SIGNAL`](signal.md) statement. To modify condition information within a condition handler, use [`RESIGNAL`](resignal.md). See [Section 15.6.7.1, “DECLARE... CONDITION Statement”](declare-condition.md), and [Section 15.6.7.2, “DECLARE... HANDLER Statement”](declare-handler.md).

To retrieve information from the diagnostics area, use the [`GET DIAGNOSTICS`](get-diagnostics.md) statement (see [Section 15.6.7.3, “GET DIAGNOSTICS Statement”](get-diagnostics.md)). For information about the diagnostics area, see [Section 15.6.7.7, “The MySQL Diagnostics Area”](diagnostics-area.md).