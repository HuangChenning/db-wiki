---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DG_BROKER_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.172 V$DG\_BROKER\_CONFIG

`V$DG_BROKER_CONFIG` provides a summary of an Oracle Data Guard broker configuration.

This is similar to the DGMGRL CLI's `SHOW CONFIGURATION` command. It provides a view of the entire Oracle Data Guard broker configuration from any database in the configuration.

| Column | Datatype | Description |
| --- | --- | --- |
| `DATABASE` | `VARCHAR2(512)` | Database unique name |
| `CONNECT_IDENTIFIER` | `VARCHAR2(512)` | Net connect identifier used to reach the database |
| `DATAGUARD_ROLE` | `VARCHAR2(27)` | Oracle Data Guard role of the database:  - `PRIMARY` - `PHYSICAL` `STANDBY` - `LOGICAL` `STANDBY` - `SNAPSHOT` `STANDBY` - `FAR` `SYNC` `INSTANCE` - `RECOVERY` `APPLIANCE` |
| `REDO_SOURCE` | `VARCHAR(30)` | The database unique name of the redo source |
| `ENABLED` | `VARCHAR2(5)` | TRUE or FALSE to denote whether or not the database is managed by Oracle Data Guard broker |
| `STATUS` | `NUMBER` | An Oracle error number denoting the database's current status |
| `SEVERITY` | `VARCHAR2(30)` | Severity of the Oracle error. Possible values:  - `FAILURE` - `SUCCESS` - `WARNING` |
| `STATUS_MESSAGE` | `VARCHAR2(256)` | Error message associated with the Oracle error number in the `STATUS` column |
| `VERSION` | `VARCHAR2(30)` | Version of the broker configuration |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |