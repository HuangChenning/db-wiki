---
title: Server Control Utility Reference
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## A Server Control Utility Reference

This appendix includes a complete reference for the Server Control Utility (SRVCTL).

See Also:

[Chapter 3, "Administering Database Instances and Cluster Databases"](admin.md) for more information about using SRVCTL to manage an Oracle RAC database

This appendix includes the following topics:

## Using SRVCTL

This section includes topics that relate to using the SRVCTL utility.

### Overview of SRVCTL

Use SRVCTL to manage configuration information. You can use SRVCTL commands to add, remove, start, stop, modify, enable, and disable a number of entities, such as databases, instances, listeners, SCAN listeners, services, grid naming service (GNS), and Oracle ASM.

Some SRVCTL operations modify the configuration data stored in the Oracle Cluster Registry (OCR). SRVCTL performs other operations, such as starting and stopping instances, by sending requests to the Oracle Clusterware process (CRSD), which then starts or stops the Oracle Clusterware resources.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

### Operational Notes for SRVCTL

SRVCTL is installed on each node by default.

This section discusses the following topics:

- Usage Information
- Character Set and Case Sensitivity of Object Values
- Summary of Tasks for Which SRVCTL Is Used
- Using SRVCTL Help
- Privileges and Security

#### Usage Information

To use SRVCTL, log in to the operating system of a node and enter the SRVCTL command and its options in case-sensitive syntax as described in "SRVCTL Command Reference".

Guidelines for using SRVCTL are:

- Only use the version of SRVCTL that is provided with Oracle Database 11g on Oracle RAC databases that are created or upgraded for Oracle Database 11g. The version of SRVCTL must be the same as the version of the object (listeners, Oracle ASM instances, Oracle RAC databases and their instances, and services) being managed. To ensure the versions are the same release, issue SRVCTL commands from the Oracle home of the database or object you are managing.
- SRVCTL does not support concurrent executions of commands on the same object. Therefore, run only one SRVCTL command at a time for each database, service, or other object.

Using Comma-Delimited Lists

When specifying a comma-delimited list as part of a SRVCTL command, there should not be any spaces between the items in the list. For example:

```
srvctl add database -g serverpool1,serverpool3
```

When you specify a comma-delimited list in a Windows environment, you must enclose the list in double quotation marks (`""`). You can enclose a comma-delimited list in double quotation marks in a Linux or UNIX environment but they will be ignored.

Specifying a Continuation of Command Line Entries

If you are entering a SRVCTL command, and you want to continue the input on a new line, then you can use the operating system continuation character. In Linux, this is the backslash (\\) symbol.

SRVCTL Command Feedback

A SRVCTL command that produces no output is a successful command. Not all SRVCTL commands return a message when it completes, successfully. However, if a SRVCTL command fails, then it always returns an error message.

#### Character Set and Case Sensitivity of Object Values

SRVCTL interacts with many different types of objects. The character set and name length limitations, and whether or not the object name is case sensitive, can vary between object types.

Table A-1 String Restrictions for SRVCTL Object Names

| Object Type | Character Set Limitations | Case Sensitive? | Maximum Length |
| --- | --- | --- | --- |
| ``` db_domain ``` | Alpha-numeric characters, underscore (\_), and number sign (#) |  | 128 characters |
| ``` db_unique_name ``` | Alpha-numeric characters, underscore (\_), number sign (#), and dollar sign ($); the first 8 characters must be unique because those characters are used to form instance names for policy-managed databases | No | 30 characters but the first 8 characters must be unique relative to any other database in the same cluster |
| ``` diskgroup_name ``` | Naming disk groups have the same limitations as naming other database objects.  See Also: [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements008.htm#SQLRF51129) for more information about database object naming rules | No (all names are converted to uppercase) |  |
| ``` instance_name ``` | Alpha-numeric characters | Depends on the platform | 15 characters |
| ``` listener_name ``` |  |  |  |
| ``` node_name ``` |  | No |  |
| ``` scan_name ``` | The first character must be an alphabetic character | No |  |
| ``` server_pool ``` | Alpha-numeric characters, underscore (\_), number sign (#), period (.), and dollar sign ($); the name cannot begin with a period, contain single quotation marks (`''`), nor can the name be "Generic" or "Free" because those two names are reserved for the built-in server pools |  | 250 characters |
| ``` service_name ``` |  |  | 250 characters |
| ``` volume_name ``` | Alphanumeric characters; dashes (-) are not allowed and the first character must be an alphabetic character. | No | 11 characters |

#### Summary of Tasks for Which SRVCTL Is Used

SRVCTL is used to manage databases, instances, cluster databases, cluster database instances, Oracle ASM instance and disk groups, services, listeners, or other clusterware resources.

- Cluster Database Configuration Tasks
	- Add, modify, and delete cluster database configuration information.
		- Add an instance or a service to, and delete an instance or service from the configuration of a cluster database.
		- Move instances and services in a cluster database configuration and modify service configurations.
		- Set and unset the environment for an instance or service in a cluster database configuration.
		- Set and unset the environment for an entire cluster database in a cluster database configuration.
- General Cluster Database Administration Tasks
	- Start and stop cluster databases
		- Start and stop cluster database instances
		- Start, stop, and relocate cluster database services
		- Obtain statuses of cluster databases, cluster database instances, or cluster database services
- Node-Level Tasks
	- Adding and deleting node level applications, server pools, and VIPs
		- Setting and unsetting the environment for node-level applications
		- Administering disk groups
		- Administering server pools
		- Administering node applications
		- Administering Oracle ASM instances
		- Starting and stopping a group of programs that includes virtual IP addresses (VIPs), listeners, and Oracle Notification Services

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD838) for information

#### Using SRVCTL Help

To see help for all SRVCTL commands, from the command line enter:

```
srvctl -h
```

To see the command syntax and a list of options for each SRVCTL command, from the command line enter:

```
srvctl command (or verb) object (or noun) -h
```

To see the SRVCTL version number enter:

```
$ srvctl -V
```

#### Privileges and Security

To use SRVCTL to change your Oracle RAC database configuration, log in to the operating system as the software owner of the home that you want to manage.

For example, if different users installed Oracle Database and the Oracle Grid Infrastructure, then log in as the database software owner (for example, `ora_db`) to manage databases and log in as the Oracle Grid Infrastructure software owner (for example, `ora_asm`) to manage the Oracle ASM instances.

Users who are members of the OSDBA operating system group can start and stop the database. To stop and start an Oracle ASM instance, you must be a member of the OSASM operating system group.

To create or register objects such as listeners, Oracle Notification Services, and services, you must be logged in to the operating system as the software owner of the Oracle home. The objects you create or register for that Oracle home will run under the user account of the owner of the Oracle home. Databases run as the database installation owner of the home from which they run.

To perform `srvctl add` operations on any object, you must be logged in as the Oracle account owner of the home on which the object runs.

For some SRVCTL commands, on Linux and UNIX systems, you must be logged in as `root`, and on Windows systems, you must be logged in as a user with Administrator privileges to run them. In this appendix, those commands are preceded by the `root` prompt (`#`) in the command examples.

### Additional Topics on SRVCTL

Difference between Using SRVCTL and CRSCTL

Use SRVCTL to manage Oracle-supplied resources such as listener, instances, disk groups, and networks, and CRSCTL for managing Oracle Clusterware and its resources.

Note:

Oracle strongly discourages directly manipulating Oracle-supplied resources (resources whose names begin with ora) using CRSCTL. This could adversely impact the cluster configuration.

Stopping Active SRVCTL Commands

Although you may be able to cancel running SRVCTL commands by pressing the Control-C keys, you may corrupt your configuration data by doing this.

You are strongly advised not to attempt to terminate SRVCTL in this manner.

### Deprecated Subprograms or Commands

The following command options have been deprecated for Oracle Database 11g release 2 (11.2):

Table A-2 Deprecated Commands and Options for SRVCTL

| Command | Deprecated Options |
| --- | --- |
| ``` srvctl add asm ``` | ``` -n node_name ``` ``` -i instance_name ``` ``` -o Oracle_home ``` ``` -p spfile ``` |
| ``` srvctl add database ``` | ``` -A {name \| IP_address}/netmask ``` |
| ``` srvctl add listener ``` | ``` -n node_name ``` |
| ``` srvctl config database ``` | ``` -t ``` |
| ``` srvctl config listener ``` | ``` -n node_name ``` |
| ``` srvctl config nodeapps ``` | ``` -n node_name ``` ``` -l ``` |
| ``` srvctl config asm ``` | ``` -i instance_name ``` |
| ``` srvctl disable nodeapps ``` | ``` -n node_name ``` |
| ``` srvctl enable asm ``` | ``` -i instance_name ``` |
| ``` srvctl enable nodeapps ``` | ``` -n node_name ``` |
| ``` srvctl getenv instance ``` | ``` -d db_unique_name ``` ``` -i instance_name ``` ``` -t "name=val_list" ``` |
| ``` srvctl getenv nodeapps ``` | ``` -n node_name ``` |
| ``` srvctl getenv service ``` | ``` -d db_unique_name ``` ``` -s service_name ``` ``` -t "name=val_list" ``` |
| ``` srvctl modify asm ``` | ``` -o Oracle_home ``` |
| ``` srvctl modify instance ``` | ``` -s asm_inst_name ``` ``` -r ``` |
| ``` srvctl remove asm ``` | ``` -n node_name ``` ``` -i instance_name ``` |
| ``` srvctl remove listener ``` | ``` -n node_name ``` |
| ``` srvctl remove nodeapps ``` | ``` -n "node_name_list" ``` |
| ``` srvctl setenv instance ``` | ``` -d db_unique_name ``` ``` -i instance_name ``` ``` -t "name=val_list" ``` ``` -T "name=val" ``` |
| ``` srvctl setenv nodeapps ``` | ``` -n node_name ``` |
| ``` srvctl setenv service ``` | ``` -d db_unique_name ``` ``` -s service_name ``` ``` -t "name=val_list" ``` ``` -T "name=val" ``` |
| ``` srvctl start asm ``` | ``` -i instance_name ``` |
| ``` srvctl status instance ``` | ``` -S level ``` |
| ``` srvctl status nodeapps ``` | ``` -n node_name ``` |
| ``` srvctl stop asm ``` | ``` -i instance_name ``` |
| ``` srvctl unsetenv instance ``` | ``` -d db_unique_name ``` ``` -i instance_name ``` ``` -t "name=val_list" ``` |
| ``` srvctl unsetenv nodeapps ``` | ``` -n node_name ``` |
| ``` srvctl unsetenv service ``` | ``` -d db_unique_name ``` ``` -s service_name ``` ``` -t "name=val_list" ``` |

## SRVCTL Command Reference

SRVCTL Command Syntax and Options

SRVCTL commands, object names, and options are case sensitive. Database, instance, listener, and service names are case insensitive and case preserving. You cannot create listener names that differ only in case, such as LISTENER and listener. SRVCTL uses the following command syntax:

```
srvctl command object [options]
```

In SRVCTL syntax:

- `command` is a verb such as `start`, `stop`, or `remove`
- `object` is the target or object on which SRVCTL performs the command, such as database or instance. You can also use object abbreviations.
- `options` extend the use of a preceding command combination to include additional parameters for the command. For example, the `-i` option indicates that a comma-delimited list of preferred instance names follows; sometimes the `-i` option only permits one value and not a list of names. The `-n` option indicates that a node name or a comma-delimited list of node names follows. Do not use spaces between the items in a comma-delimited list.

Note:

If specifying a comma-delimited list in Windows, then you must enclose the list within double quotation marks (`""`).

Table A-3 Summary of SRVCTL Commands

| Command | Description |
| --- | --- |
| `add` | Adds node applications, databases, database instances, Grid Naming Service (GNS), listeners, single client access names (SCANs), Oracle ASM instances, server pools, services, or virtual IPs (VIPs). |
| `config` | Lists the configuration for GNS, the node applications, database, Oracle ASM instance, or service. |
| `convert` | Converts a database either to or from an Oracle Real Application Clusters One Node (Oracle RAC One Node) database. |
| `disable` | Disables the database, database instance, GNS, Oracle ASM instance, or service. |
| `downgrade` | Downgrades the database configuration after you manually downgrade the database. |
| `enable` | Enables the database, database instance, GNS, Oracle ASM instance, or service. |
| `getenv` | Displays the environment variable in the configuration for the node applications, database, VIP, listener or Oracle ASM. |
| `modify` | Modifies the node applications, database, database instance, GNS, or service configuration. |
| `relocate` | Relocates GNS, OC4J, SCANs, Oracle RAC One Node databases, servers, and VIPs from one node to another. |
| `remove` | Removes the node applications, database, database instance, GNS, Oracle ASM instance, or service. |
| `setenv` | Sets the environment variable in the configuration for the node applications, database, VIP, listener or Oracle ASM. |
| `start` | Starts the node applications, database, database instance, GNS, Oracle ASM instance, or service. |
| `status` | Displays the status of the node applications, database, database instance, GNS, Oracle ASM instance, or service. |
| `stop` | Stops the node applications, database, database instance, GNS, Oracle ASM instance, or service. |
| `unsetenv` | Unsets the environment variable in the configuration for the node applications, database, VIP, listener or Oracle ASM. |
| `upgrade` | Upgrades the configuration to the version of the software on which it is running. |

SRVCTL Objects Summary

Table A-4 lists the keywords that can be used for the `object` portion of SRVCTL commands. You can use either the full name or the abbreviation for each object keyword. The Purpose column describes the object and the actions that can be performed on that object.

Table A-4 Object Keywords and Abbreviations

| Object | Keyword | Purpose |
| --- | --- | --- |
| Cluster Verification Utility | `cvu` | To add, modify, list the configuration of, enable, disable, start, stop, relocate, obtain the status of, and remove CVU resources. |
| Database | `database` | To add, modify, manage environment variables for, list the configuration of, enable, disable, start, stop, and obtain the status of databases, and also to upgrade, downgrade, and remove database configuration information about databases. |
| Disk Group | `diskgroup` | To add, modify, list the configuration of, enable, disable, start, stop, obtain the status of, and remove Oracle ASM disk groups |
| File system | `filesystem` | To add, modify, list the configuration of, enable, disable, stop, start, obtain the status of, and remove disk devices for Oracle Automatic Storage Management Cluster File System (Oracle ACFS). |
| Grid Naming Service (GNS) | gns | To add, modify, list the configuration of, enable, disable, stop, start, obtain the status of, and remove a GNS daemon. |
| Home directory (for patching) | `home` | To start, stop, and obtain the status of all clusterware resources related to a Home directory.f |
| Instance | `instance` | To add, modify, enable, disable, start, stop, obtain the status of, and remove database instances. |
| Listener | `listener` | To add, modify, manage environment variables for, list the configuration of, enable, disable, start, stop, obtain the status of, and remove listeners. |
| Network | `network` | To add, modify, list the configuration of, and remove a non-default Network.  Note: The node applications object, and the `config` and `modify` commands also manage the default network. |
| Node applications | `nodeapps` | To add, modify, manage environment variables for, list the configuration of, enable, disable, start, stop, obtain the status of, and remove node applications. |
| Oracle Automatic Storage Management | `asm` | To add, modify, manage environment variables for, list the configuration of, enable, disable, start, stop, obtain the status of, and remove Oracle ASM instances. |
| Oracle Grid Foundation OC4J container | `oc4j` | To add, modify, list the configuration of, enable, disable, start, stop, relocate, obtain the status of, and remove OC4J instances |
| Oracle Notification Service | `ons` | To add, configure, enable, start, obtain the status of, stop, disable, and remove Oracle Notification Service instances for Oracle Restart |
| Single client access name (SCAN) | `scan` | To add, list the configuration of, modify, enable, disable, start, stop, relocate, obtain the status of, and remove SCAN VIPs |
| SCAN listener | `scan_listener` | To add, list the configuration of, modify, enable, disable, start, stop, relocate, obtain the status of, and remove SCAN listeners |
| Server pool | `srvpool` | To add, modify, list the configuration of, obtain the status of, and remove server pools |
| Service | `service` | To add, modify, list the configuration of, enable, disable, start, stop, obtain the status of, relocate, and remove services |
| Virtual IP | VIP | To add, manage environment variables for, list the configuration of, enable, disable, start, stop, obtain the status of, and remove a VIP |

### add

The `srvctl add` command adds the configuration and the Oracle Clusterware applications to OCR for the cluster database, named instances, named services, or for the named nodes. To perform `srvctl add` operations, you must be logged in as the database administrator and be the Oracle account owner on Linux and UNIX systems, or you must be logged on as a user with Administrator privileges on Windows systems.

When adding an instance, the name that you specify with `-i` must match the `ORACLE_SID` parameter. The database name given with `-d db_unique_name` must match the `DB_UNIQUE_NAME` initialization parameter setting. If `DB_UNIQUE_NAME` is unspecified, then match the `DB_NAME` initialization parameter setting. The default setting for `DB_UNIQUE_NAME` uses the setting for `DB_NAME`. Also, the domain name given with `-m db_domain` must match the `DB_DOMAIN` setting.

Table A-5 srvctl add Summary

| Command | Description |
| --- | --- |
| `srvctl add asm` | Adds Oracle ASM instances |
| `srvctl add cvu` | Adds the Cluster Verification Utility resource to an Oracle Clusterware configuration |
| `srvctl add database` | Adds a database and configuration |
| `srvctl add filesystem` | Adds a volume to Oracle ACFS |
| `srvctl add gns` | Adds the Grid Naming Service (GNS) to a cluster |
| `srvctl add instance` | Adds one or more instance and configuration |
| `srvctl add listener` | Adds a listener to the node |
| `srvctl add network` | Adds a DHCP or static network |
| `srvctl add nodeapps` | Adds node applications |
| `srvctl add oc4j` | Adds OC4J instances |
| `srvctl add ons` | Adds Oracle Notification Service daemons |
| `srvctl add scan` | Adds SCAN VIPs |
| `srvctl add scan_listener` | Adds SCAN listeners |
| `srvctl add service` | Adds services |
| `srvctl add srvpool` | Adds a server pool to a cluster |
| `srvctl add vip` | Adds a VIP to a node |

#### srvctl add asm

Adds a record for an Oracle ASM instance to the entire cluster. This command needs to be run only one time from the Oracle Grid Infrastructure home.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl add asm` command with the following syntax:

```
srvctl add asm [-l listener_name
]
```

This command has only one option, `-l`, which calls for the name of a listener. If you do not specify this option, then the listener name defaults to `LISTENER`.

##### Example

To add a clusterware resource for Oracle ASM on every node in the cluster, use the following command:

```
srvctl add asm
```

#### srvctl add cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command adds the [Cluster Verification Utility (CVU)](rac_glossary.md) to an Oracle Clusterware configuration.

##### Syntax and Options

Use the `srvctl add cvu` command with the following syntax:

```
srvctl add cvu [-t check_interval_in_minutes]
```

Table A-6 srvctl add cvu Options

| Option | Description |
| --- | --- |
| ``` -t check_interval_in_minutes ``` | By default, CVU runs once every 6 hours and verifies the health of cluster. The shortest interval you can specify for CVU check is 10 minutes. |

##### Examples

An example of this command to add CVU with a check interval of 6 hours is:

```
$ srvctl add cvu -t 360
```

#### srvctl add database

Adds a database configuration to your cluster database configuration.

##### Syntax and Options

Use the `srvctl add database` command with the following syntax:

```
srvctl add database -d db_unique_name
 -o oracle_home

     [-x node_name] [-m domain_name
] [-p spfile
]
     [-c  {RACONENODE | RAC | SINGLE} [-e server_list] [-i instance_name] [-w timeout]]
     [-r {PRIMARY | PHYSICAL_STANDBY | LOGICAL_STANDBY | SNAPSHOT_STANDBY}]
     [-s start_options
] [-t stop_options] [-n db_name
 -j "acfs_path_list"]
     [-y {AUTOMATIC | MANUAL | NORESTART}] [-g server_pool_list] [-a disk_group_list]
```

Table A-7 srvctl add database Options

| Syntax | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database. |
| ``` -o oracle_home ``` | The path for the Oracle database home directory. |
| ``` -x node_name ``` | Node name on which you want to register a noncluster Oracle database.  Note: This option is available only with Oracle Clusterware and can be used with the `-g` option to create a policy-managed, noncluster database. |
| ``` -m db_domain ``` | The domain for the database  Note: You must use this option if you set the `DB_DOMAIN` initialization parameter set for the database. |
| ``` -p spfile ``` | The path name of the database server parameter file. |
| ``` -c {RACONENODE \| RAC \| SINGLE} ``` | (version 11.2.0.2 or higher) The type of database you are adding: Oracle RAC One Node, Oracle RAC, or single instance. The default is `RAC` unless you specify the `-x` `node_name` option, and the `-c` option defaults to `SINGLE`. |
| ``` -e server_list ``` | (version 11.2.0.2 or higher) List candidate servers for Oracle RAC One Node databases.  Notes: You can use this option only with administrator-managed Oracle RAC One Node databases. If your Oracle RAC One Node database is policy managed, you cannot use this option. |
| ``` -i instance_name ``` | (version 11.2.0.2 or higher) Instance name prefix for Oracle RAC One Node databases. The default value for this option is the first 12 characters of the global unique name of the database.  Notes: You can use this option only with administrator-managed Oracle RAC One Node databases. If your Oracle RAC One Node database is policy managed, you cannot use this option. |
| ``` -w timeout ``` | (version 11.2.0.2 or higher) Online database relocation timeout, in minutes, for Oracle RAC One Node databases. The default is `30`. |
| ``` -r {PRIMARY \| PHYSICAL_STANDBY \|  LOGICAL_STANDBY \|  SNAPSHOT_STANDBY} ``` | The role of the database in an Oracle Data Guard configuration. The default is `PRIMARY`.  See Also: [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/concepts.htm#SBYDB4701) for more information about database roles |
| ``` -s start_options ``` | Startup options for the database, such as `OPEN`, `MOUNT`, and `NOMOUNT`. The default value is `OPEN`.  Note: For multi-word startup options, such as `read only` and `read write`, separate the words with a space and enclose in double quotation marks (`""`). For example, `"read only"`.  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for more information about startup options |
| ``` -t stop_options ``` | Stop options for the database, such as `NORMAL`, `TRANSACTIONAL`, `IMMEDIATE`, and `ABORT`  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm#SQPUG125) for more information about shutdown options |
| ``` -n db_name ``` | The name of the database, if it is different from the unique name given by the `-d` option |
| ``` -j "acfs_path_list" ``` | A single Oracle ACFS path or a comma-delimited list of Oracle ACFS paths enclosed in double quotation marks (`""`) where the database's dependency is set.  Use this option to create dependencies on Oracle ACFS file systems other than `ORACLE_HOME`, such as for when the database uses `ORACLE_BASE` on a file system that is different from the `ORACLE_HOME` file system. |
| ``` -y {AUTOMATIC \| MANUAL \|  NORESTART} ``` | Management policy for the database.  - `AUTOMATIC` (default): The database is automatically restored to its previous running condition (started or stopped) upon restart of the database host computer. - `MANUAL`: The database is never automatically restarted upon restart of the database host computer. A `MANUAL` setting does not prevent Oracle Clusterware from monitoring the database while it is running and restarting it if a failure occurs. - `NORESTART`: Starting with Oracle Database 11g Release 2 (11.2.0.3), you can use the `NORESTART` value. Similar to the `MANUAL` setting, the database is never automatically restarted upon restart of the database host computer. A `NORESTART` setting, however, never restarts the database even if a failure occurs. |
| ``` -g "server_pool_list" ``` | Comma-delimited list of server pool names used to control database placement. If you do not specify this option, then it defaults to the Generic server pool.  Note: This option is available only with Oracle Clusterware and cannot be used with the `-x` option. |
| ``` -a "disk_group_list" ``` | Comma-delimited list of Oracle ASM disk groups if database uses Oracle ASM storage |

##### Examples

An example of this command to add a policy-managed database is:

```
srvctl add database -d crm -o /u01/oracle/product/112/mydb -m foo.com
     -p +diskgroup1/crm/spfilecrm.ora -r PHYSICAL_STANDBY -s MOUNT -t NORMAL
     -n database2 -y MANUAL -g svrpool1,svrpool2 -a "diskgroup1,diskgroup2"
```

An example of this command to add an administrator-managed database is:

```
srvctl add database -d crm -o /u01/oracle/product/112/mydb -m foo.com
```

#### srvctl add filesystem

Adds a disk device to Oracle ACFS. This command needs to be run only one time from the Oracle Grid Infrastructure home.

An Oracle ACFS file system resource is typically created for use with application resource dependency lists. For example, if an Oracle ACFS file system is configured for use as an Oracle Database home, then a resource created for the file system can be included in the resource dependency list of the Oracle Database application. This will cause the file system and stack to be automatically mounted as a result of the start action of the database application.

Note:

To manage Oracle ACFS on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ACFS.

##### Syntax and Options

Use the `srvctl add filesystem` command with the following syntax:

```
srvctl add filesystem -d volume_device
 -v volume_name
 -g diskgroup_name

                      [-m mountpoint_path
] [-u user_name
]
```

Note:

This command is only available with Oracle Clusterware.

Table A-8 srvctl add filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device ``` | The volume device path. |
| ``` -v volume_name ``` | The name of the volume. |
| ``` -g diskgroup_name ``` | The name of the Oracle ACFS disk group to which the device should be added. |
| ``` -m mountpoint_path ``` | The mount point path name for the disk device. This must be an absolute path.  Note: If the file system is not currently mounted, then you must use this parameter. |
| ``` -u user_name ``` | The name of the user authorized to mount and unmount the filesystem. |

##### Example

An example of this command is the following:

```
srvctl add filesystem -d /dev/asm/d1volume1-295 -v VOLUME1 -g RAC_DATA \
  -m /oracle/cluster1/acfs1
```

#### srvctl add gns

Use this command to add the Grid Naming Service (GNS) to a cluster when you are using a DHCP public network.

##### Syntax and Options

Use the `srvctl add gns` command with the following syntax:

```
srvctl add gns -i ip_address -d domain
```

Note:

This command is only available with Oracle Clusterware.

Table A-9 srvctl add gns Options

| Option | Description |
| --- | --- |
| ``` -i ip_address ``` | The Virtual IP (VIP) address on which GNS is to listen for DNS requests |
| ``` -d domain ``` | The network subdomain that is used for Forward DNS Lookup of cluster IP addresses |

##### Example

An example of this command is:

```
srvctl add gns -i 192.168.16.17 -d cluster.mycompany.com
```

#### srvctl add instance

Adds a configuration for an instance to your cluster database configuration.

You can only use this command for administrator-managed databases. If you have a policy-managed database, then use the `srvctl modify srvpool` command to add an instance to increase either the maximum size, minimum size, or both, of the server pool used by the database.

##### Syntax and Options

Use the `srvctl add instance` command with the following syntax:

```
srvctl add instance -d db_unique_name
 -i instance_name
 -n node_name
```

Notes:

- This command increments the `CARDINALITY` resource attribute.
- This command is only available with Oracle Clusterware and Oracle RAC.
- If you attempt to use this command on an Oracle RAC One Node database, then the command returns an error stating you must convert the database to Oracle RAC.

Table A-10 srvctl add instance Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | The unique name of the database you are adding the instance to |
| ``` -i instance_name ``` | The name of the instance you are adding |
| ``` -n node_name ``` | The name of the node on which you are creating the instance |

##### Examples

Examples of this command are:

```
$ srvctl add instance -d crm -i  crm01 -n gm01
$ srvctl add instance -d crm -i  crm02 -n gm02
$ srvctl add instance -d crm -i  crm03 -n gm03
```

#### srvctl add listener

Adds a listener to every node in a cluster.

##### Syntax and Options

Use the `srvctl add listener` command with the following syntax:

```
srvctl add listener [-l listener_name] [-o Oracle_home] 
    [-p "[TCP:]port_list[/IPC:key][/NMP:pipe_name][/TCPS:s_port][/SDP:port]"]
    [-k network_number] [-s]
```

Table A-11 srvctl add listener Options

| Option | Description |
| --- | --- |
| ``` -l listener_name ``` | Specify a listener name.  If this option is not specified, the default name of LISTENER is used. |
| ``` -o oracle_home ``` | Specify an Oracle home for the cluster database.  If you do not include this option, then it uses the Grid home by default. |
| ``` -p "[TCP:]port_list [/IPC:key] [/NMP:pipe_name] [/TCPS:s_port] [/SDP:port] ``` | Protocol specifications for the listener. `port_list` is a comma-delimited list of TCP ports or listener endpoints. |
| ``` -k network_number ``` | The optional network number from which VIPs are obtained. If not specified, the VIPs are obtained from the same default network from which the `nodeapps` VIP is obtained. |
| ``` -s ``` | Indicates you want to skip the checking of ports |

##### Example

The following command adds a listener named `listener112` that is listening on port 1341 and runs from the `/ora/ora112` home directory on every node in the cluster:

```
$ srvctl add listener -l listener112 -p 1341 -o /ora/ora112
```

#### srvctl add network

Adds a DHCP or static network. If your server connects to more than one network, then you can use this command to configure an additional network interface for Oracle RAC, allowing you to create VIPs on multiple public networks. You can also use the `LISTENER_NETWORKS` database initialization parameter to control client redirects to the appropriate network

Note:

Oracle only supports DHCP-assigned networks for the default network, not for subsequent networks.

##### Syntax and Options

Use the `srvctl add network` command with the following syntax:

```
srvctl add network [-k net_number] -S subnet/netmask[/if1[|if2|...]]
  [-w network_type] [-v]
```

Table A-12 srvctl add network Options

| Option | Description |
| --- | --- |
| ``` -k net_number ``` | Specify a network number. The default is 1. |
| ``` -S subnet/netmask [/if1[\|if2\|...]] ``` | Creates a subnet, the type of which you specify with the `-w` option. If you do not specify any interface names, then the network uses any interface on the given subnet. |
| ``` -w network_type ``` | Specify the network type: `static`, `dhcp`, or `mixed`. |
| ``` -v ``` | Verbose output. |

##### Example

An example of this command is:

```
$ srvctl add network -k 3 -S 1.2.3.4/255.255.255.0
```

#### srvctl add nodeapps

Adds a node application configuration to the specified node.

##### Syntax and Options

Use the `srvctl add nodeapps` command with one the following syntax models:

```
srvctl add nodeapps -n node_name
 -A {name | ip}/netmask[/if1[|if2|...]]
  [-e em_port] [-l ons_local_port] [-r ons_remote-port]
  [-t host[:port][,host[:port],...]] [-v]
```
```
srvctl add nodeapps -S subnet/netmask[/if1[|if2|...]] [-e em_port]
  [-l ons_local_port] [-r ons_remote-port]
  [-t host[:port][,host[:port],...]] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-13 srvctl add nodeapps Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of the node on which you want to create the node application. Node name is optional and unnecessary if you run the command on the local node. |
| ``` -A {name \| ip} /netmask[/if1 \|[if2\|...]] ``` | This specification creates a traditional VIP node application on the specified node.  Note: This option must be used for upgrade configurations and new, non-DHCP configurations. |
| ``` -S subnet/netmask [/if1 [\| if2 \|...]] ``` | Creates a DHCP subnet. If you do not specify any interface names, then the VIPs use any interface on the given subnet. |
| ``` -e em_port ``` | Local port on which Oracle Enterprise Manager listens. The default port is 2016. |
| ``` -l ons_local_port ``` | The Oracle Notification Service daemon listener port on its node.  If you do not specify this value, the Oracle Notification Service daemon listener port defaults to 6100.  Note: The local port and remote port must each be unique. |
| ``` -r ons_remote_port ``` | The port number for remote Oracle Notification Service daemon connections.  If you do not specify a port number, the default value of 6200 is used for the Oracle Notification Service remote port.  Note: The local port and remote port must each be unique. |
| ``` -t host[:port], [host[:port],[...] ``` | A list of `host``:``port` pairs of remote hosts that are part of the Oracle Notification Service network but are not part of the Oracle Clusterware cluster  Note: If `port` is not specified for a remote host, then `ons_remote_port` is used. |
| ``` -v ``` | Verbose output |

Note:

On Linux and UNIX systems, you must be logged in as `root` and on Windows, you must be logged in as a user with Administrator privileges to run this command.

##### Example

An example of this command is:

```
# srvctl add nodeapps -n crmnode1 -A 1.2.3.4/255.255.255.0
```

#### srvctl add oc4j

Adds an OC4J instance to all the nodes in the cluster.

##### Syntax and Options

```
srvctl add oc4j [-v]
```

This command has only one option, `-v`, which displays verbose output.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
srvctl add oc4j
```

#### srvctl add ons

Adds an Oracle Notification Service daemon to an Oracle Restart configuration.

Note:

This command is only available with Oracle Restart.

##### Syntax and options

```
srvctl add ons [-l ons_local_port] [-r ons_remote_port] 
    [-t host[:port][,host[:port]][...]] [-v]
```

Table A-14 srvctl add ons Options

| Option | Description |
| --- | --- |
| ``` -l ons_local_port ``` | The Oracle Notification Service daemon listening port for local client connections  Note: The local port and remote port must each be unique. |
| ``` -r ons_remote_port ``` | The Oracle Notification Service daemon listening port for connections from remote hosts  Note: The local port and remote port must each be unique. |
| ``` -t host[:port][,host[:port]][...] ``` | A list of comma-delimited `host``:``port` pairs of remote hosts that are part of the Oracle Notification Service network but are not part of the Oracle Clusterware cluster  Note: If `port` is not specified for a remote host, then `ons_remote_port` is used. |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl add ons -l 6200
```

#### srvctl add scan

Adds Oracle Clusterware resources for the given SCAN. This command creates the same number of SCAN VIP resources as the number of IP addresses that SCAN resolves to, or 3 when `network_number` identifies a DHCP network and Oracle GNS configuration.

##### Syntax and Options

Use the `srvctl add scan` command with the following syntax:

```
srvctl add scan -n scan_name [-k network_number]
  [-S subnet/netmask[/if1[|if2|...]]]
```

Note:

This command is only available with Oracle Clusterware.

Table A-15 srvctl add scan Options

| Option | Description |
| --- | --- |
| ``` -n scan_name ``` | A fully qualified host name, which includes the domain name. |
| ``` -k network_number ``` | The optional network number from which SCAN VIPs are obtained. If not specified, the SCAN VIPs are obtained from the same default network from which the `nodeapps` VIP is obtained. |
| ``` -S subnet/netmask [/if1 [\|if2\|...]] ``` | Creates the `network_number`. This option must be specified when `network_number` does not exist. |

##### Example

An example of this command is:

```
# srvctl add scan -n scan.mycluster.example.com
```

#### srvctl add scan\_listener

Adds Oracle Clusterware resources to the SCAN listeners. The number of SCAN listener resources created is the number of SCAN VIP resources.

##### Syntax and Options

Use the `srvctl add scan_listener` command with the following syntax:

```
srvctl add scan_listener [-l lsnr_name_prefix] [-s]
  [-p "[TCP:]port_list
[/IPC:key
][/NMP:pipe_name
][/TCPS:s_port
] [/SDP:port
]"]
```

Note:

This command is only available with Oracle Clusterware.

Table A-16 srvctl add scan\_listener Options

| Option | Description |
| --- | --- |
| ``` -l lsnr_name_prefix ``` | The SCAN listener name prefix. |
| ``` -s ``` | Use the `-s` option to skip checking of the ports. |
| ``` -p "[TCP:]port_list  [/IPC:key ][/NMP:pipe_name ] [/TCPS:s_port ] [/SDP:port ]" ``` | Protocol specifications for the listener. `port_list` is a comma-delimited list of TCP ports or listener endpoints.  If this option is not specified, then the default TCP port of 1521 is used. |

##### Example

An example of this command is:

```
# srvctl add scan_listener -l myscanlistener
```

#### srvctl add service

Adds services to a database and assigns them to instances. If you have multiple instances of a cluster database on the same node, then always use only one instance on that node for all of the services that node manages.

Note:

The `srvctl add service` command does not accept placement options for Oracle RAC One Node databases.

##### Syntax and Options

Use the `srvctl add service` command to create a service, using the first of the following syntax models, or to update an existing service, using the second syntax model:

```
srvctl add service -d db_unique_name
 -s service_name
 {-r "preferred_list
"
   [-a "available_list
"] [-P {BASIC | NONE | PRECONNECT}] | -g server_pool
   [-c {UNIFORM | SINGLETON]} [-k network_number]
   [-l [PRIMARY | PHYSICAL_STANDBY | LOGICAL_STANDBY | SNAPSHOT_STANDBY]
   [-y {AUTOMATIC | MANUAL}] [-q {TRUE | FALSE}] [-x {TRUE | FALSE}]
   [-j {SHORT | LONG}][-B {NONE | SERVICE_TIME | THROUGHPUT}]
   [-e {NONE | SESSION | SELECT}] [-m {NONE | BASIC}] [-z failover_retries]
   [-w failover_delay]
```
```
srvctl add service -d db_unique_name
 -s service_name

   -u {-r preferred_list
 | -a available_list
} [-f]
```

Table A-17 lists and describes all the `srvctl add service` options and whether they can be used when adding a service to a noncluster or Oracle RAC database.

Table A-17 srvctl add service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database. |
| ``` -s service_name ``` | The `service_name``.``service_domain` should be unique within the cluster unless you want to spread connections across multiple databases that offer the same service. If you do not specify the service domain as part of the service name (such as `sales.foo.com`), then the `DB_DOMAIN` database attribute is the default. |
| ``` -r preferred_list ``` | A list of preferred instances on which the service runs when the database is administrator managed.  The list of preferred instances must be mutually exclusive with the list of available instances.  Note: This option is available only with Oracle RAC and only for administrator-managed databases. |
| ``` -a available_list ``` | A list of available instances to which the service fails over when the database is administrator managed.  The list of available instances must be mutually exclusive with the list of preferred instances.  Note: This option is available only with Oracle RAC and only for administrator-managed databases. |
| ``` -P {BASIC \| NONE \| PRECONNECT} ``` | TAF policy specification (for administrator-managed databases only).  Notes:  - You can only use `PRECONNECT` when you specify the `-r` and `-a` options. - For administrator-managed databases, you cannot set the client-side TAF policy to `PRECONNECT`. |
| ``` -g server_pool ``` | The name of a server pool used when the database is policy managed.  Note: This option is available only with Oracle RAC and only for policy-managed databases. |
| ``` -c {UNIFORM \| SINGLETON} ``` | The cardinality of the service, either `UNIFORM` (offered on all instances in the server pool) or `SINGLETON` (runs on only one instance at a time).  Notes:  - This option is available only with Oracle RAC and only for policy-managed databases. - For policy-managed Oracle RAC One Node databases, all services must be `SINGLETON`. |
| ``` -k network_number ``` | Use this option to determine on which network this service is offered. The service is configured to depend on VIPs from the specified network.  Note: This option is available only with Oracle RAC and Oracle RAC One Node database configurations. |
| ``` -l {[PRIMARY] \| [PHYSICAL_STANDBY] \| [LOGICAL_STANDBY] \| [SNAPSHOT_STANDBY]} ``` | The service role.  Use this option to indicate that the service should only be automatically started upon database open when the Oracle Data Guard database role matches one of the specified service roles.  Using SRVCTL to manually start a service is not affected by the service role.  Note: The `-l` parameter is only used at database startup and by the Oracle Data Guard Broker. All manual service startup must specify the name of the service to be started by the user.  See Also:  - [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/sofo.htm#DGBKR3548) if you specify `-l` - [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/concepts.htm#SBYDB4701) for more information about database roles |
| ``` -y {AUTOMATIC \| MANUAL} ``` | Service management policy.  If `AUTOMATIC` (the default), then the service is automatically started upon restart of the database, either by a planned restart (with SRVCTL) or after a failure. Automatic restart is also subject to the service role, however (the `-l` option).  If `MANUAL`, then the service is never automatically restarted upon planned restart of the database (with SRVCTL). A `MANUAL` setting does not prevent Oracle Clusterware from monitoring the service when it is running and restarting it if a failure occurs.  Note: Using CRSCTL to stop and start the Oracle Clusterware restarts the service in the same way that a failure does. |
| ``` -q {TRUE \| FALSE} ``` | Indicates whether AQ HA notifications should be enabled (`TRUE`) for this service. |
| ``` -x {TRUE \| FALSE} ``` | Indicates whether or not Distributed Transaction Processing should be enabled for this service. This service will either be a singleton service in a policy-managed database or a preferred service on a single node in an administrator-managed database.  Note: This option is available only with Oracle RAC. |
| ``` -j {SHORT \| LONG} ``` | Assign a connection load balancing goal to the service: `SHORT` if using an integrated connection pool, `LONG` for long running connections that you want balanced by the number of sessions per node for the service |
| ``` -B {NONE \| SERVICE_TIME \| THROUGHPUT} ``` | Goal for the Load Balancing Advisory. |
| ``` -e {NONE \| SESSION \| SELECT} ``` | Failover type. |
| ``` -m {NONE \| BASIC} ``` | Failover method.  If the failover type (`-e`) is set to a value other than `NONE`, then you should choose `BASIC` for this option.  Note: This option is available only with Oracle RAC. |
| ``` -z failover_retries ``` | The number of failover retry attempts. |
| ``` -w failover_delay ``` | The time delay between failover attempts. |
| ``` -u ``` | Add a new preferred or available instance to an existing service configuration. |
| ``` -f ``` | Force the add operation even though a listener is not configured for the network. |

##### Examples

Use this example syntax to add the `gl.example.com` service to the `my_rac` database with AQ HA notifications enabled, a failover method of `BASIC`, a Connection Load Balancing Goal of `LONG`, a failover type of `SELECT`, and 180 failover retries with a delay of 5:

```
srvctl add service -d my_rac -s gl.example.com -m BASIC -e SELECT \
-z 180 -w 5 -j LONG
```

Use this example syntax to add a named service to a database with preferred instances in list one and available instances in list two, using preconnect failover for the available instances:

```
srvctl add service -d crm -s sales -r crm01,crm02 -a crm03 -P PRECONNECT
```

#### srvctl add srvpool

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list

Adds a server pool that is configured to host Oracle databases to a cluster.

##### Syntax and Options

Use the `srvctl add srvpool` command with the following syntax:

```
srvctl add srvpool -g server_pool [-i importance] [-l min_size] [-u max_size]
     [-n "node_list"] [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-18 srvctl add srvpool Options

| Option | Description |
| --- | --- |
| ``` -g server_pool ``` | The name of the server pool. |
| ``` -i importance ``` | The importance of the server pool (default is `0`). |
| ``` -l min_size ``` | The minimum size of the server pool (default is `0`). |
| ``` -u max_size ``` | The maximum size of the server pool. The default value is `-1`, which indicates that the size is unlimited. |
| ``` -n "node_names" ``` | A comma-separated list of candidate node names enclosed in double quotation marks (`""`). The server pool will only include nodes on the candidate list, but not all nodes on the candidate list will necessarily be in the server pool. |
| \-f | Add the server pool, even if requires stopping resources in other server pools. |

##### Example

An example of this command is:

```
$ srvctl add srvpool -g SP1 -i 1 -l 3 -u 7 -n "mynode1,mynode2"
```

#### srvctl add vip

Adds a VIP to a node.

##### Syntax and Options

Use the `srvctl add vip` command with the following syntax:

```
srvctl add vip -n node_name -A {name|ip}/netmask[/if1[if2|...]]
     [-k network_number
] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-19 srvctl add vip Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of the node on which you are adding the VIP |
| ``` -A {name \|ip} /netmask  [/if1 [\|if2 \|...]] ``` | This specification creates a traditional VIP node application on the specified node |
| ``` -k network_number ``` | The optional network number from which VIPs are obtained.  If not specified, the VIPs are obtained from the same default network from which the `nodeapps` VIP is obtained. |
| ``` -v ``` | Verbose output |

Note:

You cannot have multiple VIPs on the same net number (subnet or interface pair) on the same node.

##### Example

An example of this command is:

```
# srvctl add vip -n node7 -A 192.168.16.17/255.255.255.0 -k 2
```

The preceding example creates a network number, `2`, for the VIP just added. You can specify the network number after the `-k` option in other SRVCTL commands.

### config

The `srvctl config` command displays the configuration stored in the Oracle Clusterware resource attributes.

Note:

If you disabled an object for which you are trying to obtain configuration information using the `srvctl disable` `object` `-n` `node_name` command, then bear in mind that using the `srvctl disable` `object` `-n` `node_name` command on a per-node basis in your cluster to disable an object throughout the cluster is not the same as globally disabling an object using the `srvctl disable` `object` command without the `-n` option. In the former case, the `srvctl config` `object` command may report that the object is still enabled.

See Also:

`"disable"` for more information about the `srvctl disable` command

Table A-20 srvctl config Summary

| Command | Description |
| --- | --- |
| `srvctl config asm` | Displays the configuration for the Oracle ASM instances on the node |
| `srvctl config cvu` | Displays the time interval between CVU checks |
| `srvctl config database` | Displays the configuration information of the cluster database |
| `srvctl config filesystem` | Displays the configuration information for an ACFS volume |
| `srvctl config gns` | Displays the GNS configuration |
| `srvctl config listener` | Displays a list of configured listeners that are registered with Oracle Clusterware on a given node |
| `srvctl config nodeapps` | Displays the configuration information for the node applications |
| `srvctl config oc4j` | Displays the configuration of the OC4J instance |
| `srvctl config ons` | Displays configuration information for Oracle Notification Service |
| `srvctl config scan` | Displays the configuration information for SCAN VIPs |
| `srvctl config scan_listener` | Displays the configuration information for SCAN listeners |
| `srvctl config service` | Displays the configuration information for the services |
| `srvctl config srvpool` | Displays configuration information for a specific server pool |
| `srvctl config vip` | Displays the configuration information for the VIP |

#### srvctl config asm

Displays the configuration for all Oracle ASM instances.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl config asm` command with the following syntax:

```
srvctl config asm [-a]
```

Table A-21 srvctl config asm Options

| Option | Description |
| --- | --- |
| ``` -a ``` | Print detailed configuration information |

##### Example

An example of this command is:

```
srvctl config asm -a
```

#### srvctl config cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command displays the time interval, in minutes, between CVU checks.

##### Syntax and Options

Use the `srvctl config cvu` command with the following syntax:

```
srvctl config cvu
```

This command has no options.

##### Examples

The `srvctl config cvu` command returns output similar to the following:

```
CVU is configured to run once every 360 minutes
```

#### srvctl config database

Displays the configuration for an Oracle RAC database or lists all configured databases that are registered with Oracle Clusterware.

##### Syntax and Options

Use the `srvctl config database` command with the following syntax:

```
srvctl config database [-d db_unique_name
] [-a]
```

Table A-22 srvctl config database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database.  If you do not specify this option, then the utility displays the configuration of all database resources. |
| ``` -a ``` | Print detailed configuration information |

##### Examples

To list the configuration of all databases, use the following example:

```
srvctl config database -d myDB
```

The following is example output from the `srvctl config database` command:

```
$ srvctl config database -d myDB
Database unique name: myDB
Database name:
Oracle home: /scott_st2/oracle
Oracle user: scott
Spfile:
Domain:
Start options: open
Stop options: immediate
Database role: PRIMARY
Management policy: AUTOMATIC
Server pools: myDB
Database instances:
Disk Groups:
Services: scottsvc1
Type: RACOneNode
Online relocation timeout: 30
Instance name prefix: myDB
Candidate servers: node1 node2
Database is administrator managed
```

The preceding sample output shows the database type as `RACOneNode`, an Oracle RAC One Node database. Other potential types are `RAC` and `SingleInstance`. The `Online relocation timeout`, `Instance name prefix`, and `Candidate servers` fields only apply to Oracle RAC One Node databases and do not display for the other two database types. Similarly, the `Database instances` field is empty because the database type is `RACOneNode`.

#### srvctl config filesystem

Displays the configuration for an Oracle Automatic Storage Management Cluster File System (Oracle ACFS) device.

##### Syntax and Options

Use the `srvctl config filesystem` command with the following syntax:

```
srvctl config filesystem -d volume_device_path
```

Table A-23 srvctl config filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_path ``` | The path name of a device that an Oracle ACFS volume uses. |

##### Examples

The following example shows how to retrieve the configuration for an Oracle ACFS file system:

```
srvctl config filesystem -d /dev/asm/d1volume293
```

#### srvctl config gns

Displays the configuration for GNS.

##### Syntax and Options

Use the `srvctl config gns` command with the following syntax:

```
srvctl config gns [-a] [-d] [-k] [-m] [-n node_name] [-p] [-s] [-V]
[-q name] [-l] [-v]
```

Note:

This option is available only for Oracle Clusterware.

Table A-24 srvctl config gns Options

| Option | Description |
| --- | --- |
| ``` -a ``` | Print detailed configuration information. |
| ``` -d ``` | Display the subdomain served by GNS. |
| ``` -k ``` | Display network on which GNS is listening. |
| ``` -m ``` | Display the port on which the GNS daemon is listening for multicast requests. |
| ``` -n node_name ``` | Display the configuration information for GNS on the specified node. |
| ``` -p ``` | Display the port that the GNS daemon uses to communicate with the DNS server. |
| ``` -s ``` | Display the status of GNS. |
| ``` -V ``` | Display the version of GNS. |
| ``` -q name ``` | Query GNS for the records belonging to a name. |
| ``` -l ``` | List all records in GNS. |
| ``` -v ``` | Verbose output. |

#### srvctl config listener

Displays a list of configured listeners that are registered with Oracle Clusterware or displays detailed configuration information for a specific listener.

##### Syntax and Options

Use the `srvctl config listener` command with the following syntax:

```
srvctl config listener [-l listener_name
] [-a]
```

Table A-25 srvctl config listener Options

| Option | Description |
| --- | --- |
| ``` -l listener_name ``` | Listener name.  If you do not specify this option, then the name of the listener defaults to LISTENER. |
| ``` -a ``` | Print detailed configuration information. |

##### Example

An example of this command is:

```
srvctl config listener
```

#### srvctl config nodeapps

Displays the VIP configuration for each node in the cluster.

##### Syntax and Options

Use the `srvctl config nodeapps` command with the following syntax:

```
srvctl config nodeapps [-a] [-g] [-s]
```

Note:

This command is only available with Oracle Clusterware.

Table A-26 srvctl config nodeapps Option

| Option | Description |
| --- | --- |
| ``` -a ``` | Displays the VIP address configuration |
| ``` -g ``` | Displays the GSD configuration |
| ``` -s ``` | Displays the Oracle Notification Service configuration |

##### Example

An example of this command is:

```
$ srvctl config nodeapps -a -g -s
```

#### srvctl config oc4j

Displays configuration information for the OC4J instance.

Note:

This command is only available with Oracle Clusterware.
```
srvctl config oc4j
```

#### srvctl config ons

Displays configuration information for the Oracle Notification Service daemon.

Note:

This command is only available with Oracle Clusterware.
```
srvctl config ons
```

#### srvctl config scan

Displays the configuration information for all SCAN VIPs, by default, or a specific SCAN VIP identified by `ordinal_number`.

##### Syntax and Options

Use the `srvctl config scan` command with the following syntax:

```
srvctl config scan [-i ordinal_number
]
```

The only option available for this command is `-i` `ordinal_number`, which identifies any one of the three SCAN VIPs, and can take a range of values from 1 to 3.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl config scan -i 1
```

#### srvctl config scan\_listener

Displays the configuration information for all SCAN listeners, by default, or a specific listener identified by `ordinal_number`.

##### Syntax and Options

Use the `srvctl config scan_listener` command with the following syntax:

```
srvctl config scan_listener [-i ordinal_number
]
```

The only option available for this command is `-i` `ordinal_number`, which identifies any one of the three SCAN VIPs, and can take a range of values from 1 to 3.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl config scan_listener -i 1
```

#### srvctl config service

Displays the configuration for a service.

##### Syntax and Options

Use the `srvctl config service` command with the following syntax:

```
srvctl config service -d db_unique_name
 [-s service_name
]
```

Table A-27 srvctl config service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name.  If this option is not specified, then the configuration information for all services configured for the database are displayed. |

##### Examples

An example output of this command is for a policy-managed database is:

```
$ srvctl config service -d mjkpdb -s mjkpsvc1
Service name: mjkpsvc1
Service is enabled
Server pool: mjksrvpool1
Cardinality: SINGLETON
Disconnect: false
Service role: PRIMARY
Management policy: AUTOMATIC
DTP transaction: false
AQ HA notifications: false
Failover type: NONE
Failover method: NONE
TAF failover retries: 0
TAF failover delay: 0
Connection Load Balancing Goal: LONG
Runtime Load Balancing Goal: NONE
TAF policy specification: NONE
Service is enabled on nodes:
Service is disabled on nodes:
Edition: "my Edition"
```

An example output of this command is for an administrator-managed database is:

```
$ srvctl config service -d mjkdb -s mjksvc1
Service name: mjksvc1
Service is enabled
Server pool: mjkdb
Cardinality: 1
Disconnect: false
Service role: PRIMARY
Management policy: AUTOMATIC
DTP transaction: false
AQ HA notifications: false
Failover type: NONE
Failover method: NONE
TAF failover retries: 0
TAF failover delay: 0
Connection Load Balancing Goal: LONG
Runtime Load Balancing Goal: NONE
TAF policy specification: NONE
Preferred instances: mjkdb_1
Available instances:
Edition: "my Edition"
```

Service configuration for administrator-managed Oracle RAC One Node databases displays the one instance as preferred.

Note:

The `srvctl config service` command shows exactly the string value you specified for the edition using the `srvctl add | modify service` command. If you specified the edition in upper case, then `srvctl config service` displays upper case. If it is surrounded by double quotation marks (`""`), then the command displays the double quotation marks. Otherwise, the command displays an empty string.

#### srvctl config srvpool

Displays configuration information including name, minimum size, maximum size, importance, and a list of server names, if applicable, for a specific server pool in a cluster.

##### Syntax and Options

Use the `srvctl config srvpool` command with the following syntax:

```
srvctl config srvpool [-g server_pool]
```

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl config srvpool -g dbpool
```

#### srvctl config vip

Displays all VIPs on all networks in the cluster except for user VIPs.

##### Syntax and Options

Use the `srvctl config vip` command with one of the following syntax models:

```
srvctl config vip -n node_name

srvctl config vip -i vip_name
```

Note:

This command is only available with Oracle Clusterware.

Table A-28 srvctl config vip Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |
| ``` -i vip_name ``` | The VIP name |

##### Example

An example of this command is:

```
$ srvctl config vip -n crmnode1
```

### convert

Starting with Oracle Database 11g Release 2 (11.2.0.2), the `srvctl convert` command converts a database either to or from an Oracle RAC One Node database.

Syntax and Options

Use the `srvctl convert database` command with one of the following syntax models:

```
srvctl convert database -d db_unique_name -c RACONENODE [-i instance_name] [-w timeout]

srvctl convert database -d db_unique_name -c RAC [-n node_name]
```

Table A-29 srvctl convert database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database.  Note: If you specify a noncluster database, then command returns an error instructing you to use `rconfig` to convert the noncluster database to Oracle RAC or Oracle RAC One Node. |
| ``` -c RACONENODE \| RAC ``` | The type of database to which you are converting, either Oracle RAC One Node or Oracle RAC.  Note: If there is an ongoing or failed online database relocation, then the command returns an error instructing you to first complete or abort the online database relocation and then rerun the command. |
| ``` -i instance_name ``` | Instance name prefix for Oracle RAC One Node databases. The default value for this option is the first 12 characters of the global unique name of the database.  Notes:  - You can use this option only when converting from an Oracle RAC database to an Oracle RAC One Node database. - In order for the converted instance to come online, you must restart the database using the `srvctl stop/start database` commands. |
| ``` -w timeout ``` | Online database relocation timeout, in minutes, for Oracle RAC One Node databases. The default is `30`. |
| ``` -n node_name ``` | Name of the node for administrator-managed Oracle RAC database. The default is the first candidate.  Note: If you do not specify a node name or you specify a node name where the database is not running, then the command returns an error instructing you specify the correct node. |

Example

An example of this command is:

```
$ srvctl convert database -d myDB -c RACONENODE -i instance_name
```

### disable

Disables a specified object (cluster database, database instance, Oracle ASM instance, or service). Use the `srvctl disable` command when you must shut down an object for maintenance. The disabled object does not automatically restart.

When you issue the `disable` command, the object is disabled and unavailable to run under Oracle Clusterware for automatic startup, failover, or restart. Additionally, you cannot run the `srvctl start` command on a disabled object until you first re-enable the object. If you specify `-i` `instance_name` or `-n` `node_name`, then SRVCTL only disables the object on the specified instance or node.

If you do not specify `-i` `instance_name` or `-n` `node_name`, then the disable action applies to the object that you specified, globally, on all nodes in the cluster. Any object you disable globally is also disabled on any nodes you add to the cluster in the future.

Disabling an object globally is not the same as disabling an object locally on each node in the cluster. For example, if you disable a database on several nodes, individually, in a cluster, then, when you run the `srvctl start database` command, the database starts only on nodes where the database is enabled. If, however, you disable the database globally, then the `srvctl start database` is rejected because the database is disabled, clusterwide.

Table A-30 srvctl disable Summary

| Command | Description |
| --- | --- |
| `srvctl disable asm` | Disables an Oracle ASM proxy resource |
| `srvctl disable cvu` | Disables the Cluster Verification Utility |
| `srvctl disable database` | Disables the cluster database |
| `srvctl disable diskgroup` | Disables a disk group on a number of specified nodes |
| `srvctl disable filesystem` | Disables an Oracle ACFS volume |
| `srvctl disable gns` | Disables GNS |
| `srvctl disable instance` | Disables an instance |
| `srvctl disable listener` | Disables a listener |
| `srvctl disable nodeapps` | Disables a node application and GSD |
| `srvctl disable oc4j` | Disables OC4J instances |
| `srvctl disable ons` | Disables the Oracle Notification Service daemon |
| `srvctl disable scan` | Disables SCAN VIPs |
| `srvctl disable scan_listener` | Disables SCAN listeners |
| `srvctl disable service` | Disables a service |
| `srvctl disable vip` | Disables a VIP |

#### srvctl disable asm

Disables the Oracle ASM proxy resource. Oracle ASM will restart if it contains Oracle Clusterware data or if the node restarts and it was running before the node failed. The `srvctl disable asm` command also prevents the `srvctl start asm` command from starting Oracle ASM instances.

Disabling the Oracle ASM proxy resource prevents the databases and disk groups from starting because they depend on the Oracle ASM proxy resource.

Note:

- To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.
- Oracle ASM is part of the Oracle Clusterware stack and when OCR and voting disks are stored on Oracle ASM, then Oracle ASM starts when OHASD starts the Oracle Clusterware stack. The `srvctl disable asm` command does not prevent the Oracle ASM instance managed by OHASD from starting. Oracle ASM, therefore, starts as needed by the Oracle Clusterware stack.
	The `srvctl disable asm` command prevents the Oracle ASM Oracle Clusterware proxy resource, and any resources that depend on it, from starting. So, the command prevents Oracle Clusterware-managed objects, such as databases, disk groups, and file systems that depend on Oracle ASM, from starting. For example, the `srvctl start database | diskgroup | filesystem` command fails to start any of those objects on nodes where the Oracle ASM Oracle Clusterware proxy resource is disabled. The command also prevents the `srvctl start asm` command from starting Oracle ASM on remote nodes.

##### Syntax and Options

Use the `srvctl disable asm` command with the following syntax:

```
srvctl disable asm [-n node_name
]
```

Table A-31 srvctl disable asm Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl disable asm -n crmnode1
```

#### srvctl disable cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command disables the Cluster Verification Utility (CVU) for Oracle Clusterware management, if enabled.

##### Syntax and Options

Use the `srvctl disable cvu` command with the following syntax:

```
srvctl disable cvu [-n node_name]
```

You can specify a particular node on which to disable CVU.

Table A-32 srvctl disable cvu Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |

##### Examples

An example of this command to disable CVU on a single node of a cluster is:

```
$ srvctl disable cvu -n crmnode1
```

#### srvctl disable database

Disables a database. If the database is a cluster database, then its instances are also disabled.

##### Syntax and Options

Use the `srvctl disable database` command with the following syntax:

```
srvctl disable database -d db_unique_name
 [-n node_name
]
```

Table A-33 srvctl disable database Options

| Option | Description |
| --- | --- |
| ``` -d database_name ``` | Database name |
| ``` -n node_name ``` | Disables the database from running on the named node  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl disable database -d mydb1
```

#### srvctl disable diskgroup

Disables a specific disk group on a number of specified nodes.

##### Syntax and Options

Use the `srvctl disable diskgroup` command with the following syntax:

```
srvctl disable diskgroup -g diskgroup_name
 [-n node_list
]
```

Table A-34 srvctl disable diskgroup Options

| Option | Description |
| --- | --- |
| ``` -g diskgroup_name ``` | The Oracle ASM disk group name |
| ``` -n node_list ``` | Comma-delimited list of node names on which to disable the disk group  This option is only available with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl disable diskgroup -g diskgroup1 -n mynode1, mynode2
```

#### srvctl disable filesystem

Disables an Oracle ACFS volume.

##### Syntax and Options

Use the `srvctl disable filesystem` command with the following syntax:

```
srvctl disable filesystem -d volume_device_name
```

Note:

This command is only available with Oracle Clusterware.

Table A-35 srvctl disable filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | Name of the Oracle ACFS volume |

##### Example

An example of this command is:

```
$ srvctl disable filesystem -d /dev/asm/d1volume293
```

#### srvctl disable gns

Disables GNS for a specific node, or all available nodes in the cluster.

##### Syntax and Options

Use the `srvctl disable gns` command with the following syntax:

```
srvctl disable gns [-n node_name
]
```

Note:

This command is only available with Oracle Clusterware.

Table A-36 srvctl disable gns Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Name of a node in the cluster  If you do not specify this option, then SRVCTL disables GNS for the entire cluster. |

##### Example

An example of this command is:

```
$ srvctl disable gns -n crm7
```

#### srvctl disable instance

Disables an instance. If the instance that you disable with this command is the last enabled instance, then this operation also disables the database.

##### Syntax and Options

Use the `srvctl disable instance` command with the following syntax:

```
srvctl disable instance -d db_unique_name
 -i instance_name_list
```

Note:

- This command is only available with Oracle Clusterware and Oracle RAC.
- If you run this command on an Oracle RAC One Node database, then the command returns an error instructing you to use the `database` noun, instead.

Table A-37 srvctl disable instance Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -i instance_name_list ``` | Comma-delimited list of instance names |

##### Example

An example of this command is:

```
$ srvctl disable instance -d crm -i "crm1,crm3"
```

#### srvctl disable listener

Disables a listener resource.

##### Syntax and Options

Use the `srvctl disable listener` command with the following syntax:

```
srvctl disable listener [-l listener_name
] [-n node_name
]
```

Table A-38 srvctl disable listener Options

| Option | Description |
| --- | --- |
| ``` -l listener_name ``` | Name of a listener resource. If you do not specify this option, the name of the listener defaults to `LISTENER`. |
| ``` -n node_name ``` | Name of a cluster node on which the listener you want to disable is running.  This option is only available with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl disable listener -l listener_crm -n node5
```

#### srvctl disable nodeapps

Disables node applications on all nodes in the cluster.

##### Syntax and Options

Use the `srvctl disable nodeapps` command with the following syntax:

```
srvctl disable nodeapps [-g] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-39 srvctl disable nodeapps Options

| Option | Description |
| --- | --- |
| ``` -g ``` | Disables GSD |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl disable nodeapps -g -v
```

#### srvctl disable oc4j

Disables the OC4J instance on all nodes or on a specific node.

##### Syntax and Options

Use the `srvctl disable oc4j` command with the following syntax:

```
srvctl disable oc4j [-n node_name
] [-v]
```

Table A-40 srvctl disable oc4j Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of a node in the cluster |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl disable oc4j -n crm3
```

#### srvctl disable ons

Disables the Oracle Notification Service daemon for Oracle Restart installations.

```
srvctl disable ons [-v]
```

The only option for this command is `-v`, which indicates that verbose output should be displayed.

#### srvctl disable scan

Disables all SCAN VIPs, by default, or a specific SCAN VIP identified by `ordinal_number`.

##### Syntax and Options

Use the `srvctl disable scan` command with the following syntax:

```
srvctl disable scan [-i ordinal_number
]
```

The only option available for this command is `-i` `ordinal_number`, which represents which identifies any one of the three SCAN VIPs, and can take a range of values from 1 to 3.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl disable scan -i 1
```

#### srvctl disable scan\_listener

Disables all SCAN listeners, by default, or a specific listener identified by `ordinal_number`.

##### Syntax and Options

Use the `srvctl disable scan_listener` command with the following syntax:

```
srvctl disable scan_listener [-i ordinal_number
]
```

The only option available for this command is `-i` `ordinal_number`, which identifies any one of the three SCAN listeners, and can take a range of values from 1 to 3.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl disable scan_listener -i 1
```

#### srvctl disable service

Disables a service. Disabling an entire service affects all of the instances, disabling each one. When the entire service is already disabled, a `srvctl disable service` operation on the entire service affects all of the instances and disables them; it just returns an error. This means that you cannot always use the entire set of service operations to manipulate the service indicators for each instance.

##### Syntax and Options

Use the `srvctl disable service` command with the following syntax:

```
srvctl disable service -d db_unique_name

      -s "service_name_list"
 [-i instance_name | -n node_name
]
```

If you do not specify either the `-i` `instance_name` or `-n` `node_name` options, then the command disables the service on all nodes.

Table A-41 srvctl disable service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s "service_name_list" ``` | Comma-delimited list of service names, or a single service name |
| ``` -i instance_name ``` | The name of the instance that you want to disable the service for.  Note: Use this option with administrator-managed databases  Note: This option is available only with Oracle Clusterware and Oracle RAC. |
| ``` -n node_name ``` | The name of the node on which to disable the service  Note: Use this option with policy-managed databases  Note: This option is available only with Oracle Clusterware and Oracle RAC. |

##### Examples

The following example globally disables two services for the `CRM` database:

```
$ srvctl disable service -d crm -s "crm,marketing"
```

The following example disables a service for the `CRM` database that is running on the `CRM1` instance, resulting in the service still being available for the database, but on one less instance:

```
$ srvctl disable service -d crm -s crm -i crm1
```

#### srvctl disable vip

Disables a specific VIP.

##### Syntax and Options

Use the `srvctl disable vip` command with the following syntax:

```
srvctl disable vip -i vip_name [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-42 srvctl disable vip Options

| Option | Description |
| --- | --- |
| ``` -i vip_name ``` | The VIP name |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl disable vip -i vip1 -v
```

### downgrade

Starting with Oracle Database 11g Release 2 (11.2.0.2), you can use the `downgrade` command to downgrade the database configuration after you manually downgrade the database.

#### srvctl downgrade database

The `srvctl downgrade database` command downgrades the configuration of a database and its services from its current version to the specified lower version.

##### Syntax and Options

Use the `srvctl downgrade database` command as follows:

```
srvctl downgrade database -d db_unique_name -o Oracle_home -t to_version
```

Table A-43 srvctl downgrade database Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -o Oracle_home ``` | The path to the `ORACLE_HOME` |
| ``` -t to_version ``` | The version to which to downgrade |

### enable

The `srvctl enable` command enables the specified object so that it can run under Oracle Clusterware for automatic startup, failover, or restart. The Oracle Clusterware application supporting the object may be up or down to use this function. The default value is `enable`. If the object is already enabled, then the command is ignored. Enabled objects can be started, and disabled objects cannot be started.

Table A-44 srvctl enable Summary

| Command | Description |
| --- | --- |
| `srvctl enable asm` | Enables an Oracle ASM instance |
| `srvctl enable cvu` | Enables the Cluster Verification Utility |
| `srvctl enable database` | Enables the database resource |
| `srvctl enable diskgroup` | Enables a specified disk group on a number of specified nodes |
| `srvctl enable filesystem` | Enables an Oracle ACFS volume |
| `srvctl enable gns` | Enables GNS |
| `srvctl enable instance` | Enables the instance |
| `srvctl enable listener` | Enables a listener |
| `srvctl enable nodeapps` | Enables node applications and GSD |
| `srvctl enable oc4j` | Enables OC4J instances |
| `srvctl enable ons` | Enables the Oracle Notification Service daemon |
| `srvctl enable scan` | Enables SCAN VIPs |
| `srvctl enable scan_listener` | Enables SCAN listeners |
| `srvctl enable service` | Enables a service |
| `srvctl enable vip` | Enables a VIP |

#### srvctl enable asm

Enables an Oracle ASM instance.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl enable asm` command with the following syntax:

```
srvctl enable asm [-n node_name
]
```

Table A-45 srvctl enable asm Option

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl enable asm -n crmnode1
```

#### srvctl enable cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command enables the Cluster Verification Utility (CVU) for Oracle Clusterware management if disabled.

##### Syntax and Options

Use the `srvctl enable cvu` command with the following syntax:

```
srvctl enable cvu [-n node_name
]
```

You can specify a particular node on which to enable CVU.

Table A-46 srvctl enable cvu Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  Note: This option is available only with Oracle Clusterware. |

##### Examples

An example of this command to enable CVU on a single node of a cluster is:

```
$ srvctl enable cvu -n crmnode1
```

#### srvctl enable database

Enables a cluster database and its instances.

##### Syntax and Options

Use the `srvctl enable database` command with the following syntax:

```
srvctl enable database -d db_unique_name
 [-n node_name
]
```

Table A-47 srvctl enable database Options

| Option | Description |
| --- | --- |
| ``` -d database_name ``` | Database name |
| ``` -n node_name ``` | The name of the node for which the database resource should be enabled  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl enable database -d mydb1
```

#### srvctl enable diskgroup

Enables a specific disk group on a number of specified nodes.

##### Syntax and Options

Use the `srvctl enable diskgroup` command with the following syntax:

```
srvctl enable diskgroup -g diskgroup_name
 [-n node_list
]
```

Table A-48 srvctl enable diskgroup Options

| Option | Description |
| --- | --- |
| ``` -g diskgroup_name ``` | The Oracle ASM disk group name |
| ``` -n node_list ``` | Comma-delimited list of node names on which to enable the disk group  This option is only available with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl enable diskgroup -g diskgroup1 -n mynode1,mynode2
```

#### srvctl enable filesystem

Enables an Oracle ACFS volume.

##### Syntax and Options

Use the `srvctl enable filesystem` command with the following syntax:

```
srvctl enable filesystem -d volume_device_name
```

Note:

This command is only available with Oracle Clusterware.

Table A-49 srvctl enable filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | Device name of the Oracle ACFS volume |

##### Example

An example of this command is:

```
$ srvctl enable filesystem  -d /dev/asm/d1volume293
```

#### srvctl enable gns

Enables GNS on all nodes or a specific node.

##### Syntax and Options

Use the `srvctl enable gns` command with the following syntax:

```
srvctl enable gns [-n node_name
]
```

Note:

This command is available only with Oracle Clusterware.

Table A-50 srvctl enable gns Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Name of the node on which to enable GNS.  If this option is not specified, then GNS is enabled on all nodes in the cluster. |

##### Example

An example of this command is:

```
$ srvctl enable gns
```

#### srvctl enable instance

Enables an instance for an Oracle RAC database. If you use this command to enable all instances, then the database is also enabled.

##### Syntax and Options

Use the `srvctl enable instance` command with the following syntax:

```
srvctl enable instance -d db_unique_name
 -i instance_name_list
```

Note:

- This command is only available with Oracle Clusterware and Oracle RAC.
- If you run this command on an Oracle RAC One Node database, then the command returns an error instructing you to use the `database` noun, instead.

Table A-51 srvctl enable instance Option

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -i instance_name_list ``` | Comma-delimited list of instance names. |

##### Example

An example of this command is:

```
$ srvctl enable instance  -d crm -i "crm1,crm2"
```

#### srvctl enable listener

Enables a listener resource.

##### Syntax and Options

Use the `srvctl enable listener` command with the following syntax:

```
srvctl enable listener [-l listener_name
] [-n node_name
]
```

Table A-52 srvctl enable listener Options

| Option | Description |
| --- | --- |
| ``` -l listener_name ``` | Name of a listener resource. If you do not specify this option, the name of the listener defaults to LISTENER |
| ``` -n node_name ``` | Name of a cluster node  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl enable listener -l listener_crm -n node5
```

#### srvctl enable nodeapps

Enables the node applications on all nodes in the cluster.

##### Syntax and Options

Use the `srvctl enable nodeapps` command with the following syntax:

```
srvctl enable nodeapps [-g] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-53 srvctl enable nodeapps Options

| Option | Description |
| --- | --- |
| ``` -g ``` | Enables GSD |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl enable nodeapps -g -v
```

#### srvctl enable oc4j

Enables the OC4J instance on all nodes or on a specific node.

##### Syntax and Options

Use the `srvctl enable oc4j` command with the following syntax:

```
srvctl enable oc4j [-n node_name
] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-54 srvctl enable oc4j Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of a node in the cluster |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl enable oc4j -n crm3
```

#### srvctl enable ons

Enables the Oracle Notification Service daemon.

Note:

This command is only available with Oracle Restart.

##### Syntax and Options

Use the `srvctl enable ons` command with the following syntax:

```
srvctl enable ons [-v]
```

The only option for this command is -v, which indicates that verbose output should be displayed.

##### Example

An example of this command is:

```
$ srvctl enable ons
```

#### srvctl enable scan

Enables all SCAN VIPs, by default, or a specific SCAN VIP identified by its `ordinal_number`.

##### Syntax and Options

Use the `srvctl enable scan` command with the following syntax:

```
srvctl enable scan [-i ordinal_number
]
```

The only option available for this command is `-i` `ordinal_number`, which identifies any one of the three SCAN VIPs, and takes a range of values from 1 to 3.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl enable scan -i 1
```

#### srvctl enable scan\_listener

Enables all SCAN listeners, by default, or a specific listener identified by its `ordinal_number`.

##### Syntax and Options

Use the `srvctl enable scan_listener` command with the following syntax:

```
srvctl enable scan_listener [-i ordinal_number
]
```

The only option available for this command is `-i` `ordinal_number`, which identifies any one of the three SCAN listeners, and takes a range of values from 1 to 3.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl enable scan_listener -i 1
```

#### srvctl enable service

Enables a service for Oracle Clusterware. Enabling an entire service also affects the enabling of the service over all of the instances by enabling the service at each one. When the entire service is already enabled, an `srvctl enable service` operation does not affect all of the instances and enable them. Instead, this operation returns an error. Therefore, you cannot always use the entire set of service operations to manipulate the service indicators for each instance.

##### Syntax and Options

Use the `srvctl enable service` command with the following syntax:

```
srvctl enable service -d db_unique_name
 -s "service_name_list"

     [-i instance_name | -n node_name
]
```

Table A-55 srvctl enable service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name_list ``` | Comma-delimited list of service names |
| ``` -i instance_name ``` | Name of the database instance where you want the service to run  Use this option for administrator-managed databases  Note: This option is available only with Oracle Clusterware and Oracle RAC. |
| ``` -n node_name ``` | Name of the node where you want the service to run  Use this option for policy-managed databases  Note: This option is available only with Oracle Clusterware and Oracle RAC. |

##### Examples

The following example globally enables a service:

```
$ srvctl enable service -d crm -s crm
```

The following example enables a service to use a preferred instance:

```
$srvctl enable service -d crm -s crm -i crm1
```

#### srvctl enable vip

Enables a specific VIP.

##### Syntax and Options

Use the `srvctl enable vip` command with the following syntax:

```
srvctl enable vip -i vip_name [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-56 srvctl enable vip Options

| Option | Description |
| --- | --- |
| ``` -i vip_name ``` | The VIP name |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl enable vip -i crm1-vip -v
```

### getenv

Gets and displays values for the environment variables from the configuration file. Use SRVCTL with the `setenv`, `getenv`, and `unset` `env` verbs to administer the environment configurations for databases, instances, services, and node applications.

Table A-57 srvctl getenv Summary

| Command | Description |
| --- | --- |
| `srvctl getenv asm` | Gets the Oracle ASM environment values |
| `srvctl getenv database` | Gets the database environment values |
| `srvctl getenv listener` | Gets the listener environment values |
| `srvctl getenv nodeapps` | Gets the node application environment values |
| `srvctl getenv vip` | Gets the service environment values |

#### srvctl getenv asm

Displays the values for environment variables associated with Oracle ASM.

##### Syntax and Options

Use the `srvctl getenv asm` command with the following syntax:

```
srvctl getenv asm [-t "name_list"
]
```

Table A-58 srvctl getenv asm Options

| Options | Description |
| --- | --- |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables.  If this option is not specified, then the values of all environment variables associated with Oracle ASM are displayed. |

##### Example

The following example displays the current values for all the environment variables used by Oracle ASM:

```
$ srvctl getenv asm
```

#### srvctl getenv database

Displays the values for environment variables associated with a database.

##### Syntax and Options

Use the `srvctl getenv database` command with the following syntax:

```
srvctl getenv database -d db_unique_name
 [-t "name_list"
]
```

Table A-59 srvctl getenv database Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables  If this option is not specified, then the values of all environment variables associated with the database are displayed. |

##### Example

The following example gets the environment configuration for the `CRM` database:

```
$ srvctl getenv database -d crm
```

#### srvctl getenv listener

Gets the environment variables for the specified listener.

##### Syntax and Options

Use the `srvctl getenv listener` command with the following syntax:

```
srvctl getenv listener [-l listener_name
] [-t "name_list
"]
```

Table A-60 srvctl getenv listener Options

| Options | Description |
| --- | --- |
| ``` -l listener_name ``` | Listener name  If this option is not specified, the name of the listener defaults to LISTENER |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables  If this option is not specified, then the values of all environment variables associated with the listener are displayed. |

##### Example

The following example lists all environment variables for the default listener:

```
$ srvctl getenv listener
```

#### srvctl getenv nodeapps

Gets the environment variables for the node application configurations.

##### Syntax and Options

Use the `srvctl getenv nodeapps` command with the following syntax:

```
srvctl getenv nodeapps [-a] [-g] [-s] [-t "name_list
"] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-61 srvctl getenv nodeapps Options

| Options | Description |
| --- | --- |
| ``` -a ``` | Displays the VIP address configuration |
| ``` -g ``` | Displays the GSD configuration |
| ``` -s ``` | Displays the Oracle Notification Service configuration |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables  If this option is not specified, then the values of all environment variables associated with the nodeapps are displayed. |
| ``` -v ``` | Verbose output |

##### Example

The following example lists all environment variables for the node applications:

```
$ srvctl getenv nodeapps -a
```

#### srvctl getenv vip

Gets the environment variables for the specified VIP.

##### Syntax and Options

Use the `srvctl getenv vip` command with the following syntax:

```
srvctl getenv vip -i vip_name
 [-t "name_list
"] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-62 srvctl getenv vip Options

| Options | Description |
| --- | --- |
| ``` -i vip_name ``` | The name of the VIP |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables  If this option is not specified, then the values of all environment variables associated with the VIP are displayed. |
| ``` -v ``` | Verbose output |

##### Example

The following example lists all environment variables for the specified VIP:

```
$ srvctl getenv vip -i node1-vip
```

### modify

Enables you to modify the instance configuration without removing and adding Oracle Clusterware resources. Using `modify` preserves the environment in the OCR configuration that would otherwise need to be re-entered. The configuration description is modified in the OCR configuration, and a new Oracle Clusterware profile is generated and registered. The change takes effect when the application is next restarted.

Table A-63 srvctl modify Summary

| Command | Description |
| --- | --- |
| `srvctl modify asm` | Modifies the configuration for Oracle ASM |
| `srvctl modify cvu` | Modifies the check interval of the Cluster Verification Utility |
| `srvctl modify database` | Modifies the configuration for a database |
| `srvctl modify filesystem` | Modifies the user authorized to mount and unmount the Oracle ACFS volume |
| `srvctl modify gns` | Modifies the GNS configuration |
| `srvctl modify instance` | Modifies the configuration for an instance |
| `srvctl modify listener` | Modifies the listener configuration on a node |
| `srvctl modify network` | Modifies the configuration for a node application |
| `srvctl modify nodeapps` | Modifies the configuration for a node application |
| `srvctl modify oc4j` | Modifies the RMI port for an OC4J instance |
| `srvctl modify ons` | Modifies the network configuration for the Oracle Notification Service daemon |
| `srvctl modify scan` | Modifies the SCAN VIP configuration to match that of a specific SCAN VIP |
| `srvctl modify scan_listener` | Updates the SCAN listener configuration to match that of the current SCAN VIP configuration |
| `srvctl modify service` | Modifies the configuration for a service |
| `srvctl modify srvpool` | Modifies a specific server pool |

#### srvctl modify asm

Modify the listener used by Oracle ASM, the disk group discovery string used by Oracle ASM, or the SPFILE used by Oracle ASM for a noncluster database or a cluster database.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl modify asm` command with the following syntax:

```
srvctl modify asm [-n node_name
] [-l listener_name] 
     [-d asm_diskstring
] [-p spfile_path_name
]
```

Note:

This command is only available with Oracle Clusterware.

Table A-64 srvctl modify asm Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |
| ``` -l listener_name ``` | The listener name with which Oracle ASM registers |
| ``` -d asm_diskstring ``` | The new Oracle ASM disk group discovery string |
| ``` -p spfile_path_name ``` | The path name of the new spfile to be used by Oracle ASM |

##### Example

An example of this command to modify the configuration of Oracle ASM is:

```
$ srvctl modify asm -l lsnr1
```

#### srvctl modify cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command modifies the check interval for CVU in an Oracle Clusterware configuration.

##### Syntax and Options

Use the `srvctl modify cvu` command with the following syntax:

```
srvctl modify cvu [-t check_interval_in_minutes]
```

Table A-65 srvctl modify cvu Options

| Option | Description |
| --- | --- |
| ``` -t check_interval_in_minutes ``` | By default, CVU runs once every 360 minutes (six hours) and verifies the health of cluster. The shortest interval you can specify for CVU check is 10 minutes. |

##### Examples

An example of this command to modify CVU to a check interval of 4 hours is:

```
$ srvctl modify cvu -t 240
```

#### srvctl modify database

Modifies the configuration for a database.

##### Syntax and Options

Use the `srvctl modify database` command with the following syntax:

```
srvctl modify database -d db_unique_name
 [-n db_name
]
     [-o oracle_home
] [-u user_name] [-m db_domain
] [-p spfile
] 
     [-r {PRIMARY | PHYSICAL_STANDBY | LOGICAL_STANDBY | SNAPSHOT_STANDBY}]
     [-s start_options
] [-t stop_options] [-y {AUTOMATIC | MANUAL | NORESTART}]
     [-g "server_pool_list
"] [{-a "diskgroup_list" | -z}]
     [-e server_list] [-w timeout] [-j "acfs_path_list"]
```

Table A-66 srvctl modify database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -n db_name ``` | Name of the database (as specified by the `DB_NAME` initialization parameter), if it is different from the database unique name specified with the `-d` option |
| ``` -o oracle_home ``` | Path for the Oracle home for the database |
| ``` -u user_name ``` | The name of the user that owns the Oracle home directory  Note: If you specify the `-u` option, you must run this command in privileged mode. |
| ``` -m db_domain ``` | Domain for the database  Note: If the database has the initialization parameter `DB_DOMAIN` set, then you must specify this option. |
| ``` -p spfile ``` | Path name of the server parameter file for the database |
| ``` -r role [PRIMARY \|  PHYSICAL_STANDBY \|  LOGICAL_STANDBY \|  SNAPSHOT_STANDBY] ``` | Role of the database in an Oracle Data Guard configuration (`PRIMARY`, `PHYSICAL_STANDBY`, `LOGICAL_STANDBY`, or `SNAPSHOT_STANDBY`) |
| ``` -s start_options ``` | Startup options for the database, such as `OPEN`, `MOUNT`, or `NOMOUNT`  Note: For multi-word startup options, such as `read only` and `read write`, separate the words with a space and enclose in double quotation marks (`""`). For example, `"read only"`.  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for more information about startup options |
| ``` -t stop_options ``` | Stop options for the database, such as `NORMAL`, `TRANSACTIONAL`, `IMMEDIATE`, or `ABORT`  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm#SQPUG125) for more information about shutdown options |
| ``` -y [AUTOMATIC \|  MANUAL \| NORESTART] ``` | Management policy for the database resource. Starting with Oracle Database 11g Release 2 (11.2.0.3), you can use the `NORESTART` value. |
| ``` -g "server_pool_list" ``` | A comma-delimited list of the names of server pools to use for a policy-managed database  Notes:  - If the database you are modifying is administrator managed, then this option changes it to be policy managed, in addition to changing all the database's services to run as uniform services in the specified server pool. You can specify only one server pool for converting an administrator-managed database to policy managed. - This option is available only with Oracle Clusterware and Oracle RAC. |
| ``` -a "diskgroup_list" ``` | Comma-delimited list of Oracle ASM disk groups |
| ``` -z ``` | To remove the database's dependency on Oracle ASM disk groups |
| ``` -e server_list ``` | List candidate servers for Oracle RAC One Node databases.  Notes: You can use this option only with administrator-managed Oracle RAC One Node databases. If your Oracle RAC One Node database is policy managed, you cannot use this option. |
| ``` -w timeout ``` | Online database relocation timeout, in minutes, for Oracle RAC One Node databases. The default is `30`. |
| ``` -j "acfs_path_list" ``` | A single Oracle ACFS path or a comma-delimited list of Oracle ACFS paths enclosed in double quotation marks (`""`) where the database's dependency is set.  Use this option to create dependencies on Oracle ACFS file systems other than `ORACLE_HOME`, such as for when the database uses `ORACLE_BASE` on a file system that is different from the `ORACLE_HOME` file system. |

##### Usage Notes

- The `srvctl modify database` command can convert administrator-managed databases to policy-managed databases. For a running administrator-managed database, if the server list is supplied, then the node where the database is running must be on that list. The instance name prefix cannot be modified after running the `srvctl add database` command.
- You cannot change the management policy from `AUTOMATIC` (using the `-y` option) for Oracle RAC One Node databases. Any attempt to do so results in an error message. The same is true for the `-x` option, which is used to change the node on which a noncluster database runs.
- For policy-managed Oracle RAC One Node databases, you can use the `-g` option to move an Oracle RAC One Node database between server pools but you can only specify one server pool. Specifying a list of server pools returns an error.

##### Examples

The following example changes the role of a database to a logical standby:

```
$ srvctl modify database -d crm -r logical_standby
```

The following example directs the `racTest` database to use the `SYSFILES`, `LOGS`, and `OLTP` Oracle ASM disk groups.

```
$ srvctl modify database -d racTest -a "SYSFILES,LOGS,OLTP"
```

#### srvctl modify filesystem

Modifies the name of the user that is authorized to mount and unmount the Oracle ACFS volume.

##### Syntax and Options

Use the `srvctl modify filesystem` command with the following syntax:

```
srvctl modify filesystem -d volume_device_name
 -u user_name
```

Note:

This command is only available with Oracle Clusterware.

Table A-67 srvctl modify filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | Device name of the Oracle ACFS volume |
| ``` -u user_name ``` | Name of the user that is authorized to mount and unmount the Oracle ACFS volume |

##### Examples

The following example changes the authorized user to `sysad` for the `RACVOL1` volume:

```
$ srvctl modify filesystem -d /dev/asm/racvol1 -u sysad
```

#### srvctl modify gns

Modifies the IP address or domain used by GNS

##### Syntax and Options

Use the `srvctl modify gns` command with the following syntax:

```
srvctl modify gns [-i ip_address] [-d domain]
```

Table A-68 srvctl modify gns Options

| Option | Description |
| --- | --- |
| ``` -i ip_address ``` | The IP address for GNS |
| ``` -d domain ``` | The network domain for GNS |

##### Example

An example of this command is:

```
$ srvctl modify gns -i 192.000.000.003
```

#### srvctl modify instance

For an administrator-managed database, this command modifies the configuration for a database instance from its current node to another node. For a policy-managed database, this command defines an instance name to use when the database runs on the specified node.

##### Syntax and Options

Use the `srvctl modify instance` command with the following syntax:

```
srvctl modify instance -d db_unique_name
 -i instance_name
     {-n node_name
 | -z}
```

Notes:

- You cannot use this command to rename or relocate a running instance.
- This command is only available with Oracle Clusterware and Oracle RAC.

Table A-69 srvctl modify instance Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -i instance_name ``` | Database instance name |
| ``` -n node_name ``` | Name of the node on which to run the instance |
| ``` -z ``` | To remove existing node instance mapping for a policy-managed database |

##### Examples

The following example to changes the configuration of an administrator-managed database, `amdb`, so that the database instance, `amdb1`, runs on the specified node, `mynode`:

```
$ srvctl modify instance -d amdb -i amdb1 -n mynode
```

The following example causes the policy-managed database `pmdb`, when and if it runs on `mynode`, to use the instance name `pmdb1`:

```
$ srvctl modify instance -d pmdb -i pmdb1 -n mynode
```

The following example removes the directive established by the previous example:

```
$ srvctl modify instance -d pmdb -i pmdb1 -z
```

#### srvctl modify listener

Modifies the listener name, `ORACLE_HOME` path or the listener endpoints, either for the default listener, or a specific listener, or for all the listeners represented in a given list of listener names, that are registered with Oracle Restart or with Oracle Clusterware on the specified node.

If you want to change the name of a listener, then use the `srvctl remove listener` and `srvctl add listener` commands.

##### Syntax and Options

Use the `srvctl modify listener` command with the following syntax:

```
srvctl modify listener [-l listener_name] [-o oracle_home] [-u user_name
]
     [-p "[TCP:]port_list[/IPC:key][/NMP:pipe_name][/TCPS:s_port][/SDP:port]"]
     [-k network_number
]
```

Table A-70 srvctl modify listener Options

| Option | Description |
| --- | --- |
| ``` -l listener_name ``` | The name of the listener.  If you do not specify this option, then the utility uses the name `LISTENER`. |
| ``` -o oracle_home ``` | When this option is specified, SRVCTL moves the listener to run from the specified Oracle home.  Note: When using this option, the command should be run as privileged user to enable SRVCTL to update resource ownership corresponding to the new `ORACLE_HOME` owner |
| ``` -u user_name ``` | The name of the operating system user who will own the specified Oracle home  Note: This option is available only with Oracle Clusterware. |
| ``` -p "[TCP:]port_list [/IPC:key][/NMP:pipe_name] [/TCPS:s_port][/SDP:port]" ``` | Protocol specifications for the listener. `port_list` is comma-delimited list of port numbers. |
| ``` -k network_number ``` | This option changes the public subnet on which the listener listens.  Note: You should have at least one listener on the default network at all times. Do not use this option to change the network of the only listener that listens on the default network. |

##### Example

The following example changes the TCP ports for the default listener on the node `mynode1`:

```
$ srvctl modify listener -l listener1 -p "TCP:1521,1522"
```

#### srvctl modify network

Modifies the subnet for a specified network.

##### Syntax and Options

Use the `srvctl modify network` command with one of the following syntax models:

```
srvctl modify network [-k network_number
 [-S subnet/netmask[/if1[|if2|...]]]
     [-w network_type] [-v]
```

Table A-71 srvctl modify network Options

| Option | Description |
| --- | --- |
| ``` -k network_number ``` | Specify a network number. The default is 1. |
| ``` -S subnet/netmask [/if1[\|if2\|...]] ``` | Specifies a subnet number for the public network. The netmask and interfaces specified, if any, change those of the network you are modifying. If you do not specify any interface names, then the VIPs use any interface on the given subnet. |
| ``` -w network_type ``` | Specify the network type: `static`, `dhcp`, or `mixed`. |
| ``` -v ``` | Verbose output. |

##### Examples

The following example changes the subnet number, netmask, and interface list:

```
$ srvctl modify network -S 192.168.2.0/255.255.255.0/eth0
```

The following example changes the second network to DHCP:

```
$ srvctl modify network -k 2 -w dhcp
```

#### srvctl modify nodeapps

Modifies the configuration for a node application.

##### Syntax and Options

Use the `srvctl modify nodeapps` command with one of the following syntax models:

```
srvctl modify nodeapps [-n node_name
 -A new_vip_address
]
[-S subnet
/netmask[/if1[|if2|...]] [-u network_type]
     [-e em_port
] [-l ons_local_port] [-r ons_remote_port]
     [-t host[:port][,host:port,...]] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-72 srvctl modify nodeapps Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name. |
| ``` -A new_vip_address / netmask ``` | Node level Virtual IP address. The address specified by name or IP must match the subnet number of the default network.  Note: This option must be used for upgrade configurations and new non-DHCP configurations |
| ``` -S subnet/netmask [/if1[\|if2\|...]] ``` | Specifies a subnet number for the public network. The netmask and interfaces specified, if any, change those of the default network. Additionally, if you specify the `netmask` option, then you need only specify it for the first node on each network. |
| ``` -u network_type ``` | Specifies the network server type, such as `static`, `dhcp`, or `mixed`. |
| ``` -e em_port ``` | Local port on which Oracle Enterprise Manager listens. The default port is 2016. |
| ``` -l ons_local_port ``` | Port on which the Oracle Notification Service daemon listens for local client connections.  Note: The local port and remote port must each be unique. |
| ``` -r ons_remote_port ``` | Port on which the Oracle Notification Service daemon listens for connections from remote hosts.  Note: The local port and remote port must each be unique. |
| ``` -t host:port, [host:port,...] ``` | List of `host``:``port` pairs of remote hosts that are part of the Oracle Notification Service network but are not part of the cluster. If you do not specify a `port` for a remote host, then the utility uses the value you specified for `ons_remote_port`. |
| ``` -v ``` | Verbose output. |

##### Example

The following example changes the nodeapps resource on `mynode1` to use the application VIP of 100.200.300.40 with a subnet mask of 255.255.255.0 on the network interface `eth0`:

```
$ srvctl modify nodeapps -n mynode1 -A 100.200.300.40/255.255.255.0/eth0
```

#### srvctl modify oc4j

Modifies the RMI port for the OC4J instances.

##### Syntax and Options

Use the `srvctl modify oc4j` command with the following syntax:

```
srvctl modify oc4j -p oc4j_rmi_port
 [-v]
```

Table A-73 srvctl modify oc4j Options

| Option | Description |
| --- | --- |
| ``` -p oc4j_rmi_port ``` | The RMI port number used by the OC4J instance |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl modify oc4j -p 5385
```

#### srvctl modify ons

Modifies the ports used by the Oracle Notification Service daemon that is registered with Oracle Restart.

##### Syntax and Options

Use the `srvctl modify ons` command with the following syntax:

```
srvctl modify ons [-l ons_local_port] [-r ons_remote_port
]
     [-t host
[:port
][,host
[:port
]][...]] [-v]
```

Table A-74 srvctl modify ons Options

| Option | Description |
| --- | --- |
| ``` -l ons_local_port ``` | The Oracle Notification Service daemon listening port for local client connections  Note: The local port and remote port must each be unique. |
| ``` -r ons_remote_port ``` | The Oracle Notification Service daemon listening port for connections from remote hosts  Note: The local port and remote port must each be unique. |
| ``` -t host [:port ] [,host [:port ]][...]] ``` | A list of `host``:``port` pairs of remote hosts that are part of the Oracle Notification Service network but are not part of the Oracle Clusterware cluster  Note: If you do not specify `port` for a remote host, then the utility uses `ons_remote_port`. |
| `-v` | Display verbose output |

#### srvctl modify scan

Modifies the number of SCAN VIPs to the match the number of IP addresses returned by looking up the `scan_name` you specify in DNS. Presumably the `scan_name` has not changed, but DNS was changed to add or remove IP addresses, and now you must adjust the Oracle Clusterware resource configuration to match.

##### Syntax and Options

Use the `srvctl modify scan` command with the following syntax:

```
srvctl modify scan -n scan_name
```

The only option available for this command is `-n` `scan_name`, which identifies the SCAN name that resolves to the SCAN VIPs that you want to use.

Note:

This command is only available with Oracle Clusterware.

##### Example

Assume your system currently has a SCAN named `scan_name1`, and it resolves to a single IP address in DNS. If you modify the SCAN `scan_name1` in DNS to resolve to three IP addresses, then use the following command to create the additional SCAN VIP resources:

```
$ srvctl modify scan -n scan_name1
```

#### srvctl modify scan\_listener

Modifies the SCAN listener to match SCAN VIP's or modifies the SCAN listener endpoints.

##### Syntax and Options

Use the `srvctl modify scan_listener` command with the following syntax:

```
srvctl modify scan_listener {-p [TCP:]port
[/IPC:key
][/NMP:pipe_name
]
     [/TCPS:s_port
][/SDP:port
] | -u }
```

Note:

This command is only available with Oracle Clusterware.

Table A-75 srvctl modify scan\_listener Options

| Option | Description |
| --- | --- |
| ``` -p [TCP:]port [/IPC:key ] [/NMP:pipe_name ] [/TCPS:s_port ][/SDP:port ] ``` | The new SCAN listener end points |
| ``` -u ``` | Updates SCAN listener configuration to match the current SCAN VIP configuration. This option adds new resources or removes existing SCAN listener resources to match the SCAN VIP resources. |

##### Example

Assume your system currently has a SCAN named `scan_name1`, and you recently modified the DNS entry to resolve to three IP addresses instead of one. After running the `srvctl modify scan` command to create additional SCAN VIP resources, use the following command to create Oracle Clusterware resources for the additional two SCAN listeners to go with the two additional SCAN VIPs:

```
$ srvctl modify scan_listener -u
```

#### srvctl modify service

Moves a service member from one instance to another. Additionally, this command changes which instances are to be the preferred and the available instances for a service. This command supports some online modifications to the service, such as:

- Service attributes from `DBMS_SERVICE` (for example, failover delay, Runtime Load Balancing Goal, and so on) can be changed online but the changes take effect only when the service is next (re)started.
- When a service configuration is modified so that a new preferred or available instance is added, the running state of the existing service is not affected. However, the newly added instances will not automatically provide the service, until a `srvctl start service` command is issued as described.
- When there are available instances for the service, and the service configuration is modified so that a preferred or available instance is removed, the running state of the service may change unpredictably:
	- The service is stopped and then removed on some instances according to the new service configuration.
		- The service may be running on some instances that are being removed from the service configuration.
		- These services will be relocated to the next free instance in the new service configuration.

As a result of these considerations, when the online service is being modified, users may experience a brief service outage on some instances even if the instances are not being removed. Or users may experience a brief service outage on instances that are being removed from the service.

Important:

Oracle recommends that you limit configuration changes to the minimum requirement and that you not perform other service operations while the online service modification is in progress.

##### Syntax and Options

Use one of the following forms of the `srvctl modify service` command with the specified syntax:

To move a service from one instance to another:

```
srvctl modify service -d db_unique_name
 -s service_name
 -i old_instance_name
  -t new_instance_name [-f]
```

Note:

This form of the command is only available with Oracle Clusterware.

Table A-76 srvctl modify service Options for Moving a Service

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name |
| ``` -i old_instance_name ``` | Old instance name |
| ``` -t new_instance_name ``` | New instance name |
| ``` -f ``` | Disconnect all sessions during stop or relocate service operations |

To change an available instance to a preferred instance for a service:

```
srvctl modify service -d db_unique_name
 -s service_name
 -t edition_name
-i avail_inst_name
 -r [-f]
```

Note:

This form of the command is only available with Oracle Clusterware and does not accept placement options for Oracle RAC One Node databases.

Table A-77 srvctl modify service Options for Changing an Available Instance to a Preferred Instance

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name |
| ``` -t edition_name ``` | (version 11.2.0.2 or higher) The initial session edition of the service.  When an edition is specified for a service, all subsequent connections that specify the service use this edition as the initial session edition. However, if a session connection specifies a different edition, then the edition specified in the session connection is used for the initial session edition.  SRVCTL does not validate the specified edition name. During connection, the connect user must have USE privilege on the specified edition. If the edition does not exist or if the connect user does not have USE privilege on the specified edition, then SRVCTL returns an error. |
| ``` -i available_inst_name ``` | Name of the available instance to change |
| ``` -r ``` | Change instance status to preferred |
| ``` -f ``` | Disconnect all sessions during stop or relocate service operations |

To change the available and preferred status for multiple instances:

```
srvctl modify service -d db_unique_name
 -s service_name
 -n -i preferred_list
 
     [-a available_list
] [-f]
```

Note:

This form of the command is only available with Oracle Clusterware and does not accept placement options for Oracle RAC One Node databases.

Table A-78 srvctl modify service Options for Changing Available and Preferred Status of Multiple Instances

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name |
| ``` -n ``` | Uses only the instances named for this service (unnamed instances already assigned to the service are removed) |
| ``` -i preferred_instance_list ``` | List of preferred instances |
| ``` -a available_instance_list ``` | List of available instances |
| ``` -f ``` | Disconnect all sessions during stop or relocate service operations |

To modify other service attributes or to modify a service for Oracle Clusterware:

```
srvctl modify service -d db_unique_name
 -s service_name

     [-g server_pool] [-c {UNIFORM|SINGLETON}] [-P {BASIC|PRECONNECT|NONE}] 
     [-l {[PRIMARY] | [PHYSICAL_STANDBY] | [LOGICAL_STANDBY] | [SNAPSHOT_STANDBY]}
     [-q {TRUE|FALSE}] [-x {TRUE|FALSE}] [-j {SHORT|LONG}] 
     [-B {NONE|SERVICE_TIME|THROUGHPUT}] [-e {NONE|SESSION|SELECT}] 
     [-m {NONE|BASIC}] [-z failover_retries
] [-w failover_delay
]
     [-y {AUTOMATIC | MANUAL}]
```

Table A-79 srvctl modify service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name |
| ``` -g server_pool ``` | The name of a server pool used when the database is policy managed.  Note: This option is available only with Oracle RAC and only for policy-managed databases. |
| ``` -c {UNIFORM \| SINGLETON} ``` | The cardinality of the service, either `UNIFORM` (offered on all instances in the server pool) or `SINGLETON` (runs on only one instance at a time)  Note: This option is available only with Oracle Clusterware. |
| ``` -P {BASIC\|PRECONNECT\|NONE} ``` | TAF failover policy  Note: The `PRECONNECT` option applies only to administrator-managed databases. |
| ``` -l {[PRIMARY] \| [PHYSICAL _STANDBY] \| [LOGICAL _STANDBY] \| [SNAPSHOT _STANDBY]} ``` | The database modes for which the service should be started automatically.  Using SRVCTL to manually start a service is not affected by the service role.  Note: The `-l` parameter is only used at database startup and by the Oracle Data Guard Broker. All manual service startup must specify the name of the service to be started by the user.  See Also: [Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/sofo.htm#DGBKR3548) if you specify `-l` |
| ``` -q {TRUE \| FALSE} ``` | Indicates whether AQ HA notifications should be enabled (`TRUE`) for this service |
| ``` -x {TRUE \| FALSE} ``` | Indicates whether or not Distributed Transaction Processing should be enabled for this service  Note: This option is available only with Oracle Clusterware. |
| ``` -j {SHORT \| LONG} ``` | Connection Load Balancing Goal |
| ``` -B {NONE \| SERVICE_TIME \| THROUGHPUT} ``` | Runtime Load Balancing Goal |
| ``` -e {NONE \| SESSION \| SELECT} ``` | Failover type |
| ``` -m {NONE \| BASIC} ``` | Failover method |
| ``` -z failover_retries ``` | The number of failover retry attempts |
| ``` -w failover_delay ``` | The time delay between failover attempts |
| ``` -y {AUTOMATIC \| MANUAL} ``` | Service management policy |

##### Examples

An example of moving a service member from one instance to another is:

```
$ srvctl modify service -d crm -s crm -i crm1 -t crm2
```

An example of changing an available instance to a preferred instance is:

```
srvctl modify service -d crm -s crm -i crm1 -r
```

The following command exchanges a preferred and available instance:

```
$ srvctl modify service -d crm -s crm -n -i crm1 -a crm2
```

#### srvctl modify srvpool

Modifies a server pool in a cluster. If minimum size, maximum size, and importance are numerically increased, then the CRS daemon may attempt to reassign servers to this server pool, if by resizing other server pools have comparatively lower minimum size and importance, to satisfy new sizes of this server pool.

##### Syntax and Options

Use the `srvctl modify srvpool` command with the following syntax:

```
srvctl modify srvpool -g server_pool [-i importance] [-l min_size]
     [-u max_size] [-n node_name_list] [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-80 srvctl modify srvpool Options

| Option | Description |
| --- | --- |
| ``` -g server_pool ``` | The name of the server pool to modify, |
| ``` -i importance ``` | The new importance of the server pool. |
| ``` -l min_size ``` | The new minimum size of the server pool. The default value is 0. |
| ``` -u max_size ``` | The new maximum size of the server pool. A value of `-1` sets the server pool maximum size to UNLIMITED. |
| ``` -n node_name_list ``` | A comma-delimited list of candidate server names. |
| ``` -f ``` | Force the operation even though the utility stops some resource(s). |

##### Example

The following example changes the importance rank to 0, the minimum size to 2, and the maximum size to 4 for the server pool `srvpool1` on the nodes `mynode3` and `mynode4`:

```
$ srvctl modify srvpool -g srvpool1 -i 0 -l 2 -u 4 -n mynode3, mynode4
```

### relocate

The `relocate` command causes the specified object to run on a different node. The specified object must be running already.

The relocation of the object is temporary until you modify the configuration. The previously described `modify` command permanently changes the configuration.

Table A-81 srvctl relocate Summary

| Command | Description |
| --- | --- |
| `srvctl relocate cvu` | Temporarily relocates the Cluster Verification Utility |
| `srvctl relocate database` | Relocates an Oracle RAC One Node database to a different node |
| `srvctl relocate gns` | Relocates GNS to a different node |
| `srvctl relocate oc4j` | Relocates an OC4J instance to a different node |
| `srvctl relocate scan` | Relocates a SCAN VIP from its current hosting server to another server within the cluster |
| `srvctl relocate scan_listener` | Relocates a SCAN listener from its current hosting server to another server within the cluster |
| `srvctl relocate server` | Relocates named servers to another server pool |
| `srvctl relocate service` | Relocates the named service names from one named instance to another named instance |
| `srvctl relocate vip` | Relocates a specific VIP from one node to another within the cluster |

#### srvctl relocate cvu

Starting with Oracle Database 11g release 2 (11.2.0.2), this command temporarily relocates the CVU to another node in a cluster.

##### Syntax and Options

Use the `srvctl relocate cvu` command with the following syntax:

```
srvctl relocate cvu [-n node_name
]
```

Table A-82 srvctl relocate cvu Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |

##### Examples

An example of this command to temporarily relocate CVU to another node in a cluster is:

```
$ srvctl relocate cvu -n crmnode2
```

#### srvctl relocate database

Starting with Oracle Database 11g release 2 (11.2.0.2), the `srvctl relocate database` command initiates the relocation of an Oracle RAC One Node database from one node to another node. This command also cleans up after a failed relocation.

The `srvctl relocate database` command can only be used for relocating Oracle RAC One Node databases.

Syntax and Options

Use the `srvctl relocate database` command with the following syntax:

```
srvctl relocate database -d db_unique_name {[-n target_node] [-w timeout] | -a
 [-r]} [-v]
```

Table A-83 srvctl relocate database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database. |
| ``` -n target ``` | Target node to which to relocate the Oracle RAC One Node database.  Note: You must supply this option if you are relocating an administrator-managed Oracle RAC One Node database. |
| ``` -w timeout ``` | Online database relocation timeout, in minutes, for Oracle RAC One Node databases. The default is `30`. |
| ``` -a ``` | Abort failed online database relocation. |
| ``` -r ``` | Removes the target node of a failed online relocation request from the candidate server list of an administrator-managed Oracle RAC One Node database. |
| ``` -v ``` | Verbose output. |

Usage Notes

- If the Oracle RAC One Node database you want to relocate is not running, then the command returns an error.
- If another online database relocation is active for this Oracle RAC One Node database, then the command returns an error.
- If an online database relocation for this Oracle RAC One Node database has failed and the target nodes are not the same for either relocation, then the command returns an error instructing you to abort the failed online database relocation and then initiate a new one.
- If an online database relocation for this Oracle RAC One Node database has failed and the target nodes are the same (or you do not specify the target), then the command attempts to relocate the database.

Example

The following example relocates an Oracle RAC One Node database named `rac1` to a server called `node7`.

```
srvctl relocate database -d rac1 -n node7
```

#### srvctl relocate gns

Relocates GNS from its current hosting node to another node within the cluster.

##### Syntax and Options

Use the `srvctl relocate gns` command with the following syntax:

```
srvctl relocate gns [-n node_name]
```

Notes:

- On Linux and UNIX systems, you must be logged in as `root` and on Windows, you must be logged in as a user with Administrator privileges to run this command.
- This command is only available with Oracle Clusterware.

Table A-84 srvctl relocate gns Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of the node to which you want to move GNS |

##### Example

An example of this command is:

```
$ srvctl relocate gns -n node1
```

#### srvctl relocate oc4j

Relocates an OC4J instance from its current hosting node to another node within the cluster.

##### Syntax and Options

Use the `srvctl relocate oc4j` command with the following syntax:

```
srvctl relocate oc4j [-n node_name] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-85 srvctl relocate oc4j Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of the node to relocate the OC4J instance to. |
| `-v` | Display verbose output |

##### Example

An example of this command is:

```
$ srvctl relocate oc4j -n staih01 -v
```

#### srvctl relocate scan

Relocates a specific SCAN VIP from its current hosting node to another node within the cluster.

##### Syntax and Options

Use the `srvctl relocate scan` command with the following syntax:

```
srvctl relocate scan -i ordinal_number
 [-n node_name]
```

Note:

This command is only available with Oracle Clusterware.

Table A-86 srvctl relocate scan Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | An ordinal number that identifies which SCAN VIP you want to relocate. The range of values you can specify for this option is 1 to 3. |
| ``` -n node_name ``` | The name of a single node.  If you do not specify this option, then the utility chooses the node to which the SCAN VIP is relocated. |

##### Example

An example of this command is:

```
$ srvctl relocate scan -i 1 -n node1
```

#### srvctl relocate scan\_listener

Relocates a specific SCAN listener from its current hosting node to another node within the cluster.

##### Syntax and Options

Use the `srvctl relocate scan_listener` command with the following syntax:

```
srvctl relocate scan_listener -i ordinal_number
 [-n node_name]
```

Note:

This command is only available with Oracle Clusterware.

Table A-87 srvctl relocate scan\_listener Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | An ordinal number that identifies which SCAN VIP you want to relocate. The range of values you can specify for this option is 1 to 3. |
| ``` -n node_name ``` | The name of a single node.  If you do not specify this option, then the utility chooses the node to which the SCAN VIP is relocated. |

##### Example

An example of this command is:

```
$ srvctl relocate scan_listener -i 1 -n node3
```

#### srvctl relocate server

Relocates servers to a server pool in the cluster.

##### Syntax and Options

Use the `srvctl relocate server` command with the following syntax:

```
srvctl relocate server -n "server_name_list
" -g server_pool_name [-f]
```

Table A-88 srvctl relocate server Options

| Option | Description |
| --- | --- |
| ``` -n "server_name_list" ``` | A single server name or a comma-delimited list of server names enclosed in double quotation marks (`""`) that you want to relocate to a different server pool. |
| ``` -g server_pool_name ``` | The name of the server pool to which you want to move servers. |
| ``` -f ``` | Use the `-f` option to force the relocation of servers even if it means stopping some resources. |

##### Example

An example of this command is:

```
$ srvctl relocate server -n "server1, server2" -g sp3
```

#### srvctl relocate service

Relocates the named service names from one named instance to another named instance. The `srvctl relocate` command works on only one source instance and one target instance at a time, relocating a service from a single source instance to a single target instance. The target instance must be on the preferred or available list for the service.

##### Syntax and Options

Use the `srvctl relocate service` command with the following syntax:

```
srvctl relocate service -d db_unique_name
 -s service_name

    {-c source_node
 -n target_node
 | -i old_instance_name
 -t new_instance_name
}
    [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-89 srvctl relocate service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name |
| ``` -c source_node ``` | Name of the node where the service is currently running |
| ``` -n target_node ``` | Name of node where the service should be relocated |
| ``` -i old_instance_name ``` | Old instance name |
| ``` -t new_instance_name ``` | New instance name |
| ``` -f ``` | Disconnect all sessions during stop or relocate service operations |

##### Example

To temporarily relocate a named service member from `crm1` to `crm3`:

```
$ srvctl relocate service -d crm -s crm -i crm1 -t crm3
```

#### srvctl relocate vip

Relocates a specific VIP from its current hosting node to another node within the cluster.

##### Syntax and Options

Use the `srvctl relocate vip` command with the following syntax:

```
srvctl relocate vip -i vip_name
 [-n node_name] [-f]
```

Table A-90 srvctl relocate vip Options

| Option | Description |
| --- | --- |
| ``` -i vip_name ``` | Specify the name of the VIP you want to relocate. |
| ``` -n node_name ``` | Specify the name of a single target node to which you want to relocate the VIP. |
| ``` -f ``` | Specify this option to force the relocation of the VIP. |

##### Example

An example of this command is:

```
$ srvctl relocate vip -i vip1 -n node3
```

### remove

Removes the configuration information for the specified target from Oracle Clusterware. Environment settings for the object are also removed. Using this command does not destroy the specified target.

Use the `remove` verb to remove the associated resource from the management of Oracle Clusterware or Oracle Restart. Depending on the noun used, you can remove databases, services, nodeapps, Oracle ASM, Oracle Notification Service, and listeners.

If you do not use the force flag (`-f`), then Oracle Clusterware or Oracle Restart prompts you to confirm whether to proceed. If you use the force (`-f`) option, then the remove operation proceeds without prompting and continues processing even when it encounters errors. Even when the Oracle Clusterware resources cannot be removed, the OCR configuration is removed, so that the object now appears not to exist, but there are still Oracle Clusterware resources. Use the force flag (`-f`) option with extreme caution because this could result in an inconsistent OCR.

To use the `remove` verb, you must first stop the node applications, database, instance, or service for which you are specifying `srvctl remove`. Oracle recommends that you perform a disable operation before using this command, but this is not required. You must stop the target object before running the `srvctl remove` command. See the `stop` command.

Table A-91 srvctl remove Summary

| Command | Description |
| --- | --- |
| `srvctl remove asm` | Removes Oracle ASM instances |
| `srvctl remove cvu` | Removes the Cluster Verification Utility configured for the cluster |
| `srvctl remove database` | Removes a database and configuration |
| `srvctl remove diskgroup` | Removes a disk group from the Oracle Clusterware or Oracle Restart configuration |
| `srvctl remove filesystem` | Removes the configuration for an Oracle ACFS volume |
| `srvctl remove gns` | Removes GNS |
| `srvctl remove instance` | Removes instances and configurations of administrator-managed databases |
| `srvctl remove listener` | Removes the configuration of the specified listener from Oracle Clusterware or Oracle Restart |
| `srvctl remove nodeapps` | Removes node applications |
| `srvctl remove oc4j` | Removes the OC4J instance configuration |
| `srvctl remove ons` | Removes Oracle Notification Service instances |
| `srvctl remove scan` | Removes all Oracle Clusterware resources for all SCAN VIPs |
| `srvctl remove scan_listener` | Removes all Oracle Clusterware resources for all SCAN listeners |
| `srvctl remove service` | Removes services from the Oracle Clusterware or Oracle Restart configuration |
| `srvctl remove srvpool` | Removes a specific server pool |
| `srvctl remove vip` | Removes specific VIPs |

#### srvctl remove asm

Removes the Oracle ASM resource.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl remove asm` command with the following syntax:

```
srvctl remove asm [-f]
```

The `-f` option is the only option you can use with this command and it forcefully removes an Oracle ASM resource.

##### Example

An example of this command is:

```
$ srvctl remove asm -f
```

#### srvctl remove cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command removes CVU from an Oracle Clusterware configuration.

##### Syntax and Options

Use the `srvctl remove cvu` command with the following syntax:

```
srvctl remove cvu [-f]
```

Use the `-f` option to remove a running or starting CVU.

##### Examples

An example of this command to remove CVU is:

```
$ srvctl remove cvu -f
```

#### srvctl remove database

Removes a database configuration.

##### Syntax and Options

Use the `srvctl remove database` command with the following syntax:

```
srvctl remove database -d db_unique_name
 [-f] [-y]
```

Table A-92 srvctl remove database Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -f ``` | Force remove |
| ``` -y ``` | Suppress prompts |

##### Example

An example of this command is:

```
$ srvctl remove database -d crm
```

#### srvctl remove diskgroup

Removes a specific Oracle ASM disk group resource from Oracle Clusterware or Oracle Restart.

##### Syntax and Options

Use the `srvctl remove diskgroup` command with the following syntax:

```
srvctl remove diskgroup -g diskgroup_name
 [-n node_list
] [-f]
```

Table A-93 srvctl remove diskgroup Options

| Option | Description |
| --- | --- |
| ``` -g diskgroup_name ``` | The Oracle ASM disk group name. |
| ``` -n node_list ``` | Comma-delimited list of node nodes.  Note: This option is available only with Oracle Clusterware. |
| ``` -f ``` | Force remove. |

##### Example

An example of this command is:

```
$ srvctl remove diskgroup -g DG1 -f
```

#### srvctl remove filesystem

Removes a specific Oracle ACFS volume resource.

##### Syntax and Options

Use the `srvctl remove filesystem` command with the following syntax:

```
srvctl remove filesystem -d volume_device_name
 [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-94 srvctl remove filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | The Oracle ACFS volume device name |
| ``` -f ``` | Force remove |

##### Example

An example of this command is:

```
$ srvctl remove filesystem -d /dev/asm/d1volume293
```

#### srvctl remove gns

Removes GNS from the cluster.

##### Syntax and Options

Use the `srvctl remove gns` command with the following syntax:

```
srvctl remove gns [-f]
```

The only option for this command is `-f`, which indicates GNS should be removed regardless of any errors that might occur.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl remove gns
```

#### srvctl remove instance

Removes the configurations for an instance of an administrator-managed database. To remove the configurations of a policy-managed database, you must shrink the size of the server pool with the `srvctl modify srvpool` command.

If you use the `-f` option, then any services running on the instance stop. Oracle recommends that you reconfigure services to not use the instance to be removed as a preferred or available instance before removing the instance.

##### Syntax and Options

Use the `srvctl remove instance` command with the following syntax:

```
srvctl remove instance -d db_unique_name
 -i instance_name [-f]
```

Notes:

- This command is only available with Oracle Clusterware and Oracle RAC.
- If you attempt to use this command on an Oracle RAC One Node database, then the command returns an error stating that cannot remove the instance except by removing the database.

Table A-95 srvctl remove instance Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database. |
| ``` -i instance_name ``` | Instance name. |
| ``` -f ``` | Specify this option to skip checking that the instance is not running, and remove it even though it is running. This option also skips checking that the instance has no running services using it, and causes those services to stop before the instance is removed. |

##### Example

An example of this command is:

```
$ srvctl remove instance -d crm -i crm01
```

#### srvctl remove listener

Removes the configuration of the specified listener from Oracle Clusterware or Oracle Restart.

##### Syntax and Options

Use the `srvctl remove listener` command with the following syntax:

```
srvctl remove listener [-l listener_name] [-a] [-f]
```

Table A-96 srvctl remove listener Options

| Options | Description |
| --- | --- |
| ``` -l listener_name ``` | Name of the listener that you want to remove.  If you do not specify a listener name, then the listener name defaults to `LISTENER`. |
| ``` -a ``` | Removes all listener configurations. |
| ``` -f ``` | Specify this option to skip checking whether there are other resources that depend on this listener, such as databases, and remove the listener anyway. |

##### Examples

The following command removes the configuration of the listener named `lsnr01`:

```
$ srvctl remove listener -l lsnr01
```

#### srvctl remove nodeapps

Removes the node application configuration. You must have full administrative privileges to run this command. On Linux and UNIX systems, you must be logged in as `root` and on Windows systems, you must be logged in as a user with Administrator privileges.

##### Syntax

Use the `srvctl remove nodeapps` command as follows:

```
srvctl remove nodeapps [-f] [-y] [-v]
```

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
# srvctl remove nodeapps
```

Table A-97 srvctl remove nodeapps Options

| Options | Description |
| --- | --- |
| ``` -f ``` | Force remove |
| ``` -y ``` | Suppress prompts |
| ``` -v ``` | Verbose output |

#### srvctl remove oc4j

Removes the OC4J instance from the Oracle Clusterware configuration.

##### Syntax and Options

Use the `srvctl remove oc4j` command with the following syntax:

```
srvctl remove oc4j [-f] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-98 srvctl remove oc4j Options

| Options | Description |
| --- | --- |
| ``` -f ``` | Force remove |
| ``` -v ``` | Verbose output |

#### srvctl remove ons

Removes Oracle Notification Service from the Oracle Grid Infrastructure home.

##### Syntax and Options

Use the `srvctl remove ons` command with the following syntax:

```
srvctl remove ons [-f] [-v]
```

Note:

This command is only available with Oracle Restart.

Table A-99 srvctl remove ons Options

| Options | Description |
| --- | --- |
| ``` -f ``` | Force remove |
| ``` -v ``` | Verbose output |

#### srvctl remove scan

Removes Oracle Clusterware resources from all SCAN VIPs.

##### Syntax and Options

Use the `srvctl remove scan` command with the following syntax:

```
srvctl remove scan [-f]
```

The only option available for this command is `-f`, which removes the SCAN VIPs even though there are SCAN listeners running that are dependent on the SCAN VIPs. SCAN VIPs that are running are not stopped before the resources are removed, which may require manual cleanup.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl remove scan -f
```

#### srvctl remove scan\_listener

Removes Oracle Clusterware resources from all SCAN listeners.

##### Syntax and Options

Use the `srvctl remove scan_listener` command with the following syntax:

```
srvctl remove scan_listener [-f]
```

The only option available for this command is `-f`, which removes the resource even if the listener(s) is running, without stopping the listener.

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl remove scan_listener -f
```

#### srvctl remove service

Removes the configuration for a service.

##### Syntax and Options

Use the `srvctl remove service` command as follows:

```
srvctl remove service -d db_unique_name
 -s service_name
 [-i instance_name] [-f]
```

Table A-100 srvctl remove service Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name ``` | Service name |
| ``` -i instance_name ``` | Instance name  Note: This option is available only for Oracle Clusterware. |
| ``` -f ``` | Removes the service resource even though the service is running |

##### Examples

An example of this command is:

```
$ srvctl remove service -d crm -s sales
```

The following example removes the services from specific instances:

```
$ srvctl remove service -d crm -s sales -i crm01,crm02
```

#### srvctl remove srvpool

Removes a specific server pool. If there are databases or services that depend upon this server pool, then remove them first so this operation succeeds.

If you successfully remove `server_pool`, then the CRS daemon may assign its servers to other server pools depending upon their minimum size, maximum size, and importance. The CRS daemon may also return these servers to its Free server pool.

##### Syntax and Options

Use the `srvctl remove srvpool` command with the following syntax:

```
srvctl remove srvpool -g server_pool
```

Note:

This command is only available with Oracle Clusterware.

##### Example

An example of this command is:

```
$ srvctl remove srvpool -g srvpool1
```

#### srvctl remove vip

Removes specific VIPs.

##### Syntax and Options

Use the `srvctl remove vip` command with the following syntax:

```
srvctl remove vip -i "vip_name_list" [-f] [-y] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-101 srvctl remove vip Options

| Option | Description |
| --- | --- |
| ``` -i "vip_name_list" ``` | A comma-delimited list of VIP names surrounded by double quotation marks (`""`) |
| ``` -f ``` | Force remove |
| ``` -y ``` | Suppress prompts |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
$ srvctl remove vip -i "vip1,vip2,vip3" -f -y -v
```

### setenv

The `setenv` command sets values for the environment in the configuration file. Use `setenv` to set environment variables—items such as language or `TNS_ADMIN` —for Oracle Clusterware that you would typically set in your profile or session when you manage this database or database instance.

The `unsetenv` command unsets values for the environment in the configuration file.

Table A-102 srvctl setenv Summary

| Command | Description |
| --- | --- |
| `srvctl setenv asm` | Administers environment configuration for Oracle ASM |
| `srvctl setenv database` | Administers cluster database environment configurations |
| `srvctl setenv listener` | Administers listener environment configurations  Note: You cannot use this command to administer SCAN listeners. |
| `srvctl setenv nodeapps` | Administers node application environment configurations |
| `srvctl setenv vip` | Administers VIP environment configurations |

#### srvctl setenv asm

Administers Oracle ASM environment configurations.

##### Syntax and Options

Use the `srvctl setenv asm` command with the following syntax:

```
srvctl setenv asm {-t "name
=val
[,name
=val
][...]" | -T "name
=val
"}
```

Table A-103 srvctl setenv asm Options

| Options | Description |
| --- | --- |
| ``` -t "name=val[,name=val ][...]" ``` | Comma-delimited list of name-value pairs of environment variables |
| ``` -T "name=val" ``` | Enables single environment variable to be set to a value that contains commas or other special characters |

##### Example

The following example sets the language environment configuration for Oracle ASM:

```
$ srvctl setenv asm -t LANG=en
```

#### srvctl setenv database

Administers cluster database environment configurations.

##### Syntax and Options

Use the `srvctl setenv database` command with the following syntax:

```
srvctl setenv database -d db_unique_name
 
     {-t "name
=val
[,name
=val
][...]" | -T "name
=val
"}
```

Table A-104 srvctl setenv database Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -t "name=val,..." ``` | Comma-delimited list of name-value pairs of environment variables |
| ``` -T "name=val" ``` | Enables single environment variable to be set to a value that contains commas or other special characters |

##### Example

The following example sets the language environment configuration for a cluster database:

```
$ srvctl setenv database -d crm -t LANG=en
```

#### srvctl setenv listener

Administers listener environment configurations.

##### Syntax and Options

Use the `srvctl setenv listener` with the following syntax:

```
srvctl setenv listener [-l listener_name
] 
     {-t "name
=val
[,name
=val
][...]" | -T "name
=val
"}
```

Table A-105 srvctl setenv listener Options

| Options | Description |
| --- | --- |
| ``` -l listener_name ``` | Name of the listener.  If you do not specify this option, then the listener name defaults to `LISTENER`. |
| ``` -t "name=val" ``` | Comma-delimited list of name-value pairs of environment variables. |
| ``` -T "name=val" ``` | Enables single environment variable to be set to a value that contains commas or other special characters. |

##### Example

The following example sets the language environment configuration for the default listener:

```
$ srvctl setenv listener -t LANG=en
```

#### srvctl setenv nodeapps

Sets the environment variables for the node application configurations.

##### Syntax and Options

Use the `srvctl setenv nodeapps` command as follows:

```
srvctl setenv nodeapps {-t "name
=val
[,name
=val
][...]" | -T "name
=val
"} [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-106 srvctl setenv nodeapps Options

| Options | Description |
| --- | --- |
| ``` -t "name =val [,name =val ] [...]" ``` | Comma-delimited list of name-value pairs of environment variables |
| ``` -T "name=val" ``` | Enables single environment variable to be set to a value that contains commas or other special characters |
| ``` -v ``` | Verbose output |

##### Example

To set an environment variable for a node application:

```
$ srvctl setenv nodeapps -T "CLASSPATH=/usr/local/jdk/jre/rt.jar" -v
```

#### srvctl setenv vip

Administers cluster VIP environment configurations.

##### Syntax and Options

Use the `srvctl setenv vip` command with the following syntax:

```
srvctl setenv vip -i vip_name
 {-t "name
=val
[,name
=val
,...]" | -T "name
=val"
}
```

Note:

This command is only available with Oracle Clusterware.

Table A-107 srvctl setenv vip Options

| Options | Description |
| --- | --- |
| ``` -i vip_name ``` | Name of the VIP |
| ``` -t "name=val,..." ``` | Comma-delimited list of name-value pairs of environment variables |
| ``` -T "name=val" ``` | Enables single environment variable to be set to a value that contains commas or other special characters |

##### Example

The following example sets the language environment configuration for a cluster VIP:

```
$ srvctl setenv vip -i crm1-vip -t LANG=en
```

### start

Starts Oracle Restart or Oracle Clusterware enabled, non-running applications for the database, all or named instances, all or named service names, or node-level applications. For the `start` command, and for other operations that use a connect string, if you do not provide a connect string, SRVCTL uses `/as sysdba` to perform the operation. To run such operations, the owner of the `oracle` binary executables must be a member of the OSDBA group, and users running the commands must also be in the OSDBA group.

Table A-108 srvctl start Summary

| Command | Description |
| --- | --- |
| `srvctl start asm` | Starts Oracle ASM instances |
| `srvctl start cvu` | Starts the Cluster Verification Utility |
| `srvctl start database` | Starts the cluster database and its instances |
| `srvctl start diskgroup` | Starts a specified disk group on a number of nodes |
| `srvctl start filesystem` | Starts the Oracle ACFS volume resource |
| `srvctl start gns` | Starts GNS |
| `srvctl start home` | Starts Oracle Clusterware-managed or Oracle Restart-managed resources in a specific Oracle home |
| `srvctl start instance` | Starts the instance |
| `srvctl start listener` | Starts the specified listener or listeners |
| `srvctl start nodeapps` | Starts the node applications |
| `srvctl start oc4j` | Starts the OC4J instance |
| `srvctl start ons` | Starts the Oracle Notification Service daemon for Oracle Restart |
| `srvctl start scan` | Starts all SCAN VIPs |
| `srvctl start scan_listener` | Starts all SCAN listeners |
| `srvctl start service` | Starts the service |
| `srvctl start vip` | Starts a VIP |

#### srvctl start asm

Starts an Oracle ASM instance.

Notes:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl start asm` command with the following syntax:

```
srvctl start asm [-n node_name
] [-o start_options
]
```

Table A-109 srvctl start asm Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  Note: This option is available only with Oracle Clusterware. |
| ``` -o start_options ``` | Options to startup command, for example `OPEN`, `MOUNT`, or `NOMOUNT`  Note: For multi-word startup options, such as `read only` and `read write`, separate the words with a space and enclose in double quotation marks (`""`). For example, `"read only"`.  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for more information about startup options |

##### Examples

An example of this command to start an Oracle ASM instance on a single node of a cluster is:

```
$ srvctl start asm -n crmnode1
```

An example to start an Oracle ASM instance on all nodes in the cluster, or for a noncluster database, is:

```
$ srvctl start asm
```

#### srvctl start cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command starts the CVU on one node in a cluster. If you specify a node name, then CVU starts on that node.

##### Syntax and Options

Use the `srvctl start cvu` command with the following syntax:

```
srvctl start cvu [-n node_name
]
```

Table A-110 srvctl start cvu Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |

##### Examples

An example of this command to start CVU on a single node of a cluster is:

```
$ srvctl start cvu -n crmnode1
```

#### srvctl start database

Starts a cluster database and its enabled instances and all listeners on nodes with database instances. You can disable listeners that should not be started.

##### Syntax and Options

Use the `srvctl start database` command with the following syntax:

```
srvctl start database -d db_unique_name
 [-o start_options
] [-n node_name]
```

Table A-111 srvctl start database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -o start_options ``` | Options for startup command (for example: `OPEN`, `MOUNT`, or `NOMOUNT`)  Notes:  - This command option supports all database startup options. - For multi-word startup options, such as `read only` and `read write`, separate the words with a space and enclose in double quotation marks (`""`). For example, `"read only"`.  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for more information about startup options |
| ``` -n node_name ``` | The name of the node on which you want to start the database  Notes:  - This command only applies to Oracle RAC One Node databases. - The node you specify must be in the candidate list for an administrator-managed Oracle RAC One Node database or in the server pool for a policy-managed Oracle RAC One Node database. - If the database is already running on a node than the one you specify, then the command returns an error. - If you do not specify a node, then Oracle Clusterware chooses which node on which to start the Oracle RAC One Node database according to its policies, such as dispersion, number of resources, and order of candidate nodes. - If there is an active online database relocation for the Oracle RAC One Node database you are attempting to start, then both instances will already be running and the command returns an error message saying so (remember that only during an online database relocation are two instances of an Oracle RAC One Node database in existence). 	If the online database relocation failed for the Oracle RAC One Node database and you do not specify a node, then the command attempts to start both database instances. 	If the online database relocation failed for the Oracle RAC One Node database and you specify a node, then the command attempts to abort the failed relocation and start the instance on that node. |

##### Example

An example of this command is:

```
$ srvctl start database -d crm -o open
```

#### srvctl start diskgroup

Starts a specific disk group resource on a number of specified nodes.

##### Syntax and Options

Use the `srvctl start diskgroup` command with the following syntax:

```
srvctl start diskgroup -g diskgroup_name
 [-n node_list
]
```

Table A-112 srvctl start diskgroup Options

| Option | Description |
| --- | --- |
| ``` -g diskgroup_name ``` | The Oracle ASM disk group name |
| ``` -n node_list ``` | Comma-delimited list of node names on which to start the disk group resource  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl start diskgroup -g diskgroup1 -n mynode1,mynode2
```

#### srvctl start filesystem

Starts the Oracle ACFS volume resource.

##### Syntax and Options

Use the `srvctl start filesystem` command with the following syntax:

```
srvctl start filesystem -d volume_device_name
 [-n node_name
]
```

Note:

This command is only available with Oracle Clusterware.

Table A-113 srvctl start filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | The Oracle ACFS volume device name |
| ``` -n node_name ``` | The name of the node on which the Oracle ACFS volume resource should be started.  If you do not specify this option, then the utility starts the Oracle ACFS volume resource on all the available nodes in the cluster. |

#### srvctl start gns

Starts GNS on a specific node, or all nodes in the cluster.

##### Syntax and Options

Use the `srvctl start gns` command with the following syntax:

```
srvctl start gns [-l log_level] [-n node_name
]
```

Note:

This command is only available with Oracle Clusterware.

Table A-114 srvctl start gns Options

| Option | Description |
| --- | --- |
| ``` -l log_level ``` | Specify the level of logging with which GNS should run. Log levels vary between 1 (minimal tracing) and 6 (traces everything and is time consuming). |
| ``` -n node_name ``` | The name of a node in the cluster where you want to start GNS. |

#### srvctl start home

Starts all the Oracle Restart-managed or Oracle Clusterware-managed resources on the specified Oracle home.

##### Syntax and Options

Use the `srvctl start home` command with the following syntax:

```
srvctl start home -o Oracle_home
 -s state_file [-n node_name
]
```

Table A-115 srvctl start home Options

| Option | Description |
| --- | --- |
| ``` -o Oracle_home ``` | The path to the Oracle home for which you want to start the Oracle Restart or Oracle Clusterware-managed resources |
| ``` -s state_file ``` | The path name of the state file you specified when you ran either the `srvctl stop home` or the `srvctl status home` command. |
| ``` -n node_name ``` | The name of the node where the Oracle home resides.  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl start -o /u01/app/oracle/product/11.2.0/db_1 -s ~/state.txt
```

#### srvctl start instance

Starts instances in the cluster database and all listeners on nodes with database instances. You can disable listeners that should not be started.

##### Syntax and Options

Use the `srvctl start instance` command with the following syntax:

```
srvctl start instance -d db_unique_name
 {-n node_name -i "instance_name_list
"}
     [-o start_options
]
```

In Windows, you must enclose the list of comma-delimited instance names in double quotation marks (`""`).

Notes:

- This command is only available with Oracle Clusterware and Oracle RAC.
- If you run this command on an Oracle RAC One Node database, then the command returns an error instructing you to use the `database` noun, instead.

Table A-116 srvctl start instance Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -n node_name ``` | The name of a single node  Note: Use this option for policy-managed databases. |
| ``` -i "instance_name_list" ``` | Specify either exactly one instance name or a comma-delimited list of instance names  Note: Use this option for administrator-managed databases. |
| ``` -o start_options ``` | Options for startup command (for example: `OPEN`, `MOUNT`, or `NOMOUNT`)  Note: For multi-word startup options, such as `read only` and `read write`, separate the words with a space and enclose in double quotation marks (`""`). For example, `"read only"`.  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for more information about startup options |

##### Example

An example of starting an instance for a policy-managed database is:

```
$ srvctl start instance -d crm -n node2
```

An example of starting an instance for an administrator-managed database is:

```
$ srvctl start instance -d crm -i "crm2,crm3"
```

#### srvctl start listener

Starts the default listener on the specified `node_name`, or starts all of the listeners represented in a given list of listener names, that are registered with Oracle Clusterware on the given node.

##### Syntax and Options

Use the `srvctl start listener` command with the following syntax:

```
srvctl start listener [-n node_name
] [-l listener_name_list]
```

Table A-117 srvctl start listener Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  Note: This option is available only with Oracle Clusterware. |
| ``` -l listener_name_list ``` | Listener name  If you do not specify this option, then the listener name defaults to `LISTENER`. |

##### Example

An example of this command is:

```
$ srvctl start listener -n mynode1
```

#### srvctl start nodeapps

Starts node-level applications on a node or all nodes in the cluster.

##### Syntax and Options

Use the `srvctl start nodeapps` command with the following syntax:

```
srvctl start nodeapps [-n node_name
] [-g] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-118 srvctl start nodeapps Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  If you do not specify this option, then the utility starts the nodeapps on all active nodes in the cluster. |
| ``` -g ``` | Starts GSD, only |
| ``` -v ``` | Verbose output |

##### Example

An example of this command is:

```
srvctl start nodeapps
```

#### srvctl start oc4j

Starts the OC4J instance.

##### Syntax and Options

Use the `srvctl start oc4j` command with the following syntax:

```
srvctl start ocj4 [-v]
```

There is only one option for this command, `-v`, which is used to indicate that verbose output should be displayed.

Note:

This command is only available with Oracle Clusterware.

#### srvctl start ons

Starts the Oracle Notification Service daemon.

Note:

This command is only available with Oracle Restart.

##### Syntax and Options

Use the `srvctl start ons` command with the following syntax:

```
srvctl start ons [-v]
```

There is only one option for this command, `-v`, which is used to indicate that verbose output should be displayed.

#### srvctl start scan

Starts all SCAN VIPs, by default, or a specific SCAN VIP, on all nodes or a specific node in the cluster.

##### Syntax and Options

Use the `srvctl start scan` command with the following syntax:

```
srvctl start scan [-i ordinal_number
] [-n node_name]
```

Note:

This command is only available with Oracle Clusterware.

Table A-119 srvctl start scan Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | An ordinal number that identifies which SCAN VIP you want to start. The range of values you can specify for this option is 1 to 3.  If you do not specify this option, then the utility starts all the SCAN VIPs. |
| ``` -n node_name ``` | The name of a single node.  If you do not specify this option, then the utility starts the SCAN VIPs on all nodes in the cluster. |

##### Example

To start the SCAN VIP identified by the ordinal number 1 on the `node1` node, use the following command:

```
$ srvctl start scan -i 1 -n node1
```

#### srvctl start scan\_listener

Starts all SCAN listeners, by default, or a specific listener on all nodes or a specific node in the cluster.

##### Syntax and Options

Use the `srvctl start scan_listener` command with the following syntax:

```
srvctl start scan_listener [-n node_name
] [-i ordinal_number
]
```

Note:

This command is only available with Oracle Clusterware.

Table A-120 srvctl start scan\_listener Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | An ordinal number that identifies which SCAN Listener you want to start. The range of values you can specify for this option is 1 to 3.  If you do not specify this option, then the utility starts all the SCAN listeners. |
| ``` -n node_name ``` | The name of a single node.  If you do not specify this option, then the utility starts the SCAN listeners on all nodes in the cluster. |

##### Example

An example of this command is:

```
$ srvctl start scan_listener -i 1
```

#### srvctl start service

Starts a service or multiple services on the specified instance. The `srvctl start service` command will fail if you attempt to start a service on an instance if that service is already running on its maximum number of instances, that is, its number of preferred instances. You may move a service or change the status of a service on an instance with the `srvctl modify service` and `srvctl relocate service` commands described later in this appendix.

Note:

All manual service startup must specify the name of the service to be started by the user.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/sofo.htm#DGBKR3548)

##### Syntax and Options

Use the `srvctl start service` command with the following syntax:

```
srvctl start service -d db_unique_name
 
            [-s "service_name_list
" [-n node_name
 | -i instance_name]] 
            [-o start_options
]
```

Table A-121 srvctl start service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s "service_name_list" ``` | Comma-delimited list of service names.  If you do not include this option, then SRVCTL starts all of the services for the specified database. |
| ``` -n node_name ``` | The name of the node where the service should be started. Use this option for policy-managed databases.  Note: This option is available only with Oracle Clusterware. |
| ``` -i instance_name ``` | The name of the instance for which the service should be started. Use this option for administrator-managed databases.  Note: This option is available only with Oracle Clusterware. |
| ``` -o start_options ``` | Options to startup command, such as `OPEN`, `MOUNT`, or `NOMOUNT`  Note: For multi-word startup options, such as `read only` and `read write`, separate the words with a space and enclose in double quotation marks (`""`). For example, `"read only"`.  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve045.htm#SQPUG128) for more information about startup options |

##### Examples

The following example starts a named service. If the instances that support these services, including available instances that the service uses for failover, are not running but are enabled, then SRVCTL starts them.

```
$ srvctl start service -d crm -s crm
```

The following example starts a named service on a specified instance:

```
$ srvctl start service -d crm -s crm -i crm2
```

#### srvctl start vip

Starts a specific VIP or a VIP on a specific node.

##### Syntax and Options

Use the `srvctl start vip` command with the following syntax:

```
srvctl start vip {-n node_name | -i vip_name } [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-122 srvctl start vip Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |
| ``` -i vip_name ``` | The VIP name |
| ``` -v ``` | Verbose start |

##### Example

An example of this command is:

```
$ srvctl start vip -i crm1-vip -v
```

### status

Displays the current state of a named database, instances, services, disk group, listener, node application, or other resource managed by Oracle Clusterware.

Table A-123 srvctl status Summary

| Command | Description |
| --- | --- |
| `srvctl status asm` | Displays the status of Oracle ASM instances |
| `srvctl status cvu` | Displays the status of the Cluster Verification Utility |
| `srvctl status database` | Displays the status of a database |
| `srvctl status diskgroup` | Displays status of a specific disk group on a number of nodes |
| `srvctl status filesystem` | Displays the status of an Oracle ACFS volume |
| `srvctl status gns` | Displays the status of GNS |
| `srvctl status home` | Displays the status of the resources associated with the specified Oracle home |
| `srvctl status instance` | Displays the status of a instance |
| `srvctl status listener` | Displays the status of a listener resource |
| `srvctl status nodeapps` | Displays the status of node applications |
| `srvctl status oc4j` | Determines which node is running the Oracle Database QoS Management server |
| `srvctl status ons` | Displays the status of Oracle Notification Service |
| `srvctl status scan` | Displays the status of SCAN VIPs |
| `srvctl status scan_listener` | Displays the status of SCAN listeners |
| `srvctl status server` | Displays the status of servers |
| `srvctl status service` | Displays the status of services |
| `srvctl status srvpool` | Displays the status of server pools |
| `srvctl status vip` | Displays the status of VIPs |

#### srvctl status asm

Displays the status of an Oracle ASM instance.

Note:

To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use the SRVCTL binary in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use the SRVCTL binary in the database home to manage Oracle ASM.

##### Syntax and Options

Use the `srvctl status asm` command with the following syntax:

```
srvctl status asm [-n node_name
] [-a] [-v]
```

Table A-124 srvctl status asm Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name. If you do not specify this option, the SRVCTL displays the status of all Oracle ASM instances.  Note: This option is available only with Oracle Clusterware. |
| ``` -a ``` | Print detailed status information. |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status asm -n crmnode1 -a
```

#### srvctl status cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command displays the current state of CVU on one node in a cluster. If you specify a node name, then the command checks CVU status on that node.

##### Syntax and Options

Use the `srvctl status cvu` command with the following syntax:

```
srvctl status cvu [-n node_name
]
```

Table A-125 srvctl status cvu Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |

##### Examples

An example of this command to check the status of CVU on a single node of a cluster is:

```
$ srvctl status cvu -n crmnode1
```

#### srvctl status database

Displays the status of instances and their services, and where the instances are running.

If you run this command on an Oracle RAC One Node database, then the output shows the status of any online database relocation (active, failed, or inactive), and the source and destination nodes of the relocation.

##### Syntax and Options

Use the `srvctl status database` command with the following syntax:

```
srvctl status database -d db_unique_name
 [-f] [-v]
```

Table A-126 srvctl status database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -f ``` | Include disabled applications |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status database -d crm -v
```

#### srvctl status diskgroup

Displays the status of a specific disk group on a number of specified nodes.

##### Syntax and Options

Use the `srvctl status diskgroup` command with the following syntax:

```
srvctl status diskgroup -g diskgroup_name
 [-n node_list
] [-a] [-v]
```

Table A-127 srvctl status diskgroup Options

| Option | Description |
| --- | --- |
| ``` -g diskgroup_name ``` | The Oracle ASM disk group name |
| ``` -n node_list ``` | Comma-delimited list of node names on which to check status of the disk group  Note: This option is available only with Oracle Clusterware. |
| ``` -a ``` | Display enabled status information of disk group |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status diskgroup -g diskgroup1 -n mynode1,mynode2 -a
```

#### srvctl status filesystem

Displays the status of the specified Oracle ACFS volume.

##### Syntax and Options

Use the `srvctl status filesystem` command with the following syntax:

```
srvctl status filesystem -d volume_device_name
 [-v]
```

Table A-128 srvctl status filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | The device name of the Oracle ACFS volume |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status filesystem -d /dev/asm/d1volume293
```

#### srvctl status gns

Displays the current state of GNS.

##### Syntax and Options

Use the `srvctl status gns` command with the following syntax:

```
srvctl status gns [-n node_name [-v]]
```

Note:

This command is only available with Oracle Clusterware.

Table A-129 srvctl status gns Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Specify a node on which GNS is running for which you want to display the state |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

#### srvctl status home

Displays the status of all the Oracle Restart-managed or Oracle Clusterware-managed resources for the specified Oracle home.

##### Syntax and Options

Use the `srvctl status home` command with the following syntax:

```
srvctl status home -o Oracle_home
 -s state_file [-n node_name
]
```

Table A-130 srvctl status home Options

| Option | Description |
| --- | --- |
| ``` -o Oracle_home ``` | The path to the Oracle home for which you want to start the Oracle Restart or Oracle Clusterware-managed resources |
| ``` -s state_file ``` | The path name the text file that holds the state information generated by this command. |
| ``` -n node_name ``` | The name of the node where the Oracle home resides.  Note: This option is available only with Oracle Clusterware. |

##### Example

An example of this command is:

```
$ srvctl status home -o /u01/app/oracle/product/11.2.0/db_1 -s ~/state.txt
```

#### srvctl status instance

Displays the status of instances.

##### Syntax and Options

Use the `srvctl status instance` command with the following syntax:

```
srvctl status instance -d db_unique_name
 {-n node_name | -i "instance_name_list
"}
     [-f] [-v]
```

Note:

This command is only available with Oracle Clusterware and Oracle RAC.

Table A-131 srvctl status instance Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -n node_name ``` | Node name  Note: Use this option for policy-managed databases |
| ``` -i "instance_name_list" ``` | Comma-delimited list of instance names  Note: Use this option for administrator-managed databases |
| ``` -f ``` | Include disabled applications |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status instance -d crm -i "crm1,crm2" -v
```

#### srvctl status listener

Displays the status of listener resources.

##### Syntax and Options

Use the `srvctl status listener` command with the following syntax:

```
srvctl status listener [-l listener_name
] [-n node_name
 [-v]]
```

Table A-132 srvctl status listener Options

| Option | Description |
| --- | --- |
| ``` -l listener_name ``` | Name of a listener.  If you do not specify this option, then the listener name defaults to `LISTENER` |
| ``` -n node_name ``` | Name of a cluster node.  Note: This option is available only for Oracle Clusterware. |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status listener -n node2
```

#### srvctl status nodeapps

Displays the status of node applications.

##### Syntax and Options

Use the `srvctl status nodeapps` command with the following syntax:

```
srvctl status nodeapps
```

Note:

This command is only available with Oracle Clusterware.

#### srvctl status oc4j

Determines which node is running the Oracle Database QoS Management server.

##### Syntax and Options

Use the `srvctl status oc4j` command with the following syntax:

```
srvctl status oc4j [-n node_name
 [-v]]
```

Note:

This command is only available with Oracle Clusterware.

Table A-133 srvctl status oc4j Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Specify a node on which the Oracle Database QoS Management server is running for which you want to display the state |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

#### srvctl status ons

Displays the current state of the Oracle Notification Service daemon.

Note:

This command is only available with Oracle Restart.

##### Syntax and Options

Use the `srvctl status ons` command with the following syntax:

```
srvctl status ons
```

#### srvctl status scan

Displays the status for all SCAN VIPs, by default, or a specific SCAN VIP.

##### Syntax and Options

Use the `srvctl status scan` command with the following syntax:

```
srvctl status scan [-i ordinal_number
 [-v]]
```

Note:

This command is only available with Oracle Clusterware.

Table A-134 srvctl status scan Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | Specify an ordinal number that identifies a specific SCAN VIP. The range of values you can specify for this option is 1 to 3. If you do not specify this option, then the utility displays the status of all SCAN VIPs in the cluster. |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status scan -i 1
```

#### srvctl status scan\_listener

Displays the status for all SCAN listeners, by default, or a specific listener.

##### Syntax and Options

Use the `srvctl status scan_listener` command with the following syntax:

```
srvctl status scan_listener [-i ordinal_number
 [-v]]
```

Note:

This command is only available with Oracle Clusterware.

Table A-135 srvctl status scan\_listener Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | Specify an ordinal number that identifies a specific SCAN VIP. The range of values you can specify for this option is 1 to 3. If you do not specify this option, then the utility displays the status of all SCAN VIPs in the cluster. |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status scan_listener -i 1
```

#### srvctl status server

Displays the current state of named servers.

##### Syntax and Options

Use the `srvctl status server` command with the following syntax:

```
srvctl status server -n "server_name_list
" [-a]
```

Table A-136 srvctl status server Options

| Option | Description |
| --- | --- |
| ``` -n "server_name_list" ``` | Comma-delimited list of server names. |
| ``` -a ``` | Print detailed status information. |

##### Example

The following example displays the status of a named server:

```
$ srvctl status server -n server11 -a
```

#### srvctl status service

Displays the status of a service.

For Oracle RAC One Node databases, if there is an online database relocation in process, then the `srvctl status service` command displays the source and destination nodes and the status of the relocation, whether it is active or failed.

##### Syntax and Options

Use the `srvctl status service` command with the following syntax:

```
srvctl status service -d db_unique_name
 [-s "service_name_list
"] [-f] [-v]
```

Table A-137 srvctl status service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s "service_name_list" ``` | Comma-delimited list of service names.  If you do not specify this option, then the utility lists the status of all the services for the specified database. |
| ``` -f ``` | Include disabled applications |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

The following example displays the status of a named service globally across the clustered database:

```
$ srvctl status service -d crm -s crm -v
```

#### srvctl status srvpool

Displays all server pool names and number of servers (and names of servers if you specify the `-a` option) that are currently assigned to each server pool, if you do not specify the `-g` option. When you specify the `-g` option, the command displays the preceding information for the specified server pool.

##### Syntax and Options

Use the `srvctl status srvpool` command with the following syntax:

```
srvctl status srvpool [-g server_pool] [-a]
```

Note:

This command is only available with Oracle Clusterware.

Table A-138 srvctl status srvpool Options

| Option | Description |
| --- | --- |
| ``` -g server_pool ``` | Name of the server pool |
| ``` -a ``` | Print detailed status information |

##### Example

An example of this command is:

```
$ srvctl status srvpool -g srvpool1 -a
```

#### srvctl status vip

Displays status for a specific VIP or a VIP on a specific node.

##### Syntax and Options

Use the `srvctl status vip` command with the following syntax:

```
srvctl status vip {-n node_name | -i vip_name} [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-139 srvctl status vip Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name |
| ``` -i vip_name ``` | The VIP name |
| ``` -v ``` | Displays `INTERNAL_STATE`, which indicates actions in progress by Oracle Clusterware, such as starting, stopping, or cleaning. If the internal state is STABLE, then the `-v` option displays nothing because this is the normal state. Additionally, the `-v` option displays `STATE_DETAILS`, which may indicate additional information provided by the resource about why it is in its current state. |

##### Example

An example of this command is:

```
$ srvctl status vip -i node1-vip
```

### stop

Stops the Oracle Clusterware applications for the database, all or named instances, all or named service names, listeners, or node level application resources. Only the Oracle Clusterware applications that are starting or running are stopped. Objects running outside of Oracle Clusterware are not stopped.

You should disable an object that you intend to remain stopped after you issue a `srvctl stop` command. See the `srvctl disable` command starting with `srvctl disable database`.

Notes:

- If the object is stopped and is not disabled, then it can restart as a result of another planned operation. The object does not restart as a result of a failure. Oracle recommends that you disable any object that should remain stopped after you issue a `stop` command.
- When you use the `-f` (force) flag to stop dependent applications, as well as the object, then those dependent applications do not restart when the object is later restarted or after the node fails. You must restart the dependent applications, manually, except for services with AUTOMATIC management policy when a database is stopped.

Table A-140 srvctl stop Summary

| Command | Description |
| --- | --- |
| `srvctl stop asm` | Stops Oracle ASM instances |
| `srvctl stop cvu` | Stops the Cluster Verification Utility resource |
| `srvctl stop database` | Stops the cluster database |
| `srvctl stop diskgroup` | Stops a specific disk group on a specified number of nodes |
| `srvctl stop filesystem` | Stops the Oracle ACFS volume resource |
| `srvctl stop gns` | Stops GNS |
| `srvctl stop home` | Stops the resources for the specified Oracle home |
| `srvctl stop instance` | Stops the instance |
| `srvctl stop listener` | Stops the specified listener or listeners |
| `srvctl stop nodeapps` | Stops the node-level applications |
| `srvctl stop oc4j` | Stops the OC4J instance |
| `srvctl stop ons` | Stops Oracle Notification Service |
| `srvctl stop scan` | Stops all SCAN VIPs |
| `srvctl stop scan_listener` | Stops all SCAN listeners |
| `srvctl stop service` | Stops the service |
| `srvctl stop vip` | Stops VIP resources |

#### srvctl stop asm

Stops an Oracle ASM instance.

##### Syntax and Options

Use the `srvctl stop asm` command with the following syntax:

```
srvctl stop asm [-n node_name
] [-o stop_options
] [-f]
```

Notes:

- To manage Oracle ASM on Oracle Database 11g release 2 (11.2) installations, use SRVCTL in the Oracle Grid Infrastructure home for a cluster (Grid home). If you have Oracle RAC or Oracle Database installed, then you cannot use SRVCTL in the database home to manage Oracle ASM.
- You cannot use this command when OCR is stored in Oracle ASM because it will not stop Oracle ASM. To stop Oracle ASM you must shut down Oracle Clusterware.

Table A-141 srvctl stop asm Option

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of the node on which to stop the Oracle ASM instance.  If you do not specify this option, then the utility stops the Oracle ASM instance on every active node in the cluster.  Note: This option is available only with Oracle Clusterware. |
| ``` -o stop_options ``` | Options for shutdown command, such as `NORMAL`, `TRANSACTIONAL`, `IMMEDIATE`, or `ABORT`  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm#SQPUG125) for more information about shutdown options |
| ``` -f ``` | Use this option to stop disk groups, file systems and databases that depend on Oracle ASM |

##### Example

An example of this command is:

```
$ srvctl stop asm -n crmnode1 -i +asm1
```

#### srvctl stop cvu

Starting with Oracle Database 11g Release 2 (11.2.0.2), this command stops the Cluster Verification Utility (CVU) that is either in the running or starting state.

##### Syntax and Options

Use the `srvctl stop cvu` command with the following syntax:

```
srvctl stop cvu [-f]
```

The `-f` option is the only option you can use with this command. The `-f` option forces CVU to stop.

##### Examples

An example of this command to stop CVU:

```
$ srvctl stop cvu
```

#### srvctl stop database

Stops a database, its instances, and its services. When the database later restarts, services with `AUTOMATIC` management start automatically but services with `MANUAL` management policy must be started manually.

##### Syntax and Options

Use the `srvctl stop database` command with the following syntax:

```
srvctl stop database -d db_unique_name
 [-o stop_options
] [-f]
```

Table A-142 srvctl stop database Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database. |
| ``` -o stop_options ``` | Use this option to specify `shutdown` command options, such as `NORMAL`, `TRANSACTIONAL`, `IMMEDIATE`, or `ABORT`  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm#SQPUG125) for more information about shutdown options |
| ``` -f ``` | This option stops the database, its instances, its services, and any resources that depend on those services |

##### Example

An example of this command is:

```
$ srvctl stop database -d crm -o NORMAL
```

#### srvctl stop diskgroup

Stops a specific disk group resource on a number of specified nodes.

##### Syntax and Options

Use the `srvctl stop diskgroup` command with the following syntax:

```
srvctl stop diskgroup -g diskgroup_name
 [-n node_list
] [-f]
```

Table A-143 srvctl stop diskgroup Options

| Option | Description |
| --- | --- |
| ``` -g diskgroup_name ``` | The Oracle ASM disk group name |
| ``` -n node_list ``` | Comma-delimited list of node names on which to stop the disk group  Note: This option is available only with Oracle Clusterware. |
| ``` -f ``` | This option does not stop the databases that depend on the disk group you are stopping, but instead performs a forceful dismount that may cause those databases to fail |

##### Example

An example of this command is:

```
$ srvctl stop diskgroup -g diskgroup1 -n mynode1,mynode2 -f
```

#### srvctl stop filesystem

Stops the Oracle ACFS volume resource.

##### Syntax and Options

Use the `srvctl stop filesystem` command with the following syntax:

```
srvctl stop filesystem -d volume_device_name
 [-n node_name
] [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-144 srvctl stop filesystem Options

| Option | Description |
| --- | --- |
| ``` -d volume_device_name ``` | The Oracle ACFS volume device name |
| ``` -n node_name ``` | The name of a node  If you do not specify this option, then the utility stops the volume resource on all active nodes in the cluster. |
| ``` -f ``` | This option stops the file system and also stops any databases or other resources that depend on this file system. |

##### Example

An example of this command is:

```
$ srvctl stop filesystem -d /dev/asm/d1volume293 -f
```

#### srvctl stop gns

Stops GNS for the cluster.

##### Syntax and Options

Use the `srvctl stop gns` command with the following syntax:

```
srvctl stop gns [-n node_name [-v] [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-145 srvctl stop gns Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of a node on which GNS is running |
| ``` -v ``` | Verbose output |
| ``` -f ``` | Force stop |

##### Example

An example of this command is:

```
$ srvctl stop gns
```

#### srvctl stop home

Stops all the Oracle Restart-managed or Oracle Clusterware-managed resources on the specified Oracle home.

##### Syntax and Options

Use the `srvctl stop home` command with the following syntax:

```
srvctl stop home -o Oracle_home
 -s state_file [-t stop_options
] 
                 [-n node_name
] [-f]
```

Table A-146 srvctl stop home Options

| Option | Description |
| --- | --- |
| ``` -o Oracle_home ``` | The path to the Oracle home for which you want to start the Oracle Restart or Oracle Clusterware-managed resources |
| ``` -s state_file ``` | The path name where you want the state file to be written. |
| ``` -t stop_options ``` | Shutdown options for the database, such as `NORMAL`, `TRANSACTIONAL`, `IMMEDIATE`, or `ABORT`  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm#SQPUG125) for more information about shutdown options |
| ``` -n node_name ``` | The name of the node where the Oracle home resides.  Note: This option is available only with Oracle Clusterware. |
| ``` -f ``` | Stop the resources even if errors are reported. |

##### Example

An example of this command is:

```
$ srvctl stop -o /u01/app/oracle/product/11.2.0/db_1 -s ~/state.txt
```

#### srvctl stop instance

Stops instances and stops any services running on specified instances, unless you specify the `-f` option. If you specify `-f`, then the services fail over to an available instance when the instance stops.

##### Syntax and Options

Use the `srvctl stop instance` command with the following syntax:

```
srvctl stop instance -d db_unique_name
 {[-n node_name]|[-i "instance_name_list
"]}
     [-o stop_options
] [-f]
```

In Windows, you must enclose the list of comma-delimited instance names in double quotation marks (`""`).

Note:

- This command is only available with Oracle Clusterware and Oracle RAC.
- If you run this command on an Oracle RAC One Node database, then the command returns an error instructing you to use the `database` noun, instead.

Table A-147 srvctl stop instance Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -n node_name ``` | The name of a single node  Note: Use this option for policy-managed databases. |
| ``` -i "instance_name" ``` | Comma-delimited instance names enclosed in double quotation marks  Note: Use this option for administrator-managed databases. |
| ``` -o stop_options ``` | Options for shutdown command, such as `NORMAL`, `TRANSACTIONAL LOCAL`, `IMMEDIATE`, or `ABORT`  See Also: [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm#SQPUG125) for more information about shutdown options |
| ``` -f ``` | This option fails the running services over to another instance. |

##### Example

An example of stopping an instance in a policy-managed database is:

```
$ srvctl stop instance -d crm -n node1
```

An example of stopping an instance in an administrator-managed database is:

```
$ srvctl stop instance -d crm -i crm1
```

#### srvctl stop listener

Stops the default listener on the specified `node_name`, or the listeners represented in a given list of listener names, that are registered with Oracle Clusterware on the given node.

This command can also be used to stop a listener on a noncluster database from the noncluster database home. SRVCTL does not accept the `-n` option, however, when run from a noncluster database home.

##### Syntax and Options

Use the `srvctl stop listener` command with the following syntax:

```
srvctl stop listener [-n node_name
] [-l listener_name_list] [-f]
```

Table A-148 srvctl stop listener Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | The name of a single node on which a particular listener runs.  Note: This option is available only with Oracle Clusterware. |
| ``` -l listener_name ``` | The name of the listener you want to stop.  If you do not specify this option, then the listener name defaults to `LISTENER`. |
| ``` -f ``` | Force stop |

##### Example

An example of this command is:

```
$ srvctl stop listener -n mynode1
```

#### srvctl stop nodeapps

Stops node-level applications on a node in the cluster.

##### Syntax and Options

Use the `srvctl stop nodeapps` command with the following syntax:

```
srvctl stop nodeapps [-n node_name] [-g] [-r] [-f] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-149 srvctl stop nodeapps Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | Node name  If you do not specify this option, then the utility stops the nodeapps on all active nodes in the cluster. |
| ``` -g ``` | Stops GSD, only |
| ``` -r ``` | Relocate VIP  Note: If you specify this option, then you must also specify the `-n` `node_name` option. |
| ``` -f ``` | Force stop |
| ``` -v ``` | Display verbose output |

##### Example

An example of this command is:

```
$ srvctl stop nodeapps
```

#### srvctl stop oc4j

Stops the OC4J instance.

##### Syntax and Options

Use the `srvctl stop oc4j` command with the following syntax:

```
srvctl stop oc4j [-f] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-150 srvctl stop oc4j Options

| Option | Description |
| --- | --- |
| ``` -f ``` | Force stop of the SCAN Listener. |
| `-v` | Display verbose output |

##### Example

An example of this command is:

```
$ srvctl stop oc4j -f -v
```

#### srvctl stop ons

Stops the Oracle Notification Service daemon.

Note:

This command is only available with Oracle Restart.

##### Syntax and Options

Use the `srvctl stop ons` command with the following syntax:

```
srvctl stop ons [-v]
```

The only option for this command is the `-v` option, which specifies that verbose output should be displayed.

##### Example

An example of this command is:

```
$ srvctl stop ons -v
```

#### srvctl stop scan

Stops all SCAN VIPs, by default, or a specific SCAN VIP identified by `ordinal_number`.

##### Syntax and Options

Use the `srvctl stop scan` command with the following syntax:

```
srvctl stop scan [-i ordinal_number
] [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-151 srvctl stop scan Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | An ordinal number that identifies which SCAN VIP you want to stop. The range of values you can specify for this option is 1 to 3.  If you do not specify this option, then the utility stops all the SCAN VIPs. |
| ``` -f ``` | Force stop of the SCAN VIP. |

##### Example

An example of this command is:

```
$ srvctl stop scan -i 1
```

#### srvctl stop scan\_listener

Stops all SCAN listeners, by default, or a specific listener identified by `ordinal_number`.

##### Syntax and Options

Use the `srvctl start scan_listener` command with the following syntax:

```
srvctl stop scan_listener [-i ordinal_number
] [-f]
```

Note:

This command is only available with Oracle Clusterware.

Table A-152 srvctl stop scan\_listener Options

| Option | Description |
| --- | --- |
| ``` -i ordinal_number ``` | An ordinal number that identifies which SCAN listener you want to stop. The range of values you can specify for this option is 1 to 3.  If you do not specify this option, then the utility stops all the SCAN listeners. |
| ``` -f ``` | Force stop of the SCAN listener. |

##### Example

An example of this command is:

```
$ srvctl stop scan_listener -i 1
```

#### srvctl stop service

Stops one or more services globally across the cluster database, or on the specified instance.

##### Syntax and Options

Use the `srvctl stop service` command with the following syntax:

```
srvctl stop service -d db_unique_name
 [-s "service_name_list
"
     [-n node_name | -i instance_name] [-f]
```

In Windows, you must enclose the list of comma-delimited service names in double quotation marks (`""`).

Table A-153 srvctl stop service Options

| Option | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -s service_name_list ``` | Comma-delimited list of service names enclosed in double quotation marks (`""`).  If you do not provide a service name list, then SRVCTL stops all services on the database. |
| ``` -n node_name ``` | The name of the node on which the services should be stopped. Use this option for policy-managed databases.  Note: This option is available only with Oracle Clusterware. |
| ``` -i instance_name ``` | The name of the instance for which the services should be stopped. Use this option for administrator-managed databases.  Note: This option is available only with Oracle Clusterware. |
| ``` -f ``` | Force SRVCTL to stop the service; this causes SRVCTL to disconnect all of the sessions transactionally, requiring the sessions using the service to reconnect and then connect to another instance.  Note: If you do not specify the `-f` option, then sessions already connected to this service stay connected, but new sessions cannot be established to the service. |

##### Examples

The following example stops a service globally across a cluster database:

```
$ srvctl stop service -d crm -s crm
```

The following example stops a service on a specified instance:

```
$ srvctl stop  service -d crm -s crm -i crm2
```

#### srvctl stop vip

Stops a specific VIP or all VIPs on a specific node, including any VIPs that were relocated due to a failover.

##### Syntax and Options

Use the `srvctl stop vip` command with the following syntax:

```
srvctl stop vip {-n node_name | -i vip_name} [-r] [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-154 srvctl stop vip Options

| Option | Description |
| --- | --- |
| ``` -n node_name ``` | This option stops all VIPs on a specific node, including failed-over VIPs |
| ``` -i vip_name ``` | This option stops a specific VIP |
| ``` -r ``` | Relocate VIP  Note: You must use the `-n` `node_name` option with the `-r` option. |
| ``` -v ``` | Verbose output |

##### Example

To stop all the VIPs on `mynode1`, including any failed-over VIPS, use the following command:

```
$ srvctl stop vip -n mynode1 -v
```

### unsetenv

The `unsetenv` command unsets values for the environment in the configuration file. It allows users to administer environment configuration for the objects.

Table A-155 srvctl unsetenv Command Summary

| Command | Description |
| --- | --- |
| `srvctl unsetenv asm` | Unsets the value for one or more Oracle ASM environment variables |
| `srvctl unsetenv database` | Unsets the value for one or more cluster database environment variables |
| `srvctl unsetenv listener` | Unsets the value for one or more listener environment variables. |
| `srvctl unsetenv nodeapps` | Unsets the value for one or more node application environment variables |
| `srvctl unsetenv vip` | Unsets the value for one or more VIP environment variables |

#### srvctl unsetenv asm

Unsets the Oracle ASM environment configurations.

##### Syntax and Options

Use the `srvctl unsetenv asm` command as follows:

```
srvctl unsetenv asm -t "name_list
"
```

Table A-156 srvctl unsetenv asm Options

| Options | Description |
| --- | --- |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables enclosed in double quotation marks (`""`) |

##### Example

The following example unsets the environment configuration for an Oracle ASM environment variable:

```
$ srvctl unsetenv asm -t CLASSPATH
```

#### srvctl unsetenv database

Unsets the cluster database environment configurations.

##### Syntax and Options

Use the `srvctl unsetenv database` command as follows:

```
srvctl unsetenv database -d db_unique_name
 -t "name_list
"
```

Table A-157 srvctl unsetenv database Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -t "name_list" ``` | Names of environment variables |

##### Example

The following example unsets the environment configuration for a cluster database environment variable:

```
$ srvctl unsetenv database -d crm -t CLASSPATH
```

#### srvctl unsetenv listener

Unsets the environment configuration for a listener.

##### Syntax and Options

Use the `srvctl unsetenv listener` command as follows:

```
srvctl unsetenv listener [-l listener_name
] -t "name_list
"
```

Table A-158 srvctl unsetenv listener Options

| Options | Description |
| --- | --- |
| ``` -l listener_name ``` | Name of the listener.  If you do not specify this option, then the name of the listener defaults to `LISTENER`. |
| ``` -t "name_list" ``` | Names of environment variables |

##### Example

The following example unsets the environment configuration for the node applications:

```
$ srvctl unsetenv listener -t "TNS_ADMIN"
```

#### srvctl unsetenv nodeapps

Unsets the environment configuration for the node applications.

##### Syntax and Options

Use the `srvctl unsetenv nodeapps` command as follows:

```
srvctl unsetenv nodeapps -t "name_list
" [-v]
```

Note:

This command is only available with Oracle Clusterware.

Table A-159 srvctl unsetenv nodeapps Options

| Options | Description |
| --- | --- |
| ``` -t "name_list" ``` | Names and values of environment variables |
| `-v` | Display verbose output |

##### Example

The following example unsets the environment configuration for the node applications:

```
$ srvctl unsetenv nodeapps -t "test_var1,test_var2"
```

#### srvctl unsetenv vip

Unsets the environment configuration for the specified cluster VIP.

##### Syntax and Options

Use the `srvctl unsetenv vip` command as follows:

```
srvctl unsetenv vip -i vip_name
 -t "name_list
" [-v]
```

Table A-160 srvctl unsetenv vip Options

| Options | Description |
| --- | --- |
| ``` -i vip_name ``` | Name of the cluster VIP |
| ``` -t "name_list" ``` | Comma-delimited list of the names of environment variables |
| ``` -v ``` | Verbose output |

##### Example

The following example unsets the `CLASSPATH` environment variable for a cluster VIP:

```
$ srvctl unsetenv vip -i crm2-vip -t CLASSPATH
```

### upgrade

Starting with Oracle Database 11g Release 2 (11.2.0.2), the `upgrade` command upgrades the configuration to the version of the software on which it is running.

#### srvctl upgrade database

The `srvctl upgrade database` command upgrades the configuration of a database and all of its services to the version of the database home from where this command is run.

##### Syntax and Options

Use the `srvctl upgrade database` command as follows:

```
srvctl upgrade database -d db_unique_name -o Oracle_home
```

Table A-161 srvctl upgrade database Options

| Options | Description |
| --- | --- |
| ``` -d db_unique_name ``` | Unique name for the database |
| ``` -o Oracle_home ``` | The path to the `ORACLE_HOME` |