---
title: "V$MAP_ELEMENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2052.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MAP_ELEMENT` displays a list of all element mapping structures in the SGA of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `ELEM_NAME` | `VARCHAR2(256)` | Element name |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `ELEM_CFGID` | `VARCHAR2(256)` | Configuration ID (N/A if configuration ID is not supported) |
| `ELEM_TYPE` | `VARCHAR2(12)` | Element type: |
| `ELEM_SIZE` | `NUMBER` | Element Size in HKB |
| `ELEM_NSUBELEM` | `NUMBER` | Number of Subelements |
| `ELEM_DESCR` | `VARCHAR2(256)` | Element Description |
| `STRIPE_SIZE` | `NUMBER` | Stripe Size in HKB for RAID-5 and STRIPE elements, `0` for the remaining types |
| `LIB_IDX` | `NUMBER` | Index of the library which claims ownership of the element |