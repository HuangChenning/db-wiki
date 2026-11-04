---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RMAN_BACKUP_TYPE.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view contains information used in filtering the other Enterprise Manager views when generating reports on specific backup types.

This view is used internally by Enterprise Manager.

| Column | Data Type | Description |
| --- | --- | --- |
| `WEIGHT` | `NUMBER` | Used internally by Enterprise Manager to set precedence order of different backup types in reports. |
| `INPUT_TYPE` | `VARCHAR2(13)` | Used internally by Enterprise Manager to represent possible filters used in creating various reporting screens. |