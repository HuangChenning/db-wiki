---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PROCESS_MEMORY_DETAIL.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.131 V$PROCESS\_MEMORY\_DETAIL

`V$PROCESS_MEMORY_DETAIL` provides detailed information on dynamic PGA memory usage for each automatically captured snapshot.

| Column | Datatype | Description |
| --- | --- | --- |
| `PID` | `NUMBER` | Oracle process identifier |
| `SERIAL#` | `NUMBER` | Oracle process serial number |
| `TIMESTAMP` | `DATE` | Time at which the snapshot was taken |
| `SQL_ID` | `VARCHAR2(13)` | Identifier for the relevant SQL statement |
| `TOTAL_MB` | `NUMBER` | Total number of megabytes of PGA memory allocated at the time of the snapshot |
| `CATEGORY` | `VARCHAR2(15)` | Category name. Categories include:  - `SQL` - `PL/SQL` - `OLAP` - `JAVA` - `Freeable` - `Other` |
| `NAME` | `VARCHAR2(26)` | PGA memory allocation comment. Small allocations may be grouped together with `NAME` set to `Miscellaneous` for performance reasons. |
| `HEAP_NAME` | `VARCHAR2(15)` | Name of heap or heaps (if same name) containing the allocations |
| `BYTES` | `NUMBER` | Bytes of PGA memory allocated in the process from heaps with the given heap name and with the given allocation comment |
| `ALLOCATION_COUNT` | `NUMBER` | Number of allocations with the comment found in the process inside heaps with the given heap name |
| `HEAP_DESCRIPTOR` | `RAW(4 \| 8)` | If all the allocations are from one heap, then this is the address of the heap descriptor for that heap. Otherwise, this column is null. |
| `PARENT_HEAP_DESCRIPTOR` | `RAW(4 \| 8)` | If all the allocations are from one heap, then this is the address of the parent heap descriptor for that heap. Otherwise, this column is null. If the heap has no parent, the value is zero. |
| `MOST_RECENT` | `NUMBER` | Oracle process identifier (`PID`) for most recent snapshot |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |