---
title: "V$LOADISTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2025.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOADISTAT` contains errors that occurred when updating indexes on a table during a load using the Direct Path API.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(31)` | Schema name |
| `TABNAME` | `VARCHAR2(31)` | Table name |
| `INDEXNAME` | `VARCHAR2(31)` | Index name |
| `SUBNAME` | `VARCHAR2(31)` | Index sub name |
| `MESSAGE_NUM` | `NUMBER` | Error message number |
| `MESSAGE` | `VARCHAR2(4000)` | Error message |