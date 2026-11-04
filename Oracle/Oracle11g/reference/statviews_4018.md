---
title: DBA_HIST_PARAMETER_NAME
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4018.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_PARAMETER_NAME` displays information about the parameter names captured in the workload repository. This view is used with the `DBA_HIST_PARAMETER` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `PARAMETER_HASH` | `NUMBER` | `NOT NULL` | Parameter hash |
| `PARAMETER_NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the parameter |