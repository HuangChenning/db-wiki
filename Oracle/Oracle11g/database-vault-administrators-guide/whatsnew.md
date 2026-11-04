---
title: "What's New in Oracle Database Vault?"
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/whatsnew.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

This section describes new features in Oracle Database Vault for this release of Oracle Database.

This section contains:

## New Oracle Database Vault Features in Oracle Database 11g Release 2 (11.2.0.4)

This section contains:

- Expanded Ability to Use Trace Files for Oracle Database Vault Events
- New Role for Cleaning the Oracle Database Vault Audit Trail

### Expanded Ability to Use Trace Files for Oracle Database Vault Events

Available in Oracle Database 11g Release 2 (11.2.0.3) but not documented is the expanded ability to use trace files to diagnose Oracle Database Vault events. The trace files help you to perform the following activities:

- Track the success and failures of Database Vault events
- Diagnose bugs and other issues that may arise

See ["Using Trace Files to Diagnose Events in the Database"](troubleshooting.md) for more information.

### New Role for Cleaning the Oracle Database Vault Audit Trail

For better separation of duty, this release introduces the `DV_AUDIT_CLEANUP` role, which can be granted to any user who is responsible for cleaning the Database Vault audit trail. This role does not apply to unified auditing environments.

See ["DV\_AUDIT\_CLEANUP Audit Trail Cleanup Role"](db_objects.md) for more information.

## New Oracle Database Vault Features in Oracle Database 11g Release 2 (11.2.0.3)

This section contains:

- New Role to Support the XStream in an Oracle Database Vault Environment
- New Roles to Support Oracle GoldenGate in an Oracle Database Vault Environment
- Deprecation of Database Vault Configuration Assistant

### New Role to Support the XStream in an Oracle Database Vault Environment

Users who want to use XStream in an Oracle Database Vault environment must now be granted the `DV_XSTREAM_ADMIN` role.

See ["DV\_XSTREAM\_ADMIN XStream Administrative Role"](db_objects.md) for more information.

### New Roles to Support Oracle GoldenGate in an Oracle Database Vault Environment

Users who want to use Oracle GoldenGate in an Oracle Database Vault environment must be granted one of the following roles, depending on how they plan to use Oracle GoldenGate:

- `DV_GOLDENGATE_ADMIN` role if they want to configure Oracle GoldenGate
- `DV_GOLDENGATE_REDO_ACCESS` role if they want to use the GoldenGate `TRANLOGOPTIONS DBLOGREADER` method to access redo logs

See the following sections for more information:

- ["DV\_GOLDENGATE\_ADMIN Oracle GoldenGate Administrative Role"](db_objects.md)
- ["DV\_GOLDENGATE\_REDO\_ACCESS Oracle GoldenGate Redo Log Access Role"](db_objects.md)

### Deprecation of Database Vault Configuration Assistant

Database Vault Configuration Assistant (DVCA) has been deprecated starting with this release. The functionality for DVCA to add languages to Database Vault has been replaced with the `DBMS_MACADM.ADD_NLS_DATA` procedure.

See ["Adding Languages to Oracle Database Vault"](dvca.md) for more information.

## Changed Oracle Database Vault Features in Oracle Database 11g Release 2 (11.2.0.2)

This section contains:

- Desupport for the Oracle Data Pump EXP and IMP Utilities

### Desupport for the Oracle Data Pump EXP and IMP Utilities

Starting with this release, the Oracle Data Pump `EXP` and `IMP` utilities cannot be used in an Oracle Database Vault environment.

See ["Using Oracle Data Pump in an Oracle Database Vault Environment"](dba.md) for more information about using Oracle Data Pump with Oracle Database Vault.

## New Oracle Database Vault Features in Oracle Database 11g Release 2 (11.2.0.2)

This section contains:

- DBMS\_MACADM Procedures Now Use Previous Values for Defaults

### DBMS\_MACADM Procedures Now Use Previous Values for Defaults

Default settings for some of the values for the following `DBMS_MACADM` PL/SQL package procedures are now based on their previous settings:

- `DBMS_MACADM.UPDATE_REALM`
- `DBMS_MACADM.UPDATE_REALM_AUTH`
- `DBMS_MACADM.UPDATE_RULE_SET`
- `DBMS_MACADM.UPDATE_COMMAND_RULE`
- `DBMS_MACADM.UPDATE_FACTOR`
- `DBMS_MACADM.UPDATE_ROLE`

For example, suppose you created or updated a realm to have realm checking enabled. When you use the `DBMS_MACADM.UPDATE_REALM` procedure to modify the realm, the `enabled` parameter default is set to enable realm checking.

For more information, see [Chapter 12, "Using the DBMS\_MACADM Package."](apis_dbms_macadm.md)

## New Oracle Database Vault Features in Oracle Database 11g Release 2 (11.2.0.1)

This section contains:

- Integration with Oracle Enterprise Manager
- Oracle Data Pump Support
- Oracle Database Job Scheduler Support
- Additional Oracle Database Vault Roles
- Additional Default Rule Sets
- Expanded Range for Fail Codes Used for Rule Set Creation
- Changes to Oracle Database Vault PL/SQL Packages
- Changes to Database Vault Configuration Assistant
- Support for Oracle Recovery Manager
- SYS Control of EXECUTE Privilege for the DBMS\_RLS PL/SQL Package
- Stronger Protection for the DVSYS Schema
- OS\_AUTHENT\_PREFIX Parameter No Longer Modified
- NOSYSDBA Parameter of ORAPWD Deprecated

### Integration with Oracle Enterprise Manager

You now can perform a set of Oracle Database Vault functions from both Oracle Database Enterprise Manager Database Control Release 11.2 and Grid Control Release 10.2.0.5. This integration also applies to Releases 9.2.0.8, 10.2.0.4, and 11.1.0.7 of Oracle Database Vault.

From Database Control, you now can perform the following tasks:

- Monitor the Database Vault-enabled database
- Access Oracle Database Vault reports

From Grid Control, you can perform these tasks:

- Propagate Oracle Database Vault security policies across multiple database servers to help ensure consistent policies across the enterprise
- Administer and monitor all Oracle Database Vault-protected servers from a single centralized management console
- Automate alerts when unauthorized attempts are made to access Oracle Database Vault-protected databases
- Access Oracle Database Vault reports

See the following sections for more information:

- ["Accessing the Oracle Database Vault Pages and DVA from Oracle Enterprise Manager"](getting_started.md)
- ["Using Oracle Database Vault with Oracle Enterprise Manager"](dba.md)

### Oracle Data Pump Support

Oracle Data Pump users now can export and import data in an Oracle Database Vault environment.

See ["Using Oracle Data Pump in an Oracle Database Vault Environment"](dba.md) for more information.

### Oracle Database Job Scheduler Support

Users who are responsible for scheduling database jobs now can do so in an Oracle Database Vault environment.

See ["Scheduling Database Jobs in an Oracle Database Vault Environment"](dba.md) for more information.

### Additional Oracle Database Vault Roles

Oracle Database Vault includes the following new roles:

- `DV_MONITOR`
- `DV_STREAMS_ADMIN`
- `DV_PATCH_ADMIN`

See the following sections for more information:

- ["About Oracle Database Vault Roles"](db_objects.md)
- ["DV\_MONITOR Database Vault Monitoring Role"](db_objects.md)
- ["DV\_STREAMS\_ADMIN Oracle Streams Configuration Role"](db_objects.md)
- ["DV\_PATCH\_ADMIN Database Vault Database Patch Role"](db_objects.md)

### Additional Default Rule Sets

Oracle Database Vault now provides the following additional rule sets:

- Allow Fine Grained Control of System Parameters
- Allow Oracle Data Pump Operation
- Allow Scheduler Job

See ["Default Rule Sets"](cfrulset.md) for more information.

### Expanded Range for Fail Codes Used for Rule Set Creation

You are no longer restricted to negative numbers when you specify a fail code for the creation of a rule set. You can enter a number the ranges of -20999 to -20000 or 20000 to 20999.

See ["Error Handling Options"](cfrulset.md) for more information.

### Changes to Oracle Database Vault PL/SQL Packages

The `DBMS_MACADM` and `DBMS_MACSEC_ROLES` PL/SQL packages have changed as follows:

- The DBMS\_MACADM.CREATE\_RULE\_SET and UPDATE\_RULE\_SET procedure have a new parameter, is\_static. The `is_static` parameter determines how often a rule set is evaluated when a SQL statement accesses it. See ["CREATE\_RULE\_SET Procedure"](apis_dbms_macadm.md) and ["UPDATE\_RULE\_SET Procedure"](apis_dbms_macadm.md) for more information.
- The DBMS\_MACADM package has the following new procedures:
	- `AUTHORIZE_DATAPUMP_USER` authorizes an Oracle Database Pump user perform Oracle Data Pump operations when Oracle Database Vault is enabled. See ["AUTHORIZE\_DATAPUMP\_USER Procedure"](apis_dbms_macadm.md) for more information.
		- `UNAUTHORIZE_DATAPUMP_USER` revokes the authorization that was granted by the `AUTHORIZE_DATAPUMP_USER` procedure. See ["UNAUTHORIZE\_DATAPUMP\_USER Procedure"](apis_dbms_macadm.md) for more information.
		- `AUTHORIZE_SCHEDULER_USER` grants a user authorization to schedule database jobs when Oracle Database Vault is enabled. See ["AUTHORIZE\_SCHEDULER\_USER Procedure"](apis_dbms_macadm.md) for more information.
		- `UNAUTHORIZE_SCHEDULER_USER` revokes the authorization that was granted by the `AUTHORIZE_SCHEDULER_USER` procedure. See ["UNAUTHORIZE\_SCHEDULER\_USER Procedure"](apis_dbms_macadm.md) for more information.
- The DBMS\_MACSEC\_ROLES.SET\_ROLE procedure has been enhanced. You now can specify multiple roles with the `p_role` parameter. See ["SET\_ROLE Procedure"](apis_macsec_roles.md) for more information.

### Changes to Database Vault Configuration Assistant

Database Vault Configuration Assistant (DVCA) has the following changes:

- Addition of the dbuniquename parameter. The `dbuniquename` parameter enables you to specify a globally unique name for an Oracle database. See ["Adding Languages to Oracle Database Vault"](dvca.md) for more information.
- Removal of the optionrac parameter. The `optionrac` parameter was used for configuring Oracle Database Vault on Oracle Real Application Clusters (Oracle RAC) nodes. The new procedure for configuring Oracle Database Vault on Oracle RAC nodes is simpler. See ["Configuring Oracle Database Vault on Oracle RAC Nodes"](dvca.md) for more information.

### Support for Oracle Recovery Manager

You now can use Oracle Recovery Manager (RMAN) in an Oracle Database Vault environment.

See ["Using Oracle Database Vault with Oracle Recovery Manager"](dba.md).

### SYS Control of EXECUTE Privilege for the DBMS\_RLS PL/SQL Package

In previous releases of Oracle Database Vault, the `SYS` user was prevented from granting or revoking the `EXECUTE` privilege on the `DBMS_RLS` PL/SQL package to other users. Starting with this release, user `SYS` can resume granting and revoking `EXECUTE` on `DBMS_RLS` to other users.

### Stronger Protection for the DVSYS Schema

To keep `DVSYS` as a protected schema, you can no longer drop its objects, even if the recycle bin is disabled. For better security for other realms, you should disable the recycle bin.

See ["Security Considerations for the Recycle Bin"](guidelines.md).

### OS\_AUTHENT\_PREFIX Parameter No Longer Modified

Oracle Database Vault no longer modifies the `OS_AUTHENT_PREFIX` initialization parameter during installation. The default value for the `OS_AUTHENT_PREFIX` parameter is `OPS$`.

See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams176.htm#REFRN10152) for more information about this parameter.

### NOSYSDBA Parameter of ORAPWD Deprecated

The `NOSYSDBA` parameter of the `ORAPWD` utility has been deprecated in this release. It is no longer necessary in Oracle Database Vault. As part of this deprecation, the `lockout` parameter of the DVCA utility has been deprecated as well.