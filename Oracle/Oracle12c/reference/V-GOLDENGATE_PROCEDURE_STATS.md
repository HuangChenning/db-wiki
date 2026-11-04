---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-GOLDENGATE_PROCEDURE_STATS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$GOLDENGATE_PROCEDURE_STATS` displays procedural replication statistics processed by each Oracle GoldenGate apply server.

| Column | Datatype | Description |
| --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` | Name of the apply process |
| `SERVER_ID` | `NUMBER` | Parallel apply server slave ID |
| `PROCEDURE_OWNER` | `VARCHAR2(128)` | Owner of the replicated procedure |
| `PACKAGE_NAME` | `VARCHAR2(128)` | Replicated procedure package |
| `PROCEDURE_NAME` | `VARCHAR2(128)` | Replicated procedure name |
| `LAST_UPDATE` | `DATE` | Time of the last update of the statistics |
| `TOTAL_EXECUTIONS` | `NUMBER` | Number of executions of the procedure by this apply server |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include: - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).