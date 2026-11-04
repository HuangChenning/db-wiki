---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/AUDIT_UNIFIED_ENABLED_POLICIES.html
tags:
  - oracle
  - 12c
  - reference
---

`AUDIT_UNIFIED_ENABLED_POLICIES` describes all the audit policies that are enabled in the database.

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(128)` |  | Username of the database user for whom the audit policy is enabled. If the audit policy is enabled for all users, then the value is `ALL USERS`.  This column is `NULL` for audit policies that are enabled on granted role.  This column is deprecated in Oracle Database 12c Release 2 (12.2.0.1), and may be removed in a future release. |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the audit policy |
| `ENABLED_OPT` | `VARCHAR2(7)` |  | Enabled option of the audit policy. Possible values:  - `BY`: For policies that are enabled on users - `EXCEPT`: For policies that are enabled on users - `INVALID`: For policies that are not enabled on either users or roles  This column is deprecated in Oracle Database 12c Release 2 (12.2.0.1), and may be removed in a future release. |
| `ENABLED_OPTION` | `VARCHAR2(15)` |  | Enabled option of the audit policy. Possible values:  - `BY USER`: For policies that are enabled on users - `EXCEPT USER`: For policies that are enabled on users - `BY GRANTED ROLE`: For policies that are enabled on roles - `INVALID`: For policies that are not enabled on either users or roles  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `ENTITY_NAME` | `VARCHAR2(128)` |  | Database entity (user name or role name) on which the audit policy is enabled.  When an audit policy is enabled on all database users, `ALL USERS` is displayed in this column.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `ENTITY_TYPE` | `VARCHAR2(7)` |  | Database entity type. Possible values:  - `USER`: Indicates that the policy is enabled on a user or users. - `ROLE`: Indicates that the policy is enabled on a role or roles.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `SUCCESS` | `VARCHAR2(3)` |  | Indicates whether the audit policy is enabled for auditing successful events (`YES`) or not (`NO`) |
| `FAILURE` | `VARCHAR2(3)` |  | Indicates whether the audit policy is enabled for auditing unsuccessful events (`YES`) or not (`NO`) |