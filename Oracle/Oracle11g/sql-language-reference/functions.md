---
title: Functions
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

## 5 Functions

Functions are similar to operators in that they manipulate data items and return a result. Functions differ from operators in the format of their arguments. This format enables them to operate on zero, one, two, or more arguments:

```
function(argument, argument, ...)
```

A function without any arguments is similar to a pseudocolumn (refer to [Chapter 2, "Pseudocolumns"](pseudocolumns.md)). However, a pseudocolumn typically returns a different value for each row in the result set, whereas a function without any arguments typically returns the same value for each row.

This chapter contains these sections:

- [About SQL Functions](functions001.md)
- [Single-Row Functions](functions002.md)
	- [Numeric Functions](functions002.md)
		- [Character Functions Returning Character Values](functions002.md)
		- [Character Functions Returning Number Values](functions002.md)
		- [Character Set Functions](functions002.md)
		- [Datetime Functions](functions002.md)
		- [General Comparison Functions](functions002.md)
		- [Conversion Functions](functions002.md)
		- [Large Object Functions](functions002.md)
		- [Collection Functions](functions002.md)
		- [Hierarchical Functions](functions002.md)
		- [Data Mining Functions](functions002.md)
		- [XML Functions](functions002.md)
		- [Encoding and Decoding Functions](functions002.md)
		- [NULL-Related Functions](functions002.md)
		- [Environment and Identifier Functions](functions002.md)
- [Aggregate Functions](functions003.md)
- [Analytic Functions](functions004.md)
- [Object Reference Functions](functions005.md)
- [Model Functions](functions006.md)
- [OLAP Functions](functions007.md)
- [Data Cartridge Functions](functions008.md)
- [About User-Defined Functions](functions256.md)