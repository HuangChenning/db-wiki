---
title: "V$RESTORE_POINT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2137.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RESTORE_POINT` displays information about restore points.

| Column | Datatype | Description |
| --- | --- | --- |
| `SCN` | `NUMBER` | Database SCN when the restore point was created |
| `DATABASE_INCARNATION#` | `NUMBER` | Database incarnation number when the restore point was created |
| `GUARANTEE_FLASHBACK_DATABASE` | `VARCHAR2(3)` | Indicates whether flashback log files will be kept to ensure a flashback to this point (`YES`) or not (`NO`) |
| `STORAGE_SIZE` | `NUMBER` | Approximate number of bytes of disk space currently tied up supporting this restore point. This will only be nonzero for guaranteed restore points. |
| `TIME` | `TIMESTAMP(9)` | Wall-clock time when the restore point was created |
| `RESTORE_POINT_TIME` | `TIMESTAMP(9)` | Time that was specified when the restore point was created. If a time was not specified, this value is NULL. |
| `PRESERVED` | `VARCHAR2(3)` | Indicates whether the restore point must be explicitly deleted (`YES`) or not (`NO`) |
| `NAME` | `VARCHAR2(128)` | Name of the restore point |