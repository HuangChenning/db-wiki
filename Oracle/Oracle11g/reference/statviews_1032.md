---
title: ALL_CHANGE_PROPAGATION_SETS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1032.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CHANGE_PROPAGATION_SETS` displays information about the Change Data Capture propagated change sets.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PROPAGATION_SOURCE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the change source |
| `PROPAGATION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the propagation |
| `STAGING_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Name of the staging database for the propagation |
| `CHANGE_SET_PUBLISHER` | `VARCHAR2(30)` | `NOT NULL` | Publisher of the distributed change set |
| `CHANGE_SET_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the distributed change set |