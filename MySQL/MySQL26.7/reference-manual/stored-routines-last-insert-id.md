---
title: "MySQL :: MySQL 26.7 Reference Manual :: 27.2.4 Stored Procedures, Functions, Triggers, and LAST_INSERT_ID()"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/stored-routines-last-insert-id.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 27.2.4 Stored Procedures, Functions, Triggers, and LAST\_INSERT\_ID()

Within the body of a stored routine (procedure or function) or a trigger, the value of [`LAST_INSERT_ID()`](information-functions.md) changes the same way as for statements executed outside the body of these kinds of objects (see [Section 14.15, “Information Functions”](information-functions.md)). The effect of a stored routine or trigger upon the value of [`LAST_INSERT_ID()`](information-functions.md) that is seen by following statements depends on the kind of routine:

- If a stored procedure executes statements that change the value of [`LAST_INSERT_ID()`](information-functions.md), the changed value is seen by statements that follow the procedure call.
- For stored functions and triggers that change the value, the value is restored when the function or trigger ends, so following statements do not see a changed value.