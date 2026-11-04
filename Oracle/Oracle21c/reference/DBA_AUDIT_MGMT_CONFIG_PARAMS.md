---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUDIT_MGMT_CONFIG_PARAMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.170 DBA\_AUDIT\_MGMT\_CONFIG\_PARAMS

`DBA_AUDIT_MGMT_CONFIG_PARAMS` displays information about the currently configured audit trail properties that are used by the `DBMS_AUDIT_MGMT` PL/SQL package.

Note:

This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12c auditing or unified auditing is enabled for the database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(1024)` | `NOT NULL` | Name of the property |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the property |
| `AUDIT_TRAIL` | `VARCHAR2(28)` |  | Audit trails for which the property is configured:  - `STANDARD AUDIT TRAIL` - `FGA AUDIT TRAIL` - `STANDARD AND FGA AUDIT TRAIL` - `OS AUDIT TRAIL` - `XML AUDIT TRAIL` - `OS AND XML AUDIT TRAIL` - `ALL AUDIT TRAILS` - `UNIFIED AUDIT TRAIL` |

Note:

In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated when the `DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL` PL/SQL procedure is invoked. If the procedure was used when the database was in read-only mode, use `DBMS_AUDIT_MGMT.GET_AUDIT_TRAIL` to check the value of the property.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS65429) for more information about the parameters specified with the `DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY` procedure