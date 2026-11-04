---
title: "RMAN Compatibility: Scenario"
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat005.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Assume that you maintain a production databases of the following releases:

- 9.2.0
- 10.2.0
- 11.2.0

You want to record RMAN repository data about these databases in a single recovery catalog database. According to [Table B-2](compat003.md), you can use a single 11.2.0 recovery catalog database with a 11.2.0 catalog schema for all target databases. Ensure that the version of the RMAN client used to back up each target database meets the following requirements:

- Use the 9.2.0 RMAN executable to back up the 9.2.0 database.
- Use either the 9.2.0 or 10.2.0 RMAN executable to back up the 10.2.0 database.
- Use any RMAN executable to back up the 11.2.0 database.