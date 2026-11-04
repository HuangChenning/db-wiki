---
title: "What's New in Database Utilities?"
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/whatsnew.htm
tags:
  - oracle
  - 11g
  - utilities
---

This section describes new features of the Oracle Database 11g utilities, and provides pointers to additional information. For information about features that were introduced in earlier releases of Oracle Database, refer to the documentation for those releases.

## Oracle Database 11g Release 2 (11.2.0.3) New Features in Oracle Database Utilities

This section lists the major new and changed features in Oracle Database 11g release 2 (11.2.0.3).

- Oracle LogMiner now supports `XMLType` data stored as binary XML.
- Oracle LogMiner now supports `XMLType` data stored in object-relational format.

Support for both of these storage formats is available only on Oracle Database 11g Release 2 (11.2.0.3) or higher with a redo compatibility setting of 11.2.0.3 or higher. See ["Supported Datatypes, Storage Attributes, and Database and Redo Log File Versions"](logminer.md) for more information about Oracle LogMiner supported data types.

## Oracle Database 11g Release 2 (11.2.0.2) New Features in Oracle Database Utilities

This section lists the major new and changed features in Oracle Database 11g release 2 (11.2.0.2).

- The Data Pump Import `TRANSFORM` parameter has a new transform named `SEGMENT_CREATION` which allows you to alter the segment creation attributes for the table(s) being loaded. See the Data Pump Import ["TRANSFORM"](dp_import.md) parameter for more information.
- The default size of the first extent of any new segment for a partitioned table is now 8 MB instead of 64 KB. This helps improve performance of inserts and queries on partitioned tables. Although partitioned tables will start with a larger initial size, once sufficient data is inserted the space consumption will be the same as in previous releases. You can override the default by setting the INITIAL size in the storage clause for the table. This new default only applies to table partitions and LOB partitions.

## Oracle Database 11g Release 2 (11.2.0.1) New Features in Oracle Database Utilities

This section lists the major new and changed features in Oracle Database 11g release 2 (11.2.0.1).

Data Pump Export and Data Pump Import

- Data Pump provides a legacy mode in which you can use original Export and Import parameters when performing Data Pump Export and Import operations. See [Chapter 4, "Data Pump Legacy Mode"](dp_legacy.md) for more information.
- The restriction that in Tables mode all tables had to reside in the same schema has been removed. You can now specify tables in multiple schemas.
- The restriction that only one object (table or partition) could be specified if a wildcard character, %, was used as part of the object name has been removed. You can now specify multiple tables and partitions and use the wildcard character, %, in all of them. But if you are specifying partitions, they must be from different tables.
- Data Pump worker processes can be distributed across Oracle Real Application Clusters (Oracle RAC) instances, a subset of Oracle RAC instances, or confined to the instance where the Data Pump job is started. It is also now possible to start Data Pump jobs and run them on different Oracle RAC instances simultaneously. See the Export [CLUSTER](dp_export.md) parameter and the Import [CLUSTER](dp_import.md) parameter.
- Specific editions can be exported and imported. See the Export [SOURCE\_EDITION](dp_export.md) parameter and the Import [TARGET\_EDITION](dp_import.md) parameter.
- When performing an import operation, you can use the new `DISABLE_APPEND_HINT` value on the `DATA_OPTIONS` parameter to specify that you do not want the import operation to use the `APPEND` hint while loading the data object. See the Import [DATA\_OPTIONS](dp_import.md) parameter.

External Tables

- The `ORACLE_LOADER` access driver has been enhanced to allow the specification of a user-supplied preprocessor program that reads data from a file that is not in a format supported by the driver. See the [PREPROCESSOR](et_params.md) parameter.

Original Export

- In Oracle Database 11g release 2 (11.2), the `DEFERRED_SEGMENT_CREATION` parameter is set to `TRUE` by default. This means that any tables you create do not have any segments until the first row of data is inserted into the table. Original Export ignores tables without segments. Therefore, if you create any new tables and do not insert any data before performing an export, those tables are not exported. (Note that Data Pump Export does not have this limitation because it does not ignore tables without segments.)

Other Utilities

- A new PL/SQL package, `DBMS_METADATA_DIFF`, allows you to compare the metadata for two SQL objects (tables, indexes, and so on) and get the following information in return:
	- An XML document showing the metadata for both objects, including the ways they are the same and the ways they are different
		- A set of `ALTER` statements to make one object like the other
	See Also:
	- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_metadiff.htm#ARPLS354) for a description of the `DBMS_METADATA_DIFF` API
	- [Chapter 20, "Using the Metadata APIs"](metadata_api.md)

## New Features in Oracle Database Utilities 11g Release 1

This section lists the major new features that have been added for Oracle Database 11g release 1 (11.1).

Data Pump Export and Data Pump Import

For the Data Pump Export and Data Pump Import products, new features have been added that allow you to do the following:

- Compress both data and metadata, only data, only metadata, or no data during an export. See the Export [COMPRESSION](dp_export.md) parameter.
- Specify additional encryption options in the following areas:
	- You can choose to encrypt both data and metadata, only data, only metadata, no data, or only encrypted columns during an export. See the Export [ENCRYPTION](dp_export.md) parameter.
		- You can specify a specific encryption algorithm to use during an export. See the Export [ENCRYPTION\_ALGORITHM](dp_export.md) parameter.
		- You can specify the type of security to use for performing encryption and decryption during an export. For example, perhaps the dump file set will be imported into a different or remote database and it must remain secure in transit. Or perhaps the dump file set will be imported on-site using the Oracle encryption wallet but it may also need to be imported offsite where the wallet is not available. See the Export [ENCRYPTION\_MODE](dp_export.md) parameter.
- Perform table mode exports and imports using the transportable method. For information on using this feature during export, see the Export [TRANSPORTABLE](dp_export.md) parameter. For information on using this feature during import, see the Import [TRANSPORTABLE](dp_import.md) parameter.
- Specify how partitioned tables should be handled during import operations. See the Import [PARTITION\_OPTIONS](dp_import.md) parameter for a description of this parameter.
- Overwrite existing dump files during an export operation. See the Export [REUSE\_DUMPFILES](dp_export.md) parameter.
- Rename tables during an import operation. See the Import [REMAP\_TABLE](dp_import.md) parameter.
- Specify that a data load should proceed even if non-deferred constraint violations are encountered. This is valid only for import operations that use the external tables access method. See the Import [DATA\_OPTIONS](dp_import.md) parameter.
- Specify that XMLType columns are to be exported in uncompressed CLOB format regardless of the XMLType storage format that was defined for them. See the Export [DATA\_OPTIONS](dp_export.md) parameter.
- During an export, specify a remap function that takes as a source the original value of the designated column and returns a remapped value that will replace the original value in the dump file. See the Export [REMAP\_DATA](dp_export.md) parameter.
- During an import, remap data as it is being loaded into a new database. See the Import [REMAP\_DATA](dp_import.md) parameter.
- Automatic restart of workers on the same instance.

Additionally, Data Pump now performs a one-time automatic restart of workers (on the same instance) that have stopped due to certain errors. For example, if someone manually stops a process, the worker is automatically restarted one time, on the same instance. If the process stops a second time, it must be manually restarted.

External Tables

For the External Tables functionality, the following new features have been added to the `ORACLE_DATAPUMP` access driver:

- Ability to compress data before it is written to the dump file set. See the external tables [COMPRESSION](et_dp_driver.md) parameter.
- Ability to encrypt data before it is written to the dump file set. See the external tables [ENCRYPTION](et_dp_driver.md) parameter.

LogMiner Utility

LogMiner now provides the following additional support:

- The LogMiner utility now supports `XMLType` data when it is stored in `CLOB` format.

See ["Supported Datatypes and Table Storage Attributes"](logminer.md).

Automatic Diagnostic Repository Command Interpreter (ADRCI)

The Automatic Diagnostic Repository Command Interpreter (ADRCI) provides a way for you to work with the diagnostic data contained in the Automatic Diagnostic Repository (ADR). The ADR is a file-based repository for database diagnostic data, such as traces, dumps, the alert log, health monitor reports, and more. It has a unified directory structure across multiple instances and multiple products.

See [Chapter 16, "ADRCI: ADR Command Interpreter"](adrci.md) for more information.