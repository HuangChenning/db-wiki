---
title: Topics for Database Administrators and Developers
book: Concepts
doc_id: E40540-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40540/cmntopc.htm
tags:
  - oracle
  - 11g
  - concepts
---

## 17 Topics for Database Administrators and Developers

The previous parts of this manual described the basic architecture of Oracle Database. This chapter summarizes common database topics that are important for both database administrators and developers, and provides pointers to other manuals, not an exhaustive account of database features.

This chapter contains the following sections:

See Also:

[Chapter 18, "Concepts for Database Administrators"](cncptdba.md) discusses topics specific to DBAs. [Chapter 19, "Concepts for Database Developers"](cncptdev.md) discusses topics for developers.

## Overview of Database Security

In general, [database security](glossary.md) involves user authentication, encryption, access control, and monitoring.

### User Accounts

Each Oracle database has a list of valid database users. The database contains several default accounts, including the default administrative account `SYSTEM` (see ["SYS and SYSTEM Schemas"](tablecls.md)). You can create user accounts as needed.

To access a database, a user must provide a valid user name and authentication credential. The credential may be a password, Kerberos ticket, or public key infrastructure (PKI) certificate. You can configure database security to lock accounts based on failed login attempts.

#### Privilege and Role Authorization

In general, [database access control](glossary.md) involves restricting data access and database activities. For example, you can restrict users from querying specified tables or executing specified database commands.

A user [privilege](glossary.md) is the right to run specific SQL statements. Privileges can be divided into the following categories:

- System privilege
	This is the right to perform a specific action in the database, or perform an action on any objects of a specific type. For example, `CREATE USER` and `CREATE SESSION` are system privileges.
- Object privilege
	This is the right to perform a specific action on an object, for example, query the `employees` table. Privilege types are defined by the database.

Privileges are granted to users at the discretion of other users. Administrators should grant privileges to users so they can accomplish tasks required for their jobs. Good security practice involves granting a privilege only to a user who requires that privilege to accomplish the necessary work.

A [role](glossary.md) is a named group of related privileges that you grant to users or other roles. A role helps manage privileges for a database application or user group.

Figure 17-1 depicts a common use for roles. The roles `PAY_CLERK`, `MANAGER`, and `REC_CLERK` are assigned to different users. The application role `ACCTS_PAY`, which includes the privilege to execute the `ACCTS_PAY` application, is assigned to users with the `PAY_CLERK` and `MANAGER` role. The application role `ACCTS_REC`, which includes the privilege to execute the `ACCTS_REC` application, is assigned to users with the `REC_CLERK` and `MANAGER` role.

Figure 17-1 Common Uses for Roles

![Figure 17-1 Common Uses for Roles](img/cncpt082.gif)

> At the top of the graphic are a series of five icons represent users. The second row shows User Roles. The first icon is a PAY\_CLERK Role, which points to the first two users, a MANAGER Role, which points to the third user, and a REC\_CLERK Role, which points to the last two users. The third row of icons shows Application Roles. The ACCTS\_PAY Role points to PAY\_CLERK Role and MANAGER Role. The ACCTS\_REC Role points to MANAGER Role and REC\_CLERK Role. The last row of icons shows Application Privileges. The text "Privileges to execute the ACCTS\_PAY application" points to the ACCTS\_PAY Role. The text "Privileges to execute the ACCTS\_REC application" points to the ACCTS\_REC Role.
>
> End of description.
  

See Also:

- [Oracle Database 2 Day + Security Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10575/tdpsg_privileges.htm#TDPSG30000) and [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG40431) to learn how to manage privileges
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG004) to learn about using roles for security
- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/users_secure.htm#ADMQS072) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/secure.htm#ADMIN11240) to learn how to administer roles
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5176.htm#REFRN29027) to learn about the `SESSION_PRIVS` view

#### Profiles

In the context of system resources, a [user profile](glossary.md) is a named set of resource limits and password parameters that restrict database usage and [instance](glossary.md) resources for a user. Profiles can limit the number of concurrent [sessions](glossary.md) for a user, CPU processing time available for each session, and amount of logical I/O available (see ["Buffer I/O"](memory.md)). For example, the `clerk` profile could limit a user to system resources required for clerical tasks.

Note:

It is preferable to use Database Resource Manager to limit resources and to use profiles to manage passwords.

Profiles provide a single point of reference for users that share a set of attributes. You can assign a profile to one set of users, and a default profile to all others. Each user has at most one profile assigned at any point in time.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/users.htm#DBSEG20244) to learn how to manage resources with profiles
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6010.htm#SQLRF01310) for `CREATE PROFILE` syntax and semantics

### Authentication

In Oracle Database, [database authentication](glossary.md) is the process by which a user presents credentials to the database, which verifies the credentials and allows access to the database. Validating the identity establishes a trust relationship for further interactions. Authentication also enables accountability by making it possible to link access and actions to specific identities.

Oracle Database provides different authentication methods, including the following:

- Authentication by the database
	Oracle database can authenticate users using a password, Kerberos ticket, or PKI certificate. Oracle also supports RADIUS-compliant devices for other forms of authentication, including biometrics. The type of authentication must be specified when a user is created in the Oracle database.
- Authentication by the operating system
	Some operating systems permit Oracle Database to use information they maintain to authenticate users. After being authenticated by the operating system, users can connect to a database without specifying a user name or password.

Database operations such as shutting down or starting up the database should not be performed by non-administrative database users. These operations require `SYSDBA` or `SYSOPER` privileges (see ["Connection with Administrator Privileges"](startup.md)).

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG003) and [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asointro.htm#ASOAG9479) for more information about authentication methods
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN11046) to learn about administrative authentication

### Encryption

In general, [encryption](glossary.md) is the process of transforming data into an unreadable format using a secret key and an encryption algorithm. Encryption is often used to meet regulatory compliance requirements, such as those associated with the Payment Card Industry Data Security Standard (PCI-DSS) or breach notification laws. For example, credit card numbers, social security numbers, or patient health information must be encrypted.

#### Network Encryption

Encrypting data as it travels across a network between a client and server is known as [network encryption](glossary.md). An intruder can use a network packet sniffer to capture information as it travels on the network, and then spool it to a file for malicious use. Encrypting data on the network prevents this sort of activity.

#### Transparent Data Encryption

Oracle Advanced Security [Transparent Data Encryption](glossary.md) enables you to encrypt individual table columns or a tablespace. When a user inserts data into an encrypted column, the database automatically encrypts the data. When users select the column, the data is decrypted. This form of encryption is transparent, provides high performance, and is easy to implement.

Transparent data encryption includes industry-standard encryption algorithms such as the Advanced Encryption Standard (AES) and built-in key management.

### Oracle Data Redaction

Starting in Oracle Database 11g Release 2 (11.2.0.4), [Oracle Data Redaction](glossary.md) enables you to mask (redact) data that is queried by low-privileged users or applications. The redaction occurs in real time when users query the data. Oracle Data Redaction is a part of Oracle Advanced Security.

Data redaction supports the following redaction function types:

- Full data redaction
	In this case, the database redacts the entire contents of the specified columns in a table or view. For example, a `VARCHAR2` column for a last name displays a single space.
- Partial data redaction
	In this case, the database redacts portions of the displayed output. For example, an application can present a credit card number ending in `1234` as `xxxx-xxxx-xxxx-1234`. You can use regular expressions for both full and partial redaction. A regular expression can redact data based on a search pattern. For example, you can use regular expressions to redact specific phone numbers or email addresses.
- Random data redaction
	In this case, the database displays the data as randomly generated values, depending on the data type of the column. For example, the number `1234567` can appear as `83933895`.

Data redaction is not a comprehensive security solution. For example, it does not prevent directly connected, privileged users from performing inference attacks on redacted data. Such attacks identify redacted columns and, by process of elimination, try to back into actual data by repeating SQL queries that guess at stored values. To detect and prevent inference and other attacks originating from privileged users, Oracle recommends pairing Oracle Data Redaction with related database security products such as Oracle Audit Vault and Database Firewall, and Oracle Database Vault.

Data redaction works as follows:

- Use the `DBMS_REDACT` package to create a redaction policy for a specified table.
- In the policy, specify a predefined redaction function.
- Whether the database shows the actual or redacted value of a column depends on the policy. If the data is redacted, then the redaction occurs at the top-level select list immediately before display to the user.

The following example adds a full data redaction policy to redact the `employee_id` column of the `hr.employees` table:

```
BEGIN
 DBMS_REDACT.ADD_POLICY(
   object_schema    => 'hr'
,  object_name      => 'employees'
,  column_name      => 'employee_id'
,  policy_name      => 'mask_emp_ids'
,  function_type    => DBMS_REDACT.FULL
,  expression       => '1=1'
);
END;
/
```

In the preceding example, the expression setting, which evaluates to `true`, applies the redaction to users who are not granted the `EXEMPT REDACTION POLICY` privilege.

See Also:

- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/redaction.htm#ASOAG596) to learn about data redaction
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_redact.htm#ARPLS73800) to learn about `DBMS_REDACT`

### Access Control

Oracle Database provides many techniques to control access to data. This section summarizes some of these techniques.

#### Oracle Database Vault

[Oracle Database Vault](glossary.md) is a security option that restricts privileged user access to application data. You can use Oracle Database Vault to control when, where, and how the databases, data, and applications are accessed. Thus, you can address common security problems such as protecting against insider threats, complying with regulatory requirements, and enforcing separation of duty.

#### Virtual Private Database (VPD)

[Oracle Virtual Private Database (VPD)](glossary.md) enables you to enforce security at the row and column level. A [security policy](glossary.md) establishes methods for protecting a database from accidental or malicious destruction of data or damage to the database infrastructure.

VPD is useful when security protections such as privileges and roles are not sufficiently fine-grained. For example, you can allow all users to access the `employees` table, but create security policies to restrict access to employees in the same department as the user.

Essentially, the database adds a dynamic `WHERE` clause to a SQL statement issued against the table, [view](glossary.md), or [synonym](glossary.md) to which an Oracle VPD security policy was applied. The `WHERE` clause allows only users whose credentials pass the security policy to access the protected data.

#### Oracle Label Security (OLS)

Oracle Label Security (OLS) is a security option that enables you to assign data classification and control access using security labels. You can assign a label to both data and users.

When assigned to data, the label can be attached as a hidden column to existing tables, providing transparency to existing SQL. For example, rows that contain highly sensitive data can be labeled `HIGHLY SENSITIVE`, while rows that are less sensitive can be labeled `SENSITIVE`, and so on. When a user attempts to access data, OLS compares the user label with the data label and determines whether access should be granted. Unlike VPD, OLS provides an out-of-the-box security policy and the metadata repository for defining and storing labels.

### Monitoring

Oracle Database provides multiple tools and techniques for monitoring user activity.

#### Database Auditing

Database auditing is the monitoring and recording of selected user database actions. You can use standard auditing to audit SQL statements, privileges, schemas, objects, and network and multitier activity. Alternatively, you can use fine-grained auditing to monitor specific database activities, such as actions on a database table or times that activities occur. For example, you can audit a table accessed after 9:00 p.m.

Reasons for using auditing include:

- Enabling future accountability for current actions
- Deterring users (or others, such as intruders) from inappropriate actions based on their accountability
- Investigating, monitoring, and recording suspicious activity
- Addressing auditing requirements for compliance

See Also:

- [Oracle Database 2 Day + Security Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10575/tdpsg_auditing.htm#TDPSG50000) and [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG006) to learn how to enable and disable auditing
- [Oracle Label Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10745/audit.htm#OLSAG074) to learn about Oracle Label Security auditing, which supplements standard auditing

#### Oracle Audit Vault and Database Firewall

Oracle Audit Vault and Database Firewall (Oracle AVDF) provide a first line of defense for databases and consolidate audit data from databases, operating systems, and directories. A SQL grammar-based engine monitors and blocks unauthorized SQL traffic before it reaches the database. For compliance reporting and alerting, Oracle AVDF combines database activity data from the network with detailed audit data. You can tailor auditing and monitoring controls to meet enterprise security requirements.

See Also:

[Oracle Audit Vault and Database Firewall Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=SIGAD40487)

#### Enterprise Manager Auditing Support

[Oracle Enterprise Manager](glossary.md) (Enterprise Manager) enables you to view and configure audit-related initialization parameters. Also, you can administer objects when auditing statements and schema objects. For example, Enterprise Manager enables you to display and search for the properties of current audited statements, privileges, and objects. You can enable and disable auditing as needed.

## Overview of High Availability

Availability is the degree to which an application, service, or functionality is available on demand. For example, an [OLTP](glossary.md) database used by an online bookseller is available to the extent that it is accessible by customers making purchases. Reliability, recoverability, timely error detection, and continuous operations are the primary characteristics of high availability.

The importance of high availability in a database environment is tied to the cost of downtime, which is the time that a resource is unavailable. Downtime can be categorized as either planned or unplanned. The main challenge when designing a highly available environment is examining all possible causes of downtime and developing a plan to deal with them.

See Also:

[Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/overview.htm#HAOVW001) for an introduction to high availability

### High Availability and Unplanned Downtime

Oracle Database provides high availability solutions to prevent, tolerate, and reduce downtime for all types of unplanned failures. Unplanned downtime can be categorized by its causes:

- Site Failures
- Computer Failures
- Storage Failures
- Data Corruption
- Human Errors

See Also:

[Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/unplanned.htm#HAOVW117) to learn about protecting against unplanned downtime

#### Site Failures

A site failure occurs when an event causes all or a significant portion of an application to stop processing or slow to an unusable service level. A site failure may affect all processing at a data center, or a subset of applications supported by a data center. Examples include an extended site-wide power or network failure, a natural disaster making a data center inoperable, or a malicious attack on operations or the site.

The simplest form of protection against site failures is to create database backups using RMAN and store them offsite. You can restore the database to another host. However, this technique can be time-consuming, and the backup may not be current. Maintaining one or more standby databases in a Data Guard environment enables you to provide continuous database service if the production site fails.

See Also:

- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/overview.htm#HAOVW113) to learn about site failures
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmintro.htm#BRADV89341) for information on RMAN and backup and recovery solutions
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/concepts.htm#SBYDB00010) for an introduction to standby databases

#### Computer Failures

A computer failure outage occurs when the system running the database becomes unavailable because it has shut down or is no longer accessible. Examples of computers failures include hardware and operating system failures.

The following Oracle features protect against or help respond to computer failures:

- Enterprise Grids
	In an Oracle Real Applications Cluster (Oracle RAC) environment, Oracle Database runs on two or more systems in a cluster while concurrently accessing a single shared database. A single database system spans multiple hardware systems yet appears to the application as a single database. See "Overview of Grid Computing".
- Oracle Data Guard
	Data Guard enables you to maintain a copy of a production database, called a standby database, that can reside on a different continent or in the same data center. If the primary database is unavailable because of an outage, then Data Guard can switch any standby database to the primary role, minimizing downtime. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/rollup.htm#SBYDB00830).
- Oracle Restart
	Components in the Oracle Database software stack, including the database instance, listener, and [Oracle ASM](glossary.md) instance, can restart automatically after a component failure or whenever the database host computer restarts. Oracle Restart ensures that Oracle components are started in the proper order, in accordance with component dependencies. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/restart.htm#ADMIN12708) to learn how to configure Oracle Restart.
- Fast Start Fault Recovery
	A common cause of unplanned downtime is a system fault or crash. The fast start fault recovery technology in Oracle Database automatically bounds database [instance recovery](glossary.md) time. See [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for information on fast start fault recovery.

See Also:

[Oracle Database High Availability Best Practices](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HABPT00202) to learn how to use High Availability for processes and applications that run in a single-instance database

#### Storage Failures

A storage failure outage occurs when the storage holding some or all of the database contents becomes unavailable because it has shut down or is no longer accessible. Examples of storage failures include the failure of a disk drive or storage array.

In addition to Oracle Data Guard, solutions for storage failures include the following:

- Oracle Automatic Storage Management (Oracle ASM)
	Oracle ASM is a vertically integrated file system and volume manager in the database kernel (see ["Oracle Automatic Storage Management (Oracle ASM)"](physical.md)). Oracle ASM eliminates the complexity associated with managing data and disks, and simplifies mirroring and the process of adding and removing disks.
- Backup and recovery
	The Recovery Manager (RMAN) utility can back up data, restore data from a previous backup, and recover changes to that data up to the time before the failure occurred (see ["Backup and Recovery"](cncptdba.md)).

See Also:

- [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/asm.htm#ADMQS12100) to learn how to administer Oracle ASM disks with Oracle Enterprise Manager (Enterprise Manager)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmcon.htm#OSTMG036) to learn more about Oracle ASM

#### Data Corruption

A data corruption occurs when a hardware, software or network component causes corrupt data to be read or written. For example, a volume manager error causes bad disk read or writes. Data corruptions are rare but can have a catastrophic effect on a database, and therefore a business.

In addition to Data Guard and Recovery Manager, Oracle Database supports the following forms of protection against data corruption:

- Lost write protection
	A [data block](glossary.md) lost write occurs when an I/O subsystem acknowledges the completion of the block write when the write did not occur. You can configure the database so that it records buffer cache block reads in the redo log. Lost write detection is most effective when used with Data Guard.
- Data block corruption detection
	A block corruption is a data block that is not in a recognized Oracle format, or whose contents are not internally consistent. Several database components and utilities, including RMAN, can detect a corrupt block and record it in `V$DATABASE_BLOCK_CORRUPTION`. If the environment uses a real-time standby database, then RMAN can automatically repair corrupt blocks.
- Data Recovery Advisor
	Data Recovery Advisor is an Oracle tool that automatically diagnoses data failures, determines and presents appropriate repair options, and executes repairs at the user's request.

See Also:

- [Oracle Database High Availability Best Practices](https://docs.oracle.com/cd/E11882_01/server.112/e10803/outage.htm#HABPT00405) to learn how to protect against data corruptions
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmintro.htm#BRADV89341) for information on RMAN and backup and recovery solutions

#### Human Errors

A human error outage occurs when unintentional or malicious actions are committed that cause data in the database to become logically corrupt or unusable. The service level impact of a human error outage can vary significantly depending on the amount and critical nature of the affected data.

Much research cites human error as the largest cause of downtime. Oracle Database provides powerful tools to help administrators quickly diagnose and recover from these errors. It also includes features that enable end users to recover from problems without administrator involvement.

Oracle Database recommends the following forms of protection against human error:

- Restriction of user access
	The best way to prevent errors is to restrict user access to data and services. Oracle Database provides a wide range of security tools to control user access to application data by authenticating users and then allowing administrators to grant users only those privileges required to perform their duties (see "Overview of Database Security").
- Oracle Flashback Technology
	Oracle Flashback Technology is a family of human error correction features in Oracle Database. Oracle Flashback provides a SQL interface to quickly analyze and repair human errors. For example, you can perform:
	- Fine-grained surgical analysis and repair for localized damage
		- Rapid correction of more widespread damage
		- Recovery at the row, transaction, table, tablespace, and database level
- Oracle LogMiner
	Oracle LogMiner is a relational tool that enables [online files](glossary.md) to be read, analyzed, and interpreted using SQL (see ["Oracle LogMiner"](cncptdba.md)).

See Also:

- [Oracle Database High Availability Best Practices](https://docs.oracle.com/cd/E11882_01/server.112/e10803/outage.htm#HABPT00405) to learn how to recover from human errors
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmintro.htm#BRADV89342) and [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_flashback.htm#ADFNS1008) to learn more about Oracle Flashback features
- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/logminer.htm#SUTIL1553) to learn more about Oracle LogMiner

### High Availability and Planned Downtime

Planned downtime can be just as disruptive to operations, especially in global enterprises that support users in multiple time zones. In this case, it is important to design a system to minimize planned interruptions such as routine operations, periodic maintenance, and new deployments.

Planned downtime can be categorized by its causes:

- System and Database Changes
- Data Changes
- Application Changes

See Also:

[Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/planned.htm#HAOVW144) to learn about features and solutions for planned downtime

#### System and Database Changes

Planned system changes occur when you perform routine and periodic maintenance operations and new deployments, including scheduled changes to the operating environment that occur outside of the organizational data structure in the database. Examples include adding or removing CPUs and cluster nodes (a node is a computer on which a database instance resides), upgrading system hardware or software, and migrating the system platform.

Oracle Database provides dynamic resource provisioning as a solution to planned system and database changes:

- Dynamic reconfiguration of the database
	Oracle Database dynamically accommodates various changes to hardware and database configurations, including adding and removing processors from an SMP server and adding and remove storage arrays using Oracle ASM. For example, Oracle Database monitors the operating system to detect changes in the number of CPUs. If the `CPU_COUNT` initialization parameter is set to the default, then the database workload can dynamically take advantage of newly added processors.
- Autotuning memory management
	Oracle Database uses a noncentralized policy to free and acquire memory in each subcomponent of the [SGA](glossary.md) and the [PGA](glossary.md). Oracle Database autotunes memory by prompting the operating system to transfer granules of memory to components that require it. See ["Memory Management"](cncptdba.md).
- Automated distributions of data files, control files, and online redo log files
	Oracle ASM automates and simplifies the layout of data files, control files, and log files by automatically distributing them across all available disks. See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmcon.htm#OSTMG036) to learn more about Oracle ASM.

#### Data Changes

Planned data changes occur when there are changes to the logical structure or physical organization of Oracle Database objects. The primary objective of these changes is to improve performance or manageability. Examples include table redefinition, adding table [partitions](glossary.md), and creating or rebuilding indexes.

Oracle Database minimizes downtime for data changes through online reorganization and redefinition. This architecture enables you to perform the following tasks when the database is open:

- Perform online table redefinition, which enables you to make table structure modifications without significantly affecting the availability of the table
- Create, analyze, and reorganize [indexes](glossary.md) (see [Chapter 3, "Indexes and Index-Organized Tables"](indexiot.md))
- Move table partitions (see ["Overview of Partitions"](schemaob.md))

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01514) to learn how to change data structures online

#### Application Changes

Planned application changes may include changes to data, schemas, and programs. The primary objective of these changes is to improve performance, manageability, and functionality. An example is an application upgrade.

Oracle Database supports the following solutions for minimizing application downtime required to make changes to an application's database objects:

- Rolling patch updates
	Oracle Database supports the application of patches to the nodes of an Oracle RAC system in a rolling fashion. See [Oracle Database High Availability Best Practices](https://docs.oracle.com/cd/E11882_01/server.112/e10803/schedule_outage.htm#HABPT00403).
- Rolling release upgrades
	Oracle Database supports the installation of database software upgrades, and the application of patchsets, in a rolling fashion—with near zero database downtime—by using Data Guard SQL Apply and logical standby databases. See [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/intro.htm#UPGRD00190).
- Edition-based redefinition
	Edition-based redefinition enables you to upgrade the database objects of an application while the application is in use, thus minimizing or eliminating down time. Oracle Database accomplishes this task by changing (redefining) database objects in a private environment known as an [edition](glossary.md). See [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS020).
- [DDL](glossary.md) with the default `WAIT` option
	DDL commands require exclusive [locks](glossary.md) on internal structures (see ["DDL Locks"](consist.md)). In previous releases, DDL commands would fail if they could not obtain the locks. DDL specified with the `WAIT` option resolves this issue. See [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/planned.htm#HAOVW182).
- Creation of triggers in a disabled state
	You can create a [trigger](glossary.md) in the disabled state so that you can ensure that your code compiles successfully before you enable the trigger. See [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/sql_cursor.htm#LNPLS1609).

## Overview of Grid Computing

Grid computing is a computing architecture that effectively pools large numbers of servers and storage into a flexible, on-demand resource for all enterprise computing needs. A Database Server Grid is a collection of commodity servers connected together to run on one or more databases. A Database Storage Grid is a collection of low-cost modular storage arrays combined together and accessed by the computers in the Database Server Grid.

With the Database Server and Storage Grid, you can build a pool of system resources. You can dynamically allocate and deallocate these resources based on business priorities.

Figure 17-2 illustrates the Database Server Grid and Database Storage Grid in a Grid enterprise computing environment.

Figure 17-2 Grid Computing Environment

![Figure 17-2 Grid Computing Environment](img/haovw004.gif)

> This illustration shows the components of a Grid computing environment.
>
> Several database server clusters are shown connected to one another though an interconnect to form the Database Server Grid. The Database Server Grid is then connected to the Database Storage Grid—shown as several database clusters—through storage switches.
>
> End of image description.
  

See Also:

- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/grid.htm#HAOVW189) for an overview of Grid Computing
- `http://www.gridforum.org/` to learn about the standards organization Global Grid Forum (GGF)

### Database Server Grid

Oracle Real Application Clusters (Oracle RAC) enables multiple instances that are linked by an interconnect to share access to an Oracle database. In an Oracle RAC environment, Oracle Database runs on two or more systems in a cluster while concurrently accessing a single shared database. Oracle RAC enables a Database Server Grid by providing a single database that spans multiple low-cost servers yet appears to the application as a single, unified database system.

Oracle Clusterware is software that enables servers to operate together as if they are one server. Each server looks like any standalone server. However, each server has additional processes that communicate with each other so that separate servers work together as if they were one server. Oracle Clusterware provides all of the features required to run the cluster, including node membership and messaging services.

See Also:

- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/adminoc.htm#TDPRC222) for an introduction to Oracle Clusterware and Oracle RAC
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admcon.htm#RACAD7279) to learn how to manage an Oracle RAC database
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD1111) to learn how to administer and deploy Oracle Clusterware

#### Scalability

In a Database Server Grid, Oracle RAC enables you to add nodes to the cluster as the demand for capacity increases. The Cache Fusion technology implemented in Oracle RAC enables you to scale capacity without changing your applications. Thus, you can scale the system incrementally to save costs and eliminate the need to replace smaller single-node systems with larger ones.

You can incrementally add nodes to a cluster instead of replacing existing systems with larger nodes. Grid Plug and Play simplifies addition and removal of nodes from a cluster, making it easier to deploy clusters in a dynamically provisioned environment. Grid Plug and Play also enables databases and services to be managed in a location-independent manner. SCAN enables clients to connect to the database service without regard for its location within the grid.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admcon.htm#RACAD7274) to learn more about Cache Fusion
- [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) to learn how to install Grid Plug and Play

#### Fault Tolerance

Fault tolerance is the protection provided by a high availability architecture against the failure of a component in the architecture. A key advantage of the Oracle RAC architecture is the inherent fault tolerance provided by multiple nodes. Because the physical nodes run independently, the failure of one or more nodes does not affect other nodes in the cluster.

Failover can happen to any node on the Grid. In the extreme case, an Oracle RAC system provides database service even when all but one node is down. This architecture allows a group of nodes to be transparently put online or taken offline, for maintenance, while the rest of the cluster continues to provide database service.

Oracle RAC provides built-in integration with Oracle Clients and connection pools. With this capability, an application is immediately notified of any failure through the pool that terminates the connection. The application avoids waiting for a TCP timeout and can immediately take the appropriate recovery action. Oracle RAC integrates the [listener](glossary.md) with Oracle Clients and the connection pools to create optimal application throughput. Oracle RAC can balance cluster workload based on the load at the time of the transaction.

See Also:

- ["Database Resident Connection Pooling"](dist_pro.md)
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD076) to learn more about automatic workload management
- [Oracle Database High Availability Best Practices](https://docs.oracle.com/cd/E11882_01/server.112/e10803/outage.htm#HABPT04406) for an overview of fault tolerance in Oracle RAC

#### Services

Oracle RAC supports services that can group database workloads and route work to the optimal instances assigned to offer the services. A service represents the workload of applications with common attributes, performance thresholds, and priorities.

You define and apply business policies to these services to perform tasks such as to allocate nodes for times of peak processing or to automatically handle a server failure. Using services ensures the application of system resources where and when they are needed to achieve business goals.

Services are integrated with the Database Resource Manager, which enables you to restrict the resources that are used by a service within an instance. In addition, Oracle Scheduler jobs can run using a service, as opposed to using a specific instance.

See Also:

- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/configwlm.htm#TDPRC289) to learn about Oracle services
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dbrm.htm#ADMIN11841) to learn about the Database Resource Manager and Oracle Scheduler

### Database Storage Grid

A DBA or storage administrator can use the Oracle ASM interface to specify the disks within the Database Storage Grid that ASM should manage across all server and storage platforms. ASM partitions the disk space and evenly distributes the data across the disks provided to ASM. Additionally, ASM automatically redistributes data as disks from storage arrays are added or removed from the Database Storage Grid.

See Also:

- ["Oracle Automatic Storage Management (Oracle ASM)"](physical.md)
- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/grid.htm#HAOVW192) for an overview of the Database Storage Grid
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmfilesystem.htm#OSTMG30000) for more information about clustered Oracle ASM

## Overview of Data Warehousing and Business Intelligence

A data warehouse is a relational database designed for query and analysis rather than for [transaction](glossary.md) processing. For example, a data warehouse could track historical stock prices or income tax records. A warehouse usually contains data derived from historical transaction data, but it can include data from other sources.

A data warehouse environment includes several tools in addition to a relational database. A typical environment includes an [ETL](glossary.md) solution, an [OLAP](glossary.md) engine, Oracle Warehouse Builder, client analysis tools, and other applications that gather data and deliver it to users.

### Data Warehousing and OLTP

A common way of introducing data warehousing is to refer to the characteristics of a data warehouse as set forth by William Inmon <sup>Foot 1</sup> :

- Subject-Oriented
	Data warehouses enable you to define a database by subject matter, such as sales.
- Integrated
	Data warehouses must put data from disparate sources into a consistent format. They must resolve such problems as naming conflicts and inconsistencies among units of measure. When they achieve this goal, they are said to be integrated.
- Nonvolatile
	The purpose of a warehouse is to enable you to analyze what has occurred. Thus, after data has entered into the warehouse, data should not change.
- Time-Variant
	The focus of a data warehouse is on change over time.

Data warehouses and OLTP database have different requirements. For example, to discover trends in business, data warehouses must maintain large amounts of data. In contrast, good performance requires historical data to be moved regularly from OLTP systems to an archive. Table 17-1 lists differences between data warehouses and OLTP.

Table 17-1 Data Warehouses and OLTP Systems

| Characteristics | Data Warehouse | OLTP |
| --- | --- | --- |
| Workload | Designed to accommodate ad hoc queries. You may not know the workload of your data warehouse in advance, so it should be optimized to perform well for a wide variety of possible queries. | Supports only predefined operations. Your applications might be specifically tuned or designed to support only these operations. |
| Data modifications | Updated on a regular basis by the ETL process using bulk data modification techniques. End users of a data warehouse do not directly update the database. | Subject to individual [DML](glossary.md) statements routinely issued by end users. The OLTP database is always up to date and reflects the current state of each business transaction. |
| Schema design | Uses denormalized or partially denormalized schemas (such as a star schema) to optimize query performance. | Uses fully normalized schemas to optimize DML performance and to guarantee data consistency. |
| Typical operations | A typical query scans thousands or millions of rows. For example, a user may request the total sales for all customers last month. | A typical operation accesses only a handful of records. For example, a user may retrieve the current order for a single customer. |
| Historical data | Stores many months or years of data to support historical analysis. | Stores data from only a few weeks or months. Historical data retained as needed to meet the requirements of the current transaction. |

See Also:

- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/concept.htm#DWHSG001) for a more detailed description of a database warehouse
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_oltp.htm#VLDBG006) for a more detailed description of an OLTP system

### Data Warehouse Architecture

Data warehouses and their architectures vary depending on the business requirements. This section describes common data warehouse architectures.

#### Data Warehouse Architecture (Basic)

Figure 17-3 shows a simple architecture for a data warehouse. End users directly access data that was transported from several source systems to the data warehouse.

Figure 17-3 Architecture of a Data Warehouse

![Figure 17-3 Architecture of a Data Warehouse](img/cncpt170.gif)

> The image shows a data warehouse with metadata, raw data, and summary data. Data going in to the data warehouse comes from data sources (operational systems and flat files) and from users (doing analysis, reporting, and mining).
>
> End of description.
>
> [Copyright © 1993, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

Figure 17-3 shows both the metadata and raw data of a traditional OLTP system and summary data. A summary is an aggregate view that improves query performance by precalculating expensive [joins](glossary.md) and aggregation operations and storing the results in a table. For example, a summary table can contain the sums of sales by region and by product. Summaries are also called [materialized views](glossary.md).

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008) to learn about basic materialized views

#### Data Warehouse Architecture (with a Staging Area)

In the architecture shown in Figure 17-3, operational data must be cleaned and processed before being put into the warehouse. Figure 17-4 shows a data warehouse with a staging area, which is a place where data is preprocessed before entering the warehouse. A staging area simplifies the tasks of building summaries and managing the warehouse.

Figure 17-4 Architecture of a Data Warehouse with a Staging Area

![Figure 17-4 Architecture of a Data Warehouse with a Staging Area](img/cncpt171.gif)

> The image shows a data warehouse with metadata, raw data, and summary data. Data going into the data warehouse comes from data sources (operational systems and flat files) and from users (doing analysis, reporting, and mining).The operational data from the data sources first goes to a staging area.
>
> End of description.
  

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transform.htm#DWHSG014) to learn about different transportation mechanisms

#### Data Warehouse Architecture (with a Staging Area and Data Marts)

You may want to customize your warehouse architecture for different groups within your organization. You can achieve this goal by transporting data in the warehouse to data marts, which are independent databases designed for a specific business or project. Typically, data marts include many summary tables.

Figure 17-5 separates purchasing, sales, and inventory information into independent data marts. A financial analyst can query the data marts for historical information about purchases and sales.

Figure 17-5 Architecture of a Data Warehouse with a Staging Area and Data Marts

![Figure 17-5 Architecture of a Data Warehouse with a Staging Area and Data Marts](img/cncpt172.gif)

> The image shows a data warehouse with metadata, raw data, and summary data. Data going in to the data warehouse comes from data sources (operational systems and flat files) and from users (doing analysis, reporting, and mining).The operational data from the data sources first goes to a staging area. The user data is separated into lines of business, such as sales and purchasing.
>
> End of description.
  

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transport.htm#DWHSG013) to learn about transformation mechanisms

### Overview of Extraction, Transformation, and Loading (ETL)

The process of extracting data from source systems and bringing it into the warehouse is commonly called ETL: extraction, transformation, and loading. ETL refers to a broad process rather than three well-defined steps.

In a typical scenario, data from one or more operational systems is extracted and then physically transported to the target system or an intermediate system for processing. Depending on the method of transportation, some transformations can occur during this process. For example, a SQL statement that directly accesses a remote target through a gateway can concatenate two columns as part of the `SELECT` statement.

Oracle Database is not itself an ETL tool. However, Oracle Database provides a rich set of capabilities usable by ETL tools such as Oracle Warehouse Builder and customized ETL solutions. ETL capabilities provided by Oracle Database include:

- Transportable tablespaces
	You can transport [tablespaces](glossary.md) between different computer architectures and operating systems. Transportable tablespaces are the fastest way for moving large volumes of data between two Oracle databases. See [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tspaces.htm#ADMIN01101) to learn about transportable tablespaces.
- Table functions
	A table function can produce a set of rows as output and can accept a set of rows as input. Table functions provide support for pipelined and parallel execution of transformations implemented in PL/SQL, C, or Java without requiring the use of intermediate staging tables. See [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/transform.htm#DWHSG014) to learn about table functions.
- External tables
	External tables enable external data to be joined directly and in parallel without requiring it to be first loaded in the database (see ["External Tables"](tablecls.md)). Thus, external tables enable the pipelining of the loading phase with the transformation phase.
- Table compression
	To reduce disk use and memory use, you can store tables and partitioned tables in a compressed format (see ["Table Compression"](tablecls.md)). The use of [table compression](glossary.md) often leads to a better scaleup for read-only operations and faster query execution.
- Change Data Capture
	This feature efficiently identifies and captures data that has been added to, updated in, or removed from, relational tables and makes this change data available for use by applications or individuals.

See Also:

- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) to learn about Change Data Capture
- [Oracle Warehouse Builder Data Modeling, ETL, and Data Quality Guide](https://docs.oracle.com/cd/E11882_01/owb.112/e10935/transformdata_intro.htm#WBETL04000) for an overview of ETL

### Business Intelligence

Business intelligence is the analysis of an organization's information as an aid to making business decisions. Business intelligence and analytical applications are dominated by actions such as drilling up and down hierarchies and comparing aggregate values. Oracle Database provides several technologies to support business intelligence operations.

#### Analytic SQL

Oracle Database has introduced many SQL operations for performing analytic operations. These operations include ranking, moving averages, cumulative sums, ratio-to-reports, and period-over-period comparisons. For example, Oracle Database supports the following forms of analytic SQL:

- SQL for aggregation
	Aggregate functions such as `COUNT` return a single result row based on groups of rows rather than on single rows. Aggregation is fundamental to data warehousing. To improve aggregation performance in a warehouse, the database provides extensions to the `GROUP BY` clause to make querying and reporting easier and faster. See [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/aggreg.htm#DWHSG020) to learn about aggregation.
- SQL for analysis
	Analytic functions compute an aggregate value based on a group of rows. They differ from aggregate functions in that they return multiple rows for each group. Oracle has advanced SQL analytical processing capabilities using a family of analytic SQL functions. For example, these analytic functions enable you to calculate rankings and percentiles and moving windows. See [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/analysis.htm#DWHSG021) to learn about SQL for analysis and reporting.
- SQL for modeling
	With the `MODEL` clause, you can create a multidimensional array from query results and apply rules to this array to calculate new values. For example, you can partition data in a sales view by country and perform a model computation, as defined by multiple rules, on each country. One rule could calculate the sales of a product in 2011 as the sum of sales in 2009 and 2010. See [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/sqlmodel.htm#DWHSG022) to learn about SQL modeling.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions001.htm#SQLRF51173) to learn about SQL functions

#### OLAP

Oracle online analytical processing (OLAP) provides native multidimensional storage and rapid response times when analyzing data across multiple [dimensions](glossary.md). OLAP enables analysts to quickly obtain answers to complex, iterative queries during interactive sessions.

Oracle OLAP has the following primary characteristics:

- Oracle OLAP is integrated in the database so that you can use standard SQL administrative, querying, and reporting tools.
- The OLAP engine runs within the kernel of Oracle Database.
- Dimensional objects are stored in Oracle Database in their native multidimensional format.
- Cubes and other dimensional objects are first class data objects represented in the Oracle [data dictionary](glossary.md).
- Data security is administered in the standard way, by granting and revoking privileges to Oracle Database users and roles.

Oracle OLAP offers the power of simplicity: one database, standard administration and security, and standard interfaces and development tools.

See Also:

- ["Overview of Dimensions"](schemaob.md)
- [Oracle OLAP User's Guide](https://docs.oracle.com/cd/E11882_01/olap.112/e17123/overview.htm#OLAUG100) for an overview of Oracle OLAP

#### Data Mining

Data mining involves automatically searching large stores of data for patterns and trends that go beyond simple analysis. Data mining uses sophisticated mathematical algorithms to segment data and evaluate the probability of future events. Typical applications of data mining include call centers, ATMs, E-business relational management (ERM), and business planning.

With Oracle Data Mining, the data, data preparation, model building, and model scoring results all remain in the database. Oracle Data Mining supports a PL/SQL API, a Java API, SQL functions for model scoring, and a GUI called Oracle Data Miner. Thus, Oracle Database provides an infrastructure for application developers to integrate data mining seamlessly with database applications.

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/process.htm#DMCON002)

## Overview of Oracle Information Integration

As an organization evolves, it becomes increasingly important for it to be able to share information among multiple databases and applications. The basic approaches to sharing information are as follows:

- Consolidation
	You can consolidate the information into a single database, which eliminates the need for further integration. Oracle RAC, Grid computing, and Oracle VPD can enable you to consolidate information into a single database.
- Federation
	You can leave information distributed, and provide tools to federate this information, making it appear to be in a single virtual database.
- Sharing
	You can share information, which lets you maintain the information in multiple data stores and applications.

This section focuses on Oracle solutions for federating and sharing information.

See Also:

[Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_intro2ii.htm#TDPII006) for an introduction to data replication and integration

### Federated Access

The foundation of federated access is a distributed environment, which is a network of disparate systems that seamlessly communicate with each other. Each system in the environment is called a node. The system to which a user is directly connected is called the local system. Additional systems accessed by this user are remote systems.

A distributed environment enables applications to access and exchange data from the local and remote systems. All the data can be simultaneously accessed and modified.

#### Distributed SQL

Distributed SQL synchronously accesses and updates data distributed among multiple databases. An Oracle distributed database system can be transparent to users, making it appear as a single Oracle database.

Distributed SQL includes distributed queries and [distributed transactions](glossary.md). The Oracle distributed database architecture provides query and transaction transparency. For example, standard DML statements work just as they do in a non-distributed database environment. Additionally, applications control transactions using the standard SQL statements `COMMIT`, `SAVEPOINT`, and `ROLLBACK`.

See Also:

- ["Overview of Distributed Transactions"](transact.md)
- [Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_distdbs.htm#TDPII015) to learn about distributed SQL
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/ds_txns.htm#ADMIN031) to learn how to manage distributed transactions

#### Database Links

A database link is a connection between two physical databases that enables a client to access them as one logical database. Oracle Database uses database links to enable users on one database to access objects in a remote database. A local user can access a link to a remote database without being a user on the remote database.

Figure 17-6 shows an example of user `hr` accessing the `employees` table on the remote database with the global name `hq.example.com`. The `employees` synonym hides the identity and location of the remote schema object.

Figure 17-6 Database Link

![Figure 17-6 Database Link](img/cncpt243.gif)

> On the left of the diagram is an icon of the HR user. This user issues the statement: SELECT \* FROM employees. An arrow leads from the user icon to a Local database. Above this database is the text: PUBLIC SYNONYM employees -> employees@HQ.EXAMPLE.COM. The arrow continues on and ends in Remote database, which contains the EMPLOYEES table. The arrow is labeled "Database link (unidirectional)."
>
> End of description.
  

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/ds_admin.htm#ADMIN12150) to learn about database links

### Information Sharing

At the heart of any integration is the sharing of data among applications in the enterprise. Oracle Streams is the asynchronous information sharing infrastructure in Oracle Database. This infrastructure enables the propagation and management of data, transactions, and events in a data stream either within a database, or from one database to another.

Oracle Streams includes replication and messaging. Replication is the process of sharing database objects and data at multiple databases. Messaging is the sharing of information between applications and users.

#### Oracle Streams Replication

In Oracle Streams replication, a change to a database object at one database can be shared with other databases in the replication environment. For example, Oracle Streams propagates an update to an `employees` table to an identical `employees` table in a different database. In this way, the database objects and data are kept synchronized at all databases in the replication environment.

Typical uses for Oracle Streams replication include:

- Creating a reporting site to offload processing from a primary OLTP site.
- Providing load balancing and improved scalability and availability for a call center or similar application.
- Providing site autonomy between locations to satisfy certain common business requirements.
- Transforming and consolidating data from multiple locations.
- Replicating data between different platforms and Oracle Database releases, and across a wide area network (WAN).

##### Oracle Streams Information Flow

The architecture of Oracle Streams is very flexible. Figure 17-7 depicts the basic information flow in a replication environment.

Figure 17-7 Oracle Streams Information Flow

![Figure 17-7 Oracle Streams Information Flow](img/cncpt200.gif)

> The image cncpt200.gif shows the Streams information flow as a series of arrows. First is the capture phase, then staging, and then consumption.
>
> End of description.
>
> [Copyright © 1993, 2015, Oracle and/or its affiliates. All rights reserved.](https://docs.oracle.com/cd/E11882_01/dcommon/html/cpyr.htm)
  

As shown in Figure 17-7, Oracle Streams contains the following basic elements:

- Capture
	Oracle Streams can implicitly capture DML and DDL changes. Rules determine which changes are captured. Changes are formatted into logical change records (LCRs), which are messages with a specific format describing a database change.
- Staging
	LCRs are placed in a staging area, which is a queue that stores and manages captured messages. Message staging provides a holding area with security, as well as auditing and tracking of message data. Propagations can send messages from one queue to another. The queues can reside in the same or different databases.
- Consumption
	LCRs remain in a staging area until subscribers consume them implicitly or explicitly. An apply process implicitly applies changes encapsulated in LCRs.

Note:

Oracle Streams is fully inter-operational with [materialized views](glossary.md), which you can use to maintain updatable or read-only copies of data (see ["Overview of Materialized Views"](schemaob.md)).

See Also:

[Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_repcont.htm#TDPII065) to learn how to replicate data using Oracle Streams

##### Oracle Streams Replication Environments

Oracle Streams enables you to configure many different types of custom replication environments. However, the following types of replication environments are the most common:

- Two-Database
	Only two databases share the replicated database objects. The changes made to replicated database objects at one database are captured and sent directly to the other database, where they are applied.
	In a one-way replication environment, only one database allows changes to the replicated database objects, with the other database containing read-only replicas of these objects. In a bi-directional replication environment, both databases can allow changes to the replicated objects. In this case, both databases capture changes to these database objects and send the changes to the other database, where they are applied.
- Hub-and-Spoke
	A central database, or hub, communicates with secondary databases, or spokes. The spokes do not communicate directly with each other. In a hub-and-spoke replication environment, the spokes might or might not allow changes to the replicated database objects.
- N-Way
	Each database communicates directly with every other database in the environment. The changes made to replicated database objects at one database are captured and sent directly to each of the other databases in the environment, where they are applied.

See Also:

[Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_repcont.htm#TDPII077) to learn more about common replication environments

#### Oracle Streams Advanced Queuing (AQ)

Oracle Streams Advanced Queuing (AQ) is a robust and feature-rich message queuing system integrated with Oracle Database. When an organization has different systems that must communicate with each other, a messaging environment can provide a standard, reliable way to transport critical information between these systems.

A sample use case is a business that enters orders in an Oracle database at headquarters. When an order is entered, the business uses AQ to send the order ID and order date to a database in a warehouse. These messages alert employees at the warehouse about the orders so that they can fill and ship them.

##### Message Queuing and Dequeuing

Advanced Queuing stores user messages in abstract storage units called queues. Enqueuing is the process by which producers place messages into queues. Dequeuing is the process by which consumers retrieve messages from queues.

Support for explicit dequeue allows developers to use Oracle Streams to reliably exchange messages. They can also notify applications of changes by leveraging the change capture and propagation features of Oracle Streams.

Figure 17-8 shows a sample application that explicitly enqueues and dequeues messages through Advanced Queuing, enabling it to share information with partners using different messaging systems. After being enqueued, messages can be transformed and propagated before being dequeued to the partner's application.

Figure 17-8 Oracle Streams Message Queuing

![Figure 17-8 Oracle Streams Message Queuing](img/cncpt310.gif)

> This figure shows an application that explicitly enqueues and dequeues messages through Oracle Streams Advanced Queuing as a method of sharing information with business partners or customers with different messaging systems. Once enqueued, messages can be transformed and propagated as desired, before being dequeued to a business partner's application that is a non-database oriented messaging systems.
>
> End of figure description.
  

##### Advanced Queuing Features

Oracle Streams Advanced Queuing supports all the standard features of message queuing systems. These features include:

- Asynchronous application integration
	Oracle Streams Advanced Queuing offers several ways to enqueue messages. A capture process or synchronous capture can capture the messages implicitly, or applications and users can capture messages explicitly.
- Extensible integration architecture
	Many applications are integrated with a distributed hub and spoke model with Oracle Database as the hub. The distributed applications on an Oracle database communicate with queues in the same hub. Multiple applications share the same queue, eliminating the need to add queues to support additional applications.
- Heterogeneous application integration
	Advanced Queuing provides applications with the full power of the Oracle type system. It includes support for scalar data types, Oracle Database object types with inheritance, `XMLType` with additional [operators](glossary.md) for XML data, and `ANYDATA`.
- Legacy application integration
	The Oracle Messaging Gateway integrates Oracle Database applications with other message queuing systems, such as Websphere MQ and Tibco.
- Standards-Based API support
	Oracle Streams Advanced Queuing supports industry-standard APIs: SQL, JMS, and SOAP. Changes made using SQL are captured automatically as messages.

See Also:

- [Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_messaging.htm#TDPII026) to learn how to send messages using Advanced Queuing
- [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/aq_intro.htm#ADQUE0100)

#### Oracle Streams Use Case

For a sample use case, assume that a company uses Oracle Streams to maintain multiple copies of a corporate Web site. The business requirements include:

- A reporting database must contain the most current data for analysts in a New York office to perform ad hoc querying.
- Updatable materialized views must support the field sales staff.
- Data must be shared with applications hosted on a Sybase database.

Figure 17-9 illustrates this Streams configuration.

Figure 17-9 Streams Configuration

![Figure 17-9 Streams Configuration](img/cncpt199.gif)

> This graphic shows four database icons labeled London, Tokyo, NY, and Report. The first three databases are connected by arrows going in both directions. A single arrow points from NY to Report. NY also points to a Gateway icon attached to a Sybase icon. The London database is connected through three double-headed arrows to a set of four client icons.
>
> End of figure description.
  

Oracle Streams is used to replicate data in an n-way configuration consisting of sites in New York, London, and Tokyo. At each site, Streams implicit capture collects any changes that occur for subscribed tables in each local region, and stages them locally in the queue. Changes captured in each region are then forwarded to each of the other region's databases. Changes made at each database can be reflected at every other database, providing complete data for the subscribed objects throughout the world.

At each regional database, an Oracle Streams apply process applies the changes automatically. As changes are applied, Oracle Streams checks for and resolves any conflicts. Streams can also be used to exchange data for particular tables with non-Oracle databases. Using the Oracle Database Gateway for Sybase, a Streams apply process applies the changes to a Sybase database using the same mechanisms as it does for Oracle databases.

The reporting database is hosted in New York. This database is a fully functional Oracle database that has a read-only copy of the relevant application tables. The reporting site is not configured to capture changes on these application tables. Oracle Streams imposes no restrictions on the configuration or use of this reporting database.

The London site also serves as the master site for several updatable materialized view sites. Each salesperson receives an updatable copy of the required portion of data. These sites typically only connect once a day to upload their orders and download any changes made after their last refresh.

See Also:

[Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_repcont.htm#TDPII192) for examples of configuring Oracle Streams

---

Footnote Legend

Footnote 1: Building the Data Warehouse, John Wiley and Sons, 1996.