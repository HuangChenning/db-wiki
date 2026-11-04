---
title: "V$GCSHVMASTER_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1154.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GCSHVMASTER_INFO` describes the current and previous master instances and the number of re-masterings of Global Cache Service resources except those belonging to files mapped to a particular master.

| Column | Datatype | Description |
| --- | --- | --- |
| `HV_ID` | `NUMBER` | PCM hash value ID |
| `CURRENT_MASTER` | `NUMBER` | Master instance of this PCM hash value ID |
| `PREVIOUS_MASTER` | `NUMBER` | Previous master instance of this PCM hash value ID |
| `REMASTER_CNT` | `NUMBER` | Number of times this has been remastered |