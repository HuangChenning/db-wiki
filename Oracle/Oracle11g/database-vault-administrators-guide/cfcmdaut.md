---
title: Configuring Command Rules
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/cfcmdaut.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 6 Configuring Command Rules

This chapter contains:

## What Are Command Rules?

A command rule is a rule that you create to protect `SELECT`, `ALTER SYSTEM`, database definition language (DDL), and data manipulation language (DML) statements that affect one or more database objects. To customize and enforce the command rule, you associate it with a rule set, which is a collection of one or more rules. The command rule is enforced at run time. Command rules affect anyone who tries to use the SQL statements it protects, regardless of the realm in which the object exists. If you want to protect realm-specific objects, see ["Defining Realm Authorization"](cfrealms.md).

A command rule has the following attributes, in addition to associating a command rule to a command:

- SQL statement the command rule protects
- Owner of the object the command rule affects
- Database object the command rule affects
- Whether the command rule is enabled
- An associated rule set

For more information about SQL statements and operations, refer to [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm). See also "SQL Statements That Can Be Protected by Command Rules".

Command rules can be categorized as follows:

- Command rules that have a system-wide scope. With this type, you can only create one command rule for each database instance. Examples are command rules for the `ALTER SYSTEM` and `CONNECT` statements.
- Command rules that are schema specific. An example is creating a command rule for the `DROP TABLE` statement.
- Command rules that are object specific. An example is creating a command rule for the `DROP TABLE` statement with a specific table included in the command rule definition.

When a user executes a statement affected by a command rule, Oracle Database Vault checks the realm authorization first. If it finds no realm violation and if the associated command rules are enabled, then Database Vault evaluates the associated rule sets. If all the rule sets evaluate to TRUE, then the statement is authorized for further processing. If any of the rule sets evaluate to FALSE, then the statement is not authorized and a command rule violation is created. [Chapter 5, "Configuring Rule Sets,"](cfrulset.md) describes rule sets in detail.

You can define a command rule that uses factors for the `CONNECT` event to permit or deny sessions after the usual steps–user authentication process, factor initialization, and Oracle Label Security integration–are complete.

For example, you can configure a command rule that allows DDL statements such as `CREATE TABLE`, `DROP TABLE`, and `ALTER TABLE` in the `BIZAPP` schema to be authorized after business hours, but not during business hours.

You can run reports on the command rules that you create in Oracle Database Vault. See "Related Reports and Data Dictionary View" for more information.

This chapter explains how to configure command rules by using Oracle Database Vault Administrator. To configure command rules by using the PL/SQL interfaces and packages provided by Oracle Database Vault, refer to the following chapters:

- [Chapter 12, "Using the DBMS\_MACADM Package"](apis_dbms_macadm.md)
- [Chapter 15, "Using the Oracle Database Vault PL/SQL Interfaces"](plsql_interfaces.md)

## Default Command Rules

Table 6-1 lists default command rules that Oracle Database Vault provides.

Table 6-1 Default Command Rules

| SQL Statement | Object Name | Rule Set Name |
| --- | --- | --- |
| `ALTER PROFILE` | \- | Can Maintain Accounts/Profiles |
| `ALTER SYSTEM` | \- | Allow Fine Grained Control of System Parameters |
| `ALTER USER` | \- | Can Maintain Own Account |
| `CREATE PROFILE` | \- | Can Maintain Accounts/Profiles |
| `CREATE USER` | \- | Can Maintain Accounts/Profiles |
| `DROP PROFILE` | \- | Can Maintain Accounts/Profiles |
| `DROP USER` | \- | Can Maintain Accounts/Profiles |

The following set of command rules helps you to achieve separation of duty for user management:

- `ALTER PROFILE`
- `ALTER USER`
- `CREATE PROFILE`
- `CREATE USER`
- `DROP PROFILE`
- `DROP USER`

To grant a user the ability to use these commands, you can grant the user the role that the rule set checks. For example, the `CREATE USER` command rule ensures that a user who tries to run a `CREATE USER` statement has the `DV_ACCTMGR` role.

## SQL Statements That Can Be Protected by Command Rules

You can protect the following SQL statements by using command rules:

| `ALTER CLUSTER` | `CREATE CONTEXT` | `DROP DIRECTORY` |
| --- | --- | --- |
| `ALTER DIMENSION` | `CREATE DATABASE LINK` | `DROP FUNCTION` |
| `ALTER FUNCTION` | `CREATE DIMENSION` | `DROP INDEX` |
| `ALTER INDEX` | `CREATE DIRECTORY` | `DROP INDEXTYPE` |
| `ALTER INDEXTYPE` | `CREATE FUNCTION` | `DROP JAVA` |
| `ALTER JAVA` | `CREATE INDEX` | `DROP LIBRARY` |
| `ALTER OPERATOR` | `CREATE INDEXTYPE` | `DROP OPERATOR` |
| `ALTER OUTLINE` | `CREATE JAVA` | `DROP OUTLINE` |
| `ALTER PACKAGE` | `CREATE LIBRARY` | `DROP PACKAGE` |
| `ALTER PACKAGE BODY` | `CREATE OPERATOR` | `DROP PACKAGE BODY` |
| `ALTER PROCEDURE` | `CREATE OUTLINE` | `DROP PROCEDURE` |
| `ALTER PROFILE` | `CREATE PACKAGE` | `DROP PROFILE` |
| `ALTER RESOURCE COST` | `CREATE PACKAGE BODY` | `DROP ROLE` |
| `ALTER ROLE` | `CREATE PROCEDURE` | `DROP ROLLBACK SEGMENT` |
| `ALTER ROLLBACK SEGMENT` | `CREATE PROFILE` | `DROP SEQUENCE` |
| `ALTER SEQUENCE` | `CREATE ROLE` | `DROP SNAPSHOT` |
| `ALTER SNAPSHOT` | `CREATE ROLLBACK SEGMENT` | `DROP SNAPSHOT LOG` |
| `ALTER SNAPSHOT LOG` | `CREATE SCHEMA` | `DROP TABLE` |
| `ALTER SYNONYM` | `CREATE SEQUENCE` | `DROP TABLESPACE` |
| `ALTER SYSTEM` | `CREATE SNAPSHOT` | `DROP TRIGGER` |
| `ALTER TABLE` | `CREATE SNAPSHOT LOG` | `DROP TYPE` |
| `ALTER TABLESPACE` | `CREATE SYNONYM` | `DROP TYPE BODY` |
| `ALTER TRIGGER` | `CREATE TABLE` | `DROP USER` |
| `ALTER TYPE` | `CREATE TABLESPACE` | `DROP VIEW` |
| `ALTER TYPE BODY` | `CREATE TRIGGER` | `EXECUTE` |
| `ALTER USER` | `CREATE TYPE` | `GRANT` |
| `ALTER VIEW` | `CREATE TYPE BODY` | `INSERT` |
| `ANALYZE CLUSTER` | `CREATE USER` | `NOAUDIT` |
| `ANALYZE INDEX` | `CREATE VIEW` | `RENAME` |
| `ANALYZE TABLE` | `DELETE` | `REVOKE` |
| `ASSOCIATE STATISTICS` | `DISASSOCIATE STATISTICS` | `SELECT` |
| `AUDIT` | `DROP CLUSTER` | `TRUNCATE CLUSTER` |
| `COMMENT` | `DROP CONTEXT` | `TRUNCATE TABLE` |
| `CONNECT` | `DROP DATABASE LINK` | `UPDATE` |
| `CREATE CLUSTER` | `DROP DIMENSION` |  |

## Creating and Editing a Command Rule

Follow these steps:

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Administration page, under Database Vault Feature Administration, click Command Rules.
3. In the Command Rules page:
	- To create a new command rule, click Create.
		- To edit an existing command rule, select it from the list and then click Edit.
4. In the Create (or Edit) Command Rule page, enter the following settings, and then click OK.
	- General
		- Applicability
		- Rule Set

General

Enter the following settings:

- Command: Select the SQL statement or operation for which you want to create a command rule. This attribute is mandatory.
- Status: Select either Enabled or Disabled to enable or disable the command rule during run time. The default is Enabled. This attribute is mandatory.

Applicability

Enter the following settings:

- Object Owner: From the list, select the owner of the object the command rule affects. You can use wildcard character `%` to select all owners. (However, you cannot use wildcard characters with text, such as `EM%` to select all owners whose names begin in `EM`.) This attribute is mandatory for all SQL statements that operate on objects within a specific schema. See "SQL Statements That Can Be Protected by Command Rules" for a list of supported SQL statements.
	Note that the `SELECT`, `INSERT`, `UPDATE`, `DELETE`, and `EXECUTE` statements are not allowed for a selection of all (%) or the `SYS` and `DVSYS` schemas.
- Object Name: Enter the name of the database object that the command rule affects, or specify % to select all database objects. However, you cannot use wildcard characters with text (for example, `EMP_%` to specify all tables beginning with the characters `EMP_`). This attribute is mandatory, if you selected an object owner from the Object Owner list.
	You can run Oracle Database Vault reports on objects that the command rule affects. See the "Related Reports and Data Dictionary View" for more information.

Rule Set

From the list, select the rule set that you want to associate with the command rule. This attribute is mandatory.

If the rule set evaluates to true, then the SQL statement succeeds. If it evaluates to false, the statement fails, and then Oracle Database Vault raises a command rule violation. (You can track rule violations by using the Command Rule Configuration Issues Report, discussed in [Chapter 18](reports.md).) Any auditing and custom event handling associated with the rule set occurs as a part of the command rule processing.

See [Chapter 5, "Configuring Rule Sets,"](cfrulset.md) for more information about rule sets.

See Also:

["Propagating Oracle Database Vault Policies to Other Databases"](dba.md)

## Deleting a Command Rule

Before you delete a command rule, you can locate the various references to it by querying the command rule-related Oracle Database Vault views. See [Chapter 16, "Oracle Database Vault Data Dictionary Views,"](views.md) for more information.

To delete a command rule:

1. In the Oracle Database Vault Administration page, select Command Rules.
2. In the Command Rules page, select the command rule that you want to remove.
3. Click Remove.
4. In the Confirmation page, click Yes.

## How Command Rules Work

["How Realms Work"](cfrealms.md) describes what happens when a database account issues a `SELECT`, DDL, or DML statement that affects objects within a realm.

The following actions take place when `SELECT`, DDL, or DML statement is issued:

1. Oracle Database Vault queries all the command rules that need to be applied.
	For `SELECT`, DDL, and DML statements, multiple command rules may apply because the object owner and object name support wildcard notation.
	You can associate rule sets with both command rules and realm authorizations. Oracle Database Vault evaluates the realm authorization rule set first, and then it evaluates the rule sets that apply to the command type being evaluated.
2. For each command rule that applies, Oracle Database Vault evaluates its associated rule set.
3. If the associated rule set of any of the applicable command rules returns false or errors, Oracle Database Vault prevents the command from executing. Otherwise, the command is authorized for further processing. The configuration of the rule set with respect to auditing and event handlers dictates the auditing or custom processing that occurs.
	Command rules override object privileges. You can disable (or set the Disabled setting for) either a command or a rule set of a command. If a command rule is disabled, then the command rule is not allowed to run regardless of its associated rule set. That is, the command rule itself is disabled. However, if you disable a rule set of a command rule, then the rule set is not checked. In that case, the command rule is allowed to run without any condition. If the command rule has been set to the Disabled setting, then you are prevented from querying the table even though you have the `SELECT` privilege on the table. (Only the rule set has been disabled, not the command rule itself.)

## Tutorial: Using a Command Rule to Control Table Creations by a User

This section contains:

- About This Tutorial
- Step 1: Connect as User SCOTT and Create a Table
- Step 2: Connect Using the DVOWNER or DV\_ADMIN Role and Create a Command Rule
- Step 3: Test the Command Rule
- Step 4: Remove the Components for this Tutorial

See Also:

["Tutorial: Creating an Email Alert for Security Violations"](cfrulset.md) for another example of how a command rule can work with a rule set to send an email alert when a violation occurs

### About This Tutorial

In this tutorial, you create a simple command rule that disables and then enables the ability of user `SCOTT` to create tables.

### Step 1: Connect as User SCOTT and Create a Table

1. Log in to SQL\*Plus as user `SCOTT`.
	```
	sqlplus scott
	Enter password: password
	```
	If the `SCOTT` account is locked and expired, then log in as the Database Vault Account Manager and unlock `SCOTT` and create a new password. For example:
	```
	sqlplus amalcolm_dvacctmgr
	Enter password: password
	ALTER USER SCOTT ACCOUNT UNLOCK IDENTIFIED BY password;
	```
	Replace `password` with a password that is secure. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG33223) for the minimum requirements for creating passwords.
	```
	CONNECT SCOTT
	Enter password: password
	```
2. As user `SCOTT`, create a table.
	```
	CREATE TABLE t1 (num NUMBER);
	```
3. Now drop the table.
	```
	DROP TABLE t1;
	```

At this stage, user `SCOTT` can create and drop tables. Do not exit SQL\*Plus yet, and remain connected as `SCOTT`. You must use it later on when `SCOTT` tries to create another table.

### Step 2: Connect Using the DVOWNER or DV\_ADMIN Role and Create a Command Rule

1. Log in to Oracle Database Vault Administrator as a user who has been granted the `DV_OWNER` or `DV_ADMIN` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. In the Oracle Database Vault Administrator Administration page, click Command Rules.
	The Command Rules page appears.
3. Click Create.
	The Create Command Rule page appears.
4. Enter the following settings:
	- Command list: Select CREATE TABLE
		- Status: Set to Enabled so that the command rule is active.
		- Object Owner: Select SCOTT.
		- Object Name: Set to % so that it applies to all objects in the `SCOTT` schema.
		- Rule Set: Select Disabled so that user `SCOTT` is prevented from creating tables.
5. Click OK.
	Do not exit Database Vault Administrator

Command rules take effect immediately. Right away, user `SCOTT` is prevented from creating tables, even though he is still in the same user session he was in a moment ago, before you created the CREATE TABLE command rule.

### Step 3: Test the Command Rule

1. In SQL\*Plus, ensure that you are logged on as user `SCOTT`.
	```
	CONNECT SCOTT
	Enter password: password
	```
2. Try to create a table.
	```
	CREATE TABLE t1 (num NUMBER);
	```
	The following output should appear:
	```
	ORA-47400: Command Rule violation for create table on SCOTT.T1
	```
	As you can see, `SCOTT` is no longer allowed to create tables, even in his own schema.
3. In Oracle Database Vault Administrator, do the following:
	1. In the Command Rules page, select the CREATE TABLE command rule and then click Edit.
		2. In the Edit Command Rule page, select Enabled from the Rule Set list.
		3. Click OK.
4. In SQL\*Plus, as user `SCOTT`, try creating the table again.
	```
	CREATE TABLE t1 (num NUMBER);
	Table created.
	```

Now that the CREATE TABLE command rule is set to Enabled, user `SCOTT` is once again permitted to create tables. (Do not exit SQL\*Plus.)

### Step 4: Remove the Components for this Tutorial

1. In Oracle Database Vault Administrator, remove the CREATE TABLE command rule as follows:
	- Return to the Command Rules page.
		- Select the CREATE TABLE command rule and then click Remove.
		- In the Confirmation page, click Yes.
2. Log in to SQL\*Plus as user `SCOTT` and remove the `t1` table.
	```
	DROP TABLE t1;
	```
3. If you no longer need the `SCOTT` account to be available, then connect as the Database Vault Account Manager and enter the following `ALTER USER` statement:
	```
	CONNECT amalcolm_dvacctmgr
	Enter password: password
	ALTER USER SCOTT ACCOUNT LOCK PASSWORD EXPIRE;
	```

## Guidelines for Designing Command Rules

Follow these guidelines to design command rules:

- Create finer-grained command rules, because they are far easier to maintain.
	For example, if you want to prevent `SELECT` statements from occurring on specific schema objects, then design multiple command rules to stop the `SELECT` statements on those specific schema objects, rather than creating a general command rule to prevent `SELECT` statements in the schema level.
- When designing rules for the CONNECT event, be careful to include logic that does not inadvertently lock out any required user connections. If any account has been locked out accidentally, ask a user who has been granted the `DV_ADMIN` or `DV_OWNER` role to log in and correct the rule that is causing the lock-out problem. The CONNECT command rule does not apply to users with the `DV_OWNER` and `DV_ADMIN` roles. This prevents improperly configured CONNECT command rules from causing a complete lock-out.
	If the account has been locked out, you can disable Oracle Database Vault, correct the rule that is causing the lock-out problem, and then reenable Oracle Database Vault. Even when Oracle Database Vault is disabled, you still can use Database Vault Administrator and the Database Vault PL/SQL packages. See [Appendix B, "Disabling and Enabling Oracle Database Vault,"](dvdisabl.md) for instructions on disabling and reenabling Database Vault.
- Sometimes you must temporarily relax an enabled command rule for an administrative task. Rather than disabling the command rule, have the Security Manager (the account with the `DV_ADMIN` or `DV_OWNER` role) log in, set the rule set to Enabled, turn on Auditing on Success or Failure for the default rule set named Enabled, and then set the command rule back to its original rule set when the task is complete.
- When designing command rules, be careful to consider automated processes such as backup where these procedures may be inadvertently disabled. You can account for these tasks by creating rules that allow the command when a series of Oracle Database Vault factors is known to be true (for example, the program being used), and the account being used or the computer or network on which the client program is running.

## How Command Rules Affect Performance

The performance of a command rule depends on the complexity of the rules in the rule set associated with the command rule. For example, suppose a rule set invokes a PL/SQL function that takes 5 seconds to run. In this case, a command rule that uses that rule set would take 5 seconds to grant access for the command statement to run.

You can check the system performance by running tools such as Oracle Enterprise Manager (including Oracle Enterprise Manager Database Control, which is installed by default with Oracle Database), `Statspack`, and `TKPROF`. For more information about Oracle Enterprise Manager, see the Oracle Enterprise Manager documentation set. For information about Database Control, refer to its online Help. [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) describes the `Statspack` and `TKPROF` utilities.

## Related Reports and Data Dictionary View

Table 6-2 lists Oracle Database Vault reports that are useful for analyzing command rules. See [Chapter 18, "Oracle Database Vault Reports,"](reports.md) for information about how to run these reports.

Table 6-2 Reports Related to Command Rules

| Report | Description |
| --- | --- |
| ["Command Rule Audit Report"](reports.md) | Lists audit records generated by command rule processing operations |
| ["Command Rule Configuration Issues Report"](reports.md) | Tracks rule violations, in addition to other configuration issues the command rule may have |
| ["Object Privilege Reports"](reports.md) | Lists object privileges that the command rule affects |
| ["Sensitive Objects Reports"](reports.md) | Lists objects that the command rule affects |
| ["Rule Set Configuration Issues Report"](reports.md) | Lists rules sets that have no rules defined or enabled, which may affect the command rules that use them |

You can use the `DVSYS.DBA_DV_COMMAND_RULE` data dictionary view to find the SQL statements that are protected by command rules. See ["DVSYS.DBA\_DV\_COMMAND\_RULE View"](views.md) for more information.