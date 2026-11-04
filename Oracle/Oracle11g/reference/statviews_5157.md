---
title: PUBLIC_DEPENDENCY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5157.htm
tags:
  - oracle
  - 11g
  - reference
---

`PUBLIC_DEPENDENCY` lists dependencies to and from objects, by object number.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | Object number |
| `REFERENCED_OBJECT_ID` | `NUMBER` | `NOT NULL` | Referenced object (the parent object) |