---
title: "V$SERVICES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3012.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SERVICES` displays information about the services in the database.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_ID` | `NUMBER` | Service ID |
| `NAME` | `VARCHAR2(64)` | Name of the service |
| `NAME_HASH` | `NUMBER` | Service name hash |
| `NETWORK_NAME` | `VARCHAR2(512)` | Network name |
| `CREATION_DATE` | `DATE` | Creation date |
| `CREATION_DATE_HASH` | `NUMBER` | Creation date hash |
| `GOAL` | `VARCHAR2(12)` | Service workload management goal: |
| `DTP` | `VARCHAR2(1)` | Indicates whether the service is for DTP or distributed transactions including XA transactions (`Y`) or not (`N`) |
| `AQ_HA_NOTIFICATION` | `VARCHAR2(3)` | Indicates whether AQ notifications are sent for HA events (`YES`) or not (`NO`) |
| `CLB_GOAL` | `VARCHAR2(5)` | Connection load balancing goal used with statistics that are sent to the listeners to determine how new connections are distributed: |