---
title: TS_PITR_CHECK
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5192.htm
tags:
  - oracle
  - 11g
  - reference
---

This view, created by `catpitr.sql`, provides information on any dependencies or restrictions that might prevent tablespace point-in-time recovery from proceeding. This view applies only to the tablespace point-in-time recovery feature.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJ1_OWNER` | `VARCHAR2(30)` | `NOT NULL` | The owner of the object preventing tablespace point-in-time recovery. See the `REASON` column for details. |
| `OBJ1_NAME` | `VARCHAR2(30)` | `NOT NULL` | The name of the object preventing tablespace point-in-time recovery |
| `OBJ1_TYPE` | `VARCHAR2(15)` |  | The object type for the object preventing tablespace point-in-time recovery |
| `OBJ1_SUBNAME` | `VARCHAR2(30)` |  | Subordinate to `OBJ1_NAME` |
| `TS1_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace containing the object preventing tablespace point-in-time recovery |
| `OBJ2_NAME` | `VARCHAR2(30)` |  | The name of a second object which may be preventing tablespace point-in-time recovery. If NULL, object 1 is the only object preventing recovery. |
| `OBJ2_TYPE` | `VARCHAR2(15)` |  | The object type for the second object (will be NULL if `OBJ2_NAME` is NULL) |
| `OBJ2_OWNER` | `VARCHAR2(30)` |  | The owner of the second object (will be NULL if `OBJ2_NAME` is NULL) |
| `OBJ2_SUBNAME` | `VARCHAR2(30)` |  | Subordinate to `OBJ2_NAME` |
| `TS2_NAME` | `VARCHAR2(30)` |  | Name of the tablespace containing second object which may be preventing tablespace point-in-time recovery (-1 indicates not applicable) |
| `CONSTRAINT_NAME` | `VARCHAR2(30)` |  | Name of the constraint |
| `REASON` | `VARCHAR2(78)` |  | Reason why tablespace point-in-time recovery cannot proceed |