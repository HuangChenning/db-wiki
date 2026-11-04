---
title: "V$HS_AGENT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1179.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HS_AGENT` displays the set of HS agents currently running on a given host. There is one row per agent process.

| Column | Datatype | Description |
| --- | --- | --- |
| `AGENT_ID` | `NUMBER` | Oracle Net session identifier used for connections to the agent (the identifier used in the `LISTENER.ORA` file) |
| `MACHINE` | `VARCHAR2(64)` | Operating system machine name |
| `PROCESS` | `VARCHAR2(9)` | Operating system process identifier of the agent |
| `PROGRAM` | `VARCHAR2(48)` | Program name of the agent |
| `OSUSER` | `VARCHAR2(30)` | Operating system user |
| `STARTTIME` | `DATE` | Starting time |
| `AGENT_TYPE` | `NUMBER` | Type of the agent |
| `FDS_CLASS_ID` | `NUMBER` | ID of the Foreign Data Store class |
| `FDS_INST_ID` | `NUMBER` | Instance name of the Foreign Data Store |