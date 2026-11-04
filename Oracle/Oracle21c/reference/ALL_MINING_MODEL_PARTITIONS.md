---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MINING_MODEL_PARTITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.274 ALL\_MINING\_MODEL\_PARTITIONS

`ALL_MINING_MODEL_PARTITIONS` describes all the model partitions accessible to the user.

Related Views

- `DBA_MINING_MODEL_PARTITIONS` describes all the model partitions accessible to the system.
- `USER_MINING_MODEL_PARTITIONS` describes the user's own model partitions. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Name of the model owner |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the model |
| `PARTITION_NAME` | `VARCHAR2(128)` | – | Name of the model partition |
| `POSITION` | `NUMBER` | – | Column position number for partitioning column. Column position represents the position of the column in a multi-column partitioning key, or 1 for a unary column partitioning key. |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the column used for partitioning |
| `COLUMN_VALUE` | `VARCHAR2(4000)` | – | Value of the column for this partition |