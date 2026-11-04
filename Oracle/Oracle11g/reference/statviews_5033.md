---
title: DBA_SUBSCR_REGISTRATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5033.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SUBSCR_REGISTRATIONS` displays information about all subscription registrations in the database.

Related View

`USER_SUBSCR_REGISTRATIONS` displays information about the subscription registrations owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REG_ID` | `NUMBER` |  | Registration ID |
| `SUBSCRIPTION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the subscription registration. The subscription name is of the form `schema``.``queue` if the registration is for a single consumer queue or `schema``.``queue``:``consumer_name` if the registration is for a multi-consumer queue. |
| `LOCATION_NAME` | `VARCHAR2(256)` | `NOT NULL` | Location endpoint of the registration |
| `USER#` | `NUMBER` | `NOT NULL` | Internally generated user ID |
| `USER_CONTEXT` | `RAW(128)` |  | Context the user provided during registration of PL/SQL registrations or an internally generated context for OCI registrations |
| `CONTEXT_SIZE` | `NUMBER` |  | Size of the context |
| `NAMESPACE` | `VARCHAR2(9)` |  | Namespace of the subscription registration: - `ANONYMOUS` - `AQ` - `DBCHANGE` |
| `PRESENTATION` | `VARCHAR2(7)` |  | Presentation format of notifications: - `DEFAULT - Binary` - `XML` |
| `VERSION` | `VARCHAR2(5)` |  | Database version: - `8.1.6` - `10.2` - `11.1` |
| `STATUS` | `VARCHAR2(8)` |  | Status of the registration: - `DB REG` - Database registration - `LDAP REG` - LDAP registration |
| `ANY_CONTEXT` | `ANYDATA` |  | AnyData user context (used for Streams replication registrations) |
| `CONTEXT_TYPE` | `NUMBER` |  | Type of the user context |
| `QOSFLAGS` | `VARCHAR2(13)` |  | Quality of service of the registration: - `RELIABLE` - Reliable notifications persist across instance and database restarts - `PAYLOAD` - Payload delivery is required. It is only supported for client notification and only for RAW queues. - `PURGE_ON_NTFN` - Registration is to be purged automatically when the first notification is delivered to this registration location |
| `PAYLOAD_CALLBACK` | `VARCHAR2(4000)` |  | Any callback registered to serialize the notification payload |
| `TIMEOUT` | `TIMESTAMP(6)` |  | Registration timeout |
| `REG_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time of the registration |
| `NTFN_GROUPING_CLASS` | `VARCHAR2(4)` |  | Notification grouping class |
| `NTFN_GROUPING_VALUE` | `NUMBER` |  | Notification grouping value |
| `NTFN_GROUPING_TYPE` | `VARCHAR2(7)` |  | Notification grouping type: |
| `NTFN_GROUPING_START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Notification grouping start time |
| `NTFN_GROUPING_REPEAT_COUNT` | `VARCHAR2(40)` |  | Notification grouping repeat count, or `FOREVER` |

See Also:

["USER\_SUBSCR\_REGISTRATIONS"](statviews_5468.md)