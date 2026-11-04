---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/changes-in-this-release-for-oracle-automatic-storage-management-administrators-guide.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Changes in This Release for Oracle Automatic Storage Management Administrators Guide

## Changes in Oracle Automatic Storage Management 19c

Oracle ASM 19c introduces stricter permission checks for file-group and file-movement operations, enhanced SRVCTL management of ASM network resources, password-file metadata cache flushing, and ASMCMD improvements including optional password creation, forced replacement and format options, sparse-parent assignment, and file-group movement. It also adds parity-protected file support through `REDUNDANCY` settings for single or double parity. The `pwcreate` password option is deprecated, and Flex Cluster leaf nodes are desupported.

Read More: [Changes in Oracle Automatic Storage Management 19c](changes-in-oracle-automatic-storage-management-19c.md)

## Changes in Oracle ACFS and Oracle ADVM in Oracle ASM 19c

Oracle ACFS 19c enhances diagnostic commands and views, supports online `fsck` analysis on Linux, and improves replication by allowing most replication commands for non-root ASM users and enabling remote standby termination. Deprecated capabilities include replication protocol version 1, ACFS encryption on Solaris and Windows, ACFS on Windows, ACFS Security (Vault), ACFS Auditing, ACFS on Member Clusters, and Cluster Domain Member Clusters; these may be removed in future releases, with ASM, DBFS, or Windows shares suggested as alternatives for Windows ACFS use.

Read More: [Changes in Oracle ACFS and Oracle ADVM in Oracle ASM 19c](changes-in-oracle-acfs-and-oracle-advm-in-oracle-asm-19c.md)