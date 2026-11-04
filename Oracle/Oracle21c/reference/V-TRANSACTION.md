---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TRANSACTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.121 V$TRANSACTION

`V$TRANSACTION` lists the active transactions in the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the transaction state object |
| `XIDUSN` | `NUMBER` | Undo segment number |
| `XIDSLOT` | `NUMBER` | Slot number |
| `XIDSQN` | `NUMBER` | Sequence number |
| `UBAFIL` | `NUMBER` | Undo block address (UBA) filenum |
| `UBABLK` | `NUMBER` | UBA block number |
| `UBASQN` | `NUMBER` | UBA sequence number |
| `UBAREC` | `NUMBER` | UBA record number |
| `STATUS` | `VARCHAR2(16)` | Status |
| `START_TIME` | `VARCHAR2(20)` | Start time (wall clock) |
| `START_SCNB` | `NUMBER` | Start system change number (SCN) base |
| `START_SCNW` | `NUMBER` | Start SCN wrap |
| `START_UEXT` | `NUMBER` | Start extent number |
| `START_UBAFIL` | `NUMBER` | Start UBA file number |
| `START_UBABLK` | `NUMBER` | Start UBA block number |
| `START_UBASQN` | `NUMBER` | Start UBA sequence number |
| `START_UBAREC` | `NUMBER` | Start UBA record number |
| `SES_ADDR` | `RAW(4 \| 8)` | User session object address |
| `FLAG` | `NUMBER` | Flag |
| `SPACE` | `VARCHAR2(3)` | `YES` if a space transaction |
| `RECURSIVE` | `VARCHAR2(3)` | `YES` if a recursive transaction |
| `NOUNDO` | `VARCHAR2(3)` | `YES` if a no undo transaction |
| `PTX` | `VARCHAR2(3)` | `YES` if parallel transaction |
| `NAME` | `VARCHAR2(256)` | Name of a named transaction |
| `PRV_XIDUSN` | `NUMBER` | Previous transaction undo segment number |
| `PRV_XIDSLT` | `NUMBER` | Previous transaction slot number |
| `PRV_XIDSQN` | `NUMBER` | Previous transaction sequence number |
| `PTX_XIDUSN` | `NUMBER` | Rollback segment number of the parent XID |
| `PTX_XIDSLT` | `NUMBER` | Slot number of the parent XID |
| `PTX_XIDSQN` | `NUMBER` | Sequence number of the parent XID |
| `DSCN-B` | `NUMBER` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `DSCN_BASE`. |
| `DSCN-W` | `NUMBER` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `DSCN_WRAP`. |
| `USED_UBLK` | `NUMBER` | Number of undo blocks used |
| `USED_UREC` | `NUMBER` | Number of undo records used |
| `LOG_IO` | `NUMBER` | Logical I/O |
| `PHY_IO` | `NUMBER` | Physical I/O |
| `CR_GET` | `NUMBER` | Consistent gets |
| `CR_CHANGE` | `NUMBER` | Consistent changes |
| `START_DATE` | `DATE` | Start time (wall clock) |
| `DSCN_BASE` | `NUMBER` | Dependent SCN base |
| `DSCN_WRAP` | `NUMBER` | Dependent SCN wrap |
| `START_SCN` | `NUMBER` | Start SCN |
| `DEPENDENT_SCN` | `NUMBER` | Dependent SCN |
| `XID` | `RAW(8)` | Transaction XID |
| `PRV_XID` | `RAW(8)` | Previous transaction XID |
| `PTX_XID` | `RAW(8)` | Parent transaction XID |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |