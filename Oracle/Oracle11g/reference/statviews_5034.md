---
title: DBA_SUBSCRIBED_COLUMNS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5034.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SUBSCRIBED_COLUMNS` describes the columns of source tables to which any subscriber has subscribed. This view is intended for use by Change Data Capture publishers.

Related View

`USER_SUBSCRIBED_COLUMNS` describes the columns of source tables to which the current user has subscribed.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `HANDLE` | `NUMBER` | `NOT NULL` | Subscription handle |
| `SOURCE_SCHEMA_NAME` | `VARCHAR2(30)` | `NOT NULL` | Source table schema identifier |
| `SOURCE_TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Source table identifier |
| `COLUMN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Source table column identifier |
| `SUBSCRIPTION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the subscription |
| `SOURCE_DB` | `VARCHAR2(128)` |  | Source database global name |

See Also:

["USER\_SUBSCRIBED\_COLUMNS"](statviews_5469.md)