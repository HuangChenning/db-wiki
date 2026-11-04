---
title: "V$MAP_COMP_LIST"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2051.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_COMP_LIST` displays supplementary information for all element mapping structures.

| Column | Datatype | Description |
| --- | --- | --- |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `NUM_COMP` | `NUMBER` | Number of components (maximum is 5) |
| `COMP1_NAME` | `VARCHAR2(256)` | Name of the first component |
| `COMP1_VAL` | `VARCHAR2(256)` | Value of the first component |
| `COMP2_NAME` | `VARCHAR2(256)` | Name of the second component |
| `COMP2_VAL` | `VARCHAR2(256)` | Value of the second component |
| `COMP3_NAME` | `VARCHAR2(256)` | Name of the third component |
| `COMP3_VAL` | `VARCHAR2(256)` | Value of the third component |
| `COMP4_NAME` | `VARCHAR2(256)` | Name of the fourth component |
| `COMP4_VAL` | `VARCHAR2(256)` | Value of the fourth component |
| `COMP5_NAME` | `VARCHAR2(256)` | Name of the fifth component |
| `COMP5_VAL` | `VARCHAR2(256)` | Value of the fifth component |