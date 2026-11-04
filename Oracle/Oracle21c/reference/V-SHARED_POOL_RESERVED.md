---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SHARED_POOL_RESERVED.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.40 V$SHARED\_POOL\_RESERVED

`V$SHARED_POOL_RESERVED` displays statistics that help you tune the reserved pool and space within the shared pool.

| Column | Datatype | Description |
| --- | --- | --- |
| `FREE_SPACE` | `NUMBER` | Total amount of free space on the reserved list in bytes <sup>Foot 1</sup> |
| `AVG_FREE_SIZE` | `NUMBER` | Average size of the free memory on the reserved list in bytes <sup>Foot 1</sup> |
| `FREE_COUNT` | `NUMBER` | Number of free pieces of memory on the reserved list <sup>Foot 1</sup> |
| `MAX_FREE_SIZE` | `NUMBER` | Size of the largest free piece of memory on the reserved list in bytes <sup>Foot 1</sup> |
| `USED_SPACE` | `NUMBER` | Total amount of used memory on the reserved list in bytes <sup>Foot 1</sup> |
| `AVG_USED_SIZE` | `NUMBER` | Average size of the used memory on the reserved list in bytes <sup>Foot 1</sup> |
| `USED_COUNT` | `NUMBER` | Number of used pieces of memory on the reserved list <sup>Foot 1</sup> |
| `MAX_USED_SIZE` | `NUMBER` | Size of the largest used piece of memory on the reserved list in bytes <sup>Foot 1</sup> |
| `REQUESTS` | `NUMBER` | Number of times that the reserved list was searched for a free piece of memory <sup>Foot 1</sup> |
| `REQUEST_MISSES` | `NUMBER` | Number of times the reserved list did not have a free piece of memory to satisfy the request, and started flushing objects from the LRU list <sup>Foot 1</sup> |
| `LAST_MISS_SIZE` | `NUMBER` | Request size of the last request miss in bytes, when the reserved list did not have a free piece of memory to satisfy the request and started flushing objects from the LRU list <sup>Foot 1</sup> |
| `MAX_MISS_SIZE` | `NUMBER` | Request size of the largest request miss in bytes, when the reserved list did not have a free piece of memory to satisfy the request and started flushing objects from the LRU list <sup>Foot 1</sup> |
| `REQUEST_FAILURES` | `NUMBER` | Number of times that no memory was found to satisfy a request. If an internal flush (used to free up memory) does not meet a memory need, then the error `ORA-04031` occurs.<sup>Foot 2</sup> |
| `LAST_FAILURE_SIZE` | `NUMBER` | Request size of the last failed request in bytes. If an internal flush (used to free up memory) does not meet a memory need, then the error `ORA-04031` occurs.<sup>Foot 2</sup> |
| `ABORTED_REQUEST_THRESHOLD` | `NUMBER` | Minimum size of a request in bytes which signals an `ORA-04031` error without flushing objects <sup>Foot 2</sup> |
| `ABORTED_REQUESTS` | `NUMBER` | Number of requests that signalled an `ORA-04031` error without flushing objects <sup>Foot 2</sup> |
| `LAST_ABORTED_SIZE` | `NUMBER` | Last size of the request in bytes that returned an `ORA-04031` error without flushing objects from the LRU list <sup>Foot 2</sup> |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup>

These columns are valid only if the initialization parameter `SHARED_POOL_RESERVED_SIZE` is set to a valid value.

<sup>Footnote 2</sup>

These columns contain values which are valid even if `SHARED_POOL_RESERVED_SIZE` is not set.