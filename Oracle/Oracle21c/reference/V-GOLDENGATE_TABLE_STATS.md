---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GOLDENGATE_TABLE_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.271 V$GOLDENGATE\_TABLE\_STATS

`V$GOLDENGATE_TABLE_STATS` displays table statistics for all the tables used by each Oracle GoldenGate apply server.

| Column | Datatype | Description |
| --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `SERVER_ID` | `NUMBER` | Parallel apply server worker ID |
| `SOURCE_TABLE_OWNER` | `VARCHAR2(128)` | Source owner of the captured or replicated table |
| `SOURCE_TABLE_NAME` | `VARCHAR2(128)` | Source name of the captured or replicated table |
| `DESTINATION_TABLE_OWNER` | `VARCHAR2(128)` | Target owner of the captured or replicated table |
| `DESTINATION_TABLE_NAME` | `VARCHAR2(30)` | Target name of the captured or replicated table |
| `LAST_UPDATE` | `DATE` | Time of the last update of the statistics |
| `TOTAL_INSERTS` | `NUMBER` | Number of insert operations on this table processed by this apply server |
| `TOTAL_UPDATES` | `NUMBER` | Number of update operations on this table processed by this apply server |
| `TOTAL_DELETES` | `NUMBER` | Number of delete operations on this table processed by this apply server |
| `INSERT_COLLISIONS` | `NUMBER` | Number of insert collisions on this table encountered by this apply server |
| `UPDATE_COLLISIONS` | `NUMBER` | Number of update collisions on this table encountered by this apply server |
| `DELETE_COLLISIONS` | `NUMBER` | Number of delete collisions on this table encountered by this apply server |
| `REPERROR_RECORDS` | `NUMBER` | Number of change records that resulted in an error that were recorded on this table by this apply server |
| `REPERROR_IGNORES` | `NUMBER` | Number of change records that resulted in an error that were ignored on this table by this apply server |
| `WAIT_DEPENDENCIES` | `NUMBER` | Number of waits for this table due to dependency |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `CDR_INSERT_ROW_EXISTS` | `NUMBER` | Number of conflicts where an insert gets an ORA-00001 error |
| `CDR_UPDATE_ROW_EXISTS` | `NUMBER` | Number of conflicts where an update gets an ORA-26786 error |
| `CDR_UPDATE_ROW_MISSING` | `NUMBER` | Number of conflicts where an update gets an ORA-26787 error |
| `CDR_DELETE_ROW_EXISTS` | `NUMBER` | Number of conflicts where a delete gets an ORA-26786 error |
| `CDR_DELETE_ROW_MISSING` | `NUMBER` | Number of conflicts where a delete gets an ORA-26787 error |
| `CDR_SUCCESSFUL_RESOLUTIONS` | `NUMBER` | Number of successfully resolved conflicts |
| `CDR_FAILED_RESOLUTIONS` | `NUMBER` | Number of conflicts that could not be resolved due to an error during resolution |
| `LOB_OPERATIONS` | `NUMBER` | The number of LOB updates (LOB writes, LOB trims, and LOB erases) applied by the inbound server. |