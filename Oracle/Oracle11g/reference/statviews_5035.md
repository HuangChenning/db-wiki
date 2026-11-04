---
title: DBA_SUBSCRIBED_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5035.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SUBSCRIBED_TABLES` describes all source tables in the database to which any subscriber has subscribed. This view is intended for use by Change Data Capture publishers.

Related View

`USER_SUBSCRIBED_TABLES` describes the source tables to which the current user has subscribed.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLE` | `NUMBER` | `NOT NULL` | Subscription handle |
| `SOURCE_SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Source table owner |
| `SOURCE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Source table name |
| `VIEW_NAME` | `VARCHAR2(30)` |  | Subscriber view name |
| `CHANGE_SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Change set name |
| `SUBSCRIPTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the subscription |

See Also:

["USER\_SUBSCRIBED\_TABLES"](statviews_5470.md)