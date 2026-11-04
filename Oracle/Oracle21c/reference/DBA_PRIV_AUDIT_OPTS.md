---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PRIV_AUDIT_OPTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.251 DBA\_PRIV\_AUDIT\_OPTS

`DBA_PRIV_AUDIT_OPTS` describes current system privileges being audited across the system and by user.

Note:

This view is relevant when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(128)` |  | User name if by user auditing; `ANY CLIENT` if access by a proxy on behalf of a client is being audited; NULL for systemwide auditing |
| `PROXY_NAME` | `VARCHAR2(128)` |  | Name of the proxy user which is performing an operation for the client; NULL if the client is performing the operation directly |
| `PRIVILEGE` | `VARCHAR2(40)` | `NOT NULL` | Name of the system privilege being audited |
| `SUCCESS` | `VARCHAR2(10)` |  | Mode for `WHENEVER SUCCESSFUL` system auditing |
| `FAILURE` | `VARCHAR2(10)` |  | Mode for `WHENEVER NOT SUCCESSFUL` system auditing |