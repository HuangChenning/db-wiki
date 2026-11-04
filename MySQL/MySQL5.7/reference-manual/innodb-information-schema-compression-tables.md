---
title: "14.16.1 InnoDB INFORMATION_SCHEMA Tables about Compression"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/innodb-information-schema-compression-tables.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 14.16.1 InnoDB INFORMATION\_SCHEMA Tables about Compression

There are two pairs of `InnoDB` `INFORMATION_SCHEMA` tables about compression that can provide insight into how well compression is working overall:

- [`INNODB_CMP`](information-schema-innodb-cmp-table.md) and [`INNODB_CMP_RESET`](information-schema-innodb-cmp-table.md) provide information about the number of compression operations and the amount of time spent performing compression.
- [`INNODB_CMPMEM`](information-schema-innodb-cmpmem-table.md) and [`INNODB_CMPMEM_RESET`](information-schema-innodb-cmpmem-table.md) provide information about the way memory is allocated for compression.