---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_UNIFIED_POLICY_COMMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.177 AUDIT\_UNIFIED\_POLICY\_COMMENTS

`AUDIT_UNIFIED_POLICY_COMMENTS` shows the description of each unified audit policy, if a description was entered for the unified audit policy using the `COMMENT ` SQL statement.

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the unified audit policy |