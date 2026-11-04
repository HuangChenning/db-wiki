---
title: Cluster Verification Utility Reference
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## A Cluster Verification Utility Reference

The Cluster Verification Utility (CVU) performs system checks in preparation for installation, patch updates, or other system changes. Using CVU ensures that you have completed the required system configuration and preinstallation steps so that your Oracle Grid Infrastructure or Oracle Real Application Clusters (Oracle RAC) installation, update, or patch operation completes successfully.

With Oracle Clusterware 11g release 2 (11.2), Oracle Universal Installer is fully integrated with CVU, automating many CVU prerequisite checks. Oracle Universal Installer runs all prerequisite checks and associated fixup scripts when you run the installer.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD005) for information about using the Server Control utility (SRVCTL) to manage CVU
- [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) and [Oracle Real Application Clusters Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about how to manually install CVU

Note:

Check for and download updated versions of CVU on Oracle Technology Network at

`http://www.oracle.com/technology/index.html`

This appendix describes CVU under the following topics:

## About Cluster Verification Utility

This section includes topics which relate to using CVU.

- Overview
- Operational Notes
- Special Topics

### Overview

CVU can verify the primary cluster components during an operational phase or stage. A component can be basic, such as free disk space, or it can be complex, such as checking Oracle Clusterware integrity. For example, CVU can verify multiple Oracle Clusterware subcomponents across Oracle Clusterware layers. Additionally, CVU can check disk space, memory, processes, and other important cluster components. A stage could be, for example, database installation, for which CVU can verify whether your system meets the criteria for an Oracle Real Application Clusters (Oracle RAC) installation. Other stages include the initial hardware setup and the establishing of system requirements through the fully operational cluster setup.

Table A-1 lists verifications you can perform using CVU.

Table A-1 Performing Various CVU Verifications

| Verification to Perform | CVU Commands to Use |
| --- | --- |
| System requirements verification | `cluvfy comp sys` |
| Oracle ACFS verification | `cluvfy stage [-pre \| -post] cfs` |
| Storage verifications | - `cluvfy comp cfs` - `cluvfy comp space` - `cluvfy comp ssa` - `cluvfy stage [-pre \| -post] acfscfg` |
| Network verification | `cluvfy stage -post hwos` |
| Connectivity verifications | - `cluvfy comp nodecon` - `cluvfy comp nodereach` |
| Cluster Time Synchronization Services verification | `cluvfy comp clocksync` |
| User and Permissions verification | `cluvfy comp admprv` |
| Node comparison and verification | `cluvfy comp peer` |
| Installation verification | - `cluvfy stage -pre dbcfg` - `cluvfy stage -pre dbinst` - `cluvfy stage [-pre \| -post] crsinst` - `cluvfy stage [-pre \| -post] hacfg` - `cluvfy stage [-pre \| -post] nodeadd` |
| Deletion verification | `cluvfy stage -post nodedel` |
| Cluster Integrity verification | `cluvfy comp clu` |
| Oracle Clusterware and Oracle ASM Component verifications | - `cluvfy comp acfs` - `cluvfy comp asm` - `cluvfy comp clumgr` - `cluvfy comp crs` - `cluvfy comp dhcp` - `cluvfy comp dns` - `cluvfy comp gns` - `cluvfy comp gpnp` - `cluvfy comp ha` - `cluvfy comp nodeapp` - `cluvfy comp ocr` - `cluvfy comp ohasd` - `cluvfy comp olr` - `cluvfy comp scan` - `cluvfy comp software` - `cluvfy comp vdisk` |

### Operational Notes

This section includes the following topics:

- Installation Requirements
- Usage Information
- CVU Configuration File
- Privileges and Security
- Using CVU Help

Installation Requirements

CVU installation requirements are:

- At least 30 MB free space for the CVU software on the node from which you run CVU
- A work directory with at least 25 MB free space on each node. The default location of the work directory is `/tmp` on Linux and UNIX systems, and the value specified in the `TEMP` environment variable on Windows systems. You can specify a different location by setting the `CV_DESTLOC` environment variable.
	When using CVU, the utility attempts to copy any needed information to the CVU work directory. It checks for the existence of the work directory on each node. If it does not find one, then it attempts to create one. Make sure that the CVU work directory either exists on all nodes in your cluster or proper permissions are established on each node for the user running CVU to create that directory.
- Java 1.4.1 on the local node

Usage Information

CVU includes two scripts: `runcluvfy.sh` (`runcluvfy.bat` on Windows), which you use before installing Oracle software, and `cluvfy` (`cluvfy.bat` on Windows), located in the `Grid_home` `/bin` directory. The `runcluvfy.sh` script contains temporary variable definitions which enable it to run before you install Oracle Grid Infrastructure or Oracle Database. After you install Oracle Grid Infrastructure, use the `cluvfy` command to check prerequisites and perform other system readiness checks.

Note:

Oracle Universal Installer runs `cluvfy` to check all prerequisites during Oracle software installation.

Before installing Oracle software, run `runcluvfy.sh` from the mountpoint path of the software installation media, as follows:

```
cd /mountpoint
./runcluvfy.sh options
```

In the preceding example, the `options` variable represents CVU command options that you select. For example:

```
$ cd /mnt/dvdrom
$ ./runcluvfy.sh comp nodereach -n node1,node2 -verbose
```

When you enter a CVU command, it provides a summary of the test. During preinstallation, Oracle recommends that you obtain detailed output by using the `-verbose` argument with the CVU command. The `-verbose` argument produces detailed output of individual checks. Where applicable, it shows results for each node in a tabular layout.

Run the CVU command-line tool using the `cluvfy` command. Using `cluvfy` does not adversely affect your cluster environment or your installed software. You can run `cluvfy` commands at any time, even before the Oracle Clusterware installation. In fact, CVU is designed to assist you as soon as your hardware and operating system are operational. If you run a command that requires Oracle Clusterware on a node, then CVU reports an error if Oracle Clusterware is not yet installed on that node.

The node list that you use with CVU commands should be a comma-delimited list of host names without a domain. CVU ignores domains while processing node lists. If a CVU command entry has duplicate node entries after removing domain information, then CVU eliminates the duplicate node entries. Wherever supported, you can use the `-n all` option to verify all of your cluster nodes that are part of a specific Oracle RAC installation.

For network connectivity verification, CVU discovers all of the available network interfaces if you do not specify an interface on the CVU command line. For storage accessibility verification, CVU discovers shared storage for all of the supported storage types if you do not specify a particular storage identification on the command line. CVU also discovers the Oracle Clusterware home if one is available.

CVU Configuration File

You can use the CVU configuration file to define specific inputs for the execution of CVU. The path for the configuration file is `Grid_home` `/cv/admin/cvu_config` (or `Staging_area` `\clusterware\stage\cvu\cv\admin` on Windows platforms). You can modify this file using a text editor. The inputs to CVU are defined in the form of key entries. You must follow these rules when modifying the CVU configuration file:

- Key entries have the syntax `name=value`
- Each key entry and the value assigned to the key only defines one property
- Lines beginning with the number sign (`#`) are comment lines and are ignored
- Lines that do not follow the syntax `name=value` are ignored

The following is the list of keys supported by CVU:

- `CV_NODE_ALL`: If set, it specifies the list of nodes that should be picked up when Oracle Clusterware is not installed and a `-n` all option has been used in the command line. By default, this entry is commented out.
- `CV_ORACLE_RELEASE`: If set, it specifies the specific Oracle release (`10gR1`, `10gR2`, `11gR1`, or `11gR2`) for which the verifications have to be performed. If set, you do not have to use the `-r` `release` option wherever it is applicable. The default value is `11gR2`.
- `CV_RAW_CHECK_ENABLED`: If set to `TRUE`, it enables the check for accessibility of shared disks on Linux and Unix systems. This shared disk accessibility check requires that you install the `cvuqdisk` RPM Package Manager (rpm) on all of the nodes. By default, this key is set to `TRUE` and shared disk check is enabled.
- `CV_ASSUME_DISTID`: This property is used in cases where CVU cannot detect or support a particular platform or a distribution. Oracle does not recommend that you change this property as this might render CVU non-functional.
- `CV_XCHK_FOR_SSH_ENABLED`: If set to `TRUE`, it enables the X-Windows check for verifying user equivalence with `ssh`. By default, this entry is commented out and X-Windows check is disabled.
- `ORACLE_SRVM_REMOTECOPY`: If set, it specifies the location for the `scp` or `rcp` command to override the CVU default value. By default, this entry is commented out and CVU uses `/usr/bin/scp` and `/usr/sbin/rcp`.
- `ORACLE_SRVM_REMOTESHELL`: If set, it specifies the location for `ssh/rsh` command to override the CVU default value. By default, this entry is commented out and the tool uses `/usr/sbin/ssh` and `/usr/sbin/rsh`.
- `CV_ASSUME_CL_VERSION`: By default, the command line parser uses `crs activeversion` for the display of command line syntax usage and syntax validation. Use this property to pass a version other than `crs activeversion` for command line syntax display and validation. By default, this entry is commented out.

If CVU does not find a key entry defined in the configuration file, then CVU searches for the environment variable that matches the name of the key. If the environment variable is set, then CVU uses its value, otherwise CVU uses a default value for that entity.

Privileges and Security

CVU assumes that the current user is the user that owns the Oracle software installation, for example, `oracle`. For most CVU commands, you do not have to be the `root` user.

Using CVU Help

The `cluvfy` commands have context sensitive help that shows their usage based on the command-line arguments that you enter. For example, if you enter `cluvfy`, then CVU displays high-level generic usage text describing the stage and component syntax. The following is a list of context help commands:

- `cluvfy -help`: CVU displays detailed CVU command information.
- `cluvfy -version`: CVU displays the version of Oracle Clusterware.
- `cluvfy comp -list`: CVU displays a list of components that can be checked, and brief descriptions of how the utility checks each component.
- `cluvfy comp -help`: CVU displays detailed syntax for each of the valid component checks.
- `cluvfy stage -list`: CVU displays a list of valid stages.
- `cluvfy stage -help`: CVU displays detailed syntax for each of the valid stage checks.

You can also use the `-help` option with any CVU command. For example, `cluvfy stage -pre nodeadd -help` returns detailed information for that particular command.

If you enter an invalid CVU command, then CVU shows the correct usage for that command. For example, if you type `cluvfy stage -pre dbinst`, then CVU shows the correct syntax for the precheck commands for the `dbinst` stage. Enter the `cluvfy -help` command to see detailed CVU command information.

### Special Topics

This section includes the following topics:

- Generating Fixup Scripts
- Using CVU to Determine if Installation Prerequisites are Complete
- Using CVU with Oracle Database 10g Release 1 or 2
- Entry and Exit Criteria
- Verbose Mode and UNKNOWN Output
- CVU Node List Shortcuts

Generating Fixup Scripts

You can use the `-fixup` flag with certain CVU commands to generate [fixup script](glossary.md) s before installation. Oracle Universal Installer can also generate fixup scripts during installation. The installer then prompts you to run the script as `root` in a separate terminal session. If you generate a fixup script from the command line, then you can run it as `root` after it is generated. When you run the script, it raises kernel values to required minimums, if necessary, and completes other operating system configuration.

By default, fixup scripts are generated in the `/tmp` directory on Linux and UNIX systems and in the location specified in the `TEMP` environment variable on Windows systems. You can use the `cluvfy stage -pre crsinst` command to specify a different location in which to generate fixup scripts. For example:

```
cluvfy stage -pre crsinst -n node1 -fixup -fixupdir /db11202/fixit.sh
```

Using CVU to Determine if Installation Prerequisites are Complete

You can use CVU to determine which system prerequisites for installation are completed. Use this option if you are installing Oracle 11g release 2 (11.2) software on a system with a pre-existing Oracle software installation. In using this option, note the following:

- You must run CVU as the user account you plan to use to run the installation. You cannot run CVU as `root`, and running CVU as another user other than the user that is performing the installation does not ensure the accuracy of user and group configuration for installation or other configuration checks.
- Before you can complete a clusterwide status check, SSH must be configured for all cluster nodes. You can use the installer to complete SSH configuration, or you can complete SSH configuration yourself between all nodes in the cluster. You can also use CVU to generate a fixup script to configure SSH connectivity.
- CVU can assist you by finding preinstallation steps that must be completed, but it cannot perform preinstallation tasks.

Use the following syntax to determine what preinstallation steps are completed, and what preinstallation steps you must perform; running the command with the `-fixup` flag generates a fixup script to complete kernel configuration tasks as needed:

```
$ ./runcluvfy.sh stage -pre crsinst -fixup -n node_list
```

In the preceding syntax example, replace the `node_list` variable with the names of the nodes in your cluster, separated by commas. On Windows, you must enclose the comma-delimited node list in double quotation marks (`""`).

For example, for a cluster with mountpoint `/mnt/dvdrom/`, and with nodes `node1`, `node2`, and `node3`, enter the following command:

```
$ cd /mnt/dvdrom/
$ ./runcluvfy.sh stage -pre crsinst -fixup -n node1,node2,node3
```

Review the CVU report, and complete additional steps as needed.

See Also:

Your platform-specific installation guide for more information about installing your product

Using CVU with Oracle Database 10g Release 1 or 2

You can use CVU on the Oracle Database 11g release 2 (11.2) media to check system requirements for Oracle Database 10g Release 1 (10.1) and later installations. To use CVU to check Oracle Clusterware installations, append the command `-r` `release_code` flag to the standard CVU system check commands.

For example, to perform a verification check prior to installing Oracle Clusterware version 10. 2 on a system where the media mountpoint is `/mnt/dvdrom` and the cluster nodes are `node1`, `node2`, and `node3`, enter the following command:

```
$ cd /mnt/dvdrom
$ ./runcluvfy.sh stage -pre crsinst -n node1,node2,node3 -r 10gR2
```

Note:

If you do not specify a release version to check, then CVU checks for 11g release 2 (11.2) requirements.

Entry and Exit Criteria

When verifying stages, CVU uses entry and exit criteria. Each stage has entry criteria that define a specific set of verification tasks to be performed before initiating that stage. This check prevents you from beginning a stage, such as installing Oracle Clusterware, unless you meet the Oracle Clusterware prerequisites for that stage.

The exit criteria for a stage define another set of verification tasks that you must perform after the completion of the stage. Post-checks ensure that the activities for that stage have been completed. Post-checks identify stage-specific problems before they propagate to subsequent stages.

Verbose Mode and UNKNOWN Output

Although by default CVU reports in nonverbose mode by only reporting the summary of a test, you can obtain detailed output by using the `-verbose` argument. The `-verbose` argument produces detailed output of individual checks and where applicable shows results for each node in a tabular layout.

If a `cluvfy` command responds with `UNKNOWN` for a particular node, then this is because CVU cannot determine whether a check passed or failed. The cause could be a loss of reachability or the failure of user equivalence to that node. The cause could also be any system problem that was occurring on that node when CVU was performing a check.

The following is a list of possible causes for an `UNKNOWN` response:

- The node is down
- Executables that CVU requires are missing in `Grid_home` `/bin` or the `Oracle home` directory
- The user account that ran CVU does not have privileges to run common operating system executables on the node
- The node is missing an operating system patch or a required package
- The node has exceeded the maximum number of processes or maximum number of open files, or there is a problem with IPC segments, such as shared memory or semaphores

CVU Node List Shortcuts

To provide CVU a list of all of the nodes of a cluster, enter `-n all`. CVU attempts to obtain the node list in the following order:

1. If vendor clusterware is available, then CVU selects all of the configured nodes from the vendor clusterware using the `lsnodes` utility.
2. If Oracle Clusterware is installed, then CVU selects all of the configured nodes from Oracle Clusterware using the `olsnodes` utility.
3. If neither the vendor clusterware nor Oracle Clusterware is installed, then CVU searches for a value for the `CV_NODE_ALL` key in the configuration file.
4. If vendor clusterware and Oracle Clusterware are not installed and no key named `CV_NODE_ALL` exists in the configuration file, then CVU searches for a value for the `CV_NODE_ALL` environmental variable. If you have not set this variable, then CVU reports an error.

To provide a partial node list, you can set an environmental variable and use it in the CVU command. For example, on Linux or UNIX systems you can enter:

```
setenv MYNODES node1,node3,node5
cluvfy comp nodecon -n $MYNODES [-verbose]
```

## Cluster Verification Utility Command Reference

This section lists and describes the following CVU commands:

- `cluvfy comp acfs`
- `cluvfy comp admprv`
- `cluvfy comp asm`
- `cluvfy comp cfs`
- `cluvfy comp clocksync`
- `cluvfy comp clu`
- `cluvfy comp clumgr`
- `cluvfy comp crs`
- `cluvfy comp dhcp`
- `cluvfy comp dns`
- `cluvfy comp freespace`
- `cluvfy comp gns`
- `cluvfy comp gpnp`
- `cluvfy comp ha`
- `cluvfy comp healthcheck`
- `cluvfy comp nodeapp`
- `cluvfy comp nodecon`
- `cluvfy comp nodereach`
- `cluvfy comp ocr`
- `cluvfy comp ohasd`
- `cluvfy comp olr`
- `cluvfy comp peer`
- `cluvfy comp scan`
- `cluvfy comp software`
- `cluvfy comp space`
- `cluvfy comp ssa`
- `cluvfy comp sys`
- `cluvfy comp vdisk`
- `cluvfy stage [-pre | -post] acfscfg`
- `cluvfy stage [-pre | -post] cfs`
- `cluvfy stage [-pre | -post] crsinst`
- `cluvfy stage -pre dbcfg`
- `cluvfy stage -pre dbinst`
- `cluvfy stage [-pre | -post] hacfg`
- `cluvfy stage -post hwos`
- `cluvfy stage [-pre | -post] nodeadd`
- `cluvfy stage -post nodedel`

### cluvfy comp acfs

Use the `cluvfy comp acfs` component verification command to check the integrity of Oracle ASM Cluster File System on all nodes in a cluster.

Syntax

```
cluvfy comp acfs [-n [node_list] | [all]] [-f file_system] [-verbose]
```

Parameters

Table A-2 cluvfy comp acfs Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -f file_system ``` | The name of the file system to check. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp admprv

Use the `cluvfy comp admprv` command to verify user accounts and administrative permissions for installing Oracle Clusterware and Oracle RAC software, and for creating an Oracle RAC database or modifying an Oracle RAC database configuration.

Syntax

```
cluvfy comp admprv [-n node_list]
{ -o user_equiv [-sshonly] |
 -o crs_inst [-orainv orainventory_group] |
 -o db_inst [-osdba osdba_group] [-fixup [-fixupdir fixup_dir]] | 
 -o db_config -d oracle_home [-fixup [-fixupdir fixup_dir]] }
 [-verbose]
```

Parameters

Table A-3 cluvfy comp admprv Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -o user_equiv [-sshonly] ``` | Checks user equivalence between the nodes. On Linux and UNIX platforms, this command verifies user equivalence first using `ssh` and then using `rsh`, if the `ssh` check fails.  To verify the equivalence only through `ssh`, use the `-sshonly` option. |
| ``` -o crs_inst ``` | Checks administrative privileges for installing Oracle Clusterware. |
| ``` -orainv orainventory_group ``` | The name of the Oracle Inventory group. If you do not specify this option, then CVU uses `oinstall` as the inventory group. |
| ``` -o db_inst ``` | Checks administrative privileges for installing Oracle RAC. |
| ``` -osdba osdba_group ``` | The name of the OSDBA group. If you do not specify this option, then CVU uses `dba` as the OSDBA group. |
| ``` -o db_config ``` | Checks administrative privileges for creating or configuring an Oracle RAC database. |
| ``` -d oracle_home ``` | The directory where the Oracle software is installed. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

- By default, the equivalence check does not verify X-Windows configurations, such as whether you have disabled X-forwarding, whether you have the proper setting for the `DISPLAY` environment variable, and so on.
	To verify X-Windows aspects during user equivalence checks, set the `CV_XCHK_FOR_SSH_ENABLED` key to `TRUE` in the configuration file that resides in the `CV_HOME/cv/admin/cvu_config` directory before you run the `cluvfy comp admprv -o user_equiv` command.

Examples

Example 1: Verifying User Equivalence for All Nodes

You can verify user equivalence for all of the nodes by running the following command:

```
cluvfy comp admprv -n all -o user_equiv -verbose
```

Example 2: Verifying Permissions Required to Install Oracle Clusterware

You can verify that the permissions required for installing Oracle Clusterware have been configured on the nodes `racnode1` and `racnode2` by running the following command:

```
cluvfy comp admprv -n racnode1,racnode2 -o crs_inst -verbose
```

Example 3: Verifying Permissions Manage Oracle RAC Databases

You can verify that the permissions required for creating or modifying an Oracle RAC database using the `C:\app\oracle\product\11.2.0\dbhome_1` Oracle home directory, and generate a script to configure the permissions by running the following command:

```
cluvfy comp admprv -n all -o db_config -d C:\app\oracle\product\11.2.0\dbhome_1 -fixup -verbose
```

### cluvfy comp asm

Use the `cluvfy comp asm` component verification command to check the integrity of Oracle Automatic Storage Management (Oracle ASM) on all nodes in the cluster. This check ensures that the ASM instances on the specified nodes are running from the same Oracle home and that `asmlib`, if it exists, has a valid version and ownership.

Syntax

```
cluvfy comp asm [-n node_list | all ] [-verbose]
```

Parameters

Table A-4 cluvfy comp asm Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list \| all ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

Examples

Verifying the Integrity of Oracle ASM on All Nodes

To verify the integrity of Oracle ASM on all of the nodes in the cluster, use the following command:

```
cluvfy comp asm –n all
```

This command produces output similar to the following:

```
Verifying ASM Integrity

Task ASM Integrity check started...

Starting check to see fi ASM is running on all cluster nodes...

ASM Running check passed. ASM is running on all specified nodes

Starting Disk Groups check to see if at least one Disk Group configured...
Disk Group Check passed. At least one Disk Group configured

Task ASM Integrity check passed...

Verification of ASM Integrity was successful.
```

### cluvfy comp cfs

Use the `cluvfy comp cfs` component verification command to check the integrity of the clustered file system (OCFS for Windows or OCFS2) you provide using the `-f` option. CVU checks the sharing of the file system from the nodes in the node list.

Syntax

```
cluvfy comp cfs [-n node_list] -f file_system [-verbose]
```

Parameters

Table A-5 cluvfy comp cfs Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -f file_system ``` | The name of the file system. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

- This check is supported for OCFS2 version 1.2.1, or higher.

Examples

Verifying the Integrity of a Cluster File System on All the Nodes

To verify the integrity of the cluster file system `/oradbshare` on all of the nodes, use the following command:

```
cluvfy comp cfs -f /oradbshare –n all -verbose
```

### cluvfy comp clocksync

Use the `cluvfy comp clocksync` component verification command to clock synchronization across all the nodes in the node list. CVU verifies a time synchronization service is running (Oracle Cluster Time Synchronization Service (CTSS) or Network Time Protocol (NTP)), that each node is using the same reference server for clock synchronization, and that the time offset for each node is within permissible limits.

Syntax

```
cluvfy comp clocksync [-noctss] [-n node_list [all]] [-verbose]
```

Parameters

Table A-6 cluvfy comp clocksync Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -noctss ``` | If you specify this option, then CVU does not perform a check on CTSS. Instead, CVU checks the platform's native time synchronization service, such as NTP. |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp clu

Use the `cluvfy comp clu` component verification command to check the integrity of the cluster on all the nodes in the node list.

Syntax

```
cluvfy comp clu [-n node_list] [-verbose]
```

Parameters

Table A-7 cluvfy comp clu Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

Example

Verifying the Integrity of a Cluster

To verify the integrity of the cluster on all of the nodes, use the following command:

```
cluvfy comp clu -n all
```

This command produces output similar to the following:

```
Verifying cluster integrity

Checking cluster integrity...

Cluster integrity check passed

Verification of cluster integrity was successful.
```

### cluvfy comp clumgr

Use the `cluvfy comp clumgr` component verification command to check the integrity of cluster manager subcomponent, or Oracle Cluster Synchronization Services (CSS), on all the nodes in the node list.

Syntax

```
cluvfy comp clumgr [-n node_list] [-verbose]
```

Parameters

Table A-8 cluvfy comp clumgr Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp crs

Run the `cluvfy comp crs` component verification command to check the integrity of the Cluster Ready Services (CRS) daemon on the specified nodes.

Syntax

```
cluvfy comp crs [-n node_list] [-verbose]
```

Parameters

Table A-9 cluvfy comp crs Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp dhcp

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `cluvfy comp dhcp` component verification command to verify that the DHCP server exists on the network and is capable of providing a required number of IP addresses. This verification also verifies the response time for the DHCP server. You must run this command as `root`.

Syntax

```
# cluvfy comp dhcp -clustername cluster_name [-vipresname vip_resource_name]
[-port dhcp_port] [-n node_list] [-verbose]
```

Parameters

Table A-10 cluvfy comp dhcp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -clustername cluster_name ``` | The name of the cluster of which you want to check the integrity of DHCP. |
| ``` -vipresname vip_resource_name ``` | The name of the VIP resource. |
| ``` -port dhcp_port ``` | The port on which DHCP listens. The default port is 67. |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

Before running this command, ensure that the network resource is offline. Use the `srvctl stop nodeapps` command to bring the network resource offline, if necessary.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/srvctladmin.htm#RACAD5042) for more information about the `srvctl stop nodeapps` command

### cluvfy comp dns

Starting with Oracle Database 11g release 2 (11.2.0.2), use the `cluvfy comp dns` component verification command to verify that the Grid Naming Service (GNS) subdomain delegation has been properly set up in the Domain Name Service (DNS) server.

Run `cluvfy comp dns -server` on one node of the cluster. On each node of the cluster run `cluvfy comp dns -client` to verify the DNS server setup for the cluster.

Syntax

```
cluvfy comp dns -server -domain gns_sub_domain -vipaddress gns_vip_address] [-port dns_port]
[-verbose]

cluvfy comp dns -client -domain gns_sub_domain -vip gns_vip [-port dns_port]
[-last] [-verbose]
```

Parameters

Table A-11 cluvfy comp dns Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -server ``` | Start a test DNS server that listens on the domain specified by the `-domain` option. |
| ``` -client ``` | Validate connectivity to a test DNS server started on specified address. You must specify the same information you specified when you started the DNS server. |
| ``` -domain gns_sub_domain ``` | The GNS subdomain name. |
| ``` -vipaddress gns_vip_address ``` | GNS virtual IP address in the form `{` `IP_name` `\|` `IP_address` `}/` `net_mask` `/` `interface_name`. You can specify either `IP_name`, which is a name that resolves to an IP address, or `IP_address`, which is an IP address. Either name or address is followed by `net_mask`, which is the subnet mask for the IP address, and `interface_name`, which is the interface on which to start the IP address. |
| ``` -vip gns_vip ``` | GNS virtual IP address, which is either a name that resolves to an IP address or a dotted decimal numeric IP address. |
| ``` -port dns_port ``` | The port on which DNS listens. The default port is 53. |
| ``` -last ``` | Send a termination request to the test DNS server after all the validations are complete. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

- This command is not supported on Windows operating systems.
- On the last node specify the `-last` option to terminate the `cluvfy comp dns -server` instance.
- If the port number is lower than 1024, then you must run CVU as `root`.
- Do not run this check while the GNS Oracle Clusterware resource is online.

### cluvfy comp freespace

Use the `cluvfy comp freespace` component verification command to check the free space available in the Oracle Clusterware home storage and ensure that there is at least 5% of the total space available. For example, if the total storage is 10GB, then the check ensures that at least 500MB of it is free.

Syntax

```
cluvfy comp freespace [-n node_list | all]
```

If you choose to include the `-n` option, then enter a comma-delimited list of node names on which to run the command. Alternatively, you can specify `all` after `-n` to check all of the nodes in the cluster.

### cluvfy comp gns

Use the `cluvfy comp gns` component verification command to verify the integrity of the Oracle Grid Naming Service (GNS) on the cluster.

Syntax

```
cluvfy comp gns -precrsinst -domain gns_domain -vip gns_vip [-n node_list]
 [-verbose]

cluvfy comp gns -postcrsinst [-verbose]
```

Parameters

Table A-12 cluvfy comp gns Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -precrsinst ``` | Perform checks on GNS domain name and GNS VIP before Oracle Clusterware is installed. |
| ``` -domain gns_domain ``` | The GNS sub domain name |
| ``` -vip gns_vip ``` | The GNS virtual IP address |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -postcrsinst ``` | Check the integrity of GNS on all nodes in the cluster |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp gpnp

Use the `cluvfy comp gpnp` component verification command to check the integrity of Grid Plug and Play on all of the nodes in a cluster.

Syntax

```
cluvfy comp gpnp [-n node_list] [-verbose]
```

Parameters

Table A-13 cluvfy comp gpnp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp ha

Use the `cluvfy comp ha` component verification command to check the integrity of Oracle Restart on the local node.

Syntax

```
cluvfy comp ha [-verbose]
```

If you include the `-verbose` option, then CVU prints detailed output.

### cluvfy comp healthcheck

Use the `cluvfy comp healthcheck` component verification command to check your Oracle Clusterware and Oracle Database installations for their compliance with mandatory requirements and best practices guidelines, and to ensure that they are functioning properly.

Syntax

```
cluvfy comp healthcheck [-collect {cluster|database}] [-db db_unique_name]
 [-bestpractice|-mandatory] [-deviations] [-html] [-save [-savedir directory_path]]
```

Parameters

Table A-14 cluvfy comp healthcheck Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -collect {cluster\|database} ``` | Use `-collect` to specify that you want to perform checks for Oracle Clusterware (`cluster`) or Oracle Database (`database`). If you do not use the `-collect` flag with the `healthcheck` option, then CVU performs checks for both Oracle Clusterware and Oracle Database. |
| ``` -db db_unique_name ``` | Use `-db` to specify checks on the specific database that you enter after the `-db` flag.  CVU uses JDBC to connect to the database as the user `cvusys` to verify various database parameters. For this reason, if you want CVU to perform checks for the database you specify with the `-db` flag, then you must first create the `cvusys` user on that database, and grant that user the CVU-specific role, `cvusapp`. You must also grant members of the `cvusapp` role select permissions on system tables.  Use the `cvusys.sql` script included in the `CVU_home` `/cv/admin` directory to facilitate the creation of this user. This SQL script creates the `cvusys` user on all the databases that you want to verify using CVU.  If you use the `-db` flag but do not provide a unique database name, then CVU discovers all the Oracle Databases on the cluster. To perform best practices checks on these databases, you must create the `cvusys` user on each database, and grant that user the `cvusapp` role with the select privileges needed to perform the best practice checks. |
| ``` [-bestpractice\|-mandatory  [-deviations]] ``` | Use the `-bestpractice` flag to specify best practice checks, and the `-mandatory` flag to specify mandatory checks. Add the `-deviations` flag to specify that you want to see only the deviations from either the best practice recommendations or the mandatory requirements. You can specify either the `-bestpractice` or `-mandatory` flag, but not both flags. If you specify neither `-bestpractice` nor `-mandatory`, then CVU displays both best practices and mandatory requirements. |
| ``` -html ``` | Use the `-html` flag to generate a detailed report in HTML format.  If you specify the `-html` flag, and a browser CVU recognizes is available on the system, then CVU starts the browser and displays the report on the browser when the checks are complete.  If you do not specify the `-html` flag, then CVU generates the detailed report in a text file. |
| ``` -save [-savedir directory_path] ``` | Use the `-save` or `-save -savedir` flags to save validation reports (`cvuchecdkreport_` `timestamp``.txt` and `cvucheckreport_` `timestamp``.htm`), where `timestamp` is the time and date of the validation report. |

### cluvfy comp nodeapp

Use the component `cluvfy comp nodeapp` command to check for the existence of node applications, namely VIP, NETWORK, ONS, and GSD, on all of the specified nodes.

Syntax

```
cluvfy comp nodeapp [-n node_list] [-verbose]
```

Parameters

Table A-15 cluvfy comp nodeapp Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy comp nodecon

Use the `cluvfy comp nodecon` component verification command to check the connectivity among the nodes specified in the node list. If you provide an interface list, then CVU checks the connectivity using only the specified interfaces.

Syntax

```
cluvfy comp nodecon -n node_list [-i interface_list] [-verbose]
```

Parameters

Table A-16 cluvfy comp nodecon Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -i interface_list ``` | The comma-delimited list of interface names. If you do not specify this option, then CVU discovers the available interfaces and checks connectivity using each of them. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

- You can run this command in verbose mode to identify the mappings between the interfaces, IP addresses, and subnets.
- Use the `nodecon` command without the `-i` option and with `-n` set to `all` to use CVU to:
	- Discover all of the network interfaces that are available on the cluster nodes
		- Review the interfaces' corresponding IP addresses and subnets
		- Obtain the list of interfaces that are suitable for use as VIPs and the list of interfaces to private interconnects
		- Verify the connectivity between all of the nodes through those interfaces

Examples

Example 1: Verifying the connectivity between nodes through specific network interfaces:

You can verify the connectivity between the nodes `node1` and `node3` through interface `eth0` by running the following command:

```
cluvfy comp nodecon -n node1,node3 –i eth0 -verbose
```

Example 2: Discovering all available network interfaces and verifying the connectivity between the nodes in the cluster through those network interfaces:

Use the following command to discover all of the network interfaces that are available on the cluster nodes. CVU then reviews the interfaces' corresponding IP addresses and subnets. Using this information, CVU obtains a list of interfaces that are suitable for use as VIPs and a list of interfaces to private interconnects. Finally, CVU verifies the connectivity between all of the nodes in the cluster through those interfaces.

```
cluvfy comp nodecon -n all -verbose
```

### cluvfy comp nodereach

Use the `cluvfy comp nodereach` component verification command to check the reachability of specified nodes from a source node.

Syntax

```
cluvfy comp nodereach -n node_list [-srcnode node] [-verbose]
```

Parameters

Table A-17 cluvfy comp nodereach Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -srcnode node ``` | The name of the source node from which CVU performs the reachability test. If you do not specify a source node, then the node on which you run the command is used as the source node. |
| ``` -verbose ``` | CVU prints detailed output. |

Example

Verifying the network connectivity between nodes in the cluster:

To verify that `node3` is reachable over the network from the local node, use the following command:

```
cluvfy comp nodereach -n node3
```

This command produces output similar to the following:

```
Verifying node reachability

Checking node reachability...
Node reachability check passed from node ”node1”

Verification of node reachability was successful.
```

### cluvfy comp ocr

Use the `cluvfy comp ocr` component verification command to check the integrity of Oracle Cluster Registry (OCR) on all the specified nodes.

Syntax

```
cluvfy comp ocr [-n node_list] [-verbose]
```

Parameters

Table A-18 cluvfy comp ocr Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

This command does not verify the integrity of OCR contents. You must use the OCRCHECK utility to verify the contents of OCR.

Example

Verifying the integrity of OCR on the local node

To verify the integrity of OCR on the local node, run the following command:

```
cluvfy comp ocr
```

This command produces output similar to the following:

```
Verifying OCR integrity

Checking OCR integrity...

Checking the absence of a non-clustered configurationl...
All nodes free of non-clustered, local-only configurations

ASM Running check passed. ASM is running on all specified nodes

Checking OCR config file ”/etc/oracle/ocr.loc”...

OCR config file ”/etc/oracle/ocr.loc” check successful

Disk group for ocr location ”+DATA” available on all the nodes

NOTE:
This check does not verify the integrity of the OCR contents. Execute &rsquor;ocrcheck' as a privileged user to verify the contents of OCR.

OCR integrity check passed

Verification of OCR integrity was successful.
```

### cluvfy comp ohasd

Use the `cluvfy comp ohasd` component verification command to check the integrity of the Oracle High Availability Services daemon.

Syntax

```
cluvfy comp ohasd [-n node_list] [-verbose]
```

Parameters

Table A-19 cluvfy comp ohasd Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

Example

Verifying the integrity of the Oracle high availability services daemon on all nodes in the cluster

To verify that the Oracle High Availability Services daemon is operating correctly on all nodes in the cluster, use the following command:

```
cluvfy comp ohasd -n all -verbose
```

This command produces output similar to the following:

```
Verifying OHASD integrity

Checking OHASD integrity...
ohasd is running on node ”node1”
ohasd is running on node ”node2”
ohasd is running on node ”node3”
ohasd is running on node ”node4”

OHASD integrity check passed

Verification of OHASD integrity was successful.
```

### cluvfy comp olr

Use the `cluvfy comp olr` component verification command to check the integrity of Oracle Local Registry (OLR) on the local node.

Syntax

```
cluvfy comp olr [-verbose]
```

If you include the `-verbose` option, then CVU prints detailed output.

Usage Notes

This command does not verify the integrity of the OLR contents. You must use the `ocrcheck -local` command to verify the contents of OCR.

Example

Verifying the integrity of the OLR on a node

To verify the integrity of the OLR on the current node, run the following command:

```
cluvfy comp olr -verbose
```

This command produces output similar to the following:

```
Verifying OLR integrity

Checking OLR integrity...

Checking OLR config file...

OLR config file check successful

Checking OLR file attributes...

OLR file check successful

WARNING:
This check does not verify the integrity of the OLR contents. Execute &rsquor;ocrcheck -local' as a privileged user to verify the contents of OLR.

OLR integrity check passed

Verification of OLR integrity was successful.
```

### cluvfy comp peer

Use the `cluvfy comp peer` component verification command to check the compatibility and properties of the specified nodes against a reference node. You can check compatibility for non-default user group names and for different releases of the Oracle software. This command compares physical attributes, such as memory and swap space, as well as user and group values, kernel settings, and installed operating system packages.

Syntax

```
cluvfy comp peer -n node_list [-refnode node]
 [-r {10gR1 | 10gR2 | 11gR1 | 11gR2}] [-orainv orainventory_group]
 [-osdba osdba_group] [-verbose]
```

Parameters

Table A-20 cluvfy comp peer Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -refnode ``` | The node that CVU uses as a reference for checking compatibility with other nodes. If you do not specify this option, then CVU reports values for all the nodes in the node list. |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -r {10gR1 \| 10gR2 \| 11gR1 \|  11gR2} ``` | Specifies the software release that CVU checks as required for installation of Oracle Clusterware or Oracle RAC. If you do not specify this option, then CVU assumes Oracle Clusterware or Oracle Database 11g release 2 (11.2). |
| ``` -orainv orainventory_group ``` | The name of the Oracle Inventory group. If you do not specify this option, then CVU uses `oinstall` as the inventory group.  Note: This parameter is not available on Windows systems. |
| ``` -osdba osdba_group ``` | The name of the OSDBA group. If you do not specify this option, then CVU uses `dba` as the OSDBA group.  Note: This parameter is not available on Windows systems. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

Peer comparison with the `-refnode` option compares the system properties of other nodes against the reference node. If the value does not match (the value is not equal to reference node value), then CVU flags that comparison as a deviation from the reference node. If a group or user does not exist on reference node as well as on the other node, CVU reports this comparison as 'passed' because there is no deviation from the reference node. Similarly, CVU reports as 'failed' a comparison with a node that has more total memory than the reference node.

Example

Comparing the configuration of select cluster nodes

The following command lists the values of several preselected properties on different nodes from Oracle Database 11g release 2 (11.2):

```
cluvfy comp peer -n node1,node2,node4,node7 -verbose
```

### cluvfy comp scan

Use the `cluvfy comp scan` component verification command to check the Single Client Access Name (SCAN) configuration.

Syntax

```
cluvfy comp scan [-verbose]
```

If you include the `-verbose` option, then CVU prints detailed output.

Example

Verifying the SCAN configuration

To verify that the SCAN and SCAN listeners are configured and operational on all nodes in the cluster, use the following command:

```
cluvfy comp scan
```

This command produces output similar to the following:

```
Verifying scan

Checking Single Client Access Name (SCAN)...

Checking TCP connectivity to SCAN Listeners...
TCP connectivity to SCAN Listeners exists on all cluster nodes

Checking name resolution setup for ”node1.example.com”...

Verification of SCAN VIP and Listener setup passed

Verification of scan was successful.
```

### cluvfy comp software

Use the `cluvfy comp software` component verification command to check the files and attributes installed with the Oracle software.

Syntax

```
cluvfy comp software [-n node_list] [-d oracle_home] 
 [-r {10gR1 | 10gR2 | 11gR1 | 11gR2}] [-verbose]
```

Parameters

Table A-21 cluvfy comp software Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -d oracle_home ``` | The directory where the Oracle Database software is installed. If you do not specify this option, then the files installed in the Grid home are verified. |
| ``` -r {10gR1 \| 10gR2 \| 11gR1 \|  11gR2} ``` | Specifies the software release that CVU checks as required for installation of Oracle Clusterware or Oracle RAC. If you do not specify this option, then CVU assumes Oracle Clusterware or Oracle Database 11g release 2 (11.2). |
| ``` -verbose ``` | CVU prints detailed output. |

Example

Verifying the software configuration on all nodes in the cluster for the Oracle Clusterware home directory.

To verify that the installed files for Oracle Clusterware 11g release 2 are configured correctly, use a command similar to the following:

```
cluvfy comp software -n all -verbose
```

This command produces output similar to the following:

```
Verifying software

Check: Software

 1021 files verified

Software check passed

Verification of software was successful.
```

### cluvfy comp space

Use the `cluvfy comp space` component verification command to check for free disk space at the location you specify in the `-l` option on all the specified nodes.

Syntax

```
cluvfy comp space [-n node_list] -l storage_location 
 -z disk_space {B | K | M | G} [-verbose]
```

Parameters

Table A-22 cluvfy comp space Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -l storage_location ``` | The directory path to the storage location to check |
| ``` -z disk_space {B\|K\|M\|G} ``` | The required disk space, in units of bytes (B), kilobytes (K), megabytes (M), or gigabytes (G). There should be no space between the numerical value and the byte indicator, for example, 2G. Use only whole numbers. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

The `space` component does not support block or raw devices.

See Also:

The Oracle Certification site on My Oracle Support for the most current information about certified storage options:

`https://support.oracle.com`

Examples

Verifying the availability of free space on all nodes

You can verify that each node has 5 GB of free space in the `/home/dbadmin/products` directory by running the following command:

```
cluvfy comp space -n all -l /home/dbadmin/products –z 5G -verbose
```

### cluvfy comp ssa

Use the `cluvfy comp ssa` component verification command to discover and check the sharing of the specified storage locations. CVU checks sharing for nodes in the node list.

Syntax

```
cluvfy comp ssa [-n node_list] [-s storageID_list]
 [-t {software | data | ocr_vdisk}] [-verbose]
```

Parameters

Table A-23 cluvfy comp ssa Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -s storageID_list ``` | A comma-delimited list of storage IDs, for example, `/dev/sda,/dev/sdb`.  If you do not specify the `-s` option, then CVU discovers supported storage types and checks sharing for each of them. |
| ``` -t {software \| data \|  ocr_vdisk} ``` | The type of Oracle file that will be stored on the storage device.  If you do not provide the `-t` option, then CVU discovers or checks the `data` file type. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

- The current release of `cluvfy` has the following limitations on Linux regarding shared storage accessibility check.
	- Currently NAS storage and OCFS2 (version 1.2.1 or higher) are supported.
		See Also:
		[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for more information about NAS mount options
		- For sharedness checks on NAS, `cluvfy` commands require that you have write permission on the specified path. If the `cluvfy` user does not have write permission, `cluvfy` reports the path as `not` `shared`.
- To perform discovery and shared storage accessibility checks for SCSI disks on Linux systems, CVU requires the CVUQDISK package. If you attempt to use CVU and the CVUQDISK package is not installed on all of the nodes in your Oracle RAC environment, then CVU responds with an error. See "Shared Disk Discovery on Red Hat Linux" for information about how to install the CVUQDISK package.

Examples

Example 1: Discovering All of the Available Shared Storage Systems on Your System

To discover all of the shared storage systems available on your system, run the following command:

```
cluvfy comp ssa -n all -verbose
```

Example 2: Verifying the Accessibility of a Specific Storage Location

You can verify the accessibility of specific storage locations, such as `/dev/sda`, for storing data files for all the cluster nodes by running a command similar to the following:

```
cluvfy comp ssa -n all -s /dev/sda,/dev/sdb,/dev/sdc
```

This command produces output similar to the following:

```
Verifying shared storage acessibility

Checking shared storage accessibility...

”/dev/sda” is shared
”/dev/sdb” is shared
”/dev/sdc” is shared

Shared storage check was successful on nodes ”node1,node2,node3,node4”

Verification of shared storage accessibility was successful.
```

### cluvfy comp sys

Use the `cluvfy comp sys` component verification command to check that the minimum system requirements are met for the specified product on all the specified nodes.

Syntax

```
cluvfy comp sys [-n node_list] -p {crs | ha | database} 
 [-r {10gR1 | 10gR2 | 11gR1 | 11gR2}] [-osdba osdba_group]
 [-orainv orainventory_group] [-fixup [-fixupdir fixup_dir]] [-verbose]
```

Parameters

Table A-24 cluvfy comp sys Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| `-p {crs \| ha \| database}` | Specifies whether CVU checks the system requirements for Oracle Clusterware, Oracle Restart (HA), or Oracle RAC. |
| ``` -r {10gR1 \| 10gR2 \| 11gR1 \| 11gR2} ``` | Specifies the Oracle Database release that CVU checks as required for installation of Oracle Clusterware or Oracle RAC. If you do not specify this option, then CVU assumes Oracle Database 11g release 2 (11.2). |
| ``` -osdba osdba_group ``` | The name of the OSDBA group. If you do not specify this option, then CVU uses `dba` as the OSDBA group. |
| ``` -orainv orainventory_group ``` | The name of the Oracle Inventory group. If you do not specify this option, then CVU uses `oinstall` as the inventory group. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -verbose ``` | CVU prints detailed output. |

Examples

Verifying the system requirements for installing Oracle Clusterware

To verify the system requirements for installing Oracle Clusterware 11g release 2 on the cluster nodes `node1`,`node2` and `node3`, run the following command:

```
cluvfy comp sys -n node1,node2,node3 -p crs -verbose
```

### cluvfy comp vdisk

Use the `cluvfy comp vdisk` component verification command to check the voting disks configuration and the `udev` settings for the voting disks on all the specified nodes.

See Also:

[Oracle Grid Infrastructure Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e41961/storage.htm#CWLIN304) for more information about `udev` settings

Syntax

```
cluvfy comp vdisk [-n node_list] [-verbose]
```

Parameters

Table A-25 cluvfy comp vdisk Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster.  If you do not specify this option, then CVU checks only the local node. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage \[-pre | -post\] acfscfg

se the `cluvfy stage -pre acfscfg` command to verify your cluster nodes are set up correctly before configuring Oracle ASM Cluster File System (Oracle ACFS).

Use the `cluvfy stage -post acfscfg` to check an existing cluster after you configure Oracle ACFS.

Syntax

```
cluvfy stage -pre acfscfg -n node_list [-asmdev asm_device_list] [-verbose]

cluvfy stage -post acfscfg -n node_list [-verbose]
```

Parameters

Table A-26 cluvfy stage \[-pre | -post\] acfscfg Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -asmdev asm_device_list ``` | The list of devices you plan for Oracle ASM to use. If you do not specify this option, then CVU uses an internal operating system-dependent value, for example, `/dev/raw/*` on Linux systems. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage \[-pre | -post\] cfs

Use the `cluvfy stage -pre cfs` stage verification command to verify your cluster nodes are set up correctly before setting up OCFS2 or OCFS for Windows.

Use the `cluvfy stage -post cfs` stage verification command to perform the appropriate checks on the specified nodes after setting up OCFS2 or OCFS for Windows.

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform for a list of supported shared storage types

Syntax

```
cluvfy stage -pre cfs -n node_list -s storageID_list [-verbose]

cluvfy stage -post cfs -n node_list -f file_system [-verbose]
```

Parameters

Table A-27 cluvfy stage \[-pre | -post\] cfs Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -s storageID_list ``` | The comma-delimited list of storage locations to check. |
| ``` -verbose ``` | CVU prints detailed output. |

Examples

Example 1: Check that a specific shared device is configured correctly before configuring OCFS2

To check that a shared device is configured correctly before setting up OCFS2, use a command similar to the following, where you replace /dev/sdd5 with the name of the shared device on your system:

```
cluvfy stage -pre cfs -n node1,node2,node3,node4 -s /dev/sdd5
```

Example 2: Check that an OCFS for Windows file system was configured correctly

To check that the configuration of OCFS for Windows completely successfully and that all nodes have access to this new file system, use a command similar to the following, where you replace E:\\ocfs\\db1 with the location of the OCFS for Windows file system for your cluster:

```
cluvfy stage -post cfs -n all -f E:\ocfs\db1
```

### cluvfy stage \[-pre | -post\] crsinst

Use the `cluvfy stage -pre crsinst` command to check the specified nodes before installing Oracle Clusterware. CVU performs additional checks on OCR and voting disks if you specify the `-c` and `-q` options.

Use the `cluvfy stage -post crsinst` command to check the specified nodes after installing Oracle Clusterware.

Syntax

```
cluvfy stage -pre crsinst -n node_list [-r {10gR1 | 10gR2 | 11gR1 | 11gR2}]
 [-c ocr_location_list] [-q voting_disk_list] [-osdba osdba_group]
 [-orainv orainventory_group] [-asm [-asmgrp asmadmin_group] [-asmdev asm_device_list]]
 [-crshome Grid_home] [-fixup [-fixupdir fixup_dir]
 [-networks network_list]
 [-verbose]]

cluvfy stage -post crsinst -n node_list [-verbose]
```

Parameters

Table A-28 cluvfy stage \[-pre | -post\] crsinst Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -r {10gR1 \| 10gR2 \| 11gR1 \| 11gR2} ``` | Specifies the Oracle Clusterware release that CVU checks as required for installation of Oracle Clusterware. If you do not specify this option, then CVU assumes Oracle Clusterware 11g release 2 (11.2). |
| ``` -c ocr_location_list ``` | A comma-delimited list of directory paths for OCR locations or files that CVU checks for availability to all nodes. If you do not specify this option, then the OCR locations are not checked. |
| ``` -q voting_disk_list ``` | A comma-delimited list of directory paths for voting disks that CVU checks for availability to all nodes. If you do not specify this option, then the voting disk locations are not checked |
| ``` -osdba osdba_group ``` | The name of the OSDBA group. If you do not specify this option, then CVU uses `dba` as the OSDBA group. |
| ``` -orainv orainventory_group ``` | The name of the Oracle Inventory group. If you do not specify this option, then CVU uses `oinstall` as the inventory group. |
| ``` -asm ``` | Indicates that Oracle ASM is used for storing the Oracle Clusterware files. |
| ``` -asmgrp asmadmin_group ``` | The name of the OSASM group. If you do not specify this option, then CVU uses `dba` as the OSDBA group |
| ``` -asm -asmdev asm_device_list ``` | A list of devices you plan for Oracle ASM to use that CVU checks for availability to all nodes.  If you do not specify this option, then CVU uses an internal operating system-dependent value. |
| `-crshome` `Grid_home` | The location of the Oracle Grid Infrastructure or Oracle Clusterware home directory. If you do not specify this option, then the supplied file system location is checked for sufficient free space for an Oracle Clusterware installation. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -networks network_list ``` | Checks the network parameters of a comma-delimited list of networks in the form of `"` `if_name` `"` `[:``subnet_id` `[:public \| :cluster_interconnect]]`.  - You can use the asterisk (`*`) wildcard character when you specify the network interface name (`if_name`), such as `eth*`, to match interfaces. - Specify a subnet number for the network interface for the `subnet_id` variable and choose the type of network interface. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage -pre dbcfg

Use the `cluvfy stage -pre dbcfg` command to check the specified nodes before configuring an Oracle RAC database to verify whether your system meets all of the criteria for creating a database or for making a database configuration change.

Syntax

```
cluvfy stage -pre dbcfg -n node_list -d Oracle_home [-fixup [-fixupdir fixup_dir]]
[-verbose]
```

Parameters

Table A-29 cluvfy stage -pre dbcfg Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -d Oracle_home ``` | The location of the Oracle home directory for the database that is being checked. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage -pre dbinst

Use the `cluvfy stage -pre dbinst` command to check the specified nodes before installing or creating an Oracle RAC database to verify that your system meets all of the criteria for installing or creating an Oracle RAC database.

Syntax

```
cluvfy stage -pre dbinst -n node_list [-r {10gR1 | 10gR2 | 11gR1 | 11gR2}]
 [-osdba osdba_group] [-d Oracle_home] [-fixup [-fixupdir fixup_dir] [-verbose]
```

Parameters

Table A-30 cluvfy stage -pre dbinst Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -r {10gR1 \| 10gR2 \| 11gR1 \| 11gR2} ``` | Specifies the Oracle Database release that CVU checks as required for installation of Oracle RAC. If you do not specify this option, then CVU assumes Oracle Database 11g release 2 (11.2). |
| ``` -osdba osdba_group ``` | The name of the OSDBA group. If you do not specify this option, then CVU uses `dba` as the OSDBA group. |
| ``` -d Oracle_home ``` | The location of the Oracle home directory where you are installing Oracle RAC and creating the Oracle RAC database. If you specify this option, then the specified location is checked for sufficient free disk space for a database installation. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage \[-pre | -post\] hacfg

Use the `cluvfy stage -pre hacfg` command to check a local node before configuring Oracle Restart.

Use the `cluvfy stage -post hacfg` command to check the local node after configuring Oracle Restart.

Syntax

```
cluvfy stage -pre hacfg [-osdba osdba_group] [-orainv orainventory_group]
[-fixup [-fixupdir fixup_dir]] [-verbose]

cluvfy stage -post hacfg [-verbose]
```

Parameters

Table A-31 cluvfy stage \[-pre | -post\] hacfg Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -osdba osdba_group ``` | The name of the OSDBA group. If you do not specify this option, then CVU uses `dba` as the OSDBA group. |
| ``` -orainv orainventory_group ``` | The name of the Oracle Inventory group. If you do not specify this option, then CVU uses `oinstall` as the inventory group. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage -post hwos

Use the `cluvfy stage -post hwos` stage verification command to perform network and storage verifications on the specified nodes in the cluster before installing Oracle software. This command also checks for supported storage types and checks each one for sharing.

Syntax

```
cluvfy stage -post hwos -n node_list [-s storageID_list] [-verbose]
```

Parameters

Table A-32 cluvfy stage -post hwos Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -s storageID_list ``` | Checks the comma-delimited list of storage locations for sharing of supported storage types.  If you do not provide the `-s` option, then CVU discovers supported storage types and checks sharing for each of them. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage \[-pre | -post\] nodeadd

Use the `cluvfy stage -pre nodeadd` command to verify the specified nodes are configured correctly before adding them to your existing cluster, and to verify the integrity of the cluster before you add the nodes.

This command verifies that the system configuration, such as the operating system version, software patches, packages, and kernel parameters, for the nodes that you want to add, is compatible with the existing cluster nodes, and that the clusterware is successfully operating on the existing nodes. Run this command on any node of the existing cluster.

Use the `cluvfy stage -post nodeadd` command to verify that the specified nodes have been successfully added to the cluster at the network, shared storage, and clusterware levels.

Syntax

```
cluvfy stage -pre nodeadd -n node_list [-vip vip_list] 
 [-fixup [-fixupdir fixup_dir]] [-verbose]

cluvfy stage -post nodeadd -n node_list [-verbose]
```

Parameters

Table A-33 cluvfy stage \[-pre | -post\] nodeadd Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | A comma-delimited list of nondomain qualified node names on which to conduct the verification. These are the nodes you are adding or have added to the cluster. |
| `-v` `vip_list` | A comma-delimited list of virtual IP addresses to be used by the new nodes. |
| ``` -fixup [-fixupdir fixup_dir] ``` | Specifies that if the verification fails, then CVU generates fixup instructions, if feasible. Use the `-fixupdir` option to specify a specific directory in which CVU generates the fixup instructions. If you do not specify a directory, CVU uses its work directory. |
| ``` -verbose ``` | CVU prints detailed output. |

### cluvfy stage -post nodedel

Use the `cluvfy stage -post nodedel` command to verify that specific nodes have been successfully deleted from a cluster. Typically, this command verifies that the node-specific interface configuration details have been removed, the nodes are no longer a part of cluster configuration, and proper Oracle ASM cleanup has been performed.

Syntax

```
cluvfy stage -post nodedel -n node_list [-verbose]
```

Parameters

Table A-34 cluvfy stage -post nodedel Command Parameters

| Parameter | Description |
| --- | --- |
| ``` -n node_list ``` | The comma-delimited list of nondomain qualified node names on which to conduct the verification. If you specify `all`, then CVU checks all of the nodes in the cluster. |
| ``` -verbose ``` | CVU prints detailed output. |

Usage Notes

If the `cluvfy stage -post nodedel` check fails, then repeat the node deletion procedure.

See Also:

[Chapter 4, "Adding and Deleting Cluster Nodes"](adddelclusterware.md)

## Troubleshooting and Diagnostic Output for CVU

This section describes the following troubleshooting topics for CVU:

- Enabling Tracing
- Known Issues for the Cluster Verification Utility

### Enabling Tracing

You can enable tracing by setting the environment variable `SRVM_TRACE` to true. For example, in `tcsh` an entry such as `setenv SRVM_TRACE true` enables tracing.

The CVU trace files are created in the `CV_HOME/cv/log` directory by default. Oracle Database automatically rotates the log files and the most recently created log file has the name `cvutrace.log.0`. You should remove unwanted log files or archive them to reclaim disk place if needed.

CVU does not generate trace files unless you enable tracing. To use a non-default location for the trace files, set the `CV_TRACELOC` environment variable to the absolute path of the desired trace directory.

### Known Issues for the Cluster Verification Utility

This section describes the following known limitations for Cluster Verification Utility (CVU):

- Database Versions Supported by Cluster Verification Utility
- Linux Shared Storage Accessibility (ssa) Check Reports Limitations
- Shared Disk Discovery on Red Hat Linux

#### Database Versions Supported by Cluster Verification Utility

The current CVU release supports only Oracle Database 10g or higher, Oracle RAC, and Oracle Clusterware; CVU is not backward compatible. CVU cannot check or verify Oracle Database products for releases prior to Oracle Database 10g.

#### Linux Shared Storage Accessibility (ssa) Check Reports Limitations

The current release of `cluvfy` has the following limitations on Linux regarding shared storage accessibility check.

- OCFS2 (version 1.2.1 or higher) is supported.
- For sharedness checks on NAS, `cluvfy` commands require you to have write permission on the specified path. If the user running the `cluvfy` command does not have write permission, then `cluvfy` reports the path as `not` `shared`.

#### Shared Disk Discovery on Red Hat Linux

To perform discovery and shared storage accessibility checks for SCSI disks on Red Hat Linux 4.0 (or higher) and SUSE Linux Enterprise Server, CVU requires the CVUQDISK package. If you attempt to use CVU and the CVUQDISK package is not installed on all of the nodes in your Oracle RAC environment, then CVU responds with an error.

Perform the following procedure to install the CVUQDISK package:

1. Login as the `root` user.
2. Copy the package, `cvuqdisk-1.0.6-1.rpm` (or higher version) to a local directory. You can find this rpm in the `rpm` subdirectory of the top-most directory in the Oracle Clusterware installation media. For example, you can find `cvuqdisk-1.0.6-1.rpm` in the directory `/` `mountpoint` `/clusterware/rpm/` where `mountpoint` is the mount point for the disk on which the directory is located.
	```
	# cp /mount_point/clusterware/rpm/cvuqdisk-1.0.6-1.rpm /u01/oradba
	```
3. Set the `CVUQDISK_GRP` environment variable to the operating system group that should own the CVUQDISK package binaries. If `CVUQDISK_GRP` is not set, then, by default, the `oinstall` group is the owner's group.
	```
	# set CVUQDISK_GRP=oinstall
	```
4. Determine whether previous versions of the CVUQDISK package are installed by running the command `rpm -q cvuqdisk`. If you find previous versions of the CVUQDISK package, then remove them by running the command `rpm -e cvuqdisk` `previous_version` where `previous_version` is the identifier of the previous CVUQDISK version, as shown in the following example:
	```
	# rpm -q cvuqdisk
	cvuqdisk-1.0.2-1
	# rpm -e cvuqdisk-1.0.2-1
	```
5. Install the latest CVUQDISK package by running the command `rpm -iv cvuqdisk-1.0.6-1.rpm`.
	```
	# cd /u01/oradba
	# rpm -iv cvuqdisk-1.0.6-1.rpm
	```