---
title: "V$ASM_USERGROUP_MEMBER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1035.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ASM_USERGROUP_MEMBER` displays the members for each ASM File Access Control group.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | ASM disk group number |
| `MEMBER_NUMBER` | `NUMBER` | Number of the user group member |
| `MEMBER_INCARNATION` | `NUMBER` | Incarnation number of the user group member |
| `USERGROUP_NUMBER` | `NUMBER` | User group number |
| `USERGROUP_INCARNATION` | `NUMBER` | Incarnation number of the user group |