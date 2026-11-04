---
title: "V$ASM_DISKGROUP_STAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1028.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_DISKGROUP_STAT` displays performance statistics in the same way that `V$ASM_DISKGROUP` does, but without performing discovery of new disk groups. This results in a less expensive operation. However, since discovery is not performed, the output of this view does not include any data about disk groups that are new to the system.

The columns for `V$ASM_DISKGROUP_STAT` are the same as those for `V$ASM_DISKGROUP`.

See Also:

["V$ASM\_DISKGROUP"](dynviews_1027.md)