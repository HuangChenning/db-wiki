---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-DG_BROKER_CONFIG.html
tags:
  - oracle
  - 12c
  - reference
---

`V$DG_BROKER_CONFIG` provides a summary of an Oracle Data Guard broker configuration.

This is similar to the DGMGRL CLI's `SHOW CONFIGURATION` command. It provides a view of the entire Oracle Data Guard broker configuration from any database in the configuration.

| Column | Datatype | Description |
| --- | --- | --- |
| `DATABASE` | `VARCHAR2(512)` | Database unique name |
| `CONNECT_IDENTIFIER` | `VARCHAR2(512)` | Net connect identifier used to reach the database |
| `DATAGUARD_ROLE` | `VARCHAR2(27)` | Oracle Data Guard role of the database:  - `PRIMARY` - `PHYSICAL_STANDBY` - `LOGICAL_STANDBY` - `SNAPSHOT_STANDBY` - `FAR SYNC INSTANCE` - `RECOVERY APPLIANCE` |
| `REDO_SOURCE` | `VARCHAR(30)` | The database unique name of the redo source |
| `ENABLED` | `VARCHAR2(5)` | TRUE or FALSE to denote whether or not the database is managed by Oracle Data Guard broker |
| `STATUS` | `NUMBER` | An Oracle error number denoting the database's current status |
| `VERSION` | `VARCHAR2(30)` | Version of the broker configuration |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |