---
title: "17.20 InnoDB memcached Plugin"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/innodb-memcached.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Important

The `InnoDB` **memcached** plugin was removed in MySQL 8.3.0, and was deprecated in MySQL 8.0.22.

The `InnoDB` **memcached** plugin (`daemon_memcached`) provides an integrated **memcached** daemon that automatically stores and retrieves data from `InnoDB` tables, turning the MySQL server into a fast “key-value store”. Instead of formulating queries in SQL, you can use simple `get`, `set`, and `incr` operations that avoid the performance overhead associated with SQL parsing and constructing a query optimization plan. You can also access the same `InnoDB` tables through SQL for convenience, complex queries, bulk operations, and other strengths of traditional database software.

This “NoSQL-style” interface uses the **memcached** API to speed up database operations, letting `InnoDB` handle memory caching using its [buffer pool](glossary.md) mechanism. Data modified through **memcached** operations such as `add`, `set`, and `incr` are stored to disk, in `InnoDB` tables. The combination of **memcached** simplicity and `InnoDB` reliability and consistency provides users with the best of both worlds, as explained in [Section 17.20.1, “Benefits of the InnoDB memcached Plugin”](innodb-memcached-benefits.md). For an architectural overview, see [Section 17.20.2, “InnoDB memcached Architecture”](innodb-memcached-intro.md).