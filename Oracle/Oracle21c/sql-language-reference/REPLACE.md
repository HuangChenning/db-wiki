---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/REPLACE.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## REPLACE

Syntax

![replace](img/replace.gif)

> ```
> REPLACE(char, search_string
>         [, replacement_string ]
>        )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

`REPLACE` returns `char` with every occurrence of `search_string` replaced with `replacement_string`. If `replacement_string` is omitted or null, then all occurrences of `search_string` are removed. If `search_string` is null, then `char` is returned.

Both `search_string` and `replacement_string`, as well as `char`, can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`. The string returned is in the same character set as `char`. The function returns `VARCHAR2` if the first argument is not a LOB and returns `CLOB` if the first argument is a LOB.

`REPLACE` provides functionality related to that provided by the `TRANSLATE` function. `TRANSLATE` provides single-character, one-to-one substitution. `REPLACE` lets you substitute one string for another as well as to remove character strings.

See Also:

- [TRANSLATE](TRANSLATE.md)
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation determination rules, which define the collation `REPLACE` uses to compare characters from `char` with characters from `search_string`, and for the collation derivation rules, which define the collation assigned to the character return value of this function

Examples

The following example replaces occurrences of `J` with `BL`:

```
SELECT REPLACE('JACK and JUE','J','BL') "Changes"
     FROM DUAL;

Changes
--------------
BLACK and BLUE
```