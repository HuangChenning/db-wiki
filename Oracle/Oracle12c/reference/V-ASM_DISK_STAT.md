---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_DISK_STAT.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ASM_DISK_STAT` displays performance statistics in the same way that `V$ASM_DISK` does, but without performing discovery of new disks

This results in a less expensive operation. However, since discovery is not performed, the output of this view does not include any data about disks that are new to the system.

The columns for `V$ASM_DISK_STAT` are the same as those for `V$ASM_DISK`.

See Also:

" [V$ASM\_DISK](V-ASM_DISK.md) "