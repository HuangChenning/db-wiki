---
title: Listener Control Utility
book: Net Services Reference
doc_id: E10835-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10835/lsnrctl.htm
tags:
  - oracle
  - 11g
  - net-services-reference
---

## 1 Listener Control Utility

This chapter describes the commands and associated syntax of the [Listener Control utility](glossary.md).

This chapter contains the following topics:

## Listener Control Utility Overview

The Listener Control utility enables you to administer [listener](glossary.md) s.You can use its commands to perform basic management functions on one or more listeners. Additionally, you can view and change parameter settings.

The basic syntax of Listener Control utility commands is as follows:

```
lsnrctl command listener_name
```

In the preceding command, listener\_name is the name of the listener to be administered. If no name is specified, then the default name, `LISTENER`, is assumed.

You can also issue Listener Control utility commands at the `LSNRCTL>` program prompt. To obtain the prompt, enter `lsnrctl` with no arguments at the operating system command line. When you run `lsnrctl`, the program is started. You can then enter the necessary commands from the program prompt. The basic syntax of issuing commands from `LSNRCTL>` program prompt is as follows:

```
lsnrctl
LSNRCTL> command listener_name
```

Note:

You can combine commands in a standard text file, and then run them as a sequence of commands. To execute in batch mode, use the format:

`lsnrctl @` `file_name`

You can use either `REM` or `#` to identify comments in the batch script; all other lines are considered commands. Any commands that would typically require confirmation do not require confirmation during batch execution.

For most commands, the Listener Control utility establishes an Oracle Net connection with the listener that is used to transmit the command. To initiate an Oracle Net connection to the listener, the Listener Control utility must obtain the protocol addresses for the named listener or a listener named `LISTENER`. This is done by resolving the listener name with one of the following mechanisms:

- `listener.ora` file in the directory specified by the `TNS_ADMIN` environment variable
- `listener.ora` file in the `ORACLE_HOME/network/admin` directory.
- Naming method, for example, a `tnsnames.ora` file

If none of the preceding mechanisms resolve the listener name, then the Listener Control utility uses the default listener name `LISTENER`, resolves the host name IP address and uses port 1521.

The Listener Control utility supports several types of commands:

- Operational commands, such as START, and STOP.
- Modifier commands, such as SET TRC\_LEVEL.
- Informational commands, such as STATUS and SHOW LOG\_FILE.

## SET and SHOW Commands of the Listener Control utility

You can use the SET command to alter parameter values for a specified listener. You set the name of the listener you want to administer with the SET CURRENT\_LISTENER command. Parameter values remain in effect until the listener is shut down. If you want these settings to persist, then use the SAVE\_CONFIG command to save changes to the `listener.ora`.

You can use the SHOW command to display the current value of a configuration setting.

## Distributed Operations

The Listener Control utility can perform operations on a local or a remote listener.

To set up a computer to remotely administer a listener, do the following:

1. Ensure that the Listener Control utility (`lsnrctl`) executable is installed in the `ORACLE_HOME/bin` directory.
2. Ensure that the name of the listener you want to administer can be resolved through a `listener.ora` file or a naming method, as described in "Listener Control Utility Overview".

All commands except START can be issued when a listener is administered remotely. The Listener Control utility can only start the listener on the same computer from where the utility is running.

When issuing commands, specify the listener name as an argument. For example:

```
LSNRCTL> SERVICES lsnr
```

If the name is omitted, then listener name set with the SET CURRENT\_LISTENER command is used, or the default name, `LISTENER` is assumed.

## Oracle Net Listener Security

Local listener administration is secure through local operating system authentication, which restricts listener administration to the user who started the listener or to the super user. By default, remote listener administration is disabled.

Oracle recommends that you perform listener administration in the default mode, and access the system remotely using a remote login. When you administer the listener remotely, use Oracle Enterprise Manager or Secure Shell (SSH) to access the remote host.

## Listener Control Utility Commands

This section describes the following Listener Control utility commands:

- EXIT
- HELP
- QUIT
- RELOAD
- SAVE\_CONFIG
- SERVICES
- SET
- SET CURRENT\_LISTENER
- SET DISPLAYMODE
- SET INBOUND\_CONNECT\_TIMEOUT
- SET LOG\_DIRECTORY
- SET LOG\_FILE
- SET LOG\_STATUS
- SET SAVE\_CONFIG\_ON\_STOP
- SET TRC\_DIRECTORY
- SET TRC\_FILE
- SET TRC\_LEVEL
- SHOW
- SPAWN
- START
- STATUS
- STOP
- TRACE
- VERSION

### EXIT

Purpose

To exit from the Listener Control utility, and return to the operating system prompt.

Prerequisites

None

Syntax

From the Listener Control utility:

```
LSNRCTL> EXIT
```

Arguments

None

Usage Notes

This command is identical to the QUIT command.

Example

```
LSNRCTL> EXIT
```

### HELP

Purpose

To provide a list of all the Listener Control utility commands or provide syntax help for a particular Listener Control utility command.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl HELP command
```

From the Listener Control utility:

```
LSNRCTL> HELP command
```

Arguments

command: The Listener Control utility command. Commands are shown in the following example output.

When you enter a command as an argument to `HELP`, the Listener Control utility displays information about how to use the command. When you enter `HELP` without an argument, the Listener Control utility displays a list of all the commands.

Example

```
LSNRCTL> HELP
The following operations are available 
An asterisk (*) denotes a modifier or extended command: 
exit 
quit
reload 
services 
set* 
show*
spawn 
start                          
status 
stop 
trace          
version
```

### QUIT

Purpose

To exit the Listener Control utility and return to the operating system prompt.

Prerequisites

None

Syntax

From the Listener Control utility

```
LSNRCTL> QUIT
```

Arguments

None

Usage Notes

This command is identical to the EXIT command.

Example

```
LSNRCTL> QUIT
```

### RELOAD

Purpose

To reread the `listener.ora` file. This command enables you to add or change statically configured services without actually stopping the listener.

In addition, the database services, instances, service handlers, and listening endpoints that were dynamically registered with the listener are unregistered and subsequently registered again.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl RELOAD listener_name
```

From the Listener Control utility:

```
LSNRCTL> RELOAD listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Example

```
LSNRCTL> RELOAD
Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521)))
The command completed successfully
```

### SAVE\_CONFIG

Purpose

To save the current configuration state of the listener, including trace level, trace file, trace directory, and logging to the `listener.ora` file. Any changes are stored in `listener.ora`, preserving formatting, comments, and case as much as possible. Before modification of the `listener.ora` file, a backup of the file, called `listener.bak`, is created.

Syntax

From the operating system:

```
lsnrctl SAVE_CONFIG listener_name
```

From the Listener Control utility:

```
LSNRCTL> SAVE_CONFIG listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Usage Notes

This command enables you to save all run-time configuration changes to the `listener.ora` file.

Example

```
LSNRCTL> SAVE_CONFIG listener
Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521)))
Saved LISTENER configuration parameters.
Listener Parameter File   /oracle/network/admin/listener.ora
Old Parameter File   /oracle/network/admin/listener.bak
The command completed successfully
```

### SERVICES

Purpose

To obtain detailed information about the database services, instances, and service handlers (dispatchers and dedicated servers) to which the listener forwards client connection requests.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SERVICES listener_name
```

From the Listener Control utility:

```
LSNRCTL> SERVICES listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Usage Notes

The SET DISPLAYMODE command changes the format and the detail level of the output.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for a complete description of `SERVICES` output

Example

This example shows `SERVICES` output in the default display mode. The output shows the following:

- An instance named `sales` belonging to two services, `sales1.us.example.com` and `sales2.us.example.com`, with a total of three service handlers.
- Service `sales1.us.example.com` is handled by one dispatcher only.
- Service `sales2.us.example.com` is handled by one dispatcher and one dedicated server, as specified by in the following output.
```
LSNRCTL> SERVICES
Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=net)))
Services Summary...
Service "sales1.us.example.com" has 1 instance(s).
  Instance "sales", status READY, has 1 handler(s) for this service...
    Handler(s):
      "D000" established:0 refused:0 current:0 max:10000 state:ready
         DISPATCHER <machine: sales-server, pid: 5696>
         (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=53411))
Service "sales2.us.example.com" has 1 instance(s).
  Instance "sales", status READY, has 2 handler(s) for this service...
    Handler(s):
      "DEDICATED" established:0 refused:0 state:ready
         LOCAL SERVER
      "D001" established:0 refused:0 current:0 max:10000 state:ready
         DISPATCHER <machine: sales-server, pid: 5698>
         (ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=52618))
The command completed successfully
```

### SET

Purpose

To alter the parameter values for the listener. Parameter value changes remain in effect until the listener is shut down. To make the changes permanent, use the SAVE\_CONFIG command to save changes to the `listener.ora` file.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET parameter
```

From the Listener Control utility:

```
LSNRCTL> SET parameter
```

Arguments

parameter: A `SET` parameter to modify its configuration setting. Parameters are shown in the example output.

When you enter `SET` without an argument, the Listener Control utility displays a list of all the parameters.

Usage Notes

If you are using the `SET` commands to alter the configuration of a listener other than the default `LISTENER` listener, then use the SET CURRENT\_LISTENER command to set the name of the listener you want to administer.

Example

```
LSNRCTL> SET
The following operations are available with set.
An asterisk (*) denotes a modifier or extended command.
current_listener 
displaymode
inbound_connect_timeout
log_file
log_directory
log_status
rawmode
save_config_on_stop 
trc_file
trc_directory
trc_level
```

### SET CURRENT\_LISTENER

Purpose

To set the name of the listener to administer. Subsequent commands that would normally require `listener_name` can be issued without it.

Syntax

From the Listener Control utility

```
LSNRCTL> SET CURRENT_LISTENER listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Usage Notes

When `SET` `CURRENT_LISTENER` is set, the Listener Control utility commands act on the listener you set. You do not have to specify the name of the listener.

Example

```
LSNRCTL> SET CURRENT_LISTENER lsnr
Current Listener is lsnr
```

### SET DISPLAYMODE

Purpose

To change the format and level of detail for the SERVICES and STATUS commands.

Syntax

From the Listener Control utility:

```
LSNRCTL> SET DISPLAYMODE {compat | normal | verbose | raw}
```

Arguments

Specify one of the following modes:

`compat`: Output that is compatible with older versions of the listener.

`normal`: Output that is formatted and descriptive. Oracle recommends this mode.

`verbose`: All data received from the listener in a formatted and descriptive output.

`raw`: All data received from the listener without any formatting. This argument should be used only if recommended by Oracle Support Services.

Example

```
LSNRCTL> SET DISPLAYMODE normal
Service display mode is NORMAL
```

### SET INBOUND\_CONNECT\_TIMEOUT

Purpose

To specify the time, in seconds, for the client to complete its connect request to the listener after establishing the network connection.

If the listener does not receive the client request in the time specified, then it terminates the connection. In addition, the listener logs the IP address of the client and an `ORA-12525:TNS: listener has not received client's request in time allowed` error message to the `listener.log` file.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for additional information about specifying the time out for client connections

Syntax

From the Listener Control utility:

```
LSNRCTL> SET INBOUND_CONNECT_TIMEOUT time
```

Arguments

time: The time, in seconds. Default setting is 60 seconds.

Example

```
LSNRCTL> SET INBOUND_CONNECT_TIMEOUT 2
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "inbound_connect_timeout" set to 2
The command completed successfully.
```

### SET LOG\_DIRECTORY

Note:

This command works only if Automatic Diagnostic Repository (ADR) is not enabled. The default is for ADR to be enabled, and the log directory is `ORACLE_HOME/log/diag/` `product_type`.

Purpose

To set destination directory where the listener log file is written. By default, the log file is written to the `ORACLE_HOME/network/log` directory.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET LOG_DIRECTORY directory
```

From the Listener Control utility:

```
LSNRCTL> SET LOG_DIRECTORY directory
```

Arguments

directory: The directory path of the listener log file.

Example

```
LSNRCTL> SET LOG_DIRECTORY /usr/oracle/admin 
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "log_directory" set to /usr/oracle/admin
The command completed successfully
```

### SET LOG\_FILE

Note:

This command works only if Automatic Diagnostic Repository (ADR) is not enabled. The default is for ADR to be enabled, and the log directory is `ORACLE_HOME/log/diag/` `product_type`.

Purpose

To set the name for the listener log file. By default, the log file name is `listener.log`.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET LOG_FILE file_name
```

From the Listener Control utility:

```
LSNRCTL> SET LOG_FILE file_name
```

Arguments

file\_name: The file name of the listener log.

Example

```
LSNRCTL> SET LOG_FILE list.log
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "log_file" set to list.log
The command completed successfully
```

### SET LOG\_STATUS

Purpose

To turn listener logging on or off.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET LOG_STATUS {on | off}
```

From the Listener Control utility:

```
LSNRCTL> SET LOG_STATUS {on | off}
```

Arguments

`on`: To turn logging on.

`off`: To turn logging off.

Example

```
LSNRCTL> SET LOG_STATUS on
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "log_status" set to ON
The command completed successfully
```

### SET SAVE\_CONFIG\_ON\_STOP

Purpose

To specify whether changes made to the parameter values for the listener by the SET commands are to be saved to the `listener.ora` file at the time the listener is stopped with the STOP command.

When changes are saved, the Listener Control utility tries to preserve formatting, comments, and letter case. Before modification of the `listener.ora` file, a back up of the file, called `listener.bak`, is created.

To have all parameters saved immediately, use the SAVE\_CONFIG command.

Syntax

From the operating system:

```
lsnrctl SET SAVE_CONFIG_ON_STOP  {on | off}
```

From the Listener Control utility:

```
LSNRCTL> SET SAVE_CONFIG_ON_STOP  {on | off}
```

Arguments

`on`: To save configuration to `listener.ora`.

`off`: To not save configuration to `listener.ora`.

Example

```
LSNRCTL> SET SAVE_CONFIG_ON_STOP on
LISTENER parameter "save_config_on_stop" set to ON
The command completed successfully
```

### SET TRC\_DIRECTORY

Note:

This command works only if Automatic Diagnostic Repository (ADR) is not enabled. The default is for ADR to be enabled, and the log directory is `ORACLE_HOME/log/diag/` `product_type`.

Purpose

To set the destination directory where the listener trace files are written. By default, the trace file are written to the `ORACLE_HOME/network/trace` directory.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET TRC_DIRECTORY directory
```

From the Listener Control utility:

```
LSNRCTL> SET TRC_DIRECTORY directory
```

Arguments

directory: The directory path of the listener trace files.

Example

```
LSNRCTL> SET TRC_DIRECTORY /usr/oracle/admin
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "trc_directory" set to /usr/oracle/admin
The command completed successfully
```

### SET TRC\_FILE

Note:

This command works only if Automatic Diagnostic Repository (ADR) is not enabled. The default is for ADR to be enabled, and the log directory is `ORACLE_HOME/log/diag/` `product_type`.

Purpose

To set the name of the listener trace file. By default, the trace file name is `listener.trc`.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET TRC_FILE file_name
```

From the Listener Control utility:

```
LSNRCTL> SET TRC_FILE file_name
```

Arguments

file\_name: The file name of the listener trace.

Example

```
LSNRCTL> SET TRC_FILE list.trc
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "trc_file" set to list.trc
The command completed successfully
```

### SET TRC\_LEVEL

Purpose

To set a specific level of tracing for the listener.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SET TRC_LEVEL level
```

From the Listener Control utility:

```
LSNRCTL> SET TRC_LEVEL level
```

Arguments

level: One of the following trace levels:

- `off` for no trace output
- `user` for user trace information
- `admin` for administration trace information
- `support` for Oracle Support Services trace information

Usage Notes

This command has the same functionality as the TRACE command.

Example

```
LSNRCTL> SET TRC_LEVEL admin
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
LISTENER parameter "trc_level" set to admin
The command completed successfully
```

### SHOW

Purpose

To view the current parameter values for the listener.

All of the SET parameters have equivalent `SHOW` parameters.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SHOW parameter
```

From the Listener Control utility:

```
LSNRCTL> SHOW parameter
```

Arguments

parameter: A `SHOW` parameter to view its configuration settings. Parameters are shown in the example output.

When you enter `SHOW` without an argument, the Listener Control utility displays a list of all the parameters.

Example

```
LSNRCTL> SHOW
The following properties are available with SHOW:
An asterisk (*) denotes a modifier or extended command:
current_listener 
displaymode
inbound_connect_timeout
log_file
log_directory
log_status
rawmode
save_config_on_stop 
trc_file
trc_directory
trc_level
```

### SPAWN

Purpose

To start a program stored on the computer on which the listener is running, and which is listed with an alias in the `listener.ora` file.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl SPAWN listener_name alias (arguments='arg1,arg2,...')
```

From the Listener Control utility

```
LSNRCTL> SPAWN listener_name alias (arguments='arg1,arg2,...')
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

alias: The alias of the program to be spawned off is specified by a `listener.ora` file entry, similar to the following:

```
alias = (PROGRAM=(NAME=)(ARGS=)(ENVS=))
```

For example:

```
nstest = (PROGRAM=(NAME=nstest)(ARGS=test1)(ENVS='ORACLE_HOME=/usr/oracle'))
```

Example

This program can then be spawned off using the following command:

```
lsnrctl SPAWN listener_name nstest
```

### START

Purpose

To start the named listener.

Prerequisites

Listener must not be running.

Syntax

From the operating system:

```
lsnrctl START listener_name
```

From the Listener Control utility:

```
LSNRCTL> START listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Usage Notes

To start a listener configured in the `listener.ora` file with a name other than `LISTENER`, include that name.

For example, if the listener name is `tcp_lsnr`, enter:

```
lsnrctl START tcp_lsnr
```

From the Listener Control utility:

```
LSNRCTL> START tcp_lsnr
```

Example

```
LSNRCTL> START

Starting /private/sales_group/sales/bin/tnslsnr: please wait...

TNSLSNR for Linux: Version 11.2.0.0.0 
System parameter file is /oracle/network/admin/listener.ora
Log messages written to /oracle/network/log/listener.log
Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)))

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 11.2.0.0.0 
Start Date                15-NOV-2008 18:02:25
Uptime                    0 days 0 hr. 0 min. 0 sec
Trace Level               off
Security                  OFF
SNMP                      OFF
Listener Parameter File   /oracle/network/admin/listener.ora
Listener Log File         /oracle/network/log/listener.log
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)))
The listener supports no services
The command completed successfully
```

### STATUS

Purpose

To display basic status information about a listener, including a summary of listener configuration settings, listening protocol addresses, and a summary of services registered with the listener.

Note:

You can also obtain the status of the listener through the Oracle Enterprise Manager Console. See the [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/toc.htm) for additional information.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl STATUS listener_name
```

From the Listener Control utility:

```
LSNRCTL> STATUS listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Usage Notes

The SET DISPLAYMODE command changes the format and level of the detail of the output.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for a complete description of `STATUS` output

Example

The following example shows `STATUS` output in the default display mode. The output contains:

- Listener configuration settings
- Listening endpoints summary
- Services summary, which is an abbreviated version of the SERVICES command output
```
LSNRCTL> STATUS
Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=net)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 11.2.0.0.0 -
Beta
Start Date                15-JAN-2008 12:02:00
Uptime                    0 days 0 hr. 5 min. 29 sec
Trace Level               support
Security                  OFF
SNMP                      OFF
Listener Parameter File   /oracle/network/admin/listener.ora
Listener Log File         /oracle/network/log/listener.log
Listener Trace File       /oracle/network/trace/listener.trc

Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=net)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=sales-server)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=sales-server)(PORT=2484)))
 
Services Summary...
Service "sales1.us.example.com" has 1 instance(s).
  Instance "sales", status READY, has 1 handler(s) for this service...
Service "sales2.us.example.com" has 1 instance(s).
  Instance "sales", status READY, has 2 handler(s) for this service...
The command completed successfully
```

### STOP

Purpose

To stop the named listener.

Prerequisites

The listener must be running.

Syntax

From the operating system:

```
lsnrctl STOP listener_name
```

From the Listener Control utility:

```
LSNRCTL> STOP listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Example

```
LSNRCTL> STOP
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
The command completed successfully
```

### TRACE

Purpose

To turn on tracing for the listener.

Syntax

From the operating system:

```
lsnrctl trace level listener_name
```

From the Listener Control utility:

```
LSNRCTL> trace level listener_name
```

Arguments

level: One of the following trace levels:

- `off` for no trace output
- `user` for user trace information
- `admin` for administration trace information
- `support` for Oracle Support Services trace information

listener\_name: Specify the listener name, if the default name of `LISTENER` is not used.

Usage Notes

This command has the same functionality as `SET TRC_LEVEL` command.

Example

```
LSNRCTL> TRACE ADMIN lsnr
Connecting to (ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
Opened trace file: /oracle/network/trace/listener.trc
The command completed successfully
```

### VERSION

Purpose

To display the current version of Listener Control utility.

Prerequisites

None

Syntax

From the operating system:

```
lsnrctl VERSION listener_name
```

From the Listener Control utility:

```
LSNRCTL> VERSION listener_name
```

Arguments

listener\_name: The listener name, if the default name of `LISTENER` is not used.

Example

```
LSNRCTL> VERSION listener1
Connecting to ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521))
TNSLSNR for Linux: Version 11.2.0.0.0
        TNS for Linux: Version 11.2.0.0.0 
        Oracle Bequeath NT Protocol Adapter for Linux: Version 11.2.0.0.0
        Unix Domain Socket IPC NT Protocol Adaptor for Linux: Version 11.2.0.0.0 
        TCP/IP NT Protocol Adapter for Linux: Version 11.2.0.0.0
The command completed successfully
```