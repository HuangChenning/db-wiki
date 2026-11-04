---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGMNR_DICTIONARY_BUILDLOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.156 DBA\_LOGMNR\_DICTIONARY\_BUILDLOG

`DBA_LOGMNR_DICTIONARY_BUILDLOG` describes all successful LogMiner dictionary builds available for GoldenGate `REGISTER` `EXTRACT`.

When this view is queried from a PDB, it returns only LogMiner dictionary builds performed in that PDB.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(384)` |  | User-supplied name of the LogMiner dictionary build |
| `DATE_OF_BUILD` | `VARCHAR2(20)` |  | Date and time at which the LogMiner dictionary build was performed |
| `START_SCN` | `NUMBER` |  | Begin SCN of the LogMiner dictionary build operation |
| `END_SCN` | `NUMBER` |  | End SCN of the LogMiner dictionary build operation |
| `BUILD_TYPE` | `VARCHAR2(20)` |  | Internal string that identifies how the LogMiner dictionary build was initiated |
| `BUILD_OP` | `NUMBER` |  | Internal number that identifies how the LogMiner dictionary build was initiated |
| `CONTAINER_ID` | `NUMBER` |  | ID of the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) |
| `CONTAINER_UID` | `NUMBER` |  | Unique number that identifies the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) |
| `CONTAINER_NAME` | `VARCHAR2(384)` |  | Name of the container in which the LogMiner dictionary build was performed (the CDB root or a PDB) |
| `RESETLOGS_CHANGE#` | `NUMBER` |  | SCN that identifies the redo branch of the LogMiner dictionary build |

Note:

This view is available starting with Oracle Database 21c.