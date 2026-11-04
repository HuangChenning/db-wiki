---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/dba_hist_-views.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.5 DBA\_HIST\_\* Views

The DBA\_HIST views show the local Automatic Workload Repository (AWR) data present on a CDB root or a PDB.

If a DBA\_HIST view is queried from a CDB root, the view shows all the AWR data stored on the CDB root.

If a DBA\_HIST view is queried from a PDB, the view shows the subset of the CDB root AWR data that is specific to that PDB. Also, the view shows the PDB level snapshots at that PDB, if they exist.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-CE73D449-0EE9-4022-B1F1-AA12F0955C03) for an introduction to AWR
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGDBA-GUID-4188466A-1206-4945-812B-A4A830DA61BC) for an introduction to Oracle Database views for accessing AWR data stored on the CDB root and individual PDBs in a multitenant environment