---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DATABASE_PROPERTIES.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.185 DATABASE\_PROPERTIES

`DATABASE_PROPERTIES` lists permanent database properties.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROPERTY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Property name |
| `PROPERTY_VALUE` | `VARCHAR2(4000)` |  | Property value |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Property description |

Note:

The `CDB_PROPERTIES` view provides access to data visible to PDBs through the `DATABASE_PROPERTIES` view.