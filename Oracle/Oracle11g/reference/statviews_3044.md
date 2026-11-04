---
title: DBA_ALERT_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3044.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ALERT_HISTORY` describes a time-limited history of alerts which are no longer outstanding.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SEQUENCE_ID` | `NUMBER` | `NOT NULL` | Alert sequence number |
| `REASON_ID` | `NUMBER` |  | ID of the alert reason |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the object on which the alert was issued |
| `OBJECT_NAME` | `VARCHAR2(513)` |  | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(30)` |  | Name of the subobject |
| `OBJECT_TYPE` | `VARCHAR2(64)` |  | Object type |
| `REASON` | `VARCHAR2(4000)` |  | Reason for the alert |
| `TIME_SUGGESTED` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time when the alert was last updated |
| `CREATION_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time when the alert was first produced |
| `SUGGESTED_ACTION` | `VARCHAR2(4000)` |  | Advice of the recommended action |
| `ADVISOR_NAME` | `VARCHAR2(30)` |  | Name of the advisor to be invoked for more information |
| `METRIC_VALUE` | `NUMBER` |  | Value of the related metrics |
| `MESSAGE_TYPE` | `VARCHAR2(12)` |  | Message type: - `Notification` - `Warning` |
| `MESSAGE_GROUP` | `VARCHAR2(64)` |  | Name of the message group to which the alert belongs |
| `MESSAGE_LEVEL` | `NUMBER` |  | Severity message level (1 to 32) |
| `HOSTING_CLIENT_ID` | `VARCHAR2(64)` |  | ID of the client or security group to which the alert relates |
| `MODULE_ID` | `VARCHAR2(64)` |  | ID of the module that originated the alert |
| `PROCESS_ID` | `VARCHAR2(128)` |  | Process ID |
| `HOST_ID` | `VARCHAR2(256)` |  | DNS host name of the originating host |
| `HOST_NW_ADDR` | `VARCHAR2(256)` |  | IP or other network address of the originating host |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Originating instance name |
| `INSTANCE_NUMBER` | `NUMBER` |  | Originating instance number |
| `USER_ID` | `VARCHAR2(30)` |  | User ID |
| `EXECUTION_CONTEXT_ID` | `VARCHAR2(60)` |  | ID of the thread of execution |
| `ERROR_INSTANCE_ID` | `VARCHAR2(142)` |  | ID of an error instance plus a sequence number |
| `RESOLUTION` | `VARCHAR2(7)` |  | Resolution: |