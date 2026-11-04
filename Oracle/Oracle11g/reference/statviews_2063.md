---
title: ALL_SERVICES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2063.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SERVICES` displays all services in the database. The view excludes rows marked for deletion.

Related View

`DBA_SERVICES` displays all services in the database. The view excludes rows marked for deletion.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVICE_ID` | `NUMBER` |  | Unique ID for the service |
| `NAME` | `VARCHAR2(64)` |  | Service name for a queue |
| `NAME_HASH` | `NUMBER` |  | Hash of the short name for the service |
| `NETWORK_NAME` | `VARCHAR2(512)` |  | Network name used to connect to the service |
| `CREATION_DATE` | `DATE` |  | Date the service was created |
| `CREATION_DATE_HASH` | `NUMBER` |  | Hash of the creation date |
| `FAILOVER_METHOD` | `VARCHAR2(64)` |  | Failover method (`BASIC` or `NONE`) for the service |
| `FAILOVER_TYPE` | `VARCHAR2(64)` |  | Failover type (`SESSION` or `SELECT`) for the service |
| `FAILOVER_RETRIES` | `NUMBER(10)` |  | Number of retries when failing over the service |
| `FAILOVER_DELAY` | `NUMBER(10)` |  | Delay between retries when failing over the service |
| `MIN_CARDINALITY` | `NUMBER` |  | Reserved for internal use |
| `MAX_CARDINALITY` | `NUMBER` |  | Reserved for internal use |
| `GOAL` | `VARCHAR2(12)` |  | Service workload management goal: - `NONE` - `SERVICE_TIME` - `THROUGHPUT` |
| `DTP` | `VARCHAR2(1)` |  | Indicates whether the service is for DTP or distributed transactions including XA transactions (`Y`) or (`N`) |
| `ENABLED` | `VARCHAR2(3)` |  | Reserved for internal use |
| `AQ_HA_NOTIFICATIONS` | `VARCHAR2(3)` |  | Indicates whether AQ notifications are sent for HA events (`YES`) or not (`NO`) |
| `CLB_GOAL` | `VARCHAR2(5)` |  | Connection load balancing goal. It is used with statistics that are sent to the listeners to determine how new connections are distributed. It may be either `LONG` or `SHORT`. |
| `EDITION` <sup>Foot 1</sup> | `VARCHAR2(30)` |  | A non-NULL value specifies the initial session edition for subsequent database connections that use the service and do not specify an edition. A NULL value has no effect. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).