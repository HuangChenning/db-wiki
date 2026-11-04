---
title: Cross-Version Compatibility of Recovery Catalog Exports and Imports
book: Backup and Recovery Reference
doc_id: E10643-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/backup.112/e10643/compat004.htm
tags:
  - oracle
  - 11g
  - backup-and-recovery-reference
---

Data Pump Exports of the recovery catalog are often used as a way to backup its contents. When planning to use Data Pump Export to make a logical backup of the recovery catalog, see [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/original_import.htm#SUTIL103) for details on compatibility issues relating to the use of database exports across versions of Oracle Database.

Exports from a later version of the database cannot be imported into databases running under earlier versions. You must export your recovery catalog data using the export utility from the earliest version of Oracle Database that you used for a recovery catalog.

For example, to export recovery catalog data from a 9.2.0.5 database and import it into an 8.1.7.4 version of Oracle for disaster recovery, you must use the export utility from the 8.1.7.4 release of Oracle to perform the export operation. Otherwise, the import operation fails.