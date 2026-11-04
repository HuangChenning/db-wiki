---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/record-comparisons.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Record Comparisons

Records cannot be tested natively for nullity, equality, or inequality.

These `BOOLEAN` expressions are illegal:

- `My_Record IS NULL`
- `My_Record_1 = My_Record_2`
- `My_Record_1 > My_Record_2`

You must write your own functions to implement such tests. For information about writing functions, see [PL/SQL Subprograms](plsql-subprograms.md).