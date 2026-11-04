---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/introduction-to-auditing.html
tags:
  - oracle
  - 21c
  - security-guide
---

Privileged users can create policies that track the changes that all users, including other privileged users, make in the database.

Note:

Except where noted, this part describes how to use pure unified auditing, in which all audit records are centralized in one place.

- What Is Auditing?  
	Auditing is the monitoring and recording of database activity, from both database users and nondatabase users.
- Why Is Auditing Used?  
	You typically use auditing to monitor user activity.
- Best Practices for Auditing  
	You should follow best practices guidelines for auditing.
- What Is Unified Auditing?  
	In unified auditing, the unified audit trail captures audit information from a variety of sources.
- Benefits of the Unified Audit Trail  
	The benefits of a unified audit trail are many.
- Checking if Your Database Has Migrated to Pure Unified Auditing  
	The `V$OPTION` dynamic view indicates if your database has been migrated to using pure unified auditing (that is, traditional auditing is turned off).
- Mixed Mode Auditing  
	Mixed mode auditing is the default auditing in a newly installed database.
- Who Can Perform Auditing?  
	Oracle provides two roles for users who perform auditing: `AUDIT_ADMIN` and `AUDIT_VIEWER`.
- Unified Auditing in a Multitenant Environment  
	You can apply audit settings to individual PDBs or to the CDB, depending on the type of policy.
- Auditing in a Distributed Database  
	Auditing is site autonomous in that a database instance audits only the statements issued by directly connected users.

**Parent topic:** [Monitoring Database Activity with Auditing](part_6.md)

### 25.1 What Is Auditing?

Auditing is the monitoring and recording of database activity, from both database users and nondatabase users.

"Nondatabase users" refers to application users who are recognized in the database using the `CLIENT_IDENTIFIER` attribute. To audit this type of user, you can use a unified audit policy condition, a fine-grained audit policy, or Oracle Database Real Application Security.

This guide describes how to use unified auditing. Alternatively, you can use traditional auditing, but traditional auditing (described in the Oracle Database release 11.2 [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG006)) has been deprecated starting in Oracle Database release 21c. In traditional auditing, there are separate audit trails for individual components, such as `SYS.AUD$` for the database audit trail, `SYS.FGA_LOG$` for fine-grained auditing, and `DVSYS.AUDIT_TRAIL$` for Oracle Database Vault. Unified auditing enables you to create policies that consolidate these audit trails into one audit trail, which is viewable in the `UNIFIED_AUDIT_TRAIL` data dictionary view. (Other unified audit trail views, such as `AUDIT_UNIFIED_POLICIES`, are available.) A consolidated audit data trail has many advantages over the individual audit trails in traditional auditing. This way, you can run analysis reports on an entire set of audit data in one operation, rather than having to first gather them into one location before performing the analysis. Audit mining tools such as Oracle Audit Vault can look at one location rather than several in order to gather audit records. A unified audit trail ensures that the audit information is consistently formatted and contains consistent fields.

You can base unified auditing on individual actions, such as the type of SQL statement executed, or on combinations of session metadata that can include the user name, application, time, and so on.

You can configure auditing for both successful and failed activities, and include or exclude specific users from the audit. You can audit individual actions of the pluggable database (PDB) or individual actions in the entire multitenant container database (CDB). In addition to auditing the standard activities the database provides, auditing can include activities from Oracle Database Real Application Security, Oracle Recovery Manager, Oracle Data Pump, Oracle Machine Learning for SQL, Oracle Database Vault, Oracle Label Security, and Oracle SQL\*Loader direct path events.

Auditing is enabled by default. All audit records are written to the unified audit trail in a uniform format and are made available through the `UNIFIED_AUDIT_TRAIL` view. These records reside in the `AUDSYS` schema. The audit records are stored in the `SYSAUX` tablespace by default. Oracle recommends that you configure a different tablespace for the unified audit trail, which you can do by using the `DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION` procedure. Be aware that for Oracle Database Standard Edition and Express Edition, but not for Enterprise Edition, you can only associate the tablespace for unified auditing once. You should perform this association before you generate any audit records for the unified audit trail. After you have associated the tablespace, you cannot modify it because partitioning is only supported on Enterprise Edition.

You can configure auditing by using any of the following methods:

- Group audit settings into one unified audit policy. You can create one or more unified audit policies that define all the audit settings that your database needs.
- Use one of the predefined unified audit policies. Oracle Database provides predefined unified audit policies that encompass the standard audit settings that most regulatory agencies require.
- Create fine-grained audit policies. You can create fine-grained audit policies that capture specific activities such as the time an action occurred.
- Enable one of the recommended audit policies that are provided in Oracle Data Safe.

Oracle recommends that you audit your databases. Auditing is an effective method of enforcing strong internal controls so that your site can meet its regulatory compliance requirements. This enables you to monitor business operations, and find activity that may deviate from company policy. By creating effective audit policies, you can generate an audit record for audit and compliance personnel. Be selective with auditing and ensure that it meets your business compliance needs.

**Related Topics**

- [Auditing Activities with Unified Audit Policies and the AUDIT Statement](configuring-audit-policies.md)
- [Auditing Activities with the Predefined Unified Audit Policies](configuring-audit-policies.md)
- [Auditing Specific Activities with Fine-Grained Auditing](configuring-audit-policies.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=ARPLS-GUID-77C238AB-7B08-4D84-B3B8-4FC5CBDB4A3F)

**Parent topic:** Introduction to Auditing

### 25.2 Why Is Auditing Used?

You typically use auditing to monitor user activity.

Auditing can be used to accomplish the following:

- Enable accountability for actions. These include actions taken in a particular schema, table, or row, or affecting specific content.
- Deter users (or others, such as intruders) from inappropriate actions based on their accountability.
- Investigate suspicious activity. For example, if a user is deleting data from tables, then a security administrator can audit all connections to the database and all successful and unsuccessful deletions of rows from all tables in the database.
- Notify an auditor of the actions of an unauthorized user. For example, an unauthorized user could be changing or deleting data, or the user has more privileges than expected, which can lead to reassessing user authorizations.
- Support post-incident investigations.
- Monitor and gather data about specific database activities. For example, the database administrator can gather statistics about which tables are being updated, how many logical I/Os are performed, or how many concurrent users connect at peak times.
- Detect problems with an authorization or access control implementation. For example, you can create audit policies that you expect will never generate an audit record because the data is protected in other ways. However, if these policies generate audit records, then you will know the other security controls are not properly implemented.
- Address auditing requirements for compliance. Regulations such as the following have common auditing-related requirements:
	- Sarbanes-Oxley Act
		- Health Insurance Portability and Accountability Act (HIPAA)
		- International Convergence of Capital Measurement and Capital Standards: a Revised Framework (Basel II)
		- Japan Privacy Law
		- European Union Directive on Privacy and Electronic Communications

**Parent topic:** Introduction to Auditing

### 25.3 Best Practices for Auditing

You should follow best practices guidelines for auditing.

- As a general rule, design your auditing strategy to collect the amount of information that you need to meet compliance requirements, but focus on activities that cause the greatest security concerns. For example, auditing every table in the database is not practical, but auditing tables with columns that contain sensitive data, such as salaries, is. With both unified and fine-grained auditing, there are mechanisms you can use to design audit policies that focus on specific activities to audit.
- Periodically archive and purge the audit trail data. You can use the `DBMS_AUDIT_MGMT` package to purge audit records in several different ways. You should regularly review the collected audit records and establish a system for collecting and retaining audit records based on your site's retention policies. In addition to `DBMS_AUDIT_MGMT`, Oracle Data Safe and Oracle Audit Vault and Database Firewall provide features that enable you manage the archiving and purging of audit trail data.

### 25.4 What Is Unified Auditing?

In unified auditing, the unified audit trail captures audit information from a variety of sources.

Unified auditing enables you to capture audit records from the following sources:

- Audit records (including `SYS` audit records) from unified audit policies and `AUDIT` settings
- Fine-grained audit records from the `DBMS_FGA` PL/SQL package
- Oracle Database Real Application Security audit records
- Oracle Recovery Manager audit records
- Oracle Database Vault audit records
- Oracle Label Security audit records
- Oracle Machine Learning for SQL records
- Oracle Data Pump
- Oracle SQL\*Loader Direct Load
- Oracle XML DB HTTP and FTP protocol messages

The unified audit trail, which resides in a read-only table in the `AUDSYS` schema in the `SYSAUX` tablespace, makes this information available in a uniform format in the `UNIFIED_AUDIT_TRAIL` data dictionary view, and is available in both single-instance and Oracle Database Real Application Clusters environments. In addition to the user `SYS`, users who have been granted the `AUDIT_ADMIN` and `AUDIT_VIEWER` roles can query these views. If your users only need to query the views but not create audit policies, then grant them the `AUDIT_VIEWER` role.

When the database is writeable, audit records are written to the unified audit trail. If the database is not writable, then audit records are written to new format operating system files in the `$ORACLE_BASE/audit/$ORACLE_SID` directory.

### 25.5 Benefits of the Unified Audit Trail

The benefits of a unified audit trail are many.

For example:

- After unified auditing is enabled, it does not depend on the initialization parameters that were used in previous releases. See [Table G-1](how-unified-auditing-migration-affects-individual-audit-features.md) for a list of these initialization parameters.
- The audit records, including records from the `SYS` audit trail, for all the audited components of your Oracle Database installation are placed in one location and in one format, rather than your having to look in different places to find audit trails in varying formats. This consolidated view enables auditors to co-relate audit information from different components. For example, if an error occurred during an `INSERT` statement, standard auditing can indicate the error number and the SQL that was executed. Oracle Database Vault-specific information can indicate whether this error happened because of a command rule violation or realm violation. Note that there will be two audit records with a distinct `AUDIT_TYPE`. With this unification in place, `SYS` audit records appear with `AUDIT_TYPE` set to `Standard Audit`.
- The management and security of the audit trail is also improved by having it in single audit trail.
- Overall auditing performance is greatly improved. By default, the audit records are automatically written to an internal relational table in the `AUDSYS` schema.
- You can create named audit policies that enable you to audit the supported components listed at the beginning of this section, as well as `SYS` administrative users. Furthermore, you can build conditions and exclusions into your policies.
- If you are using an Oracle Audit Vault and Database Firewall environment, then the unified audit trail greatly facilitates the collection of audit data, because all of this data will come from one location.

Note:

In previous releases, users were allowed to add and remove audit configuration to objects in their own schemas without any additional privileges. This ability is no longer allowed.

**Parent topic:** Introduction to Auditing

### 25.6 Checking if Your Database Has Migrated to Pure Unified Auditing

The `V$OPTION` dynamic view indicates if your database has been migrated to using pure unified auditing (that is, traditional auditing is turned off).

- Query the `VALUE` column of the `V$OPTION` dynamic view as follows, entering `Unified Auditing` in the case shown:
	```
	SELECT VALUE FROM V$OPTION WHERE PARAMETER = 'Unified Auditing';
	PARAMETER         VALUE
	----------------  ----------
	Unified Auditing  TRUE
	```

This output shows that unified auditing is enabled and traditional auditing is disabled. If pure unified auditing has not been enabled, then the output is `FALSE`, which implies that your database is using mixed mode auditing. Mixed mode auditing means that both traditional auditing and unified auditing are present.

### 25.7 Mixed Mode Auditing

Mixed mode auditing is the default auditing in a newly installed database.

- About Mixed Mode Auditing  
	Mixed mode auditing enables both traditional (that is, the audit facility from releases earlier than release 12c) and the new audit facilities (unified auditing).
- Enablement of Unified Auditing  
	By default and depending on the edition of Oracle Database, Oracle Database uses mixed mode auditing, supporting both unified audit and traditional audit.
- How Database Creation Determines the Type of Auditing You Have Enabled  
	Unified auditing uses the `$ORACLE_BASE/audit` directory as the location for the operating system files.
- Capabilities of Mixed Mode Auditing  
	Mixed mode auditing provides several capabilities.

**Parent topic:** Introduction to Auditing

#### 25.7.1 About Mixed Mode Auditing

Mixed mode auditing enables both traditional (that is, the audit facility from releases earlier than release 12c) and the new audit facilities (unified auditing).

When you create a new database, by default the database uses mixed mode auditing.

You can enable the database in either of these two modes: the mixed mode auditing or pure unified auditing mode. Even though the features of unified auditing are enabled in both these modes, there are differences between them. In mixed mode, you can use the new unified audit facility alongside the traditional auditing facility. In pure unified auditing, you only use the unified audit facility.

Note:

Starting with Oracle Database release 21c, traditional auditing is deprecated, and in release 23c, it is desupported. Oracle recommends that you turn off traditional auditing and use unified auditing instead. Oracle Database has mandatory audits that cannot be turned off. This enables you to audit the most common security relevant events.

Table 25-1 summarizes the features of these two modes and how you enable them.

Table 25-1 Differences Between Mixed Mode Audting and Pure Unified Auditing

| Mode | Features | How to Enable |
| --- | --- | --- |
| Mixed mode auditing | Has both traditional and unified auditing | Ensure that at least one unified audit policy is enabled in your database. Typically you will see the `ORA_SECURECONFIG` and `ORA_LOGIN_LOGOUT` policies enabled by default. |
| Pure unified auditing | Has only unified auditing; traditional auditing is turned off | Link the `oracle` binary with `uniaud_on`, and then restart the database. Relinking the binary turns off traditional audit. After you have decided to use pure unified auditing, you can relink the `oracle` binary with the unified audit option turned on. This turns off traditional auditing.  [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=UPGRD-GUID-EB285325-CA65-41B4-BE58-D3F69CFED789) describes how to enable pure unified auditing. |

Mixed mode is intended to introduce unified auditing, so that you can have a feel of how it works and what its nuances and benefits are. Mixed mode enables you to migrate your existing applications and scripts to use unified auditing. Once you have decided to use pure unified auditing, you can relink the `oracle` binary with the unified audit option turned on and thereby enable it as the one and only audit facility the Oracle database runs. If you decide to revert back to mixed mode, you can.

As in previous releases, the traditional audit facility is driven by the `AUDIT_TRAIL` initialization parameter. Only for mixed mode auditing, you should set this parameter to the appropriate traditional audit trail. This traditional audit trail will then be populated with audit records, along with the unified audit trail.

When you upgrade your database to the current release, traditional auditing is preserved, and the new audit records are written to the traditional audit trail. After you complete the migration, the audit records from the previous release are still available in those audit trails. You then can archive and purge these older audit trails by using the `DBMS_AUDIT_MGMT` PL/SQL procedures, based on your enterprise retention policies.

#### 25.7.2 Enablement of Unified Auditing

By default and depending on the edition of Oracle Database, Oracle Database uses mixed mode auditing, supporting both unified audit and traditional audit.

When you are ready to migrate to pure unified audit mode (which turns off traditional audit and improves audit performance), link the `oracle` binary with `uniaud_on`, and then restart the database, as described in [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dbseg&id=UPGRD-GUID-EB285325-CA65-41B4-BE58-D3F69CFED789).

#### 25.7.3 How Database Creation Determines the Type of Auditing You Have Enabled

Unified auditing uses the `$ORACLE_BASE/audit` directory as the location for the operating system files.

For newly created databases, mixed mode auditing is enabled by default through the predefined policies `ORA_SECURECONFIG` and `ORA_LOGIN_LOGOUT`.

Ensure that at least one unified audit policy is enabled in your database. Enable the `ORA_SECURECONFIG` and `ORA_LOGIN_LOGOUT` policies if they are not yet enabled. Note that Oracle Database has mandatory audits that cannot be turned off, so auditing of the most common security relevant events will continue to happen even if none of the unified audit policies are enabled.

#### 25.7.4 Capabilities of Mixed Mode Auditing

Mixed mode auditing provides several capabilities.

These capabilities are as follows:

- It enables the use of all existing auditing initialization parameters: `AUDIT_TRAIL`, `AUDIT_FILE_DEST`, `AUDIT_SYS_OPERATIONS`, and `AUDIT_SYSLOG_LEVEL`.
- It writes mandatory audit records only to the traditional audit trails.
- It bases standard audit records on the standard audit configuration, and writes these records to the audit trail designated by the `AUDIT_TRAIL` initialization parameter.
	However, be aware that standard audit trail records are also generated based on unified audit policies and only these audit records are written to the unified audit trail. The standard audit records generated as a result of unified audit policies follow the semantics of unified audit policy enablement.
- Administrative user sessions generate `SYS` audit records. These records are written if the `AUDIT_SYS_OPERATIONS` initialization parameter is set to `TRUE`. This process writes the records only to the traditional audit trails. However, when unified audit policies are enabled for administrative users, these unified audit records are also written to unified audit trail.
- The format of the audit records that are written to traditional audit trails remains the same as in Oracle Database 11g Release 2.
- Oracle Database immediately writes unified audit records to an internal relational table in the `AUDSYS` schema.
- The performance cost of writing an audit record is equivalent to the sum of the times required for generating and writing an audit record to the traditional audit trail and the unified audit trail.
- Mixed mode auditing provides a glance of the unified audit mode features. Oracle recommends that you migrate to unified audit mode once you are comfortable with the new style of audit policies and audit trail.

### 25.8 Who Can Perform Auditing?

Oracle provides two roles for users who perform auditing: `AUDIT_ADMIN` and `AUDIT_VIEWER`.

The privileges that these roles provide are as follows:

- AUDIT\_ADMIN role. This role enables you to create unified and fine-grained audit policies, use the `AUDIT` and `NOAUDIT` SQL statements, view audit data, and manage the audit trail administration. Grant this role only to trusted users.
- AUDIT\_VIEWER role. This role enables users to view and analyze audit data. It provides the `EXECUTE` privilege on the `DBMS_AUDIT_UTIL` PL/SQL package. The kind of user who needs this role is typically an external auditor.

To change audit policies or modify the audit trail (including purging old audit data), you must be granted the `AUDIT_ADMIN` role. An auditor can view audit data after being granted the `AUDIT_VIEWER` role.

**Parent topic:** Introduction to Auditing

### 25.9 Unified Auditing in a Multitenant Environment

You can apply audit settings to individual PDBs or to the CDB, depending on the type of policy.

Each PDB, including the root, has its own unified audit trail.

- Unified audit policies created with the CREATE AUDIT POLICY and AUDIT statements: You can create policies for both the root and individual PDBs.
- Audit records written to the syslog: On UNIX platforms, you can set the `UNIFIED_AUDIT_COMMON_SYSTEMLOG` initialization parameter in the CDB root to enable certain unified audit trail columns to be written to SYSLOG. On both Windows and UNIX, you can set the `UNIFIED_AUDIT_SYSTEMLOG` parameter in both the root and PDB level.
- Fine-grained audit policies: You can create policies for individual PDBs only, not the root.
- Purging the audit trail: You can perform purge operations for both the root and individual PDBs.

**Related Topics**

- [Unified Audit Policies or AUDIT Settings in a Multitenant Environment](configuring-audit-policies.md)
- [Enabling SYSLOG and Windows Event Viewer Captures for the Unified Audit Trail](administering-the-audit-trail.md)
- [Creating a Fine-Grained Audit Policy](configuring-audit-policies.md)
- [Purging Audit Trail Records](administering-the-audit-trail.md)

**Parent topic:** Introduction to Auditing

### 25.10 Auditing in a Distributed Database

Auditing is site autonomous in that a database instance audits only the statements issued by directly connected users.

A local Oracle Database node cannot audit actions that take place in a remote database.

**Parent topic:** Introduction to Auditing