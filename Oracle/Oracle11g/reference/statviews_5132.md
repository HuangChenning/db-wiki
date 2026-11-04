---
title: HS_BASE_DD
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5132.htm
tags:
  - oracle
  - 11g
  - reference
---

`HS_BASE_DD` displays information from the base data dictionary translation table.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DD_TABLE_ID` | `NUMBER` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |
| `DD_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Oracle data dictionary table |
| `DD_TABLE_DESC` | `VARCHAR2(255)` |  | Description of the Oracle data dictionary table |