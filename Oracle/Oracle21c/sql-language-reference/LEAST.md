---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/LEAST.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## LEAST

Syntax

![least](img/least.gif)

> ```
> LEAST(expr [, expr ]...)
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`LEAST` returns the least of a list of one or more expressions. Oracle Database uses the first `expr` to determine the return type. If the first `expr` is numeric, then Oracle determines the argument with the highest numeric precedence, implicitly converts the remaining arguments to that data type before the comparison, and returns that data type. If the first `expr` is not numeric, then each `expr` after the first is implicitly converted to the data type of the first `expr` before the comparison.

Oracle Database compares each `expr` using nonpadded comparison semantics. The comparison is binary by default and is linguistic if the `NLS_COMP` parameter is set to `LINGUISTIC` and the `NLS_SORT` parameter has a setting other than `BINARY`. Character comparison is based on the numerical codes of the characters in the database character set and is performed on whole strings treated as one sequence of bytes, rather than character by character. If the value returned by this function is character data, then its data type is `VARCHAR2` if the first `expr` is a character data type and `NVARCHAR2` if the first `expr` is a national character data type.

See Also:

- " [Data Type Comparison Rules](Data-Type-Comparison-Rules.md) " for more information on character comparison
- [Table 2-8](Data-Type-Comparison-Rules.md) for more information on implicit conversion and " [Floating-Point Numbers](Data-Types.md) " for information on binary-float comparison semantics
- " [GREATEST](GREATEST.md) ", which returns the greatest of a list of one or more expressions
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation determination rules, which define the collation `LEAST` uses to compare character values for `expr`, and for the collation derivation rules, which define the collation assigned to the return value of this function when it is a character value

Examples

The following statement selects the string with the least value:

```
SELECT LEAST('HARRY','HARRIOT','HAROLD') "Least"
  FROM DUAL;
 
Least 
------
HAROLD
```

In the following statement, the first argument is numeric. Oracle Database determines that the argument with the highest numeric precedence is the third argument, converts the remaining arguments to the data type of the third argument, and returns the least value as that data type:

```
SELECT LEAST (1, '2.1', '.000832') "Least"
  FROM DUAL;
 
Least
-------
.000832
```