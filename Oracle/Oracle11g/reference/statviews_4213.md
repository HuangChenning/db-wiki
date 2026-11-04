---
title: DBA_REGISTRY_LOG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4213.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REGISTRY_LOG` displays operating information about components loaded into the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPTIME` | `VARCHAR2(20)` |  | Operation time |
| `NAMESPACE` | `VARCHAR2(30)` |  | Component namespace |
| `COMP_ID` | `VARCHAR2(30)` |  | Component identifier |
| `OPERATION` | `VARCHAR2(11)` |  | Operation name |
| `MESSAGE` | `VARCHAR2(1000)` |  | Message |