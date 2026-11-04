---
title: "17.8.5 Configuring the Number of Background InnoDB I/O Threads"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/innodb-performance-multiple_io_threads.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 17.8.5 Configuring the Number of Background InnoDB I/O Threads

`InnoDB` uses background [threads](glossary.md) to service various types of I/O requests. You can configure the number of background threads that service read and write I/O on data pages using the [`innodb_read_io_threads`](innodb-parameters.md) and [`innodb_write_io_threads`](innodb-parameters.md) configuration parameters. These parameters signify the number of background threads used for read and write requests, respectively. They are effective on all supported platforms. You can set values for these parameters in the MySQL option file (`my.cnf` or `my.ini`); you cannot change values dynamically. The default value for [`innodb_read_io_threads`](innodb-parameters.md) is the number of available logical processors on the system divided by 2, with a minimum default value of `4`. The default value for [`innodb_write_io_threads`](innodb-parameters.md) is 4. The permissible values range from `1-64` for both options.

The purpose of these configuration options to make `InnoDB` more scalable on high end systems. Each background thread can handle up to 256 pending I/O requests. A major source of background I/O is [read-ahead](glossary.md) requests. `InnoDB` tries to balance the load of incoming requests in such way that most background threads share work equally. `InnoDB` also attempts to allocate read requests from the same extent to the same thread, to increase the chances of coalescing the requests. If you have a high end I/O subsystem and you see more than 64 × [`innodb_read_io_threads`](innodb-parameters.md) pending read requests in `SHOW ENGINE INNODB STATUS` output, you might improve performance by increasing the value of [`innodb_read_io_threads`](innodb-parameters.md).

On Linux systems, `InnoDB` uses the asynchronous I/O subsystem by default to perform read-ahead and write requests for data file pages, which changes the way that `InnoDB` background threads service these types of I/O requests. For more information, see [Section 17.8.6, “Using Asynchronous I/O on Linux”](innodb-linux-native-aio.md).

For more information about `InnoDB` I/O performance, see [Section 10.5.8, “Optimizing InnoDB Disk I/O”](optimizing-innodb-diskio.md).