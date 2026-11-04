---
title: Concepts and Administration
book: Data Guard Concepts and Administration
doc_id: E85767-01
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sbydb/release-changes.html
tags:
  - oracle
  - 12c
  - data-guard-concepts-and-administration
---

This preface lists changes in Oracle Data Guard Concepts and Administration.

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

The following are changes in Oracle Data Guard Concepts and Administration for Oracle Database 12c Release 2 (12.2.0.1).

- A new `INSTANCES [ ALL | integer]` clause is available on the SQL `ALTER RECOVER MANAGED STANDBY DATABASE` command which enables you to control the number of instances on a physical standby that Redo Apply uses. See [Setting Up Multi-Instance Redo Apply](configuring-data-guard-standby-databases-in-oracle-RAC.md).
- Logical standby now supports long identifiers (128 bytes).
- You can now upgrade databases that use Oracle Label Security (OLS) to new Oracle Database releases and patch sets by using Oracle Data Guard database rolling upgrades using a transient logical standby database and the PL/SQL package, `DBMS_ROLLING`. See [Oracle Label Security](data-type-ddl-support-on-logical-standby-databases.md).
- You can now upgrade databases that use Oracle Database Vault to new Oracle Database releases and patch sets by using Oracle Data Guard database rolling upgrades with a transient logical standby and the PL/SQL package, `DBMS_ROLLING`. See [Oracle Database Vault](data-type-ddl-support-on-logical-standby-databases.md).
- A new database initialization parameter, `DATA_GUARD_SYNC_LATENCY`, enables you to define the maximum amount of time (in seconds) that the primary database may wait before disconnecting subsequent destinations after at least one synchronous standby has acknowledged receipt of the redo. See [Configuring an Oracle Database to Send Redo Data](oracle-data-guard-redo-transport-services.md)
- You can now detect lost writes and also inconsistencies between a primary database and physical standby databases by using the new PL/SQL procedure, `DBMS_DBCOMP.DBCOMP`. See [Using the DBCOMP Procedure to Detect Lost Writes and Other Inconsistencies](examples-of-using-oracle-data-guard.md).
- The new `ENABLED_PDBS_ON_STANDBY` initialization parameter enables you to specify a subset of pluggable databases (PDBs) for replication on a physical standby of a multitenant container database (CDB). In releases prior to Oracle Database 12c Release 2 (12.2.0.1), you had to specify either all PDBs or none. See [Creating a Physical Standby of a CDB](creating-oracle-data-guard-physical-standby.md).
- Oracle Database In-Memory column store (IM column store) is now supported on standby databases in Oracle Active Data Guard (ADG) environments. See [IM Column Store in an Active Data Guard Environment](managing-oracle-data-guard-physical-standby-databases.md).
- Oracle Active Data Guard is integrated with Oracle Sharding. See [Oracle Active Data Guard Supports Oracle Sharding.](introduction-to-oracle-data-guard-concepts.md)
- You can use the new `FARSYNC` option on the RMAN `DUPLICATE` command to create an Oracle Data Guard far sync instance. You can do so using either active database duplication or backup-based duplication. See [Using the DUPLICATE Command to Create a Standby Database](creating-data-guard-standby-database-using-RMAN.md).
- You can now use the Oracle Diagnostic Pack with an Oracle Active Data Guard standby database that is open read-only. See [Using Oracle Diagnostic Pack to Tune Oracle Active Data Guard Standbys](managing-oracle-data-guard-physical-standby-databases.md).
- The number of alternate log archive destinations that you can define has been increased with the capability to create groups of log archive destinations. You can define priority of group members, as well as policies in a failure state. See [Alternate Destinations](creating-oracle-data-guard-far-sync-instance.md).
- Rolling upgrades performed using the `DBMS_ROLLING` PL/SQL package are supported on multitenant container databases (CDBs). See [DBMS\_ROLLING Upgrades and CDBs](using-DBMS_ROLLING-to-perform-rolling-upgrade.md).
- Password file changes done on the primary database are now automatically propagated to standby databases. The only exception to this is far sync instances. Updated password files must still be manually copied to far sync instances because far sync instances receive redo, but do not apply it. Once the password file is up-to-date at the far sync instance, the redo containing the password update at the primary is automatically propagated to any standby databases that are set up to receive redo from that far sync instance. The password file is updated on the standby when the redo is applied.
- When a physical standby database is converted into a primary, there is now an option to keep any sessions connected to the standby during the switchover/failover. This is done with the `STANDBY_DB_PRESERVE_STATES` initialization parameter. See [Role Transitions Involving Physical Standby Databases](managing-oracle-data-guard-role-transitions.md).
- You can encrypt and decrypt both new and existing tablespaces, and existing databases within an Oracle Data Guard environment. This can be done offline or online. See [Reset the TDE Master Encryption Key](managing-oracle-data-guard-physical-standby-databases.md) and [Support for Tablespace Encryption](data-type-ddl-support-on-logical-standby-databases.md).