---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-EXADIRECT_ACL.html
tags:
  - oracle
  - 19c
  - reference
---

## 7.212 V$EXADIRECT\_ACL

`V$EXADIRECT_ACL` monitors current ACLs propagated to the database instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME` | `VARCHAR2(512)` | Database service name |
| `SGID` | `VARCHAR2(39)` | Identifier of the VM allowed access to the specified service name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |