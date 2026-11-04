---
title: Troubleshooting the OSB Cloud Module
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/web_services005.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

This section lists potential issues that may affect the installation or the operation of the OSB Cloud Module:

| Symptoms | Error Messages | Resolution |
| --- | --- | --- |
| The S3 Backup installation cannot create the license file on Amazon S3. | `Time-out waiting for license file to be created.` | The first time you run the S3 Backup installer for a set of AWS identifiers, the installer creates a license file on Amazon S3. If there are problems preventing its creation the time-out error message is displayed in the installation output.  Contact Oracle support to resolve the issue. |