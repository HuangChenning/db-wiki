---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DIAG_INCIDENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.176 V$DIAG\_INCIDENT

`V$DIAG_INCIDENT` contains information about all incident metadata records present in the Automatic Diagnostic Repository (ADR) for the current container (PDB).

| Column | Datatype | Description |
| --- | --- | --- |
| `INCIDENT_ID` | `NUMBER` | ID for the current incident |
| `PROBLEM_ID` | `NUMBER` | ID for the problem that the incident is associated with |
| `CREATE_TIME` | `TIMESTAMP(9) WITH TIME ZONE` | Displays the date and time when the incident was created |
| `CLOSE_TIME` | `TIMESTAMP(9) WITH TIME ZONE` | Displays the date and time when the incident was closed |
| `STATUS` | `NUMBER` | Describes the current status for the incident. Possible values include:  - `1`: Incident is inflight - `2`: Incident is ready - `3`: Incident is tracked - `4`: Incident is closed - `5`: Incident data is removed - `6`: Incident has been purged - `7`: Incident is incomplete |
| `FLAGS` | `NUMBER` | For internal use only |
| `FLOOD_CONTROLLED` | `NUMBER` | Describes the flood control status for the current incident. Possible values include:  - `0`: Incident is not flood-controlled - `1`: Incident is fully flood controlled (no dumps) |
| `ERROR_FACILITY` | `VARCHAR2(12)` | Displays the error facility for the current incident |
| `ERROR_NUMBER` | `NUMBER` | Displays the error number for the current incident |
| `ERROR_ARG1` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG2` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG3` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG4` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG5` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG6` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG7` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG8` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `SIGNALLING_COMPONENT` | `VARCHAR2(66)` | Signalling component for the given incident |
| `SIGNALLING_SUBCOMPONENT` | `VARCHAR2(66)` | Signalling sub-component for the given incident |
| `SUSPECT_COMPONENT` | `VARCHAR2(66)` | Displays the suspect component for the given incident |
| `SUSPECT_SUBCOMPONENT` | `VARCHAR2(66)` | Displays the suspect sub-component for the given incident |
| `ECID` | `VARCHAR2(66)` | Execution context ID for the current incident |
| `IMPACT` | `NUMBER` | Describes the internal representation of the incident impact for the given incident |
| `ERROR_ARG9` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG10` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG11` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `ERROR_ARG12` | `VARCHAR2(66)` | Displays error-arguments associated with the given incident |
| `CON_UID` | `NUMBER` | Describes the container unique ID to which the data pertains |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |