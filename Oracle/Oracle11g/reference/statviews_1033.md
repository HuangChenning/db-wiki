---
title: ALL_CHANGE_PROPAGATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1033.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CHANGE_PROPAGATIONS` displays information about Change Data Capture propagations.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROPAGATION_SOURCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change source |
| `PROPAGATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the propagation |
| `STAGING_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Name of the staging database for the propagation |
| `DESTINATION_QUEUE_PUBLISHER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the destination queue |
| `DESTINATION_QUEUE` | `VARCHAR2(30)` | `NOT NULL` | Name of the destination queue |