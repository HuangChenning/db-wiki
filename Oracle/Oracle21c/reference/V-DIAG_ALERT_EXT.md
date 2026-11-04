---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DIAG_ALERT_EXT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.174 V$DIAG\_ALERT\_EXT

`V$DIAG_ALERT_EXT` shows the contents of the XML-based alert log in the Automatic Diagnostic Repository (ADR) for the current container (PDB).

| Column | Datatype | Description |
| --- | --- | --- |
| `ORIGINATING_TIMESTAMP` | `TIMESTAMP(9) WITH TIME ZONE` | Date and time when the message was generated |
| `NORMALIZED_TIMESTAMP` | `TIMESTAMP(9) WITH TIME ZONE` | Date and time when the message originated, normalized for clock drift to the Oracle Enterprise Manager repository time |
| `ORGANIZATION_ID` | `VARCHAR2(67)` | ID of the organization that wrote the originating component, usually the domain of the organization |
| `COMPONENT_ID` | `VARCHAR2(67)` | ID of the product or component that originated the message |
| `HOST_ID` | `VARCHAR2(67)` | DNS hostname of originating host |
| `HOST_ADDRESS` | `VARCHAR2(49)` | IP of other network address of the originating host for the mesaage |
| `MESSAGE_TYPE` | `NUMBER` | Type of the message, indicating that a different type of response is required. Possible values include:  - `1`: UNKNOWN - Essentially the NULL type - `2`: INCIDENT\_ERROR - The program has encountered an error for some internal or unexpected reason, and it must be reported to Oracle Support - `3`: ERROR - An error of some kind has occurred - `4`: WARNING: An action occurred or a condition was discovered that should be reviewed and may require action - `5`: NOTIFICATION: reports a normal action or event. This could be a user action such as "logon completed" - `6`: TRACE: Output of a diagnostic trace |
| `MESSAGE_LEVEL` | `NUMBER` | Level the message belongs to. Lower level values imply higher severity for errors. Possible values include:  - `1`: `CRITICAL`: critical errors - `2`: `SEVERE`: severe errors - `8`: `IMPORTANT`: important message - `16`: `NORMAL`: normal message |
| `MESSAGE_ID` | `VARCHAR2(67)` | ID of the message |
| `MESSAGE_GROUP` | `VARCHAR2(67)` | Name of the group to which the message belongs |
| `CLIENT_ID` | `VARCHAR2(67)` | ID of the client or security group that the message relates to |
| `MODULE_ID` | `VARCHAR2(67)` | ID of the module that originated the message. This value is unique within a component. |
| `PROCESS_ID` | `VARCHAR2(35)` | ID of the process that originated the message |
| `THREAD_ID` | `VARCHAR2(67)` | ID of the thread of the process that originated the message |
| `USER_ID` | `VARCHAR2(131)` | ID of the user that originated the message |
| `INSTANCE_ID` | `VARCHAR2(67)` | For internal use only |
| `DETAILED_LOCATION` | `VARCHAR2(163)` | Absolute pathname of supplemental detail file on the originating host |
| `UPSTREAM_COMP_ID` | `VARCHAR2(103)` | ID of a component that the originating component is working with on the upstream (client) side |
| `DOWNSTREAM_COMP_ID` | `VARCHAR2(103)` | ID of a component that the originating component is working with on the downstream (server) side |
| `EXECUTION_CONTEXT_ID` | `VARCHAR2(103)` | Identifies the thread of execution that the originating component participates in |
| `EXECUTION_CONTEXT_SEQUENCE` | `NUMBER` | Execution sequence of the thread that the originating component participates in |
| `ERROR_INSTANCE_ID` | `NUMBER` | ID of the instance where error occurred |
| `ERROR_INSTANCE_SEQUENCE` | `NUMBER` | Instance sequence where error occurred |
| `MESSAGE_TEXT` | `VARCHAR2(2051)` | Fully formed and localized text of the message |
| `MESSAGE_ARGUMENTS` | `VARCHAR2(515)` | Arguments to be bound with the generic text of the message |
| `SUPPLEMENTAL_ATTRIBUTES` | `VARCHAR2(515)` | Supplemental attributes that are specific to a message. This field contains the impacts for an incident type error message. |
| `SUPPLEMENTAL_DETAILS` | `VARCHAR2(515)` | Supplemental data that is specific to a particular program and error message required to complete the diagnosis. Similar to the extra detail referred to in `DETAILED_LOCATION` but short enough to simply provide in the message itself |
| `PARTITION` | `NUMBER` | Segment number of physical file |
| `RECORD_ID` | `NUMBER` | Record number for the message (this value is same as the row number) |
| `FILENAME` | `VARCHAR2(515)` | Physical file on disk |
| `LOG_NAME` | `VARCHAR2(67)` | For internal use only |
| `PROBLEM_KEY` | `VARCHAR2(553)` | Describes the key for the current problem that the message is associated with |
| `VERSION` | `NUMBER` | ARB version number for the message |
| `CON_UID` | `NUMBER` | The unique ID of the container to which the data pertains |
| `CONTAINER_ID` | `NUMBER` | The ID of the container to which the data pertains |
| `CONTAINER_NAME` | `VARCHAR2(33)` | The name of the container to which the data pertains |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |