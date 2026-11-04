---
title: "V$LOCKED_OBJECT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2030.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOCKED_OBJECT` lists all locks acquired by every transaction on the system. It shows which sessions are holding DML locks (that is, TM-type enqueues) on what objects and in what mode.

| Column | Datatype | Description |
| --- | --- | --- |
| `XIDUSN` | `NUMBER` | Undo segment number |
| `XIDSLOT` | `NUMBER` | Slot number |
| `XIDSQN` | `NUMBER` | Sequence number |
| `OBJECT_ID` | `NUMBER` | Object ID being locked |
| `SESSION_ID` | `NUMBER` | Session ID |
| `ORACLE_USERNAME` | `VARCHAR2(30)` | Oracle user name |
| `OS_USER_NAME` | `VARCHAR2(30)` | OS user name |
| `PROCESS` | `VARCHAR2(12)` | OS process ID |
| `LOCKED_MODE` | `NUMBER` | Lock mode |