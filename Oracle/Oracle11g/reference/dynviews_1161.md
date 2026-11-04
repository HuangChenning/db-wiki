---
title: "V$GES_RESOURCE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1161.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$GES_RESOURCE` is an Oracle Real Application Clusters view. It displays information of all resources currently known to the lock manager.

| Column | Datatype | Description |
| --- | --- | --- |
| `RESP` | `RAW(4 \| 8)` | Resource pointer |
| `RESOURCE_NAME` | `VARCHAR2(30)` | Resource name in hexadecimal for the lock |
| `ON_CONVERT_Q` | `NUMBER` | `1` if on convert queue, `0` otherwise |
| `ON_GRANT_Q` | `NUMBER` | `1` if on granted queue, `0` otherwise |
| `PERSISTENT_RES` | `NUMBER` | `1` if it is a persistent resource, `0` otherwise |
| `MASTER_NODE` | `NUMBER` | Master node ID |
| `NEXT_CVT_LEVEL` | `VARCHAR2(9)` | Next lock level to convert on global convert queue |
| `VALUE_BLK_STATE` | `VARCHAR2(32)` | State of the value block |
| `VALUE_BLK` | `VARCHAR2(64)` | First 64 bytes of the value block |