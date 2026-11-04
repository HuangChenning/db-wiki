---
title: Backup On the Cloud
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/web_services001.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

The OSB Cloud Module is part of the OSB product family and provides the flexibility to back up your database to the Amazon S3 Cloud and to tape. With this cloud offering, local disk backups are sent directly to Amazon S3 for offsite storage and are fully integrated with RMAN features and functionality. In addition, OSB Cloud Module backups work with tools like Oracle Enterprise Manager and your customized RMAN scripts.

The OSB Cloud Module efficiently handles the backing up of Oracle databases to S3 storage. You can backup Oracle databases starting with Oracle Database 9 `i` Release 2 or higher. The OSB Cloud Module does not back up operating system files.

The Oracle Secure Backup Cloud Module uses the RMAN SBT (system backup to tape) interface to extend the Amazon S3 functionality for Oracle backup operations. The OSB Cloud Module offers an easy-to-manage, cost efficient, and scalable alternative to maintaining in-house data storage and managing a local, fully configured backup infrastructure.

The OSB Cloud Module has several advantages over traditional tape-based offsite backups:

- Continuous Accessibility
	OSB Cloud Module backups stored on Amazon S3 storage are always accessible. The cloud storage services availability and access model helps an organization to streamline recovery operations. For example, there is no need to ship or load tapes before a restore can be performed. You can still use familiar and standard tools like Enterprise Manager and your organization's current scripts continue to execute backup and restore tasks. With the ability to continually and easily access backups, the time spent restoring backups may be substantially reduced.
- Improved Reliability
	Because S3 storage is disk based, it is inherently more reliable than tape media. Internet storage service providers keep multiple, redundant copies of your data for availability and scalability purposes and the benefit of this practice to your organization and your data is increased reliability.