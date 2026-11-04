---
title: Oracle Connection Manager Parameters (cman.ora)
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/cman.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 8 Oracle Connection Manager Parameters (cman.ora)

This chapter provides a complete listing of the `cman.ora` file configuration parameters.

This chapter contains the following topics:

## Overview of Oracle Connection Manager Configuration File

[Oracle Connection Manager](glossary.md) configuration information, stored in the `cman.ora` file, consists of the following elements:

- Protocol address of the Oracle Connection Manager listener
- Access control parameters
- Performance parameters

By default, the `cman.ora` file is located in the `ORACLE_HOME/network/admin` directory. The `cman.ora` file can also be stored in the following locations:

- The directory specified by the `TNS_ADMIN` environment variable or registry value.
- On Linux and UNIX operating systems, the global configuration directory. For example, on the Solaris Operating System, this directory is `/var/opt/oracle`.
	See Also:
	Oracle operating system-specific documentation

Example 8-1 shows an sample of a `cman.ora` file.

Example 8-1 Sample cman.ora File

```
CMAN=
  (CONFIGURATION=
    (ADDRESS=(PROTOCOL=tcp)(HOST=proxysvr)(PORT=1521))
    (RULE_LIST=
      (RULE=(SRC=192.168.2.32/27)(DST=sales-server)(SRV=*)(ACT=accept))
        (ACTION_LIST=(AUT=on)(MCT=120)(MIT=30)))
      (RULE=(SRC=foo)(DST=hr-server)(SRV=cmon)(ACT=accept)))
    (PARAMETER_LIST=
      (MAX_GATEWAY_PROCESSES=8)
      (MIN_GATEWAY_PRCESSSES=3)
      (DIAG_ADR_ENABLED=ON)
      (ADR_BASE=/oracle/log)))
```

The `cman.ora` configuration file consists of the following sections:

- Listening address: Preceded by `ADDRESS=`, this section contains information pertinent to the listener. The `ADDRESS` parameter is required.
- Rule list: Preceded by `RULE_LIST=`, this section contains rule information. The RULE parameter is listed in the rule list section of the file. The `RULE` parameter is required.
- Parameter list: Preceded by `PARAMETER_LIST=`, this section contains all other parameters including those listed in "ADR Diagnostic Parameters for Oracle Connection Manager", and "Non-ADR Diagnostic Parameters for Oracle Connection Manager".

The following parameters are allowed in the parameter list section of the `cman.ora` file. The default values are bold. To override the default setting for a parameter, enter the parameter and a nondefault value.

`ASO_AUTHENTICATION_FILTER={` `off` `| on}`

`CONNECTION_STATISTICS={` `no` `| yes}`

`EVENT_GROUP={init_and_term | memory_ops | conn_hdlg | proc_mgmt | reg_and_load | wake_up | timer | cmd_proc | relay}`

`IDLE_TIMEOUT=` `0` or greater

`INBOUND_CONNECT_TIMEOUT=0` or greater

`LOG_DIRECTORY=` `log_directory`

`LOG_LEVEL={off | user | admin |` `support` `}`

`MAX_CMCTL_SESSIONS=` Any positive number

`MAX_CONNECTIONS=` \[1 to 1024\]

`MAX_GATEWAY_PROCESSES=` Any number greater than the minimum number of gateway processes up to 64

`MIN_GATEWAY_PROCESSES=` Any positive number less than or equal to 64. Must be less than or equal to the maximum number of gateway processes.

`OUTBOUND_CONNECT_TIMEOUT=` `0` or greater

`PASSWORD_` `instance_name` `=` Value is the encrypted instance password, if one has been set.

`SESSION_TIMEOUT=` `0` or greater

`TRACE_DIRECTORY=` `trace_directory`

`TRACE_FILELEN=` Any positive number

`TRACE_FILENO=` Any positive number

`TRACE_LEVEL={` `off` `| user | admin | support}`

`TRACE_TIMESTAMP={` `off` `| on}`

Notes:

- `INBOUND_CONNECT_TIMEOUT` default value is 60.
- `LOG_DIRECTORY` default value is `ORACLE_HOME/network/log`.
- `MAX_CMCTL_SESSIONS` default value is 4.
- `MAX_CONNECTIONS` default value is 256.
- `MAX_GATEWAY_PROCESSES` default value is 16.
- `MIN_GATEWAY_PROCESSES` default value is 2.
- `PASSWORD_` `instance_name` default value is no value.
- `TRACE_DIRECTORY` default value is `ORACLE_HOME/network/trace`.
- `TRACE_FILEEN` default value is 0.
- `TRACE_FILENO` default value is 0.
- You cannot add the parameter `PASSWORD_` `instance_name` directly to the `cman.ora` file. The parameter is added when you issue the command `SAVE_PASSWD`.

Example 8-2 shows the parameter list section of a `cman.ora` file.

Example 8-2 Parameter List Section of a cman.ora File

```
(PARAMETER_LIST= 
   (ASO_AUTHENTICATION_FILTER=ON)
   (CONNECTION_STATISTICS=NO)
   (EVENT_GROUP=INIT_AND_TERM,MEMORY_OPS,PROCESS_MGMT)
   (IDLE_TIMEOUT=30)
   (INBOUND_CONNECT_TIMEOUT=30)
   (LOG_DIRECTORY=/home/user/network/admin/log)   
   (LOG_LEVEL=SUPPORT)
   (MAX_CMCTL_SESSIONS=6)
   (MAX_CONNECTIONS=512)
   (MAX_GATEWAY_PROCESSES=10)
   (MIN_GATEWAY_PROCESSES=4)
   (OUTBOUND_CONNECT_TIMEOUT=30)
   (SESSION_TIMEOUT=60)
   (TRACE_DIRECTORY=/home/user/network/admin/trace)
   (TRACE_FILELEN=100)
   (TRACE_FILENO=2)
   (TRACE_LEVEL=SUPPORT)
   (TRACE_TIMESTAMP=ON))
```

## Oracle Connection Manager Parameters

This section lists and describes the following `cman.ora` file parameters:

- ADDRESS
- ASO\_AUTHENTICATION\_FILTER
- CONNECTION\_STATISTICS
- EVENT\_GROUP
- IDLE\_TIMEOUT
- INBOUND\_CONNECT\_TIMEOUT
- LOG\_DIRECTORY
- LOG\_LEVEL
- MAX\_CMCTL\_SESSIONS
- MAX\_CONNECTIONS
- MAX\_GATEWAY\_PROCESSES
- MIN\_GATEWAY\_PROCESSES
- OUTBOUND\_CONNECT\_TIMEOUT
- PASSWORD\_instance\_name
- RULE
- SESSION\_TIMEOUT
- TRACE\_FILE
- TRACE\_FILELEN
- TRACE\_FILENO
- TRACE\_LEVEL
- TRACE\_TIMESTAMP

### ADDRESS

Purpose

To specify the protocol address of Oracle Connection Manager.

Syntax

```
(ADDRESS=(PROTOCOL=protocol
)(HOST=host_name
)(PORT=port_number
)
```

Example

```
(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521))
```

### ASO\_AUTHENTICATION\_FILTER

Purpose

To specify whether Oracle Advanced Security authentication settings must be used by the client. The global setting can be overridden by a rule-level setting in `ACTION_LIST`.

Values

- `on` to instruct Oracle Connection Manager to reject connect requests that are not using Secure Network Services (SNS). SNS is part of the Oracle Advanced Security.
- `off` (default) to instruct Oracle Connection Manager not to check for SNS between the client and server

### CONNECTION\_STATISTICS

Purpose

To specify whether the `SHOW_CONNECTIONS` command displays connection statistics. The global setting can be overridden by a rule-level setting in `ACTION_LIST`.

Values

- `yes` to display statistics
- `no` (default) to not display statistics

### EVENT\_GROUP

Purpose

To specify which event groups are logged. Multiple events may be designated using a comma-delimited list.

Values

- `alert` for alert notifications
- `cmd_proc` for command processing
- `conn_hdlg` for connection handling
- `init_and_term` for initialization and termination
- `memory_ops` for memory operations
- `proc_mgmt` for process management
- `reg_and_load` for registration and load update
- `relay` for events associated with connection control blocks
- `timer` for gateway timeouts
- `wake_up` for events related to CMADMIN wake-up queue

Note:

The event group `ALERT` cannot be turned off.

### IDLE\_TIMEOUT

Purpose

To specify the amount of time that an established connection can remain active without transmitting data. The global setting can be overridden by a rule-level setting in `ACTION_LIST`.

Values

- `0` (default) to disable the timeout.
- any number greater than 0 to enable the timeout. The number equals the timeout period in seconds

### INBOUND\_CONNECT\_TIMEOUT

Purpose

To specify how long the Oracle Connection Manager listener waits for a valid connection from a client or another instance of Oracle Connection Manager.

Values

- `60` (default) to disable the timeout.
- any number greater than 0 to enable the timeout. The number equals the timeout period in seconds.

### LOG\_DIRECTORY

Purpose

To specify the directory for the Oracle Connection Manager log files.

### LOG\_LEVEL

Purpose

To specify the level for log messages.

Values

- `off` for no logging. This is the default.
- `user` for user-induced errors log information.
- `admin` for administration, such as installation-specific, log information.
- `support` for Oracle Support Services information.

### MAX\_CMCTL\_SESSIONS

Purpose

To specify the maximum number of concurrent local or remote sessions of the Oracle Connection Manager control utility allowable for a given instance. One of these sessions must be a local session.

Values

Any number of sessions can be designated.

### MAX\_CONNECTIONS

Purpose

To specify the maximum number of connection slots that a gateway process can handle.

Values

This parameter accepts a range of 1 to 1024.

### MAX\_GATEWAY\_PROCESSES

Purpose

To specify the maximum number of gateway processes that an instance of Oracle Connection Manager supports.

Values

The number designated must be greater than the minimum number of gateway processes. The maximum is 64.

### MIN\_GATEWAY\_PROCESSES

Purpose

To specify the minimum number of gateway processes that an instance of Oracle Connection Manager must support.

Values

Any number of sessions can be designated up to 64.

### OUTBOUND\_CONNECT\_TIMEOUT

Purpose

To specify the length of time that the Oracle Connection Manager instance waits for a valid connection to be established with the database server or with another Oracle Connection Manager instance.

Values

- `60` (default) to disable the timeout.
- Any number greater than 0 to enable the timeout. The number equals the timeout period in seconds.

### PASSWORD\_instance\_name

Purpose

To specify the encrypted instance password, if one has been set.

### RULE

Purpose

To specify an access control rule list to filter incoming connections. A rule list specifies which connections are accepted, rejected, or dropped.

Values

This parameter is listed in the rule list section of the `cman.ora` file preceded by `RULE_LIST=`.

Syntax

```
(RULE_LIST=
  (RULE=
    (SRC=host)
    (DST=host)
    (SRV=service_name)
    (ACT={accept|reject|drop})
    (ACTION_LIST=AUT={on|off}
    ((CONN_STATS={yes|no})(MCT=time)(MIT=time)(MOCT=time)))
  (RULE= ...))
```

Additional Parameters

The `RULE` parameter filters a connection or group of connections using the following parameters:

`SRC`: Specify the source host name or IP address of the client.

`DST`: Specify the destination server host name or IP address of the database server.

`SRV`: Specify database [service name](glossary.md) of Oracle Database obtained from the `SERVICE_NAME` parameter in the initialization parameter file.

`ACT`: Specify `accept` to accept incoming requests, `reject` to reject incoming requests, or `drop` to reject incoming requests without sending an error message.

`ACTION_LIST`: Specify rule-level parameter settings for some parameters. These parameters are as follows:

- `AUT`: Oracle Advanced Security authentication on client side
- `CONN_STATS`: Log input and output statistics
- `MCT`: Maximum connect time
- `MIT`: Maximum idle timeout
- `MOCT`: Maximum outbound connect time

Rule-level parameters override their global counterparts.

Usage Notes

- If no rules are specified, then all connections are rejected.
- The source and destination can be a host name, IP address, or subnet mask.
- You must enter at least one rule for client connections and one rule for CMCTL connections. Omitting one or the other results in the rejection of all connections for the rule type omitted. The last rule in the example that follows is a CMCTL rule.
- Oracle Connection Manager does not support wildcards for partial IP addresses. If you use a wildcard, then use it in place of a full IP address. The IP address of the client may, for example, be (SRC=\*).
- Oracle Connection Manager supports only the `/nn` notation for subnet addresses. In the first rule in the example, /27 represents a subnet mask that comprises 27 left-most bits.

Example

```
(RULE_LIST=
  (RULE=
    (SRC=client1-pc)
    (DST=sales-server)
    (SRV=sales.us.example.com)
    (ACT=reject))
  (RULE=
    (SRC=192.168.2.45)
    (DST=192.168.2.200)
    (SRV=db1)
    (ACT=accept))
  (RULE=
    (SRC=foo)
    (DST=foobar)
    (SRV=cmon)
    (ACT=accept)))
```

### SESSION\_TIMEOUT

Purpose

To specify the maximum time allowed for a user session. The global setting can be overridden by a rule-level setting in `ACTION_LIST`. This parameter accepts the following values:

Values

- `0` (default) to disable the timeout.
- Any number greater than 0 to enable the timeout. The number equals the timeout period in seconds.

### TRACE\_FILE

Purpose

To specify the directory for Oracle Connection Manager trace files.

### TRACE\_FILELEN

Purpose

To specify the size of the trace file in KB. When the size is reached, the trace information is written to the next file. The number of files is specified with the `TRACE_FILENO` parameter.

### TRACE\_FILENO

Purpose

To specify the number of trace files. When this parameter is set along with the `TRACE_FILELEN` parameter, trace files are used in a cyclical fashion. The first file is filled first, then the second file, and so on. When the last file has been filled, the first file is reused, and so on.

### TRACE\_LEVEL

Purpose

To specify the level for trace messages.

Values

- `off` for no tracing. This is the default.
- `user` for user-induced errors trace information.
- `admin` for administration, such as installation-specific, trace information.
- `support` for Oracle Support Services information.

### TRACE\_TIMESTAMP

Purpose

To specify the use of a timestamp for the tracing logs. If the TRACING parameter is enabled, then a time stamp in the form of `dd-mon-yyyy hh:mi:ss:mil` for every trace event in the trace file.

Values

- `off` for no timestamp is included in the file.
- `on` for timestamp to be included in the file.

## ADR Diagnostic Parameters for Oracle Connection Manager

Beginning with Oracle Database 11g, Oracle Database includes an advanced fault diagnosability infrastructure for preventing, detecting, diagnosing, and resolving problems. The problems are critical errors such as those caused by database code bugs, metadata corruption, and customer data corruption.

When a critical error occurs, it is assigned an incident number, and diagnostic data for the error, such as traces and dumps, are immediately captured and tagged with the incident number. The data is then stored in the [Automatic Diagnostic Repository (ADR)](glossary.md), a file-based repository outside the database.

This section describes the parameters used when [ADR](glossary.md) is enabled (when `DIAG_ADR_ENABLED` is set to `on`). "Non-ADR Diagnostic Parameters for Oracle Connection Manager" describes the parameters used when ADR is disabled (when `DIAG_ADR_ENABLED` is set to `off`). Non-ADR parameters listed in the `cman.ora` file are ignored when ADR is enabled.

- ADR\_BASE
- DIAG\_ADR\_ENABLED
- LOG\_LEVEL
- TRACE\_LEVEL
- TRACE\_TIMESTAMP

### ADR\_BASE

Purpose

To specify the base directory into which tracing and logging incidents are stored when ADR is enabled.

Default

The default is `ORACLE_BASE`, or `ORACLE_HOME/log` if `ORACLE_BASE` is not defined.

Values

Any valid directory path to a directory with write permission.

Example

```
ADR_BASE=/oracle/network/trace
```

### DIAG\_ADR\_ENABLED

Purpose

To indicate whether ADR tracing is enabled.

Usage

When the `DIAG_ADR_ENABLED` parameter is set to `OFF`, non-ADR file tracing is used.

Values

`on` | `off`

Example

```
DIAG_ADR_ENABLED=on
```

### LOG\_LEVEL

Purpose

To specify the level of logging performed by Oracle Connection Manager. This parameter is also applicable when non-ADR logging is used.

The following log files are used with Oracle Connection Manager:

- `instance-name_pid``.log` for the listener
- `instance-name_` `cmadmin` `_pid``.log` for CMADMIN
- `instance-name_` `cmgw` `_pid``.log` for the gateway processes

The log files are located in the `ORACLE_HOME/network/log` directory.

Default

off or 0

Values

- `off` or `0` for no log output
- `user` or `4` for user log information
- `admin` or `10` for administration log information
- `support` or `16` for Oracle Support Services log information

Example

```
LOG_LEVEL=admin
```

### TRACE\_LEVEL

Purpose

To specify the trace level for the Oracle Connection Manager instance. This parameter is also applicable when non-ADR tracing is used.

The following trace files are used with Oracle Connection Manager:

- `instance-name_pid``.trc` for the listener
- `instance-name_` `cmadmin` `_pid``.trc` for CMADMIN
- `instance-name_` `cmgw` `_pid``.trc` for the gateway processes

The log files are located in the `ORACLE_HOME/network/log` directory.

Default

off

Values

- `off` for no trace output
- `user` for user trace information
- `admin` for administration trace information
- `support` for Oracle Support Services trace information

Example

```
TRACE_LEVEL=admin
```

### TRACE\_TIMESTAMP

Purpose

To add a time stamp in the form of `dd-mon-yyyy hh:mi:ss:mil` to every trace event in the trace file for the listener. This parameter is used with the TRACE\_LEVEL parameter. This parameter is also applicable when non-ADR tracing is used.

Default

on

Values

- `on` or `true`
- `off` or `false`

Example

```
TRACE_TIMESTAMP=true
```

## Non-ADR Diagnostic Parameters for Oracle Connection Manager

This section lists the parameters used when ADR is disabled (when `DIAG_ADR_ENABLED` is set to `off`):

Notes:

The default value of DIAG\_ADR\_ENABLED is `on`. Therefore, the `DIAG_ADR_ENABLED` parameter must explicitly be set to `off` in order for non-ADR tracing to be used.

- LOG\_DIRECTORY
- TRACE\_DIRECTORY
- TRACE\_FILELEN
- TRACE\_FILENO

### LOG\_DIRECTORY

Purpose

To specify the location of Oracle Connection Manager log files. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/log
```

Values

Any valid directory path to a directory with write permission.

Example

```
LOG_DIRECTORY=/oracle/network/log
```

### TRACE\_DIRECTORY

Purpose

To specify the location of the Oracle Connection Manager trace files. Use this parameter when ADR is not enabled.

Default

```
ORACLE_HOME/network/trace
```

Values

Any valid directory path to a directory with write permission.

Example

```
TRACE_DIRECTORY=/oracle/network/admin/trace
```

### TRACE\_FILELEN

Purpose

To specify the size, in KB, of the trace file. When the size is met, the trace information is written to the next file. The number of files is specified with the TRACE\_FILENO parameter. Any size can be designated. Use this parameter when ADR is not enabled.

Default

Unlimited

Example

```
TRACE_FILELEN=100
```

### TRACE\_FILENO

Purpose

To specify the number of trace files for Oracle Connection Manager tracing. When this parameter is set along with the TRACE\_FILELEN parameter, trace files are used in a cyclical fashion. The first file is filled first, then the second file, and so on. When the last file has been filled, the first file is reused, and so on. Any number of files can be designated.

The trace file names are distinguished from one another by their sequence number. For example, if this parameter is set to `3`, then the gateway trace files would be named `instance-name_` `cmgw1` `_pid``.trc`, `instance_name_` `cmgw2` `_pid``.trc` and `instance_name_` `cmgw3` `_pid``.trc`.

In addition, trace events in the trace files are preceded by the sequence number of the file. Use this parameter when ADR is not enabled.

Default

1

Example

```
TRACE_FILENO=3
```