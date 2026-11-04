---
title: About RMAN Compatibility
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat001.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Table B-1 describes the components of an RMAN environment. Each component has a release number associated with it.

Table B-1 Components of an RMAN Environment

| Component | Release Number Refers to... |
| --- | --- |
| RMAN client | Version of RMAN client (displayed when you start RMAN) |
| Recovery catalog database | Version of Oracle Database |
| Recovery catalog schema in recovery catalog database | Version of RMAN client used to create the recovery catalog |
| Target database | Version of Oracle Database |
| Auxiliary database | Version of Oracle Database |

For example, you can use a release 9.0.1 RMAN client with:

- A release 9.0.1 target database
- A release 9.0.1 auxiliary database
- A release 8.1.7 recovery catalog database whose catalog tables were created with RMAN release 9.0.1