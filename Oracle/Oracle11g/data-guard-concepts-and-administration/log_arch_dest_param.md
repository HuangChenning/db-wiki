---
title: LOG_ARCHIVE_DEST_n Parameter Attributes
book: Data Guard Concepts and Administration
doc_id: E41134-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_arch_dest_param.htm
tags:
  - oracle
  - 11g
  - data-guard-concepts-and-administration
---

## 15 LOG\_ARCHIVE\_DEST\_n Parameter Attributes

This chapter provides reference information for the attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter, where `n` is an integer between 1 and 31. The following list shows the attributes for the parameter:

- AFFIRM and NOAFFIRM
- ALTERNATE (not supported for `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31`)
- COMPRESSION
- DB\_UNIQUE\_NAME
- DELAY
- LOCATION and SERVICE (`LOCATION` is not supported for `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31)`
- MANDATORY (not supported for `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31`)
- MAX\_CONNECTIONS
- MAX\_FAILURE
- NET\_TIMEOUT
- NOREGISTER
- REOPEN
- SYNC and ASYNC (`SYNC` is not supported for `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31)`
- TEMPLATE
- VALID\_FOR

Usage Notes

- Each database in a Data Guard configuration will typically have one destination with the `LOCATION` attribute for the archival of the online and standby redo logs and one destination with the `REMOTE` attribute for every other database in the configuration.
- If configured, each `LOG_ARCHIVE_DEST_1` through `LOG_ARCHIVE_DEST_10` destination must contain either a `LOCATION` or `SERVICE` attribute to specify a local disk directory or a remotely accessed database, respectively. Each `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` destination must contain a SERVICE attribute.
	All other attributes are optional.
- `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` cannot be specified as an `ALTERNATE` redo transport location.
- `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` can only be used when the `COMPATIBLE` initialization parameter is set to 11.2.0.0 or later.

Note:

Several attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter have been deprecated. These attributes are supported for backward compatibility only and are documented in the [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams125.htm#REFRN10086).

See Also:

[Chapter 6](log_transport.md) for more information about defining `LOG_ARCHIVE_DEST_` `n` destinations and setting up redo transport services

## AFFIRM and NOAFFIRM

Controls whether a redo transport destination acknowledges received redo data before or after writing it to the standby redo log:

- `AFFIRM` —specifies that a redo transport destination acknowledges received redo data after writing it to the standby redo log.
- `NOAFFIRM` —specifies that a redo transport destination acknowledges received redo data before writing it to the standby redo log.

| Category | AFFIRM | NOAFFIRM |
| --- | --- | --- |
| Data type | Keyword | Keyword |
| Valid values | Not applicable | Not applicable |
| Default Value | Not applicable | Not applicable |
| Requires attributes | `SERVICE` | `SERVICE` |
| Conflicts with attributes | `NOAFFIRM` | `AFFIRM` |
| Corresponds to | `AFFIRM` column of the `V$ARCHIVE_DEST` view | `AFFIRM` column of the `V$ARCHIVE_DEST` view |

Usage Notes

- If neither the `AFFIRM` nor the `NOAFFIRM` attribute is specified, the default is `AFFIRM` when the `SYNC` attribute is specified and `NOAFFIRM` when the `ASYNC` attribute is specified.
- Specification of the `AFFIRM` attribute without the `SYNC` attribute is deprecated and will not be supported in future releases.

See also:

SYNC and ASYNC attributes

Examples

The following example shows the `AFFIRM` attribute for a remote destination.

```
LOG_ARCHIVE_DEST_3='SERVICE=stby1 SYNC AFFIRM'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## ALTERNATE

Specifies an alternate archiving destination to be used when the original destination fails.

| Category | ALTERNATE=LOG\_ARCHIVE\_DEST\_ `n` |
| --- | --- |
| Data Type | String |
| Valid Value | A `LOG_ARCHIVE_DEST_` `n` destination, where `n` is a value from 1 through 10. |
| Default Value | None. If an alternate destination is not specified, then redo transport services do not automatically change to another destination. |
| Requires attributes | Not applicable |
| Conflicts with attributes | None <sup>Foot 1</sup> |
| Corresponds to | `ALTERNATE` and `STATUS` columns of the `V$ARCHIVE_DEST` view |

<sup>Footnote 1</sup> If the `REOPEN` attribute is specified with a nonzero value, the `ALTERNATE` attribute is ignored. If the `MAX_FAILURE` attribute is also specified with a nonzero value, and the failure count exceeds the specified failure threshold, the `ALTERNATE` destination is enabled. Therefore, the `ALTERNATE` attribute does not conflict with a nonzero `REOPEN` attribute value.

Usage Notes

- `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` cannot be specified as an alternate redo transport location.
- The `ALTERNATE` attribute is optional. If an alternate destination is not specified, then redo transport services do not automatically change to another destination if the original destination fails.
- You can specify only one alternate destination for each `LOG_ARCHIVE_DEST_` `n` parameter, but several enabled destinations can share the same alternate destination.
- Ideally, an alternate destination should specify either:
	- A different disk location on the same local standby database system (shown in Example 15-1)
		- A different network route to the same standby database system (shown in Example 15-2)
		- A remote standby database system that closely mirrors that of the enabled destination
- If no enabled destinations reference an alternate destination, the alternate destination is implied to be deferred, because there is no automatic method of enabling the alternate destination. However, you can enable (or defer) alternate destinations at runtime using `ALTER SYSTEM`.
- Any destination can be designated as an alternate destination, given the following restrictions:
	- At least one local mandatory destination is enabled.
		- The number of enabled destinations must meet the defined `LOG_ARCHIVE_MIN_SUCCEED_DEST` parameter value.
		- A destination cannot be its own alternate.
- Increasing the number of enabled destinations decreases the number of available alternate archiving destinations.
- When a destination fails, its alternate destination is enabled on the next archival operation. There is no support for enabling the alternate destination in the middle of the archival operation because that would require rereading already processed blocks. This is identical to the `REOPEN` attribute behavior.
- If the `REOPEN` attribute is specified with a nonzero value, the `ALTERNATE` attribute is ignored unless the `MAX_FAILURE` attribute has a nonzero value. If the `MAX_FAILURE` and `REOPEN` attributes have nonzero values and the failure count exceeds the specified failure threshold, the `ALTERNATE` destination is enabled. Therefore, the `ALTERNATE` attribute does not conflict with a nonzero `REOPEN` attribute value.

Examples

In the sample initialization parameter file in Example 15-1, `LOG_ARCHIVE_DEST_1` automatically fails over to the alternate destination `LOG_ARCHIVE_DEST_2` on the next archival operation if an error occurs or the device becomes full.

Example 15-1 Automatically Failing Over to an Alternate Destination

```
LOG_ARCHIVE_DEST_1='LOCATION=/disk1 MANDATORY MAX_FAILURE=1 
 ALTERNATE=LOG_ARCHIVE_DEST_2'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_2='LOCATION=/disk2 MANDATORY'
LOG_ARCHIVE_DEST_STATE_2=ALTERNATE
```

In both this example and in the following example, the `MAX_FAILURE` attribute must be specified or the destination will not fail over to the alternate destination when a problem is encountered. There is no default value for `MAX_FAILURE`; you must supply a value.

Example 15-2 Defining an Alternate Oracle Net Service Name to the Same Standby Database

This example shows how to define an alternate Oracle Net service name to the same standby database.

```
LOG_ARCHIVE_DEST_1='LOCATION=/disk1 MANDATORY MAX_FAILURE=1'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_2='SERVICE=stby1_path1 ALTERNATE=LOG_ARCHIVE_DEST_3'
LOG_ARCHIVE_DEST_STATE_2=ENABLE
LOG_ARCHIVE_DEST_3='SERVICE=stby1_path2'
LOG_ARCHIVE_DEST_STATE_3=ALTERNATE
```

## COMPRESSION

The `COMPRESSION` attribute is used to specify whether redo data is compressed before transmission to a redo transport destination.

Note:

Redo transport compression is a feature of the Oracle Advanced Compression option. You must purchase a license for this option before using the redo transport compression feature.

| Category | COMPRESSION=ENABLE or DISABLE |
| --- | --- |
| Data Type | Boolean |
| Valid values | `ENABLE` or `DISABLE` |
| Default value | `DISABLE` |
| Requires attributes | None |
| Conflicts with attributes | None |
| Corresponds to | `COMPRESSION` column of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `COMPRESSION` attribute is optional. If it is not specified, the default compression behavior is `DISABLE`.

Example

The following example shows the `COMPRESSION` attribute with the `LOG_ARCHIVE_DEST_` `n` parameter.

```
LOG_ARCHIVE_DEST_3='SERVICE=denver SYNC COMPRESSION=ENABLE'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## DB\_UNIQUE\_NAME

Specifies a unique name for the database at this destination.

| Category | DB\_UNIQUE\_NAME=name |
| --- | --- |
| Data Type | String |
| Valid values | The name must match the value that was defined for this database with the `DB_UNIQUE_NAME` parameter. |
| Default value | None |
| Requires attributes | None |
| Conflicts with attributes | None |
| Corresponds to | `DB_UNIQUE_NAME` column of the `V$ARCHIVE_DEST` view |

Usage Notes

- This attribute is optional if:
	- The `LOG_ARCHIVE_CONFIG=DG_CONFIG` initialization parameter is not specified.
		- This is a local destination (specified with the `LOCATION` attribute).
- This attributes is required if the `LOG_ARCHIVE_CONFIG=DG_CONFIG` initialization parameter is specified and if this is a remote destination (specified with the `SERVICE` attribute).
- Use the `DB_UNIQUE_NAME` attribute to clearly identify the relationship between a primary and standby databases. This attribute is particularly helpful if there are multiple standby databases in the Data Guard configuration.
- The name specified by the `DB_UNIQUE_NAME` must match one of the `DB_UNIQUE_NAME` values in the `DG_CONFIG` list. Redo transport services validate that the `DB_UNIQUE_NAME` attribute of the database at the specified destination matches the `DB_UNIQUE_NAME` attribute or the connection to that destination is refused.
- The name specified by the `DB_UNIQUE_NAME` attribute must match the name specified by the `DB_UNIQUE_NAME` initialization parameter of the database identified by the destination.

Example

In the following example, the `DB_UNIQUE_NAME` parameter specifies `boston` (`DB_UNIQUE_NAME=boston`), which is also specified with the `DB_UNIQUE_NAME` attribute on the `LOG_ARCHIVE_DEST_1` parameter. The `DB_UNIQUE_NAME` attribute on the `LOG_ARCHIVE_DEST_2` parameter specifies the `chicago` destination. Both `boston` and `chicago` are listed in the `LOG_ARCHIVE_CONFIG=DG_CONFIG` parameter.

```
DB_UNIQUE_NAME=boston
LOG_ARCHIVE_CONFIG='DG_CONFIG=(chicago,boston,denver)'
LOG_ARCHIVE_DEST_1='LOCATION=/arch1/ 
  VALID_FOR=(ALL_LOGFILES,ALL_ROLES) 
  DB_UNIQUE_NAME=boston'
LOG_ARCHIVE_DEST_2='SERVICE=Sales_DR 
  VALID_FOR=(ONLINE_LOGFILES,PRIMARY_ROLE) 
  DB_UNIQUE_NAME=chicago'
```

## DELAY

Specifies a minimum time lag between when redo data from the primary site is archived on a standby site and when the archived redo log file is applied to the standby database or any standbys cascaded from it.

| Category | DELAY\[=minutes\] |
| --- | --- |
| Data Type | Numeric |
| Valid values | \>=0 minutes |
| Default Value | 30 minutes |
| Requires attributes | `SERVICE` |
| Conflicts with attributes | `LOCATION`, VALID\_FOR=(\*,STANDBY\_ROLE) |
| Corresponds to | `DELAY_MINS` and `DESTINATION` columns of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `DELAY` attribute is optional. By default there is no delay.
- The `DELAY` attribute indicates the archived redo log files at the standby destination are not available for recovery until the specified time interval has expired. The time interval is expressed in minutes, and it starts when the redo data is successfully transmitted to, and archived at, the standby site.
- The `DELAY` attribute may be used to protect a standby database from corrupted or erroneous primary data. However, there is a tradeoff because during failover it takes more time to apply all of the redo up to the point of corruption.
- The `DELAY` attribute does not affect the transmittal of redo data to a standby destination.
- If you have real-time apply enabled, any delay that you set will be ignored.
- Changes to the `DELAY` attribute take effect the next time redo data is archived (after a log switch). In-progress archiving is not affected.
- You can override the specified delay interval at the standby site, as follows:
	- For a physical standby database:
		```
		SQL> ALTER DATABASE RECOVER MANAGED STANDBY DATABASE NODELAY;
		```
		- For a logical standby database:
		```
		SQL> ALTER DATABASE START LOGICAL STANDBY APPLY NODELAY;
		```
- The `DELAY` value that a cascaded standby uses is the value that was set for the `LOG_ARCHIVE_DEST_` `n` parameter on the primary that shipped the redo to the cascading standby.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about these `ALTER DATABASE` statements

Examples

You can use the `DELAY` attribute to set up a configuration where multiple standby databases are maintained in varying degrees of synchronization with the primary database. However, this protection incurs some overhead during failover, because it takes Redo Apply more time to apply all the redo up to the corruption point.

For example, assume primary database A has standby databases B and C. Standby database B is set up as the disaster recovery database and therefore has no time lag. Standby database C is set up with a 2-hour delay, which is enough time to allow user errors to be discovered before they are propagated to the standby database.

The following example shows how to specify the `DELAY` attribute for this configuration:

```
LOG_ARCHIVE_DEST_1='LOCATION=/arch/dest MANDATORY'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_2='SERVICE=stbyB SYNC AFFIRM'
LOG_ARCHIVE_DEST_STATE_2=ENABLE
LOG_ARCHIVE_DEST_3='SERVICE=stbyC DELAY=120'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

Note:

Alternatively, you can use Flashback Database to revert the database to a point-in-time or SCN in a different database incarnation as long as there is sufficient flashback log data. Using Flashback Database is described in [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm).

## LOCATION and SERVICE

Each destination must specify either the `LOCATION` or the `SERVICE` attribute to identify either a local disk directory or a remote database destination where redo transport services can transmit redo data.

`LOG_ARCHIVE_DEST_1` through `LOG_ARCHIVE_DEST_10` destinations can contain either a `LOCATION` attribute or a `SERVICE` attribute.

`LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` destinations can only contain a `SERVICE` attribute.

| Category | LOCATION=local\_disk\_directory or `USE_DB_RECOVERY_FILE_DEST` | SERVICE=net\_service\_name |
| --- | --- | --- |
| Data type | String value | String value |
| Valid values | Not applicable | Not applicable |
| Default Value | None | None |
| Requires attributes | Not applicable | Not applicable |
| Conflicts with attributes | `SERVICE`, `DELAY`, `NOREGISTER`, `SYNC`, `ASYNC`, `NET_TIMEOUT, AFFIRM,NOAFFIRM`, `COMPRESSION`, `MAX_CONNECTIONS` | `LOCATION` |
| Corresponds to | `DESTINATION` and `TARGET` columns of the `V$ARCHIVE_DEST` view | `DESTINATION` and `TARGET` columns of the `V$ARCHIVE_DEST` view |

Usage Notes

- Either the `LOCATION` or the `SERVICE` attribute must be specified. There is no default.
- The `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` parameters do not support the `LOCATION` attribute.
- If you are specifying multiple attributes, specify the `LOCATION` or `SERVICE` attribute first in the list of attributes.
- You must specify at least one local disk directory with the `LOCATION` attribute. This ensures that local archived redo log files are accessible should media recovery of a database be necessary. You can specify up to thirty additional local or remote destinations.
- For the `LOCATION` attribute, you can specify one of the following:
	- `LOCATION=` local\_disk\_directory
		This specifies a unique directory path name for a disk directory on the system that hosts the database. This is the local destination for archived redo log files.
		- `LOCATION=USE_DB_RECOVERY_FILE_DEST`
		To configure a fast recovery area, specify the directory or Oracle Storage Manager disk group that will serve as the fast recovery area using the `DB_RECOVERY_FILE_DEST` initialization parameter. For more information about fast recovery areas, see [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm).
- When you specify a `SERVICE` attribute:
	- You identify remote destinations by specifying the `SERVICE` attribute with a valid Oracle Net service name (`SERVICE=` net\_service\_name) that identifies the remote Oracle database instance to which the redo data will be sent.
		The Oracle Net service name that you specify with the `SERVICE` attribute is translated into a connection descriptor that contains the information necessary for connecting to the remote database.
		See Also:
		[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for details about setting up Oracle Net service names
		- Transmitting redo data to a remote destination requires a network connection and an Oracle database instance associated with the remote destination to receive the incoming redo data.
- To verify the current settings for `LOCATION` and `SERVICE` attributes, query the `V$ARCHIVE_DEST` fixed view:
	- The `TARGET` column identifies if the destination is local or remote to the primary database.
		- The `DESTINATION` column identifies the values that were specified for a destination. For example, the destination parameter value specifies the Oracle Net service name identifying the remote Oracle instance where the archived redo log files are located.

Examples

Example 1 Specifying the LOCATION Attribute

```
LOG_ARCHIVE_DEST_2='LOCATION=/disk1/oracle/oradata/payroll/arch/'
LOG_ARCHIVE_DEST_STATE_2=ENABLE
```

Example 2 Specifying the SERVICE Attribute

```
LOG_ARCHIVE_DEST_3='SERVICE=stby1'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## MANDATORY

Specifies that filled online log files must be successfully archived to the destination before they can be reused.

| Category | MANDATORY |
| --- | --- |
| Data type | Keyword |
| Valid values | Not applicable |
| Default value | Not applicable |
| Requires attributes | Not applicable |
| Conflicts with attributes | Optional |
| Corresponds to | `BINDING` column of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` parameters do not support the `MANDATORY` attribute.
- If `MANDATORY` is not specified, then, by default, the destination is considered to be optional.
	At least one destination must succeed, even if all destinations are optional. If archiving to an optional destination fails, the online redo log file is still available for reuse and may be overwritten eventually. However, if the archival operation of a mandatory destination fails, online redo log files cannot be overwritten.
- The `LOG_ARCHIVE_MIN_SUCCEED_DEST=` n parameter (where n is an integer from 1 to 10) specifies the number of destinations that must archive successfully before online redo log files can be overwritten.
	All `MANDATORY` destinations and optional local destinations contribute to satisfying the `LOG_ARCHIVE_MIN_SUCCEED_DEST=` n count. If the value set for the `LOG_ARCHIVE_MIN_SUCCEED_DEST` parameter is met, the online redo log file is available for reuse. For example, you can set the parameter as follows:
	```
	# Database must archive to at least two locations before 
	# overwriting the online redo log files.
	LOG_ARCHIVE_MIN_SUCCEED_DEST = 2
	```
- You must have at least one local destination, which you can declare `MANDATORY` or leave as optional.
	At least one local destination is operationally treated as mandatory, because the minimum value for the `LOG_ARCHIVE_MIN_SUCCEED_DEST` parameter is 1.
- The failure of any mandatory destination makes the `LOG_ARCHIVE_MIN_SUCCEED_DEST` parameter irrelevant.
- The `LOG_ARCHIVE_MIN_SUCCEED_DEST` parameter value cannot be greater than the number of mandatory destinations plus the number of optional local destinations.
- The `BINDING` column of the `V$ARCHIVE_DEST` fixed view specifies how failure affects the archival operation

Examples

The following example shows the `MANDATORY` attribute:

```
LOG_ARCHIVE_DEST_1='LOCATION=/arch/dest MANDATORY'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_3='SERVICE=denver MANDATORY'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## MAX\_CONNECTIONS

Enables multiple network connections to be used when sending an archived redo log file to a redo transport destination. Using multiple network connections can improve redo transport performance over high-latency network links.

| Category | Description |
| --- | --- |
| Data type | Integer |
| Valid values | 1 to 20 |
| Default value | 1 |
| Requires attributes | None |
| Conflicts with attributes | None |
| Corresponds to | `MAX_CONNECTIONS` column of the `V$ARCHIVE_DEST` view of the primary database |

Usage Notes

- The `MAX_CONNECTIONS` attribute is optional. If it is specified, it is only used when redo transport services use ARCn processes for archival.
	- If `MAX_CONNECTIONS` is set to 1 (the default), redo transport services use a single ARCn process to transmit redo data to the remote destination.
		- If `MAX_CONNECTIONS` is set to a value greater than 1, redo transport services use multiple ARCn processes to transmit redo in parallel to archived redo log files at the remote destination. Each archiver (ARCn) process uses a separate network connection.
- With multiple ARCn processes, redo transmission occurs in parallel, thus increasing the speed at which redo is transmitted to the remote destination.
- Redo that is received from an ARCn process is written directly to an archived redo log file. Therefore, it cannot be applied in real-time as it is received.
- The actual number of archiver processes in use at any given time may vary based on the archiver workload and the value of the `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter. For example, if the total of `MAX_CONNECTIONS` attributes on all destinations exceeds the value of `LOG_ARCHIVE_MAX_PROCESSES`, then Data Guard will use as many ARCn processes as possible, but the number may be less than what is specified by the `MAX_CONNECTIONS` attribute.
- When using multiple ARCn processes in an Oracle RAC environment, configure the primary instance to transport redo data to a single standby database instance. If redo transport services are not configured as such, then archival will return to the default behavior for remote archival, which is to transport redo data using a single ARCn process.

Examples

The following example shows the `MAX_CONNECTIONS` attribute:

```
LOG_ARCHIVE_DEST_1='LOCATION=/arch/dest'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
LOG_ARCHIVE_DEST_3='SERVICE=denver MAX_CONNECTIONS=3'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## MAX\_FAILURE

Controls the consecutive number of times redo transport services attempt to reestablish communication and transmit redo data to a failed destination before the primary database gives up on the destination.

| Category | MAX\_FAILURE=count |
| --- | --- |
| Data type | Numeric |
| Valid value | \>=0 |
| Default value | None |
| Requires attributes | `REOPEN` |
| Conflicts with attributes | None |
| Corresponds to | `MAX_FAILURE`, `FAILURE_COUNT`, and `REOPEN_SECS` columns of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `MAX_FAILURE` attribute is optional. By default, there are an unlimited number of archival attempts to the failed destination.
- This attribute is useful for providing failure resolution for destinations to which you want to retry transmitting redo data after a failure, but not retry indefinitely.
- When you specify the `MAX_FAILURE` attribute, you must also set the `REOPEN` attribute. Once the specified number of consecutive attempts is exceeded, the destination is treated as if the `REOPEN` attribute was not specified.
- You can view the failure count in the `FAILURE_COUNT` column of the `V$ARCHIVE_DEST` fixed view. The related column `REOPEN_SECS` identifies the `REOPEN` attribute value.
	Note:
	Once the failure count for the destination reaches the specified `MAX_FAILURE` attribute value, the only way to reuse the destination is to modify the `MAX_FAILURE` attribute value or any attribute. This has the effect of resetting the failure count to zero (0).
- The failure count is reset to zero (0) whenever the destination is modified by an `ALTER SYSTEM SET` statement. This avoids the problem of setting the `MAX_FAILURE` attribute to a value less than the current failure count value.
- Once the failure count is greater than or equal to the value set for the `MAX_FAILURE` attribute, the `REOPEN` attribute value is implicitly set to zero, which causes redo transport services to transport redo data to an alternate destination (defined with the `ALTERNATE` attribute) on the next archival operation.
- Redo transport services attempt to archive to the failed destination indefinitely if you do not specify the `MAX_FAILURE` attribute (or if you specify `MAX_FAILURE=0`), and you specify a nonzero value for the `REOPEN` attribute. If the destination has the `MANDATORY` attribute, the online redo log file is not reusable until it has been archived to this destination.

Examples

The following example allows redo transport services up to three consecutive archival attempts, tried every 5 seconds, to the `arc_dest` destination. If the archival operation fails after the third attempt, the destination is treated as if the `REOPEN` attribute was not specified.

```
LOG_ARCHIVE_DEST_1='LOCATION=/arc_dest REOPEN=5 MAX_FAILURE=3'
LOG_ARCHIVE_DEST_STATE_1=ENABLE
```

## NET\_TIMEOUT

Specifies the number of seconds that the LGWR background process will block waiting for a redo transport destination to acknowledge redo data sent to it. If an acknowledgement is not received within `NET_TIMEOUT` seconds, an error is logged and the redo transport session to that destination is terminated.

| Category | NET\_TIMEOUT=seconds |
| --- | --- |
| Data type | Numeric |
| Valid values | 1 <sup>Foot 1</sup> to 1200 |
| Default value | 30 seconds |
| Requires attributes | `SYNC` |
| Conflicts with attributes | `ASYNC` (If you specify the `ASYNC` attribute, redo transport services ignores it; no error is returned.) |
| Corresponds to | `NET_TIMEOUT` column of the `V$ARCHIVE_DEST` view of the primary database |

<sup>Footnote 1</sup> Although a minimum value of 1 second is allowed, Oracle recommends a minimum value of 8 to 10 seconds to avoid disconnecting from the standby database due to transient network errors.

Usage Notes

- The `NET_TIMEOUT` attribute is optional. However, if you do not specify the `NET_TIMEOUT` attribute it will be set to 30 seconds, but the primary database can potentially stall. To avoid this situation, specify a small, nonzero value for the `NET_TIMEOUT` attribute so the primary database can continue operation after the user-specified timeout interval expires when waiting for status from the network server.

Examples

The following example shows how to specify a 10-second network timeout value on the primary database with the `NET_TIMEOUT` attribute.

```
LOG_ARCHIVE_DEST_2='SERVICE=stby1 SYNC NET_TIMEOUT=10'
LOG_ARCHIVE_DEST_STATE_2=ENABLE
```

## NOREGISTER

Indicates that the location of the archived redo log file should not be recorded at the corresponding destination.

| Category | NOREGISTER |
| --- | --- |
| Data type | Keyword |
| Valid values | Not applicable |
| Default value | Not applicable |
| Requires attributes | `SERVICE` |
| Conflicts with attributes | `LOCATION` |
| Corresponds to | `DESTINATION` and `TARGET` columns of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `NOREGISTER` attribute is optional if the standby database destination is a part of a Data Guard configuration.
- The `NOREGISTER` attribute is required if the destination is not part of a Data Guard configuration.
- This attribute pertains to remote destinations only. The location of each archived redo log file is always recorded in the primary database control file.

Examples

The following example shows the `NOREGISTER` attribute:

```
LOG_ARCHIVE_DEST_5='NOREGISTER'
```

## REOPEN

Specifies the minimum number of seconds before redo transport services should try to reopen a failed destination.

| Category | REOPEN \[=seconds\] |
| --- | --- |
| Data Type | Numeric |
| Valid values | \>=0 seconds |
| Default Value | 300 seconds |
| Requires attributes | None |
| Conflicts with attributes | `Not applicable` |
| Corresponds to | `REOPEN_SECS` and `MAX_FAILURE` columns of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `REOPEN` attribute is optional.
- Redo transport services attempt to reopen failed destinations at log switch time.
- Redo transport services check if the time of the last error plus the `REOPEN` interval is less than the current time. If it is, redo transport services attempt to reopen the destination.
- `REOPEN` applies to all errors, not just connection failures. These errors include, but are not limited to, network failures, disk errors, and quota exceptions.
- If you specify `REOPEN` for an optional destination, it is possible for the Oracle database to overwrite online redo log files if there is an error. If you specify `REOPEN` for a `MANDATORY` destination, redo transport services will stall the primary database when it is not possible to successfully transmit redo data. When this situation occurs, consider the following options:
	- Change the destination by deferring the destination, specifying the destination as optional, or changing the `SERVICE` attribute value.
		- Specify an alternate destination.
		- Disable the destination.

Examples

The following example shows the `REOPEN` attribute.

```
LOG_ARCHIVE_DEST_3='SERVICE=stby1 MANDATORY REOPEN=60'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## SYNC and ASYNC

Specifies whether the synchronous (`SYNC`) or asynchronous (`ASYNC`) redo transport mode is to be used.

| Category | SYNC | ASYNC |
| --- | --- | --- |
| Data type | Keyword | Keyword |
| Valid values | Not applicable | Not applicable |
| Default value | Not applicable | None |
| Requires attributes | None | None |
| Conflicts with attributes | `ASYNC`, `LOCATION` | `SYNC`, `LOCATION` |
| Corresponds to | `TRANSMIT_MODE` column of the `V$ARCHIVE_DEST` view | `TRANSMIT_MODE` and column of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` parameters do not support the `SYNC` attribute.
- The redo data generated by a transaction must have been received by every enabled destination that has the `SYNC` attribute before that transaction can commit.
- The redo data generated by a transaction need not have been received at a destination that has the `ASYNC` attribute before that transaction can commit. This is the default behavior if neither `SYNC` or `ASYNC` is specified.

Examples

The following example shows the `SYNC` attribute with the `LOG_ARCHIVE_DEST_` `n` parameter.

```
LOG_ARCHIVE_DEST_3='SERVICE=stby1 SYNC'
LOG_ARCHIVE_DEST_STATE_3=ENABLE
```

## TEMPLATE

Defines a directory specification and format template for names of archived redo log files at the destination. The template is used to generate a filename that is different from the default filename format defined by the `LOG_ARCHIVE_FORMAT` initialization parameter at the redo destination.

| Category | TEMPLATE=filename\_template\_%t\_%s\_%r |
| --- | --- |
| Data Type | String value |
| Valid values | Not applicable |
| Default value | None |
| Requires attributes... | `SERVICE` |
| Conflicts with attributes... | `LOCATION` |
| Corresponds to... | `REMOTE_TEMPLATE` and `REGISTER` columns of the `V$ARCHIVE_DEST` view |

Usage Notes

- The `TEMPLATE` attribute is optional. If `TEMPLATE` is not specified, archived redo logs are named using the value of the `LOG_ARCHIVE_FORMAT` initialization parameter.
- The `TEMPLATE` attribute overrides the `LOG_ARCHIVE_FORMAT` initialization parameter setting at the remote archival destination.
- The `TEMPLATE` attribute is valid only with remote destinations (that is, destinations specified with the `SERVICE` attribute).
- The value you specify for filename\_template must contain the %s, %t, and %r directives described in Table 15-1.
	Table 15-1 Directives for the TEMPLATE Attribute
	| Directive | Description |
	| --- | --- |
	| %t | Substitute the instance thread number. |
	| %T | Substitute the instance thread number, zero filled. |
	| %s | Substitute the log file sequence number. |
	| %S | Substitute the log file sequence number, zero filled. |
	| %r | Substitute the resetlogs ID. |
	| %R | Substitute the resetlogs ID, zero filled. |
- The filename\_template value is transmitted to the destination, where it is translated and validated before creating the filename.

## VALID\_FOR

Specifies whether redo data will be written to a destination, based on the following factors:

- Whether the database is currently running in the primary or the standby role
- Whether online redo log files, standby redo log files, or both are currently being archived on the database at this destination

| Category | VALID\_FOR=(redo\_log\_type, database\_role) |
| --- | --- |
| Data Type | String value |
| Valid values | Not applicable |
| Default Value | `VALID_FOR=(ALL_LOGFILES, ALL_ROLES)` |
| Requires attributes | None |
| Conflicts with attributes | None |
| Corresponds to | `VALID_NOW`, `VALID_TYPE`, and `VALID_ROLE` columns in the `V$ARCHIVE_DEST` view |

Usage Notes

- The `VALID_FOR` attribute is optional. However, Oracle recommends that the `VALID_FOR` attribute be specified for each redo transport destination at each database in a Data Guard configuration so that redo transport continues after a role transition to any standby database in the configuration.
- To configure these factors for each `LOG_ARCHIVE_DEST_` `n` destination, you specify this attribute with a pair of keywords: `VALID_FOR=(`redo\_log\_type`,`database\_role`)`:
	- The redo\_log\_type keyword identifies the destination as valid for archiving one of the following:
		- `ONLINE_LOGFILE` —This destination is valid only when archiving online redo log files.
				- `STANDBY_LOGFILE` —This destination is valid only when archiving standby redo log files.
				- `ALL_LOGFILES` — This destination is valid when archiving either online redo log files or standby redo log files.
		- The database\_role keyword identifies the role in which this destination is valid for archiving:
		- `PRIMARY_ROLE` —This destination is valid only when the database is running in the primary role.
				- `STANDBY_ROLE` —This destination is valid only when the database is running in the standby role.
				- `ALL_ROLES` —This destination is valid when the database is running in either the primary or the standby role.
- If you do not specify the `VALID_FOR` attribute for a destination, by default, archiving online redo log files and standby redo log files is enabled at the destination, regardless of whether the database is running in the primary or the standby role. This default behavior is equivalent to setting the `(ALL_LOGFILES,ALL_ROLES)` keyword pair on the `VALID_FOR` attribute.
- The `VALID_FOR` attribute enables you to use the same initialization parameter file for both the primary and standby roles.

Example

The following example shows the default `VALID_FOR` keyword pair:

```
LOG_ARCHIVE_DEST_1='LOCATION=/disk1/oracle/oradata VALID_FOR=(ALL_LOGFILES, ALL_ROLES)'
```

When this database is running in either the primary or standby role, destination 1 archives all log files to the `/disk1/oracle/oradata` local directory location.