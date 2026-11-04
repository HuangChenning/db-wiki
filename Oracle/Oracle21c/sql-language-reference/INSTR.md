---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/INSTR.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## INSTR

Syntax

![instr](img/instr.gif)

> ```
> { INSTR
> | INSTRB
> | INSTRC
> | INSTR2
> | INSTR4
> }
> (string , substring [, position [, occurrence ] ])
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

The `INSTR` functions search `string` for `substring`. The search operation is defined as comparing the `substring` argument with substrings of `string` of the same length for equality until a match is found or there are no more substrings left. Each consecutive compared substring of `string` begins one character to the right (for forward searches) or one character to the left (for backward searches) from the first character of the previous compared substring. If a substring that is equal to `substring` is found, then the function returns an integer indicating the position of the first character of this substring. If no such substring is found, then the function returns zero.

- `position` is an nonzero integer indicating the character of `string` where Oracle Database begins the search—that is, the position of the first character of the first substring to compare with `substring`. If `position` is negative, then Oracle counts backward from the end of `string` and then searches backward from the resulting position.
- `occurrence` is an integer indicating which occurrence of `substring` in `string` Oracle should search for. The value of `occurrence` must be positive. If `occurrence` is greater than 1, then the database does not return on the first match but continues comparing consecutive substrings of `string`, as described above, until match number `occurrence` has been found.

`INSTR` accepts and returns positions in characters as defined by the input character set, with the first character of string having position 1. `INSTRB` uses bytes instead of characters. `INSTRC` uses Unicode complete characters. `INSTR2` uses UCS2 code points. `INSTR4` uses UCS4 code points.

`string` can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`. The exceptions are `INSTRC`, `INSTR2`, and `INSTR4`, which do not allow `string` to be a `CLOB` or `NCLOB`.

`substring` can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`.

The value returned is of `NUMBER` data type.

Both `position` and `occurrence` must be of data type `NUMBER`, or any data type that can be implicitly converted to `NUMBER`, and must resolve to an integer. The default values of both `position` and `occurrence` are 1, meaning Oracle begins searching at the first character of `string` for the first occurrence of `substring`. The return value is relative to the beginning of `string`, regardless of the value of `position`.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG435) for more on character length.
- [Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=ADLOB45586) for more on character length.
- [Table 2-8](Data-Type-Comparison-Rules.md) for more information on implicit conversion
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation determination rules, which define the collation the `INSTR` functions use to compare the `substring` argument with substrings of `string`

Examples

The following example searches the string `CORPORATE` `FLOOR`, beginning with the third character, for the string " `OR` ". It returns the position in `CORPORATE` `FLOOR` at which the second occurrence of " `OR` " begins:

```
SELECT INSTR('CORPORATE FLOOR','OR', 3, 2) "Instring"
  FROM DUAL;
 
  Instring
----------
        14
```

In the next example, Oracle counts backward from the last character to the third character from the end, which is the first `O` in `FLOOR`. Oracle then searches backward for the second occurrence of `OR`, and finds that this second occurrence begins with the second character in the search string:

```
SELECT INSTR('CORPORATE FLOOR','OR', -3, 2) "Reversed Instring"
  FROM DUAL;
 
Reversed Instring
-----------------
                2
```

The next example assumes a double-byte database character set.

```
SELECT INSTRB('CORPORATE FLOOR','OR',5,2) "Instring in bytes"
  FROM DUAL;

Instring in bytes
-----------------
               27
```