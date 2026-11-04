---
title: XMLCAST
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLCAST.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![xmlcast](img/xmlcast.gif)

> ```
> XMLCAST ( value_expression AS datatype )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration xmlcast.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/xmlcast.html)

## Purpose

`XMLCast` casts *value\_expression* to the scalar SQL data type specified by *datatype*. The *value\_expression* argument is a SQL expression that is evaluated. The *datatype* argument can be of data type `NUMBER`, `VARCHAR2`, `CHAR`, `CLOB`, `BLOB`, `REF` `XMLTYPE`, and any of the datetime data types.

**See Also:**

- [*Oracle XML DB Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=ADXDB0400) for more information on uses for this function and examples
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the return value of `XMLCAST` when it is a character value