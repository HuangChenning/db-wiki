---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/awr_root_-views.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.3 AWR\_ROOT\_\* Views

The AWR\_ROOT views show the AWR data stored only on a CDB root. In general, the AWR\_ROOT views are equivalent to the DBA\_HIST views.

When the AWR\_ROOT views are accessed from a CDB root, they show the AWR data specific to the CDB root.

When the AWR\_ROOT views are accessed from a PDB, they show the AWR data specific to that PDB.

See Also:

- " [AWR\_PDB\_\* Views](awr_pdb_-views.md) "
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-CE73D449-0EE9-4022-B1F1-AA12F0955C03) for an introduction to AWR
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-4188466A-1206-4945-812B-A4A830DA61BC) for more information about AWR\_ROOT views and related views for accessing AWR in a multitenant environment