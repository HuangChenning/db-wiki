---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/COMPOSE.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Syntax

![compose](img/compose.gif)

> ```
> COMPOSE(char)
> ```


Purpose

`COMPOSE` takes as its argument a string, or an expression that resolves to a string, in any data type, and returns a Unicode string in the same character set as the input. `char` can be any of the data types `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB`. For example, an `o` code point qualified by an umlaut code point will be returned as the o-umlaut code point.

`COMPOSE` returns the string in NFC normal form. For a more exclusive setting, you can first call `DECOMPOSE` with the `CANONICAL` setting and then `COMPOSE`. This combination returns the string in NFKC normal form.

`CLOB` and `NCLOB` values are supported through implicit conversion. If `char` is a character LOB value, then it is converted to a `VARCHAR` value before the `COMPOSE` operation. The operation will fail if the size of the LOB value exceeds the supported length of the `VARCHAR` in the particular development environment.

See Also:

- [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=NLSPG006) for information on Unicode character sets and character semantics
- Appendix C in [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of `COMPOSE`
- [DECOMPOSE](DECOMPOSE.md)

Examples

The following example returns the o-umlaut code point:

```
SELECT COMPOSE( 'o' || UNISTR('\0308') )
  FROM DUAL; 

CO 
-- 
ö
```

See Also:

[UNISTR](UNISTR.md)