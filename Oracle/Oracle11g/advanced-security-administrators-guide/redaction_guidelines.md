---
title: Security Guidelines for Oracle Data Redaction
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/redaction_guidelines.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## 7 Security Guidelines for Oracle Data Redaction

This chapter provides a set of security guidelines for using Oracle Data Redaction.

This chapter contains the following topics:

## 7.1 General Usage Guidelines

- Oracle Data Redaction is not intended to protect against attacks by privileged database users who run ad hoc queries directly against the database.
- Oracle Data Redaction is not intended to protect against users who run exhaustive SQL queries that attempt to determine the actual values by [inference](asogls.md).
- Oracle Data Redaction relies on the database and application context values. For applications, it is the responsibility of the application to properly initialize the context value.
- Oracle Data Redaction is not enforced for users who are logged in using the `SYSDBA` administrative privilege.
- Certain DDL statements that attempt to copy the [actual data](asogls.md) out from under the control of a data redaction policy (that is, `CREATE TABLE AS SELECT`, `INSERT AS SELECT`) are blocked by default, but you can disable this behavior by granting the user the `EXEMPT REDACTION POLICY` system privilege
- Oracle Data Redaction does not affect day-to-day database operations, such as backup and recovery, Oracle Data Pump exports and imports, Oracle Data Guard operations, and replication.
- Do not include any redacted columns in a SQL expression that is used in a `GROUP BY` clause in a SQL statement. Oracle does not support this behavior, and raises an `ORA-00979: not a GROUP BY expression` error. This happens because internally the expression in the `SELECT` list must be modified by Data Redaction, but this causes it to no longer be found when it comes time to process the `GROUP BY` clause (which is currently not updated by Data Redaction) leading to this unintended error message.

## 7.2 Restricting Administrative Access to Oracle Data Redaction Policies

You can restrict the list of users who can create, view and edit Data Redaction policies by limiting who has the `EXECUTE` privilege on the `DBMS_REDACT` package and by limiting who has the `SELECT` privilege on the `REDACTION_POLICIES` and `REDACTION_COLUMNS` views. You also can restrict who is exempted from redaction by limiting the `EXEMPT REDACTION POLICY` privilege. If you use Oracle Database Vault to restrict privileged user access, then you can use realms to restrict granting of `EXEMPT REDACTION POLICY`.

See Also:

- ["Exempting Users from Oracle Data Redaction Policies"](redaction_config.md)
- ["Oracle Data Redaction and Oracle Database Vault"](redaction_other.md)
- [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvintro.htm#DVADM001) for more information about Oracle Database Vault

## 7.3 How Oracle Data Redaction Affects the SYS, SYSTEM and Default Schemas

Both users `SYS` and `SYSTEM` automatically have the `EXEMPT REDACTION POLICY` system privilege. (`SYSTEM` has the `EXP_FULL_DATABASE` role, which includes the `EXEMPT REDACTION POLICY` system privilege.) This means that the `SYS` and `SYSTEM` users can always bypass any existing Oracle Data Redaction policies, and will always be able to view data from tables (or views) that have Data Redaction policies defined on them.

Follow these guidelines:

- Do not create Data Redaction policies on the default Oracle Database schemas, including the `SYS` and `SYSTEM` schemas.
- Be aware that granting the `EXEMPT DATA REDACTION` system privilege to additional roles may enable users to bypass Oracle Data Redaction, because the grantee role may have been granted to additional roles.
- Do not revoke the `EXEMPT DATA REDACTION` system privilege from the roles that it was granted to by default.

## 7.4 Writing Policy Expressions That Depend on SYS\_CONTEXT Attributes

Be careful when writing a policy expression that depends on a `SYS_CONTEXT` attribute that is populated by an application, because the application might not always populate that attribute. If the user somehow connects directly (rather than through the application), then the `SYS_CONTEXT` attribute would not have been populated. If you do not handle this `NULL` scenario in your policy expression, you could unintentionally reveal [actual data](asogls.md) to the querying user.

For example, suppose you wanted to create a policy expression that intends to redact the query results for everyone except users who have the client identifier value of `SUPERVISOR`. The following expression unintentionally enables querying users who have `NULL` as the value for their `CLIENT_IDENTIFIER` to see the real data:

```
SYS_CONTEXT('USERENV', 'CLIENT_IDENTIFIER') IS NOT 'SUPERVISOR'
```

A more rigorous policy expression redacts the result of the query if the client identifier is not set, that is, it has a `NULL` value.

```
SYS_CONTEXT('USERENV', 'CLIENT_IDENTIFIER') IS NOT 'SUPERVISOR' OR IS NULL
```

Remember that in SQL, comparisons with `NULL` are undefined, and are thus `FALSE`, but redaction only takes place when the policy expression evaluates to `TRUE`.

## 7.5 Creating Policies on Materialized Views

You can create Oracle Data Redaction policies on materialized views and on their base tables. However, ensure that the creator of the materialized view, or the user who performs the refresh of the materialized view, is not blocked by any Data Redaction policies. In other words, the user performing the materialized view creation or refresh operations should be exempt from the Data Redaction policy. As a best practice, when you create a new materalized view, treat it as a copy of the actual table, and then create a separate Data Redaction policy to protect it.

## 7.6 Dropping Policies When the Recycle Bin Is Enabled

If you drop a table or view that has an Oracle Data Redaction policy defined on it when the recycle bin feature is enabled, and if you query the `REDACTION_COLUMNS` or `REDACTION_POLICIES` data dictionary views before you purge the recycle bin, then you will see object names such as `BIN$...` (for example, `BIN$1Xu5PSW5VaPgQxGS5AoAEA==$0`). This is normal behavior. These policies are removed when you purge the recycle bin.

To find if the recycle bin is enabled, run the `SHOW PARAMETER RECYCLEBIN` command in SQL\*Plus.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN11682) for information about purging objects from the recycle bin