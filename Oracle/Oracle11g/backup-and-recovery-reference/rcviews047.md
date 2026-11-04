---
title: RC_RMAN_BACKUP_TYPE
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/rcviews047.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This view is used internally by Enterprise Manager.

It contains information used in filtering the other Enterprise Manager views when generating reports on specific backup types.

| Column | Data Type | Description |
| --- | --- | --- |
| `WEIGHT` | `NUMBER` | Used internally by Enterprise Manager to set precedence order of different backup types in reports. |
| `INPUT_TYPE` | `VARCHAR2(13)` | Used internally by Enterprise Manager to represent possible filters used in creating various reporting screens. |