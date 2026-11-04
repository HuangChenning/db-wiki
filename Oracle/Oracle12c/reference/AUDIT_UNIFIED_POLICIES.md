---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/AUDIT_UNIFIED_POLICIES.html
tags:
  - oracle
  - 12c
  - reference
---

`AUDIT_UNIFIED_POLICIES` describes all audit policies created in the database.

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the audit policy |
| `AUDIT_CONDITION` | `VARCHAR2(4000)` |  | Condition associated with the audit policy |
| `CONDITION_EVAL_OPT` | `VARCHAR2(9)` |  | Evaluation option associated with the audit policy's condition. The possible values are `STATEMENT`, `SESSION`, `INSTANCE`, and `NONE`. |
| `AUDIT_OPTION` | `VARCHAR2(128)` |  | Auditing option defined in the audit policy |
| `AUDIT_OPTION_TYPE` | `VARCHAR2(18)` |  | Type of the auditing option. Possible values:  - `SYSTEM PRIVILEGE` - `STANDARD ACTION` - `SYSTEM ACTION` - `XS ACTION` - `OLS_ACTION` - `DATAPUMP ACTION` - `DIRECT LOAD ACTION` - `DV ACTION` - `INVALID` - `OBJECT ACTION` - `ROLE PRIVILEGE` |
| `OBJECT_SCHEMA` | `VARCHAR2(128)` |  | Owner of the object, for an object-specific auditing option |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object, for an object-specific auditing option |
| `OBJECT_TYPE` | `VARCHAR2(23)` |  | Type of the object, for an object-specific auditing option |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the audit policy is a common audit policy or local audit policy. The value is `NULL` for a non-CDB.  For local audit policies, the value of the `COMMON` column is always `NO`.  For a CDB common policy:  - If you query `AUDIT_UNIFIED_POLICIES` from the CDB root container, the value of the `COMMON` column will be `YES` and the value of the `INHERITED` column will be `NO`. - If you query `AUDIT_UNIFIED_POLICIES` from any other container besides the CDB root container, the value of the `COMMON` column and the `INHERITED` column will be `YES`.  For an application container common policy:  - If you query `AUDIT_UNIFIED_POLICIES` from the application root container, the value of the `COMMON` column will be `YES` and the value of the `INHERITED` column will be `NO`. - If you query `AUDIT_UNIFIED_POLICIES` from any other container besides the application root container, the value of the `COMMON` column and the `INHERITED` column will be `YES`. |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the audit policy was inherited from another container (`YES`) or not (`NO`). It is `NULL` for non-CDBs.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |