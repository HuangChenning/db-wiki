---
title: "V$HVMASTER_INFO"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1182.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HVMASTER_INFO` describes the current and previous master instances and the number of re-masterings of Global Enqueue Service resources.

| Column | Datatype | Description |
| --- | --- | --- |
| `HV_ID` | `NUMBER` | Hash value ID |
| `CURRENT_MASTER` | `NUMBER` | Master instance of this hash value ID |
| `PREVIOUS_MASTER` | `NUMBER` | Previous master instance of this hash value ID |
| `REMASTER_CNT` | `NUMBER` | Number of times this has been remastered |