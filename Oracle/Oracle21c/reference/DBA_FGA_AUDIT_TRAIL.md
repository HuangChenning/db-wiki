---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_FGA_AUDIT_TRAIL.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.322 DBA\_FGA\_AUDIT\_TRAIL

`DBA_FGA_AUDIT_TRAIL` displays all audit records for fine-grained auditing.

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SESSION_ID` | `NUMBER` | `NOT NULL` | Session id of the query |
| `TIMESTAMP` | `DATE` |  | Date and time of the query in the local database session time zone |
| `DB_USER` | `VARCHAR2(128)` |  | Database username who executed the query |
| `OS_USER` | `VARCHAR2(255)` |  | Operating system username who executed the query |
| `USERHOST` | `VARCHAR2(128)` |  | Client host machine name |
| `CLIENT_ID` | `VARCHAR2(128)` |  | Client identifier in each Oracle session |
| `ECONTEXT_ID` | `VARCHAR2(64)` |  | Application execution context identifier |
| `EXT_NAME` | `VARCHAR2(4000)` |  | External name |
| `OBJECT_SCHEMA` | `VARCHAR2(128)` |  | Owner of the table or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or view |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the Fine-Grained Auditing Policy |
| `SCN` | `NUMBER` |  | System change number (SCN) of the query |
| `SQL_TEXT` | `NVARCHAR2(2000)` |  | SQL text of the query |
| `SQL_BIND` | `NVARCHAR2(2000)` |  | Bind variable data of the query |