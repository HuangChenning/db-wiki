---
title: "MySQL :: MySQL 26.7 Reference Manual :: 5.3.4 Retrieving Information from a Table"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/retrieving-data.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 5.3.4 Retrieving Information from a Table

The [`SELECT`](select.md) statement is used to pull information from a table. The general form of the statement is:

```sql
SELECT what_to_select
FROM which_table
WHERE conditions_to_satisfy;
```

*`what_to_select`* indicates what you want to see. This can be a list of columns, or `*` to indicate “all columns.” *`which_table`* indicates the table from which you want to retrieve data. The `WHERE` clause is optional. If it is present, *`conditions_to_satisfy`* specifies one or more conditions that rows must satisfy to qualify for retrieval.