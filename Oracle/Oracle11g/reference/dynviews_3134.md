---
title: "V$XSTREAM_MESSAGE_TRACKING"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3134.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$XSTREAM_MESSAGE_TRACKING` displays information about LCRs tracked through the stream that are processed by XStream components.

| Column | Datatype | Description |
| --- | --- | --- |
| `TRACKING_LABEL` | `VARCHAR2(30)` | User-specified tracking label |
| `TAG` | `RAW(30)` | First 30 bytes of the tag of the LCR |
| `COMPONENT_NAME` | `VARCHAR2(30)` | Name of the component that processed the LCR |
| `COMPONENT_TYPE` | `VARCHAR2(30)` | Type of the component that processed the LCR |
| `ACTION` | `VARCHAR2(50)` | Action performed on the LCR |
| `ACTION_DETAILS` | `VARCHAR2(100)` | Details of the action |
| `TIMESTAMP` | `TIMESTAMP(9) WITH TIME ZONE` | Time when the action was performed |
| `MESSAGE_CREATION_TIME` | `DATE` | Time when the message was created |
| `MESSAGE_NUMBER` | `NUMBER` | SCN of the message |
| `TRACKING_ID` | `RAW(16)` | Globally unique OID of the LCR |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(128)` | Name of the source database |
| `OBJECT_OWNER` | `VARCHAR2(30)` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(30)` | Name of the object |
| `XID` | `VARCHAR2(128)` | Transaction ID |
| `COMMAND_TYPE` | `VARCHAR2(30)` | Command type of the LCR |
| `MESSAGE_POSITION` | `RAW(64)` | Position of the message |

Note:

The `V$XSTREAM_MESSAGE_TRACKING` view is available starting with Oracle Database 11g Release 2 (11.2.0.2).