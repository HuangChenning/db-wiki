---
title: TS_PITR_OBJECTS_TO_BE_DROPPED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5193.htm
tags:
  - oracle
  - 11g
  - reference
---

`TS_PITR_OBJECTS_TO_BE_DROPPED` lists all objects lost as a result of performing tablespace point-in-time recovery. This view applies only to the tablespace point-in-time recovery feature.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | The owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | The name of the object that will be lost as a result of undergoing tablespace point-in-time recovery |
| `CREATION_TIME` | `DATE` | `NOT NULL` | Creation timestamp of the object |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing the object |