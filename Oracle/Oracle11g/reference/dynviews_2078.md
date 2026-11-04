---
title: "V$OBJECT_PRIVILEGE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2078.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OBJECT_PRIVILEGE` displays information about privileges associated with an object.

| Column | Datatype | Description |
| --- | --- | --- |
| `OBJECT_TYPE_NAME` | `VARCHAR2(64)` | Name of the object type |
| `OBJECT_TYPE_ID` | `NUMBER` | ID of the object type |
| `PRIVILEGE_ID` | `NUMBER` | ID of the privilege |
| `PRIVILEGE_NAME` | `VARCHAR2(64)` | Name of the privilege |