---
title: "3.3.4 Retrieving Information from a Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/retrieving-data.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 3.3.4 Retrieving Information from a Table

The [`SELECT`](select.md) statement is used to pull information from a table. The general form of the statement is:

```
SELECT what_to_select
FROM which_table
WHERE conditions_to_satisfy;
```

*`what_to_select`* indicates what you want to see. This can be a list of columns, or `*` to indicate “all columns.” *`which_table`* indicates the table from which you want to retrieve data. The `WHERE` clause is optional. If it is present, *`conditions_to_satisfy`* specifies one or more conditions that rows must satisfy to qualify for retrieval.