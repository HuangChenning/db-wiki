---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-KEY_VECTOR.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.26 V$KEY\_VECTOR

`V$KEY_VECTOR` provides debugging information related to the data structures used by in-memory aggregation for current and recent queries using key vectors.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Session ID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `TRANSLATE_ID` | `NUMBER` | Translation vector ID |
| `SQL_ID` | `VARCHAR2(13)` | SQL ID that uses the translation vector |
| `SQL_EXEC_START` | `DATE` | Time when the execution of the SQL started |
| `SQL_EXEC_ID` | `NUMBER` | SQL execution identifier |
| `PROCESS` | `VARCHAR2(64)` | Operating system client process ID |
| `STATE` | `VARCHAR2(9)` | State of the in-memory aggregation operation:  - `BYPASS` 	Refers to key vectors that are currently in use by queries that have undergone the vector transform. - `BYPASSED` 	This is a historical entry for key vectors whose queries have already finished. - `FINISHED` 	This is a historical entry for key vectors whose queries have already finished. - `RUNNING` 	Refers to key vectors that are currently in use by queries that have undergone the vector transform.  One query will probably have multiple key vectors if it has gone through the vector transform.  Also, if the query is operating in parallel, there may be multiple entries per PQ worker.  The `PROCESS` column can be joined to `V$SESSION` to differentiate these cases. |
| `TYPE` | `VARCHAR2(9)` | Type of translation vector created:  - `DOUBLEIND` - `PAGED` - `SIMPLE` - `INDIRECT` - `HASH` - `OFFSET` |
| `WIDTH` | `NUMBER` | Width (number of bits) of DOUBLEIND, SIMPLE, INDIRECT, or OFFSETvector translation array:  - 1 - 4 - 8 - 16 - 32 |
| `KEY_DATA_TYPE` | `VARCHAR2(13)` | The internal join column key data type of either DOUBLEIND, SIMPLE, INDIRECT, or OFFSET translation vectors:  - `BINARY` - `BINARY_FLOAT` - `NUMBER` - `PACKED_BINARY` - `PACKED_DATE` - `PACKED_NUMBER`  Also, a value of `NULL` is displayed for HASH translation vectors with non-numeric data types and for HASH translation vectors with more than one join key column. |
| `JOIN_COLUMN_COUNT` | `NUMBER` | Number of join columns. `PAGED` and `HASHED` are the only types which can have greater than one join column. |
| `JOIN_KEY_COUNT` | `NUMBER` | Number of join key values used to build translation vector |
| `DUP_JOIN_KEY_COUNT` | `NUMBER` | Indicates the number of key values in the key vector that have more than one parent value |
| `MIN_JOIN_KEY` | `NUMBER` | Min join key value in translation vector |
| `MAX_JOIN_KEY` | `NUMBER` | Max join key value in translation vector |
| `GROUP_KEY_COUNT` | `NUMBER` | Max dense grouping key value. This value is computed while the data that creates the translation vector is processed. |
| `FILTERED` | `NUMBER` | Number of rows filtered by translation vector |
| `PROBED` | `NUMBER` | Number of rows that probed the translation vector in key vector use row source |
| `ACTIVE` | `NUMBER` | Number of active translation vectors used as filters across all workers |
| `DISABLED` | `NUMBER` | Number of translation vector filters across all workers that were disabled |
| `MEMORY_ALLOCATED` | `NUMBER` | Amount of memory allocated for the key vector |
| `JOIN_STRUCTURE_SIZE` | `NUMBER` | Amount of memory used out of the allocated space |
| `FACT_OWNER` | `VARCHAR2(128)` | The owner of the fact table. Null when the fact table is null. |
| `FACT_NAME` | `VARCHAR2(128)` | The table that contains measure data. May be null if more than one fact table is used in the query. |
| `DIMENSION_OWNER` | `VARCHAR2(128)` | When a single table is used to construct the key vector, the table owner will appear in this column. If multiple tables are joined to serve as the dimension (more of a snowflake than a star schema shape, for one example), then this column will be null. |
| `DIMENSION_NAME` | `VARCHAR2(128)` | The table that contains attribute data and is joined to the fact table. May be null if two or more tables are used (for example, snowflake style dimension tables). |
| `CREATION_DURATION` | `NUMBER` | Records the total time in seconds that it took to create the key vector |
| `PAYLOAD_COLUMN_COUNT` | `NUMBER` | The number of columns being carried from the dimension table to the fact table scan for processing without joinback |
| `OFFLOADED` | `VARCHAR2(10)` | Indicates whether and how the key vector has been sent to an Exadata cell. Possible values:  - `NO`: The key vector has not been sent to an Exadata cell. - `YES`: The key vector was fully sent to an Exadata cell. - `COMPRESSED`: The key vector was fully sent to an Exadata cell and was compressed. - `EFILTER`: The key vector could not be sent to an Exadata cell due to the size of another constraint. Instead, a bloom filter-like data structure was sent to aid filtration. |
| `COMPRESSED_SIZE` | `NUMBER` | If the value of `OFFLOADED` is `COMPRESSED`, then this column displays the compressed size of metadata transmitted to the Exadata cell (in bytes) |
| `EFILTER_SIZE` | `NUMBER` | If the value of `OFFLOADED` is `EFILTER`, then this column displays the size of the data structure sent to the Exadata cell (in bytes) |

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL-GUID-91434A26-E81E-4609-800B-4E179A63EDBC) for more information about in-memory aggregation