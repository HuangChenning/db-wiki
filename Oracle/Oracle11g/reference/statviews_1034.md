---
title: ALL_CHANGE_SETS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1034.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CHANGE_SETS` displays information about Change Data Capture change sets.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change set |
| `CHANGE_SOURCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Change source to which the change set belongs |
| `BEGIN_DATE` | `DATE` |  | Starting point for capturing change data |
| `END_DATE` | `DATE` |  | Stopping point for capturing change data |
| `BEGIN_SCN` | `NUMBER` |  | Reserved for future use |
| `END_SCN` | `NUMBER` |  | Reserved for future use |
| `FRESHNESS_DATE` | `DATE` |  | Reserved for future use |
| `FRESHNESS_SCN` | `NUMBER` |  | Reserved for future use |
| `ADVANCE_ENABLED` | `CHAR(1)` |  | Indicates whether the change set is enabled (`Y`) or disabled (`N`), or whether capture is disabled and apply is enabled (`C`) |
| `IGNORE_DDL` | `VARCHAR2(1)` |  | Reserved for future use |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the change set |
| `ROLLBACK_SEGMENT_NAME` | `VARCHAR2(30)` |  | Reserved for future use |
| `ADVANCING` | `VARCHAR2(1)` | `NOT NULL` | Reserved for future use |
| `PURGING` | `VARCHAR2(1)` | `NOT NULL` | Reserved for future use |
| `LOWEST_SCN` | `NUMBER` |  | Low watermark for change data in the change set |
| `TABLESPACE` | `VARCHAR2(30)` |  | Reserved for future use |
| `CAPTURE_ENABLED` | `VARCHAR2(1)` |  | Indicates whether capture is enabled for the change set (`Y`) or not (`N`) |
| `STOP_ON_DDL` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether the change set stops on DDL (`Y`) or not (`N`) |
| `CAPTURE_ERROR` | `CHAR(1)` |  | Indicates whether there is a capture error (`Y`) or not (`N`) |
| `CAPTURE_NAME` | `VARCHAR2(30)` |  | Name of the Streams capture process |
| `QUEUE_NAME` | `VARCHAR2(30)` |  | Name of the Streams queue |
| `QUEUE_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the Streams queue table |
| `APPLY_NAME` | `VARCHAR2(30)` |  | Name of the Streams apply process |
| `SET_DESCRIPTION` | `VARCHAR2(255)` |  | Description of the change set |
| `PUBLISHER` | `VARCHAR2(30)` |  | Publisher of the change set |
| `LOWEST_TIMESTAMP` | `DATE` |  | Timestamp of the record with the lowest SCN in the change set |
| `MAP_NAME` | `VARCHAR2(30)` |  | Name of the mapping table; maps SCN to timestamp |