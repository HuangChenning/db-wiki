---
title: "17.12.4 Online DDL Memory Management"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/online-ddl-memory-management.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 17.12.4 Online DDL Memory Management

Online DDL operations that create or rebuild secondary indexes allocate temporary buffers during different phases of index creation. The [`innodb_ddl_buffer_size`](innodb-parameters.md) variable, introduced in MySQL 8.0.27, defines the maximum buffer size for online DDL operations. The default setting is 1048576 bytes (1 MB). The setting applies to buffers created by threads executing online DDL operations. Defining an appropriate buffer size limit avoids potential out of memory errors for online DDL operations that create or rebuild secondary indexes. The maximum buffer size per DDL thread is the maximum buffer size divided by the number of DDL threads ([`innodb_ddl_buffer_size`](innodb-parameters.md) / [`innodb_ddl_threads`](innodb-parameters.md)).

Prior to MySQL 8.0.27, [`innodb_sort_buffer_size`](innodb-parameters.md) variable defines the buffer size for online DDL operations that create or rebuild secondary indexes.