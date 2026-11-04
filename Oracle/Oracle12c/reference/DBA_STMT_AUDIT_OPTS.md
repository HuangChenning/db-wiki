---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_STMT_AUDIT_OPTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_STMT_AUDIT_OPTS` describes current system auditing options across the system and by user.

Note:

This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from `UNIFIED_AUDIT_TRAIL`.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(128)` |  | User name if by user auditing; `ANY CLIENT` if access by a proxy on behalf of a client is being audited; NULL for system-wide auditing |
| `PROXY_NAME` | `VARCHAR2(128)` |  | Name of the proxy user which is performing an operation for the client; NULL if the client is performing the operation directly |
| `AUDIT_OPTION ` | `VARCHAR2(40)` | `NOT NULL` | Name of the system auditing option |
| `SUCCESS ` | `VARCHAR2(10)` |  | Mode for `WHENEVER SUCCESSFUL` system auditing |
| `FAILURE` | `VARCHAR2(10)` |  | Mode for `WHENEVER NOT SUCCESSFUL` system auditing |