---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESOURCE_MANAGER_PLAN.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.312 RESOURCE\_MANAGER\_PLAN

`RESOURCE_MANAGER_PLAN` specifies the resource plan to use for a database (CDB or non-CDB).

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RESOURCE_MANAGER_PLAN = ` `resource_plan_name` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | Any valid character string |
| Basic | No |

In a CDB

In the root for a CDB, `RESOURCE_MANAGER_PLAN` specifies the CDB resource plan. A CDB resource plan allocates resources among PDBs.

A CDB resource plan is created using `DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN` and `CREATE_CDB_PLAN_DIRECTIVE`.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-3E84009E-5CD6-46B8-84D3-BE775D58D9AA) for more information about using `DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN` and `DBMS_RESOURCE_MANAGER.CREATE_CDB_PLAN_DIRECTIVE`
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73821) for more information about the `CREATE_CDB_PLAN` procedure and `CREATE_CDB_PLAN_DIRECTIVE` procedure for the `DBMS_RESOURCE_MANAGER` package

A session must be `root` to change the value of `RESOURCE_MANAGER_PLAN` for a CDB using the `ALTER SYSTEM` statement. For example, to enable and disable a CDB resource plan:

```
SQL> ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = CDB_resource_plan_name;
SQL> ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = '';
```

In a PDB, `RESOURCE_MANAGER_PLAN` specifies the PDB resource plan to use for the PDB.

A session must be in the PDB to enable or disable a PDB resource plan for that PDB. For example, to enable and disable a PDB resource plan:

```
SQL> ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = PDB_resource_plan_name;
SQL> ALTER SYSTEM SET RESOURCE_MANAGER_PLAN = '';
```

In a PDB, the PDB resource plan has some restrictions compared to the resource plan of a non-CDB. The following restrictions apply to PDB resource plans:

- A PDB resource plan cannot have subplans.
- A PDB resource plan cannot have a multiple-level scheduling policy.

To enforce certain PDB resource plan policies, policies regarding resource allocation among PDBs should exist in the CDB resource plan. Without a CDB resource plan, certain PDB resource plan policies will not be enforced. If a PDB resource plan contains CPU or parallel statement queuing directives and a CDB resource plan is not specified, then Resource Manager will automatically enable the `DEFAULT_CDB_PLAN` plan. To prevent this behavior, set the `RESOURCE_MANAGER_PLAN` parameter at the root level to `ORA$INTERNAL_CDB_PLAN`.

Note:

See [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN13787) for information on CPU, I/O bandwidth, and parallel execution servers requirements in CDB resource plans, and for a description of the results in the PDB resource plans when those requirements are not met.

In a Non-CDB

`RESOURCE_MANAGER_PLAN` specifies the top-level resource plan to use for an instance in a non-CDB. The resource manager will load this top-level resource plan along with all its descendants (subplans, directives, and consumer groups). If you do not specify this parameter, the resource manager is off by default.

You can change the setting of this parameter using the `ALTER SYSTEM` statement to turn on the resource manager (if it was previously off) or to turn off the resource manager or change the current resource plan (if it was previously on). If you specify a resource plan that does not exist in the data dictionary, Oracle returns an error message.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN027) for information on using Oracle Resource Manager
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS050) for information on the `DBMS_RESOURCE_MANAGER` package
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS051) for information on the `DBMS_RESOURCE_MANAGER_PRIVS` package
- " [DBA\_RSRC\_PLANS](DBA_RSRC_PLANS.md) ", " [DBA\_RSRC\_PLAN\_DIRECTIVES](DBA_RSRC_PLAN_DIRECTIVES.md) ", and the various `V$RSRC_*` dynamic performance views in [Dynamic Performance Views](dynamic-performance-views.md) for information on existing resource plans