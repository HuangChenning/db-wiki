---
title: "V$WAIT_CHAINS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3122.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$WAIT_CHAINS` displays information about blocked sessions. A wait chain is comprised of sessions that are blocked by one another. Each row represents a blocked and blocker session pair. If a wait chain is not a cyclical wait chain, then the last row for the chain does not have a blocker.

| Column | Datatype | Description |
| --- | --- | --- |
| `CHAIN_ID` | `NUMBER` | A number identifying the wait chain |
| `CHAIN_IS_CYCLE` | `VARCHAR2(5)` | Indicates whether the final blocked session in the wait chain is blocked by the initial blocked session (`TRUE`) or not (`FALSE`) |
| `CHAIN_SIGNATURE` | `VARCHAR2(801)` | An Oracle-specific text signature of the wait chain. This signature can be used to identify similar wait chains. |
| `CHAIN_SIGNATURE_HASH` | `NUMBER` | A numeric representation of `CHAIN_SIGNATURE` |
| `INSTANCE` | `NUMBER` | Blocked session's instance identifier |
| `OSID` | `VARCHAR2(25)` | Blocked session's operating system process identifier |
| `PID` | `NUMBER` | Blocked session's Oracle process identifier |
| `SID` | `NUMBER` | Blocked session's Oracle session identifier |
| `SESS_SERIAL#` | `NUMBER` | Blocked session's Oracle session serial number |
| `BLOCKER_IS_VALID` | `VARCHAR2(5)` | Indicates whether the blocked session has a blocker (`TRUE`) or not (`FALSE`) |
| `BLOCKER_INSTANCE` | `NUMBER` | Blocker session's instance identifier; NULL if `BLOCKER_IS_VALID` is `FALSE` |
| `BLOCKER_OSID` | `VARCHAR2(25)` | Blocker session's operating system process identifier; NULL if `BLOCKER_IS_VALID` is `FALSE` |
| `BLOCKER_PID` | `NUMBER` | Blocker session's Oracle process identifier; NULL if `BLOCKER_IS_VALID` is `FALSE` |
| `BLOCKER_SID` | `NUMBER` | Blocker session's Oracle session identifier; NULL if `BLOCKER_IS_VALID` is `FALSE` |
| `BLOCKER_SESS_SERIAL#` | `NUMBER` | Blocker session's Oracle session serial number; NULL if `BLOCKER_IS_VALID` is `FALSE` |
| `BLOCKER_CHAIN_ID` | `NUMBER` | If not NULL, then the blocker session is a member of another chain specified by this chain identifier. For the remaining wait chain information, see the wait chain with the specified `CHAIN_ID`. |
| `IN_WAIT` | `VARCHAR2(5)` | Indicates whether the blocked session is in a wait (`TRUE`) or not (`FALSE`) |
| `TIME_SINCE_LAST_WAIT_SECS` | `NUMBER` | Number of seconds since the last time the blocked session waited; NULL if `IN_WAIT` is `TRUE` |
| `WAIT_ID` | `NUMBER` | A number identifying the wait; NULL if `IN_WAIT` is `FALSE` |
| `WAIT_EVENT` | `NUMBER` | Resource or event number for which the blocked session is waiting; NULL if `IN_WAIT` is `FALSE` |
| `WAIT_EVENT_TEXT` | `VARCHAR2(64)` | Resource or event for which the blocked session is waiting; NULL if `IN_WAIT` is `FALSE` |
| `P1` | `NUMBER` | First additional wait parameter; NULL if `IN_WAIT` is `FALSE` |
| `P1_TEXT` | `VARCHAR2(64)` | Description of the first additional wait parameter; NULL if `IN_WAIT` is `FALSE` |
| `P2` | `NUMBER` | Second additional wait parameter; NULL if `IN_WAIT` is `FALSE` |
| `P2_TEXT` | `VARCHAR2(64)` | Description of the second additional wait parameter; NULL if `IN_WAIT` is `FALSE` |
| `P3` | `NUMBER` | Third additional wait parameter; NULL if `IN_WAIT` is `FALSE` |
| `P3_TEXT` | `VARCHAR2(64)` | Description of the third additional wait parameter; NULL if `IN_WAIT` is `FALSE` |
| `IN_WAIT_SECS` | `NUMBER` | Seconds the blocked session has been in the current wait; NULL if `IN_WAIT` is `FALSE` |
| `TIME_REMAINING_SECS` | `NUMBER` | Seconds remaining until the blocked session ends its wait (`-1` if the blocked session can indefinitely wait); NULL if `IN_WAIT` is `FALSE` |
| `NUM_WAITERS` | `NUMBER` | Number of sessions waiting for the blocked session |
| `ROW_WAIT_OBJ#` | `NUMBER` | Object ID for the table containing the row specified in `ROW_WAIT_ROW#`; NULL if `IN_WAIT` is `FALSE` |
| `ROW_WAIT_FILE#` | `NUMBER` | Identifier for the datafile containing the row specified in `ROW_WAIT_ROW#`; NULL if `IN_WAIT` is `FALSE`. This column is valid only if the blocked session is currently waiting for another transaction to commit and the value of `ROW_WAIT_OBJ#` is not `-1`. |
| `ROW_WAIT_BLOCK#` | `NUMBER` | Identifier for the block containing the row specified in `ROW_WAIT_ROW#`; NULL if `IN_WAIT` is `FALSE`. This column is valid only if the blocked session is currently waiting for another transaction to commit and the value of `ROW_WAIT_OBJ#` is not `-1`. |
| `ROW_WAIT_ROW#` | `NUMBER` | Current row being locked; NULL if `IN_WAIT` is `FALSE`. This column is valid only if the blocked session is currently waiting for another transaction to commit and the value of `ROW_WAIT_OBJ#` is not `-1`. |