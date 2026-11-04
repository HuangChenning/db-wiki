---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RMAN_OUTPUT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.181 V$RMAN\_OUTPUT

This is an in-memory view and is not recorded in the controlfile. The view can hold 32768 rows.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID of the session which is running this RMAN operation |
| `RECID` | `NUMBER` | Record ID of the corresponding `V$RMAN_STATUS` row |
| `STAMP` | `NUMBER` | Timestamp of the corresponding `V$RMAN_STATUS` row |
| `SESSION_RECID` | `NUMBER` | Record ID of the session (corresponding `V$RMAN_STATUS` row with `ROW_LEVEL` = `0`) |
| `SESSION_STAMP` | `NUMBER` | Timestamp of the session (corresponding `V$RMAN_STATUS` row with `ROW_LEVEL` = `0`) |
| `OUTPUT` | `VARCHAR2(130)` | Output text reported by RMAN |
| `RMAN_STATUS_RECID` | `NUMBER` | Owning `V$RMAN_STATUS` record ID |
| `RMAN_STATUS_STAMP` | `NUMBER` | Owning `V$RMAN_STATUS` record stamp |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `GUID` | `NUMBER` | The guid of the pluggable database (PDB) that did the RMAN operation. `V$RMAN_OUTPUT` captures the rman output.  If a PDB sysdba did the backup, the guid of the PDB is displayed in `V$RMAN_OUTPUT`. If root did the backup, then guid of the root is displayed in `V$RMAN_OUTPUT`. Root  A root user can see all of `V$RMAN_OUTPUT` rows (that is, the rows owned by all PDBs), but a PDB user can only see that PDB’s `V$RMAN_OUTPUT` rows (that is, no rows from root or other PDBs). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |