---
title: RESOURCE_MAP
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5168.htm
tags:
  - oracle
  - 11g
  - reference
---

`RESOURCE_MAP` describes resources. This table can be used to map resource names to resource numbers.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RESOURCE#` | `NUMBER` | `NOT NULL` | Numeric resource code |
| `TYPE#` | `NUMBER` | `NOT NULL` | Numeric type code |
| `NAME` | `VARCHAR2(32)` | `NOT NULL` | Name of the resource |