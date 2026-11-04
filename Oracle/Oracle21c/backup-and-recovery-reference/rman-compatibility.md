---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/rman-compatibility.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This appendix describes the requirements for compatibility among the different components of the Recovery Manager (RMAN) environment. This appendix contains these topics:

See Also:

Oracle Database Upgrade Guide

### D.1 About RMAN Compatibility

Table D-1 describes the components of an RMAN environment. Each component has a release number associated with it.

Table D-1 Components of an RMAN Environment

| Component | Release Number Refers to... |
| --- | --- |
| RMAN client | Version of RMAN client (displayed when you start RMAN) |
| Recovery catalog database | Version of Oracle Database |
| Recovery catalog schema in recovery catalog database | Version of RMAN client used to create the recovery catalog |
| Target database | Version of Oracle Database |
| Auxiliary database | Version of Oracle Database |

Starting with Oracle Database 12c, the version of the RMAN client, target database, and auxiliary database must be the same. The recovery catalog schema can be any supported catalog schema whose version is greater than the version of the RMAN client. For example an Oracle Database 12c RMAN client can only connect to a target database whose version is Oracle Database 12c, an auxiliary database whose version is Oracle Database 12c, and a recovery catalog schema that is created in an Oracle Database 12c or higher version.

### D.2 Determining the Recovery Catalog Schema Version

Use a SQL query to determine the version of the recovery catalog schema.

To determine the current release of the recovery catalog schema:

1. Use SQL\*Plus to connect to the recovery catalog database as the catalog owner. For example, enter:
	```
	% sqlplus rco@catdb
	```
2. Query the `rcver` catalog table. For example, run this query:
	```
	SQL> SELECT * FROM rcver; 
	     VERSION 
	     ------------ 
	     12.01.00.01
	```

### D.3 RMAN Compatibility Matrix

There are certain rules for RMAN compatibility.

Rules for RMAN compatibility include:

- The version of the RMAN client must be equal to the version of the target database.
- The version of the auxiliary database must be equal to the version of the RMAN client.
- The version of the recovery catalog schema must be greater than or equal to the version of the RMAN client.
- If the recovery catalog is a virtual private catalog (see `CREATE CATALOG`), then the version of the RMAN client connecting to it must be Oracle Database 10g Release 1 (10.1.0.6) or Oracle Database 10g Release 2 (10.2.0.3). Oracle 9i RMAN clients cannot connect to a virtual private catalog. This version restriction does not affect RMAN client connections to an Oracle Database 11g base recovery catalog, even if the base catalog has virtual private catalog users.
- While backing up an Oracle Database 10g or later release with the Oracle9i RMAN client, you cannot include a control file that was created using `COMPATIBLE=10.0.0` in a data file backup set. The workaround is to turn control file autobackup `ON`.
- Any release of Oracle Database can restore backup sets and copies created by any prior Oracle Database release.

Table D-2 shows version-specific requirements for RMAN components. The symbol `>=` before a release means all Oracle Database releases from this release or later along with their patches.

Table D-2 RMAN Compatibility Table

| Target/Auxiliary Database version | RMAN client version | Recovery Catalog Database version | Recovery Catalog Schema version |
| --- | --- | --- | --- |
| 11.1.0 | \>= 10.1.0.5 and <= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |
| 11.2.0 | \>= 10.1.0.5 and <= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |
| \>= 12.1.0.x | \= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |
| 18.x | \= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |
| 19.x | \= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |
| 20.x | \= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |
| 21.x | \= target database executable | \>= 11.0  (with `COMPATIBLE` parameter >=11.0) | \>= RMAN client version |

When using an older version of the RMAN client with a newer version of the database, you do not get the features added in the newer version.

### D.4 Cross-Version Compatibility of Recovery Catalog Exports and Imports

Data Pump Exports of the recovery catalog are often used as a way to backup its contents. When planning to use Data Pump Export to make a logical backup of the recovery catalog, certain compatibility issues relating to the use of database exports across versions of Oracle Database must be kept in mind.

Exports from a later version of the database cannot be imported into databases running under earlier versions. You must export your recovery catalog data using the export utility from the earliest version of Oracle Database that you use for a recovery catalog.

For example, to export the recovery catalog data from an Oracle Database 11g Release 2 (11.2) database and import it into an Oracle Database 10g Release 1 (10.1.0.5) database for disaster recovery, you must use the export utility from Oracle Database 10g Release 1 (10.1.0.5) to perform the export operation. Otherwise, the import operation fails.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/rcmrf&id=SUTIL103) for details on compatibility issues relating to the use of database exports across versions of Oracle Database

### D.5 RMAN Compatibility: Scenario

This section contains an example of the RMAN client versions and recovery catalog database versions used for production databases that use various Oracle Database versions.

Assume that you maintain a production databases of the following releases:

- Oracle Database 11g Release 1 (11.2)
- Oracle Database 12c Release 1(12.1)
- Oracle Database 12c Release 2(12.2)
- Oracle Database release 18c, version 18.1

You want to record RMAN repository data about these databases in a single recovery catalog database. According to RMAN Compatibility Matrix, you can use a single recovery catalog database whose version is Oracle Database Release 18c with a catalog schema whose version is Oracle Database Release 18c for all target databases.

Ensure that the version of the RMAN client used to back up each target database meets the following requirements:

- Use the Oracle Database 11g Release 1 (11.2) RMAN client to back up the Oracle Database 11g Release 1 (11.2) database.
- Use the Oracle Database 12c Release 1 (12.1) RMAN client to back up the Oracle Database 12c Release 1 (12.1) database.
- Use the Oracle Database 12c Release 2 (12.2) RMAN client to back up the Oracle Database 12c Release 2 (12.2) database.
- Use the Oracle Database release 18c version 18.1 RMAN client to back up the Oracle Database Release 18c database.