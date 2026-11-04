---
title: DBA_HIST_SERVICE_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4034.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_SERVICE_NAME` displays the names of the Services tracked by the Workload Repository. This view contains information for `V$SERVICES`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `SERVICE_NAME_HASH` | `NUMBER` | `NOT NULL` | Hash of the service name |
| `SERVICE_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the service |