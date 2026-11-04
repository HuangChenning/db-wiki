---
title: "17.15 InnoDB INFORMATION_SCHEMA Tables"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-information-schema.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

This section provides information and usage examples for `InnoDB` [`INFORMATION_SCHEMA`](information-schema.md) tables.

`InnoDB` `INFORMATION_SCHEMA` tables provide metadata, status information, and statistics about various aspects of the `InnoDB` storage engine. You can view a list of `InnoDB` `INFORMATION_SCHEMA` tables by issuing a [`SHOW TABLES`](show-tables.md) statement on the `INFORMATION_SCHEMA` database:

```
mysql> SHOW TABLES FROM INFORMATION_SCHEMA LIKE 'INNODB%';
```

For table definitions, see [Section 28.4, “INFORMATION\_SCHEMA InnoDB Tables”](innodb-information-schema-tables.md). For general information regarding the `MySQL` `INFORMATION_SCHEMA` database, see [Chapter 28, *INFORMATION\_SCHEMA Tables*](information-schema.md).