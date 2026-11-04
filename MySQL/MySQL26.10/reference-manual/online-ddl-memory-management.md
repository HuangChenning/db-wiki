---
title: "MySQL :: MySQL 26.10 Reference Manual :: 17.12.4 Online DDL Memory Management"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/online-ddl-memory-management.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 17.12.4 Online DDL Memory Management

Online DDL operations that create or rebuild secondary indexes allocate temporary buffers during different phases of index creation. The [`innodb_ddl_buffer_size`](innodb-parameters.md) variable defines the maximum buffer size for online DDL operations. The default setting is 1048576 bytes (1 MB). The setting applies to buffers created by threads executing online DDL operations. Defining an appropriate buffer size limit avoids potential out of memory errors for online DDL operations that create or rebuild secondary indexes. The maximum buffer size per DDL thread is the maximum buffer size divided by the number of DDL threads ([`innodb_ddl_buffer_size`](innodb-parameters.md) / [`innodb_ddl_threads`](innodb-parameters.md)).