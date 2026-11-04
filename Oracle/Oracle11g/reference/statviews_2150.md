---
title: CHAINED_ROWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2150.htm
tags:
  - oracle
  - 11g
  - reference
---

`CHAINED_ROWS` stores the output for the `ANALYZE` statement with the `LIST CHAINED ROWS` clause. You must run the `utlchain.sql` or `utlchn1.sql` script to create this table.

| Column | Description |
| --- | --- |
| `OWNER_NAME` | Table owner |
| `TABLE_NAME` | Table name |
| `CLUSTER_NAME` | Cluster the table is in, if any |
| `PARTITION_NAME` | The name of the partition |
| `SUBPARTITION_NAME` | The name of the subpartition |
| `HEAD_ROWID` | ROWID the chained row is accessed by |
| `ANALYZE_TIMESTAMP` | Date/time that the `ANALYZE` statement was issued |