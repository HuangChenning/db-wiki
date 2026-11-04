---
title: "V$MAP_EXT_ELEMENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2053.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_EXT_ELEMENT` displays supplementary information for all element mapping structures.

| Column | Datatype | Description |
| --- | --- | --- |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `NUM_ATTRB` | `NUMBER` | Number of Attributes (maximum is 5) |
| `ATTRB1_NAME` | `VARCHAR2(256)` | Name of the first Attribute |
| `ATTRB1_VAL` | `VARCHAR2(256)` | Value of the first attribute |
| `ATTRB2_NAME` | `VARCHAR2(256)` | Name of the second attribute |
| `ATTRB2_VAL` | `VARCHAR2(256)` | Value of the second attribute |
| `ATTRB3_NAME` | `VARCHAR2(256)` | Name of the third attribute |
| `ATTRB3_VAL` | `VARCHAR2(256)` | Value of the third attribute |
| `ATTRB4_NAME` | `VARCHAR2(256)` | Name of the fourth attribute |
| `ATTRB4_VAL` | `VARCHAR2(256)` | Value of the fourth attribute |
| `ATTRB5_NAME` | `VARCHAR2(256)` | Name of the fifth attribute |
| `ATTRB5_VAL` | `VARCHAR2(256)` | Value of the fifth attribute |