---
title: DBA_CLU_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3105.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_CLU_COLUMNS` maps all table columns to related cluster columns.

Related View

`USER_CLU_COLUMNS` maps all table columns owned by the current user to related cluster columns. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cluster |
| `CLUSTER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the cluster |
| `CLU_COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Key column in the cluster |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Clustered table name |
| `TAB_COLUMN_NAME` | `VARCHAR2(4000)` |  | Key column or attribute of the object type column |