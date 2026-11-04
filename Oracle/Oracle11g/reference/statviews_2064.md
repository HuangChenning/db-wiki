---
title: ALL_SOURCE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2064.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SOURCE` describes the text source of the stored objects accessible to the current user.

Related Views

- `DBA_SOURCE` describes the text source of all stored objects in the database.
- `USER_SOURCE` describes the text source of the stored objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of object: `FUNCTION`, `JAVA SOURCE`, `PACKAGE`, `PACKAGE BODY`, `PROCEDURE`, `TRIGGER`, `TYPE`, `TYPE BODY` |
| `LINE` | `NUMBER` | `NOT NULL` | Line number of this line of source |
| `TEXT` | `VARCHAR2(4000)` |  | Text source of the stored object |