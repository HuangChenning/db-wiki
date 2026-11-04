---
title: "V$FIXED_TABLE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1142.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FIXED_TABLE` displays all dynamic performance tables, views, and derived tables in the database. Some `V$` tables (for example, `V$ROLLNAME`) refer to real tables and are therefore not listed.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(30)` | Name of the object |
| `OBJECT_ID` | `NUMBER` | Identifier of the fixed object |
| `TYPE` | `VARCHAR2(5)` | Object type (`TABLE` \| `VIEW`) |
| `TABLE_NUM` | `NUMBER` | Number that identifies the dynamic performance table if it is of type `TABLE` |