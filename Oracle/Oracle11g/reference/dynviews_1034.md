---
title: "V$ASM_USERGROUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1034.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_USERGROUP` displays the creator for each ASM File Access Control group.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | ASM disk group number |
| `USERGROUP_NUMBER` | `NUMBER` | Number of the user group |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a disk group number in the high-order 8 bits and a user group number in the low-order 24 bits (for efficient access to the view) |
| `INCARNATION` | `NUMBER` | Incarnation number of the user group |
| `OWNER_NUMBER` | `NUMBER` | User group owner identified by a unique number |
| `OWNER_INCARNATION` | `NUMBER` | Incarnation number of the user group owner |
| `NAME` | `VARCHAR2(64)` | User group name |