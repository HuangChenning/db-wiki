---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ALERT_HISTORY_DETAIL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.54 DBA\_ALERT\_HISTORY\_DETAIL

`DBA_ALERT_HISTORY_DETAIL` describes a time-limited history of cleared and outstanding alerts.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEQUENCE_ID` | `NUMBER` | `NOT NULL` | Alert sequence number |
| `REASON_ID` | `NUMBER` |  | ID of the alert reason |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the object on which alert is issued |
| `OBJECT_NAME` | `VARCHAR2(513)` |  | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject (for example: partition) |
| `OBJECT_TYPE` | `VARCHAR2(64)` |  | Type of the object (for example: table, tablespace) |
| `REASON` | `VARCHAR2(4000)` |  | Reason for the alert |
| `TIME_SUGGESTED` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time when the alert was last updated |
| `CREATION_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time when the alert was first created |
| `SUGGESTED_ACTION` | `VARCHAR2(4000)` |  | Advice of the recommended action |
| `ADVISOR_NAME` | `VARCHAR2(128)` |  | Name of the advisor to be invoked for more information |
| `METRIC_VALUE` | `NUMBER` |  | Value of the related metrics |
| `MESSAGE_TYPE` | `VARCHAR2(12)` |  | Message type:  - Notification - Warning |
| `MESSAGE_GROUP` | `VARCHAR2(64)` |  | Name of the message group to which the alert belongs |
| `MESSAGE_LEVEL` | `NUMBER` |  | Severity level (1 to 32) |
| `HOSTING_CLIENT_ID` | `VARCHAR2(64)` |  | ID of the client or security group to which the alert relates |
| `MODULE_ID` | `VARCHAR2(64)` |  | ID of the module that originated the alert |
| `PROCESS_ID` | `VARCHAR2(128)` |  | Process id |
| `HOST_ID` | `VARCHAR2(256)` |  | DNS host name of the originating host |
| `HOST_NW_ADDR` | `VARCHAR2(256)` |  | IP or other network address of originating host |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Originating instance name |
| `INSTANCE_NUMBER` | `NUMBER` |  | Originating instance number |
| `USER_ID` | `VARCHAR2(128)` |  | User ID |
| `EXECUTION_CONTEXT_ID` | `VARCHAR2(128)` |  | Execution Context ID |
| `ERROR_INSTANCE_ID` | `VARCHAR2(142)` |  | ID of an error instance plus a sequence number |
| `RESOLUTION` | `VARCHAR2(11)` |  | Resolution:  - `Cleared` - `Outstanding` - `N/A` |
| `STATE_TRANSITION_NUMBER` | `NUMBER` | `NOT NULL` | Sequence number of the state transition for the alert |
| `PDB_NAME` | `VARCHAR2(128)` |  | PDB name |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |