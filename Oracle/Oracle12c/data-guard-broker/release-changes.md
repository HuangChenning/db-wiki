---
title: Broker
book: Data Guard Broker
doc_id: E85768-01
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dgbkr/release-changes.html
tags:
  - oracle
  - 12c
  - data-guard-broker
---

This preface lists changes in Oracle Data Guard Broker.

### Changes in Oracle Database 12c Release 2 (12.2.0.1)

This section describes changes in Oracle Data Guard Broker for Oracle Database 12c Release 2 (12.2.0.1).

- Data Guard broker provides a new configurable property, `DataGuardSyncLatency`, which supports the new database initialization parameter, `DATA_GUARD_SYNC_LATENCY`. See [DataGuardSyncLatency](oracle-data-guard-broker-properties.md)
- When you perform a rolling upgrade using the `DBMS_ROLLING` PL/SQL package, you no longer need to disable the broker. In addition, the broker now reports when a rolling upgrade is in progress, and tracks its status. The status information is displayed in the output of the DGMGRL commands ` SHOW CONFIGURATION` and `SHOW DATABASE`. See [SHOW CONFIGURATION](oracle-data-guard-broker-commands.md). and [SHOW DATABASE](oracle-data-guard-broker-commands.md).
- To increase high availability, you can now set multiple fast-start failover targets and the broker automatically selects which one to use. See [Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md).
- You can now start observers on multiple hosts to manage a single Data Guard broker configuration. If one observer fails, then a backup observer automatically takes its place so that the configuration is never in an unobserved state. See [Installing and Starting the Observer](using-data-guard-broker-to-manage-switchovers-failovers.md).
- You can now manage certain tasks for multiple observers from one host by creating groups of broker configurations. See [Managing Observers for Multiple Configurations](using-data-guard-broker-to-manage-switchovers-failovers.md).
- The new `VALIDATE DATABASE DATAFILE` command performs validation of data files across the primary database and standby databases. The validation of data files also detects lost writes at either database. See [VALIDATE DATABASE DATAFILE](oracle-data-guard-broker-commands.md).
- The new DGMGRL @ command allows you to run DGMGRL command scripts. See [@ (at sign) Command](oracle-data-guard-broker-commands.md).
- The broker can publish a service on each member in a configuration with a unified service name. See the [ConfigurationWideServiceName](oracle-data-guard-broker-properties.md).
- The new Data Guard broker property `ApplyInstances` can be used to engage multi-instance Redo Apply as well as to restrict the number of instances that are involved in redo apply on an Oracle Real Application Clusters (Oracle RAC) database. See [ApplyInstances](oracle-data-guard-broker-properties.md).
- You can use the DGMGRL command-line interface to configure and implement the enhanced redo destinations capability provided by the `GROUP` and `PRIORITY` attributes of the `LOG_ARCHIVE_DEST_n` parameter. See [Advanced Redo Transport Settings](managing-oracle-data-guard-broker-configuration-members.md).
- Fast-start failover, with some restrictions, can now be enabled in maximum protection mode. See [Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md).
- Password file changes done on the primary database are now automatically propagated to standby databases. The only exception to this is far-sync instances. Updated password files must still be manually copied to far-sync instances because far-sync instances receive redo, but do not apply it. Once the password file is up-to-date at the far-sync instance, the redo containing the password update at the primary is automatically propagated to any standby databases that are set up to receive redo from that far-sync instance. The password file is updated on the standby when the redo is applied.
- The broker now supports migrating a pluggable database (PDB) from one multitenant container database (CDB) to another on the same host. You can migrate a PDB from a primary CDB to another primary CDB or failover a PDB from a standby CDB to a primary CDB. See [MIGRATE PLUGGABLE DATABASE](oracle-data-guard-broker-commands.md).
- To further support Application Continuity during broker switchover operations, the broker `SWITCHOVER` command now allows you to specify whether you want to wait for sessions to drain (and optionally to specify how long to wait) before proceeding with the switchover. See the DGMGRL [SWITCHOVER](oracle-data-guard-broker-commands.md) command.
- The DGMGRL commands `SHOW DATABASE VERBOSE` and `SHOW INSTANCE VERBOSE` now show the locations of the Oracle alert log file and of the broker log file. See [SHOW DATABASE](oracle-data-guard-broker-commands.md) for an example of the output.
- A new `SPOOL` command is available to record the input and output of the DGMGRL console. See [SPOOL](oracle-data-guard-broker-commands.md).
- A new / (slash) command is available which repeats the last command input to the DGMGRL console. See [/ (slash) Command](oracle-data-guard-broker-commands.md).
- The configuration member to which a connection is made using the `CONNECT` command is now displayed upon successful completion of the command. See [CONNECT](oracle-data-guard-broker-commands.md).
- The new `SET TIME` command records the timestamp as you input each command. See [SET TIME](oracle-data-guard-broker-commands.md).