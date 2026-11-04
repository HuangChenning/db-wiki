---
title: ALTER AUDIT POLICY (Unified Auditing)
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-AUDIT-POLICY-Unified-Auditing.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

This section describes the `ALTER` `AUDIT` `POLICY` statement for **unified** **auditing**. This type of auditing is new beginning with Oracle Database 12 *c* and provides a full set of enhanced auditing features. Refer to [*Oracle Database Security Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=DBSEG630) for more information on unified auditing.

## Purpose

Use the `ALTER` `AUDIT` `POLICY` statement to modify a unified audit policy.

## Prerequisites

You must have the `AUDIT` `SYSTEM` system privilege or the `AUDIT_ADMIN` role.

If you are connected to a multitenant container database (CDB), then to modify a common unified audit policy, the current container must be the root and you must have the commonly granted `AUDIT` `SYSTEM` privilege or the `AUDIT_ADMIN` common role. To modify a local unified audit policy, the current container must be the container in which the audit policy was created and you must have the commonly granted `AUDIT` `SYSTEM` privilege or the `AUDIT_ADMIN` common role, or you must have the locally granted `AUDIT` `SYSTEM` privilege or the `AUDIT_ADMIN` local role in the container.

After you alter an unified audit policy with object audit options, the new audit settings take place immediately, for both the active and subsequent user sessions. If you alter an unified audit policy with system audit options, or audit conditions, then they become effective only for new user sessions, but not for the current user session.

## Syntax

## alter\_audit\_policy::=

[Description of the illustration alter\_audit\_policy.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/alter_audit_policy.html)

**Note:** If you specify the `ADD` or `DROP` clause, then you must specify at least one of the clauses *privilege\_audit\_clause*, *action\_audit\_clause*, or *role\_audit\_clause*.

(*privilege\_audit\_clause::=*, *action\_audit\_clause::=*, *role\_audit\_clause::=*)

## privilege\_audit\_clause::=

[Description of the illustration privilege\_audit\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/privilege_audit_clause.html)

## action\_audit\_clause::=

[Description of the illustration action\_audit\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/action_audit_clause.html)

## standard\_actions::=

[Description of the illustration standard\_actions.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/standard_actions.html)

## component\_actions::=

[Description of the illustration component\_actions.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/component_actions.html)

## role\_audit\_clause::=

[Description of the illustration role\_audit\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/role_audit_clause.html)

## Semantics

## policy

Specify the name of the unified audit policy to be modified. The policy must have been created using the `CREATE` `AUDIT` `POLICY` statement. You can find descriptions of all unified audit policies by querying the `AUDIT_UNIFIED_POLICIES` view.

**See Also:**

- [CREATE AUDIT POLICY (Unified Auditing)](CREATE-AUDIT-POLICY-Unified-Auditing.md)
- [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=REFRN29157) for more information on the `AUDIT_UNIFIED_POLICIES` view

## ADD | DROP

Use the `ADD` clause to add privileges to be audited to *policy*.

Use the `DROP` clause to remove privileges to be audited from *policy*.

Refer to *[privilege\_audit\_clause](CREATE-AUDIT-POLICY-Unified-Auditing.md)*, *[action\_audit\_clause](CREATE-AUDIT-POLICY-Unified-Auditing.md)*, and *[role\_audit\_clause](CREATE-AUDIT-POLICY-Unified-Auditing.md)* of `CREATE` `AUDIT` `POLICY` for the full semantics of these clauses.

## CONDITION

Use this clause to drop, add, or replace the audit condition for *policy*.

Specify `DROP` to drop the audit condition from *policy*.

Specify `'` *audit\_condition* `'` … to add or replace the audit condition for *policy*.

Refer to *[audit\_condition](CREATE-AUDIT-POLICY-Unified-Auditing.md)*, [EVALUATE PER STATEMENT](CREATE-AUDIT-POLICY-Unified-Auditing.md), [EVALUATE PER SESSION](CREATE-AUDIT-POLICY-Unified-Auditing.md), and [EVALUATE PER INSTANCE](CREATE-AUDIT-POLICY-Unified-Auditing.md) of `CREATE` `AUDIT` `POLICY` for the full semantics of these clauses.

## ONLY TOPLEVEL

Specify this clause to change the existing unified audit policy to audit only the top level SQL statements issued by the user.

**Example: Add Top Level Auditing**

The example changes the HR audit policy *hr\_audit\_policy* to capture only top level statements.

```md
ALTER AUDIT POLICY hr_audit_policy ADD ONLY TOPLEVEL
```

You can drop top level auditing from an existing audit policy auditing the top level SQL statements.

**Example: Drop Top Level Auditing**

```md
ALTER AUDIT POLICY hr_audit_policy DROP ONLY TOPLEVEL
```

See [*Database Security Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=DBSEG-GUID-07F3ECF8-4B1C-47B3-95E5-F5C77B14392F) for more information.

## Examples

The following examples modify unified audit policies that were created in the `CREATE` `AUDIT` `POLICY` “ [Examples](CREATE-AUDIT-POLICY-Unified-Auditing.md) ”.

**Adding Privileges, Actions, and Roles to a Unified Audit Policy: Examples**

The following statement adds the system privileges `CREATE` `ANY` `TABLE` and `DROP` `ANY` `TABLE` to unified audit policy `dml_pol`:

```md
ALTER AUDIT POLICY dml_pol
  ADD PRIVILEGES CREATE ANY TABLE, DROP ANY TABLE;
```

The following statement adds the system actions `CREATE` `JAVA`, `ALTER` `JAVA`, and `DROP` `JAVA` to unified audit policy `java_pol`:

```md
ALTER AUDIT POLICY java_pol
  ADD ACTIONS CREATE JAVA, ALTER JAVA, DROP JAVA;
```

The following statement adds the role `dba` to unified audit policy `table_pol`:

```md
ALTER AUDIT POLICY table_pol
  ADD ROLES dba;
```

The following statement adds multiple system privileges, actions, and roles to unified audit policy `security_pol`:

```md
ALTER AUDIT POLICY security_pol
  ADD PRIVILEGES CREATE ANY LIBRARY, DROP ANY LIBRARY
      ACTIONS DELETE on hr.employees,
              INSERT on hr.employees,
              UPDATE on hr.employees,
              ALL on hr.departments
      ROLES dba, connect;
```

**Dropping Privileges, Actions, and Roles from a Unified Audit Policy: Examples**

The following statement drops the system privilege `CREATE` `ANY` `TABLE` from unified audit policy `table_pol`:

```md
ALTER AUDIT POLICY table_pol
  DROP PRIVILEGES CREATE ANY TABLE;
```

The following statement drops the `INSERT` and `UPDATE` actions on `hr`.`employees` from unified audit policy `dml_pol`:

```md
ALTER AUDIT POLICY dml_pol
  DROP ACTIONS INSERT on hr.employees,
               UPDATE on hr.employees;
```

The following statement drops the role `java_deploy` from unified audit policy `java_pol`:

```md
ALTER AUDIT POLICY java_pol
  DROP ROLES java_deploy;
```

The following statement drops a system privilege, an action, and a role from unified audit policy `hr_admin_pol`:

```md
ALTER AUDIT POLICY hr_admin_pol
  DROP PRIVILEGES CREATE ANY TABLE
       ACTIONS LOCK TABLE
       ROLES audit_viewer;
```

**Adding and Dropping Actions for a Unified Audit Policy: Example**

The following statement adds `EXPORT` actions for Oracle Data Pump to unified audit policy `dp_actions_pol` and drops `IMPORT` actions for Oracle Data Pump:

```md
ALTER AUDIT POLICY dp_actions_pol
  ADD ACTIONS COMPONENT = datapump EXPORT
  DROP ACTIONS COMPONENT = datapump IMPORT;
```

**Dropping the Audit Condition from a Unified Audit Policy: Example**

The following statement drops the audit condition from unified audit policy `order_updates_pol`:

```md
ALTER AUDIT POLICY order_updates_pol
  CONDITION DROP;
```

**Modifying the Audit Condition for a Unified Audit Policy: Example**

The following statement modifies the audit condition for unified audit policy `emp_updates_pol` so that the policy is enforced only when the auditable statement is issued by a user whose UID is 102:

```md
ALTER AUDIT POLICY emp_updates_pol
  CONDITION 'UID = 102'
  EVALUATE PER STATEMENT;
```