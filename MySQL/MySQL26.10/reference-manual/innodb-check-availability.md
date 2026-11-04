---
title: "MySQL :: MySQL 26.10 Reference Manual :: 17.1.3 Verifying that InnoDB is the Default Storage Engine"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/innodb-check-availability.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.10 Reference Manual

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb

version 26.10

[26.7](https://dev.mysql.com/doc/refman/26.7/en/innodb-check-availability.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/innodb-check-availability.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/innodb-check-availability.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/innodb-check-availability.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/innodb-check-availability.html)

[MySQL 26.10 Reference Manual](https://dev.mysql.com/doc/refman/26.10/en/) / ... / Verifying that InnoDB is the Default Storage Engine

### 17.1.3 Verifying that InnoDB is the Default Storage Engine

Issue a [`SHOW ENGINES`](show-engines.md) statement to view the available MySQL storage engines. Look for `DEFAULT` in the `SUPPORT` column.

```sql
mysql> SHOW ENGINES;
```

Alternatively, query the Information Schema [`ENGINES`](information-schema-engines-table.md) table.

```sql
mysql> SELECT * FROM INFORMATION_SCHEMA.ENGINES;
```

Related Documentation

[MySQL 26.10 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.10/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.10-en.pdf) - 42.3Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.10-en.a4.pdf) - 42.4Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.tar.gz) - 272.9Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.10-en.man-gpl.zip) - 379.1Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.10.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.10.info.zip) - 4.2Mb