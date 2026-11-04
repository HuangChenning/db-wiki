---
title: Database Development Guide
book: Database Development Guide
doc_id: F31304-06
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/adfns/release-changes.html
tags:
  - oracle
  - 21c
  - development-guide
---

This is a summary of important changes in the Oracle Database Development Guide Release 21c.

### 1.1 New Features

The following are the new features in Oracle Database Development Guide for Oracle Database Release 21c.

#### 1.1.1 Manage DRCP for Individual PDBs

Starting with Oracle Database 21c, Database Resident Connection Pool (DRCP) can be configured and managed for individual PDBs.

In previous releases, DRCP could only be configured for the entire container database (CDB). This feature eases DRCP management by enabling you to configure and manage the DRCP pool for each pluggable database. This change enables tenant administrators to configure and manage independent tenant-specific pools.

This feature is enabled by a new database parameter, `ENABLE_PER_PDB_DRCP`.

See [Using Database Resident Connection Pool](performance-and-scalability.md) for more information

#### 1.1.2 Application Continuity Enhancements

Application Continuity has the following major enhancements:

- The Application Continuity Protection Check (ACCHK) feature generates Application Continuity coverage reports and database views that describe the protection of your application by Application Continuity.
- Planned Failover migrates sessions using Application Continuity when the session is ready to failover. This is automatic and is applied during planned maintenance and load rebalancing. This feature increases the coverage for sessions drained and migrated.
- A new service attribute, RESET\_STATE is introduced. The resetting of state is an important feature that clears the session state set by the application in a request at the end of request, saving application development effort. This improvement also increases coverage of Transparent Application Continuity (TAC) as the session state is clean for the beginning of the next request.

See [About Application Continuity](high-availability.md) for more information

#### 1.1.3 Automatic Reset of Session State

This important feature clears session state set by the application in a request.

You can use `RESET_STATE` to clean the state automatically at the end of a request:
- Cursors are cancelled
- PL/SQL globals are cleared
- Session duration temporary tables are truncated
- Session duration temporary lobs are cleared
`RESET_STATE` also improves your protection when using Transparent Application Continuity as session state is clean at the beginning of every request. You can use `RESET_STATE` when you set `FAILOVER_TYPE` to `TRANSACTION` or `AUTO`.

See [About Application Continuity](high-availability.md) for more information

#### 1.1.4 New OCI Registration Mode for Change Query Notifications

Applications can use client initiated connection mode to register and receive Change Query Notification(CQN).

Starting from Oracle Database release 19c, version 19.1, a new OCI registration mode has been designed to work with applications in the cloud. This new mode also works for applications running on premises. In this mode of notification delivery, the client application initiates a connection to the Oracle database server for receiving notifications. Client initiated connections do not need special network configuration, are easy to use and secure.

See [Using OCI for Client Initiated CQN Registrations](cqn.md) for more information

#### 1.1.5 Unified Auditing on an Editioned Object Now Applies to All Its Editions

Unified audit policies, if configured on an editioned object, applies to all editions of the object.

When an object is actualized in an edition, it will inherit the audit policies from an existing edition.

This support enables to have consistent audit policy definition and enforcement in all object editions, whether existing or new. Applications which rely on edition-based redefinition can take advantage of the availability of the audit policies to audit all editioned objects across editions in a consistent manner.

See [Editions and Audit Policies](editions.md) for more information

#### 1.1.6 Security Update for Native Encryption

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

See Also:

- [Choosing Between Native Network Encryption and Transport Layer Security](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=DBSEG-GUID-8F489523-9693-4147-ADFD-C05246C98790) in Oracle Database Security Guide
- [Improving Native Network Encryption Security](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/adfns&id=DBSEG-GUID-19089E9B-6FDE-44C2-8D79-DCFAF33E91BC) in Oracle Database Security Guide

### 1.2 Deprecated Feature

The following is the deprecated feature in Oracle Database Development Guide for Oracle Database Release 21c.

Oracle Database Extensions for.NET is deprecated

Oracle Database Extensions for.NET is deprecated in Oracle Database 21c. Oracle recommends that you either place.NET code in the middle tier, or use the External Procedures feature, or rewrite the code using PL/SQL or Java.