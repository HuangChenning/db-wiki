---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.6.3 MySQL Thread Pool"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/thread-pool.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.6.3 MySQL Thread Pool

MySQL Thread Pool is implemented using a server plugin. The default thread-handling model in MySQL Server executes statements using one thread per client connection. As more clients connect to the server and execute statements, overall performance degrades. The thread pool plugin provides an alternative thread-handling model designed to reduce overhead and improve performance. The plugin implements a thread pool that increases server performance by efficiently managing statement execution threads for large numbers of client connections.

The thread pool addresses several problems of the model that uses one thread per connection:

- Too many thread stacks make CPU caches almost useless in highly parallel execution workloads. The thread pool promotes thread stack reuse to minimize the CPU cache footprint.
- With too many threads executing in parallel, context switching overhead is high. This also presents a challenge to the operating system scheduler. The thread pool controls the number of active threads to keep the parallelism within the MySQL server at a level that it can handle and that is appropriate for the server host on which MySQL is executing.
- Too many transactions executing in parallel increases resource contention. In [`InnoDB`](innodb-storage-engine.md), this increases the time spent holding central mutexes. The thread pool controls when transactions start to ensure that not too many execute in parallel.

#### Additional Resources

[Section A.15, “MySQL 26.10 FAQ: MySQL Enterprise Thread Pool”](faqs-thread-pool.md)