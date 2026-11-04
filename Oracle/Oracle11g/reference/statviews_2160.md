---
title: DATABASE_PROPERTIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2160.htm
tags:
  - oracle
  - 11g
  - reference
---

`DATABASE_PROPERTIES` lists Permanent database properties.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROPERTY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Property name |
| `PROPERTY_VALUE` | `VARCHAR2(4000)` |  | Property value |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Property description |