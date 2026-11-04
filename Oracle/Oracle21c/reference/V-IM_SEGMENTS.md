---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IM_SEGMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.2 V$IM\_SEGMENTS

`V$IM_SEGMENTS` presents information about all the in-memory segments in the database.

Only segments that have an in-memory representation are displayed. If a segment is marked for the In-Memory Column Store (IM column store) but is not populated, no corresponding row for that segment is displayed in this view.

| Column | Datatype | Description |
| --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | User name of the segment owner |
| `SEGMENT_NAME` | `VARCHAR2(128)` | Name of the segment, if any |
| `PARTITION_NAME` | `VARCHAR2(128)` | Object partition name (set to NULL for non-partitioned objects) |
| `SEGMENT_TYPE` | `VARCHAR2(18)` | Type of segment:  - `TABLE` - `TABLE PARTITION` - `TABLE SUBPARTION` |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Name of the tablespace containing the segment |
| `INMEMORY_SIZE` | `NUMBER` | Size of the in-memory version of the segment, in bytes |
| `BYTES` | `NUMBER` | Number of on-disk data bytes for the segment that could be represented in memory (no space metadata blocks) |
| `BYTES_NOT_POPULATED` | `NUMBER` | Size of the portion of the on-disk segment that is not populated in memory, in bytes. |
| `POPULATE_STATUS` | `VARCHAR2(13)` | Status of segment population:  - `STARTED`: A populate task for the segment has started - `COMPLETED`: There are no populate tasks pending for the segment - `OUT` `OF` `MEMORY`: A populate task for the segment failed due to lack of space in the IM column store |
| `INMEMORY_PRIORITY` | `VARCHAR2(8)` | Indicates the priority for IM column store population:  - `LOW` - `MEDIUM` - `HIGH` - `CRITICAL` - `NONE` |
| `INMEMORY_DISTRIBUTE` | `VARCHAR2(15)` | Indicates how the IM column store is distributed in an Oracle Real Application Clusters (Oracle RAC) environment:  - `AUTO` - `BY ROWID RANGE` - `BY PARTITION` - `BY SUBPARTITION` |
| `INMEMORY_DUPLICATE` | `VARCHAR2(13)` | Indicates the duplicate setting for the IM column store in an Oracle RAC environment:  - `NO DUPLICATE` - `DUPLICATE` - `DUPLICATE ALL` |
| `INMEMORY_COMPRESSION` | `VARCHAR2(17)` | Compression level for the IM column store:  - `NO MEMCOMPRESS` - `FOR DML` - `FOR QUERY [ LOW \| HIGH ]` - `FOR CAPACITY [ LOW \| HIGH ]` - `AUTO` |
| `INMEMORY_SERVICE` | `VARCHAR2(12)` | Specifies how the IM-enabled table is populated on various instances:  - `DEFAULT`: Pre-Oracle Database 12c Release 2 (12.2.0.1) behavior - `NONE`: Do not populate on any instance - `ALL`: Populate on all instances - `USER_DEFINED`: Populate only on the instances on which the user-specified service is active. The service name corresponding to this is stored in the `INMEMORY_SERVICE_NAME` column. |
| `INMEMORY_SERVICE_NAME` | `VARCHAR2(129)` | Specifies the service name on which the IM-enabled table should be populated. This column has a value only when the corresponding `INMEMORY_SERVICE` column has a value of `USER_DEFINED`. |
| `IS_EXTERNAL` | `VARCHAR2(5)` | Indicates whether the IM segment is for an external table. Possible values:  - `TRUE`: The IM segment is for an external table. - `FALSE`: The IM segment is not for an external table. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |