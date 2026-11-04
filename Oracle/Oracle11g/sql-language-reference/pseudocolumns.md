---
title: Pseudocolumns
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/pseudocolumns.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

## 2 Pseudocolumns

A pseudocolumn behaves like a table column, but is not actually stored in the table. You can select from pseudocolumns, but you cannot insert, update, or delete their values. A pseudocolumn is also similar to a function without arguments (refer to [Chapter 5, "Functions"](functions.md)). However, functions without arguments typically return the same value for every row in the result set, whereas pseudocolumns typically return a different value for each row.

This chapter contains the following sections:

- [Hierarchical Query Pseudocolumns](pseudocolumns001.md)
- [Sequence Pseudocolumns](pseudocolumns002.md)
- [Version Query Pseudocolumns](pseudocolumns003.md)
- [COLUMN\_VALUE Pseudocolumn](pseudocolumns004.md)
- [OBJECT\_ID Pseudocolumn](pseudocolumns005.md)
- [OBJECT\_VALUE Pseudocolumn](pseudocolumns006.md)
- [ORA\_ROWSCN Pseudocolumn](pseudocolumns007.md)
- [ROWID Pseudocolumn](pseudocolumns008.md)
- [ROWNUM Pseudocolumn](pseudocolumns009.md)
- [XMLDATA Pseudocolumn](pseudocolumns010.md)