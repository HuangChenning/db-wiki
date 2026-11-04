---
title: Part VIII Setting Up RMAN for Cloud Backup and Restores
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/cloud-backups-sbt.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

This part describes how to implement a persistent cloud backup strategy using RMAN.

The following chapters describe the Oracle-supplied cloud backup modules and the procedure to integrate RMAN with each module so that you can directly backup your Oracle Database to a preferred cloud destination.

**Note:** The information provided in this section applies to Oracle Database 19c Release 27 (19.27) and later releases. Oracle Database Zero Data Loss Cloud Protect is supported for Oracle Database 19c Release Update 18 (19.18) or later.

- [Backing Up an Oracle Database to Cloud](rman-backup-cloud.md)
- [Persistent Settings for RMAN Cloud Backups](rman-cloud-settings.md)
- [Oracle Database Backup Cloud Service](backup-cloud-oci.md)
- [Oracle Database Cloud Backup Module for Azure](azure-sbt-module.md)
- [Oracle Database Cloud Backup for Amazon S3](backup-cloud-osb.md)
- [Oracle Database Zero Data Loss Cloud Protect for Autonomous Recovery Service](cloud-protect-fleet-agent.md)