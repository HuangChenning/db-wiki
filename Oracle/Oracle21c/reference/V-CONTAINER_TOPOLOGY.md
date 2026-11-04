---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CONTAINER_TOPOLOGY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.139 V$CONTAINER\_TOPOLOGY

`V$CONTAINER_TOPOLOGY` displays information about the containers associated with the current instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTANCE_NUMBER` | `NUMBER` | Instance number, as specified by the `INSTANCE_NUMBER` initialization parameter for the database in which the container resides |
| `CON_NAME` | `VARCHAR2(128)` | Container name |
| `OPEN_MODE` | `VARCHAR2(10)` | Open mode for the container:  - `MIGRATE` - `MOUNTED` - `READ` `ONLY` - `READ` `WRITE` |
| `CPU_COUNT` | `NUMBER` | CPU count, as specified by the `CPU_COUNT` initialization parameter for the container |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `IS_HYBRID_READ_ONLY` | `VARCHAR2(3)` | Reserved for future use |

Note:

This view is available starting with Oracle Database 21c.