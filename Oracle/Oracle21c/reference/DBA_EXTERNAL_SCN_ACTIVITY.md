---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_EXTERNAL_SCN_ACTIVITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.319 DBA\_EXTERNAL\_SCN\_ACTIVITY

`DBA_EXTERNAL_SCN_ACTIVITY` works in conjunction with the `DBA_DB_LINK_SOURCES` and `DBA_DB_LINKS` views to determine the source of high SCN activities.

If the SCN is increased by an inbound database link, then you can join the `DBA_EXTERNAL_SCN_ACTIVITY` view with the `DBA_DB_LINK_SOURCES` view on the `INBOUND_DB_LINK_SOURCE_ID` column to get details of the remote database where the SCN increase originated.

If the SCN is increased by an outbound database link, then the `INBOUND_DB_LINK_SOURCE_ID` column will be `NULL`, but the `OUTBOUND_DB_LINK_NAME` and `OUTBOUND_DB_LINK_OWNER` columns can be joined with the `DB_LINK` and `OWNER` columns respectively in the `DBA_DB_LINKS` view to determine the remote database that caused the SCN increase.

If neither of the above cases are true (the `INBOUND_DB_LINK_SOURCE_ID`, `OUTBOUND_DB_LINK_NAME`, and `OUTBOUND_DB_LINK_OWNER` are all `NULL`), then the SCN increase resulted from a client connection and not as a result of a database link to or from another database. You can join the `SESSION_ID` and `SESSION_SERIAL#` columns with the `SID` and `SERIAL#` columns in `V$SESSION` to get the client session details.

In a multitenant container database (CDB) environment, for every DBA\_ view, there is a corresponding CDB\_ view that contains data for all the pluggable databases (PDBs) in the CDB.

As the SCN is a property of the CDB (and not a PDB), a DBA interested in understanding large SCN jumps will likely find the `CDB_EXTERNAL_SCN_ACTIVITY` view more useful for diagnosing SCN jumps on a CDB. Querying the `CDB_EXTERNAL_SCN_ACTIVITY` view from `CDB$ROOT` ensures that external SCN jumps occurring on all PDBs are looked at and noticed. On the other hand, a query on the corresponding `DBA_EXTERNAL_SCN_ACTIVITY` view, or a query on the `CDB_EXTERNAL_SCN_ACTIVITY` view done from a PDB would only show data for that PDB (that is, details regarding any external activity that occurred on that specific PDB that resulted in large SCN jumps).

Note that the CDB\_ views would only show data from PDBs that are open at the time the query is issued. Therefore, when you are diagnosing sources of external SCN activities, Oracle recommends that you keep open any or all PDBs that might contain useful information for the diagnosis.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OPERATION_TIMESTAMP` | `TIMESTAMP(6)` | `NOT NULL` | Timestamp when SCN was received in UTC |
| `SESSION_ID` | `NUMBER` | `NOT NULL` | Session identifier of the local session that created this entry. Maps to `V$SESSION.SID` and to `V$ACTIVE_SESSION_HISTORY.SESSION_ID`. |
| `SESSION_SERIAL#` | `NUMBER` | `NOT NULL` | Session serial number of the local session that created this entry. Maps to `V$SESSION.SERIAL#` and to `V$ACTIVE_SESSION_HISTORY.SESSION_SERIAL#`. |
| `AUDIT_SESSIONID` | `NUMBER` |  | Session identifier that can be joined with `DBA_AUDIT_TRAIL.SESSIONID` or `UNIFIED_AUDIT_TRAIL.SESSIONID` (depending on which kind of auditing is enabled). Null if auditing is not enabled. |
| `USERNAME` | `VARCHAR2(128)` | `NOT NULL` | Oracle username of the user who logged into the local database. Maps to `V$SESSION.USERNAME`. |
| `INBOUND_DB_LINK_SOURCE_ID` | `NUMBER` |  | If the SCN was bumped by an inbound database link, then this is the inbound database link identified by the `DBA_DB_LINK_SOURCES.SOURCE_ID` database link.  If the SCN was not increased by an inbound database link, then this value is null. |
| `OUTBOUND_DB_LINK_NAME` | `VARCHAR2(128)` |  | If the SCN was bumped by an outbound database link, then this is the outbound database link identified by the `DBA_DB_LINKS.DB_LINK` database link.  Using this column and the `OUTBOUND_DB_LINK_OWNER` column, you can determine the source of the SCN increase for outbound links.  If the SCN was not increased by an outbound database link, then this value is null. |
| `OUTBOUND_DB_LINK_OWNER` | `VARCHAR2(128)` |  | If the SCN was bumped by an outbound database link, then this is the owner of the outbound database link identified by `DBA_DB_LINKS.OWNER`.  Using this column and the `OUTBOUND_DB_LINK_NAME` column, you can determine the source of the SCN increase for outbound links.  If the SCN was not increased by an outbound database link, then this value is null. |
| `RESULT` | `VARCHAR2(64)` | `NOT NULL` | The following SCN activities are captured:  - `REJECTED_HIGH_SCN` - SCN rejection due to unreasonable value - `REJECTED_HIGH_DELTA` - SCN rejection due to unreasonable rate of growth - `ACCEPTED` - SCN accepted with warning  Regular SCN activities which do not result in errors or warnings are not captured. SCN errors and warnings also appear in `alert.log`. |
| `EXTERNAL_SCN` | `NUMBER` | `NOT NULL` | The external SCN received from an inbound database link, an outbound database link, or a client |
| `SCN_ADJUSTMENT` | `NUMBER` | `NOT NULL` | For `ACCEPTED` SCNs in the `RESULT` column, how much the local SCN was increased.  For `REJECTED` SCNs in the `RESULT` column, the attempted SCN increase. |