---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_SERVER_REGISTRY.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_SERVER_REGISTRY` displays information about all server components in the database that are loaded into the component registry.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMP_ID` | `VARCHAR2(30)` | `NOT NULL` | Component identifier |
| `COMP_NAME` | `VARCHAR2(255)` |  | Component name |
| `VERSION` | `VARCHAR2(30)` |  | Component version loaded |
| `STATUS` | `VARCHAR2(11)` |  | Component status:  - `INVALID` - `VALID` - `LOADING` - `LOADED` - `UPGRADING` - `UPGRADED` - `DOWNGRADING` - `DOWNGRADED` - `REMOVING` - `REMOVED` |
| `MODIFIED` | `VARCHAR2(20)` |  | Time when the component was last modified |
| `CONTROL` | `VARCHAR2(128)` | `NOT NULL` | User that created the component entry |
| `SCHEMA` | `VARCHAR2(128)` | `NOT NULL` | User that contains the objects for the component |
| `PROCEDURE` | `VARCHAR2(61)` |  | Validation procedure |
| `STARTUP` | `VARCHAR2(8)` |  | Indicates whether the component requires a startup after the upgrade (`REQUIRED`) or not |
| `PARENT_ID` | `VARCHAR2(30)` |  | Parent component identifier |
| `OTHER_SCHEMAS` | `VARCHAR2(4000)` |  | A list of ancillary schema names associated with the component |