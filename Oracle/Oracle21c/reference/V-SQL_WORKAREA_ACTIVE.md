---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_WORKAREA_ACTIVE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.69 V$SQL\_WORKAREA\_ACTIVE

`V$SQL_WORKAREA_ACTIVE` contains an instantaneous view of the work areas currently allocated by the system. You can join this view against `V$SQL_WORKAREA` on `WORKAREA_ADDRESS` to access the definition of that work area. If a work area spills to disk, then this view contains information for the temporary segment created on behalf of this work area.

The last three columns are included to enable joining `V$SQL_WORKAREA_ACTIVE` with `V$TEMPSEG_USAGE` to retrieve more information on this temporary segment.

You can use this view to answer the following:

- What are the top 10 largest work areas currently allocated in the system?
- What percentage of memory is over-allocated (`EXPECTED_SIZE` `<` `ACTUAL_MEM_USED`) and under-allocated (`EXPECTED_SIZE` `>` `ACTUAL_MEM_USED`)?
- What are the active work areas using more memory than what is expected by the memory manager?
- What are the active work areas that have spilled to disk?

| Column | Datatype | Description |
| --- | --- | --- |
| `SQL_HASH_VALUE` | `NUMBER` | Hash value of the SQL statement that is currently being executed |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier of the SQL statement that is currently being executed |
| `SQL_EXEC_START` | `DATE` | Time when the execution of the SQL currently executed by this session started |
| `SQL_EXEC_ID` | `NUMBER` | SQL execution identifier (see `V$SQL_MONITOR`) |
| `WORKAREA_ADDRESS` | `RAW(4 \| 8)` | Address of the work area handle. This is the primary key for the view. |
| `OPERATION_TYPE` | `VARCHAR2(160)` | Type of operation using the work area. Can include values such as `SORT`, `HASH JOIN`, `GROUP BY`, `BUFFER`, `BITMAP MERGE`, and `BITMAP CONSTRUCTION`. |
| `OPERATION_ID` | `NUMBER` | A unique number used to identify the operation in the execution plan. This identifier can be joined to `V$SQL_PLAN` to locate the operation that uses this work area. |
| `POLICY` | `VARCHAR2(24)` | Sizing policy for this work area (`MANUAL` or `AUTO`) |
| `SID` | `NUMBER` | Session identifier |
| `QCINST_ID` | `NUMBER` | Query coordinator instance identifier. Along with `QCSID`, enables you to uniquely identify the query coordinator. |
| `QCSID` | `NUMBER` | Query coordinator session identifier. This is the same as the SID if the work area is allocated by a serial cursor. |
| `ACTIVE_TIME` | `NUMBER` | Average time this work area is active (in microseconds) |
| `WORK_AREA_SIZE` | `NUMBER` | Maximum size (in bytes) of the work area as it is currently used by the operation |
| `EXPECTED_SIZE` | `NUMBER` | Expected size (in bytes) for this work area. `EXPECTED_SIZE` is set on behalf of the operation by the memory manager. Memory can be over-allocated when `WORK_AREA_SIZE` has a higher value than `EXPECTED_SIZE`. This can occur when the operation using this work area takes a long time to resize it. |
| `ACTUAL_MEM_USED` | `NUMBER` | Amount of PGA memory (in bytes) currently allocated on behalf of this work area. This value should range between `0` and `WORK_AREA_SIZE`. |
| `MAX_MEM_USED` | `NUMBER` | Maximum memory amount (in bytes) used by this work area |
| `NUMBER_PASSES` | `NUMBER` | Number of passes corresponding to this work area (`0` if running in `OPTIMAL` mode) |
| `TEMPSEG_SIZE` | `NUMBER` | Size (in bytes) of the temporary segment used on behalf of this work area. This column is NULL if this work area has not (yet) spilled to disk. |
| `TABLESPACE` | `VARCHAR2(128)` | Tablespace name for the temporary segment created on behalf of this work area. This column is NULL if this work area has not (yet) spilled to disk. |
| `SEGRFNO#` | `NUMBER` | Relative file number within the tablespace for the temporary segment created on behalf of this work area. This column is NULL if this work area has not (yet) spilled to disk. |
| `SEGBLK#` | `NUMBER` | Block number for the temporary segment created on behalf of this work area. This column is NULL if this work area has not (yet) spilled to disk. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$SQL\_WORKAREA](V-SQL_WORKAREA.md) "
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT007) for more information about SQL work areas