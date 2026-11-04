---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_REGISTRY_HIERARCHY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.281 DBA\_REGISTRY\_HIERARCHY

`DBA_REGISTRY_HIERARCHY` displays information about the components loaded into the database, grouped by owner and organized in the component hierarchy.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Component namespace |
| `COMP_ID` | `VARCHAR2(4000)` |  | Component identifier |
| `VERSION` | `VARCHAR2(30)` |  | Component version loaded |
| `VERSION_FULL` | `VARCHAR2(30)` |  | Component full version |
| `STATUS` | `VARCHAR2(11)` |  | Component status:  - `INVALID` - `VALID` - `LOADING` - `LOADED` - `UPGRADING` - `UPGRADED` - `DOWNGRADING` - `DOWNGRADED` - `REMOVING` - `REMOVED` |
| `MODIFIED` | `VARCHAR2(20)` |  | Time when the component was last modified |