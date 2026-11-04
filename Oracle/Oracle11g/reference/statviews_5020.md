---
title: DBA_STREAMS_TP_COMPONENT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5020.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_TP_COMPONENT` displays information about each Oracle Streams component at each database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMPONENT_ID` | `NUMBER` | `NOT NULL` | ID of the Streams component |
| `COMPONENT_NAME` | `VARCHAR2(4000)` |  | Name of the Streams component |
| `COMPONENT_DB` | `VARCHAR2(128)` |  | Database where the Streams component resides |
| `COMPONENT_TYPE` | `VARCHAR2(20)` |  | Type of the Streams component: |
| `COMPONENT_CHANGED_TIME` | `DATE` |  | Time that the Streams component was last changed |