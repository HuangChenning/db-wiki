---
title: SQL Language Reference
book: SQL Language Reference
doc_id: E83703-08
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/Functions.html
tags:
  - oracle
  - 12c
  - sql-language-reference
---

Functions are similar to operators in that they manipulate data items and return a result. Functions differ from operators in the format of their arguments. This format enables them to operate on zero, one, two, or more arguments:

```
function(argument, argument, ...)
```

A function without any arguments is similar to a pseudocolumn (refer to [Pseudocolumns](Pseudocolumns.md)). However, a pseudocolumn typically returns a different value for each row in the result set, whereas a function without any arguments typically returns the same value for each row.

This chapter contains these sections:

- [About SQL Functions](About-SQL-Functions.md)
- [Single-Row Functions](Single-Row-Functions.md)
	- [Numeric Functions](Single-Row-Functions.md)
		- [Character Functions Returning Character Values](Single-Row-Functions.md)
		- [Character Functions Returning Number Values](Single-Row-Functions.md)
		- [Character Set Functions](Single-Row-Functions.md)
		- [Collation Functions](Single-Row-Functions.md)
		- [Datetime Functions](Single-Row-Functions.md)
		- [General Comparison Functions](Single-Row-Functions.md)
		- [Conversion Functions](Single-Row-Functions.md)
		- [Large Object Functions](Single-Row-Functions.md)
		- [Collection Functions](Single-Row-Functions.md)
		- [Hierarchical Functions](Single-Row-Functions.md)
		- [Data Mining Functions](Single-Row-Functions.md)
		- [XML Functions](Single-Row-Functions.md)
		- [JSON Functions](Single-Row-Functions.md)
		- [Encoding and Decoding Functions](Single-Row-Functions.md)
		- [NULL-Related Functions](Single-Row-Functions.md)
		- [Environment and Identifier Functions](Single-Row-Functions.md)
- [Aggregate Functions](Aggregate-Functions.md)
- [Analytic Functions](Analytic-Functions.md)
- [Object Reference Functions](Object-Reference-Functions.md)
- [Model Functions](Model-Functions.md)
- [OLAP Functions](OLAP-Functions.md)
- [Data Cartridge Functions](Data-Cartridge-Functions.md)
- [About User-Defined Functions](About-User-Defined-Functions.md)