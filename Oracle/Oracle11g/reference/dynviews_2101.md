---
title: "V$PROCESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2101.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PROCESS` displays information about the currently active processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDR` | `RAW(4 \| 8)` | Address of the process state object |
| `PID` | `NUMBER` | Oracle process identifier |
| `SPID` | `VARCHAR2(24)` | Operating system process identifier |
| `PNAME` | `VARCHAR2(5)` | Name of this process |
| `USERNAME` | `VARCHAR2(15)` | Operating system process username  Note: Any two-task user coming across the network has "-T" appended to the username. |
| `SERIAL#` | `NUMBER` | Process serial number |
| `TERMINAL` | `VARCHAR2(30)` | Operating system terminal identifier |
| `PROGRAM` | `VARCHAR2(48)` | Program in progress |
| `TRACEID` | `VARCHAR2(255)` | Trace file identifier |
| `TRACEFILE` | `VARCHAR2(513)` | Trace file name of the process |
| `BACKGROUND` | `VARCHAR2(1)` | `1` for a SYSTEM background process; NULL for foreground processes or non-SYSTEM background processes |
| `LATCHWAIT` | `VARCHAR2(8)` | Address of the latch the process is waiting for; NULL if none |
| `LATCHSPIN` | `VARCHAR2(8)` | This column is obsolete |
| `PGA_USED_MEM` | `NUMBER` | PGA memory currently used by the process (in bytes) |
| `PGA_ALLOC_MEM` | `NUMBER` | PGA memory currently allocated by the process (including free PGA memory not yet released to the operating system by the server process), in bytes |
| `PGA_FREEABLE_MEM` | `NUMBER` | Allocated PGA memory which can be freed (in bytes) |
| `PGA_MAX_MEM` | `NUMBER` | Maximum PGA memory ever allocated by the process (in bytes) |