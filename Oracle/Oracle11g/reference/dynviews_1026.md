---
title: "V$ASM_DISK_STAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1026.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_DISK_STAT` displays performance statistics in the same way that `V$ASM_DISK` does, but without performing discovery of new disks. This results in a less expensive operation. However, since discovery is not performed, the output of this view does not include any data about disks that are new to the system.

The columns for `V$ASM_DISK_STAT` are the same as those for `V$ASM_DISK`.

See Also:

["V$ASM\_DISK"](dynviews_1024.md)