---
title: Database Security Guide
book: Database Security Guide
doc_id: E85682-14
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dbseg/release-changes.html
tags:
  - oracle
  - 12c
  - security-guide
---

This preface contains:

- Changes in Oracle Database Security 12c Release 2 (12.2.0.1)
- Updates to Oracle Database Security 12.2

### Changes in Oracle Database Security 12c Release 2 (12.2.0.1)

Oracle Database Security Guide for Oracle Database 12c release 2 (12.2.0.1) has both new and deprecated security features.

- New Features
- Deprecated Features

**Parent topic:** Changes in This Release for Oracle Database Security Guide

#### New Features

The following features are new for this release:

- Ability to Create Application Common Objects, Users, Roles, and Profiles  
	You now can create application common objects (metadata-linked and object-linked), users, roles, and profiles.
- Application Container Security Features  
	Application containers affect several default security features, such as privilege grants to application common users, how application contexts are used, and so on.
- Addition of SYSRAC Administrative Privilege for Oracle Real Application Clusters  
	Starting with this release, the Oracle Real Applications (Oracle RAC) clusterware agent that manages Oracle RAC uses the `SYSRAC` administrative privilege.
- Administrative User Authentication Enhancements  
	Administrative user account authentication now has enhancements for password files, password profile parameters, Secure Sockets Layer (SSL), Kerberos, and multitenant environments.
- Enhancements for the Management of Administrative Passwords  
	This release introduces better security for the management of administrative passwords, by enforcing the associated administrative user’s profile password limits.
- STIG Compliance Features  
	To meet Security Technical Implementation Guide (STIG) compliance, Oracle Database now provides two new user security features.
- Better Security for Password Versions  
	In this release, Oracle Database provides several enhancements for password authentication versions.
- Ability to Automatically Lock Inactive Database User Accounts  
	Starting with this release, you can configure user accounts to automatically lock if they have been inactive over a period of time.
- More Flexibility in Controlling Database Link Access  
	Starting with this release, you have greater control in managing database link access by users.
- Ability to Control Definer's Rights Privileges for Database Links  
	The `INHERIT REMOTE PRIVILEGES` and `INHERIT ANY REMOTE PRIVILEGES` privileges control definer’s rights privileges for procedures that users accesse through a database link.
- PDB Lockdown Profiles to Restrict Operations on PDBs  
	In a multitenant environment, you now can use PDB lockdown profiles to restrict functionality available to users in a given PDB.
- Ability to Set the Identity of the Operating System User for PDBs  
	For multitenant environments, the `PDB_OS_CREDENTIAL` initialization parameter enables a different operating system user to execute external procedures using the `EXTPROC` process.
- Updated Kerberos Utilities  
	Oracle Database now supports the updated version of the Kerberos tools from MIT Kerberos 1.8.
- Additional Security Feature Support for Transparent Sensitive Data Protection  
	You now can create Transparent Sensitive Data Protection policies to use unified auditing policies, fine-grained auditing policies, and Transparent Data Encryption column encryption.
- Ability to Enable Unified Auditing for Groups of Users Through Roles  
	Starting with this release, you can enable audit policies on database roles.
- New Audit Events for Oracle Database Real Application Security  
	This release provides two new audit events for Oracle Real Application Security unified audit policies.
- Ability to Capture Oracle Virtual Private Database Predicates in the Audit Trail  
	Oracle Virtual Private Database (VPD)-generated predicates now can be captured in the audit trail.
- Enhancements for the AUDSYS Audit Schema  
	The `AUDSYS` schema, which stores unified audit records, now has better security and better read performance for unified auditing.

**Parent topic:** Changes in Oracle Database Security 12c Release 2 (12.2.0.1)

##### Ability to Create Application Common Objects, Users, Roles, and Profiles

You now can create application common objects (metadata-linked and object-linked), users, roles, and profiles.

These common objects reside in the application root. This guide explains how to manage security for application common users, roles, and profiles.

##### Application Container Security Features

Application containers affect several default security features, such as privilege grants to application common users, how application contexts are used, and so on.

The following functionality is affected:

- Application common users: In addition to other privileges, you can grant the `SYSDBA` and `SYSOPER` administrative privileges to application common users.
- Application contexts: When you create an application in the application root, you can create an application context for use with this application. This application context resides in the application root.
- Oracle Virtual Private Database: You can create Virtual Private Database policies that protect application common objects. These policies reside in the application root.
- Transparent Sensitive Data Protection: You can apply Transparent Sensitive Data Protection (TSDP) policies to the current pluggable database (PDB) or to the current application PDB only.
- Transport Layer Security: If you are using Secure Sockets Layer (SSL) and plan to use the upgraded version of SSL, which is Transport Layer Security (TLS), then you must ensure that each PDB is able to use its own wallet with its own certifications for TLS authentication.
- Auditing: In a multitenant environment for application containers, traditional, unified auditing, and fine-grained auditing are all affected by the use of application containers.

**Related Topics**

- [SYSDBA and SYSOPER Privileges for Standard Database Operations](configuring-privilege-and-role-authorization.md)
- [Oracle Virtual Private Database in a Multitenant Environment](using-oracle-vpd-to-control-data-access.md)
- [How a Multitenant Environment Affects Transparent Sensitive Data Protection](using-transparent-sensitive-data-protection.md)
- [Using Transport Layer Security in a Multitenant Environment](configuring-secure-sockets-layer-authentication.md)
- [Unified Audit Policies or AUDIT Settings in a Multitenant Environment](configuring-audit-policies.md)
- [Fine-Grained Auditing in a Multitenant Environment](configuring-audit-policies.md)

**Parent topic:** New Features

##### Addition of SYSRAC Administrative Privilege for Oracle Real Application Clusters

Starting with this release, the Oracle Real Applications (Oracle RAC) clusterware agent that manages Oracle RAC uses the `SYSRAC` administrative privilege.

##### Administrative User Authentication Enhancements

Administrative user account authentication now has enhancements for password files, password profile parameters, Secure Sockets Layer (SSL), Kerberos, and multitenant environments.

These enhancements are as follows:

- You can create password files for external users who have been granted the `SYSASM`, `SYSBACKUP`, `SYSDG`, and `SYSKM` administrative privileges in addition to the `SYSDBA` and `SYSOPER` administrative privileges. This enhancement is available in a multitenant environment, for both local and common external administrative users, and for external users in an SSL or Kerberos authentication configuration.
- The `SYSDG` administrative privilege can be used in a sharding environment.
- You can use password profile parameters, such as `PASSWORD_LIFE_TIME`, for administrative user authentication.

##### Enhancements for the Management of Administrative Passwords

This release introduces better security for the management of administrative passwords, by enforcing the associated administrative user’s profile password limits.

Examples of these profile limits are `FAILED_LOGIN_COUNT`, `PASSWORD_LOCK_TIME`, `PASSWORD_GRACE_TIME`, and `PASSWORD_LIFE_TIME`.

You now can create a password file that can apply to both administrative users and non-administrative users. When you create a password profile using the `PASSWORD_VERIFY_FUNCTION` clause of the `CREATE PROFILE` statement, this setting now applies to administrative users as well as non-administrative users, as long as you create the password file with the `ORAPWD` utility `FORMAT` parameter set to `12.2`.

In addition, for the `ORAPWD` utility, the restriction for the entries argument for the operating system password file has been removed.

##### STIG Compliance Features

To meet Security Technical Implementation Guide (STIG) compliance, Oracle Database now provides two new user security features.

These features are as follows:

- `ora12c_stig_verify_function` password complexity function
- `ora_stig_profile` user profile
- The following initialization parameters have changed to accommodate STIG requirements:
	- The default for `SEC_PROTOCOL_ERROR_FURTHER_ACTION` is now `(DROP,3)`.
		- The default for `SEC_MAX_FAILED_LOGIN_ATTEMPTS` is now `3`.
		- The default for `SQL92_SECURITY PARAMETER` is now `TRUE`.

##### Better Security for Password Versions

In this release, Oracle Database provides several enhancements for password authentication versions.

- The default for the `SQLNET.ALLOWED_LOGON_VERSION_SERVER` parameter is now `12` (Exclusive Mode) instead of `11`. A setting of `12` generates both `11G` and `12C` password versions. If you want to restrict the generation to the `12C` password version, which increases security for the passwords, then you can set `SQLNET.ALLOWED_LOGON_VERSION_SERVER` to `12a`.
	Be aware that you should check the versions of the clients that connect to the server to ensure that these clients use the `O5L_NP` ability. All Oracle Database release 11.2.0.3 and later clients have the `O5L_NP` ability. If you have an earlier Oracle Database client, then you must install the CPUOct2012 patch.
- The `12C` password version is now generated automatically. In previous releases, the `10G` password version was generated automatically.

See Also:

- [Managing Password Case Sensitivity](configuring-authentication.md)
- [Ensuring Against Password Security Threats by Using the 12C Password Version](configuring-authentication.md)
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=UPGRD-GUID-6428A98A-6621-4E49-89E5-FAFD51F04B60) for information about how password case sensitivity is affected by Oracle Database upgrades

**Parent topic:** New Features

##### Ability to Automatically Lock Inactive Database User Accounts

Starting with this release, you can configure user accounts to automatically lock if they have been inactive over a period of time.

The `CREATE USER` and `ALTER USER` SQL statements enable you to set a new profile parameter, `INACTIVE_ACCOUNT_TIME`, which enables you to automatically lock inactive accounts.

##### More Flexibility in Controlling Database Link Access

Starting with this release, you have greater control in managing database link access by users.

You can enable or disable database link access in the following areas:

- Protecting the database from man-in-the-middle attacks that access the database through database links: To control this functionality, you can set the `OUTBOUND_DBLINK_PROTOCOLS` initialization parameter.
- Controlling the ability of users to use LDAP to access data through global database links: You can set the `ALLOW_GLOBAL_DBLINKS` initialization parameter.

For more information, see [Network Connection Security](keeping-your-oracle-database-secure.md).

**Parent topic:** New Features

##### Ability to Control Definer's Rights Privileges for Database Links

The `INHERIT REMOTE PRIVILEGES` and `INHERIT ANY REMOTE PRIVILEGES` privileges control definer’s rights privileges for procedures that users accesse through a database link.

These privileges are similar to the `INHERIT PRIVILEGES` and `INHERIT ANY PRIVILEGES` privileges.

##### PDB Lockdown Profiles to Restrict Operations on PDBs

In a multitenant environment, you now can use PDB lockdown profiles to restrict functionality available to users in a given PDB.

PDB lockdown profiles enable you to restrict the access the user has to a set of features individually or in a group. This feature is designed to enhance security for situations in which identities are shared among PDBs.

##### Ability to Set the Identity of the Operating System User for PDBs

For multitenant environments, the `PDB_OS_CREDENTIAL` initialization parameter enables a different operating system user to execute external procedures using the `EXTPROC` process.

In the previous release, `EXTPROC` was used to create a credential object using `DBMS_CREDENTIAL` for authenticating and invoking external procedures. This functionality now is available on PDB level by associating a `CREDENTIAL` for the entire PDB, which will be automatically used for any `EXTPROC` external procedures executed by a database user in the PDB.

This feature enhances security for the multitenant environment by enabling each PDB to have its own operating system user account, instead of relying on one user, the `oracle` operating system user, for all PDBs in the environment. The root will continue to use the oracle operating system user account.

See [Configuring Operating System Users for a PDB](configuring-authentication.md) for more information.

**Parent topic:** New Features

##### Updated Kerberos Utilities

Oracle Database now supports the updated version of the Kerberos tools from MIT Kerberos 1.8.

In previous releases, Oracle clients needed to be manually configured by an administrator who configures a `krb5.conf` file. In this release, Oracle Database provides a generic `krb5.conf` file, which is used by default. The `kerb5.conf` file has parameters that enable realm and KDC information to be automatically retrieved from the DNS information. The auto-discovery of the realm and KDC information reduces the amount of work that you must perform to configure a client endpoint to use Kerberos.

This enhancement provides updates to the `okinit`, `oklist`, and `okdstry` Kerberos adapter command-line utilities, and provides a new utility, `okcreate`, which enables you to automate the creation of keytabs from either the KDC or a service endpoint.

##### Additional Security Feature Support for Transparent Sensitive Data Protection

You now can create Transparent Sensitive Data Protection policies to use unified auditing policies, fine-grained auditing policies, and Transparent Data Encryption column encryption.

In the previous release, you could create Transparent Sensitive Data Protection policies that use the Oracle Data Redaction and Oracle Virtual Private Database security features.

In addition, you now can use a separate wallet password for each pluggable database (PDB) in a multitenant environment so that each PDB is able to use its own wallet with its own certificates for Transparent Sensitive Data Protection authentication. The ability to specify a distinct wallet password for each PDB enables you to better restrict administrative access to the wallet. This functionality provides the necessary isolation between the tenants in a multitenant environment. These tenants can be individual companies or they can be different business units in a large corporation.

**Related Topics**

- [Using Transparent Sensitive Data Protection Policies with Unified Auditing](using-transparent-sensitive-data-protection.md)
- [Using Transparent Sensitive Data Protection Policies with Fine-Grained Auditing](using-transparent-sensitive-data-protection.md)
- [Using Transparent Sensitive Data Protection Policies with TDE Column Encryption](using-transparent-sensitive-data-protection.md)
- [Using Transport Layer Security in a Multitenant Environment](configuring-secure-sockets-layer-authentication.md)

**Parent topic:** New Features

##### Ability to Enable Unified Auditing for Groups of Users Through Roles

Starting with this release, you can enable audit policies on database roles.

This feature enables the policy to be in effect for all users who have been directly granted the role. The policy remains effective for the user as long as the user is granted the role, and as long as the role exists.

To accommodate this enhancement, the following changes have been made:

- The `AUDIT` and `NOAUDIT` statements now have a new clause, `BY USERS WITH GRANTED ROLES`.
- The `AUDIT_UNIFIED_ENABLED_POLICIES` and `DBA_XS_ENB_AUDIT_POLICIES` data dictionary views have the following new columns:
	- `ENTITY_NAME` captures the user name or role name.
		- `ENTITY_TYPE` indicates if the entity name is a `USER` or a `ROLE`.
		- `ENABLED_OPTION` displays `BY` and `EXCEPT` for policies that are enabled on users, but displays `INVALID` for policies that are enabled on roles.
- The possible output for the `AUDIT_UNIFIED_ENABLED_POLICIES.ENABLED_OPTION` column is now `BY USER`, `EXCEPT USER`, `BY GRANTED ROLE`, and `INVALID`.

##### New Audit Events for Oracle Database Real Application Security

This release provides two new audit events for Oracle Real Application Security unified audit policies.

- `AUDIT_GRANT_PRIVILEGE` audits use of the `GRANT_SYSTEM_PRIVILEGE` privilege.
- `AUDIT_REVOKE_PRIVILEGE` audits use of the `REVOKE_SYSTEM_PRIVILEGE` privilege.

##### Ability to Capture Oracle Virtual Private Database Predicates in the Audit Trail

Oracle Virtual Private Database (VPD)-generated predicates now can be captured in the audit trail.

This enhancement applies to the unified audit trail, fine-grained audit trail, and if unified auditing is not enabled, the standard audit trail (`DBA_AUDIT_TRAIL`). To accommodate this enhancement, the following data dictionary views have a new column, `RLS_INFO`:

- `UNIFIED_AUDIT_TRAIL`
- `DBA_AUDIT_TRAIL` (used for environments that are not yet migrated to unified auditing)
- `V$XML_AUDIT_TRAIL` (used for environments that are not yet migrated to unified auditing)
- `DBA_FGA_AUDIT_TRAIL` (used for environments that are not yet migrated to unified auditing)

If multiple VPD policies are enforced on a single object, then all of the VPD policy types, policy schema, policy names, and predicates are concatenated and stored in a single column. To separate the VPD predicate information for each VPD policy into individual rows in the view, a new PL/SQL package is available, `DBMS_AUDIT_UTIL`.

See Also:

- [Auditing of Oracle Virtual Private Database Predicates](configuring-audit-policies.md)
- [Fine-Grained Auditing on Tables or Views That Have Oracle VPD Policies](configuring-audit-policies.md)
- Oracle Database Reference for information about the [`UNIFIED_AUDIT_TRAIL`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=REFRN29162), [`DBA_AUDIT_TRAIL`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=REFRN23023), [`V$XML_AUDIT_TRAIL`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=REFRN30405), and [`DBA_FGA_AUDIT_TRAIL`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=REFRN23075) data dictionary views
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=ARPLS-GUID-681A56A3-BBDD-4A5B-871F-DC025870CAF3) for more information about the `DBMS_AUDIT_UTIL` PL/SQL package

**Parent topic:** New Features

##### Enhancements for the AUDSYS Audit Schema

The `AUDSYS` schema, which stores unified audit records, now has better security and better read performance for unified auditing.

In previous releases, users who had the `SELECT ANY TABLE` system privilege were able to query objects in the `AUDSYS` schema. Starting with this release, users who have this privilege are no longer able to query `AUDSYS` schema objects. Users who have been granted the `SELECT ANY DICTIONARY` system privilege can access objects in the `AUDSYS` schema.

In addition, a new internal table is available in the `AUDSYS` schema. This table stores the unified audit trail records and is designed to improve the read performance of the unified audit trail. If you migrated to unified auditing in the previous release and still have audit records in the previous location, then you can transfer the unified audit records that were created in that release to this new internal table. The `DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS` PL/SQL procedure, also new for this release, can be used to transfer these records to the new internal relational table.

See Also:

- [What Is Auditing?](introduction-to-auditing.md) for more information about the `AUDSYS` schema
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=UPGRD-GUID-4BC5F146-BF0D-4BCF-8A0B-1B67B767EEF1) for information about transferring unified audit records

**Parent topic:** New Features

#### Deprecated Features

The following features have been deprecated for this release:

- Deprecated Columns from the AUDIT\_UNIFIED\_ENABLED\_POLICIES and DBA\_XS\_ENB\_AUDIT\_POLICIES Views  
	The `USER_NAME` and `ENABLED_OPT` columns of the `AUDIT_UNIFIED_ENABLED_POLICIES` and `DBA_XS_ENB_AUDIT_POLICIES` data dictionary views are deprecated for this release.
- Deprecated Password Verification Functions  
	The `VERIFY_FUNCTION` and `VERIFY_FUNCTION_11G` password verify functions have been deprecated for this release.
- Deprecation of the UNIFIED\_AUDIT\_SGA\_QUEUE\_SIZE Initialization Parameter  
	The `UNIFIED_AUDIT_SGA_QUEUE_SIZE` initialization parameter has been deprecated.
- Deprecation of the CONTAINER\_GUID Parameter from the DBMS\_AUDIT\_MGMT Package  
	As part of an internal redesign to improve audit performance, the `CONTAINER_GUID` parameter has been deprecated from `DBMS_AUDIT_MGMT` PL/SQL package.
- Deprecation of Settings to Flush Audit Trail Records to Disk  
	You no longer need to manually flush audit records to disk because they are now automatically written to a new internal relational table.

**Parent topic:** Changes in Oracle Database Security 12c Release 2 (12.2.0.1)

##### Deprecated Columns from the AUDIT\_UNIFIED\_ENABLED\_POLICIES and DBA\_XS\_ENB\_AUDIT\_POLICIES Views

The `USER_NAME` and `ENABLED_OPT` columns of the `AUDIT_UNIFIED_ENABLED_POLICIES` and `DBA_XS_ENB_AUDIT_POLICIES` data dictionary views are deprecated for this release.

In this release, the `USER_NAME` column continues to show the names of users on whom the policy is enabled, but for policies that are enabled on roles, the `USER_NAME` column displays `NULL`.

The `ENABLED_OPT` column displays `BY` and `EXCEPT` for policies that are enabled on users, but displays `INVALID` for policies that are enabled on roles. This column is replaced by the `ENABLED_OPTION` column.

##### Deprecated Password Verification Functions

The `VERIFY_FUNCTION` and `VERIFY_FUNCTION_11G` password verify functions have been deprecated for this release.

These functions are deprecated because they enforce the weaker password restrictions from earlier releases. Instead, you should use the `ORA12C_VERIFY_FUNCTION` and `ORA12C_STRONG_VERIFY_FUNCTION` functions, which enforce stronger, more up-to-date password verification restrictions.

##### Deprecation of the UNIFIED\_AUDIT\_SGA\_QUEUE\_SIZE Initialization Parameter

The `UNIFIED_AUDIT_SGA_QUEUE_SIZE` initialization parameter has been deprecated.

This parameter is no longer necessary because starting with this release, Oracle Database auditing no longer depends on the system global area (SGA)-based queues to write unified audit records.

##### Deprecation of the CONTAINER\_GUID Parameter from the DBMS\_AUDIT\_MGMT Package

As part of an internal redesign to improve audit performance, the `CONTAINER_GUID` parameter has been deprecated from `DBMS_AUDIT_MGMT` PL/SQL package.

This parameter is no longer necessary. This deprecation affects the following `DBMS_AUDIT_MGMT` procedures:

- `DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL`
- `DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP`
- `DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP`

See Also:

- [Purging Audit Trail Records](administering-the-audit-trail.md)
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dbseg&id=ARPLS241) for more information about the `DBMS_AUDIT_MGMT` PL/SQL package

**Parent topic:** Deprecated Features

##### Deprecation of Settings to Flush Audit Trail Records to Disk

You no longer need to manually flush audit records to disk because they are now automatically written to a new internal relational table.

This enhancement enables the flushing process to bypass the common logging infrastructure queues. The deprecated settings are as follows:

- `DBMS_AUDIT_MGMT.FLUSH_UNIFIED_AUDIT_TRAIL` procedure
- `AUDIT_TRAIL_WRITE` mode of the `AUDIT_TRAIL_PROPERTY` parameter of the `DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY` procedure

### Updates to Oracle Database Security 12.2

Oracle Database release 12.2 has one new security update that applies to all releases starting from release 11.2.

- Security Update for Native Encryption  
	Oracle provides a patch that you can download to address necessary security enhancements that affect native network encryption environments in Oracle Database release 11.2 and later.

**Parent topic:** Changes in This Release for Oracle Database Security Guide

#### Security Update for Native Encryption

Oracle provides a patch that you can download to address necessary security enhancements that affect native network encryption environments in Oracle Database release 11.2 and later.

This patch is available in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).

The supported algorithms that have been improved are as follows:

- Encryption algorithms: AES128, AES192 and AES256
- Checksumming algorithms: SHA1, SHA256, SHA384, and SHA512

Algorithms that are deprecated and should not be used are as follows:

- Encryption algorithms: DES, DES40, 3DES112, 3DES168, RC4\_40, RC4\_56, RC4\_128, and RC4\_256
- Checksumming algorithm: MD5

If your site requires the use of network native encryption, then you must download the patch that is described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2). To enable a smooth transition for your Oracle Database installation, this patch provides two parameters that enable you to disable the weaker algorithms and start using the stronger algorithms. You will need to install this patch on both servers and clients in your Oracle Database installation.

An alternative to network native encryption is Transport Layer Security (TLS), which provides protection against person-in-the-middle attacks.