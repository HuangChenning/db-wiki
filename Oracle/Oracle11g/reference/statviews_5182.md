---
title: SYS_OBJECTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5182.htm
tags:
  - oracle
  - 11g
  - reference
---

`SYS_OBJECTS` maps object IDs to object types and segment data block addresses.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(15)` |  | Type of the object |
| `OBJECT_TYPE_ID` | `NUMBER` |  | Type ID of the object |
| `SEGMENT_TYPE_ID` | `NUMBER` |  | Type of segment: `TABLE, CLUSTER, INDEX, ROLLBACK, DEFERRED ROLLBACK, TEMPORARY, CACHE` |
| `OBJECT_ID` | `NUMBER` |  | Object identifier |
| `HEADER_FILE` | `NUMBER` |  | ID of the file containing the segment header |
| `HEADER_BLOCK` | `NUMBER` |  | ID of the block containing the segment header |
| `TS_NUMBER` | `NUMBER` |  | The tablespace number |