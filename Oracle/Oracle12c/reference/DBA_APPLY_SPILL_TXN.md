---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APPLY_SPILL_TXN.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_APPLY_SPILL_TXN` displays information about the transactions spilled from memory to hard disk by all apply processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APPLY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the apply process that spilled one or more transactions |
| `XIDUSN` | `NUMBER` | `NOT NULL` | Transaction ID undo segment number |
| `XIDSLT` | `NUMBER` | `NOT NULL` | Transaction ID slot number |
| `XIDSQN` | `NUMBER` | `NOT NULL` | Transaction ID sequence number |
| `PDB_ID` | `NUMBER` |  | PDB ID number  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `FIRST_SCN` | `NUMBER` | `NOT NULL` | SCN of the first message in the transaction |
| `MESSAGE_COUNT` | `NUMBER` |  | Number of messages spilled for the transaction |
| `FIRST_MESSAGE_CREATE_TIME` | `DATE` |  | Source creation time of the first message in the transaction |
| `SPILL_CREATION_TIME` | `DATE` |  | Time the first message was spilled |
| `FIRST_POSITION` | `RAW(64)` |  | Position of the first message in this transaction. This column is populated only for an XStream inbound server. |
| `TRANSACTION_ID` | `VARCHAR2(128)` |  | Transaction ID of the spilled transaction |