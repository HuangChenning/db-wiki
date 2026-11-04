---
title: PLUGGABLE_SET_CHECK
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5153.htm
tags:
  - oracle
  - 11g
  - reference
---

`PLUGGABLE_SET_CHECK` contains pluggable set checks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJ1_OWNER` | `VARCHAR2(30)` |  | Owner of the object |
| `OBJ1_NAME` | `VARCHAR2(30)` |  | Object 1 |
| `OBJ1_SUBNAME` | `VARCHAR2(30)` |  | SubObject1Name |
| `OBJ1_TYPE` | `VARCHAR2(15)` |  | Object Type |
| `TS1_NAME` | `VARCHAR2(30)` |  | Tablespace containing Object 1 |
| `OBJ2_NAME` | `VARCHAR2(30)` |  | Object Name |
| `OBJ2_SUBNAME` | `VARCHAR2(30)` |  | SubObject2Name |
| `OBJ2_TYPE` | `VARCHAR2(15)` |  | Object Type |
| `OBJ2_OWNER` | `VARCHAR2(30)` |  | Object owner of second object |
| `TS2_NAME` | `VARCHAR2(30)` |  | Tablespace containing Object 1 |
| `CONSTRAINT_NAME` | `VARCHAR2(30)` |  | Name of dependent constraint |
| `REASON` | `VARCHAR2(79)` |  | Reason for Pluggable check violation |
| `MESG_ID` | `NUMBER` |  | The message ID |