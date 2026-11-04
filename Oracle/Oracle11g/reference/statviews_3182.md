---
title: DBA_FGA_AUDIT_TRAIL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3182.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FGA_AUDIT_TRAIL` displays all audit records for fine-grained auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` | `NOT NULL` | Session id of the query |
| `TIMESTAMP` | `DATE` |  | Date and time of the query in the local database session time zone |
| `DB_USER` | `VARCHAR2(30)` |  | Database username who executed the query |
| `OS_USER` | `VARCHAR2(255)` |  | Operating system username who executed the query |
| `USERHOST` | `VARCHAR2(128)` |  | Client host machine name |
| `CLIENT_ID` | `VARCHAR2(64)` |  | Client identifier in each Oracle session |
| `ECONTEXT_ID` | `VARCHAR2(64)` |  | Application execution context identifier |
| `EXT_NAME` | `VARCHAR2(4000)` |  | External name |
| `OBJECT_SCHEMA` | `VARCHAR2(30)` |  | Owner of the table or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or view |
| `POLICY_NAME` | `VARCHAR2(30)` |  | Name of the Fine-Grained Auditing Policy |
| `SCN` | `NUMBER` |  | System change number (SCN) of the query |
| `SQL_TEXT` | `NVARCHAR2(2000)` |  | SQL text of the query |
| `SQL_BIND` | `NVARCHAR2(2000)` |  | Bind variable data of the query |
| `COMMENT$TEXT` | `VARCHAR2(4000)` |  | Comments |
| `STATEMENT_TYPE` | `VARCHAR2(7)` |  | Statement type of the query: - `SELECT` - `INSERT` - `UPDATE` - `DELETE` |
| `EXTENDED_TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` |  | Timestamp of the query in UTC (Coordinated Universal Time) time zone |
| `PROXY_SESSIONID` | `NUMBER` |  | Proxy session serial number, if an enterprise user has logged in through the proxy mechanism |
| `GLOBAL_UID` | `VARCHAR2(32)` |  | Global user identifier for the user, if the user has logged in as an enterprise user |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number as specified by the `INSTANCE_NUMBER` initialization parameter |
| `OS_PROCESS` | `VARCHAR2(16)` |  | Operating System process identifier of the Oracle process |
| `TRANSACTIONID` | `RAW(8)` |  | Transaction identifier of the transaction in which the object is accessed or modified |
| `STATEMENTID` | `NUMBER` |  | Numeric ID for each statement run (a statement may cause many actions) |
| `ENTRYID` | `NUMBER` |  | Numeric ID for each audit trail entry in the session |
| `OBJ_EDITION_NAME` | `VARCHAR2(30)` |  | Name of the edition containing the audited object |
| `DBID` | `NUMBER` |  | Database identifier of the audited database |

Note:

The `SQL_BIND` and `SQL_TEXT` columns are populated only if the policy has been created with the `AUDIT_TRAIL` parameter set to `db`, `extended`.