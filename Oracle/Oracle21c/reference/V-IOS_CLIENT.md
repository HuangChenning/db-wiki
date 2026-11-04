---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IOS_CLIENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.16 V$IOS\_CLIENT

`V$IOS_CLIENT` provides more information about IO Server clients.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENT_ID` | `NUMBER` | The unique ID for this client instance |
| `CLUSTER_ID` | `VARCHAR2(33)` | The GUID of the cluster where the client instance is running |
| `CLUSTER_NAME` | `VARCHAR2(16)` | When the query is executed on an Oracle IOServer (IOS) instance, this column shows the name of the cluster where the client (database) instance is running.  When the query is executed on a database instance, this column shows the name of the cluster where the IOS instance that the database is connected to is running. |
| `NODE` | `NUMBER` | Number of the node within the cluster where the client instance is running |
| `INSTANCE_NAME` | `VARCHAR2(64)` | Instance name of the database client instance |
| `DB_NAME` | `VARCHAR2(64)` | Database name of the database client instance |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

In an Oracle Database instance, this view returns 0 rows when queried from a PDB.