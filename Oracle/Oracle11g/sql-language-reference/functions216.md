---
title: TRANSLATE
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions216.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

  
[Description of the illustration ''translate.gif''](https://docs.oracle.com/cd/E11882_01/server.112/e41084/img_text/translate.htm)  
  

Purpose

`TRANSLATE` returns `expr` with all occurrences of each character in `from_string` replaced by its corresponding character in `to_string`. Characters in `expr` that are not in `from_string` are not replaced. The argument `from_string` can contain more characters than `to_string`. In this case, the extra characters at the end of `from_string` have no corresponding characters in `to_string`. If these extra characters appear in `expr`, then they are removed from the return value.

If a character appears multiple times in `from_string`, then the `to_string` mapping corresponding to the first occurrence is used.

You cannot use an empty string for `to_string` to remove all characters in `from_string` from the return value. Oracle Database interprets the empty string as null, and if this function has a null argument, then it returns null. To remove all characters in `from_string`, concatenate another character to the beginning of `from_string` and specify this character as the `to_string`. For example, `TRANSLATE` (`expr`, ' `x0123456789` ', ' `x` ') removes all digits from `expr`.

`TRANSLATE` provides functionality related to that provided by the `REPLACE` function. `REPLACE` lets you substitute a single string for another single string, as well as remove character strings. `TRANSLATE` lets you make several single-character, one-to-one substitutions in one operation.

This function does not support `CLOB` data directly. However, `CLOB` s can be passed in as arguments through implicit data conversion.

See Also:

["Data Type Comparison Rules"](sql_elements002.md) for more information and [REPLACE](functions153.md)

Examples

The following statement translates a book title into a string that could be used (for example) as a filename. The `from_string` contains four characters: a space, asterisk, slash, and apostrophe (with an extra apostrophe as the escape character). The `to_string` contains only three underscores. This leaves the fourth character in the `from_string` without a corresponding replacement, so apostrophes are dropped from the returned value.

```
SELECT TRANSLATE('SQL*Plus User''s Guide', ' */''', '___') FROM DUAL;

TRANSLATE('SQL*PLUSU
--------------------
SQL_Plus_Users_Guide
```