---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/Pseudocolumns.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## 3 Pseudocolumns

A pseudocolumn behaves like a table column, but is not actually stored in the table. You can select from pseudocolumns, but you cannot insert, update, or delete their values. A pseudocolumn is also similar to a function without arguments (refer to [Functions](Functions.md)). However, functions without arguments typically return the same value for every row in the result set, whereas pseudocolumns typically return a different value for each row.

This chapter contains the following sections:

- [Hierarchical Query Pseudocolumns](Hierarchical-Query-Pseudocolumns.md)
- [Sequence Pseudocolumns](Sequence-Pseudocolumns.md)
- [Version Query Pseudocolumns](Version-Query-Pseudocolumns.md)
- [COLUMN\_VALUE Pseudocolumn](COLUMN_VALUE-Pseudocolumn.md)
- [OBJECT\_ID Pseudocolumn](OBJECT_ID-Pseudocolumn.md)
- [OBJECT\_VALUE Pseudocolumn](OBJECT_VALUE-Pseudocolumn.md)
- [ORA\_ROWSCN Pseudocolumn](ORA_ROWSCN-Pseudocolumn.md)
- [ROWID Pseudocolumn](ROWID-Pseudocolumn.md)
- [ROWNUM Pseudocolumn](ROWNUM-Pseudocolumn.md)
- [XMLDATA Pseudocolumn](XMLDATA-Pseudocolumn.md)