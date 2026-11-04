---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WI_CAPTURE_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.108 DBA\_WI\_CAPTURE\_FILES

Each row in `DBA_WI_CAPTURE_FILES` represents a capture file that belongs to the workload analyzed in the current Workload Intelligence job.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload to which the given capture file belongs |
| `FILE_ID` | `NUMBER` | `NOT NULL` | The identifier of the current capture file |
| `FILE_PATH` | `VARCHAR2(4000)` | `NOT NULL` | The path of the current capture file |