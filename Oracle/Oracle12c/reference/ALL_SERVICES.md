---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SERVICES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SERVICES` displays all services in the database. The view excludes rows marked for deletion.

Related View

`DBA_SERVICES` displays all services in the database. The view excludes rows marked for deletion.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SERVICE_ID` | `NUMBER` |  | Unique ID for the service |
| `NAME` | `VARCHAR2(64)` |  | Name describing the workload |
| `NAME_HASH` | `NUMBER` |  | Hash of the short name for the service |
| `NETWORK_NAME` | `VARCHAR2(512)` |  | Network name used to connect to the service |
| `CREATION_DATE` | `DATE` |  | Date the service was created |
| `CREATION_DATE_HASH` | `NUMBER` |  | Hash of the creation date |
| `FAILOVER_METHOD` | `VARCHAR2(64)` |  | TAF only for compatibility - `BASIC` or `NONE` |
| `FAILOVER_TYPE` | `VARCHAR2(64)` |  | For Application Continuity for Java, `TRANSACTION`. For TAF, `SESSION` or `SELECT`. |
| `FAILOVER_RETRIES` | `NUMBER(10)` |  | For Application Continuity and TAF, when reconnecting after a failure, number of attempts to re-connect per incident |
| `FAILOVER_DELAY` | `NUMBER(10)` |  | For Application Continuity and TAF, when reconnecting after a failure, delay between each connection retry (in seconds) |
| `MIN_CARDINALITY` | `NUMBER` |  | Reserved for internal use |
| `MAX_CARDINALITY` | `NUMBER` |  | Reserved for internal use |
| `GOAL` | `VARCHAR2(12)` |  | Runtime Load Balancing Goal being used to create run-time load balancing and connection load balancing advice:  - `NONE` - `SERVICE_TIME` - Connections are balanced by response time - `THROUGHPUT` - Connections are balanced by throughput |
| `DTP` | `VARCHAR2(1)` |  | DTP (distributed transaction processing) enforces all sessions for a service at one instance. This is a requirement for XA before 11g, and is a requirement if resuming and suspending the same XA branch. |
| `ENABLED` | `VARCHAR2(3)` |  | Reserved for internal use |
| `AQ_HA_NOTIFICATIONS` | `VARCHAR2(3)` |  | To enable FAN for OCI connections, set AQ HA Notifications to `True`. For Oracle Database 12c, FAN uses ONS (Oracle Notification Service) |
| `CLB_GOAL` | `VARCHAR2(5)` |  | Connection load balancing goal. When using run-time load balancing, `GOAL=SERVICE_TIME` or `THROUGHPUT`, set to `SHORT`. For a session count per service only, use `LONG`. |
| `EDITION` | `VARCHAR2(128)` |  | A non-NULL value specifies the initial session edition for subsequent database connections that use the service and do not specify an edition. A NULL value has no effect. |
| `COMMIT_OUTCOME` | `VARCHAR2(3)` |  | For Transaction Guard, indicates whether the database service associated with the user session has the `COMMIT_OUTCOME` service attribute enabled (`YES`) or not (`NO`). This attribute applies on a per session basis and is set at connect time.  When `COMMIT_OUTCOME` = `YES`:  - Transaction Guard manages the commit status for all supported transaction types. The outcome of a `COMMIT` transaction is known. If there is an outage, the application can use `DBMS_APP_CONT.GET_LTXID_OUTCOME` to return a reliable status for the last in-flight work. - A logical transaction ID (LTXID) is set for each user session at login and at each successful commit.  See Also: For information about preserving the commit outcome, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADFNS338). For information about logical transaction IDs, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADFNS324). |
| `RETENTION_TIMEOUT` | `NUMBER` |  | For Transaction Guard, when `COMMIT_OUTCOME` = `YES`, this value indicates the amount of time (in seconds) that the commit outcome is retained in the database. |
| `REPLAY_INITIATION_TIMEOUT` | `NUMBER` |  | For Application Continuity, indicates a time period (in seconds) after which the request will not be replayed. The time period starts at the first request submission.  The default value is 300 seconds, which is 5 minutes. |
| `SESSION_STATE_CONSISTENCY` | `VARCHAR2(128)` |  | Describes how non-transactional is changed during a request. This parameter is considered only if `failover_type` is set to `TRANSACTION` for Application Continuity. Examples of session state are NLS settings, optimizer preferences, event settings, PL/SQL global variables, temporary tables, advanced queues, LOBs and result cache. If non-transactional values change after the request starts, the default value of `DYNAMIC` should be set. Almost all applications should use `DYNAMIC` mode. If you are unsure, use `DYNAMIC` mode. |
| `GLOBAL_SERVICE` | `VARCHAR2(3)` |  | Indicates whether the service is global. A global service is managed by Global Data Services (GDS) and can be provided by multiple databases that contain replicated data. Possible values:  - `YES`: Indicates the service is global - `NO`: Indicates the service is not global  This attribute is set when using GDS. It cannot be set by a user. |
| `PDB` | `VARCHAR2(128)` |  | Name of a PDB associated with a given service. Will contain NULL for a non-CDB or if the service is not associated with a PDB (that is, connecting to a CDB using this service will cause a user to connect to the root.)  When managing services for a PDB, use SRVCTL for Oracle RAC and Oracle RAC One Node databases, or connect to that PDB if it is a single instance (not RAC). The PDB attribute shows which PDB has the service. It cannot be set or modified explicitly. |
| `SQL_TRANSLATION_PROFILE` | `VARCHAR2(261)` |  | A non-NULL value specifies the initial SQL translation profile for subsequent database connections that use the service and do not specify a SQL translation profile. A NULL value has no effect. |
| `MAX_LAG_TIME` | `VARCHAR2(128)` |  | The maximum replication lag (in seconds) that is acceptable for a data replica to be used for providing the database service. Can only be specified for global services using the Global Data Services (GDS) interfaces. It is not supported to change this value at local databases. |
| `GSM_FLAGS` | `NUMBER` |  | Flags specific to Global Data Services (GDS). Can only be specified for global services using the GDS interfaces. It is not supported to change these values at local databases. |
| `PQ_SVC` | `VARCHAR2(64)` |  | Name of the associated parallel query rim service  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `STOP_OPTION` | `VARCHAR2(13)` |  | Stop option for sessions of this service for planned maintenance  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `FAILOVER_RESTORE` | `VARCHAR2(6)` |  | Indicates whether sessions recover their commonly used session state (like NLS, schema) when they are failed over with TAF  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `DRAIN_TIMEOUT` | `NUMBER` |  | Number of seconds to wait for sessions to be drained  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_SERVICES](DBA_SERVICES.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ARPLS73456) for more information about the `DBMS_APP_CONT.GET_LTXID_OUTCOME` procedure