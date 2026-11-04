---
title: Database Performance Tuning Guide
book: Database Performance Tuning Guide
doc_id: F32091-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/tgdba/changes-in-this-release.html
tags:
  - oracle
  - 21c
  - performance-tuning-guide
---

This preface contains:

- Changes in Oracle Database Release 21c, Version 21.1

### Changes in Oracle Database Release 21c, Version 21.1

The following are changes in Oracle Database Performance Tuning Guide for Oracle Database release 21c, version 21.1.

#### New Features

The following features are new in this release:

- Auto-Result Cache, settings to determine eligible queries for storing the result sets in the server and client result caches.
	Note:
	See [Setting the Result Cache Mode](tuning-result-cache.md)
- Directly Mapped Buffer Cache Support
- In-Memory Hybrid Scans

Note:

A multitenant container database is the only supported architecture in Oracle Database 20c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.

#### Desupported Features

Note:

A multitenant container database is the only supported architecture in Oracle Database 20c. While the documentation is being revised, legacy terminology may persist. In most cases, "database" and "non-CDB" refer to a CDB or PDB, depending on context. In some contexts, such as upgrades, "non-CDB" refers to a non-CDB from a previous release.