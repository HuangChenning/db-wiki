---
title: Oracle Database Vault Security Guidelines
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/guidelines.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## D Oracle Database Vault Security Guidelines

This appendix contains:

## Separation of Duty Guidelines

This section contains:

- How Oracle Database Vault Handles Separation of Duty
- Defining Separate Tasks in an Oracle Database Vault Environment
- Creating a Separation of Duty Matrix
- Identifying and Documenting the Tasks of Users Who Access the Database System

### How Oracle Database Vault Handles Separation of Duty

Separation of duty means that you restrict each user's privileges only to the tasks he or she is responsible for, and no more. You should assign specific categories of privileges to specific users, rather than granting many privileges to one user. Simply put, separation of duty creates accountability for each task that your organization requires.

Separation of duty has taken on increased importance over the past 10 years. For many organizations, separation of duty is a new concept that continues to evolve. Database consolidation, regulatory compliance, and outsourcing are just a few of the drivers for increased separation of duty. Oracle Database Vault separation of duty strengthens security by separating security-related administration from day-to-day DBA operations. You can tailor your Database Vault separation of duty implementation to easily adapt to current and future business requirements. Small organizations, in particular, need flexibility as they attempt to increase their security profile with limited resources.

### Defining Separate Tasks in an Oracle Database Vault Environment

Oracle Database Vault defines the following main responsibilities:

- Account management. Account management entails creating, modifying, and dropping user accounts. The `DV_ACCTMGR` role provides these privileges.
- Security administration. Security administration covers basic security tasks such as creating realms and command rules, setting security policies for database users' access, and authorizing database users for jobs they are allowed to perform. Security administrators also run security audit reports. The `DV_OWNER` and `DV_ADMIN` roles provide these privileges. (For an in-depth look at how the Oracle Database Vault roles provide for separation of duty, see ["Oracle Database Vault Roles"](db_objects.md).)
	Optionally, you can consolidate the account management and security administrative responsibilities.
- Resource management. Resource management refers to managing the database system but not accessing business data. It includes the following operations:
	- Backup operations require a predefined time to perform the backup using predefined tools.
		- Tuning and monitoring operations require ongoing performance monitoring and analysis.
		- Patching operations require temporary access only during the time the patching takes place
	For resource management, you should create a named account and a backup account for each of these tasks. Add these accounts as owners of the Data Dictionary realm. Use these accounts as the primary resource managers in the database.

You should have separate accounts for database account management, database security administration, and additional named accounts for backup operations. Auditors check for separate database accounts for different responsibilities and being able to track the actions of each account. Less important is the number of users assigned to specific tasks. Remember that Oracle Database Vault audit events are protected and that the Database Vault reports show all attempted violations.

### Creating a Separation of Duty Matrix

Before separation of duty can be successful, you must understand who performs basic administration tasks in your environment and what these administration tasks are. Even if a single database administrator is responsible for managing both new database account provisioning and application patching, it is important to document and plan for each of these tasks.Using separate administration accounts for these types of tasks provides increased accountability and reduces associated risks. In midsize to large organizations, database administrators typically must perform common administration tasks but they do not need access to business data managed by the application. Creating a matrix for your separation of duty can help you plan your Database Vault deployment. As needed, you can include additional tasks and associated users to this list. This information should become part of the overall enterprise security documentation for your organization.

Table D-1 shows an example of a separation of duty matrix.

Table D-1 Example Separation of Duty Matrix

<table><thead><tr><th rowspan="2">User, Process or Application</th><th rowspan="2">Account Creation</th><th colspan="5">Database Administration</th><th rowspan="2">Security Administrator</th></tr><tr><th headers="r1c1-t2 r1c1-t2">SYSDBA</th><th headers="r1c1-t2 r2c1-t2 r1c2-t2">Backup</th><th headers="r1c1-t2 r2c1-t2 r1c3-t2">Tuning</th><th headers="r1c1-t2 r2c1-t2 r1c3-t2 r1c4-t2">Patching</th><th headers="r1c1-t2 r2c1-t2 r1c3-t2">Monitoring</th></tr></thead><tfoot><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tfoot><tbody><tr><td headers="r1c1-t2 r2c1-t2"><p><code>JSMITH</code></p></td><td headers="r3c1-t2 r1c2-t2 r2c2-t2"><p>X</p></td><td headers="r3c1-t2 r1c3-t2 r2c3-t2"></td><td headers="r3c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"></td><td headers="r3c1-t2 r1c3-t2 r2c5-t2"></td><td headers="r3c1-t2 r1c3-t2"></td><td headers="r3c1-t2 r1c3-t2"></td><td headers="r3c1-t2"></td></tr><tr><td headers="r1c1-t2 r2c1-t2"><p><code>SHARDY</code></p></td><td headers="r4c1-t2 r1c2-t2 r2c2-t2"></td><td headers="r4c1-t2 r1c3-t2 r2c3-t2"></td><td headers="r4c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"></td><td headers="r4c1-t2 r1c3-t2 r2c5-t2"></td><td headers="r4c1-t2 r1c3-t2"></td><td headers="r4c1-t2 r1c3-t2"></td><td headers="r4c1-t2"><p>X</p></td></tr><tr><td headers="r1c1-t2 r2c1-t2"><p><code>PKESTNER</code></p></td><td headers="r5c1-t2 r1c2-t2 r2c2-t2"></td><td headers="r5c1-t2 r1c3-t2 r2c3-t2"></td><td headers="r5c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"><p>X</p></td><td headers="r5c1-t2 r1c3-t2 r2c5-t2"></td><td headers="r5c1-t2 r1c3-t2"></td><td headers="r5c1-t2 r1c3-t2"></td><td headers="r5c1-t2"></td></tr><tr><td headers="r1c1-t2 r2c1-t2"><p><code>RTYLER</code></p></td><td headers="r6c1-t2 r1c2-t2 r2c2-t2"></td><td headers="r6c1-t2 r1c3-t2 r2c3-t2"></td><td headers="r6c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"></td><td headers="r6c1-t2 r1c3-t2 r2c5-t2"></td><td headers="r6c1-t2 r1c3-t2"><p>X</p></td><td headers="r6c1-t2 r1c3-t2"></td><td headers="r6c1-t2"></td></tr><tr><td headers="r1c1-t2 r2c1-t2"><p><code>SANDERSON</code></p></td><td headers="r7c1-t2 r1c2-t2 r2c2-t2"></td><td headers="r7c1-t2 r1c3-t2 r2c3-t2"></td><td headers="r7c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"></td><td headers="r7c1-t2 r1c3-t2 r2c5-t2"><p>X</p></td><td headers="r7c1-t2 r1c3-t2"></td><td headers="r7c1-t2 r1c3-t2"><p>X</p></td><td headers="r7c1-t2"></td></tr><tr><td headers="r1c1-t2 r2c1-t2"><p><code>SYSTEM</code></p></td><td headers="r8c1-t2 r1c2-t2 r2c2-t2"></td><td headers="r8c1-t2 r1c3-t2 r2c3-t2"></td><td headers="r8c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"></td><td headers="r8c1-t2 r1c3-t2 r2c5-t2"></td><td headers="r8c1-t2 r1c3-t2"><p>EBS patching</p></td><td headers="r8c1-t2 r1c3-t2"></td><td headers="r8c1-t2"></td></tr><tr><td headers="r1c1-t2 r2c1-t2"><p><code>RMAN</code></p></td><td headers="r9c1-t2 r1c2-t2 r2c2-t2"></td><td headers="r9c1-t2 r1c3-t2 r2c3-t2"><p>X</p></td><td headers="r9c1-t2 r1c3-t2 r1c4-t2 r2c4-t2"><p>X</p></td><td headers="r9c1-t2 r1c3-t2 r2c5-t2"></td><td headers="r9c1-t2 r1c3-t2"></td><td headers="r9c1-t2 r1c3-t2"></td><td headers="r9c1-t2"></td></tr></tbody></table>

In some cases, system management tasks may require temporary access to data through specific tools and programs. When this happens, build provisions for this temporary or emergency access into the Oracle Database Vault rules and rule sets.

### Identifying and Documenting the Tasks of Users Who Access the Database System

You should document the following areas of the tasks your organization needs:

- The responsibilities of each administrative user
- The kind of access users need. For example, application owners should have data access and developers need access to development instances only.
- Who must manage the system without accessing business data (for example, users who perform backup, patching, tuning, and monitoring operations)
- The duties of each category of tasks (for example, the files that must be backed up, the applications that require patching, what exactly is monitored). Include the alternate user accounts for each of these tasks.
- The databases and applications that must be protected. This includes Oracle applications, partner applications, and custom applications.
- Who must be authorized to access business data, including the following:
	- Application owners through middle tier processes
		- Business users through an application interface
- Emergency "what if" scenarios, such as how to handle a security breach
- Reporting in a production environment, which should include the following:
	- Who runs the reports
		- Which reports must be run
		- The frequency with which each report is run
		- The users who must receive a copy of each report
- In addition to a separation of duty matrix, the creation of the following matrices:
	- An Oracle Database Vault-specific matrix, which can cover the names and tasks of users who have been granted Database Vault roles
		- An application protection matrix, which can cover the applications to be protected and the types of protections you have put in place.
	Table D-2 shows an example of protections Oracle created for PeopleSoft Applications. You can download the scripts to create these security policies from the following URL:
	`http://www.oracle.com/technetwork/database/options/database-vault/index-085211.html`
	Table D-2 Example Application Protection Maxtrix
	<table><thead><tr><th rowspan="2">Protection Type</th><th colspan="4">Authorized with Rule Set</th></tr><tr><th headers="r1c1-t3 r1c1-t3">SYSADM</th><th headers="r1c1-t3 r2c1-t3 r1c2-t3">PSFTDBA</th><th headers="r1c1-t3 r2c1-t3 r1c2-t3">SYSTEM</th><th headers="r1c1-t3 r2c1-t3 r1c2-t3">DBA</th></tr></thead><tbody><tr><td headers="r1c1-t3 r2c1-t3"><p>PeopleSoft Realm</p></td><td headers="r3c1-t3 r1c2-t3 r2c2-t3"><p>Owner</p></td><td headers="r3c1-t3 r1c2-t3 r2c3-t3"><p>Owner</p></td><td headers="r3c1-t3 r1c2-t3 r2c4-t3"><p>No Access</p></td><td headers="r3c1-t3 r1c2-t3"><p>No Access</p></td></tr><tr><td headers="r1c1-t3 r2c1-t3"><p>SELECT Command Rule</p></td><td headers="r4c1-t3 r1c2-t3 r2c2-t3"><p>Not Restricted</p></td><td headers="r4c1-t3 r1c2-t3 r2c3-t3"><p>Limit PSFTDB Rule Set</p></td><td headers="r4c1-t3 r1c2-t3 r2c4-t3"><p>No Access</p></td><td headers="r4c1-t3 r1c2-t3"><p>No Access</p></td></tr><tr><td headers="r1c1-t3 r2c1-t3"><p>CONNECT Command Rule</p></td><td headers="r5c1-t3 r1c2-t3 r2c2-t3"><p>PeopleSoftAccess Rule Set</p></td><td headers="r5c1-t3 r1c2-t3 r2c3-t3"><p>Not Restricted</p></td><td headers="r5c1-t3 r1c2-t3 r2c4-t3"><p>Not Restricted</p></td><td headers="r5c1-t3 r1c2-t3"><p>Not Restricted</p></td></tr><tr><td headers="r1c1-t3 r2c1-t3"><p>DROP TABLESPACE Command Rule</p></td><td headers="r6c1-t3 r1c2-t3 r2c2-t3"><p>Disabled Rule Set</p></td><td headers="r6c1-t3 r1c2-t3 r2c3-t3"><p>Disabled Rule Set</p></td><td headers="r6c1-t3 r1c2-t3 r2c4-t3"><p>Disabled Rule Set</p></td><td headers="r6c1-t3 r1c2-t3"><p>Disabled Rule Set</p></td></tr></tbody></table>

## Managing Oracle Database Administrative Accounts

This section contains:

- Using the SYSTEM User Account for General Administrative Uses
- Using the SYSTEM Schema for Application Tables
- Limiting the SYSDBA Administrative Privilege
- Managing Root and Operating System Access

### Using the SYSTEM User Account for General Administrative Uses

If you use the `SYSTEM` account for general database administrative purposes, create named database administrative accounts for your database administrators. Doing so increases accountability for administrative actions in the database.

### Using the SYSTEM Schema for Application Tables

If your site holds application tables in the `SYSTEM` schema, then you should add the `SYSTEM` account to your realm authorizations for these tables so that these applications can continue to work normally. You can place restrictions on the `SYSTEM` account to increase or fine-tune security for these applications. For example, you can create a Database Vault rule set to restrict the `SYSTEM` user's access to specific IP addresses.

### Limiting the SYSDBA Administrative Privilege

Limit the `SYSDBA` privilege only to users who must connect using this privilege when absolutely necessary and for applications that still require `SYSDBA` access, such as Oracle Recovery Manager (RMAN) and mandatory patching processes. For all other cases, create named database accounts to perform daily database administration. Members of the `OSDBA` user group are also given the `SYSDBA` administrative privilege.

### Managing Root and Operating System Access

Oracle Database Vault prevents highly privileged database users from accessing sensitive data. In addition, if you are using Oracle Database itself, you can use transparent data encryption to prevent the most highly privileged operating system users from accessing sensitive data. Transparent data encryption enables you to hide individual table columns. (See [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information about transparent data encryption.) As a best practice, always carefully review and restrict direct access to the operating system.

You should have personalized accounts access the operating system. These personalized accounts should, in the Linux or UNIX environments, login using `sudo` to the `oracle` software owner when needed. With `sudo`, you can control which specific command each personalized user can execute. Be sure to prevent the use of the `make`, `relink`, `gdb`, or other commands that could potentially harm the database, for these users. However, if an administrative user must install a patch or perform some other emergency operation, you can enable the `make` and `relink` commands for a limited time, and audit their actions during this period.

## Accounts and Roles Trusted by Oracle Database Vault

Oracle Database Vault restricts access to application data from many privileged users and roles in the database. However, in some cases, Oracle Database Vaults trusts certain roles and privileges.

Table D-3 lists the trusted roles and privileges that are created when you install Oracle Database Vault.

Table D-3 Trusted Oracle Database Vault Roles and Privileges

| Role or Privilege | Status | Description |
| --- | --- | --- |
| `DV_ACCTMGR` role | Open | Role created during installation and used for creating new database accounts |
| `DV_OWNER` role | Open | Role created during installation and used for managing realms, factors and command rules. This user can add himself or herself to realm authorizations. Users who have the `DV_ACCTMGR` role cannot alter this user. |
| `SYSDBA` privilege | Enabled | Privilege created during Oracle Database installation. Required by some Oracle features. See "Managing SYSDBA Access" for guidelines on managing `SYSDBA`. |
| `SYSOPER` privilege | Enabled | Privilege created during Oracle Database installation. Database startup and shutdown. Granted to `SYS` only by default. See "Managing SYSOPER Access" for guidelines on managing `SYSOPER`. |

## Accounts and Roles That Should be Limited to Trusted Individuals

Several accounts and roles have very powerful privileges in a default Oracle Database installation. You should limit these accounts and roles only to trusted individuals.

- Managing Users with Root Access to the Operating System
- Managing the Oracle Software Owner
- Managing SYSDBA Access
- Managing SYSOPER Access

### Managing Users with Root Access to the Operating System

Users who have root user access have full control over the system, including the following activities:

- Reading unencrypted files
- Moving and deleting any files
- Starting or stopping any program on the system
- Logging in as any user, including the user who owns the Oracle Database installation

Oracle Database Vault does not provide protection against the operating system root access. Ensure that you grant root user privileges only to the appropriate people with the appropriate responsibility.

### Managing the Oracle Software Owner

Users who have access to a system as the Oracle software owner have control over the Oracle software, including the following activities:

- Reading unencrypted database files
- Moving and deleting database files
- Starting or stopping Oracle programs in the system

Oracle Database Vault does not provide protection against the operating system access of the Oracle software owner. Ensure that you grant Oracle software owner access only to the appropriate people with the appropriate responsibility.

### Managing SYSDBA Access

By default, Oracle Database limits `SYSDBA` access to administrative users in the `OSDBA` group and to the user `SYS`. The `SYSDBA` privilege is a trusted privilege in Oracle Database Vault. Grant this privilege to trusted users only.

### Managing SYSOPER Access

By default, Oracle Database limits `SYSOPER` access to operating system users in the `OSOPER` group and to the user `SYS`. It prevents `SYSOPER` from modifying the Oracle data dictionary directly. The `SYSOPER` privilege has limited privileges within the database, but individuals with this role can start and shut down the Oracle database. Only grant the `SYSOPER` privilege to trusted individuals.

## Guidelines for Using Oracle Database Vault in a Production Environment

Follow these guidelines when running Oracle Database Vault in a production environment:

- Run a full test of your applications to ensure that the Database Vault policies you have created are working as expected
- Monitor the performance of your applications, and if necessary, tune your rule expressions
- Assign responsibilities to the appropriate production support and security groups, as follows:
	- Assign security responsibilities to the database security administrator.
		- Assign account management to the database account manager.
		- Assign resource management tasks to database administrators.
- Back up your Database Vault API scripts to a secure server.

## Secure Configuration Guidelines

Follow these configuration and security guidelines:

- Security Considerations for the UTL\_FILE and DBMS\_FILE\_TRANSFER Packages
- Security Considerations for the Recycle Bin
- Security Considerations for the CREATE ANY JOB Privilege
- Security Considerations for the CREATE EXTERNAL JOB Privilege
- Security Considerations for the LogMiner Packages
- Security Considerations for the ALTER SYSTEM and ALTER SESSION Privileges

Note:

- Installing patches and new applications might re-grant some of the privileges that Oracle recommends that you revoke in this section. Check these privileges after you install patches and new applications to verify that they are still revoked.
- When you revoke `EXECUTE` privileges on packages, ensure that you grant `EXECUTE` on the packages to the owner, check the package dependencies, and recompile any invalid packages after the revoke.
	To find users who have access to the package, log in to SQL\*Plus as `SYSTEM` and issue the following query.
	```
	SELECT * FROM DBA_TAB_PRIVS WHERE TABLE_NAME = package_name;
	```
	`package_name` is the name of the package you are looking for.
	To find the users, packages, procedures, and functions that are dependent on the package, issue this query:
	```
	SELECT OWNER, NAME, TYPE  FROM ALL_DEPENDENCIES 
	WHERE REFERENCED_NAME = package_name;
	```
	Note that these two queries do not identify references to packages made through dynamic SQL.

### Security Considerations for the UTL\_FILE and DBMS\_FILE\_TRANSFER Packages

The `UTL_FILE` package is owned by `SYS` and granted to `PUBLIC`. However, a user must have access to the directory object to manipulate the files in that operating system directory. You can configure the `UTL_FILE` package securely; see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/u_file.htm#ARPLS069) for more information.

The `DBMS_FILE_TRANSFER` package is owned by `SYS` and granted to the `EXECUTE_CATALOG_ROLE`. Users with `EXECUTE` access on this package can move files from one location to another on the same file system. They also can move files between database instances, including databases on remote systems.

To secure the `DBMS_FILE_TRANSFER` package, do the following:

- Revoke the `EXECUTE` privilege from the `DBMS_FILE_TRANSFER` package and grant the `EXECUTE` privilege only to trusted users who need it.
- Create command rules to control the `CREATE DATABASE LINK` and `CREATE DIRECTORY` SQL statements. See ["Creating and Editing a Command Rule"](cfcmdaut.md) for information on creating command rules by using Oracle Database Vault Administrator.

Alternatively, Example D-1 and Example D-2 show how you can use the Oracle Database Vault `DBMS_MACADM` package to create command rules that limit and enable access to the `CREATE DATABASE LINK` statement, which is used to establish connections to remote databases. To use this method, log in to SQL\*Plus using the Oracle Database Vault Owner account.

Example D-1 Creating a Command Rule to Deny Access to CREATE DATABASE LINK

```
BEGIN 
 DBMS_MACADM.CREATE_COMMAND_RULE (
  command       => 'CREATE DATABASE LINK', 
  rule_set_name => 'Disabled', 
  object_owner  => '%', 
  object_name   => '%', 
  enabled       => DBMS_MACUTL.G_YES); 
  END; 
  / 
COMMIT;
```

When a valid user must use the `CREATE DATABASE LINK` statement, the Oracle Database Vault owner can reenable it from Oracle Database Vault Administrator or issue the following commands in SQL\*Plus.

Example D-2 Creating a Command Rule to Enable Access to CREATE DATABASE LINK

```
BEGIN 
 DBMS_MACADM.UPDATE_COMMAND_RULE (
  command       => 'CREATE DATABASE LINK', 
  rule_set_name => 'Enabled', 
  object_owner  => '%', 
  object_name   => '%', 
  enabled       => DBMS_MACUTL.G_YES); 
 END; 
 /  
COMMIT;
```

Similarly, Example D-3 shows command rules that disable and enable access to `CREATE DIRECTORY`.

Example D-3 Command Rules to Disable and Enable Access to CREATE DIRECTORY

```
-- Disable access to CREATE DIRECTORY
BEGIN
 DBMS_MACADM.CREATE_COMMAND_RULE (
  command       => 'CREATE DIRECTORY', 
  rule_set_name => 'Disabled', 
  object_owner  => '%', 
  object_name   => '%', 
  enabled       => dbms_macutl.g_yes); 
 END; 
  / 
COMMIT;

-- Enable access to CREATE DIRECTORY
BEGIN 
 dbms_macadm.update_command_rule (
  command       => 'CREATE DIRECTORY', 
  rule_set_name => 'Enabled', 
  object_owner  => '%', 
  object_name   => '%', 
  enabled       => dbms_macutl.g_yes); 
 END; 
 /
COMMIT;
```

### Security Considerations for the Recycle Bin

In Oracle Database Vault, the `ALTER SYSTEM` command rule prevents the recycle bin feature from being enabled, but if the recycle bin is already enabled, it cannot prevent you from disabling it. When the recycle bin feature is enabled, realm-protected objects that are dropped go into the recycle bin. Once there, the objects are no longer protected by the realm. The exception is objects in the `DVSYS` schema: To keep `DVSYS` as a protected schema, you cannot drop its objects, even if the recycle bin is disabled. For better security for other realms, you should disable the recycle bin.

In SQL\*Plus, you can check the contents of the recycle bin as follows:

```
SELECT * FROM RECYCLEBIN;
SELECT * FROM USER_RECYCLEBIN;
```

To purge the contents of the recycle bin, use the `PURGE` SQL statement:

```
PURGE RECYCLEBIN;
PURGE USER_RECYCLEBIN;
```

To disable the recycle bin:

1. Log in to SQL\*Plus as `SYS` using the `SYSDBA` privilege.
	```
	sqlplus sys as sysdba
	Enter password: password
	```
2. Ensure that the recycle bin is disabled.
	```
	SHOW PARAMETER RECYCLEBIN
	```
3. If the recycle bin is on, then disable it.
	```
	ALTER SYSTEM SET RECYCLEBIN=OFF SCOPE=SPFILE;
	```
4. Restart Oracle Database.
	```
	SHUTDOWN IMMEDIATE
	STARTUP
	```

### Security Considerations for the CREATE ANY JOB Privilege

The `CREATE ANY JOB` privilege has been revoked from the `DBA` and the `SCHEDULER_ADMIN` roles. Ensure that this change does not affect your applications.

See ["Scheduling Database Jobs in an Oracle Database Vault Environment"](dba.md) for more information.

### Security Considerations for the CREATE EXTERNAL JOB Privilege

The `CREATE EXTERNAL JOB` privilege was introduced in Oracle Database 10g Release 2 (10.2). It is required for database users who want to execute jobs that run on the operating system outside the database. By default, this privilege is granted to all users who have been granted the `CREATE JOB` privilege. For greater security, revoke this privilege from users who do not need it and then grant it only to those users who do need it.

### Security Considerations for the LogMiner Packages

In this release of Oracle Database Vault, the role `EXECUTE_CATALOG_ROLE` no longer has the `EXECUTE` privilege granted by default on the following LogMiner packages:

- `DBMS_LOGMNR`
- `DBMS_LOGMNR_D`
- `DBMS_LOGMNR_LOGREP_DICT`
- `DBMS_LOGMNR_SESSION`

Ensure that this change does not affect your applications.

### Security Considerations for the ALTER SYSTEM and ALTER SESSION Privileges

Be aware that trace and debug commands have the potential to show Oracle database memory information. Oracle Database Vault does not protect against these commands. To help secure the Oracle database memory information, Oracle recommends that you strictly control access to the `ALTER SYSTEM` and `ALTER SESSION` privileges. These privileges can be granted by the user `SYS` when connected as `SYSDBA` and by any user granted the `DBA` role.

Oracle also recommends that you add rules to the existing command rule for `ALTER SYSTEM` statement. You can use Oracle Database Vault Administrator to create a rule and add it to a rule set. You should grant the `ALTER SESSION` privilege only to trusted users. (For example, the `ALTER SESSION` statement can enable tracing.)

Example D-4 shows how you can create this type of rule. This rule prevent users with `ALTER SYSTEM` privilege from issuing the command `ALTER SYSTEM DUMP`. Log in to SQL\*Plus as the Oracle Database Vault Owner when you create this command rule.

Example D-4 Adding Rules to the Existing ALTER SYSTEM Command Rule

```
CONNECT amalcolm_dvacctmgr
Enter password: password

BEGIN
 DBMS_MACADM.CREATE_RULE('NO_SYSTEM_DUMP',
 '(INSTR(UPPER(DVSYS.DV_SQL_TEXT),''DUMP'') = 0)');
 END;
/
EXEC DBMS_MACADM.ADD_RULE_TO_RULE_SET
  ('Allow Fine Grained Control of System Parameters','NO_SYSTEM_DUMP');

COMMIT;
```

Alternatively, you can use Oracle Database Vault Administrator to create and add this rule to the rule set. See ["Creating a Rule to Add to a Rule Set"](cfrulset.md) for more information.