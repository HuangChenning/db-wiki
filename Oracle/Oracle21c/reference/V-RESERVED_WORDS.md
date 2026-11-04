---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RESERVED_WORDS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.166 V$RESERVED\_WORDS

To determine whether a particular keyword is reserved in any way, check the `RESERVED`, `RES_TYPE`, `RES_ATTR`, and `RES_SEMI` columns.

| Column | Datatype | Description |
| --- | --- | --- |
| `KEYWORD` | `VARCHAR2(128)` | Name of the keyword |
| `LENGTH` | `NUMBER` | Length of the keyword |
| `RESERVED` | `VARCHAR2(1)` | Indicates whether the keyword cannot be used as an identifier (`Y`) or whether the keyword is not reserved (`N`) |
| `RES_TYPE` | `VARCHAR2(1)` | Indicates whether the keyword cannot be used as a type name (`Y`) or whether the keyword is not reserved (`N`) |
| `RES_ATTR` | `VARCHAR2(1)` | Indicates whether the keyword cannot be used as an attribute name (`Y`) or whether the keyword is not reserved (`N`) |
| `RES_SEMI` | `VARCHAR2(1)` | Indicates whether the keyword is not allowed as an identifier in certain situations, such as in DML (`Y`) or whether the keyword is not reserved (`N`) |
| `DUPLICATE` | `VARCHAR2(1)` | Indicates whether the keyword is a duplicate of another keyword (`Y`) or whether the keyword is not a duplicate (`N`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |