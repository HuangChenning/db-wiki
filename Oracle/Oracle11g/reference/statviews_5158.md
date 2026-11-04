---
title: PUBLICSYN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5158.htm
tags:
  - oracle
  - 11g
  - reference
---

`PUBLICSYN` contains information on public synonyms.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAME` | `VARCHAR2(30)` |  | Name of the synonym |
| `CREATOR` | `VARCHAR2(30)` |  | Owner of the synonym |
| `TNAME` | `VARCHAR2(30)` |  | Table of which this is a synonym |
| `DATABASE` | `VARCHAR2(128)` |  | Database in which the table resides |
| `TABTYPE` | `VARCHAR2(9)` |  | Type of table |