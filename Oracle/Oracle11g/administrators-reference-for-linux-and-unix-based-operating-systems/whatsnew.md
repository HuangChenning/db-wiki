---
title: "What's New in Oracle Database 11g Release 2 (11.2)"
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/whatsnew.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

This section describes new features that are available with Oracle Database 11g Release 2 (11.2).

## Oracle Database 11g Release 2 (11.2.0.3) New Features

The following new feature is provided with Oracle Database 11g Release 2 (11.2.0.3)

### TDE Hardware Acceleration for Oracle Solaris

Starting with Oracle Database 11g Release 2 (11.2.0.3), cryptographic hardware acceleration for TDE also works with Solaris 11 running on SPARC T3, SPARC T4, and Intel Xeon with AES-NI.

## Oracle Database 11g Release 2 (11.2.0.2) New Features

The following new feature is provided with Oracle Database 11g Release 2 (11.2.0.2).

### TDE Hardware Acceleration for Linux

Transparent Data Encryption (TDE) can automatically detect whether the database host system includes specialized cryptographic silicon that accelerates the encryption or decryption processing. When detected, TDE uses the specialized silicon for cryptographic processing accelerating the overall cryptographic performance significantly.

In Oracle Database 11g Release 2 (11.2.0.2), cryptographic hardware acceleration for TDE is only available on Intel Xeon with AES-NI, and for Linux x86 and Linux x86-64 on Oracle Linux 5 and Red Hat Enterprise Linux 5.