---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IP_ACL.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.22 V$IP\_ACL

`V$IP_ACL` provides information about access control to database services from network hosts.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERVICE_NAME` | `VARCHAR2(512)` | The database service name |
| `HOST` | `VARCHAR2(64)` | The host being granted access to the `SERVICE_NAME`. The host can be a hostname, dotted-decimal IPv4 or heximal IPv6 address. Wildcard "\*" for IPv4 and Classless Inter-Domain Routing (CIDR) format is allowed. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs - `1`: This value is used for rows containing data that pertain only to the root - n: Where n is the applicable container ID for the rows containing data |