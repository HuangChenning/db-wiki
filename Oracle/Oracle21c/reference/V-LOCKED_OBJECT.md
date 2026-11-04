---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOCKED_OBJECT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.45 V$LOCKED\_OBJECT

`V$LOCKED_OBJECT` lists all locks acquired by every transaction on the system. It shows which sessions are holding DML locks (that is, TM-type enqueues) on what objects and in what mode.

| Column | Datatype | Description |
| --- | --- | --- |
| `XIDUSN` | `NUMBER` | Undo segment number |
| `XIDSLOT` | `NUMBER` | Slot number |
| `XIDSQN` | `NUMBER` | Sequence number |
| `OBJECT_ID` | `NUMBER` | Object ID being locked |
| `SESSION_ID` | `NUMBER` | Session ID |
| `ORACLE_USERNAME` | `VARCHAR2(128)` | Oracle user name |
| `OS_USER_NAME` | `VARCHAR2(128)` | Operating system user name |
| `PROCESS` | `VARCHAR2(24)` | Operating system process ID |
| `LOCKED_MODE` | `NUMBER` | Lock mode. The numeric values for this column map to these text values for the lock modes for table locks:  - `0` - NONE: lock requested but not yet obtained - `1` - NULL - `2` - ROWS\_S (SS): Row Share Lock - `3` - ROW\_X (SX): Row Exclusive Table Lock - `4` - SHARE (S): Share Table Lock - `5` - S/ROW-X (SSX): Share Row Exclusive Table Lock - `6` - Exclusive (X): Exclusive Table Lock  See Also: [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1342) for more information about lock modes for table locks |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |