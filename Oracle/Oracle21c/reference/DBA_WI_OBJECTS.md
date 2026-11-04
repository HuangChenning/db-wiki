---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WI_OBJECTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.110 DBA\_WI\_OBJECTS

Each row in `DBA_WI_OBJECTS` represents a database object (table) that is accessed by the given template in the given Workload Intelligence job.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload of which the given object has been accessed |
| `TEMPLATE_ID` | `NUMBER` | `NOT NULL` | The identifier of the template in the given job by which the current object has been accessed |
| `OBJECT_ID` | `NUMBER` | `NOT NULL` | The identifier of the current object |
| `ACCESS_TYPE` | `VARCHAR2(2)` | `NOT NULL` | Possible values:  - `R` - Indicates that the current object has been accessed for reading by the given template - `W` - Indicates that the current object has been accessed for writing by the given template - `RW` - Indicates that the current object has been accessed for both reading and writing by the given template |