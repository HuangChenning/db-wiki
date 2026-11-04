---
title: "V$LOGMNR_LATCH"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2038.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGMNR_LATCH` can be joined with the `V$LATCH` and the `V$LATCH_CHILDREN` views to obtain statistics about different latches used by active LogMiner persistent sessions. A persistent LogMiner session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating a Streams capture.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Unique identifier of the LogMiner persistent session |
| `NAME` | `VARCHAR2(32)` | Name of the Latch: - `LogMiner internal state` - Identifies the latch that protects communications between the LogMiner `READER`, `PREPARER`, and `BUILDER` processes - `LogMiner memory allocation` - Identifies the latch that protects all memory allocation and deallocation inside LogMiner - `LogMiner transaction list` - Identifies the latch that protects interaction between the LogMiner layer and its clients (Data Guard SQL Apply on a logical standby database or Oracle Streams) |
| `CHILD_ADDR` | `RAW(4)` | Address of the child latch object. This column matches the corresponding `ADDR` column in the `V$LATCH_CHLDREN` view |
| `STATE` | `VARCHAR2(6)` | State of the Latch: - `UNINIT` - The latch structure is uninitialized; that is, it is not currently assigned to any LogMiner persistent session - `READY` - The latch structure is being used by a persistent LogMiner session |