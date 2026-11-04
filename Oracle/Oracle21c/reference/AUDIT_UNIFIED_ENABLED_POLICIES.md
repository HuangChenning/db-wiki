---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_UNIFIED_ENABLED_POLICIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.175 AUDIT\_UNIFIED\_ENABLED\_POLICIES

`AUDIT_UNIFIED_ENABLED_POLICIES` describes all the audit policies that are enabled in the database.

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the audit policy |
| `ENABLED_OPTION` | `VARCHAR2(15)` |  | Enabled option of the audit policy. Possible values:  - `BY USER`: For policies that are enabled on users - `EXCEPT USER`: For policies that are enabled on users - `BY GRANTED ROLE`: For policies that are enabled on roles - `INVALID`: For policies that are not enabled on either users or roles |
| `ENTITY_NAME` | `VARCHAR2(128)` |  | Database entity (user name or role name) on which the audit policy is enabled.  When an audit policy is enabled on all database users, `ALL USERS` is displayed in this column. |
| `ENTITY_TYPE` | `VARCHAR2(7)` |  | Database entity type. Possible values:  - `USER`: Indicates that the policy is enabled on a user or users. - `ROLE`: Indicates that the policy is enabled on a role or roles. |
| `SUCCESS` | `VARCHAR2(3)` |  | Indicates whether the audit policy is enabled for auditing successful events (`YES`) or not (`NO`) |
| `FAILURE` | `VARCHAR2(3)` |  | Indicates whether the audit policy is enabled for auditing unsuccessful events (`YES`) or not (`NO`) |