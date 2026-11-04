---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-MAP_FILE_IO_STACK.html
tags:
  - oracle
  - 12c
  - reference
---

`V$MAP_FILE_IO_STACK` displays the hierarchical arrangement of storage containers for files. Each row in the view represents a level in the hierarchy.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_MAP_IDX` | `NUMBER` | File index (corresponds to `FILE_MAP_IDX` in `V$MAP_FILE`) |
| `DEPTH` | `NUMBER` | Element depth within the I/O stack |
| `ELEM_IDX` | `NUMBER` | Index corresponding to the element |
| `CU_SIZE` | `NUMBER` | Contiguous set of logical blocks of the file (in HKB units) that is resident contiguously on the element |
| `STRIDE` | `NUMBER` | Number of HKB between contiguous units (CU) in the file that are contiguous on this element. Used in RAID5 and striped files. |
| `NUM_CU` | `NUMBER` | Number of contiguous units that are adjacent to each other on this element that are separated by `STRIDE` HKB in the file. In RAID5, the number of contiguous units also include the parity stripes. |
| `ELEM_OFFSET` | `NUMBER` | Element offset in HKB units |
| `FILE_OFFSET` | `NUMBER` | Offset in HKB units from the start of the file to the first byte of the contiguous units |
| `DATA_TYPE` | `VARCHAR2(15)` | Datatype:  - `DATA` - `PARITY` - `DATA AND PARITY` |
| `PARITY_POS` | `NUMBER` | Position of the parity. Only for RAID5. This column is needed to distinguish the parity from the data part. |
| `PARITY_PERIOD` | `NUMBER` | Parity period. Only for RAID5. |
| `ID` | `NUMBER` | Unique identifier |
| `PARENT_ID` | `NUMBER` | Parent identifier |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |