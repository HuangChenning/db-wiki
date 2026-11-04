---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-MAP_ELEMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.67 V$MAP\_ELEMENT

`V$MAP_ELEMENT` displays a list of all element mapping structures in the SGA of the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `ELEM_NAME` | `VARCHAR2(256)` | Element name |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `ELEM_CFGID` | `VARCHAR2(256)` | Configuration ID (N/A if configuration ID is not supported) |
| `ELEM_TYPE` | `VARCHAR2(12)` | Element type:  - `MIRROR` - `STRIPE` - `RAID5` - `CONCATENATED` - `PARTITION` - `DISK` - `NONE` |
| `ELEM_SIZE` | `NUMBER` | Element Size in HKB |
| `ELEM_NSUBELEM` | `NUMBER` | Number of Subelements |
| `ELEM_DESCR` | `VARCHAR2(256)` | Element Description |
| `STRIPE_SIZE` | `NUMBER` | Stripe Size in HKB for RAID-5 and STRIPE elements, `0` for the remaining types |
| `LIB_IDX` | `NUMBER` | Index of the library which claims ownership of the element |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |