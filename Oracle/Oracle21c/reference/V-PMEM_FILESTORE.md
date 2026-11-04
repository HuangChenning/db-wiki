---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PMEM_FILESTORE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.124 V$PMEM\_FILESTORE

`V$PMEM_FILESTORE` displays information about Persistent Memory Filestores (PMEM Filestores).

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(65)` | PMEM Filestore name |
| `MOUNT_POINT` | `VARCHAR2(513)` | Operating system directory path for the mount point of the PMEM Filestore |
| `BACKING_FILE` | `VARCHAR2(513)` | Operating system file path for the backing file of the PMEM Filestore |
| `BLOCK_SIZE` | `NUMBER` | Block size of the PMEM Filestore (in bytes) |
| `TOTAL_BYTES` | `NUMBER` | Current size of the PMEM Filestore (in bytes) |
| `AUTOEXTENSIBLE` | `VARCHAR2(4)` | Indicates whether the PMEM Filestore is autoextensible (`YES`) or not (`NO`) |
| `INCREMENT_BY` | `NUMBER` | If the PMEM Filestore is autoextensible, then this column displays the size of an autoextension increment (in bytes)  If the PMEM Filestore is not autoextensible, then the value of this column is 0 |
| `MAX_BYTES` | `NUMBER` | Maximum autoextend size (in bytes) |
| `AVAILABLE_BYTES` | `NUMBER` | Amount of free space currently available in the PMEM Filestore (in bytes) |
| `USED_BYTES` | `NUMBER` | Amount of space currently allocated to data and metadata in the PMEM Filestore (in bytes) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.