---
title: Documentation Addendum
book: Readme
doc_id: E41331-17
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/doc_addendum.htm
tags:
  - oracle
  - 11g
  - readme
---

## 6 Documentation Addendum

This section contains corrections to the following Oracle Documentation:

Section 6.1, "Oracle Automatic Storage Management Administrator's Guide"

Section 6.2, "Oracle Clusterware Administration and Deployment Guide"

Section 6.3, "Oracle Database Backup and Recovery Reference"

Section 6.4, "Oracle Database Backup and Recovery User's Guide"

Section 6.5, "Oracle Database Data Warehousing Guide"

Section 6.6, "Oracle Database Net Services Reference"

Section 6.7, "Oracle Database Reference"

Section 6.8, "Oracle Database Utilities"

Section 6.9, "Oracle Real Application Clusters Administration and Deployment Guide"

Section 6.10, "Oracle Real Application Clusters Installation Guide"

Section 6.11, "Oracle Text Application Developer's Guide"

Section 6.12, "Oracle Text Reference"

## 6.1 Oracle Automatic Storage Management Administrator's Guide

Note the following changes with regard to the Oracle Automatic Storage Management Administrator's Guide, 11g release 2 (11.2), part number E18951.

### 6.1.1 Chapter 1: Introduction to Oracle Automatic Storage Management

In the section "Extents" found in the section titled "About Oracle ASM Files" under the main section titled "Understanding Oracle ASM Concepts" should read as follows:

The contents of Oracle ASM files are stored in a disk group as a set, or collection, of extents that are stored on individual disks within disk groups. Each extent resides on an individual disk. Extents consist of one or more allocation units (AU). To accommodate increasingly larger files, Oracle ASM uses variable size extents.

Variable size extents enable support for larger Oracle ASM data files, reduce SGA memory requirements for very large databases, and improve performance for file create and open operations. The initial extent size equals the disk group allocation unit size and it increases by a factor of 4 or 16 at predefined thresholds. This feature is automatic for newly created and resized data files when specific disk group compatibility attributes are set to 11.1 or higher. For information about compatibility attributes, see "Disk Group Compatibility".

For disk groups with an AU size less than 4 MB, the extent size of a file varies as follows:

- Extent size always equals the disk group AU size for the first 20000 extent sets (0 - 19999).
- Extent size equals 4\*AU size for the next 20000 extent sets (20000 - 39999).
- Extent size equals 16\*AU size for the next 20000 and higher extent sets (40000+).

Figure 1-4 shows the Oracle ASM file extent relationship with allocation units...

For disk groups with AU sizes greater than or equal to 4 MB, the extent size of a file, depending on the redundancy of the disk group, varies as follows:

- For the 4 MB AU size, the extent size equals the disk group AU size for the first 15658728, 6710880, and 3728269 extents for external, normal, and high redundancy disk groups respectively.
- For the 8 MB AU size, the extent size equals the disk group AU size for the first 16777216, 7829368, and 4846749 extents for external, normal, and high redundancy disk groups respectively.
- For the 16 MB AU size, the extent size equals the disk group AU size for the first 16777216, 8388608, and 5405989 extents for external, normal, and high redundancy disk groups respectively.
- For the 32 MB AU size, the extent size equals the disk group AU size for the first 16777216, 8388608, and 5592405 extents for external, normal, and high redundancy disk groups respectively.

For all cases, the size of the remaining extent sets is 16\*AU size. Extents with a size equal to 4\*AU size are not created.

### 6.1.2 Chapter 3: Administering Oracle ASM Instances

In the PROCESSES description found in the section titled "Oracle ASM Parameter Setting Recommendations" under the section titled "Configuring Initialization Parameters for Oracle ASM Instances," the following paragraph should be included:

For Oracle Grid Infrastructure, 11g release 2 (11.2.0.3 and 11.2.0.4), the `PROCESSES` initialization parameter defaults to a value equal to "available CPU cores \* 80 + 40" in the Oracle ASM SPFILE. Because the default value for the `MEMORY_TARGET` initialization parameter is based on the value of `PROCESSES`, the value can be insufficient if there is a large number of CPU cores or a large number of disk groups. You should increase the value of the `MEMORY_MAX_TARGET` and `MEMORY_TARGET` initialization parameters before upgrading to or installing Oracle Grid Infrastructure, 11g release 2 (11.2.0.3 and 11.2.0.4).

### 6.1.3 Chapter 4: Administering Oracle ASM Disk Groups

In the STORAGE.TYPE description found in the section titled "Disk Group Attributes," the restriction that "ZFS storage must be added through Direct NFS (dNFS)" no longer applies if the `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes are set to 11.2.0.4 or higher

### 6.1.4 Chapter 12: Oracle ASM Command-Line Utility

Note the following changes with regard to Chapter 12 of the Oracle Automatic Storage Management Administrator's Guide, 11g release 2 (11.2), part number E18951.

#### 6.1.4.1 Section: ASMCMD Volume Management Commands

In the section "volcreate" found in the "ASMCMD Volume Management Commands" section, the following warning applies:

WARNING:

Specifying `--redundancy` unprotected means that Oracle ASM mirroring is not available for data recovery with the Oracle ADVM volume. The redundancy setting (normal) of the disk group does not provide mirroring for an unprotected Oracle ADVM volume. The unprotected configuration is not recommended for production environments as intermittent storage access failures can result in the loss of data. Backups are strongly recommended.

#### 6.1.4.2 Section: ASMCMD Disk Group Management Commands

In the section "iostat" of the "ASMCMD Disk Group Management Commands" section, the units for the I/O times specified by the `Read_Time` and `Write_Time` attributes should be seconds, not hundredths of seconds.

## 6.2 Oracle Clusterware Administration and Deployment Guide

Note the following changes with regard to the Oracle Clusterware Administration and Deployment Guide for 11g release 2 (11.2), part number E41959.

### 6.2.1 Chapter 4: Adding and Deleting Cluster Nodes

The Adding Cluster Node procedure does not list the extra steps required to successfully add a node to a cluster if the environment is Exadata. The steps in Chapter 4 work if the environment is non-Exadata. However, if you follow these steps to add a node to a cluster running on an Exadata machine, then `root.sh` fails because some of the required steps are missing.

The complete steps for adding a node to a cluster running on an Exadata machine are provided in Chapter 7 "Maintaining Oracle Exadata Racks" in the Oracle Exadata Database Machine Owner's Guide.

### 6.2.2 Chapter 5: Cloning Oracle Clusterware

In the section titled "Creating a Cluster by Cloning Oracle Clusterware," "Step 2: Deploy the Oracle Grid Infrastructure Home on the Destination Nodes" incorrectly instructs you to run the following commands to restore the cleared information:

```
chmod u+s Grid_home/bin/oracle 
chmod g+s Grid_home/bin/oracle 
chmod u+s Grid_home/bin/extjob 
chmod u+s Grid_home/bin/jssu 
chmod u+s Grid_home/bin/oradism
```

These instructions should be ignored. The Oracle Clusterware Administration and Deployment Guide is fixed in 12c release 1 (12.1) and higher releases.

### 6.2.3 Chapter 6: Making Applications Highly Available Using Oracle Clusterware

In the sub-section titled "Automatically Manage Restart Attempts Counter for Resources" in the section titled "Managing Automatic Restart of Oracle Clusterware Resources," the first three lines need to be replaced with the following:

"When a resource fails, Oracle Clusterware attempts to restart the resource the number of times specified in the `RESTART_ATTEMPTS` resource attribute. Note that this attribute does not specify the number of attempts to restart a failed resource (always one attempt), but rather the number of times the resource fails locally, before the Clusterware attempts to fail it over. The CRSD process maintains an internal counter to track how often Oracle Clusterware restarts a resource. The number of times Oracle Clusterware has restarted a resource locally is reflected in the `RESTART_COUNT` resource attribute."

## 6.3 Oracle Database Backup and Recovery Reference

Note the following changes with regard to the Oracle Database Backup and Recovery Reference for 11g release 2 (11.2), part number E10643.

### 6.3.1 Chapter 3: RMAN Commands: RECOVER to VALIDATE

In the Usage Notes for the `VALIDATE` command, second paragraph, the first two sentences need to be replaced with the following:

The `VALIDATE` command does not skip any blocks during validation.

## 6.4 Oracle Database Backup and Recovery User's Guide

Note the following changes with regard to the Oracle Database Backup and Recovery User's Guide for 11g release 2 (11.2), part number E10642.

### 6.4.1 Chapter 22: Tuning RMAN Performance

In the sub-section titled "Allocation of Input Disk Buffers" in the section titled "Read Phase" in the section titled "Basic Concepts of RMAN Performance Tuning", the first sentence after Figure 22-3 needs to be replaced with the following:

If a channel is backing up files stored in ASM, then the number of input disk buffers equals the number of physical disks in the ASM disk group only if the level of multiplexing is 1.

### 6.4.2 Chapter 24: Duplicating a Database

In the sub-section titled "Step 2: Choosing a Strategy for Naming Duplicate Files" of the section titled "Preparing to Duplicate a Database", the parameter name in the second bullet needs to be changed from `DB_FILE_CREATE_DEST` to `DB_CREATE_FILE_DEST`.

## 6.5 Oracle Database Data Warehousing Guide

Note the following changes with regard to the Oracle Database Data Warehousing Guide for 11g release 2 (11.2), part number E25554.

### 6.5.1 Chapter 9: Basic Materialized Views

In the sub-section titled "Restrictions on Fast Refresh on Materialized Views with Aggregates" in the section titled "Refresh Options" in the section titled "Creating Materialized Views", the following restriction must be added:

- The materialized view is not based on one or more remote tables.

### 6.5.2 Chapter 10: Advanced Materialized Views

In the sub-section titled "Querying Materialized Views with Virtual Private Database (VPD)" in the section titled "Security Issues with Materialized Views", the second paragraph needs to be replaced with the following:

Using materialized views with Virtual Private Database is similar. When you create a materialized view, there must not be any VPD policies in effect against the base relations of the materialized view for the owner of the materialized view. If any VPD policies exist, then you must use the `USING TRUSTED CONSTRAINTS` clause when creating the materialized view. The owner of the materialized view may establish a VPD policy on the new materialized view. Users who access the materialized view are subject to the VPD policy on the materialized view. However, they are not additionally subject to the VPD policies of the underlying base relations of the materialized view, because security processing of the underlying base relations is performed against the owner of the materialized view.

## 6.6 Oracle Database Net Services Reference

Note the following changes with regard to the Oracle Database Net Services Reference for 11g release 2 (11.2), part number E10835.

### 6.6.1 Chapter 5: Parameters for the sqlnet.ora File

Note the following changes with regard to Section 5.2 titled "sqlnet.ora Profile Parameters".

#### 6.6.1.1 SQLNET.EXPIRE\_TIME

In the sub-section titled "SQLNET.EXPIRE\_TIME", add the following point as a limitation:

- The use of `SQLNET.EXPIRE_TIME` with TCPS is unsupported.

#### 6.6.1.2 SSL\_VERSION

The entire sub-section titled "SSL\_VERSION" should be changed to read as follows:

Purpose

To limit allowable SSL or TLS versions used for connections.

Usage Notes

Clients and database servers must use a compatible version. This parameter should only be used when absolutely necessary for backward compatibility. The current default uses TLS version 1.2 which is the version required for multiple security compliance requirements.

If you set `SSL_VERSION` to `undetermined`, then by default it uses `3.0`.

Default

```
1.2
```

Values

Note:

The sqlnet.ora parameter `ADD_SSLV3_TO_DEFAULT` has no impact on this parameter.

```
undertermined | 3.0 | 1.0 | 1.1 | 1.2
```

If you want to specify one version or another version, then use "or". The following values are permitted:

```
1.0 or 3.0 | 1.2 or 3.0 | 1.1 or 1.0 | 1.2 or 1.0 | 1.2 or 1.1 | 1.1 or 1.0 or 3.0 | 1.2 or 1.0 or 3.0 | 1.2 or 1.1 or 1.0 | 1.2 or 1.1 or 3.0 | 1.2 or 1.1 or 1.0 or 3.0
```

Example

```
SSL_VERSION=1.2
```

The remaining version numbers correspond to the TLS versions, such as, TLSv1.0, TLSv1.1, and TLSv1.2.

### 6.6.2 Chapter 6: Local Naming Parameters in the tnsnames.ora File

Note the following changes with regard to Chapter 6 in the Oracle Database Net Services Reference.

#### 6.6.2.1 Section Title: Connection Data Section

In the sub-section titled "HS" in the section titled "Connection Data Section," the Example should be changed to read:

```
net_service_name=
  (DESCRIPTION=
    (ADDRESS=...)
    (ADDRESS=...)
    (CONNECT_DATA=
      (SID=sales6)
    (HS=ok)))
```

The `(HS=ok)` clause is a top level clause, independent and at the same level as the `ADDRESS` or `CONNECT_DATA` clause.

#### 6.6.2.2 Section Title: Security Section

In the sub-section titled "SECURITY" in the section titled "Security Section," the Usage Note should be changed to read "The parameters permitted under `SECURITY` are `SSL_SERVER_CERT_DN` and `AUTHENTICATION_SERVICE`."

#### 6.6.2.3 Section Title: Timeout Parameters

In the sub-section titled "CONNECT\_TIMEOUT" in the section titled "Timeout Parameters," all instances of `TCP_CONNECT_TIMEOUT` should be changed to `TCP.CONNECT_TIMEOUT`.

### 6.6.3 Chapter 8: Oracle Connection Manager Parameters (cman.ora)

In the sub-section titled "INBOUND\_CONNECT\_TIMEOUT" in the section titled "Oracle Connection Manager Parameters", the first bullet under Values must read as follows:

- `60 secs` is the default. Use value `0` to disable timeout.

## 6.7 Oracle Database Reference

Note the following changes with regard to the Oracle Database Reference guide for 11g release 2 (11.2), part number E40402.

### 6.7.1 Chapter 1: Initialization Parameters

Note the following changes with regard to the section titled "Initialization Parameter Descriptions".

#### 6.7.1.1 ASM\_DISKGROUPS

The `ASM_DISKGROUPS` parameter is dynamic. If you are using a server parameter file (SPFILE), then you do not have to manually alter the value of `ASM_DISKGROUPS` except in an Oracle Flex ASM configuration.

In an Oracle Flex ASM configuration, Oracle ASM automatically adds a disk group to the parameter when the disk group is successfully created or mounted. Oracle ASM also automatically removes a disk group from the parameter when the disk group is dropped. However, the SPFILE is not updated on a manual dismount.

#### 6.7.1.2 SYSDBA Not Needed for REDO\_TRANSPORT\_USER

The `REDO_TRANSPORT_USER` initialization parameter description says that users must have the `SYSDBA` or `SYSOPER` privilege to use the parameter. This is incorrect. Users must have the `SYSOPER` privilege to use this parameter.

## 6.8 Oracle Database Utilities

Note the following changes with regard to the Oracle Database Utilities guide for 11g release 2 (11.2), part number E22490.

### 6.8.1 Chapter 2: Data Pump Export

The following restriction is added to the `ACCESS_METHOD` parameter for Data Pump Export:

The `ACCESS_METHOD` parameter for Data Pump Export is not valid for transportable tablespace jobs.

The following restriction is added to the `TRANSPORT_TABLESPACES` parameter for Data Pump Export:

Transportable tablespace jobs do not support the `ACCESS_METHOD` parameter for Data Pump Export.

### 6.8.2 Chapter 3: Data Pump Import

The following restriction is added to the `ACCESS_METHOD` parameter for Data Pump Import:

The `ACCESS_METHOD` parameter for Data Pump Import is not valid for transportable tablespace jobs.

The following restriction is added to the `TRANSPORT_TABLESPACES` parameter for Data Pump Import:

Transportable tablespace jobs do not support the `ACCESS_METHOD` parameter for Data Pump Import.

## 6.9 Oracle Real Application Clusters Administration and Deployment Guide

Note the following changes with regard to the Oracle Real Application Clusters Administration and Deployment Guide for 11g release 2 (11.2), part number E41960.

### 6.9.1 Chapter 10: Adding and Deleting Oracle RAC from Nodes on Linux and UNIX Systems

In the section titled "Adding Oracle RAC to Nodes with Oracle Clusterware Installed," step 2 specifies the script name as `root.sh`. This is incorrect. The correct name for the script is `root.bat`.

### 6.9.2 Appendix A: Server Control Utility Reference

In the sections titled "srvctl start listener" and "srvctl stop listener", the following text is incorrect in the tables:

"If you do not specify this option, then the listener name defaults to `LISTENER`."

- The correct text for "srvctl start listener" should be:
	"If you do not specify this parameter, then all the known listeners are started."
- The correct text for "srvctl stop listener" should be:
	"If you do not specify this parameter, then all the known listeners are stopped."

## 6.10 Oracle Real Application Clusters Installation Guide

Note the following changes with regard to the Oracle Real Application Clusters Installation Guide for 11g release 2 (11.2), part number E41962.

### 6.10.1 Appendix C: Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases

In the sub-section titled "Converting Databases to Oracle RAC Using Oracle Enterprise Manager" in the section titled "Preparing to Convert with rconfig and Oracle Enterprise Manager," remove step 4 and replace step 3 with the following:

3\. On the Database home page, from the Availability menu, select Convert to Cluster Database.

## 6.11 Oracle Text Application Developer's Guide

Note the following changes with regard to Oracle Text Application Developer's Guide, 11g release 2 (11.2), part number E24435.

### 6.11.1 Chapter 11: Using XML Query Result Set Interface

The first paragraph in the section titled "Using the XML Query Result Set Interface" should be changed to read:

The `CTX_QUERY.RESULT_SET()` and `CTX_QUERY.RESULT_SET_CLOB_QUERY()` APIs enable you to obtain query results with a single query, rather than running multiple `CONTAINS()` queries to achieve the same result. The two APIs are identical except that one uses a `VARCHAR2` query parameter, and the other uses a `CLOB` query parameter to allow for longer queries.

## 6.12 Oracle Text Reference

Note the following changes with regard to [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm), 11g release 2 (11.2), part number E24436.

### 6.12.1 Chapter 8: CTX\_DDL Package

For the `ADD_STOPCLASS` procedure, English is the only language supported for stopclasses.

### 6.12.2 Chapter 10: CTX\_QUERY Package

This chapter should contain the following new section:

RESULT\_SET\_CLOB\_QUERY

This procedure executes an XML query and generates a result set based on a `CLOB` query parameter in XML.

The `RESULT_SET_CLOB_QUERY` procedure is identical to the `RESULT_SET` procedure except that the data type of its query parameter is `CLOB` instead of `VARCHAR2` to handle longer queries.

Syntax

```
CTX_QUERY.RESULT_SET_CLOB_QUERY (
   index_name            IN VARCHAR2,
   query                 IN CLOB,
   result_set_descriptor IN CLOB,
   result_set            IN OUT CLOB,
   part_name             IN VARCHAR2 DEFAULT 
);
```