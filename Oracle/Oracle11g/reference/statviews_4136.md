---
title: DBA_MINING_MODEL_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4136.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_MINING_MODEL_TABLES` describes the tables that contain metadata about the mining models in the database. Mining models are schema objects created by Oracle Data Mining.

Model tables reside in the schema of the mining model owner. The metadata stored in the tables is controlled by Oracle Data Mining APIs. The tables are read-only. They should not be modified by users.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the mining model |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `TABLE_TYPE` | `VARCHAR2(21)` |  | The type of metadata stored in the table |