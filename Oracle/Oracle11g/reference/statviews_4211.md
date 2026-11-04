---
title: DBA_REGISTRY_HIERARCHY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4211.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_REGISTRY_HIERARCHY` displays information about the components loaded into the database, grouped by owner and organized in the component hierarchy.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAMESPACE` | `VARCHAR2(30)` | `NOT NULL` | Component namespace |
| `COMP_ID` | `VARCHAR2(4000)` |  | Component identifier |
| `VERSION` | `VARCHAR2(30)` |  | Component version loaded |
| `STATUS` | `VARCHAR2(11)` |  | Component status: - `INVALID` - `VALID` - `LOADING` - `LOADED` - `UPGRADING` - `UPGRADED` - `DOWNGRADING` - `DOWNGRADED` - `REMOVING` - `REMOVED` |
| `MODIFIED` | `VARCHAR2(20)` |  | Time when the component was last modified |