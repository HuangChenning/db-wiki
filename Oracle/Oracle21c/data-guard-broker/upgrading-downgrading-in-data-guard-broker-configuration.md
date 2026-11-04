---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/upgrading-downgrading-in-data-guard-broker-configuration.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

Use these topics to upgrade or downgrade Oracle databases and Oracle Enterprise Manager Cloud Control (Cloud Control) in a broker configuration.

See Also:

[Oracle Data Guard Installation](oracle-data-guard-broker-installation-requirements.md)

### Considerations While Using the DBMS\_ROLLING Package

When upgrading from Oracle Database Version 12.2 to a higher database version, broker management can remain enabled. However, some considerations must be kept in mind.

The considerations are as follows:

- The broker configuration files must be in a release-neutral location and accessible throughout the upgrade process.
- After upgrading the leading group members, ensure broker communication between the leading group and the trailing group is successful before proceeding with the upgrade process.
	Communication may be disrupted if network files are either not moved to the upgraded `ORACLE_HOME` or need to be edited appropriately. In such cases, shut down the upgraded databases (transient logical standby and any other Leading Group Standby databases), stop the listener, copy the `listener.ora` and `tnsnames.ora` or fix them as appropriate, restart the listener, and restart the databases.
- Before you run the `DBMS_ROLLING` procedure, the physical standby databases must have been operating in Active Data Guard mode.
	If the physical standby databases were operating only in the mounted mode, and the primary database is a multitenant database, you must open the primary database including all its PDBs, and the temp file configuration must be confirmed before you run procedures in the `DBMS_ROLLING` package. This ensures that the necessary temp files are created and available during the upgrade process.