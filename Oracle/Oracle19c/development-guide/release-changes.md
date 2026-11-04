---
title: Database Development Guide
book: Database Development Guide
doc_id: E96334-10
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/adfns/release-changes.html
tags:
  - oracle
  - 19c
  - development-guide
---

## Changes in Oracle Database Release 19c

The following are changes in Oracle Database Development Guide for Oracle Database Release 19c.

### New Features

New features in this release for Oracle Database Development Guide.

#### New OCI Registration Mode for Change Query Notifications

Applications can use client initiated connection mode to register and receive Change Query Notification(CQN).

Starting from Oracle Database release 19c, version 19.1, a new OCI registration mode has been designed to work with applications in the cloud. This new mode also works for applications running on premises. In this mode of notification delivery, the client application initiates a connection to the Oracle database server for receiving notifications. Client initiated connections do not need special network configuration, are easy to use and secure.

See [Using OCI for Client Initiated CQN Registrations](cqn.md) for more information

### Deprecated Features

This section lists the deprecated features that were part of Database Development Guide.

Features Deprecated in Oracle Database 19c

Oracle Fail Safe is deprecated. It can be desupported and unavailable in a future release.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=UPGRD-GUID-FB1CB9F6-F520-4772-9DBF-24CD70D0D628) for more information.

Security Update for Native Encryption

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

- [Choosing Between Native Network Encryption and Transport Layer Security](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=DBSEG-GUID-8F489523-9693-4147-ADFD-C05246C98790) in Oracle Database Security Guide
- [Improving Native Network Encryption Security](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=DBSEG-GUID-19089E9B-6FDE-44C2-8D79-DCFAF33E91BC) in Oracle Database Security Guide

### Desupported Features

Desupported Features in Oracle Database 19c

Oracle Multimedia has been desupported in its entirety. Oracle recommends that you store multimedia content in SecureFiles LOBs and use third-party products.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/adfns&id=UPGRD-GUID-BABC1C60-EA07-4EBE-8C67-B69B59E4F742) for more information.