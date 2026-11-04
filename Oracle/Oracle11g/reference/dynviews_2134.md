---
title: "V$RESERVED_WORDS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2134.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RESERVED_WORDS` displays a list of all SQL keywords. To determine whether a particular keyword is reserved in any way, check the `RESERVED`, `RES_TYPE`, `RES_ATTR`, and `RES_SEMI` columns.

| Column | Datatype | Description |
| --- | --- | --- |
| `KEYWORD` | `VARCHAR2(30)` | Name of the keyword |
| `LENGTH` | `NUMBER` | Length of the keyword |
| `RESERVED` | `VARCHAR2(1)` | Indicates whether the keyword cannot be used as an identifier (`Y`) or whether the keyword is not reserved (`N`) |
| `RES_TYPE` | `VARCHAR2(1)` | Indicates whether the keyword cannot be used as a type name (`Y`) or whether the keyword is not reserved (`N`) |
| `RES_ATTR` | `VARCHAR2(1)` | Indicates whether the keyword cannot be used as an attribute name (`Y`) or whether the keyword is not reserved (`N`) |
| `RES_SEMI` | `VARCHAR2(1)` | Indicates whether the keyword is not allowed as an identifier in certain situations, such as in DML (`Y`) or whether the keyword is not reserved (`N`) |
| `DUPLICATE` | `VARCHAR2(1)` | Indicates whether the keyword is a duplicate of another keyword (`Y`) or whether the keyword is not a duplicate (`N`) |