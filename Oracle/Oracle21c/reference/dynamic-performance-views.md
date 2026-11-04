---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/dynamic-performance-views.html
tags:
  - oracle
  - 21c
  - reference
---

## Part III Dynamic Performance Views

This part describes the dynamic performance views, which are often referred to as `V$` views.

This part contains the following chapters:

- [Dynamic Performance (V$) Views: V$ACCESS to V$HVMASTER\_INFO](dynamic-performance-v-views-1.md)
- [Dynamic Performance (V$) Views: V$IM\_COLUMN\_LEVEL to V$RULE\_SET\_AGGREGATE\_STATS](dynamic-performance-v-views-2.md)
- [Dynamic Performance (V$) Views: V$SCHEDULER\_RUNNING\_JOBS to V$ZONEMAP\_USAGE\_STATS](dynamic-performance-v-views-3.md)

Note:

Oracle also maintains tables and views that change only when a change is made to the data dictionary. These static tables and views are described in [Static Data Dictionary Views](static-data-dictionary-views.md).

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.