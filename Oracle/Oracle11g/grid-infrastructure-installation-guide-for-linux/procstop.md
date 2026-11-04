---
title: How to Upgrade to Oracle Grid Infrastructure 11g Release 2
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/procstop.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## F How to Upgrade to Oracle Grid Infrastructure 11g Release 2

This appendix describes how to perform Oracle Clusterware and Oracle Automatic Storage Management upgrades.

Oracle Clusterware upgrades can be rolling upgrades, in which a subset of nodes are brought down and upgraded while other nodes remain active. Oracle Automatic Storage Management 11g Release 2 (11.2) upgrades can be rolling upgrades. If you upgrade a subset of nodes, then a software-only installation is performed on the existing cluster nodes that you do not select for upgrade.

This appendix contains the following topics:

## F.1 Back Up the Oracle Software Before Upgrades

Before you make any changes to the Oracle software, Oracle recommends that you create a backup of the Oracle software and databases.

## F.2 Unset Oracle Environment Variables

Unset Oracle environment variables.

If you have set ORA\_CRS\_HOME as an environment variable, following instructions from Oracle Support, then unset it before starting an installation or upgrade. You should never use ORA\_CRS\_HOME as an environment variable except under explicit direction from Oracle Support.

Check to ensure that installation owner login shell profiles (for example, `.profile` or `.cshrc`) do not have ORA\_CRS\_HOME set.

If you have had an existing installation on your system, and you are using the same user account to install this installation, then unset the following environment variables: ORA\_CRS\_HOME; ORACLE\_HOME; ORA\_NLS10; TNS\_ADMIN; and any other environment variable set for the Oracle installation user that is connected with Oracle software homes.

## F.3 About Oracle ASM and Oracle Grid Infrastructure Installation and Upgrade

In past releases, Oracle Automatic Storage Management (Oracle ASM) was installed as part of the Oracle Database installation. With Oracle Database 11g release 2 (11.2), Oracle ASM is installed when you install the Oracle Grid Infrastructure components and shares an Oracle home with Oracle Clusterware when installed in a cluster such as with Oracle RAC or with Oracle Restart on a standalone server.

If you have an existing Oracle ASM instance, you can either upgrade it at the time that you install Oracle Grid Infrastructure, or you can upgrade it after the installation, using Oracle ASM Configuration Assistant (ASMCA). However, be aware that a number of Oracle ASM features are disabled until you upgrade Oracle ASM, and Oracle Clusterware management of Oracle ASM does not function correctly until Oracle ASM is upgraded, because Oracle Clusterware only manages Oracle ASM when it is running in the Oracle Grid Infrastructure home. For this reason, Oracle recommends that if you do not upgrade Oracle ASM at the same time as you upgrade Oracle Clusterware, then you should upgrade Oracle ASM immediately afterward.

You can perform out-of-place upgrades to an Oracle ASM instance using Oracle ASM Configuration Assistant (ASMCA). In addition to running ASMCA using the graphic user interface, you can run ASMCA in non-interactive (silent) mode.

In prior releases, you could use Database Upgrade Assistant (DBUA) to upgrade either an Oracle Database, or Oracle ASM. That is no longer the case. You can only use DBUA to upgrade an Oracle Database instance. Use Oracle ASM Configuration Assistant (ASMCA) to upgrade Oracle ASM.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) and [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for additional information about upgrading existing Oracle ASM installations

## F.4 Restrictions for Clusterware and Oracle ASM Upgrades

Oracle recommends that you use CVU to check if here are any patches required for upgrading your existing Oracle Grid Infrastructure 11g release 2 or Oracle RAC database 11g Release 2 installations.

See Also:

Section F.6, "Using CVU to Validate Readiness for Oracle Clusterware Upgrades"

Be aware of the following restrictions and changes for upgrades to Oracle Grid Infrastructure installations, which consists of Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM):

- To upgrade existing Oracle Clusterware installations to Oracle Grid Infrastructure 11g, your release must be greater than or equal to 10.1.0.5, 10.2.0.3, 11.1.0.6, or 11.2.
- To upgrade existing Oracle Grid Infrastructure installations from 11.2.0.2 to a later release, you must apply patch 11.2.0.2.1 (11.2.0.2 PSU 1) or later.
- If you have Oracle ACFS file systems on Oracle Grid Infrastructure 11g release 2 (11.2.0.1), you upgrade Oracle Grid Infrastructure to any later version (11.2.0.2 or 11.2.0.3), and you take advantage of Redundant Interconnect Usage and add one or more additional private interfaces to the private network, then you must restart the Oracle ASM instance on each upgraded cluster member node.
- Do not delete directories in the Grid home. For example, do not delete Grid\_home/OPatch. If you delete the directory, then the Grid infrastructure installation owner cannot use OPatch to patch the Grid home, and OPatch displays the error "checkdir error: cannot create Grid\_home/OPatch'
- To upgrade existing 11.2.0.1 Oracle Grid Infrastructure installations to Oracle Grid Infrastructure 11.2.0.2, you must first verify if you need to apply any mandatory patches for upgrade to succeed. Refer to Section F.6 for steps to check readiness.
	See Also:
	"Oracle 11gR2 Upgrade Companion" Note 785351.1 on My Oracle Support:
	`https://support.oracle.com`
- To upgrade existing Oracle Grid Infrastructure from 11.2.0.2, to 11.2.0.3 or later, you must apply patch 11.2.0.2.1 (11.2.0.2 PSU 1) or later.
- To upgrade existing 11.1 Oracle Clusterware installations to Oracle Grid Infrastructure 11.2.0.3 or later, you must patch the release 11.1 Oracle Clusterware home with the patch for bug 7308467.
- Oracle Clusterware and Oracle ASM upgrades are always out-of-place upgrades. With 11g Release 2 (11.2), you cannot perform an in-place upgrade of Oracle Clusterware and Oracle ASM to existing homes.
- If the existing Oracle Clusterware home is a shared home, note that you can use a non-shared home for the Oracle Grid Infrastructure for a Cluster home for Oracle Clusterware and Oracle ASM 11g Release 2 (11.2).
- With Oracle Clusterware 11g release 1 and later releases, the same user that owned the Oracle Clusterware 10g software must perform the Oracle Clusterware 11g upgrade. Before Oracle Database 11g, either all Oracle software installations were owned by the Oracle user, typically `oracle`, or Oracle Database software was owned by `oracle`, and Oracle Clusterware software was owned by a separate user, typically `crs`.
- Oracle ASM and Oracle Clusterware both run in the Oracle Grid Infrastructure home.
- During a major version upgrade to 11g Release 2 (11.2), the software in the 11g Release 2 (11.2) Oracle Grid Infrastructure home is not fully functional until the upgrade is completed. Running `srvctl`, `crsctl`, and other commands from the 11g Release 2 (11.2) home is not supported until the final `rootupgrade.sh` script is run and the upgrade is complete across all nodes.
	To manage databases in the existing earlier version (release 10.x or 11.1) database homes during the Oracle Grid Infrastructure upgrade, use the `srvctl` from the existing database homes.
- During Oracle Clusterware installation, if there is a single instance Oracle ASM version on the local node, then it is converted to a clustered Oracle ASM 11g Release 2 (11.2) installation, and Oracle ASM runs in the Oracle Grid Infrastructure home on all nodes.
- With Oracle Clusterware 11g Release 2 (11.2) and later, you can perform upgrades on a shared Oracle Clusterware home.
- If a single instance (non-clustered) Oracle ASM installation is on a remote node, which is a node other than the local node (the node on which the Oracle Grid Infrastructure installation is being performed), then it will remain a single instance Oracle ASM installation. However, during installation, if you select to place the Oracle Cluster Registry (OCR) and voting disk files on Oracle ASM, then a clustered Oracle ASM installation is created on all nodes in the cluster, and the single instance Oracle ASM installation on the remote node will become nonfunctional.
- With the release of Oracle Database and Oracle RAC 11g Release 2 (11.2), using Database Configuration Assistant or the installer to store Oracle Clusterware or Oracle Database files on block or raw devices is not supported.
	If you intend to upgrade an existing Oracle RAC database, or an Oracle RAC database with Oracle ASM instances, then you can use an existing raw or block device partition, and perform a rolling upgrade of your existing installation. Performing a new installation using block or raw devices is not allowed.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm)

## F.5 Preparing to Upgrade an Existing Oracle Clusterware Installation

If you have an existing Oracle Clusterware installation, then you upgrade your existing cluster by performing an out-of-place upgrade. You cannot perform an in-place upgrade.

This section contains the following topics:

- Checks to Complete Before Upgrade an Existing Oracle Clusterware Installation
- Running the Oracle RACcheck Upgrade Readiness Assessment

### F.5.1 Checks to Complete Before Upgrade an Existing Oracle Clusterware Installation

Complete the following tasks before starting an upgrade:

1. For each node, use Cluster Verification Utility to ensure that you have completed preinstallation steps. It can generate Fixup scripts to help you to prepare servers. In addition, the installer will help you to ensure all required prerequisites are met.
	Ensure that you have information you will need during installation, including the following:
	- An Oracle base location for Oracle Clusterware.
		- An Oracle Grid Infrastructure home location that is different from your existing Oracle Clusterware location
		- A SCAN address
		- Privileged user operating system groups to grant access to Oracle ASM data files (the OSDBA for ASM group), to grant administrative privileges to the Oracle ASM instance (OSASM group), and to grant a subset of administrative privileges to the Oracle ASM instance (OSOPER for ASM group)
		- `root` user access, to run scripts as `root` during installation
2. For the installation owner running the installation, if you have environment variables set for the existing installation, then unset the environment variables `$ORACLE_HOME` and `$ORACLE_SID`, as these environment variables are used during upgrade. For example:
	```
	$ unset ORACLE_BASE
	$ unset ORACLE_HOME
	$ unset ORACLE_SID
	```
	See Also:
	Section F.2, "Unset Oracle Environment Variables"

### F.5.2 Running the Oracle RACcheck Upgrade Readiness Assessment

The RACcheck (Oracle RAC Configuration Audit Tool) Upgrade Readiness Assessment can be used to obtain an automated upgrade-specific health check for upgrades to Oracle Grid Infrastructure 11.2.0.3, 11.2.0.4, and 12.1.0.1. You can run the RACcheck Upgrade Readiness Assessment tool and automate many of the manual pre-upgrade and post upgrade checks.

Oracle recommends that you download and run the latest version of RACcheck from My Oracle Support. For information about downloading, configuring, and running RACcheck configuration audit tool, refer to My Oracle Support note 1457357.1, which is available at the following URL:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1457357.1`

## F.6 Using CVU to Validate Readiness for Oracle Clusterware Upgrades

Review the contents in this section to validate that your cluster is ready for upgrades.

### F.6.1 About the CVU Grid Upgrade Validation Command Options

Navigate to the staging area for the upgrade, where the `runcluvfy.sh` command is located, and run the command `runcluvfy.sh stage -pre crsinst -upgrade` to check the readiness of your Oracle Clusterware installation for upgrades. Running `runcluvfy.sh` with the `-pre crsinst -upgrade` flags performs system checks to confirm if the cluster is in a correct state for upgrading from an existing clusterware installation.

The command uses the following syntax, where variable content is indicated by italics:

```
runcluvfy.sh stage -pre crsinst -upgrade [-n node_list] [-rolling] -src_crshome 
src_Gridhome -dest_crshome dest_Gridhome -dest_version dest_version
[-fixup [-fixupdir path]] [-verbose]
```

The options are:

- `-n` `nodelist`
	The `-n` flag indicates cluster member nodes, and `nodelist` the comma-delimited list of non-domain qualified node names on which you want to run a preupgrade verification. If you do not add the `-n` flag to the verification command, then all the nodes in the cluster are verified. You must add the `-n` flag if the clusterware is down on the node where `runcluvfy.sh` is run.
- `-rolling`
	Use this flag to verify readiness for rolling upgrades.
- `-src_crshome` `src_Gridhome`
	Use this flag to indicate the location of the source Oracle Clusterware or Grid home that you are upgrading, where `src_Gridhome` is the path to the home that you want to upgrade.
- `-dest_crshome` `dest_Gridhome`
	Use this flag to indicate the location of the upgrade Grid home, where `dest_ Gridhome` is the path to the Grid home.
- `-dest_version` `dest_version`
	Use the `dest_version` flag to indicate the release number of the upgrade, including any patchset. The release number must include the five digits designating the release to the level of the platform-specific patch. For example: 11.2.0.2.0.
- `-fixup` \[`-fixupdir` `path`\]
	Use the `-fixup` flag to indicate that you want to generate instructions for any required steps you need to complete to ensure that your cluster is ready for an upgrade. The default location is the CVU work directory. If you want to place the fixup instructions in a different directory, then add the flag `-fixupdir`, and provide the path to the directory where you want to put the instructions for required fixes.
- `-verbose`
	Use the `-verbose` flag to produce detailed output of individual checks

### F.6.2 Example of Verifying System Upgrade Readiness for Grid Infrastructure

You can verify that the permissions required for installing Oracle Clusterware have been configured on the nodes `node1` and `node2` by running the following command:

```
$ ./runcluvfy.sh stage -pre crsinst -upgrade -n node1,node2 -rolling -src_crshome 
/u01/app/grid/11.2.0.1 -dest_crshome /u01/app/grid/11.2.0.2 -dest_version 11.2.0.3.0 -fixup -fixupdir /home/grid/fixup -verbose
```

### F.6.3 Verifying System Readiness for Oracle Database Upgrades

Use Cluster Verification Utility to assist you with system checks in preparation for starting a database upgrade. The installer runs the appropriate CVU checks automatically, and either prompts you to fix problems, or provides a fixup script to be run on all nodes in the cluster before proceeding with the upgrade.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm)

## F.7 Performing Rolling Upgrades From an Earlier Release

Use the following procedures to upgrade Oracle Clusterware or Oracle Automatic Storage Management:

- Performing a Rolling Upgrade of Oracle Clusterware
- Completing an Oracle Clusterware Upgrade when Nodes Become Unreachable
- Performing a Rolling Upgrade of Oracle Automatic Storage Management

Note:

When you upgrade to Oracle Clusterware 11g Release 2 (11.2), Oracle Automatic Storage Management (Oracle ASM) is installed in the same home as Oracle Clusterware. In Oracle documentation, this home is called the Oracle Grid Infrastructure home, or Grid home. Also note that Oracle does not support attempting to add additional nodes to a cluster during a rolling upgrade.

### F.7.1 Performing a Rolling Upgrade of Oracle Clusterware

Use the following procedure to upgrade Oracle Clusterware from an earlier release to a later release:

Note:

Oracle recommends that you leave Oracle RAC instances running. When you start the root script on each node, that node's instances are shut down and then started up again by the `rootupgrade.sh` script. If you upgrade from release 11.2.0.1 to any later version (11.2.0.2 or 11.2.0.3), then all nodes are selected by default. You cannot select or de-select the nodes.

For single instance Oracle Databases on the cluster, only those that use Oracle ASM need to be shut down. Listeners do not need to be shut down.

1. Start the installer, and select the option to upgrade an existing Oracle Clusterware and Oracle ASM installation.
2. On the node selection page, select all nodes.
3. Select installation options as prompted.
4. When prompted, run the `rootupgrade.sh` script on each node in the cluster that you want to upgrade.
	Run the script on the local node first. The script shuts down the earlier release installation, replaces it with the new Oracle Clusterware release, and starts the new Oracle Clusterware installation.
	After the script completes successfully, you can run the script in parallel on all nodes except for one, which you select as the last node. When the script is run successfully on all the nodes except the last node, run the script on the last node.
5. After running the `rootupgrade.sh` script on the last node in the cluster, if you are upgrading from a release earlier than release 11.2.0.1, and left the check box with ASMCA marked, as is the default, then Oracle ASM Configuration Assistant runs automatically, and the Oracle Clusterware upgrade is complete. If you uncloaked the box on the interview stage of the upgrade, then ASMCA is not run automatically.
	If an earlier version of Oracle Automatic Storage Management is installed, then the installer starts Oracle ASM Configuration Assistant to upgrade Oracle ASM to 11g Release 2 (11.2). You can choose to upgrade Oracle ASM at this time, or upgrade it later.
	Oracle recommends that you upgrade Oracle ASM at the same time that you upgrade the Oracle Clusterware binaries. Until Oracle ASM is upgraded, Oracle databases that use Oracle ASM cannot be created. Until Oracle ASM is upgraded, the 11g Release 2 (11.2) Oracle ASM management tools in the Grid home (for example, `srvctl`) will not work.
6. Because the Oracle Grid Infrastructure home is in a different location than the former Oracle Clusterware and Oracle ASM homes, update any scripts or applications that use utilities, libraries, or other files that reside in the Oracle Clusterware and Oracle ASM homes.

Note:

At the end of the upgrade, if you set the OCR backup location manually to the older release Oracle Clusterware home (CRS home), then you must change the OCR backup location to the Oracle Grid Infrastructure home (Grid home). If you did not set the OCR backup location manually, then this issue does not concern you.

Because upgrades of Oracle Clusterware are out-of-place upgrades, the previous release Oracle Clusterware home cannot be the location of the OCR backups. Backups in the old Oracle Clusterware home could be deleted.

### F.7.2 Completing an Oracle Clusterware Upgrade when Nodes Become Unreachable

If some nodes become unreachable in the middle of an upgrade, then you cannot complete the upgrade, because the upgrade script (`rootupgrade.sh`) did not run on the unreachable nodes. Because the upgrade is incomplete, Oracle Clusterware remains in the previous release version. You can confirm that the upgrade is incomplete by entering the command `crsctl query crs activeversion`.

To resolve this problem, run the `rootupgrade.sh` command with the `-force` flag using the following syntax:

Grid\_home/ `rootupgrade -force`

For example:

```
# /u01/app/11.2.0/grid/rootupgrade -force
```

This command forces the upgrade to complete. Verify that the upgrade has completed by using the command `crsctl query crs activeversion`. The active version should be the upgrade release.

### F.7.3 Performing a Rolling Upgrade of Oracle Automatic Storage Management

After you have completed the Oracle Clusterware 11g Release 2 (11.2) upgrade, if you did not choose to upgrade Oracle ASM when you upgraded Oracle Clusterware, then you can do it separately using the Oracle Automatic Storage Management Configuration Assistant (`asmca`) to perform rolling upgrades.

You can use asmca to complete the upgrade separately, but you should do it soon after you upgrade Oracle Clusterware, as Oracle ASM management tools such as `srvctl` will not work until Oracle ASM is upgraded.

Note:

ASMCA performs a rolling upgrade only if the earlier version of Oracle ASM is either 11.1.0.6 or 11.1.0.7. Otherwise, ASMCA performs a normal upgrade, in which ASMCA brings down all Oracle ASM instances on all nodes of the cluster, and then brings them all up in the new Grid home.

#### F.7.3.1 Preparing to Upgrade Oracle ASM

Note the following if you intend to perform rolling upgrades of Oracle ASM:

- The active version of Oracle Clusterware must be 11g Release 2 (11.2). To determine the active version, enter the following command:
	```
	$ crsctl query crs activeversion
	```
- You can upgrade a single instance Oracle ASM installation to a clustered Oracle ASM installation. However, you can only upgrade an existing single instance Oracle ASM installation if you run the installation from the node on which the Oracle ASM installation is installed. You cannot upgrade a single instance Oracle ASM installation on a remote node.
- You must ensure that any rebalance operations on your existing Oracle ASM installation are completed before starting the upgrade process.
- During the upgrade process, you alter the Oracle ASM instances to an upgrade state. Because this upgrade state limits Oracle ASM operations, you should complete the upgrade process soon after you begin. The following are the operations allowed when an Oracle ASM instance is in the upgrade state:
	- Diskgroup mounts and dismounts
		- Opening, closing, resizing, or deleting database files
		- Recovering instances
		- Queries of fixed views and packages: Users are allowed to query fixed views and run anonymous PL/SQL blocks using fixed packages, such as `dbms_diskgroup`)

#### F.7.3.2 Upgrading Oracle ASM

Complete the following procedure to upgrade Oracle ASM:

1. On the node you plan to start the upgrade, set the environment variable ASMCA\_ROLLING\_UPGRADE as true. For example:
	```
	$ export ASMCA_ROLLING_UPGRADE=true
	```
2. From the Oracle Grid Infrastructure 11g Release 2 (11.2) home, start ASMCA. For example:
	```
	$ cd /u01/11.2/grid/bin
	$ ./asmca
	```
3. Select Upgrade.
	ASM Configuration Assistant upgrades Oracle ASM in succession for all nodes in the cluster.
4. After you complete the upgrade, run the command to unset the ASMCA\_ROLLING\_UPGRADE environment variable.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) and [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for additional information about preparing an upgrade plan for Oracle ASM, and for starting, completing, and stopping Oracle ASM upgrades

## F.8 Updating DB Control and Grid Control Target Parameters

Because Oracle Clusterware release 2 (11.2) is an out-of-place upgrade of the Oracle Clusterware home in a new location (the Oracle Grid Infrastructure for a Cluster home, or Grid home), the path for the CRS\_HOME parameter in some parameter files must be changed. If you do not change the parameter, then you encounter errors such as "cluster target broken" on DB control or Grid control.

Use the following procedure to resolve this issue:

1. Log in to `dbconsole` or `gridconsole`.
2. Navigate to the Cluster tab.
3. Click Monitoring Configuration
4. Update the value for Oracle Home with the new Grid home path.

## F.9 Unlocking the Existing Oracle Clusterware Installation

After upgrade from previous releases, if you want to deinstall the previous release Oracle Grid Infrastructure Grid home, then you must first change the permission and ownership of the previous release Grid home. Complete this task using the following procedure:

Log in as root, and change the permission and ownership of the previous release Grid home using the following command syntax, where oldGH is the previous release Grid home, swowner is the Oracle Grid Infrastructure installation owner, and oldGHParent is the parent directory of the previous release Grid home:

  
#chmod -R 755 oldGH  
#chown -R swowner oldGH  
#chown swowner oldGHParent  

For example:

```
#chmod -R 755 /u01/app/11.2.0.1/grid
#chown -R grid /u01/app/11.2.0.1/grid
#chown grid /u01/app/11.2.0.1
```

After you change the permissions and ownership of the previous release Grid home, log in as the Oracle Grid Infrastructure Installation owner (grid, in the preceding example), and use the 11.2.0.2.0 standalone deinstallation tool to remove the previous release Grid home (oldGH).

You can obtain the standalone deinstallation tool from the following URL:

```
http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html
```

Click the See All link for the downloads for your operating system platform, and scan the list of downloads for the deinstall utility.

## F.10 Downgrading Oracle Clusterware After an Upgrade

After a successful or a failed upgrade to Oracle Clusterware 11g Release 2 (11.2), you can restore Oracle Clusterware to the previous version.

The restoration procedure in this section restores the Oracle Clusterware configuration to the state it was in before the Oracle Clusterware 11g Release 2 (11.2) upgrade. Any configuration changes you performed during or after the Oracle Grid Infrastructure 11g Release 2 (11.2) upgrade are removed and cannot be recovered.

In the following procedure, the local node is the first node on which the rootupgrade script was run. The remote nodes are all other nodes that were upgraded.

To restore Oracle Clusterware to the previous release:

1. Use the downgrade procedure for the release to which you want to downgrade.
	Downgrading to releases prior to 11g release 2 (11.2.0.1):
	On all remote nodes, use the command syntax Grid\_home `/perl/bin/perl rootcrs.pl -downgrade [-force]` to stop the 11g Release 2 (11.2) resources, shut down the 11g Release 2 (11.2) stack.
	Note:
	This command does not reset the OCR, or delete `ocr.loc`.
	Command syntax is as follows:
	```
	# /u01/app/11.2.0/grid/perl/bin/perl rootcrs.pl -downgrade -oldcrshome -version
	```
	For example:
	```
	# /u01/app/11.2.0/grid/perl/bin/perl rootcrs.pl -downgrade -oldcrshome 
	/u01/app/crs -version 11.1.0.1.0
	```
	Note:
	Ensure that Oracle Clusterware version is specified in the correct format. For example, 11.1.0.1.0.
	If you want to stop a partial or failed 11g Release 2 (11.2) installation and restore the previous release Oracle Clusterware, then use the `-force` flag with this command.
	Downgrading to a release 11.2.0.1 or later release:
	Use the command syntax Grid\_home `/perl/bin/perl rootcrs.pl -downgrade -oldcrshome` oldGridHomePath `-version` oldGridversion, where `oldGridhomepath` is the path to the previous release Oracle Grid Infrastructure home, and `oldGridversion` is the release to which you want to downgrade. For example:
	```
	# /u01/app/11.2.0/grid/perl/bin/perl rootcrs.pl -downgrade -oldcrshome /u01/app/11.2.0/grid -version 11.2.0.1.0
	```
	If you want to stop a partial or failed 11g release 2 (11.2) installation and restore the previous release Oracle Clusterware, then use the -force flag with this command.
2. After the `rootcrs.pl -downgrade` script has completed on all remote nodes, on the local node use the command syntax Grid\_home/crs/install/rootcrs.pl -downgrade -lastnode -oldcrshome pre11.2\_crs\_home -version pre11.2\_crs\_version \[-force\], where pre11.2\_crs\_home is the home of the earlier Oracle Clusterware installation, and pre11.2\_crs\_version is the release number of the earlier Oracle Clusterware installation.
	For example:
	```
	# /u01/app/11.2.0/grid/perl/bin/perl rootcrs.pl -downgrade  -lastnode -oldcrshome 
	/u01/app/crs -version 11.1.0.6.0
	```
	This script downgrades the OCR. If you want to stop a partial or failed 11g Release 2 (11.2) installation and restore the previous release Oracle Clusterware, then use the `-force` flag with this command.
3. Log in as the Grid infrastructure installation owner, and run the following commands, where `/u01/app/grid` is the location of the new (upgraded) Grid home (11.2):
	```
	.Grid_home/oui/bin/runInstaller -nowait -waitforcompletion -ignoreSysPrereqs -updateNodeList -silent CRS=false ORACLE_HOME=/u01/app/grid
	```
4. As the Grid infrastructure installation owner, run the command./runInstaller -nowait -waitforcompletion -ignoreSysPrereqs -updateNodeList -silent CRS=true ORACLE\_HOME=pre11.2\_crs\_home, where pre11.2\_crs\_home represents the home directory of the earlier Oracle Clusterware installation.
	For example:
	```
	.Grid_home/oui/bin/runInstaller -nowait -waitforcompletion -ignoreSysPrereqs -updateNodeList -silent CRS=true ORACLE_HOME=/u01/app/crs
	```
5. For downgrades to 11.2 and later releases
	1. If you are downgrading from Oracle Grid Infrastructure release 2 (11.2.0.4) to an earlier release of 11.2, after execution of `rootupgrade.sh` is completed on all cluster nodes, run the following command from the 11.2.0.4 Grid home:
		```
		acfsroot uninstall
		```
		2. From the earlier release Grid home, run the following command as a privileged user (`root`):
		```
		acfsroot install
		```
		3. On each node, start Oracle Clusterware from the earlier release Oracle Clusterware home using the command `crsctl start crs`. For example, where the earlier release home is `crshome11202`, use the following command on each node:
		`crshome11202/bin/crsctl start crs`
	For downgrades to 11.1 and earlier releases
	You are prompted to run `root.sh` from the earlier release Oracle Clusterware installation home in sequence on each member node of the cluster. After you complete this task, downgrade is completed.
	Running `root.sh` from the earlier release Oracle Clusterware installation home restarts the Oracle Clusterware stack, starts up all the resources previously registered with Oracle Clusterware in the older version, and configures the old initialization scripts to run the earlier release Oracle Clusterware stack.
6. Change the following environment variables to point to the directories of the release to which you are downgrading:
	- `ORACLE_HOME`
		- `PATH`
	Ensure that your `oratab` file and any client scripts that set the value of `ORACLE_HOME` point to the downgraded Oracle home.

## F.11 Checking Cluster Health Monitor Repository Size After Upgrading

If you are upgrading from a prior release using IPD/OS to Oracle Grid Infrastructure release 2 (11.2.0.2 and later), then you should review the Cluster Health Monitor repository size (the CHM repository). Oracle recommends that you review your CHM repository needs, and enlarge the repository size if you want to maintain a larger CHM repository.

Note:

Your previous IPD/OS repository is deleted when you install Oracle Grid Infrastructure, and you run the `root.sh` script on each node.

Cluster Health Monitor is not available with IBM: Linux on System z configurations.

By default, the CHM repository size for release 11.2.0.3 and later is a minimum of either 1GB or 3600 seconds (1 hour). For release 11.2.0.2 and 11.2.0.3, the CHM repository is one Gigabyte (1 GB), regardless of the size of the cluster.

To enlarge the CHM repository, use the following command syntax, where RETENTION\_TIME is the size of CHM repository in number of seconds:

oclumon manage -repos resize RETENTION\_TIME

The value for RETENTION\_TIME must be more than `3600` (one hour) and less than `259200` (three days). If you enlarge the CHM repository size, then you must ensure that there is local space available for the repository size you select on each node of the cluster. If there is not sufficient space available, then you can move the repository to shared storage.

For example, to set the repository size to four hours:

```
$ oclumon manage -repos resize 14400
```