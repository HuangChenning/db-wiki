---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_REGISTRY_LOG.html
tags:
  - oracle
  - 12c
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