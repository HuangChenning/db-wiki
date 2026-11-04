---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/static-data-dictionary-views.html
tags:
  - oracle
  - 21c
  - reference
---

## Part II Static Data Dictionary Views

This part describes data dictionary tables and views. These tables and views are called static, because they change only when a change is made to the data dictionary (for example, when a new table is created or when a user is granted new privileges).

This part contains the following chapters:

- [Static Data Dictionary Views: ALL\_ALL\_TABLES to ALL\_OUTLINES](static-data-dictionary-views-1.md)
- [Static Data Dictionary Views: ALL\_PART\_COL\_STATISTICS to DATABASE\_PROPERTIES](static-data-dictionary-views-2.md)
- [Static Data Dictionary Views: DBA\_2PC\_NEIGHBORS to DBA\_HIST\_JAVA\_POOL\_ADVICE](static-data-dictionary-views-3.md)
- [Static Data Dictionary Views: DBA\_HIST\_LATCH to DBA\_STORED\_SETTINGS](static-data-dictionary-views-4.md)
- [Static Data Dictionary Views: DBA\_STREAMS\_ADD\_COLUMN to USER\_ZONEMAPS](static-data-dictionary-views-5.md)

Note:

Oracle also maintains views that monitor ongoing database activity. These dynamic performance views are described in [Dynamic Performance Views](dynamic-performance-views.md).

Note:

A multitenant container database is the only supported architecture in Oracle Database 21c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.