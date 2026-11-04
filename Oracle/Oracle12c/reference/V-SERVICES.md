---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SERVICES.html
tags:
  - oracle
  - 12c
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
| `GOAL` | `VARCHAR2(12)` | Runtime Load Balancing Goal being used to create run-time load balancing and connection load balancing advice:  - `NONE` - `SERVICE_TIME` - Connections are balanced by response time - `THROUGHPUT` - Connections are balanced by throughput |
| `DTP` | `VARCHAR2(1)` | Indicates whether or not Distributed Transaction Processing is enabled for this service. When Distributed Transaction Processing is set to `Y` (YES), it means that the service is offered at exactly one instance at a time for XA affinity. Possible values:  - Y - YES - `N` - NO |
| `AQ_HA_NOTIFICATION` | `VARCHAR2(3)` | Indicates whether FAN - Fast Application Notification for OCI connections is set (`YES`) or not (`NO`) |
| `CLB_GOAL` | `VARCHAR2(5)` | Connection load balancing goal used with statistics that are sent to the listeners to determine how new connections are distributed:  - `LONG` - is using session count - `SHORT` - is using service time or throughput |
| `COMMIT_OUTCOME` | `VARCHAR2(3)` | For Transaction Guard, indicates whether the database service associated with the user session has the `COMMIT_OUTCOME` service attribute enabled (`YES`) or not (`NO`). This attribute applies on a per session basis and is set at connect time.  When `COMMIT_OUTCOME` = `YES`:  - Transaction Guard manages the commit status for all supported transaction types. The outcome of a `COMMIT` transaction is known. If there is an outage, the application can use `DBMS_APP_CONT.GET_LTXID_OUTCOME` to return a reliable status for the last in-flight work. - A logical transaction ID (LTXID) is set for each user session at login and at each successful commit.  See Also: For information about preserving the commit outcome, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADFNS338). For information about logical transaction IDs, see [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADFNS324) |
| `RETENTION_TIME` | `NUMBER` | For Transaction Guard, when `COMMIT_OUTCOME` = `YES`, this value indicates the amount of time (in seconds) that the commit outcome is retained in the database. |
| `REPLAY_INITIATION_TIMEOUT` | `NUMBER` | For Application Continuity, this option specifies the difference between the time (in seconds) of original execution of the first operation of a request and the time that the replay is ready to start after a successful reconnect. Application Continuity will not replay after the specified amount of time has passed. This option is intended to avoid the unintentional execution of a request when a system is recovered after a long period of time. The default is 5 minutes (300 seconds). |
| `SESSION_STATE_CONSISTENCY` | `VARCHAR2(128)` | Describes how non-transactional is changed during a request. This parameter is considered only if `failover_type` is set to `TRANSACTION` for Application Continuity. Examples of session state are NLS settings, optimizer preferences, event settings, PL/SQL global variables, temporary tables, advanced queues, LOBs, and result cache. If non-transactional values change after the request starts, the default value of `DYNAMIC` should be set. Almost all applications should use `DYNAMIC` mode. If you are unsure, use `DYNAMIC` mode. |
| `GLOBAL` | `VARCHAR2(3)` | Indicates whether the service is global. A global service is managed by Global Service Manager (GSM) and can be provided by multiple databases that contain replicated data. Possible values:  - `YES`: Indicates the service is global - `NO`: Indicates the service is not global |
| `PDB` | `VARCHAR2(128)` | Name of a pluggable database (PDB) associated with a given service. Will contain `NULL` if a database is a non-CDB or if the service is not associated with a PDB (that is, connecting to a CDB using this service will cause a user to connect to the root.) |
| `SQL_TRANSLATION_PROFILE` | `VARCHAR2(261)` | A non-NULL value specifies the initial SQL translation profile for subsequent database connections that use the service and do not specify a SQL translation profile. A NULL value has no effect. |
| `MAX_LAG_TIME` | `VARCHAR2(128)` | The maximum replication lag (in seconds) that is acceptable for a data replica to be used for providing the database service. Can only be specified for global services. |
| `STOP_OPTION` | `VARCHAR2(128)` | Stop option for sessions of this service for planned maintenance  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `FAILOVER_RESTORE` | `VARCHAR2(128)` | Indicates whether sessions recover their commonly used session state (like NLS, schema) when they are failed over with TAF  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `DRAIN_TIMEOUT` | `NUMBER` | Number of seconds to wait for sessions to be drained  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |