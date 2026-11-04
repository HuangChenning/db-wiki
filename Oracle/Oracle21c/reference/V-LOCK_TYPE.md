---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOCK_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.43 V$LOCK\_TYPE

`V$LOCK_TYPE` describes the type of locks available.

| Column | Datatype | Description |
| --- | --- | --- |
| `TYPE` | `VARCHAR2(64)` | A two-letter internal resource identifier |
| `NAME` | `VARCHAR2(64)` | Resource type name. This is a short (less than 32 characters) enqueue type name. |
| `ID1_TAG` | `VARCHAR2(64)` | Description of the enqueue type. |
| `ID2_TAG` | `VARCHAR2(64)` | Further description of the enqueue type. |
| `IS_USER` | `VARCHAR2(3)` | User enqueue. These are enqueues that are acquired as a direct result of a SQL statement. Applications may get deadlocks on these enqueues. Such deadlocks are considered application errors. |
| `IS_RECYCLE` | `VARCHAR2(3)` | Indicates whether the enqueue requires caching of the associated resource in the DLM's resource cache.  Possible values:  - `NO`: Means the enqueue requires caching of the associated resource in the DLM's resource cache - `YES`: Means the enqueue does not require caching of the associated resource in the DLM's resource cache |
| `DESCRIPTION` | `VARCHAR2(4000)` | Explanation of how or for what purpose the enqueue is used. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |