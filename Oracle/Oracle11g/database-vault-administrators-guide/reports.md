---
title: Oracle Database Vault Reports
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/reports.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## 18 Oracle Database Vault Reports

This chapter contains:

See Also:

["Using Oracle Database Vault-Specific Reports in Enterprise Manager Grid Control"](dba.md)

## Categories of Oracle Database Vault Reports

Oracle Database Vault provides a selection of reports that display security-related information from the database. These reports also show custom Oracle Database Vault audit event information. The reports are in two categories:

- Database Vault Reports. These reports allow you to check configuration issues with realms, command rules, factors, factor identities, rule sets, and secure application roles. These reports also reveal realm violations, auditing results, and so on.
- General Security Reports. These reports allow you to check the status of object privileges, database account system privileges, sensitive objects, privilege management, powerful database accounts and roles, initialization parameters, profiles, account passwords, security audits, and other security vulnerability reports.

## Who Can Run the Oracle Database Vault Reports?

You must log on using an account that has the `DV_OWNER`, `DV_ADMIN`, or `DV_SECANALYST` role before you can run the Oracle Database Vault reports. For more information about these roles, see the following sections:

- ["DV\_OWNER Database Vault Owner Role"](db_objects.md)
- ["DV\_ADMIN Database Vault Configuration Administrator Role"](db_objects.md)
- ["DV\_SECANALYST Database Vault Security Analyst Role"](db_objects.md)

## How to Run Oracle Database Vault Reports

To run Oracle Database Vault reports:

1. Log in to Database Vault Administrator as a user who has been granted the `DV_OWNER`, `DV_ADMIN`, or `DV_SECANALYST` role.
	["Starting Oracle Database Vault"](getting_started.md) explains how to log in.
2. Select either Database Vault Reports or General Security Reports.
	These report categories are described in the following sections:
	- "Generating Oracle Database Vault Reports"
		- "Generating General Security Reports"
3. Select a report and click Run Report to run the report.
	You can run many of the reports without any input parameters. For example, if you select the Audit Privileges Report, and click Run Report, then you can immediately see the report results. However, some of the available reports require at least one input parameter before the results can be displayed.
	The Report Results page displays the report content in a tabular fashion with the column headings shown at the top of the report. The page displays the report title and the date and time when the report was run. Click Return to Reports Menu to return to the Reports page, so that you can select and run a different report if you want.
	Some of the reports require at least one input parameter to be provided before they can be run. For example, when you select Object Dependencies Report and click Run Report, the Report Parameters page is displayed. The Owner box enables you to select the database account that owns the object. The Object Name field specifies the name of the object. You can use wildcard characters like the percentage sign (%), which defaults to all object names. The Result Set Size parameter determines the maximum number of result rows that are displayed. If you want all records to be displayed, then select All.The parameters that you enter on this page are passed directly to the SQL query that generates the report results. Click Run Report to display the report results based on the specified parameters.

## Generating Oracle Database Vault Reports

To generate Oracle Database Vault reports, click the Database Vault Reports tab, and then select from the following categories of reports:

- Oracle Database Vault Configuration Issues Reports
- Oracle Database Vault Auditing Reports

### Oracle Database Vault Configuration Issues Reports

The configuration issues reports are:

- Command Rule Configuration Issues Report
- Factor Configuration Issues Report
- Factor Without Identities Report
- Identity Configuration Issues Report
- Realm Authorization Configuration Issues Report
- Rule Set Configuration Issues Report
- Secure Application Configuration Issues Report

#### Command Rule Configuration Issues Report

The Command Rule Configuration Issues Report displays command rules for which the following configuration issues exist:

- Rule set for the command rule is disabled.
- Rule set for the command rule is incomplete.
- Object owner for the command rule does not exist. This can happen when the user account for the object has been dropped.

#### Factor Configuration Issues Report

The Factor Configuration Issues Report displays Oracle Database Vault factors for which the following configuration issues exist:

- Rule set for factor assignment is disabled.
- Rule set for factor assignment is incomplete.
- Audit options for the factor are invalid.
- No factor retrieval method or constant exists.
- No subfactors (that is, child factors) are linked to a factor identity.
- No subfactors (child factors) are linked to a label factor.
- Oracle Label Security policy does not exist for the factor.

#### Factor Without Identities Report

The Factor Without Identities Report displays Oracle Database Vault factors that have no identities defined in the access control configuration. For some factors such as `Background_Job_Id`, this may not be a real problem, but the report can help you determine whether your access control configuration is complete and whether you have accounted for all factor configuration.

#### Identity Configuration Issues Report

The Identity Configuration Issues Report displays Oracle Database Vault factor identities where the following configuration issues exist:

- Label identity for the Oracle Label Security label for this identity has been removed and no longer exists.
- No map exists for the identity.

#### Realm Authorization Configuration Issues Report

The Realm Authorization Configuration Issues Report displays Oracle Database Vault realm information where the following configuration issues exist.

- Rule set for a realm authorization is disabled.
- Grantee does not exist for a realm authorization.
- Owner does not exist for a realm-secured object. This can happen when the user account has been dropped.

In most cases, however, these types of issues are caught when you configure the realm and during validation.

#### Rule Set Configuration Issues Report

The Rule Set Configuration Issues Report displays Oracle Database Vault rule set information when no rules are defined or enabled for a rule set.

#### Secure Application Configuration Issues Report

The Secure Application Configuration Issues Report displays Database Vault secure application role information where the following configuration issues exist:

- The database role does not exist. This can happen when the database role has been dropped.
- The rule set for role is disabled.
- The rule set for role is incomplete.

### Oracle Database Vault Auditing Reports

The auditing reports are:

- Realm Audit Report
- Command Rule Audit Report
- Factor Audit Report
- Label Security Integration Audit Report
- Core Database Vault Audit Trail Report
- Secure Application Role Audit Report

#### Realm Audit Report

The Realm Audit Report shows audit records generated by the realm protection and realm authorization operations. You can manage realm authorizations by using rule sets, and then audit the rule set processing results. A realm violation occurs when the database account, performing an action on a realm-protected object, is not authorized to perform that action. Oracle Database Vault audits the violation even if you do not specify any rule sets attached to the realm. When you configure a realm, you can set it to audit instances of realm violations. You can use this information to investigate attempts to break security.

#### Command Rule Audit Report

The Command Rule Audit Report shows audit records generated by command rule processing operations. When you configure a command rule, you can set it to audit the rule set processing results.

#### Factor Audit Report

The Factor Audit Report shows factors that failed to evaluate or were set to create audit records under various conditions. It also shows failed attempts to set factors.

You can audit instances where a factor identity cannot be resolved and assigned (such as No data found or Too many rows). A factor can have an associated rule set that assigns an identity to the factor at run time. When you configure a factor, you can set it to audit the rule set processing results.

#### Label Security Integration Audit Report

The Label Security Integration Audit Report shows audit records generated by the session initialization operation and the session label assignment operation of label security. You can audit instances where the label security session fails to initialize, and where the label security component prevents a session from setting a label that exceeds the maximum session label.

#### Core Database Vault Audit Trail Report

The Core Database Vault Audit Trail Report shows audit records generated by the core access security session initialization operation. You can audit instances where the access security session fails to initialize. It displays the following data:

| Violation Attempt | Instance Number |
| --- | --- |
| Timestamp | Object Name |
| Return Code | Rule Set |
| Account | Command |
| User Host |  |

#### Secure Application Role Audit Report

The Secure Application Role Audit Report shows the audit records generated by the secure application role-enabling operation for Oracle Database Vault.

## Generating General Security Reports

To generate general security reports, click the General Security Reports tab, and then select from the following reports:

- Object Privilege Reports
- Database Account System Privileges Reports
- Sensitive Objects Reports
- Privilege Management - Summary Reports
- Powerful Database Accounts and Roles Reports
- Initialization Parameters and Profiles Reports
- Database Account Password Reports
- Security Audit Report: Core Database Audit Report
- Other Security Vulnerability Reports

### Object Privilege Reports

The object privilege reports are:

- Object Access By PUBLIC Report
- Object Access Not By PUBLIC Report
- Direct Object Privileges Report
- Object Dependencies Report

#### Object Access By PUBLIC Report

The Object Access By PUBLIC Report lists all objects whose access has been granted to `PUBLIC`. It details all the object access the database accounts that you specify on the Report Parameters page, through object grants to `PUBLIC`. On the Reports Parameters page, you can filter the results based on the privilege, the object owner, or the object name.

Note:

This report can be quite large if you choose the defaults.

#### Object Access Not By PUBLIC Report

The Object Access Not By PUBLIC Report describes all the object access the database accounts that you specify on the Report Parameters page, through grants to the account directly or through a role, but excluding the grants to `PUBLIC`. On the Reports Parameters page, you can filter the results based on the privilege, the object owner or the object name.

Note:

This report can be quite large if you choose the defaults.

#### Direct Object Privileges Report

The Direct Object Privileges Report shows the direct object privileges granted to nonsystem database accounts. The following database accounts are excluded from the report:

| `CTXSYS` | `LBACSYS` | `SYS` | `WMSYS` |
| --- | --- | --- | --- |
| `DMSYS` | `MDSYS` | `SYSMAN` |  |
| `DVSYS` | `ORDSYS` | `SYSTEM` |  |
| `EXFSYS` | `PUBLIC` | `WKSYS` |  |

#### Object Dependencies Report

The Object Dependencies Report describes all dependencies in the database between procedures, packages, functions, package bodies, and triggers, including dependencies on views created without any database links. It can help you develop a security policy using the principle of least privilege for existing applications. If a database object, such as a `UTL_FILE` package, has privileges granted to `PUBLIC` or some other global role, then you can use the Object Dependencies Report to determine an account that may depend on the object and to determine how the account uses the object. To run the report, enter the database account you are inspecting for dependency and the object it may be dependent on, in the Report Parameters page.

The Report Results page shows the dependent object and object type and the source object name and type. This report shows where the potentially sensitive object is being used. By looking at several accounts, you might be able to see patterns that can help you develop restricted roles. These restricted roles can replace `PUBLIC` grants on widely used sensitive objects.

### Database Account System Privileges Reports

The database account system privileges reports are:

- Direct System Privileges By Database Account Report
- Direct and Indirect System Privileges By Database Account Report
- Hierarchical System Privileges by Database Account Report
- ANY System Privileges for Database Accounts Report
- System Privileges By Privilege Report

#### Direct System Privileges By Database Account Report

The Direct System Privileges By Database Account Report displays all system privileges that have been directly granted to the database account selected on the Report Parameters page. It also shows whether a privilege has been granted the `WITH ADMIN` option.

#### Direct and Indirect System Privileges By Database Account Report

The Direct and Indirect System Privileges By Database Account Report displays all the system privileges for the database account selected on the Report Parameters page. The system privileges may have been granted directly or granted through a database role that has the `WITH ADMIN` status.

#### Hierarchical System Privileges by Database Account Report

The Hierarchical System Privileges by Database Account Report displays a hierarchical breakdown of role-based system privileges and direct system privileges granted to the database account specified on the Report Parameters page.

#### ANY System Privileges for Database Accounts Report

The ANY System Privileges for Database Accounts Report shows all `ANY` system privileges granted to the specified database account or role. `ANY` system privileges are very powerful and should be judiciously assigned to accounts and roles.

#### System Privileges By Privilege Report

The System Privileges By Privilege Report displays the database accounts and roles that have the system privilege selected on the Report Parameters page.

### Sensitive Objects Reports

The sensitive objects reports are:

- Execute Privileges to Strong SYS Packages Report
- Access to Sensitive Objects Report
- Public Execute Privilege To SYS PL/SQL Procedures Report
- Accounts with SYSDBA/SYSOPER Privilege Report

#### Execute Privileges to Strong SYS Packages Report

The Execute Privileges to Strong SYS Packages Report shows the database accounts and roles that have the `EXECUTE` privilege on system packages that can be used to access operating system resources or other powerful system packages. The following system PL/SQL packages are included:

| `DBMS_ALERT` | `DBMS_RANDOM` |
| --- | --- |
| `DBMS_BACKUP_RESTORE` | `DBMS_REPAIR` |
| `DBMS_CAPTURE_ADM` | `DBMS_REPCAT` |
| `DBMS_DDL` | `DBMS_REPCAT_ADMIN` |
| `DBMS_DISTRIBUTED_TRUST_ADMIN` | `DBMS_RESOURCE_MANAGER` |
| `DBMS_FGA` | `DBMS_RESOURCE_MANAGER_PRIVS` |
| `DBMS_JOB` | `DBMS_RLS` |
| `DBMS_LDAP` | `DBMS_SESSION` |
| `DBMS_LOB` | `DEBUG_EXTPROC` |
| `DBMS_LOGMNR` | `UTL_FILE` |
| `DBMS_LOGMNR_D` | `UTL_HTTP` |
| `DBMS_OBFUSCATION_TOOLKIT` | `UTL_SMTP` |
| `DBMS_ORACLE_TRACE_AGENT` | `UTL_TCP` |
| `DBMS_PIPE` |  |

#### Access to Sensitive Objects Report

The Access to Sensitive Objects Report shows the database accounts and roles that have object privileges on system tables or views that contain sensitive information. It includes the following system tables and views:

| `ALL_SOURCE` | `PROFILE$` |
| --- | --- |
| `ALL_USERS` | `PROXY_ROLE_DATA$` |
| `APPROLE$` | `PROXY_ROLE_INFO$` |
| `AUD$` | `ROLE_ROLE_PRIVS` |
| `AUDIT_TRAIL$` | `SOURCE$` |
| `DBA_ROLE_PRIVS` | `STATS$SQLTEXT` |
| `DBA_ROLES` | `STATS$SQL_SUMMARY` |
| `DBA_TAB_PRIVS` | `STREAMS$_PRIVILEGED_USER` |
| `DBMS_BACKUP_RESTORE` | `SYSTEM_PRIVILEGE_MAP` |
| `DEFROLE$` | `TABLE_PRIVILEGE_MAP` |
| `FGA_LOG$` | `TRIGGER$` |
| `LINK$` | `USER$` |
| `OBJ$` | `USER_HISTORY$` |
| `OBJAUTH$` | `USER_TAB_PRIVS` |
| `OBJPRIV$` | `SYSTEM_PRIVILEGE_MAP` |

#### Public Execute Privilege To SYS PL/SQL Procedures Report

The Public Execute Privilege to SYS PL/SQL Procedures Report shows all database accounts and roles that have execute privileges on packages owned by `SYS`. This can be used to determine which privileges can be revoked from `PUBLIC`, or from other accounts and roles. This reduces vulnerabilities as part of an overall security policy implementation using the principle of least privilege.

#### Accounts with SYSDBA/SYSOPER Privilege Report

The Accounts with SYSDBA/SYSOPER Privilege Report displays database accounts that have `SYS` -privileged connection privileges. It also shows whether the accounts use an external password. However, note that this report does not include operating system users who can become `SYSDBA`.

### Privilege Management - Summary Reports

The privilege management summary reports are:

- Privileges Distribution By Grantee Report
- Privileges Distribution By Grantee, Owner Report
- Privileges Distribution By Grantee, Owner, Privilege Report

See Also:

["DVSYS.DBA\_DV\_PUB\_PRIVS View"](views.md) to find the values on which the counts listed in these reports are based

#### Privileges Distribution By Grantee Report

The Privileges Distribution By Grantee Report displays the count of privileges granted to a database account or role. This provides insight into accounts and roles that may have powerful privileges.

#### Privileges Distribution By Grantee, Owner Report

The Privileges Distribution By Grantee, Owner Report displays a count of privileges based on the grantee and the owner of the object. This provides insight into accounts or roles that may have powerful privileges. You can use this report if you suspect potential intruders or insider threats are looking for accounts that have powerful privileges as accounts to attack or compromise. If intruders can compromise the account (for example, by guessing the password), they can get more privileges than they already have.

#### Privileges Distribution By Grantee, Owner, Privilege Report

The Privileges Distribution By Grantee, Owner, Privilege Report displays a count of privileges based on the privilege, the grantee, and the owner of the object. This provides insight into the accounts or roles that may have powerful privileges.

### Powerful Database Accounts and Roles Reports

The powerful database accounts and roles reports are:

- WITH ADMIN Privilege Grants Report
- Accounts With DBA Roles Report
- Security Policy Exemption Report
- BECOME USER Report
- ALTER SYSTEM or ALTER SESSION Report
- Password History Access Report
- WITH GRANT Privileges Report
- Roles/Accounts That Have a Given Role Report
- Database Accounts With Catalog Roles Report
- AUDIT Privileges Report
- OS Security Vulnerability Privileges Report

#### WITH ADMIN Privilege Grants Report

The WITH ADMIN Privileges Grants Report shows all database accounts and roles that have been granted privileges with the `WITH ADMIN` clause. This privilege can be misused to give another account more system privileges than required.

#### Accounts With DBA Roles Report

The Accounts With DBA Roles Report shows all database accounts that have the `DBA` role granted to them. The `DBA` role is a privileged role that can be misused. It is often granted to a database account to save time and to avoid having to determine the least number of privileges an account really needs. This report can help you to start applying a policy using the principle of least privilege to an existing database.

For guidelines on deciding who should have privileged roles, see [Appendix D, "Oracle Database Vault Security Guidelines."](guidelines.md)

#### Security Policy Exemption Report

The Security Policy Exemption Report shows database (but not Oracle Database Vault) accounts and roles that have the `EXEMPT ACCESS POLICY` system privilege granted to them. Accounts that have this privilege can bypass all Virtual Private Database (VPD) policy filters and any Oracle Label Security policies that use Oracle Virtual Private Database indirectly. This is a powerful system privilege that should be granted only if absolutely necessary, as it presents a target to gain access to sensitive information in tables that are protected by Oracle Virtual Private Database or Oracle Label Security. You can use the auditing policies described in [Appendix A, "Auditing Oracle Database Vault,"](audplcy.md) to audit the use of this privilege.

#### BECOME USER Report

The BECOME USER Report shows all database accounts roles that have the `BECOME USER` system privilege. This is a very powerful system privilege: it enables the `IMP_FULL_DATABASE` and `EXP_FULL_DATABASE` roles for use with Oracle Data Pump. Accounts that possess this privilege can be misused to get sensitive information or to compromise an application.

#### ALTER SYSTEM or ALTER SESSION Report

The ALTER SYSTEM or ALTER SESSION Report shows all database accounts and roles that have the `ALTER SYSTEM` or `ALTER SESSION` privilege. Oracle recommends that you restrict these privileges only to those accounts and roles that truly need them (for example, the `SYS` account and the `DV_ADMIN` role). The `ALTER SYSTEM` statement can be used to change the security-related database initialization parameters that are set to recommended values as part of the Oracle Database Vault security strengthening service. Both the `ALTER SYSTEM` and `ALTER SESSION` statements can be used to dump database trace files, potentially containing sensitive configuration information, to the operating system.

For guidelines on using the `ALTER SYSTEM` and `ALTER SESSION` privileges, see ["Security Considerations for the ALTER SYSTEM and ALTER SESSION Privileges"](guidelines.md).

#### Password History Access Report

The Password History Access Report shows database accounts that have access to the `USER_HISTORY$` table that stores hashed passwords that were previously used by each account. Access to this table can make guessing the existing password for an account easier for someone hacking the database.

#### WITH GRANT Privileges Report

The WITH GRANT Privileges Report shows all database accounts that have been granted privileges with the `WITH GRANT` clause. Remember that `WITH GRANT` is used for object-level privileges: An account that has been granted privileges using the `WITH GRANT` option can be misused to grant object privileges to another account.

#### Roles/Accounts That Have a Given Role Report

This report displays the database accounts and roles to which a role has been granted. This report is provided for dependency analysis.

#### Database Accounts With Catalog Roles Report

The Database Accounts With Catalog Roles Report displays all database accounts and roles that have the following roles granted to them:

- `DELETE_CATALOG_ROLE`
- `EXECUTE_CATALOG_ROLE`
- `RECOVERY_CATALOG_OWNER`
- `SELECT_CATALOG_ROLE`

These catalog-based roles have a very large number of powerful privileges. They should be granted with caution, much like the `DBA` role, which uses them.

#### AUDIT Privileges Report

The AUDIT Privileges Report displays all database accounts and roles that have the `AUDIT ANY` or `AUDIT SYSTEM` privilege. This privilege can be used to disable auditing, which could be used to eliminate the audit trail record of a intruder who has compromised the system. The accounts that have this privilege could be targets for intruders.

#### OS Security Vulnerability Privileges Report

The OS Security Vulnerability Privileges Report shows the database accounts and roles that have the required system privileges to export sensitive or otherwise protected information to the operating system.

### Database Account Password Reports

The database account password reports are:

- Database Account Default Password Report
- Database Account Status Report

#### Database Account Default Password Report

The Database Account Default Password Report lists the database accounts that have default passwords. Default passwords are provided during the Oracle Database installation.

You should change the passwords for accounts included in this report to nondefault, complex passwords to help secure the database.

#### Database Account Status Report

The Database Account Status Report provides a quick view of existing database accounts. The report shows the account status for each account, which helps you identify accounts that must be locked. Lock and expiry dates provide information that helps determine whether the account was locked as a result of password aging. If a special password and resource secure profile is used, then you can identify accounts that are not using them. Accounts not using organizationally defined default tablespaces also can be identified, and the temporary tablespace for accounts can be determined. This report also identifies accounts that use external passwords.

### Security Audit Report: Core Database Audit Report

The Core Database Audit Report returns audit records for the audit policy defined in [Appendix A, "Auditing Oracle Database Vault,"](audplcy.md) and any auditing records that are generated for audit statements you have defined.

This report only displays audit records that are captured if the database initialization parameter `AUDIT_TRAIL` has been set to `DB`. For more information about the `AUDIT_TRAIL` parameter, see [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm).

### Other Security Vulnerability Reports

The other security vulnerability reports are:

- Java Policy Grants Report
- OS Directory Objects Report
- Objects Dependent on Dynamic SQL Report
- Unwrapped PL/SQL Package Bodies Report
- Username/Password Tables Report
- Tablespace Quotas Report
- Non-Owner Object Trigger Report

#### Java Policy Grants Report

The Java Policy Grants Report shows the Java policy permissions stored in the database. It helps reveal violations to the principle of least privilege. Look for `GRANT`, `READ`, or `WRITE` privileges to `PUBLIC` or other accounts and roles that do not necessarily need the privilege. It is advisable to disable Java loading privileges from `PUBLIC`, if Java is not required in the database.

Note:

Oracle JVM, the Java virtual machine option provided with Oracle Database Vault, must be installed before you can run the Java Policy Grants Report.

#### OS Directory Objects Report

The OS Directory Objects Report shows all directory objects that exist in the database, whether they are available to `PUBLIC`, and what their privileges are. Directory objects should exist only for secured operating system (OS) directories, and access to them within the database should be protected. You should never use the root operating system directory on any storage device (for example, `/`), because it allows remote database sessions to look at all files on the device.

#### Objects Dependent on Dynamic SQL Report

The Objects Dependent on Dynamic SQL Report shows objects that leverage dynamic SQL. Potential intruders have a greater chance of using this channel if parameter checking or bind variables are not used. The report helps by narrowing the scope of where to look for problems by pointing out who is using dynamic SQL. Such objects can be a target for a SQL injection attack and must be secured to avoid this type of attack. After determining the objects that use dynamic SQL, do the following:

- Check the privileges that client applications (for example, a Web application) have over the object.
- Check the access granted for the object to `PUBLIC` or a wider account base.
- Validate parameters.
- Use bind variables where possible.

#### Unwrapped PL/SQL Package Bodies Report

The Unwrapped PL/SQL Package Bodies Report displays PL/SQL package procedures that are not wrapped. Oracle provides a wrap utility that obfuscates code to the point where it cannot be read in the data dictionary or from the data dictionary views. This helps reduce the ability of an intruder to circumvent data protection by eliminating the ability to read source code that manipulates data.

#### Username/Password Tables Report

The Username/Password Tables Report helps to identify application tables in the database that store user names and password strings. You should examine these tables to determine if the information is encrypted. (Search for column names such as `%USER%NAME%` or `%PASSWORD%`.) If it is not, modify the code and applications using these tables to protect them from being visible to database sessions.

#### Tablespace Quotas Report

The Tablespace Quotas Report shows all database accounts that have quotas on one or more tablespaces. These tablespaces can become potential targets for denial-of-service (DoS) attacks.

#### Non-Owner Object Trigger Report

The Non-Owner Object Trigger Report lists triggers that are owned by a database account that is different from the account that owns the database object on which the trigger acts. If the trigger is not part of a trusted database application, then it can steal sensitive data, possibly from tables protected through Oracle Label Security or Virtual Private Database (VPD), and place it into an unprotected table for subsequent viewing or export.