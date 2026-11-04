---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/PUBLICSYN.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.221 PUBLICSYN

`PUBLICSYN` contains information on public synonyms.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAME ` | `VARCHAR2(128)` |  | Name of the synonym |
| `CREATOR ` | `VARCHAR2(128)` |  | Owner of the synonym |
| `TNAME ` | `VARCHAR2(128)` |  | Table of which this is a synonym |
| `DATABASE ` | `VARCHAR2(128)` |  | Database in which the table resides |
| `TABTYPE ` | `VARCHAR2(10)` |  | Type of table |