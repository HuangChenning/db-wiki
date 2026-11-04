---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.201 DBA\_AUTOTASK\_STATUS

`DBA_AUTOTASK_STATUS` displays status information for automated maintenance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STATUS` | `VARCHAR2(8)` |  | Shows the status of automated maintenance. Possible values are:  - `ENABLED` - `DISABLED` - `ALLOWED` - `INVALID` |
| `LAST_CHANGE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of last status change |