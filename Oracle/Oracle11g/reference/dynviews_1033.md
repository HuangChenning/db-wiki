---
title: "V$ASM_USER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1033.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_USER` displays the effective operating system user names of connected database instances and of file owners.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | ASM disk group number |
| `USER_NUMBER` | `NUMBER` | ASM internal unique user number |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a user number in the low-order 24 bits (for efficient access to the view) |
| `INCARNATION` | `NUMBER` | Incarnation number of the user |
| `OS_ID` | `VARCHAR2(128)` | Operating system user ID |
| `OS_NAME` | `VARCHAR2(64)` | Operating system user name |