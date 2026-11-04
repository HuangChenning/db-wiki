---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_AUTOTASK_STATUS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_AUTOTASK_STATUS` displays status information for automated maintenance.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STATUS` | `VARCHAR2(8)` |  | Shows the status of automated maintenance. Possible values are:  - `ENABLED` - `DISABLED` - `ALLOWED` - `INVALID` |
| `LAST_CHANGE` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of last status change |