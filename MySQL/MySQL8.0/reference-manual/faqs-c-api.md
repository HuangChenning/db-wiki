---
title: "A.13 MySQL 8.0 FAQ: C API, libmysql"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/faqs-c-api.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Frequently asked questions about MySQL C API and libmysql.

A.13.1. What is “MySQL Native C API”? What are typical benefits and use cases?

A.13.2. Which version of libmysql should I use?

A.13.3. What if I want to use the “NoSQL” X DevAPI?

A.13.4. How to I download libmysql?

A.13.5. Where is the documentation?

A.13.6. How do I report bugs?

A.13.7. Is it possible to compile the library myself?

| **A.13.1.** | What is “MySQL Native C API”? What are typical benefits and use cases? |
| --- | --- |
|  | libmysql is a C-based API that you can use in C applications to connect with the MySQL database server. It is also itself used as the foundation for drivers for standard database APIs like ODBC, Perl's DBI, and Python's DB API. |
| **A.13.2.** | Which version of libmysql should I use? |
|  | For MySQL 8.0 and 5.7 we recommend libmysql 8.0. |
| **A.13.3.** | What if I want to use the “NoSQL” X DevAPI? |
|  | For C-language and X DevApi Document Store for MySQL, we recommend MySQL Connector/C++. Connector/C++ has compatible C headers. (This is not applicable to MySQL 5.7 or before.) |
| **A.13.4.** | How to I download libmysql? |
|  | - Linux: The Client Utilities Package is available from the [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) download page. - Repos: The Client Utilities Package is available from the [Yum](https://dev.mysql.com/downloads/repo/yum/), [APT](https://dev.mysql.com/downloads/repo/apt/), [SuSE repositories](https://dev.mysql.com/downloads/repo/suse/). - Windows: The Client Utilities Package is available from [Windows Installer](https://dev.mysql.com/downloads/installer/). |
| **A.13.5.** | Where is the documentation? |
|  | See [MySQL 8.0 C API Developer Guide](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/). |
| **A.13.6.** | How do I report bugs? |
|  | Please report any bugs or inconsistencies you observe to our [Bugs Database](https://bugs.mysql.com/). Select the C API Client as shown. |
| **A.13.7.** | Is it possible to compile the library myself? |
|  | Compiling MySQL Server also compiles libmysqlclient; there is not a way to only compile libmysqlclient. For related information, see [MySQL C API Implementations](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/c-api-implementations.html). |