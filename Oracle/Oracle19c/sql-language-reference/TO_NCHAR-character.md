---
title: TO_NCHAR (character)
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/TO_NCHAR-character.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

## to\_nchar\_char::=

![to_nchar_char](img/to_nchar_char.gif)

> ```
> TO_NCHAR({char | clob | nclob})
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration to\_nchar\_char.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/to_nchar_char.html)

## Purpose

`TO_NCHAR` (character) converts a character string, `CHAR`, `VARCHAR2`, `CLOB`, or `NCLOB` value to the national character set. The value returned is always `NVARCHAR2`. This function is equivalent to the `TRANSLATE` … `USING` function with a `USING` clause in the national character set.

**See Also:**

- “ [Data Conversion](Data-Type-Comparison-Rules.md) ” and [TRANSLATE... USING](TRANSLATE-USING.md)
- in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of this function

## Examples

The following example converts `VARCHAR2` data from the `oe.customers` table to the national character set:

```md
SELECT TO_NCHAR(cust_last_name) FROM customers
   WHERE customer_id=103;

TO_NCHAR(CUST_LAST_NAME)
--------------------------------------------------
Taylor
```