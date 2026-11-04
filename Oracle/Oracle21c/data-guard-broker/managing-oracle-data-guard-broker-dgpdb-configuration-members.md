---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/managing-oracle-data-guard-broker-dgpdb-configuration-members.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

Learn how to manage DG PDB broker configurations and monitor the state of configuration members.

Note:

The only supported protection mode for DB PDB configurations is maximum performance mode.

This chapter contains the following topics:

### Managing Broker Configuration Members

The broker uses information in its configuration files to manage and monitor the state of members in the DG PDB configuration.

The `COMPATIBLE` initialization parameter in the source database and the target database must be set to 21.1 or higher.

Tasks performed for CDB configurations such as setting configuration properties, creating configuration files, starting Data Guard broker, and enabling or disabling broker configurations are also applicable to DG PDB configurations.

Note:

Although you can configure a DG PDB for a PDB that is part of a CDB that already has a standby database, a role change between such a PDB and its DG PDB results in an inconsistent PDB configuration between the primary and standby databases. Similarly, a role change between the primary and standby database will result in the DG PDB being orphaned because it no longer has a source PDB. When you use Data Guard broker to manage the Data Guard primary and standby databases, creating a DG PDB in such a scenario not allowed.

When broker is not used to manage the Data Guard environment, it is recommended to avoid setting up a PDB for Data Guard protection when the container to which the PDB belongs already has a Data Guard standby database.

### Managing States of Broker Configuration Members

The standby PDBs in a DG PDB configuration can be in the `APPLY-ON` or `APPLY-OFF` state.

The following table describes the various states for standby PDBs in a DG PDB configuration. No standby databases are listed because they cannot be used in a DG PDB configuration.

Table 5-1 Database States and Descriptions in DG PDB Configurations

| Database role | State Name | Description |
| --- | --- | --- |
| Target PDB | `APPLY-ON` | Redo Apply is started on the target PDB within the target configuration.  If this is an Oracle Real Application Clusters (Oracle RAC) instance, redo apply is started only on the instance where the command is run. The PDB cannot be opened if recovery is running. If the PDB is open when the command to start recovery is run, the PDB is closed. |
| Target PDB | `APPLY-OFF` | Redo Apply is stopped on the target PDB. |

### State Transitions for DG PDBs

Use the DGMGRL `EDIT             DATABASE` command to explicitly change the state of a standby PDB. You can only change the state of the entire database, including all its PDBs.

For example, the following command changes the state of the target database `target-prim` to `APPLY-OFF`:

```
DGMGRL > EDIT PLUGGABLE DATABASE 'target-prim' SET STATE = 'APPLY-OFF';
Succeeded.
```

### Managing Database Properties in DG PDB Configurations

Database properties of members in a DG PDB configuration are of two types: monitorable properties or configurable properties.

Use monitorable properties to view run-time information related to configuration members. Monitorable properties can be viewed only when the member is enabled. Use the `SHOW DATABASE VERBOSE` command to list all monitorable properties. Use the `SHOW DATABASE` command to view details about a particular property. Use the `SHOW PLUGGABLE                     DATABASE` command to view information about the source PDB or target PDB.

Configurable properties impact the operation or configuration of a database. Use configurable properties to view and dynamically update information related to configuration members. You can edit properties regardless of the member's state. If the member is disabled when a property is edited, the property value takes effect after the member or configuration is enabled, as appropriate.

Use the `EDIT DATABASE` command to update the properties of the source database or target database. Use the `EDIT PLUGGABLE                     DATABASE` command to update the state of a source PDB or target PDB.

The `SHOW DATABASE` command has been enhanced to display information about Data Guard at the PDB level. In a DG PDB configuration, the `SHOW                     DATABASE` output shows whether the database has any source or target PDBs, and the number of PDBs in each role.

Example 5-1 Displaying the Properties of a Source Database

```
DGMGRL> SHOW DATABASE boston;
 
Database - boston
  Role: PRIMARY
  Intended State: TRANSPORT-ON
  PDB Data Guard Role: SOURCE and TARGET
  Instance(s):
    bos1
  Data Guard Source PDB(s): 1
  Data Guard Target PDB(s): 2

Database Status:
SUCCESS
```

Example 5-2 Displaying the Properties of Individual PDBs

This example uses the `SHOW PLUGGABLE DATABASE` command to display information about the target PDB `dgpdb_sales`.

```
DGMGRL> SHOW PLUGGABLE DATABASE 'dgpdb_sales' AT 'newyork';

Pluggable database 'dgpdb_sales' at database 'newyork'

  Data Guard Role: Physical Standby
  Con_ID: 7
  Source: con_id 6 at boston
  Transport Lag: +00 00:00:00 seconds
  Intended State: APPLY-ON
  Apply State: Running
```

### Managing Redo Transport Services for DG PDBs

The broker automatically starts redo transport services between a source database and target database once you set up at least one PDB for replication.

To turn on redo transport services for the source database:

1. Connect to the source database.
2. Use the `EDIT CONFIGURATION SET AS SOURCE` command to specify the source database that must be set up for redo transport.

### Viewing Transport Lag and Apply Lag

Transport lag is a measure of the degree to which redo transport or redo apply lags behind the source database.

The redo transport service transmits redo data from the source database to the target database. The log apply services at the individual target PDB updates the target PDB with this redo data, thereby keeping the target PDBs consistent with the source PDBs. Each target PDB has its own log apply service. The archived redo log files and standby redo log files contain all of the database changes except for unrecoverable or unlogged changes.

Transport Lag

The transport lag is displayed in the output of the `SHOW                     PLUGGABLE DATABASE` command. This lag represents, in seconds, the amount of redo data that has not been received by the target CDB for the specified DG PDB.

Average Apply Rate

If the Apply State is Running, the average apply rate is displayed in the output of the `SHOW PLUGGABLE DATABASE` command. The average apply rate pertains to a particular PDB.

### Monitoring a DG PDB Configuration

Monitor the status of the configuration and its members to view statistics, diagnostic information, detect problems, and quickly take necessary actions.

After a DG PDB configuration is enabled, the broker schedules an automatic health check on the individual members. It monitors and reports problems with redo transport and recovery progress. Diagnostic information is written to the broker log files (drc\*.log) and can be viewed using DGMGRL commands.

### Querying Database Status in DG PDB Configurations

Use DGMGRL to query information about the DG PDB configuration and its members.

You can view the status of the DG PDB configuration and detailed information about the source database and target database.

Example 5-3 Displaying Information for a DG PDB Configuration

This example displays information about a DG PDB configuration.

```
DGMGRL> SHOW CONFIGURATION;
 
 
Configuration – MyConfig1
  Protection Mode: MaxPerformance
  Members:
  boston - Primary database
    newyork - Primary database in MyConfig2 configuration
 
Data Guard for PDB: Enabled in SOURCE role

Configuration Status:
SUCCESS
```