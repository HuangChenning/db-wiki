---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAP_OBJECT.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.210 MAP\_OBJECT

`MAP_OBJECT` is a global temporary table that displays the hierarchical arrangement of storage containers for objects. Each row in the table represents a level in the hierarchy.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_NAME` | `VARCHAR2(2000)` |  | Name of the object |
| `OBJECT_OWNER` | `VARCHAR2(2000)` |  | Owner of the object |
| `OBJECT_TYPE` | `VARCHAR2(2000)` |  | Object type |
| `FILE_MAP_IDX` | `NUMBER` |  | File index (corresponds to `FILE_MAP_IDX` in `V$MAP_FILE`) |
| `DEPTH` | `NUMBER` |  | Element depth within the I/O stack |
| `ELEM_IDX` | `NUMBER` |  | Index corresponding to the element |
| `CU_SIZE` | `NUMBER` |  | Contiguous set of logical blocks of the file (in HKB units) that is resident contiguously on the element |
| `STRIDE` | `NUMBER` |  | Number of HKB between contiguous units (CU) in the file that are contiguous on this element. Used in RAID5 and striped files. |
| `NUM_CU` | `NUMBER` |  | Number of contiguous units that are adjacent to each other on this element that are separated by STRIDE HKB in the file. In RAID5, the number of contiguous units also include the parity stripes. |
| `ELEM_OFFSET` | `NUMBER` |  | Element offset (in HKB units) |
| `FILE_OFFSET` | `NUMBER` |  | Offset (in HKB units) from the start of the file to the first byte of the contiguous units |
| `DATA_TYPE` | `VARCHAR2(2000)` |  | Data type (`DATA`, `PARITY`, or `DATA AND PARITY`) |
| `PARITY_POS` | `NUMBER` |  | Position of the parity. Only for RAID5. This field is needed to distinguish the parity from the data part. |
| `PARITY_PERIOD` | `NUMBER` |  | Parity period. Only for RAID5. |