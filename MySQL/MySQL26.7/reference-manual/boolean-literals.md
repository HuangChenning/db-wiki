---
title: "MySQL :: MySQL 26.7 Reference Manual :: 11.1.6 Boolean Literals"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/boolean-literals.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

[Documentation Home](https://dev.mysql.com/doc/)

---

MySQL 26.7 Reference Manual

Related Documentation

[MySQL 26.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.7/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.7-en.pdf) - 42.0Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.7-en.a4.pdf) - 42.1Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.tar.gz) - 272.1Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.zip) - 378.3Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.7.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.7.info.zip) - 4.2Mb

version 26.7

[26.10](https://dev.mysql.com/doc/refman/26.10/en/boolean-literals.html)  
[9.7 current](https://dev.mysql.com/doc/refman/9.7/en/boolean-literals.html)  
[8.4](https://dev.mysql.com/doc/refman/8.4/en/boolean-literals.html)  
[8.0](https://dev.mysql.com/doc/refman/8.0/en/boolean-literals.html)  

[8.0 Japanese](https://dev.mysql.com/doc/refman/8.0/ja/boolean-literals.html)

[MySQL 26.7 Reference Manual](https://dev.mysql.com/doc/refman/26.7/en/) / ... / Boolean Literals

### 11.1.6 Boolean Literals

The constants `TRUE` and `FALSE` evaluate to `1` and `0`, respectively. The constant names can be written in any lettercase.

```sql
mysql> SELECT TRUE, true, FALSE, false;
        -> 1, 1, 0, 0
```

[PREV](bit-value-literals.md) [HOME](index.md) [UP](literals.md) [NEXT](null-values.md)

Related Documentation

[MySQL 26.7 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/26.7/en/)

Download this Manual

[PDF (US Ltr)](https://downloads.mysql.com/docs/refman-26.7-en.pdf) - 42.0Mb  
[PDF (A4)](https://downloads.mysql.com/docs/refman-26.7-en.a4.pdf) - 42.1Mb  
[Man Pages (TGZ)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.tar.gz) - 272.1Kb  
[Man Pages (Zip)](https://downloads.mysql.com/docs/refman-26.7-en.man-gpl.zip) - 378.3Kb  
[Info (Gzip)](https://downloads.mysql.com/docs/mysql-26.7.info.gz) - 4.2Mb  
[Info (Zip)](https://downloads.mysql.com/docs/mysql-26.7.info.zip) - 4.2Mb