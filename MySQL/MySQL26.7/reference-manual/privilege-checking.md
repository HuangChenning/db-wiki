---
title: "MySQL :: MySQL 26.7 Reference Manual :: 10.15.6 Privilege Checking"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/privilege-checking.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 10.15.6 Privilege Checking

In complex scenarios where the query uses SQL SECURITY DEFINER views or stored routines, it may be that a user is denied from seeing the trace of its query because it lacks some extra privileges on those objects. In that case, the trace will be shown as empty and the INSUFFICIENT\_PRIVILEGES column will show "1".