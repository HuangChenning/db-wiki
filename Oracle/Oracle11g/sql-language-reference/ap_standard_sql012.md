---
title: Oracle Extensions to Standard SQL
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/ap_standard_sql012.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Oracle supports numerous features that extend beyond standard SQL. If you are concerned with the portability of your applications to other implementations of SQL, then use Oracle's FIPS Flagger to help identify the use of Oracle extensions to Entry SQL-92 in your embedded SQL programs. The FIPS Flagger is part of the Oracle precompilers and the SQL\*Module compiler. The FIPS Flagger can also be enabled in SQL\*Plus by using `ALTER` `SESSION` `SET` `FLAGGER` `=` `ENTRY`. While SQL-92 has been superseded by SQL:2008, there has been no conformance testing authority for any version of SQL since SQL-92; hence, Entry SQL-92 offers you the most assurance of portability.

See Also:

[Pro\*COBOL Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10826/toc.htm) and [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm) for information on how to use the FIPS Flagger