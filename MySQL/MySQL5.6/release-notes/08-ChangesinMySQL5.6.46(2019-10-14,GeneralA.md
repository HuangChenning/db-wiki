---
title: "Changes in MySQL 5.6.46 (2019-10-14, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=7"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

- Configuration Notes
- Security Notes
- Bugs Fixed

> Configuration Notes

- It is now possible to compile MySQL 5.6 using OpenSSL 1.1.1, enabling compilation support for MySQL

5.6 against OpenSSL even when OpenSSL 1.0.2 reaches End of Life status at the end of 2019.

## MySQL 5.6 Release Notes

In addition, MySQL 5.6 now supports TLSv1.1 and TLSv1.2 protocols for encrypted connections. This applies to MySQL Server, MySQL clients such as `mysql` and `mysqldump`, and master/slave replication.

Previously, MySQL 5.6 supported only TLSv1, so TLSv1.1/TLSv1.2 support enables use of more secure TLS protocols. It also enables connecting from MySQL 5.6 clients and replication slaves to MySQL 5.7 and higher servers that have TLSv1 disabled, which previously was not possible. It also means that MySQL 5.7 and higher clients that do not want to use TLSv1 can connect to MySQL 5.6 servers. (WL#12903)

- All MySQL 5.6 builds now use OpenSSL. MySQL no longer supports using yaSSL as the SSL library,

and source distributions no longer include yaSSL.

The `WITH_SSL` `CMake` option no longer permits `bundled` (use yaSSL) as a valid value, and the default option value has changed from `bundled` to `system` (use the version of OpenSSL installed on the host system). (WL #13289)

> Security Notes

- The linked OpenSSL library for MySQL Server has been updated to version 1.1.1c. Issues fixed

in the new OpenSSL version are described at https://www.openssl.org/news/cl111.txt and https://www.openssl.org/news/vulnerabilities.html. (Bug #29868818)

> Bugs Fixed

- Improper locking during storage engine initialization could cause a server exit. (Bug #29782379)
- VS2019 produced compilation errors with debug compilation selected due to use of the `/ZI` flag. Now /

`Z7` is used instead. (Bug #29691691, Bug #95125)

- For MySQL Community Edition, the cipher order specified by the client was used in preference to the

order on the server side, unless the server was configured with an explicit `ssl_cipher` order. (Bug#26882825)

- Password masking was incomplete for `SHOW PROCESSLIST` and some `INFORMATION_SCHEMA` and

Performance Schema tables. (Bug #20712046)

- The `-DWITH_EXAMPLE_STORAGE_ENGINE=1` `CMake` option was ignored but should not have been. If -

`DWITH_EXAMPLE_STORAGE_ENGINE=0` is given, the `EXAMPLE` storage engine is built as a plugin. (Bug#70859, Bug #17772560, Bug #30133062)References: See also: Bug #18324650.
