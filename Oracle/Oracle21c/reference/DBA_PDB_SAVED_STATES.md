---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PDB_SAVED_STATES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.237 DBA\_PDB\_SAVED\_STATES

`DBA_PDB_SAVED_STATES` shows information about the current saved PDB states in the CDB.

This view is a data link, so the data is also available within the PDB.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CON_ID` | `NUMBER` | `NOT NULL` | The ID of the PDB |
| `CON_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the PDB |
| `INSTANCE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the instance for which the state is saved |
| `CON_UID` | `NUMBER` | `NOT NULL` | Unique ID assigned to the PDB at creation time |
| `GUID` | `RAW(16)` |  | Globally unique immutable ID assigned to the PDB at creation time |
| `STATE` | `VARCHAR2(14)` |  | Open state of the PDB |
| `RESTRICTED` | `VARCHAR2(3)` |  | Restricted mode of the PDB |

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF55667) for more information about preserving a PDB's open mode across an instance restart