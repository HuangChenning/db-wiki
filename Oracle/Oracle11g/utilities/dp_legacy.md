---
title: Data Pump Legacy Mode
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_legacy.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 4 Data Pump Legacy Mode

If you use original Export (exp) and Import (imp), then you may have scripts you have been using for many years. To ease the transition to the newer Data Pump Export and Import utilities, Data Pump provides a legacy mode which allows you to continue to use your existing scripts with Data Pump.

Data Pump enters legacy mode once it determines a parameter unique to original Export or Import is present, either on the command line or in a script. As Data Pump processes the parameter, the analogous Data Pump Export or Data Pump Import parameter is displayed. Oracle strongly recommends that you view the new syntax and make script changes as time permits.

Note:

Data Pump Export and Import only handle dump files and log files in the Data Pump format. They never create or read dump files compatible with original Export or Import. If you have a dump file created with original Export, then you must use original Import to import the data into the database.

This chapter contains the following sections:

## Parameter Mappings

This section describes how original Export and Import parameters map to the Data Pump Export and Import parameters that supply similar functionality.

### Using Original Export Parameters with Data Pump

Data Pump Export accepts original Export parameters when they map to a corresponding Data Pump parameter. Table 4-1 describes how Data Pump Export interprets original Export parameters. Parameters that have the same name and functionality in both original Export and Data Pump Export are not included in this table.

Table 4-1 How Data Pump Export Handles Original Export Parameters

| Original Export Parameter | Action Taken by Data Pump Export Parameter |
| --- | --- |
| ``` BUFFER ``` | This parameter is ignored. |
| ``` COMPRESS ``` | This parameter is ignored. In original Export, the `COMPRESS` parameter affected how the initial extent was managed. Setting `COMPRESS=n` caused original Export to use current storage parameters for the initial and next extent.  The Data Pump Export `COMPRESSION` parameter is used to specify how data is compressed in the dump file, and is not related to the original Export `COMPRESS` parameter. |
| ``` CONSISTENT ``` | Data Pump Export determines the current time and uses `FLASHBACK_TIME`. |
| `CONSTRAINTS` | If original Export used `CONSTRAINTS=n`, then Data Pump Export uses `EXCLUDE=CONSTRAINTS`.  The default behavior is to include constraints as part of the export. |
| ``` DIRECT ``` | This parameter is ignored. Data Pump Export automatically chooses the best export method. |
| ``` FEEDBACK ``` | The Data Pump Export `STATUS=30` command is used. Note that this is not a direct mapping because the `STATUS` command returns the status of the export job, as well as the rows being processed.  In original Export, feedback was given after a certain number of rows, as specified with the `FEEDBACK` command. In Data Pump Export, the status is given every so many seconds, as specified by `STATUS`. |
| ``` FILE ``` | Data Pump Export attempts to determine the path that was specified or defaulted to for the `FILE` parameter, and also to determine whether a directory object exists to which the schema has read and write access.  See "Management of File Locations in Data Pump Legacy Mode" for more information about how Data Pump handles the original Export `FILE` parameter. |
| ``` GRANTS ``` | If original Export used `GRANTS=n`, then Data Pump Export uses `EXCLUDE=GRANT`.  If original Export used `GRANTS=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Export default behavior. |
| ``` INDEXES ``` | If original Export used `INDEXES=n`, then Data Pump Export uses the `EXCLUDE=INDEX` parameter.  If original Export used `INDEXES=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Export default behavior. |
| `LOG` | Data Pump Export attempts to determine the path that was specified or defaulted to for the `LOG` parameter, and also to determine whether a directory object exists to which the schema has read and write access.  See "Management of File Locations in Data Pump Legacy Mode" for more information about how Data Pump handles the original Export `LOG` parameter.  The contents of the log file will be those of a Data Pump Export operation. See "Log Files" for information about log file location and content. |
| ``` OBJECT_CONSISTENT ``` | This parameter is ignored because Data Pump Export processing ensures that each object is in a consistent state when being exported. |
| ``` OWNER ``` | The Data Pump `SCHEMAS` parameter is used. |
| ``` RECORDLENGTH ``` | This parameter is ignored because Data Pump Export automatically takes care of buffer sizing. |
| ``` RESUMABLE ``` | This parameter is ignored because Data Pump Export automatically provides this functionality to users who have been granted the `EXP_FULL_DATABASE` role. |
| ``` RESUMABLE_NAME ``` | This parameter is ignored because Data Pump Export automatically provides this functionality to users who have been granted the `EXP_FULL_DATABASE` role. |
| ``` RESUMABLE_TIMEOUT ``` | This parameter is ignored because Data Pump Export automatically provides this functionality to users who have been granted the `EXP_FULL_DATABASE` role. |
| ``` ROWS ``` | If original Export used `ROWS=y`, then Data Pump Export uses the `CONTENT=ALL` parameter.  If original Export used `ROWS=n`, then Data Pump Export uses the `CONTENT=METADATA_ONLY` parameter. |
| ``` STATISTICS ``` | This parameter is ignored because statistics are always saved for tables as part of a Data Pump export operation. |
| ``` TABLESPACES ``` | If original Export also specified `TRANSPORT_TABLESPACE=n`, then Data Pump Export ignores the `TABLESPACES` parameter.  If original Export also specified `TRANSPORT_TABLESPACE=y`, then Data Pump Export takes the names listed for the `TABLESPACES` parameter and uses them on the Data Pump Export `TRANSPORT_TABLESPACES` parameter. |
| `TRANSPORT_TABLESPACE` | If original Export used `TRANSPORT_TABLESPACE=n` (the default), then Data Pump Export uses the `TABLESPACES` parameter.  If original Export used `TRANSPORT_TABLESPACE=y`, then Data Pump Export uses the `TRANSPORT_TABLESPACES` parameter and only the metadata is exported. |
| ``` TRIGGERS ``` | If original Export used `TRIGGERS=n`, then Data Pump Export uses the `EXCLUDE=TRIGGER` parameter.  If original Export used `TRIGGERS=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Export default behavior. |
| ``` TTS_FULL_CHECK ``` | If original Export used `TTS_FULL_CHECK=y`, then Data Pump Export uses the `TRANSPORT_FULL_CHECK` parameter.  If original Export used `TTS_FULL_CHECK=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Export default behavior. |
| ``` VOLSIZE ``` | When the original Export `VOLSIZE` parameter is used, it means the location specified for the dump file is a tape device. The Data Pump Export dump file format does not support tape devices. Therefore, this operation terminates with an error. |

### Using Original Import Parameters with Data Pump

Data Pump Import accepts original Import parameters when they map to a corresponding Data Pump parameter. Table 4-2 describes how Data Pump Import interprets original Import parameters. Parameters that have the same name and functionality in both original Import and Data Pump Import are not included in this table.

Table 4-2 How Data Pump Import Handles Original Import Parameters

| Original Import Parameter | Action Taken by Data Pump Import Parameter |
| --- | --- |
| ``` BUFFER ``` | This parameter is ignored. |
| ``` CHARSET ``` | This parameter was desupported several releases ago and should no longer be used. It will cause the Data Pump Import operation to abort. |
| ``` COMMIT ``` | This parameter is ignored. Data Pump Import automatically performs a commit after each table is processed. |
| ``` COMPILE ``` | This parameter is ignored. Data Pump Import compiles procedures after they are created. A recompile can be executed if necessary for dependency reasons. |
| ``` CONSTRAINTS ``` | If original Import used `CONSTRAINTS=n`, then Data Pump Import uses the `EXCLUDE=CONSTRAINT` parameter.  If original Import used `CONSTRAINTS=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Import default behavior. |
| ``` DATAFILES ``` | The Data Pump Import `TRANSPORT_DATAFILES` parameter is used. |
| ``` DESTROY ``` | If original Import used `DESTROY=y`, then Data Pump Import uses the `REUSE_DATAFILES` `=y` parameter.  If original Import used `DESTROY=n`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Import default behavior. |
| ``` FEEDBACK ``` | The Data Pump Import `STATUS=30` command is used. Note that this is not a direct mapping because the `STATUS` command returns the status of the import job, as well as the rows being processed.  In original Import, feedback was given after a certain number of rows, as specified with the `FEEDBACK` command. In Data Pump Import, the status is given every so many seconds, as specified by `STATUS.` |
| `FILE` | Data Pump Import attempts to determine the path that was specified or defaulted to for the `FILE` parameter, and also to determine whether a directory object exists to which the schema has read and write access.  See "Management of File Locations in Data Pump Legacy Mode" for more information about how Data Pump handles the original Import `FILE` parameter. |
| ``` FILESIZE ``` | This parameter is ignored because the information is already contained in the Data Pump dump file set. |
| `FROMUSER` | The Data Pump Import `SCHEMAS` parameter is used. If `FROMUSER` was used without `TOUSER` also being used, then import schemas that have the `IMP_FULL_DATABASE` role cause Data Pump Import to attempt to create the schema and then import that schema's objects. Import schemas that do not have the `IMP_FULL_DATABASE` role can only import their own schema from the dump file set. |
| ``` GRANTS ``` | If original Import used `GRANTS=n`, then Data Pump Import uses the `EXCLUDE=OBJECT_GRANT` parameter.  If original Import used `GRANTS=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Import default behavior. |
| ``` IGNORE ``` | If original Import used `IGNORE=y`, then Data Pump Import uses the `TABLE_EXISTS_ACTION=APPEND` parameter. This causes the processing of table data to continue.  If original Import used `IGNORE=n`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Import default behavior. |
| ``` INDEXES ``` | If original Import used `INDEXES=n`, then Data Pump Import uses the `EXCLUDE=INDEX` parameter.  If original Import used `INDEXES=y`, then the parameter is ignored and does not need to be remapped because that is the Data Pump Import default behavior. |
| `INDEXFILE` | The Data Pump Import `SQLFILE={directory-object:}filename` and `INCLUDE=INDEX` parameters are used.  The same method and attempts made when looking for a directory object described for the `FILE` parameter also take place for the `INDEXFILE` parameter.  If no directory object was specified on the original Import, then Data Pump Import uses the directory object specified with the `DIRECTORY` parameter. |
| `LOG` | Data Pump Import attempts to determine the path that was specified or defaulted to for the `LOG` parameter, and also to determine whether a directory object exists to which the schema has read and write access.  See "Management of File Locations in Data Pump Legacy Mode" for more information about how Data Pump handles the original Import `LOG` parameter.  The contents of the log file will be those of a Data Pump Import operation. See "Log Files" for information about log file location and content. |
| ``` RECORDLENGTH ``` | This parameter is ignored because Data Pump handles issues about record length internally. |
| ``` RESUMABLE ``` | This parameter is ignored because this functionality is automatically provided for users who have been granted the `IMP_FULL_DATABASE` role. |
| ``` RESUMABLE_NAME ``` | This parameter is ignored because this functionality is automatically provided for users who have been granted the `IMP_FULL_DATABASE` role. |
| ``` RESUMABLE_TIMEOUT ``` | This parameter is ignored because this functionality is automatically provided for users who have been granted the `IMP_FULL_DATABASE` role. |
| ``` ROWS=N ``` | If original Import used `ROWS=n`, then Data Pump Import uses the `CONTENT=METADATA_ONLY` parameter.  If original Import used `ROWS=y`, then Data Pump Import uses the `CONTENT=ALL` parameter. |
| ``` SHOW ``` | If `SHOW=y` is specified, then the Data Pump Import `SQLFILE=[directory_object:]file_name` parameter is used to write the DDL for the import operation to a file. Only the DDL (not the entire contents of the dump file) is written to the specified file. (Note that the output is not shown on the screen as it was in original Import.)  The name of the file will be the file name specified on the `DUMPFILE` parameter (or on the original Import `FILE` parameter, which is remapped to `DUMPFILE`). If multiple dump file names are listed, then the first file name in the list is used. The file will be located in the directory object location specified on the `DIRECTORY` parameter or the directory object included on the `DUMPFILE` parameter. (Directory objects specified on the `DUMPFILE` parameter take precedence.) |
| ``` STATISTICS ``` | This parameter is ignored because statistics are always saved for tables as part of a Data Pump Import operation. |
| ``` STREAMS_CONFIGURATION ``` | This parameter is ignored because Data Pump Import automatically determines it; it does not need to be specified. |
| ``` STREAMS_INSTANTIATION ``` | This parameter is ignored because Data Pump Import automatically determines it; it does not need to be specified |
| `TABLESPACES` | If original Import also specified `TRANSPORT_TABLESPACE=n` (the default), then Data Pump Import ignores the `TABLESPACES` parameter.  If original Import also specified `TRANSPORT_TABLESPACE=y`, then Data Pump Import takes the names supplied for this `TABLESPACES` parameter and applies them to the Data Pump Import `TRANSPORT_TABLESPACES` parameter. |
| ``` TOID_NOVALIDATE ``` | This parameter is ignored. OIDs are no longer used for type validation. |
| `TOUSER` | The Data Pump Import `REMAP_SCHEMA` parameter is used. There may be more objects imported than with original Import. Also, Data Pump Import may create the target schema if it does not already exist.  The `FROMUSER` parameter must also have been specified in original Import or the operation will fail. |
| `TRANSPORT_TABLESPACE` | The `TRANSPORT_TABLESPACE` parameter is ignored, but if you also specified the `DATAFILES` parameter, then the import job continues to load the metadata. If the `DATAFILES` parameter is not specified, then an `ORA-39002:invalid operation` error message is returned. |
| ``` TTS_OWNERS ``` | This parameter is ignored because this information is automatically stored in the Data Pump dump file set. |
| ``` VOLSIZE ``` | When the original Import `VOLSIZE` parameter is used, it means the location specified for the dump file is a tape device. The Data Pump Import dump file format does not support tape devices. Therefore, this operation terminates with an error. |

## Management of File Locations in Data Pump Legacy Mode

Original Export and Import and Data Pump Export and Import differ on where dump files and log files can be written to and read from because the original version is client-based and Data Pump is server-based.

Original Export and Import use the `FILE` and `LOG` parameters to specify dump file and log file names, respectively. These file names always refer to files local to the client system and they may also contain a path specification.

Data Pump Export and Import use the `DUMPFILE` and `LOGFILE` parameters to specify dump file and log file names, respectively. These file names always refer to files local to the server system and cannot contain any path information. Instead, a directory object is used to indirectly specify path information. The path value defined by the directory object must be accessible to the server. The directory object is specified for a Data Pump job through the `DIRECTORY` parameter. It is also possible to prepend a directory object to the file names passed to the `DUMPFILE` and `LOGFILE` parameters. For privileged users, Data Pump supports the use of a default directory object if one is not specified on the command line. This default directory object, `DATA_PUMP_DIR`, is set up at installation time.

If Data Pump legacy mode is enabled and the original Export `FILE=` `filespec` parameter and/or `LOG=` `filespec` parameter are present on the command line, then the following rules of precedence are used to determine a file's location:

Note:

If the `FILE` parameter and `LOG` parameter are both present on the command line, then the rules of precedence are applied separately to each parameter.

Also, when a mix of original Export/Import and Data Pump Export/Import parameters are used, separate rules apply to them. For example, suppose you have the following command:

```
expdp system FILE=/user/disk/foo.dmp LOGFILE=foo.log DIRECTORY=dpump_dir
```

The Data Pump legacy mode file management rules, as explained in this section, would apply to the `FILE` parameter. The normal (that is, non-legacy mode) Data Pump file management rules, as described in ["Default Locations for Dump, Log, and SQL Files"](dp_overview.md), would apply to the `LOGFILE` parameter.

1. If a path location is specified as part of the file specification, then Data Pump attempts to look for a directory object accessible to the schema executing the export job whose path location matches the path location of the file specification. If such a directory object cannot be found, then an error is returned. For example, assume that a server-based directory object named `USER_DUMP_FILES` has been defined with a path value of `'/disk1/user1/dumpfiles/'` and that read and write access to this directory object has been granted to the `hr` schema. The following command causes Data Pump to look for a server-based directory object whose path value contains `'/disk1/user1/dumpfiles/'` and to which the `hr` schema has been granted read and write access:
	```
	expdp hr FILE=/disk1/user1/dumpfiles/hrdata.dmp
	```
	In this case, Data Pump uses the directory object `USER_DUMP_FILES`. The path value, in this example `'/disk1/user1/dumpfiles/'`, must refer to a path on the server system that is accessible to the Oracle Database.
	If a path location is specified as part of the file specification, then any directory object provided using the `DIRECTORY` parameter is ignored. For example, if the following command is issued, then Data Pump does not use the `DPUMP_DIR` directory object for the file parameter, but instead looks for a server-based directory object whose path value contains `'/disk1/user1/dumpfiles/'` and to which the `hr` schema has been granted read and write access:
	```
	expdp hr FILE=/disk1/user1/dumpfiles/hrdata.dmp DIRECTORY=dpump_dir
	```
2. If no path location is specified as part of the file specification, then the directory object named by the `DIRECTORY` parameter is used. For example, if the following command is issued, then Data Pump applies the path location defined for the `DPUMP_DIR` directory object to the `hrdata.dmp` file:
	```
	expdp hr FILE=hrdata.dmp DIRECTORY=dpump_dir
	```
3. If no path location is specified as part of the file specification and no directory object is named by the `DIRECTORY` parameter, then Data Pump does the following, in the order shown:
	1. Data Pump looks for the existence of a directory object of the form `DATA_PUMP_DIR_` `schema_name`, where `schema_name` is the schema that is executing the Data Pump job. For example, the following command would cause Data Pump to look for the existence of a server-based directory object named `DATA_PUMP_DIR_HR`:
		```
		expdp hr FILE=hrdata.dmp
		```
		The `hr` schema also must have been granted read and write access to this directory object. If such a directory object does not exist, then the process moves to step b.
		2. Data Pump looks for the existence of the client-based environment variable `DATA_PUMP_DIR`. For instance, assume that a server-based directory object named `DUMP_FILES1` has been defined and the `hr` schema has been granted read and write access to it. Then on the client system, the environment variable `DATA_PUMP_DIR` can be set to point to `DUMP_FILES1` as follows:
		```
		setenv DATA_PUMP_DIR DUMP_FILES1
		expdp hr FILE=hrdata.dmp
		```
		Data Pump then uses the served-based directory object `DUMP_FILES1` for the `hrdata.dmp` file.
		If a client-based environment variable `DATA_PUMP_DIR` does not exist, then the process moves to step c.
		3. If the schema that is executing the Data Pump job has DBA privileges, then the default Data Pump directory object, `DATA_PUMP_DIR`, is used. This default directory object is established at installation time. For example, the following command causes Data Pump to attempt to use the default `DATA_PUMP_DIR` directory object, assuming that system has DBA privileges:
		```
		expdp system FILE=hrdata.dmp
		```

See Also:

["Default Locations for Dump, Log, and SQL Files"](dp_overview.md) for information about Data Pump file management rules of precedence under normal Data Pump conditions (that is, non-legacy mode)

## Adjusting Existing Scripts for Data Pump Log Files and Errors

Data Pump legacy mode requires that you review and update your existing scripts written for original Export and Import because of differences in file format and error reporting.

### Log Files

Data Pump Export and Import do not generate log files in the same format as those created by original Export and Import. Any scripts you have that parse the output of original Export and Import must be updated to handle the log file format used by Data Pump Export and Import. For example, the message `Successfully Terminated` does not appear in Data Pump log files.

### Error Cases

Data Pump Export and Import may not produce the same errors as those generated by original Export and Import. For example, if a parameter that is ignored by Data Pump Export would have had an out-of-range value in original Export, then an informational message is written to the log file stating that the parameter is being ignored. No value checking is performed, therefore no error message is generated.

### Exit Status

Data Pump Export and Import have enhanced exit status values to allow scripts to better determine the success of failure of export and import jobs. Any scripts that look at the exit status should be reviewed and updated, if necessary.