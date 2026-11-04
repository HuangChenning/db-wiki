---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_APP_PDB_STATUS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.95 DBA\_APP\_PDB\_STATUS

`DBA_APP_PDB_STATUS` provides information about applications in all the application PDBs in the current application container. It provides this information when queried in the application root.

The view should be queried in the application root.

This view can be used to show which version of an application has been synced to which application PDBs.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CON_UID` | `NUMBER` |  | Unique ID of the PDB |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `APP_ID` | `NUMBER` |  | Id of the application |
| `APP_VERSION` | `VARCHAR2(30)` |  | Version of the application |
| `APP_STATUS` | `VARCHAR2(12)` |  | Status of the application |