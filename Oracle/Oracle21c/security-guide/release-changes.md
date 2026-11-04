---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/release-changes.html
tags:
  - oracle
  - 21c
  - security-guide
---

This preface contains:

### Changes in Oracle Database Security 21c

Oracle Database Security Guide for Oracle Database 21c has new security features.

- New and Updated Password User Profiles for STIG and CIS  
	This release introduces a new user profile and an updated user profile to comply with STIG and CIS standards for password management.
- Gradual Database Password Rollover for Applications  
	Starting with this release, an application can change its database passwords without an administrator having to schedule downtime.
- Force Upgraded Password File to be Case Sensitive  
	Starting with this release, the parameter to enable or disable password file case sensitivity is removed. All passwords in new password files are case-sensitive.
- Minimum Password Length Enforcement for All PDBs  
	Starting with this release, you can enforce a minimum password length on all PDBs by creating a mandatory profile in the CDB root.
- Ability to Specify the Location of the CMU Wallet and dsi.ora File with a Database Property  
	You now can specify a location of centrally managed users (CMU) wallet and `dsi.ora` files for an individual PDB by using a database property on the PDB.
- Addition of USER\_APPLICATION\_ROLES Data Dictionary View  
	Starting with this release, the `USER_APPLICATION_ROLES` data dictionary view will provide a subset of roles that are available in `DBA_APPLICATION_ROLES` that only apply to the current user.
- Windows Authentication No Longer Uses NTLM by Default  
	For Microsoft Windows installations with `AUTHENTICATION_SERVICES=NTS`, starting with this release, the `SQLNET.NO_NTLM` parameter setting in the `sqlnet.ora` file will default to `TRUE`.
- New System Privilege and Initialization Parameter for Diagnostic Events  
	This release introduces better security controls for the setting of debug-events (events++, error-numbers) and debug-actions through `ALTER SESSION` and `ALTER SYSTEM` operations.
- Ability to Use Multiple Kerberos Principals with a Single Database Client  
	Starting with this release, when you configure Kerberos authentication for an Oracle Database client, you can specify multiple Kerberos principals with a single Oracle Database client.
- Multiple Wallet Support for Distinct SSL Connections in One Process  
	Starting with this release, you can configure database clients to maintain multiple Secure Sockets Layer (SSL) sessions using different SSL certificates.
- Oracle Database Connections to Kerberos Servers Now Default to TCP  
	In previous releases, Oracle Database connections to Kerberos servers defaulted to start with User Datagram Protocol (UDP).
- Updated Support for Micro Edition Suite (MES) for FIPS 140.2  
	Starting with this release, Oracle Database supports Micro Edition Suite (MES) version 4.5 for FIPS 140.2.
- Oracle SQL\*Loader Support for Object Store Credentials  
	Starting with this release, Oracle SQL\*Loader accesses data in an object store by presenting user-defined credentials.
- Unified Audit Policy Configuration Changes Effective Immediately  
	Starting with this release, changes that are made to a unified audit policy will become effective immediately in the current session and in all other on-going active sessions.
- Support for DBMS\_CRYPTO Asymmetric Key Operations  
	Starting with this release, the `DBMS_CRYPTO` PL/SQL package supports asymmetric key operations, in addition to the existing support for symmetric key operations.
- Predefined Unified Audit Policies for Security Technical Implementation Guide Compliance  
	Starting with this release, you can audit for Security Technical Implementation Guide (STIG) compliance by using new predefined unified audit policies.
- Unified Audit Policies Enforced on the Current User  
	Starting with this release, unified audit policies are enforced on the current user who executes the SQL statement.
- Auditing for Oracle XML DB HTTP and FTP Services  
	Starting with this release, you can create unified audit policies for database connections made using the database protocol servers for HTTP, HTTPS, and FTP.
- Unified Auditing on an Editioned Object Now Applies to All Its Editions  
	Starting with this release, unified audit policies, if configured for auditing actions on an editioned object, apply to all editions of the object.
- Deprecation of Traditional Auditing  
	Starting with this release, traditional auditing is deprecated. Oracle recommends that you use unified auditing, which enables selective and more effective auditing inside Oracle Database.

**Parent topic:** Changes in This Release for Oracle Database Security Guide

#### New and Updated Password User Profiles for STIG and CIS

This release introduces a new user profile and an updated user profile to comply with STIG and CIS standards for password management.

The `ORA_STIG_PROFILE` user profile has been updated with the latest Security Technical Implementation Guide's (STIG) guidelines, and the `ORA_CIS_PROFILE`, new for this release, has the latest Center for Internet Security (CIS) guidelines for passwords.

You can use these user profiles directly with their database users or use them as part of your own user profiles. Oracle keeps these profiles up to date to make it easier for you to implement password policies that meet STIG and CIS guidelines.

#### Gradual Database Password Rollover for Applications

Starting with this release, an application can change its database passwords without an administrator having to schedule downtime.

To accomplish this, a database administrator can associate a profile having a non-zero limit for the `PASSWORD_ROLLOVER_TIME` password profile parameter, new with this release, with an application schema. This allows the database password of the application user to be altered while allowing the older password to remain valid for the time specified by the `PASSWORD_ROLLOVER_TIME` limit. During the rollover period of time, the application instance can use either the old password or the new password to connect to the database server. When the rollover time expires, only the new password is allowed.

Before this enhancement, an administrator normally took the application down when the application database password was being rotated. This is because the password update requires changes on both the database and the application side. With the gradual database password rollover enhancement, the application can continue to use the older password until the new password is configured in the application.

In addition to the new clause `PASSWORD_ROLLOVER_TIME` in the `CREATE PROFILE` and `ALTER PROFILE` statements, the `ALTER USER` statement has a new clause, `EXPIRE PASSWORD ROLLOVER PERIOD`. The `ACCOUNT_STATUS` column of the `DBA_USERS` and `USER_USERS` data dictionary views have several new statuses indicating values to indicate rollover status.

#### Force Upgraded Password File to be Case Sensitive

Starting with this release, the parameter to enable or disable password file case sensitivity is removed. All passwords in new password files are case-sensitive.

Case-sensitive password files provide more security than older password files that are case insensitive. Oracle recommends that you use case-sensitive password files. However, upgraded password files from earlier Oracle Database releases can retain their original case-insensitivity. You can force your password files to be case-sensitive by migrating password files from one format to another.

#### Minimum Password Length Enforcement for All PDBs

Starting with this release, you can enforce a minimum password length on all PDBs by creating a mandatory profile in the CDB root.

The mandatory profile is a generic profile and can only have the `PASSWORD_VERIFY_FUNCTION` parameter in the `CREATE MANDATORY PROFILE` statement to define the password limit.

This profile adds a minimum password length to the local profiles with which the PDB user is associated. Because a common user sets the mandatory profile in the CDB, a PDB administrator cannot remove the password length requirement from local profiles and allow users to set insecure short passwords.

#### Ability to Specify the Location of the CMU Wallet and dsi.ora File with a Database Property

You now can specify a location of centrally managed users (CMU) wallet and `dsi.ora` files for an individual PDB by using a database property on the PDB.

This enhancement enables a PDB administrator to specify a location to store these files rather than being limited by the `sqlnet.ora` `WALLET_LOCATION` parameter or having to use the default wallet locations. This feature works almost exactly as using `WALLET_LOCATION` or the default wallet location except that users with administrative privileges will not be able to start the database because directory objects are part of the database. To store the CMU wallet and `dsi.ora` files in the location path specified by a database directory object, you must set the `CMU_WALLET` database property to this directory object.

After you have set the `CMU_WALLET` database property to a directory object for an individual PDB, you should store the CMU wallet and `dsi.ora` files for this PDB in the location specified by the directory object, so that they can be accessed through the corresponding file systems.

#### Addition of USER\_APPLICATION\_ROLES Data Dictionary View

Starting with this release, the `USER_APPLICATION_ROLES` data dictionary view will provide a subset of roles that are available in `DBA_APPLICATION_ROLES` that only apply to the current user.

`USER_APPLICATION_ROLES` enables the current user to see all the application roles that have been granted to the user instead of the list of all possible application roles available in `DBA_APPLICATION_ROLES`.

#### Windows Authentication No Longer Uses NTLM by Default

For Microsoft Windows installations with `AUTHENTICATION_SERVICES=NTS`, starting with this release, the `SQLNET.NO_NTLM` parameter setting in the `sqlnet.ora` file will default to `TRUE`.

In previous releases, the default for this parameter was `FALSE`. `SQLNET.NO_NTLM` controls whether NTLM can be used with NTS authentication. A `TRUE` setting means that NTLM cannot be used in NTS authentication. Because NTLM does not normally provide mutual authentication and is hence less secure, a `TRUE` setting for `SQLNET.NO_NTLM` makes the database and client more secure.

The `SQLNET.NO_NTLM` parameter is used on both the server and the client. If you have upgraded a Microsoft Windows installation of an Oracle database or a client in which `SQLNET.NO_NTLM` had not been set, then its default will be `TRUE`.

#### New System Privilege and Initialization Parameter for Diagnostic Events

This release introduces better security controls for the setting of debug-events (events++, error-numbers) and debug-actions through `ALTER SESSION` and `ALTER SYSTEM` operations.

To support this enhancement, the following features are available:

- `ENABLE DIAGNOSTICS` system privilege
- `DIAGNOSTICS_CONTROL` initialization parameter

Some debug-events and debug-actions are not safe and should be exposed to users with caution. In previous releases, privilege control for the usage of these diagnostics was not sufficient. With this new privilege control, regular users can be blocked from using these diagnostics to better support separation of duty.

#### Ability to Use Multiple Kerberos Principals with a Single Database Client

Starting with this release, when you configure Kerberos authentication for an Oracle Database client, you can specify multiple Kerberos principals with a single Oracle Database client.

To enable this functionality, you will need to create a separate credential cache for each user in the client and then use the connect string to specify the user.

In previous releases, you were restricted to one Kerberos principal for each Oracle Database client.

#### Multiple Wallet Support for Distinct SSL Connections in One Process

Starting with this release, you can configure database clients to maintain multiple Secure Sockets Layer (SSL) sessions using different SSL certificates.

This feature allows multi-threaded clients use multiple wallets with different certificates for simultaneous SSL sessions.

This enhancement enables the database client to connect simultaneously with different external identities. This allows multi-threaded clients to use multiple wallets with different certificates for simultaneous SSL sessions.

#### Oracle Database Connections to Kerberos Servers Now Default to TCP

In previous releases, Oracle Database connections to Kerberos servers defaulted to start with User Datagram Protocol (UDP).

If you prefer the Oracle Database connections to start with UDP connections, then you can modify the Kerberos `krb5.conf` configuration file to start the connections using UDP.

This enhancement speeds the authentication process for environments that have many Kerberos Key Distribution Center (KDC) servers.

#### Updated Support for Micro Edition Suite (MES) for FIPS 140.2

Starting with this release, Oracle Database supports Micro Edition Suite (MES) version 4.5 for FIPS 140.2.

The Micro Edition Suite (MES) version 4.5 updates include four new CVEs in the RSA BSAFE MES library, support for the rules that FIPS 140.2 requires, and access to the updated NZ/ZT library from the Crypto Foundation.

This enhancement enables the Oracle Database FIPS 140.2 configuration to benefit from new features and security improvements available from the latest RSA BSAFE MES library.

#### Oracle SQL\*Loader Support for Object Store Credentials

Starting with this release, Oracle SQL\*Loader accesses data in an object store by presenting user-defined credentials.

Oracle SQL\*Loader now enables you to specify credentials that you define allowing files in an object store to be loaded into an Oracle database.

#### Unified Audit Policy Configuration Changes Effective Immediately

Starting with this release, changes that are made to a unified audit policy will become effective immediately in the current session and in all other on-going active sessions.

In previous releases, users who were affected by a changed unified audit policy had to log out of and then back into the session in order for the unified audit policy to take effect.

#### Support for DBMS\_CRYPTO Asymmetric Key Operations

Starting with this release, the `DBMS_CRYPTO` PL/SQL package supports asymmetric key operations, in addition to the existing support for symmetric key operations.

To implement the support for asymmetric key operations, the following procedures have been added to the `DBMS_CRYPTO` package:

- `PKENCRYPT`
- `PKDECRYPT`
- `SIGN`
- `VERIFY`

#### Predefined Unified Audit Policies for Security Technical Implementation Guide Compliance

Starting with this release, you can audit for Security Technical Implementation Guide (STIG) compliance by using new predefined unified audit policies.

These polices are as follows:

- `ORA_STIG_RECOMMENDATIONS`
- `ORA_ALL_TOPLEVEL_ACTIONS`
- `ORA_LOGON_LOGOFF`

#### Unified Audit Policies Enforced on the Current User

Starting with this release, unified audit policies are enforced on the current user who executes the SQL statement.

In previous releases, unified audit policies were enforced on the user who owned the top-level user session (that is, the login user session) in which the SQL statement is executed.

Scenarios in which the current user is different from the login user include but is not limited to the following:

- Trigger execution
- Definer rights procedure execution
- Functions and procedures that are executed during the evaluation of views

#### Auditing for Oracle XML DB HTTP and FTP Services

Starting with this release, you can create unified audit policies for database connections made using the database protocol servers for HTTP, HTTPS, and FTP.

A unified audit policy can track requests that have been made to servlets, such as those used by Oracle Enterprise Manager Express, Oracle Database Native Web Services, and HTTP and FTP that use the Oracle XML DB Repository.

This enhancement enables you to track and monitor access to Oracle Database provided by the HTTP, HTTPS, and FTP protocols, including access by WebDAV clients

#### Unified Auditing on an Editioned Object Now Applies to All Its Editions

Starting with this release, unified audit policies, if configured for auditing actions on an editioned object, apply to all editions of the object.

This support enables to have consistent audit policy definition and enforcement in all object editions, whether existing or new. Applications which rely on edition-based redefinition can take advantage of the availability of the audit policies to audit all editioned objects in a consistent manner.

#### Deprecation of Traditional Auditing

Starting with this release, traditional auditing is deprecated. Oracle recommends that you use unified auditing, which enables selective and more effective auditing inside Oracle Database.

Oracle introduced unified auditing with Oracle Database 12c. In addition to providing built-in audit operation support, unified auditing simplifies management of auditing within the database, provides the ability to accelerate auditing based on conditions, and increases the security of audit data generated by the database. Unified auditing and traditional auditing (mixed mode) has been the default auditing mode from Oracle Database 12c onward. Mixed mode auditing was offered to enable you to become familiar with unified auditing, and to transition from traditional auditing. With the deprecation of traditional auditing in this release, Oracle recommends that you migrate to unified auditing.

### Updates to Oracle Database Security 21c

Oracle Database release 21c has one new security update that applies to all releases starting from release 11.2.

- Security Update for Native Encryption  
	Oracle provides a patch that you can download to address necessary security enhancements that affect native network encryption environments in Oracle Database release 11.2 and later.
- Ability to Configure Transport Layer Security Connections without Client Wallets  
	Available in Oracle Database release 19.14, an Oracle Database client will not be required to provide a wallet to hold well-known CA root certificates if they are available elsewhere in the local system.

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

#### Ability to Configure Transport Layer Security Connections without Client Wallets

Available in Oracle Database release 19.14, an Oracle Database client will not be required to provide a wallet to hold well-known CA root certificates if they are available elsewhere in the local system.

Transport Layer Security (TLS) encryption requires either one-way authentication or two-way authentication. In one-way authentication (the default), which is commonly used for HTTPS connections, the server certificate is verified using well-known root CA certificates that are already available in local systems. Starting in this release, you will no longer need to install and configure a wallet to hold a well-known root certificate if it is already available in the local system.

This enhancement greatly simplifies the Oracle Database client installation and the use of TLS protocol to encrypt Oracle Database client-server communications.