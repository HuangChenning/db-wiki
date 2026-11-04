---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_MINING_MODEL_TABLES.html
tags:
  - oracle
  - 19c
  - reference
---

## 5.182 DBA\_MINING\_MODEL\_TABLES

`DBA_MINING_MODEL_TABLES` describes the tables that contain metadata about the mining models in the database.

Mining models are schema objects created by Oracle Data Mining.

Model tables reside in the schema of the mining model owner. The metadata stored in the tables is controlled by Oracle Data Mining APIs. The tables are read-only. They should not be modified by users.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the mining model |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `TABLE_TYPE` | `VARCHAR2(21)` |  | The type of metadata stored in the table |