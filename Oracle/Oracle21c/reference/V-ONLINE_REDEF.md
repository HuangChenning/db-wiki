---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ONLINE_REDEF.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.102 V$ONLINE\_REDEF

`V$ONLINE_REDEF` provides information about the status of currently running online redefinitions.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number, which is used to uniquely identify a session's objects |
| `REDEFINITION_ID` | `NUMBER` | Redefinition identifier |
| `TABLE_OWNER` | `VARCHAR2(129)` | Owner of the table currently being redefined. The table resides in this user's schema. |
| `ORIGINAL_TABLE_NAME` | `VARCHAR2(129)` | Name of the original table |
| `INTERIM_TABLE_NAME` | `VARCHAR2(1024)` | Interim table currently being redefined |
| `PARTITION_NAME` | `VARCHAR2(1024)` | Partition of the table currently being redefined. The table resides in this user's schema. |
| `OPERATION` | `VARCHAR2(128)` | Operations during the redefining process:  - `start_redef_table` - `sync_interim_table` - `copy_table_dependents` - `finish_redef_table` - `abort_redef_table` |
| `SUBOPERATION` | `VARCHAR2(128)` | Sub operation during the redefining process |
| `DETAILED_MESSAGE` | `VARCHAR2(1024)` | Details of operations during redefining process. This can include details such as the number of DML being processed, execution start\_time, and partition\_name |
| `PROGRESS` | `VARCHAR2(128)` | Percentage of completion of each operation |
| `REFRESH_STATEMENT_SQL_ID` | `VARCHAR2(128)` | The SQL ID for the statement in the `REFRESH_STATEMENT` column |
| `REFRESH_STATEMENT` | `VARCHAR2(4000)` | A refresh statement executed during a refresh operation in some online redefinition procedures. When refresh is a sub operation in the `SUBOPERATION` column, there will be a refresh statement in this `REFRESH_STATEMENT` column. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |