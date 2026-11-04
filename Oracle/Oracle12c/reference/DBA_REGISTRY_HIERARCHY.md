---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_REGISTRY_HIERARCHY.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_REGISTRY_HIERARCHY` displays information about the components loaded into the database, grouped by owner and organized in the component hierarchy.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Component namespace |
| `COMP_ID` | `VARCHAR2(4000)` |  | Component identifier |
| `VERSION` | `VARCHAR2(30)` |  | Component version loaded |
| `STATUS` | `VARCHAR2(11)` |  | Component status:  - `INVALID` - `VALID` - `LOADING` - `LOADED` - `UPGRADING` - `UPGRADED` - `DOWNGRADING` - `DOWNGRADED` - `REMOVING` - `REMOVED` |
| `MODIFIED` | `VARCHAR2(20)` |  | Time when the component was last modified |