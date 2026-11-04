---
title: Concepts and Administration
book: Data Guard Concepts and Administration
doc_id: F31838-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sbydb/loe.html
tags:
  - oracle
  - 21c
  - data-guard-concepts-and-administration
---

- [3-1 Creating the Control File for the Standby Database](creating-oracle-data-guard-physical-standby.md)
- [3-2 Modifying Initialization Parameters for a Physical Standby Database](creating-oracle-data-guard-physical-standby.md)
- [3-3 Querying V$DATAGUARD\_PROCESS to Verify Redo Transmission from Primary to Secondary Database](creating-oracle-data-guard-physical-standby.md)
- [4-1 Primary Database: Logical Standby Role Initialization Parameters](creating-oracle-data-guard-logical-standby.md)
- [4-2 Modifying Initialization Parameters for a Logical Standby Database](creating-oracle-data-guard-logical-standby.md)
- [5-1 Some of the Initialization Parameters Used for Far Sync Instances](creating-oracle-data-guard-far-sync-instance.md)
- [5-2 Configuring for Single Destination Failover](creating-oracle-data-guard-far-sync-instance.md)
- [5-3 Configuring for Multiple Standby Database Redo Destination Failover](creating-oracle-data-guard-far-sync-instance.md)
- [5-4 Parameters Used to Set Up the High Availability Far Sync Instance](creating-oracle-data-guard-far-sync-instance.md)
- [5-5 Parameters Used to Set Up Protection After a Role Change](creating-oracle-data-guard-far-sync-instance.md)
- [7-1 Some of the Initialization Parameters Used When Cascading Redo](oracle-data-guard-redo-transport-services.md)
- [10-1 Performing DML Operations on a Physical Standby Database](managing-oracle-data-guard-physical-standby-databases.md)
- [10-2 Automatically Recompiling Modified PL/SQL Objects](managing-oracle-data-guard-physical-standby-databases.md)
- [10-3 Enabling the Result Cache for an Existing Table](managing-oracle-data-guard-physical-standby-databases.md)
- [10-4 Enabling the Result Cache for Queries Containing Hints](managing-oracle-data-guard-physical-standby-databases.md)
- [11-1 `V$DATAGUARD_STATS` Contents for a Logical Standby Database](managing-oracle-data-guard-logical-standby-databases.md)
- [14-1 Setting Switchover to Enforce Apply Lag Requirements](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-2 Resetting Logging Back to Its Default Value](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-3 Designating a Database as an Optional Participant](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-4 Setting a Database to Protect the Transient Logical Standby](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-5 Blocking Operations Not Supported by Transient Logical Standbys](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-6 Basic Rolling Upgrade Steps](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-7 Rolling Upgrade Between Two Databases](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-8 Rolling Upgrade Between Three Databases](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-9 Rolling Upgrade Between Four Databases](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-10 Rolling Upgrade on a Reader Farm](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-11 Rolling Upgrade for Application Testing](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-12 Resuming a Rolling Upgrade After a Failover to a New Primary](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [14-13 Resuming a Rolling Upgrade After a Failover to a New Transient Logical](using-DBMS_ROLLING-to-perform-rolling-upgrade.md)
- [15-1 Primary and All Standbys Are Mounted or Open and DBCOMP Is Executed From the Primary](examples-of-using-oracle-data-guard.md)
- [15-2 Primary and All Standbys Are Mounted or Open and DBCOMP Is Executed From a Standby](examples-of-using-oracle-data-guard.md)
- [15-3 Primary Is Mounted or Open, But Not All Standbys Are, and DBCOMP is Executed From the Primary](examples-of-using-oracle-data-guard.md)
- [15-4 Primary Is Mounted or Open, But Not All Standbys Are, and DBCOMP is Executed From a Standby](examples-of-using-oracle-data-guard.md)
- [15-5 Primary is Not Mounted, But Multiple Standbys Are Mounted or Open](examples-of-using-oracle-data-guard.md)
- [15-6 Primary Is Mounted or Open, But No Standbys Are Mounted or Open](examples-of-using-oracle-data-guard.md)
- [17-1 Automatically Failing Over to an Alternate Local Destination](LOG_ARCHIVE_DEST_n-parameter-attributes.md)
- [17-2 Automatic Local Alternate Fallback](LOG_ARCHIVE_DEST_n-parameter-attributes.md)
- [A-1 Setting a Retry Time and Limit](troubleshooting-oracle-data-guard.md)
- [A-2 Specifying an Alternate Destination](troubleshooting-oracle-data-guard.md)
- [C-1 PL/SQL Skip Procedure for RegisterSchema](data-type-ddl-support-on-logical-standby-databases.md)