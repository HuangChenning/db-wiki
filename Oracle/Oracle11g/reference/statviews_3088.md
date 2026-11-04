---
title: DBA_AUTOTASK_OPERATION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3088.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_AUTOTASK_OPERATION` displays all automated maintenance task operations for each client.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CLIENT_NAME` | `VARCHAR2(64)` |  | Name of the client |
| `OPERATION_NAME` | `VARCHAR2(64)` |  | Name of the operation |
| `OPERATION_TAG` | `VARCHAR2(3)` |  | Tag for the operation |
| `PRIORITY_OVERRIDE` | `VARCHAR2(7)` |  | User-specified priority at which the task executes: |
| `ATTRIBUTES` | `VARCHAR2(4000)` |  | Attributes of the operation |
| `USE_RESOURCE_ESTIMATES` | `VARCHAR2(5)` |  | Indicates whether resource usage estimates are used for the operation (`TRUE`) or not (`FALSE`) |
| `STATUS` | `VARCHAR2(8)` |  | Job status: |