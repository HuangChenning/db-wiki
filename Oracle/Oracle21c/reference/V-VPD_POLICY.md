---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-VPD_POLICY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.129 V$VPD\_POLICY

`V$VPD_POLICY` displays all the fine-grained security policies and predicates associated with the cursors currently in the library cache.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4 \| 8)` | Cursor address |
| `PARADDR` | `RAW(4 \| 8)` | Parent cursor address |
| `SQL_HASH` | `NUMBER` | SQL hash number |
| `SQL_ID` | `VARCHAR2(13)` | SQL identifier |
| `CHILD_NUMBER` | `NUMBER` | Cursor's child number under the parent |
| `OBJECT_OWNER` | `VARCHAR2(128)` | Owner of the object with the policy |
| `OBJECT_NAME` | `VARCHAR2(128)` | Name of the object with the policy |
| `POLICY_GROUP` | `VARCHAR2(128)` | Name of the policy group |
| `POLICY` | `VARCHAR2(128)` | Name of the policy |
| `POLICY_FUNCTION_OWNER` | `VARCHAR2(128)` | Owner of the policy function |
| `PREDICATE` | `VARCHAR2(4000)` | Predicate for the policy (truncated to `4000` bytes in length) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |