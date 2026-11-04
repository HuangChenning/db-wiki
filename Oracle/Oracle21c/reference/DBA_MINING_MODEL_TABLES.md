---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_MINING_MODEL_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.182 DBA\_MINING\_MODEL\_TABLES

`DBA_MINING_MODEL_TABLES` describes the tables that contain metadata about the machine learning models in the database.

Machine learning models are schema objects created by Oracle Machine Learning for SQL (OML4SQL).

Model tables reside in the schema of the machine learning model owner. The metadata stored in the tables is controlled by OML4SQL APIs. The tables are read-only. They should not be modified by users.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the machine learning model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the machine learning model |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `TABLE_TYPE` | `VARCHAR2(21)` |  | The type of metadata stored in the table |