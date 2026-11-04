---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DIAG_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.177 V$DIAG\_INFO

`V$DIAG_INFO` describes the state of Automatic Diagnostic Repository (ADR) functionality using `NAME=VALUE` pairs.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | Instance ID |
| `NAME` | `VARCHAR2(64)` | Identifies a piece of data that reflects the state of ADR, such as whether it is enabled, where the directories and files are located, and how many ongoing issues (incidents and problems) there are.  Possible values include:  - `Diag Enabled`: Indicates whether ADR is enabled or not - `ADR Base` through `Health Monitor`: Display different directories (ADR base, ADR home, and then subdirectories within the ADR home) - `Default Trace File`: Specifies the current default trace file for the current process - `Active Problem Count` and `Active Incident Count`: Specify how many problems/incidents there are in this ADR that either happened in the last 24 hours or have a piece of metadata set indicating that it is a persistent error (like a disk corruption) |
| `VALUE` | `VARCHAR2(512)` | Describes the current state of the piece of data identified in the `NAME` column |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |