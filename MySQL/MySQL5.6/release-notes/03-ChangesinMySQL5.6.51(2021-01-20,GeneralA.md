---
title: "Changes in MySQL 5.6.51 (2021-01-20, General Availability)"
book: MySQL 5.6 Release Notes
version: "5.6"
source: "MySQL/MySQL5.6/sources/mysql-5.6-relnotes-en.pdf#page=4"
tags:
  - mysql
  - mysql-5.6
  - release-notes
---

Note MySQL 5.6.51 is the last release of the MySQL 5.6 series.

- Security Notes
- Bugs Fixed

> Security Notes

- The linked OpenSSL library for MySQL Server has been updated to version 1.1.1i. Issues fixed

in the new OpenSSL version are described at https://www.openssl.org/news/cl111.txt and https://www.openssl.org/news/vulnerabilities.html. (Bug #32260610)

> Bugs Fixed

- InnoDB: The full-text search synchronization thread attempted to read a previously-freed word from the

index cache. (Bug #31310404)

- The server did not handle all cases of the `WHERE_CONDITION` optimization correctly. (Bug #31905199)
- Privileges for some `INFORMATION_SCHEMA` tables were checked incorrectly. (Bug #31553323)
- In certain cases, the server did not handle multiply-nested subqueries correctly. (Bug #31472704)
- A buffer overflow in the client library was fixed. (Bug #30885987)
