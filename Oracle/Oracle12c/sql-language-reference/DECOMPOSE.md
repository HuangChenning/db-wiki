---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/DECOMPOSE.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![decompose](img/decompose.gif)

> ```
> DECOMPOSE( string [, { 'CANONICAL' | 'COMPATIBILITY' } ] )
> ```


Purpose

`DECOMPOSE` is valid only for Unicode characters. `DECOMPOSE` takes as its argument a string in any data type and returns a Unicode string after decomposition in the same character set as the input. For example, an o-umlaut code point will be returned as the "o" code point followed by an umlaut code point.

- `string` can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`.
- `CANONICAL` causes canonical decomposition, which allows recomposition (for example, with the `COMPOSE` function) to the original string. This is the default and returns the string in NFD normal form.
- `COMPATIBILITY` causes decomposition in compatibility mode. In this mode, recomposition is not possible. This mode is useful, for example, when decomposing half-width and full-width katakana characters, where recomposition might not be desirable without external formatting or style information. It returns the string in NFKD normal form.

`CLOB` and `NCLOB` values are supported through implicit conversion. If `char` is a character LOB value, then it is converted to a `VARCHAR` value before the `COMPOSE` operation. The operation will fail if the size of the LOB value exceeds the supported length of the `VARCHAR` in the particular development environment.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=NLSPG014) for information on Unicode character sets and character semantics
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of `DECOMPOSE`
- [COMPOSE](COMPOSE.md)

Examples

The following example decomposes the string " `Châteaux` " into its component code points:

```
SELECT DECOMPOSE ('Châteaux')
  FROM DUAL; 

DECOMPOSE
---------
Châteaux
```

Note:

The results of this example can vary depending on the character set of your operating system.