---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PUBLICSYN.html
tags:
  - oracle
  - 12c
  - reference
---

`PUBLICSYN` contains information on public synonyms.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAME ` | `VARCHAR2(128)` |  | Name of the synonym |
| `CREATOR ` | `VARCHAR2(128)` |  | Owner of the synonym |
| `TNAME ` | `VARCHAR2(128)` |  | Table of which this is a synonym |
| `DATABASE ` | `VARCHAR2(128)` |  | Database in which the table resides |
| `TABTYPE ` | `VARCHAR2(10)` |  | Type of table |