---
title: "27.6 libmysqld, the Embedded MySQL Server Library"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/libmysqld.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The embedded MySQL server library makes it possible to run a full-featured MySQL server inside a client application. The main benefits are increased speed and more simple management for embedded applications.

Note

The `libmysqld` embedded server library is deprecated as of MySQL 5.7.19 and is removed in MySQL 8.0.

The embedded server library is based on the client/server version of MySQL, which is written in C/C++. Consequently, the embedded server also is written in C/C++. There is no embedded server available in other languages.

The API is identical for the embedded MySQL version and the client/server version. To change a threaded application to use the embedded library, you normally only have to add calls to the following functions.

**Table 27.2 MySQL Embedded Server Library Functions**

| Function | When to Call |
| --- | --- |
| [`mysql_library_init()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-init.html) | Call it before any other MySQL function is called, preferably early in the `main()` function. |
| [`mysql_library_end()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-end.html) | Call it before your program exits. |
| [`mysql_thread_init()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-thread-init.html) | Call it in each thread you create that accesses MySQL. |
| [`mysql_thread_end()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-thread-end.html) | Call it before calling `pthread_exit()`. |

Then, link your code with `libmysqld.a` instead of `libmysqlclient.a`. To ensure binary compatibility between your application and the server library, always compile your application against headers for the same series of MySQL that was used to compile the server library. For example, if `libmysqld` was compiled against MySQL 5.6 headers, do not compile your application against MySQL 5.7 headers, or vice versa.

Because the ``mysql_library_*`xxx`*()`` functions are also included in `libmysqlclient.a`, you can change between the embedded and the client/server version by just linking your application with the right library. See [mysql\_library\_init()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-library-init.html).

One difference between the embedded server and the standalone server is that for the embedded server, authentication for connections is disabled by default.