---
title: "A.7 MySQL 8.4 FAQ: INFORMATION_SCHEMA"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/faqs-information-schema.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

A.7.1. Where can I find documentation for the MySQL INFORMATION\_SCHEMA database?

A.7.2. Is there a discussion forum for INFORMATION\_SCHEMA?

A.7.3. Where can I find the ANSI SQL 2003 specification for INFORMATION\_SCHEMA?

A.7.4. What is the difference between the Oracle Data Dictionary and MySQL INFORMATION\_SCHEMA?

A.7.5. Can I add to or otherwise modify the tables found in the INFORMATION\_SCHEMA database?

| **A.7.1.** | Where can I find documentation for the MySQL `INFORMATION_SCHEMA` database? |
| --- | --- |
|  | See [Chapter 28, *INFORMATION\_SCHEMA Tables*](information-schema.md).  You may also find the [MySQL User Forums](https://forums.mysql.com/list.php?20) to be helpful. |
| **A.7.2.** | Is there a discussion forum for `INFORMATION_SCHEMA`? |
|  | See the [MySQL User Forums](https://forums.mysql.com/list.php?20). |
| **A.7.3.** | Where can I find the ANSI SQL 2003 specification for `INFORMATION_SCHEMA`? |
|  | Unfortunately, the official specifications are not freely available. (ANSI makes them available for purchase.) However, there are books available, such as *SQL-99 Complete, Really* by Peter Gulutzan and Trudy Pelzer, that provide a comprehensive overview of the standard, including `INFORMATION_SCHEMA`. |
| **A.7.4.** | What is the difference between the Oracle Data Dictionary and MySQL `INFORMATION_SCHEMA`? |
|  | Both Oracle and MySQL provide metadata in tables. However, Oracle and MySQL use different table names and column names. The MySQL implementation is more similar to those found in DB2 and SQL Server, which also support `INFORMATION_SCHEMA` as defined in the SQL standard. |
| **A.7.5.** | Can I add to or otherwise modify the tables found in the `INFORMATION_SCHEMA` database? |
|  | No. Since applications may rely on a certain standard structure, this should not be modified. For this reason, *we cannot support bugs or other issues which result from modifying `INFORMATION_SCHEMA` tables or data*. |