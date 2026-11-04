---
title: "V$ASM_TEMPLATE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1032.htm
tags:
  - oracle
  - 11g
  - reference
---

In an Oracle ASM instance, `V$ASM_TEMPLATE` displays one row for every template present in every disk group mounted by the Oracle ASM instance. In a database instance, `V$ASM_TEMPLATE` displays one row for every template present in every disk group mounted by the Oracle ASM instance with which the database instance communicates.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Owning disk group number (foreign key to the `V$ASM_DISKGROUP` view) |
| `ENTRY_NUMBER` | `NUMBER` | Template number (primary key) |
| `REDUNDANCY` | `VARCHAR2(6)` | Redundancy of the template: |
| `STRIPE` | `VARCHAR2(6)` | Indicates how the template is striped: |
| `SYSTEM` | `VARCHAR2(1)` | Indicates whether the template is a system template (`Y`) or not (`N`) |
| `NAME` | `VARCHAR2(30)` | Name of the template |
| `PRIMARY_REGION` | `VARCHAR2(4)` | Region used for allocating primary extents: |
| `MIRROR_REGION` | `VARCHAR2(4)` | Region for allocating mirrored extents: |