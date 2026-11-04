---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FS_FAILOVER_OBSERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.241 V$FS\_FAILOVER\_OBSERVERS

`V$FS_FAILOVER_OBSERVERS` provides information about fast-start failover observers.

If you are querying on the primary database, this view returns three rows, each describing one observer. However, only a row having an non-empty value in column `NAME` corresponds to a started observer. If you are querying on a non-primary database, the behavior of this view is not defined.

| Column | Datatype | Description |
| --- | --- | --- |
| `NAME` | `VARCHAR2(513)` | The fast-start failover observer name |
| `REGISTERED` | `VARCHAR2(4)` | Indicates if this observer is registered (`YES`) or not (`NO`). Note that the observer is registered only if `HOST` is not `NULL`. |
| `HOST` | `VARCHAR2(513)` | The name of the host where this observer is running |
| `ISMASTER` | `VARCHAR2(4)` | Indicates if this observer is the master observer (`YES`) or not (`NO`) |
| `TIME_SELECTED` | `TIMESTAMP(9)` | Shows when this observer became master observer, if `ISMASTER` is `YES`; otherwise the following constant appears:  `1990–01–01 00:00:00.00` |
| `PINGING_PRIMARY` | `VARCHAR2(4)` | Possible values: - `YES`: Observer is currently connected to the primary database - `NO`: Observer is not connected to the primary database  Note: This field is consistent throughout an Oracle Real Application Clusters (Oracle RAC) environment; that is, if the observer is connected to any instance of the primary database in the Oracle RAC environment, all instances will show a value of `YES`. |
| `PINGING_TARGET` | `VARCHAR2(4)` | Possible values: - `YES`: Observer is currently connected to the target standby database - `NO`: Observer is not connected to the target standby database  Note: This field is consistent throughout an Oracle Real Application Clusters (Oracle RAC) environment; that is, if the observer is connected to any instance of the target standby database in the Oracle RAC environment, all instances will show a value of `YES`. |
| `LOG_FILE` <sup>Foot 1</sup> | `VARCHAR2(513)` | Full path to the observer log file |
| `STATE_FILE` <sup>Foot 1</sup> | `VARCHAR2(513)` | Full path to the observer runtime data file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.