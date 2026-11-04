---
title: DBA_SUBSCRIPTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5036.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SUBSCRIPTIONS` describes all subscriptions in the database. This view is intended for use by Change Data Capture publishers.

Related View

`USER_SUBSCRIPTIONS` describes the subscriptions created by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLE` | `NUMBER` | `NOT NULL` | Subscription handle |
| `SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Change set name |
| `USERNAME` | `VARCHAR2(30)` | `NOT NULL` | User name of the subscriber |
| `CREATED` | `DATE` | `NOT NULL` | Subscription creation date |
| `STATUS` | `VARCHAR2(1)` | `NOT NULL` | Status of the subscriptions: |
| `EARLIEST_SCN` | `NUMBER` | `NOT NULL` | Subscription window low boundary |
| `LATEST_SCN` | `NUMBER` | `NOT NULL` | Subscription window high boundary |
| `DESCRIPTION` | `VARCHAR2(255)` |  | Comment field for the subscriber |
| `LAST_PURGED` | `DATE` |  | Last time the subscriber called the `PURGE_WINDOW` for this subscription |
| `LAST_EXTENDED` | `DATE` |  | Last time the subscriber called the `EXTEND_WINDOW` for this subscription |
| `SUBSCRIPTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the subscription |

See Also:

["USER\_SUBSCRIPTIONS"](statviews_5471.md)