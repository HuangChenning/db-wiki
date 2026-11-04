---
title: DBMS_AUDIT_MGMT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_audit_mgmt.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 27 DBMS\_AUDIT\_MGMT

The `DBMS_AUDIT_MGMT` package provides subprograms to manage audit trail records. These subprograms enable audit administrators to manage the various audit trail types like database audit trails, operating system (OS) audit trails, and XML audit trails.

See Also:

["Verifying Security Access with Auditing"](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG006) in the Oracle Database Security Guide for more information on using the `DBMS_AUDIT_MGMT` package to manage audit trails

This chapter contains the following topics:

---

## Using DBMS\_AUDIT\_MGMT

This section contains topics which relate to using the `DBMS_AUDIT_MGMT` package. The following topics are included:

- Overview
- Security Model
- Constants
- Views

---

### Overview

Database auditing helps meet your database security and compliance requirements. Audit records are written to database tables, operating system (OS) files, or XML files depending on the `AUDIT_TRAIL` initialization parameter setting.

When `AUDIT_TRAIL` is set to `DB`, database records are written to the `AUD$` table. When `AUDIT_TRAIL` is set to OS, audit records are written to operating system files. When `AUDIT_TRAIL` is set to XML, audit records are written to operating system files in XML format.

See Also:

["Verifying Security Access with Auditing"](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG006) in the Oracle Database Security Guide for more background information on database auditing

It is important to manage your audit records properly in order to ensure efficient performance and disk space management. The `DBMS_AUDIT_MGMT` subprograms enable you to efficiently manage your audit trail records.

The `DBMS_AUDIT_MGMT` package provides a subprogram that allows you to move the database audit trail tables out of the `SYSTEM` tablespace. This improves overall database performance by reducing the load on the `SYSTEM` tablespace. It also enables you to dedicate an optimized tablespace for audit records.

The `DBMS_AUDIT_MGMT` subprograms also enable you to manage your operating system and XML audit files. You can define properties like the maximum size and age of an audit file. This enables you to keep the file sizes of OS and XML audit files in check.

The `DBMS_AUDIT_MGMT` subprograms enable you to perform cleanup operations on all audit trail types. Audit trails can be cleaned based on the Last Archive Timestamp value. The Last Archive Timestamp represents the timestamp of the most recent audit record that was securely archived.

The `DBMS_AUDIT_MGMT` package provides a subprogram that enables audit administrators to set the last archive timestamp for archived audit records. This subprogram can also be used by external archival systems to set the last archive timestamp.

The `DBMS_AUDIT_MGMT` subprograms also enable you to configure jobs that periodically delete audit trail records. The frequency with which these jobs should run can be controlled by the audit administrator.

---

### Security Model

All `DBMS_AUDIT_MGMT` subprograms require the user to have `EXECUTE` privilege over the `DBMS_AUDIT_MGMT` package. The `SYSDBA` role has `EXECUTE` privileges on the package by default.

Oracle strongly recommends that only audit administrators should have `EXECUTE` privileges over the `DBMS_AUDIT_MGMT` package.

---

### Constants

The `DBMS_AUDIT_MGMT` package defines several enumerated constants that can be used for specifying parameter values. Enumerated constants must be prefixed with the package name, for example, `DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD`.

The `DBMS_AUDIT_MGMT` package includes the constants shown in the following tables:

- DBMS\_AUDIT\_MGMT Constants - Audit Trail Types
- DBMS\_AUDIT\_MGMT Constants - Audit Trail Properties
- DBMS\_AUDIT\_MGMT Constants - Purge Job Status

Audit trails can be classified based on whether audit records are written to database tables, operating system files, or XML files. Table 27-1 lists the audit trail type constants.

Table 27-1 DBMS\_AUDIT\_MGMT Constants - Audit Trail Types

| Constant | Type | Description |
| --- | --- | --- |
| `AUDIT_TRAIL_ALL` | `PLS_INTEGER` | All audit trail types. This includes the standard database audit trail (`SYS.AUD$` and `SYS.FGA_LOG$` tables), operating system (OS) audit trail, and XML audit trail. |
| `AUDIT_TRAIL_AUD_STD` | `PLS_INTEGER` | Standard database audit records in the `SYS.AUD$` table |
| `AUDIT_TRAIL_DB_STD` | `PLS_INTEGER` | Both standard audit (`SYS.AUD$`) and FGA audit(`SYS.FGA_LOG$`) records |
| `AUDIT_TRAIL_FGA_STD` | `PLS_INTEGER` | Standard database fine-grained auditing (FGA) records in the `SYS.FGA_LOG$` table |
| `AUDIT_TRAIL_FILES` | `PLS_INTEGER` | Both operating system (OS) and XML audit trails |
| `AUDIT_TRAIL_OS` | `PLS_INTEGER` | Operating system audit trail. This refers to the audit records stored in operating system files. |
| `AUDIT_TRAIL_XML` | `PLS_INTEGER` | XML audit trail. This refers to the audit records stored in XML files. |

Audit trail properties determine the audit configuration settings. Table 27-2 lists the constants related to audit trail properties.

Table 27-2 DBMS\_AUDIT\_MGMT Constants - Audit Trail Properties

| Constant | Type | Description |
| --- | --- | --- |
| `CLEAN_UP_INTERVAL` | `PLS_INTEGER` | Interval, in hours, after which the cleanup procedure is called to clear audit records in the specified audit trail |
| `DB_DELETE_BATCH_SIZE` | `PLS_INTEGER` | Specifies the batch size to be used for deleting audit records in database audit tables. The audit records are deleted in batches of size equal to `DB_DELETE_BATCH_SIZE`. |
| `FILE_DELETE_BATCH_SIZE` | `PLS_INTEGER` | Specifies the batch size to be used for deleting audit files in the audit directory. The audit files are deleted in batches of size equal to `FILE_DELETE_BATCH_SIZE`. |
| `OS_FILE_MAX_AGE` | `PLS_INTEGER` | Specifies the maximum number of days for which an operating system (OS) or XML audit file can be kept open before a new audit file gets created |
| `OS_FILE_MAX_SIZE` | `PLS_INTEGER` | Specifies the maximum size, in kilobytes (KB), to which an operating system (OS) or XML audit file can grow before a new file is opened |

The audit trail purge job cleans the audit trail. Table 27-3 lists the constants related to purge job status values.

Table 27-3 DBMS\_AUDIT\_MGMT Constants - Purge Job Status

| Constant | Type | Description |
| --- | --- | --- |
| `PURGE_JOB_DISABLE` | `PLS_INTEGER` | Disables a purge job |
| `PURGE_JOB_ENABLE` | `PLS_INTEGER` | Enables a purge job |

---

### Views

The views listed in Table 27-4 are used to display `DBMS_AUDIT_MGMT` configuration and cleanup events.

Table 27-4 Views used by DBMS\_AUDIT\_MGMT

| View | Description |
| --- | --- |
| `DBA_AUDIT_MGMT_CLEAN_EVENTS` | Displays the cleanup event history |
| `DBA_AUDIT_MGMT_CLEANUP_JOBS` | Displays the currently configured audit trail purge jobs |
| `DBA_AUDIT_MGMT_CONFIG_PARAMS` | Displays the currently configured audit trail properties |
| `DBA_AUDIT_MGMT_LAST_ARCH_TS` | Displays the last archive timestamps set for the audit trails |

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information on these views

---

## Subprogram Groups

The `DBMS_AUDIT_MGMT` package subprograms can be grouped into the following categories:

- Audit Trail Management Subprograms
- Audit Trail Cleanup Subprograms

---

### Audit Trail Management Subprograms

Audit trail management subprograms enable you to manage audit trail properties.

Table 27-5 Audit Trail Management Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAR\_AUDIT\_TRAIL\_PROPERTY Procedure | Clears the value for the audit trail property that you specify |
| SET\_AUDIT\_TRAIL\_LOCATION Procedure | Moves the audit trail tables from their current tablespace to a user-specified tablespace |
| SET\_AUDIT\_TRAIL\_PROPERTY Procedure | Sets an audit trail property for the audit trail type that you specify |

The Summary of DBMS\_AUDIT\_MGMT Subprograms contains a complete listing of all subprograms in the package.

---

### Audit Trail Cleanup Subprograms

Audit trail cleanup subprograms help you perform cleanup related operations on the audit trail records.

Table 27-6 Audit Trail Cleanup Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAN\_AUDIT\_TRAIL Procedure | Deletes audit trail records/files that have been archived |
| CLEAR\_LAST\_ARCHIVE\_TIMESTAMP Procedure | Clears the timestamp set by the SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure |
| CREATE\_PURGE\_JOB Procedure | Creates a purge job for periodically deleting the audit trail records/files |
| DEINIT\_CLEANUP Procedure | Undoes the setup and initialization performed by the INIT\_CLEANUP Procedure |
| DROP\_PURGE\_JOB Procedure | Drops the purge job created using the CREATE\_PURGE\_JOB Procedure |
| INIT\_CLEANUP Procedure | Sets up the audit management infrastructure and sets a default cleanup interval for audit trail records/files |
| IS\_CLEANUP\_INITIALIZED Function | Checks to see if the INIT\_CLEANUP Procedure has been run for an audit trail type |
| SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure | Sets a timestamp indicating when the audit records/files were last archived |
| SET\_PURGE\_JOB\_INTERVAL Procedure | Sets the interval at which the CLEAN\_AUDIT\_TRAIL Procedure is called for the purge job that you specify |
| SET\_PURGE\_JOB\_STATUS Procedure | Enables or disables the purge job that you specify |

The Summary of DBMS\_AUDIT\_MGMT Subprograms contains a complete listing of all subprograms in the package.

---

## Summary of DBMS\_AUDIT\_MGMT Subprograms

Table 27-7 DBMS\_AUDIT\_MGMT Package Subprograms

| Subprogram | Description |
| --- | --- |
| CLEAN\_AUDIT\_TRAIL Procedure | Deletes audit trail records that have been archived |
| CLEAR\_AUDIT\_TRAIL\_PROPERTY Procedure | Clears the value for the audit trail property that you specify |
| CLEAR\_LAST\_ARCHIVE\_TIMESTAMP Procedure | Clears the timestamp set by the SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure |
| CREATE\_PURGE\_JOB Procedure | Creates a purge job for periodically deleting the audit trail records |
| DEINIT\_CLEANUP Procedure | Undoes the setup and initialization performed by the INIT\_CLEANUP Procedure |
| DROP\_PURGE\_JOB Procedure | Drops the purge job created using the CREATE\_PURGE\_JOB Procedure |
| GET\_AUDIT\_COMMIT\_DELAY Function | Returns the Audit Commit Delay as the number of seconds. This is the maximum time that it takes to `COMMIT` an audit record to the database audit trail. |
| INIT\_CLEANUP Procedure | Sets up the audit management infrastructure and sets a default cleanup interval for audit trail records |
| IS\_CLEANUP\_INITIALIZED Function | Checks to see if the INIT\_CLEANUP Procedure has been run for an audit trail type |
| SET\_AUDIT\_TRAIL\_LOCATION Procedure | Moves the audit trail tables from their current tablespace to a user-specified tablespace |
| SET\_AUDIT\_TRAIL\_PROPERTY Procedure | Sets the audit trail properties for the audit trail type that you specify |
| SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure | Sets a timestamp indicating when the audit records were last archived |
| SET\_PURGE\_JOB\_INTERVAL Procedure | Sets the interval at which the CLEAN\_AUDIT\_TRAIL Procedure is called for the purge job that you specify |
| SET\_PURGE\_JOB\_STATUS Procedure | Enables or disables the purge job that you specify |

---

### CLEAN\_AUDIT\_TRAIL Procedure

This procedure deletes audit trail records. The `CLEAN_AUDIT_TRAIL` procedure is usually called after the SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure has been used to set the last archived timestamp for the audit records.

Syntax

```
DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL(
   audit_trail_type         IN PLS_INTEGER,
   use_last_arch_timestamp  IN BOOLEAN DEFAULT TRUE) ;
```

Parameters

Table 27-8 CLEAN\_AUDIT\_TRAIL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the cleanup operation needs to be performed. Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types". |
| `use_last_arch_timestamp` | Specifies whether the last archived timestamp should be used for deciding on the records that should be deleted.  A value of `TRUE` indicates that only audit records created before the last archive timestamp should be deleted.  A value of `FALSE` indicates that all audit records should be deleted.  The default value is `TRUE`. Oracle recommends using this value, as this helps guard against inadvertent deletion of records. |

Usage Notes

The following usage notes apply:

- When cleaning up operating system (OS) or XML audit files, only files in the current audit directory, specified by the `AUDIT_FILE_DEST` parameter, are cleaned up.
- For Windows platforms, no cleanup is performed when the `audit_trail_type` parameter is set to `DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS.` This is because operating system (OS) audit records on Windows are written to the Windows Event Viewer.
- For Unix platforms, no cleanup is performed for cases where the operating system (OS) audit records are written to the syslog. When the `audit_trail_type` parameter is set to `DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,` it removes only the `*.aud` files under the directory specified by the `AUDIT_FILE_DEST` initialization parameter.
	See Also:
	["AUDIT\_SYSLOG\_LEVEL"](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams016.htm#REFRN10263) in the Oracle Database Reference
- When the `audit_trail_type` parameter is set to `DBMS_AUDIT_MGMT.AUDIT_TRAIL_XML,` this procedure only removes XML audit files (`*.xml`) from the current audit directory.
	Oracle database maintains a book-keeping file `(adx_` `$ORACLE_SID``.txt`) for the XML audit files. This file is not removed by the cleanup procedure.

Examples

The following example calls the `CLEAN_AUDIT_TRAIL` procedure to clean up the operating system (OS) audit trail records that were updated before the last archive timestamp.

```
BEGIN
DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL(
   audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,
   use_last_arch_timestamp => TRUE);
END;
/
```

---

### CLEAR\_AUDIT\_TRAIL\_PROPERTY Procedure

This procedure clears the value for the audit trail property that is specified. Audit trail properties are set using the SET\_AUDIT\_TRAIL\_PROPERTY Procedure.

The `CLEAR_AUDIT_TRAIL_PROPERTY` procedure can optionally reset the property value to it's default value through the `use_default_values` parameter.

Syntax

```
DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY(
   audit_trail_type        IN PLS_INTEGER,
   audit_trail_property    IN PLS_INTEGER,
   use_default_values      IN BOOLEAN DEFAULT FALSE) ;
```

Parameters

Table 27-9 CLEAR\_AUDIT\_TRAIL\_PROPERTY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the property needs to be cleared. Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" |
| `audit_trail_property` | The audit trail property whose value needs to be cleared. You cannot clear the value for the `CLEANUP_INTERVAL` property.  Audit trail properties are listed in Table 27-2, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Properties" |
| `use_default_values` | Specifies whether the default value of the `audit_trail_property` should be used in place of the cleared value. A value of `TRUE` causes the default value of the parameter to be used. A value of `FALSE` causes the `audit_trail_property` to have no value.  The default value for this parameter is `FALSE`. |

Usage Notes

The following usage notes apply:

- You can use this procedure to clear the value for an audit trail property that you do not wish to use. For example, if you do not want a restriction on the operating system audit file size, then you can use this procedure to reset the `OS_FILE_MAX_SIZE` property.
	You can also use this procedure to reset an audit trail property to it's default value. You need to set `use_default_values` to `TRUE` when invoking the procedure.
- The `DB_DELETE_BATCH_SIZE` property needs to be individually cleared for the `AUDIT_TRAIL_AUD_STD` and `AUDIT_TRAIL_FGA_STD` audit trail types. You cannot clear this property collectively using the `AUDIT_TRAIL_DB_STD` and `AUDIT_TRAIL_ALL` audit trail types.
- If you clear the value of the DB\_DELETE\_BATCH\_SIZE property with `use_default_value` set to `FALSE`, the default value of DB\_DELETE\_BATCH\_SIZE is still assumed. This is because audit records are always deleted in batches.
- The `FILE_DELETE_BATCH_SIZE` property needs to be individually cleared for the `AUDIT_TRAIL_OS` and `AUDIT_TRAIL_XML` audit trail types. You cannot clear this property collectively using the `AUDIT_TRAIL_FILES` and `AUDIT_TRAIL_ALL` audit trail types.
- If you clear the value of the FILE\_DELETE\_BATCH\_SIZE property with `use_default_value` set to `FALSE`, the default value of FILE\_DELETE\_BATCH\_SIZE is still assumed. This is because audit files are always deleted in batches.
- You cannot clear the value for the `CLEANUP_INTERVAL` property.

Examples

The following example calls the `CLEAR_AUDIT_TRAIL_PROPERTY` procedure to clear the value for the audit trail property, `OS_FILE_MAX_SIZE`. The procedure uses a value of `FALSE` for the `USE_DEFAULT_VALUES` parameter. This means that there will be no maximum size threshold for operating system (OS) audit files.

```
BEGIN
DBMS_AUDIT_MGMT.CLEAR_AUDIT_TRAIL_PROPERTY(
   AUDIT_TRAIL_TYPE        =>  DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,
   AUDIT_TRAIL_PROPERTY    =>  DBMS_AUDIT_MGMT.OS_FILE_MAX_SIZE,
   USE_DEFAULT_VALUES      =>  FALSE );
END;
/
```

---

### CLEAR\_LAST\_ARCHIVE\_TIMESTAMP Procedure

This procedure clears the timestamp set by the SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure.

Syntax

```
DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type     IN PLS_INTEGER,
   rac_instance_number  IN PLS_INTEGER DEFAULT NULL) ;
```

Parameters

Table 27-10 CLEAR\_LAST\_ARCHIVE\_TIMESTAMP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the timestamp needs to be cleared. Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types". |
| `rac_instance_number` | The instance number for the Oracle Real Application Clusters (Oracle RAC) instance. The default value is `NULL`.  The `rac_instance_number` is not relevant for single instance databases. |

Usage Notes

The following usage notes apply:

- The timestamp for only one `audit_trail_type` can be cleared at a time.
- The following are invalid `audit_trail_type` values for this procedure and cannot be used:
	- AUDIT\_TRAIL\_ALL
		- AUDIT\_TRAIL\_DB\_STD
		- AUDIT\_TRAIL\_FILES

Examples

The following example calls the `CLEAR_LAST_ARCHIVE_TIMESTAMP` procedure to clear the timestamp value for the operating system (OS) audit trail type.

```
BEGIN
DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type     =>  DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,
   rac_instance_number  =>  1);
END;
/
```

---

### CREATE\_PURGE\_JOB Procedure

This procedure creates a purge job for periodically deleting the audit trail records.

This procedure carries out the cleanup operation at intervals specified by the user. It calls the CLEAN\_AUDIT\_TRAIL Procedure to perform the cleanup operation.

The SET\_PURGE\_JOB\_INTERVAL Procedure is used to modify the frequency of the purge job.

The SET\_PURGE\_JOB\_STATUS Procedure is used to enable or disable the purge job.

The DROP\_PURGE\_JOB Procedure is used to drop a purge job created with the `CREATE_PURGE_JOB` procedure.

Syntax

```
DBMS_AUDIT_MGMT.CREATE_PURGE_JOB(
   audit_trail_type            IN PLS_INTEGER,
   audit_trail_purge_interval  IN PLS_INTEGER,
   audit_trail_purge_name      IN VARCHAR2,
   use_last_arch_timestamp     IN BOOLEAN DEFAULT TRUE) ;
```

Parameters

Table 27-11 CREATE\_PURGE\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the purge job needs to be created. Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types". |
| `audit_trail_purge_interval` | The interval, in hours, at which the clean up procedure is called. A lower value means that the cleanup is performed more often. |
| `audit_trail_purge_name` | A name to identify the purge job. |
| `use_last_arch_timestamp` | Specifies whether the last archived timestamp should be used for deciding on the records that should be deleted.  A value of `TRUE` indicates that only audit records created before the last archive timestamp should be deleted.  A value of `FALSE` indicates that all audit records should be deleted.  The default value is `TRUE`. |

Usage Notes

Use this procedure to schedule the CLEAN\_AUDIT\_TRAIL Procedure for your audit trail records.

Examples

The following example calls the `CREATE_PURGE_JOB` procedure to create a cleanup job called `CLEANUP`, for all audit trail types. It sets the `audit_trail_purge_interval` parameter to 100. This means that the cleanup job is invoked every 100 hours. It also sets the `use_last_arch_timestamp` parameter value to `TRUE`. This means that all audit records older than the last archive timestamp are deleted.

```
BEGIN
DBMS_AUDIT_MGMT.CREATE_PURGE_JOB(
  audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_ALL,
  audit_trail_purge_interval => 100 /* hours */,  
  audit_trail_purge_name => 'CLEANUP',
  use_last_arch_timestamp => TRUE);
END;
/
```

---

### DEINIT\_CLEANUP Procedure

This procedure undoes the setup and initialization performed by the INIT\_CLEANUP Procedure. The `DEINIT_CLEANUP` procedure clears the value of the `default_cleanup_interval` parameter. However, when used for audit tables, it does not move the audit trail tables back to their original tablespace.

Syntax

```
DBMS_AUDIT_MGMT.DEINIT_CLEANUP(
   audit_trail_type  IN PLS_INTEGER) ;
```

Parameters

Table 27-12 DEINIT\_CLEANUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the procedure needs to be called.  Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" |

Examples

The following example clears the `default_cleanup_interval` parameter setting for the standard database audit trail:

```
BEGIN
DBMS_AUDIT_MGMT.DEINIT_CLEANUP(
  AUDIT_TRAIL_TYPE  => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD);
END;
/
```

---

### DROP\_PURGE\_JOB Procedure

This procedure drops the purge job created using the CREATE\_PURGE\_JOB Procedure. The name of the purge job is passed as an argument.

Syntax

```
DBMS_AUDIT_MGMT.DROP_PURGE_JOB(
   audit_trail_purge_name    IN VARCHAR2) ;
```

Parameters

Table 27-13 DROP\_PURGE\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_` purge\_name | The name of the purge job which is being deleted. This is the purge job name that you specified with the CREATE\_PURGE\_JOB Procedure. |

Examples

The following example calls the DROP\_PURGE\_JOB procedure to drop the purge job called `CLEANUP`.

```
BEGIN
DBMS_AUDIT_MGMT.DROP_PURGE_JOB(
  AUDIT_TRAIL_PURGE_NAME  => 'CLEANUP');
END;
/
```

---

### GET\_AUDIT\_COMMIT\_DELAY Function

This function returns the Audit Commit Delay as the number of seconds. Audit Commit Delay is the maximum time that it takes to `COMMIT` an audit record to the database audit trail. If it takes more time to COMMIT an audit record than defined by the Audit Commit Delay, then a copy of the audit record is written to the operating system (OS) audit trail.

The Audit Commit Delay value is useful when determining the last archive timestamp for database audit records.

Syntax

```
DBMS_AUDIT_MGMT.GET_AUDIT_COMMIT_DELAY
  RETURN NUMBER;
```

---

### INIT\_CLEANUP Procedure

This procedure sets up the audit management infrastructure and a default cleanup interval for the audit trail records. If the audit trail tables are in the `SYSTEM` tablespace, then the procedure moves them to the `SYSAUX` tablespace.

Moving the audit trail tables out of the `SYSTEM` tablespace enhances overall database performance. The `INIT_CLEANUP` procedure moves the audit trail tables to the `SYSAUX` tablespace. If the SET\_AUDIT\_TRAIL\_LOCATION Procedure has already moved the audit tables elsewhere, then no tables are moved.

The SET\_AUDIT\_TRAIL\_LOCATION Procedure enables you to specify an alternate target tablespace for the database audit tables.

The `INIT_CLEANUP` procedure is currently not relevant for the `AUDIT_TRAIL_OS`, `AUDIT_TRAIL_XML`, and `AUDIT_TRAIL_FILES` audit trail types. No preliminary set up is required for these audit trail types.

See Also:

Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" for a list of all audit trail types

This procedure also sets a default cleanup interval for the audit trail records.

Syntax

```
DBMS_AUDIT_MGMT.INIT_CLEANUP(
   audit_trail_type          IN PLS_INTEGER,
   default_cleanup_interval  IN PLS_INTEGER);
```

Parameters

Table 27-14 INIT\_CLEANUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the clean up operation needs to be initialized.  Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" |
| `default_cleanup_interval` | The default time interval, in hours, after which the cleanup procedure should be called. The minimum value is 1 and the maximum is 999. |

Usage Notes

The following usage notes apply:

- This procedure may involve data movement across tablespaces. This can be a resource intensive operation especially if your database audit trail tables are already populated. Oracle recommends that you invoke the procedure during non-peak hours.
- You should ensure that the `SYSAUX` tablespace, into which the audit trail tables are being moved, has sufficient space to accommodate the audit trail tables. You should also optimize the `SYSAUX` tablespace for frequent write operations.
- You can change the `default_cleanup_interval` later using the SET\_AUDIT\_TRAIL\_PROPERTY Procedure.
- If you do not wish to move the audit trail tables to the `SYSAUX` tablespace, then you should use the `DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION` procedure to move the audit trail tables to another tablespace before calling the `INIT_CLEANUP` procedure.
	See Also:
	"SET\_AUDIT\_TRAIL\_LOCATION Procedure"

Examples

The following example calls the `INIT_CLEANUP` procedure to set a `default_cleanup_interval` of 12 hours for all audit trail types:

```
BEGIN
DBMS_AUDIT_MGMT.INIT_CLEANUP(
              audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_ALL,
      default_cleanup_interval => 12 /* hours */);
END;
/
```

See Also:

Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" for a list of all audit trail types

---

### IS\_CLEANUP\_INITIALIZED Function

This function checks to see if the INIT\_CLEANUP Procedure has been run for an audit trail type. The `IS_CLEANUP_INITIALIZED` function returns `TRUE` if the procedure has already been run for the audit trail type. It returns `FALSE` if the procedure has not been run for the audit trail type.

This function is currently not relevant for the `AUDIT_TRAIL_OS`, `AUDIT_TRAIL_XML`, and `AUDIT_TRAIL_FILES` audit trail types. The function always returns TRUE for these audit trail types. No preliminary set up is required for these audit trail types.

See Also:

Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" for a list of all audit trail types

Syntax

```
DBMS_AUDIT_MGMT.DEINIT_CLEANUP(
   audit_trail_type  IN PLS_INTEGER)
 RETURN BOOLEAN;
```

Parameters

Table 27-15 IS\_CLEANUP\_INITIALIZED Function Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the function needs to be called.  Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" |

Examples

The following example checks to see if the standard database audit trail type has been initialized for cleanup operation. If the audit trail type has not been initialized, then it calls the INIT\_CLEANUP Procedure to initialize the audit trail type.

```
BEGIN
 IF 
   NOT DBMS_AUDIT_MGMT.IS_CLEANUP_INITIALIZED(DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD)
 THEN
   DBMS_AUDIT_MGMT.INIT_CLEANUP(
      audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD,
      default_cleanup_interval => 12 /* hours */);
 END IF;
END;
/
```

---

### SET\_AUDIT\_TRAIL\_LOCATION Procedure

This procedure moves the audit trail tables from their current tablespace to a user-specified tablespace.

The `SET_AUDIT_TRAIL_LOCATION` procedure is currently not relevant for the `AUDIT_TRAIL_OS`, `AUDIT_TRAIL_XML`, and `AUDIT_TRAIL_FILES` audit trail types. The `AUDIT_FILE_DEST` initialization parameter is the only way you can specify the destination directory for these audit trail types.

See Also:

- Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" for a list of all audit trail types
- ["AUDIT\_FILE\_DEST"](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams014.htm#REFRN10004) in the Oracle Database Reference

Syntax

```
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION(
   audit_trail_type            IN PLS_INTEGER,
   audit_trail_location_value  IN VARCHAR2) ;
```

Parameters

Table 27-16 SET\_AUDIT\_TRAIL\_LOCATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the audit trail location needs to be set.  Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" |
| `audit_trail_location_value` | The target location/tablespace for the audit trail records |

Usage Notes

The following usage notes apply:

- This procedure involves data movement across tablespaces. This can be a resource intensive operation especially if your database audit trail tables are already populated. Oracle recommends that you invoke the procedure during non-peak hours.
- You should ensure that the target tablespace, into which the audit trail tables are being moved, has sufficient space to accommodate the audit trail tables. You should also optimize the target tablespace for frequent write operations.
- This procedure is valid for the following `audit_trail_type` values only:
	- AUDIT\_TRAIL\_AUD\_STD
		- AUDIT\_TRAIL\_FGA\_STD
		- AUDIT\_TRAIL\_DB\_STD

Examples

The following example moves the database audit trail tables, `AUD$` and `FGA_LOG$`, from the current tablespace to a user-created tablespace called `RECORDS`:

```
BEGIN
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION(
       audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_DB_STD,
       audit_trail_location_value =>  'RECORDS');
END;
/
```

---

### SET\_AUDIT\_TRAIL\_PROPERTY Procedure

This procedure sets an audit trail property for the audit trail type that is specified.

The procedure sets properties like `OS_FILE_MAX_SIZE`, `OS_FILE_MAX_AGE`, and `FILE_DELETE_BATCH_SIZE` for operating system (OS) and XML audit trail types. The `OS_FILE_MAX_SIZE` and `OS_FILE_MAX_AGE` properties determine the maximum size and age of an audit trail file before a new audit trail file gets created. The `FILE_DELETE_BATCH_SIZE` property specifies the number of audit trail files that are deleted in one batch.

The procedure sets properties like `DB_DELETE_BATCH_SIZE` and `CLEANUP_INTERVAL` for the database audit trail type. `DB_DELETE_BATCH_SIZE` specifies the batch size in which records get deleted from audit trail tables. This ensures that if a cleanup operation gets interrupted midway, the process does not need to start afresh the next time it is invoked. This is because all batches before the last processed batch are already committed.

The `CLEANUP_INTERVAL` specifies the frequency, in hours, with which the cleanup procedure is called.

Syntax

```
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY(
   audit_trail_type            IN PLS_INTEGER,
   audit_trail_property        IN PLS_INTEGER,
   audit_trail_property_value  IN PLS_INTEGER) ;
```

Parameters

Table 27-17 SET\_AUDIT\_TRAIL\_PROPERTY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the property needs to be set. Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types" |
| `audit_trail_property` | The audit trail property that is being set. Audit trail properties are listed in Table 27-2, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Properties" |
| `audit_trail_property_value` | The value of the property specified using `audit_trail_property`. The following are valid values for audit trail properties:  - `OS_FILE_MAX_SIZE` can have a minimum value of 1 and maximum value of 2000000. The default value is 10000. `OS_FILE_MAX_SIZE` is measured in kilobytes (KB). - `OS_FILE_MAX_AGE` can have a minimum value of 1 and a maximum value of 497. The default value is 5. `OS_FILE_MAX_AGE` is measured in days. - `DB_DELETE_BATCH_SIZE` can have a minimum value of 100 and a maximum value of 1000000. The default value is 10000. `DB_DELETE_BATCH_SIZE` is measured as the number of audit records that are deleted in one batch. - `FILE_DELETE_BATCH_SIZE` can have a minimum value of 100 and a maximum value of 1000000. The default value is 1000. `FILE_DELETE_BATCH_SIZE` is measured as the number of audit files that are deleted in one batch. - `CLEANUP_INTERVAL` can have a minimum value of 1 and a maximum value of 999. The default value is set using the INIT\_CLEANUP Procedure. `CLEANUP_INTERVAL` is measured in hours. |

Usage Notes

The following usage notes apply:

- The audit trail properties for which you do not explicitly set values use their default values.
- If you have set both the `OS_FILE_MAX_SIZE` and `OS_FILE_MAX_AGE` properties for an operating system (OS) or XML audit trail type, then a new audit trail file gets created depending on which of these two limits is reached first.
	For example, let us take a scenario where `OS_FILE_MAX_SIZE` is 10000 and `OS_FILE_MAX_AGE` is 5. If the operating system audit file is already more than 5 days old and has a size of 9000 KB, then a new audit file is opened. This is because one of the limits has been reached.
- The `DB_DELETE_BATCH_SIZE` property needs to be individually set for the `AUDIT_TRAIL_AUD_STD` and `AUDIT_TRAIL_FGA_STD` audit trail types. You cannot set this property collectively using the `AUDIT_TRAIL_DB_STD` and `AUDIT_TRAIL_ALL` audit trail types.
- The `DB_DELETE_BATCH_SIZE` property enables you to control the number of audit records that are deleted in one batch. Setting a large value for this parameter requires increased allocation for the undo log space.
- The `FILE_DELETE_BATCH_SIZE` property needs to be individually set for the `AUDIT_TRAIL_OS` and `AUDIT_TRAIL_XML` audit trail types. You cannot set this property collectively using the `AUDIT_TRAIL_FILES` and `AUDIT_TRAIL_ALL` audit trail types.
- The `FILE_DELETE_BATCH_SIZE` property enables you to control the number of audit files that are deleted in one batch. Setting a very large value may engage the `GEN0` background process for a long time.

Examples

The following example calls the `SET_AUDIT_TRAIL_PROPERTY` procedure to set the `OS_FILE_MAX_SIZE` property for the operating system (OS) audit trail. It sets this property value to 102400. This means that a new audit file gets created every time the current audit file size reaches 100 MB.

```
BEGIN
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY(
       audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,
       audit_trail_property  =>  DBMS_AUDIT_MGMT.OS_FILE_MAX_SIZE,
       audit_trail_property_value =>  102400 /* 100MB*/ );
END;
/
```

The following example calls the `SET_AUDIT_TRAIL_PROPERTY` procedure to set the `OS_FILE_MAX_AGE` property for the operating system (OS) audit trail. It sets this property value to 5. This means that a new audit file gets created every sixth day.

```
BEGIN
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY(
       audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,
       audit_trail_property  =>  DBMS_AUDIT_MGMT.OS_FILE_MAX_AGE,
       audit_trail_property_value  =>  5 /* days */);
END;
/
```

The following example calls the `SET_AUDIT_TRAIL_PROPERTY` procedure to set the `DB_DELETE_BATCH_SIZE` property for the `AUDIT_TRAIL_AUD_STD` audit trail. It sets this property value to 100000. This means that during a cleanup operation, audit records are deleted from the `SYS.AUD$` table in batches of size 100000.

```
BEGIN
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY(
       audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_AUD_STD,
       audit_trail_property => DBMS_AUDIT_MGMT.DB_DELETE_BATCH_SIZE,
       audit_trail_property_value => 100000 /* delete batch size */);
END;
/
```

---

### SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure

This procedure sets a timestamp indicating when the audit records were last archived. The audit administrator provides the timestamp to be attached to the audit records. The CLEAN\_AUDIT\_TRAIL Procedure uses this timestamp to decide on the audit records to be deleted.

Syntax

```
DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type     IN PLS_INTEGER,
   last_archive_time    IN TIMESTAMP,
   rac_instance_number  IN PLS_INTEGER DEFAULT NULL) ;
```

Parameters

Table 27-18 SET\_LAST\_ARCHIVE\_TIMESTAMP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_type` | The audit trail type for which the timestamp needs to be set. Audit trail types are listed in Table 27-1, "DBMS\_AUDIT\_MGMT Constants - Audit Trail Types". |
| `last_archive_time` | The `TIMESTAMP` value based on which the audit records or files should be deleted. This indicates the last time when the audit records/files were archived. |
| `rac_instance_number` | The instance number for the Oracle Real Application Clusters (Oracle RAC) instance.The default value is `NULL`.  The `rac_instance_number` is not relevant for the database audit trail type, as the database audit trail tables are shared by all Oracle RAC instances. The `rac_instance_number` is also not relevant for a single-instance database. |

Usage Notes

The following usage notes apply:

- The `last_archive_time` must be specified in Coordinated Universal Time (UTC) when the audit trail types are `AUDIT_TRAIL_AUD_STD` or `AUDIT_TRAIL_FGA_STD`. This is because the database audit trails store the timestamps in UTC. UTC is also known as Greenwich Mean Time (GMT).
- The `last_archive_time` must be specified as the local time zone time when the audit trail types are `AUDIT_TRAIL_OS` or `AUDIT_TRAIL_XML`. The time zone must be the time zone of the machine where the OS or XML audit files were created. This is because the operating system audit files are cleaned based on the audit file's Last Modification Timestamp property. The Last Modification Timestamp property value is stored in the local time zone of the machine.
- The following `audit_trail_type` values for valid for this procedure:
	- `AUDIT_TRAIL_AUD_STD`
		- `AUDIT_TRAIL_FGA_STD`
		- `AUDIT_TRAIL_OS`
		- `AUDIT_TRAIL_XML`
- When using an Oracle Real Application Clusters (Oracle RAC) database, Oracle recommends that you use the Network Time Protocol (NTP) to synchronize individual Oracle RAC nodes.

Examples

The following example calls the `SET_LAST_ARCHIVE_TIMESTAMP` procedure to set the last archive timestamp for the operating system (OS) audit trail type on Oracle RAC instance 1. It uses the `TO_TIMESTAMP` function to convert a character string into a timestamp value.

A subsequent call to the CLEAN\_AUDIT\_TRAIL Procedure, with `use_last_arch_timestamp` set to `TRUE`, will delete all those OS audit files from the current `AUDIT_FILE_DEST` directory that were modified before 10-Sep-2007 14:10:10.0.

```
BEGIN
DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS,
   last_archive_time => TO_TIMESTAMP('10-SEP-0714:10:10.0','DD-MON-RRHH24:MI:SS.FF'),
   rac_instance_number => 1);
END;
/
```

---

### SET\_PURGE\_JOB\_INTERVAL Procedure

This procedure sets the interval at which the CLEAN\_AUDIT\_TRAIL Procedure is called for the purge job specified. The purge job must have already been created using the CREATE\_PURGE\_JOB Procedure.

Syntax

```
DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL(
   audit_trail_purge_name      IN VARCHAR2,
   audit_trail_interval_value  IN PLS_INTEGER) ;
```

Parameters

Table 27-19 SET\_PURGE\_JOB\_INTERVAL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_purge_name` | The name of the purge job for which the interval is being set. This is the purge job name that you specified with the CREATE\_PURGE\_JOB Procedure. |
| `audit_trail_interval_value` | The interval, in hours, at which the clean up procedure should be called. This value modifies the audit\_trail\_purge\_interval parameter set using the CREATE\_PURGE\_JOB Procedure |

Usage Notes

Use this procedure to modify the audit\_trail\_purge\_interval parameter set using the CREATE\_PURGE\_JOB Procedure.

Examples

The following example calls the `SET_PURGE_JOB_INTERVAL` procedure to change the frequency at which the purge job called `CLEANUP` is invoked. The new interval is set to 24 hours.

```
BEGIN
DBMS_AUDIT_MGMT.SET_PURGE_JOB_INTERVAL(
  AUDIT_TRAIL_PURGE_NAME       => 'CLEANUP',
  AUDIT_TRAIL_INTERVAL_VALUE   => 24 );
END;
/
```

---

### SET\_PURGE\_JOB\_STATUS Procedure

This procedure enables or disables the specified purge job. The purge job must have already been created using the CREATE\_PURGE\_JOB Procedure.

Syntax

```
DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS(
   audit_trail_purge_name    IN VARCHAR2,
   audit_trail_status_value  IN PLS_INTEGER) ;
```

Parameters

Table 27-20 SET\_PURGE\_JOB\_STATUS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `audit_trail_purge_name` | The name of the purge job for which the status is being set. This is the purge job name that you specified with the CREATE\_PURGE\_JOB Procedure. |
| `audit_trail_status_value` | One of the values specified in DBMS\_AUDIT\_MGMT Constants - Purge Job Status.  The value `PURGE_JOB_ENABLE` enables the specified purge job.  The value `PURGE_JOB_DISABLE` disables the specified purge job. |

Examples

The following example calls the SET\_PURGE\_JOB\_STATUS procedure to enable the `CLEANUP` purge job.

```
BEGIN
DBMS_AUDIT_MGMT.SET_PURGE_JOB_STATUS(
  audit_trail_purge_name      => 'CLEANUP',
  audit_trail_status_value    => DBMS_AUDIT_MGMT.PURGE_JOB_ENABLE);
END;
/
```