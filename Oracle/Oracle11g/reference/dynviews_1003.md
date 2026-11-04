---
title: "V$ACCESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1003.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ACCESS` displays information about locks that are currently imposed on library cache objects. The locks are imposed to ensure that they are not aged out of the library cache while they are required for SQL execution.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session number that is accessing an object |
| `OWNER` | `VARCHAR2(64)` | Owner of the object |
| `OBJECT` | `VARCHAR2(1000)` | Name of the object |
| `TYPE` | `VARCHAR2(64)` | Type identifier for the object |