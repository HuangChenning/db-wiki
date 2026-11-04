---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CHAINED_ROWS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.181 CHAINED\_ROWS

`CHAINED_ROWS` stores the output for the `ANALYZE` statement with the `LIST CHAINED ROWS` clause.

You must run the `utlchain.sql` or `utlchn1.sql` script to create this table.

| Column | Description |
| --- | --- |
| `OWNER_NAME` | Table owner |
| `TABLE_NAME` | Table name |
| `CLUSTER_NAME` | Cluster the table is in, if any |
| `PARTITION_NAME` | The name of the partition |
| `SUBPARTITION_NAME` | The name of the subpartition |
| `HEAD_ROWID` | ROWID the chained row is accessed by |
| `ANALYZE_TIMESTAMP` | Date/time that the `ANALYZE` statement was issued |