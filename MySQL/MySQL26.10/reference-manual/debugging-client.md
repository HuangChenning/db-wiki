---
title: "MySQL :: MySQL 26.10 Reference Manual :: 7.9.2 Debugging a MySQL Client"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/debugging-client.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 7.9.2 Debugging a MySQL Client

To be able to debug a MySQL client with the integrated debug package, you should configure MySQL with [`-DWITH_DEBUG=1`](source-configuration-options.md). See [Section 2.8.7, “MySQL Source-Configuration Options”](source-configuration-options.md).

Before running a client, you should set the `MYSQL_DEBUG` environment variable:

```svg
$> MYSQL_DEBUG=d:t:O,/tmp/client.trace
$> export MYSQL_DEBUG
```

This causes clients to generate a trace file in `/tmp/client.trace`.

If you have problems with your own client code, you should attempt to connect to the server and run your query using a client that is known to work. Do this by running [**mysql**](mysql.md) in debugging mode (assuming that you have compiled MySQL with debugging on):

```svg
$> mysql --debug=d:t:O,/tmp/client.trace
```

This provides useful information in case you mail a bug report. See [Section 1.6, “How to Report Bugs or Problems”](bug-reports.md).

If your client crashes at some 'legal' looking code, you should check that your `mysql.h` include file matches your MySQL library file. A very common mistake is to use an old `mysql.h` file from an old MySQL installation with new MySQL library.