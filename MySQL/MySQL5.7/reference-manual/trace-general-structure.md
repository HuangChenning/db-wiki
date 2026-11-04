---
title: "8.15.11 Trace General Structure"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/trace-general-structure.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.15.11 Trace General Structure

A trace follows the actual execution path very closely; for each join, there is a join preparation object, a join optimization object, and a join execution object. Query transformations (`IN` to `EXISTS`, outer join to inner join, and so on), simplifications (elimination of clauses), and equality propagation are shown in subobjects. Calls to the range optimizer, cost evaluations, reasons why an access path is chosen over another one, or why a sorting method is chosen over another one, are shown as well.