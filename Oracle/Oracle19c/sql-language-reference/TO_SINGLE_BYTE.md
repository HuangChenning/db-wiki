---
title: TO_SINGLE_BYTE
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/TO_SINGLE_BYTE.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![to_single_byte](img/to_single_byte.gif)

> ```
> TO_SINGLE_BYTE(char)
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration to\_single\_byte.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/to_single_byte.html)

## Purpose

`TO_SINGLE_BYTE` returns *char* with all of its multibyte characters converted to their corresponding single-byte characters. *char* can be of data type `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2`. The value returned is in the same data type as *char*.

Any multibyte characters in *char* that have no single-byte equivalents appear in the output as multibyte characters. This function is useful only if your database character set contains both single-byte and multibyte characters.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

**See Also:**

- “ [Data Type Comparison Rules](Data-Type-Comparison-Rules.md) ” for more information.
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of `TO_SINGLE_BYTE`

## Examples

The following example illustrates going from a multibyte `A` in UTF8 to a single byte ASCII `A`:

```md
SELECT TO_SINGLE_BYTE( CHR(15711393)) FROM DUAL;

T
-
A
```