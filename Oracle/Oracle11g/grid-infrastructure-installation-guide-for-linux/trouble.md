---
title: Troubleshooting the Oracle Grid Infrastructure Installation Process
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/trouble.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## A Troubleshooting the Oracle Grid Infrastructure Installation Process

This appendix provides troubleshooting information for installing Oracle Grid Infrastructure.

See Also:

The Oracle Database 11g Oracle RAC documentation set in the Documentation directory:

This appendix contains the following topics:

## A.1 General Installation Issues

The following is a list of examples of types of errors that can occur during installation. It contains the following issues:

- An error occurred while trying to get the disks
- Could not execute auto check for display colors using command /usr/X11R6/bin/xdpyinfo
- CRS-5823:Could not initialize agent framework.
- Failed to connect to server, Connection refused by server, or Can't open display
- Failed to initialize ocrconfig
- INS-32026 INSTALL\_COMMON\_HINT\_DATABASE\_LOCATION\_ERROR
- MEMORY\_TARGET not supported on this system
- Nodes unavailable for selection from the OUI Node Selection screen
- Node nodename is unreachable
- PROT-8: Failed to import data from specified file to the cluster registry
- PRVE-0038: The SSH LoginGraceTime setting, or fatal: Timeout before authentication
- root.sh or rootupgrade.sh Script Fails on the Second Node Due to Multicast Issues
- Timed out waiting for the CRS stack to start
- YPBINDPROC\_DOMAIN: Domain not bound
- Other Installation Issues and Errors

An error occurred while trying to get the disks

Cause: There is an entry in `/etc/oratab` pointing to a non-existent Oracle home. The OUI log file should show the following error: "java.io.IOException: /home/oracle/OraHome/bin/kfod: not found"

Action: Remove the entry in `/etc/oratab` pointing to a non-existing Oracle home.

CRS-5018:(:CLSN00037:) Removed unused HAIP route:

Cause: Typically, this error indicates that something (usually Zero Configuration Networking, `zeroconf`) has created the indicated route that is conflicting with the HAIP code. The error indicates that the Oracle software has removed the route to ensure appropriate stack functioning.

Action: The Zero Configuration Networking feature should be disabled when using Oracle Clusterware, as this feature may cause communication issues between cluster member nodes.

To disable Zero Configuration Networking:

1. Log in as root.
2. Change directory to `/etc/sysconfig`
3. Create a copy of `/etc/sysconfig/network`. For example:
	```
	# cp network network_old
	```
4. Use a text editor to open the file `/etc/sysconfig/network`.
5. Check the file for the value for `NOZEROCONF` to confirm that it is set to yes. If you do not find this parameter in the file, then append the following entry to the file:
	```
	NOZEROCONF=yes
	```
	Save the file after you update this setting.
6. Restart the network services. For example:
	```
	# service network restart
	```
7. Repeat this process on each cluster member node.

Could not execute auto check for display colors using command /usr/X11R6/bin/xdpyinfo

Cause: Either the DISPLAY variable is not set, or the user running the installation is not authorized to open an X window. This can occur if you run the installation from a remote terminal, or if you use an `su` command to change from a user that is authorized to open an X window to a user account that is not authorized to open an X window on the display, such as a lower-privileged user opening windows on the `root` user's console display.

Action: Run the command `echo $DISPLAY` to ensure that the variable is set to the correct visual or to the correct host. If the display variable is set correctly then either ensure that you are logged in as the user authorized to open an X window, or run the command `xhost +` to allow any user to open an X window.

If you are logged in locally on the server console as `root`, and used the su - command to change to the Oracle Grid Infrastructure installation owner, then log out of the server, and log back in as the grid installation owner.

CRS-5823:Could not initialize agent framework.

Cause: Installation of Oracle Grid Infrastructure fails when you run `root.sh`. Oracle Grid Infrastructure fails to start because the local host entry is missing from the hosts file.

The Oracle Grid Infrastructure alert.log file shows the following:

```
[/oracle/app/grid/bin/orarootagent.bin(11392)]CRS-5823:Could not initialize
agent framework. Details at (:CRSAGF00120:) in
/oracle/app/grid/log/node01/agent/crsd/orarootagent_root/orarootagent_root.log
2010-10-04 12:46:25.857
[ohasd(2401)]CRS-2765:Resource 'ora.crsd' has failed on server 'node01'.
```

You can verify this as the cause by checking `crsdOUT.log` file, and finding the following:

```
Unable to resolve address for localhost:2016
ONS runtime exiting
Fatal error: eONS: eonsapi.c: Aug 6 2009 02:53:02
```

Action: Add the local host entry in the hosts file.

Failed to connect to server, Connection refused by server, or Can't open display

Cause: These are typical of X Window display errors on Windows or UNIX systems, where `xhost` is not properly configured, or where you are running as a user account that is different from the account you used with the `startx` command to start the X server.

Action: In a local terminal window, log in as the user that started the X Window session, and enter the following command:

$ xhost fullyqualifiedRemoteHostname

For example:

```
$ xhost somehost.example.com
```

Then, enter the following commands, where `workstationname` is the host name or IP address of your workstation.

Bourne, Bash, or Korn shell:

```
$ DISPLAY=workstationname:0.0
$ export DISPLAY
```

To determine whether X Window applications display correctly on the local system, enter the following command:

```
$ xclock
```

The X clock should appear on your monitor. If this fails to work, then use of the `xhost` command may be restricted.

If you are using a VNC client to access the server, then ensure that you are accessing the visual that is assigned to the user that you are trying to use for the installation. For example, if you used the `su` command to become the installation owner on another user visual, and the `xhost` command use is restricted, then you cannot use the `xhost` command to change the display. If you use the visual assigned to the installation owner, then the correct display will be available, and entering the `xclock` command will display the X clock.

When the X clock appears, then close the X clock and start the installer again.

Failed to initialize ocrconfig

You have the wrong options configured for NFS in the `/etc/fstab` file.

You can confirm this by checking `ocrconfig.log` files located in the path `Grid_home` `/log/node` `number` `/client` and finding the following:

```
/u02/app/crs/clusterregistry, ret -1, errno 75, os err string Value too large
for defined data type
2007-10-30 11:23:52.101: [ OCROSD][3085960896]utopen:6'': OCR location
```

Action: For file systems mounted on NFS, provide the correct mount configuration for NFS mounts in the `/etc/fstab` file:
```
rw,sync,bg,hard,nointr,tcp,vers=3,timeo=300,rsize=32768,wsize=32768,actimeo=0
```

Note:

You should not have `netdev` in the mount instructions, or `vers=2`. The `netdev` option is only required for OCFS file systems, and `vers=2` forces the kernel to mount NFS using the older version 2 protocol.

After correcting the NFS mount information, remount the NFS mount point, and run the `root.sh` script again. For example, with the mount point `/u02`:

```
#umount /u02
#mount -a -t nfs
#cd $GRID_HOME
#sh root.sh
```

INS-32026 INSTALL\_COMMON\_HINT\_DATABASE\_LOCATION\_ERROR

Cause: The location selected for the Grid home for a cluster installation is located under an Oracle base directory.

Action: For Oracle Grid Infrastructure for a Cluster installations, the Grid home must not be placed under one of the Oracle base directories, or under Oracle home directories of Oracle Database installation owners, or in the home directory of an installation owner. During installation, ownership of the path to the Grid home is changed to `root`. This change causes permission errors for other installations. In addition, the Oracle Clusterware software stack may not come up under an Oracle base path.

MEMORY\_TARGET not supported on this system

Cause: On Linux systems, insufficient `/dev/shm` size for PGA and SGA.

If you are installing on a Linux system, note that Memory Size (SGA and PGA), which sets the initialization parameter MEMORY\_TARGET or MEMORY\_MAX\_TARGET, cannot be greater than the shared memory file system (`/dev/shm`) on your operating system.

Increase the `/dev/shm` mountpoint size. For example:
```
# mount -t tmpfs shmfs -o size=4g /dev/shm
```

Also, to make this change persistent across system restarts, add an entry in `/etc/fstab` similar to the following:

```
shmfs /dev/shm tmpfs size=4g 0
```

Nodes unavailable for selection from the OUI Node Selection screen

Cause: Oracle Grid Infrastructure is either not installed, or the Oracle Grid Infrastructure services are not up and running.

Action: Install Oracle Grid Infrastructure, or review the status of your installation. Consider restarting the nodes, as doing so may resolve the problem.

Node nodename is unreachable

Cause: Unavailable IP host

Action: Attempt the following:
1. Run the shell command `ifconfig -a`. Compare the output of this command with the contents of the `/etc/hosts` file to ensure that the node IP is listed.
2. Run the shell command `nslookup` to see if the host is reachable.

PROT-8: Failed to import data from specified file to the cluster registry

Cause: Insufficient space in an existing Oracle Cluster Registry device partition, which causes a migration failure while running `rootupgrade.sh`. To confirm, look for the error "utopen:12:Not enough space in the backing store" in the log file `Grid_home` `/log/` hostname `/client/ocrconfig_` `pid``.log`, where `pid` stands for the process id.

Action: Identify a storage device that has 300 MB or more available space. Oracle recommends that you allocate the entire disk to Oracle ASM.

PRVE-0038: The SSH LoginGraceTime setting, or fatal: Timeout before authentication

Cause: PRVE-0038: The SSH LoginGraceTime setting on node "nodename" may result in users being disconnected before login is completed. This error may because the default timeout value for SSH connections is too low, or if the LoginGraceTime parameter is commented out.

Action: Oracle recommends uncommenting the LoginGraceTime parameter in the OpenSSH configuration file `/etc/ssh/sshd_config`, and setting it to a value of 0 (unlimited).

root.sh or rootupgrade.sh Script Fails on the Second Node Due to Multicast Issues

In the final stages while running `root.sh` or `rootupgrade.sh` on the second node, the follow error is reported and the script fails:
```
Failed to start Cluster Synchorinisation Service in clustered mode at /u01/app/crs/11.2.0.2/crs/install/crsconfig_lib.pm line 1016.
```

Action: Multicast communication must be enabled on all cluster nodes. To determine if the multicast requirements are met, run the multicast test tool (`mcasttest.pl`). You might also be required to install patches.

Contact My Oracle Support for more information, and to obtain the multicast test tool and patches.

See Also:

[Section 2.7.4, "Multicast Requirements for Networks Used by Oracle Grid Infrastructure."](prelinux.md)

Timed out waiting for the CRS stack to start

Cause: If a configuration issue prevents the Oracle Grid Infrastructure software from installing successfully on all nodes, then you may see error messages such as "Timed out waiting for the CRS stack to start," or you may notice that Oracle Clusterware-managed resources were not create on some nodes after you exit the installer. You also may notice that resources have a status other than ONLINE.

See Also:

[Section 6.5, "Deconfiguring Oracle Clusterware Without Removing Binaries"](rem_orcl.md)

YPBINDPROC\_DOMAIN: Domain not bound

Cause: This error can occur during postinstallation testing when the public network interconnect for a node is pulled out, and the VIP does not fail over. Instead, the node hangs, and users are unable to log in to the system. This error occurs when the Oracle home, `listener.ora`, Oracle log files, or any action scripts are located on an NAS device or NFS mount, and the name service cache daemon `nscd` has not been activated.

Enter the following command on all nodes in the cluster to start the nscd service:
```
/sbin/service  nscd start
```

### A.1.1 Other Installation Issues and Errors

For additional help in resolving error messages, refer to My Oracle Support. For example, the note with Doc ID 1367631.1 contains some of the most common installation issues for Oracle Grid Infrastructure and Oracle Clusterware.

## A.2 Interpreting CVU "Unknown" Output Messages Using Verbose Mode

If you run Cluster Verification Utility using the `-verbose` argument, and a Cluster Verification Utility command responds with `UNKNOWN` for a particular node, then this is because Cluster Verification Utility cannot determine if a check passed or failed. The following is a list of possible causes for an "Unknown" response:

- The node is down
- Common operating system command binaries required by Cluster Verification Utility are missing in the `/bin` directory in the Oracle Grid Infrastructure home or Oracle home directory
- The user account starting Cluster Verification Utility does not have privileges to run common operating system commands on the node
- The node is missing an operating system patch, or a required package
- The node has exceeded the maximum number of processes or maximum number of open files, or there is a problem with IPC segments, such as shared memory or semaphores

## A.3 Interpreting CVU Messages About Oracle Grid Infrastructure Setup

If the Cluster Verification Utility report indicates that your system fails to meet the requirements for Oracle Grid Infrastructure installation, then use the topics in this section to correct the problem or problems indicated in the report, and run Cluster Verification Utility again.

- User Equivalence Check Failed
- Node Reachability Check or Node Connectivity Check Failed
- User Existence Check or User-Group Relationship Check Failed

User Equivalence Check Failed

Cause: Failure to establish user equivalency across all nodes. This can be due to not creating the required users, or failing to complete secure shell (SSH) configuration properly.

Action: Cluster Verification Utility provides a list of nodes on which user equivalence failed.

For each node listed as a failure node, review the installation owner user configuration to ensure that the user configuration is properly completed, and that SSH configuration is properly completed. The user that runs the Oracle Clusterware installation must have permissions to create SSH connections.

Oracle recommends that you use the SSH configuration option in OUI to configure SSH. You can use Cluster Verification Utility before installation if you configure SSH manually, or after installation, when SSH has been configured for installation.

For example, to check user equivalency for the user account `oracle`, use the command `su - oracle` and check user equivalence manually by running the `ssh` command on the local node with the `date` command argument using the following syntax:

```
$ ssh nodename date
```

The output from this command should be the timestamp of the remote node identified by the value that you use for `nodename`. If you are prompted for a password, then you need to configure SSH. If `ssh` is in the default location, the `/usr/bin` directory, then use `ssh` to configure user equivalence. You can also use `rsh` to confirm user equivalence.

If you see a message similar to the following when entering the date command with SSH, then this is the probable cause of the user equivalence error:

```
The authenticity of host 'node1 (140.87.152.153)' can't be established.
RSA key fingerprint is 7z:ez:e7:f6:f4:f2:4f:8f:9z:79:85:62:20:90:92:z9.
Are you sure you want to continue connecting (yes/no)?
```

Enter yes, and then run Cluster Verification Utility to determine if the user equivalency error is resolved.

If `ssh` is in a location other than the default, `/usr/bin`, then Cluster Verification Utility reports a user equivalence check failure. To avoid this error, navigate to the directory `Grid_home` `/cv/admin`, open the file `cvu_config` with a text editor, and add or update the key `ORACLE_SRVM_REMOTESHELL` to indicate the `ssh` path location on your system. For example:

```
# Locations for ssh and scp commands
ORACLE_SRVM_REMOTESHELL=/usr/local/bin/ssh
ORACLE_SRVM_REMOTECOPY=/usr/local/bin/scp
```

Note the following rules for modifying the `cvu_config` file:

- Key entries have the syntax name=value
- Each key entry and the value assigned to the key defines one property only
- Lines beginning with the number sign (#) are comment lines, and are ignored
- Lines that do not follow the syntax name=value are ignored

When you have changed the path configuration, run Cluster Verification Utility again. If `ssh` is in another location than the default, you also must start OUI with additional arguments to specify a different location for the remote shell and remote copy commands. Enter `runInstaller -help` to obtain information about how to use these arguments.

Note:

When you or OUI run `ssh` or `rsh` commands, including any login or other shell scripts they start, you may see errors about invalid arguments or standard input if the scripts generate any output. You should correct the cause of these errors.

To stop the errors, remove all commands from the `oracle` user's login scripts that generate output when you run `ssh` or `rsh` commands.

If you see messages about X11 forwarding, then complete the task ["Setting Display and X11 Forwarding Configuration"](prelinux.md) to resolve this issue.

If you see errors similar to the following:

```
stty: standard input: Invalid argument
stty: standard input: Invalid argument
```

These errors are produced if hidden files on the system (for example, `.bashrc` or `.cshrc`) contain `stty` commands. If you see these errors, then refer to [Chapter 2](prelinux.md), ["Preventing Installation Errors Caused by Terminal Output Commands"](prelinux.md) to correct the cause of these errors.

Node Reachability Check or Node Connectivity Check Failed

Cause: One or more nodes in the cluster cannot be reached using TCP/IP protocol, through either the public or private interconnects.

Action: Use the command `/bin/ping` `address` to check each node address. When you find an address that cannot be reached, check your list of public and private addresses to make sure that you have them correctly configured. If you use third-party vendor clusterware, then refer to the vendor documentation for assistance. Ensure that the public and private network interfaces have the same interface names on each node of your cluster.

User Existence Check or User-Group Relationship Check Failed

Cause: The administrative privileges for users and groups required for installation are missing or incorrect.

Action: Use the `id` command on each node to confirm that the installation owner user (for example, `grid` or `oracle`) is created with the correct group membership. Ensure that you have created the required groups, and create or modify the user account on affected nodes to establish required group membership.

See Also:

["Creating Groups, Users and Paths for Oracle Grid Infrastructure"](prelinux.md) in [Chapter 2](prelinux.md) for instructions about how to create required groups, and how to configure the installation owner user

## A.4 About the Oracle Clusterware Alert Log

The Oracle Clusterware alert log is the first place to look for serious errors. In the event of an error, it can contain path information to diagnostic logs that can provide specific information about the cause of errors.

After installation, Oracle Clusterware posts alert messages when important events occur. For example, you might see alert messages from the Cluster Ready Services (CRS) daemon process when it starts, if it aborts, if the failover process fails, or if automatic restart of a CRS resource failed.

Oracle Enterprise Manager monitors the Clusterware log file and posts an alert on the Cluster Home page if an error is detected. For example, if a voting disk is not available, a `CRS-1604` error is raised, and a critical alert is posted on the Cluster Home page. You can customize the error detection and alert settings on the Metric and Policy Settings page.

The location of the Oracle Clusterware log file is `CRS_home` `/log/` `hostname` `/alert` `hostname``.log`, where `CRS_home` is the directory in which Oracle Clusterware was installed and `hostname` is the host name of the local node.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm)

## A.5 Missing Operating System Packages On Linux

You have missing operating system packages on your system if you receive error messages such as the following during Oracle Grid Infrastructure, Oracle RAC, or Oracle Database installation:

```
libstdc++.so.5: cannot open shared object file: No such file or directory
libXp.so.6: cannot open shared object file: No such file or directory
```

Errors such as these should not occur, as missing packages should have been identified during installation. They may indicate that you are using an operating system distribution that has not been certified, or that you are using an older version of the Cluster Verification Utility.

If you have a Linux support network configured, such as the Red Hat network or Oracle Unbreakable Linux support, then use the `up2date` command to determine the name of the package. For example:

```
# up2date --whatprovides libstdc++.so.5
compat-libstdc++-33.3.2.3-47.3
```

Also, download the most recent version of Cluster Verification Utility to make sure that you have the current required packages list. You can obtain the most recent version at the following URL:

```
http://www.oracle.com/technetwork/database/options/clustering/downloads/cvu-download-homepage-099973.html
```

## A.6 Performing Cluster Diagnostics During Oracle Grid Infrastructure Installations

If the installer does not display the Node Selection page, then use the following command syntax to check the integrity of the Cluster Manager:

```
cluvfy comp clumgr -n node_list -verbose
```

In the preceding syntax example, the variable `node_list` is the list of nodes in your cluster, separated by commas.

Note:

If you encounter unexplained installation errors during or after a period when cron jobs are run, then your cron job may have deleted temporary files before the installation is finished. Oracle recommends that you complete installation before daily cron jobs are run, or disable daily cron jobs that perform cleanup until after the installation is completed.

## A.7 About Using CVU Cluster Healthchecks After Installation

Starting with Oracle Grid Infrastructure 11g release 2 (11.2.0.3) and later, you can use the CVU healthcheck command option to check your Oracle Clusterware and Oracle Database installations for their compliance with mandatory requirements and best practices guidelines, and to check to ensure that they are functioning properly.

Use the following syntax to run the healthcheck command option:

cluvfy comp healthcheck \[-collect {cluster|database}\] \[-db db\_unique\_name\] \[-bestpractice|-mandatory\] \[-deviations\] \[-html\] \[-save \[-savedir directory\_path\]

For example:

```
$ cd /home/grid/cvu_home/bin
$ ./cluvfy comp healthcheck -collect cluster -bestpractice -deviations -html
```

The options are:

- `-collect [cluster|database]`
	Use this flag to specify that you want to perform checks for Oracle Clusterware (cluster) or Oracle Database (database). If you do not use the collect flag with the healthcheck option, then cluvfy comp healthcheck performs checks for both Oracle Clusterware and Oracle Database.
- `-db` `db_unique_name`
	Use this flag to specify checks on the database unique name that you enter after the `db` flag.
	CVU uses JDBC to connect to the database as the user `cvusys` to verify various database parameters. For this reason, if you want checks to be performed for the database you specify with the `-db` flag, then you must first create the `cvusys` user on that database, and grant that user the CVU-specific role, `cvusapp`. You must also grant members of the `cvusapp` role `select` permissions on system tables.
	A SQL script is included in CVU\_home `/cv/admin/cvusys.sql` to facilitate the creation of this user. Use this SQL script to create the cvusys user on all the databases that you want to verify using CVU.
	If you use the `db` flag but do not provide a database unique name, then CVU discovers all the Oracle Databases on the cluster. If you want to perform best practices checks on these databases, then you must create the `cvusys` user on each database, and grant that user the `cvusapp` role with the `select` privileges needed to perform the best practice checks.
- `[-bestpractice | -mandatory] [-deviations`\]
	Use the `bestpractice` flag to specify best practice checks, and the `mandatory` flag to specify mandatory checks. Add the `deviations` flag to specify that you want to see only the deviations from either the best practice recommendations or the mandatory requirements. You can specify either the `-bestpractice` or `-mandatory` flag, but not both flags. If you specify neither `-bestpractice` or `-mandatory`, then both best practices and mandatory requirements are displayed.
- `-html`
	Use the `html` flag to generate a detailed report in HTML format.
	If you specify the `html` flag, and a browser CVU recognizes is available on the system, then the browser is started and the report is displayed on the browser when the checks are complete.
	If you do not specify the html flag, then the detailed report is generated in a text file.
- `-save [-savedir` `dir_path`\]
	Use the `save` or `-save -savedir` flags to save validation reports (`cvuchecdkreport_` `timestamp``.txt` and `cvucheckreport_` `timestamp``.htm`), where `timestamp` is the time and date of the validation report.
	If you use the `save` flag by itself, then the reports are saved in the path `CVU_home` `/cv/report`, where `CVU_home` is the location of the CVU binaries.
	If you use the flags `-save -savedir`, and enter a path where you want the CVU reports saved, then the CVU reports are saved in the path you specify.

## A.8 Interconnect Configuration Issues

If you plan to use multiple network interface cards (NICs) for the interconnect, and you do not configure them during installation or after installation with Redundant Interconnect Usage, then you should use a third party solution to bond the interfaces at the operating system level. Otherwise, the failure of a single NIC will affect the availability of the cluster node.

If you install Oracle Grid Infrastructure and Oracle RAC, then they must use the same NIC or bonded NIC cards for the interconnect.

If you use bonded NIC cards, then they must be on the same subnet.

If you encounter errors, then carry out the following system checks:

- Verify with your network providers that they are using correct cables (length, type) and software on their switches. In some cases, to avoid bugs that cause disconnects under loads, or to support additional features such as Jumbo Frames, you may need a firmware upgrade on interconnect switches, or you may need newer NIC driver or firmware at the operating system level. Running without such fixes can cause later instabilities to Oracle RAC databases, even though the initial installation seems to work.
- Review VLAN configurations, duplex settings, and auto-negotiation in accordance with vendor and Oracle recommendations.

## A.9 SCAN VIP and SCAN Listener Issues

If the final check of your installation reports errors related to the SCAN VIP addresses or listeners, then check the following items to make sure your network is configured correctly:

- Check the file `/etc/resolv.conf`, and verify the contents are the same on each node.
- Verify that there is a DNS entry for the SCAN, and that it resolves to three valid IP addresses. Use the command `nslookup` `scan-name`; this command should return the DNS server name, and the three IP addresses configured for the SCAN.
- Use the `ping` command to test the IP addresses assigned to the SCAN; you should receive a response for each IP address.
	Note:
	If you do not have a DNS configured for your cluster environment, then you can create an entry for the SCAN in the `/etc/hosts` file on each node. However, using the `/etc/hosts` file to resolve the SCAN results in having only one SCAN available for the entire cluster instead of three. Only the first entry for SCAN in the `hosts` file is used.
- Ensure the SCAN VIP uses the same netmask that is used by the public interface.

If you need additional assistance troubleshooting errors related to the SCAN, the SCAN VIP or listeners, then refer to My Oracle Support. For example, the note with Doc ID 1373350.1 contains some of the most common issues for SCANs and listeners.

## A.10 Storage Configuration Issues

The following is a list of issues involving storage configuration:

- Recovery from Losing a Node Filesystem or Grid Home
- Oracle ASM Library Driver Issues

### A.10.1 Recovery from Losing a Node Filesystem or Grid Home

With Oracle Clusterware release 11.2 and later, if you remove a filesystem by mistake, or encounter another storage configuration issue that results in losing the Oracle Local Registry or otherwise corrupting a node, you can recover the node in one of two ways:

1. Restore the node from an operating system level backup (preferred)
2. Remove the node, and then add the node. With 11.2 and later clusters, profile information for is copied to the node, and the node is restored.

The feature that enables cluster nodes to be removed and added again, so that they can be restored from the remaining nodes in the cluster, is called Grid Plug and Play (GPnP). Grid Plug and Play eliminates per-node configuration data and the need for explicit add and delete nodes steps. This allows a system administrator to take a template system image and run it on a new node with no further configuration. This removes many manual operations, reduces the opportunity for errors, and encourages configurations that can be changed easily. Removal of the per-node configuration makes the nodes easier to replace, because they do not need to contain individually-managed state.

Grid Plug and Play reduces the cost of installing, configuring, and managing database nodes by making their per-node state disposable. It allows nodes to be easily replaced with regenerated state.

Initiate recovery of a node using addnode syntax similar to the following, where `lostnode` is the node that you are adding back to the cluster:

If you are using Grid Naming Service (GNS):

```
$ ./addNode.sh -silent "CLUSTER_NEW_NODES=lostnode"
```

If you are not using GNS:

```
$ ./addNode.sh -silent "CLUSTER_NEW_NODES={lostnode}" "CLUSTER_NEW_VIRTUAL_HOSTNAMES={lostnode-vip}"
```

Note that you require access to root to be able to run the root.sh script on the node you restore, to recreate OCR keys and to perform other configuration tasks. When you see prompts to overwrite your existing information in /usr/local/bin, accept the default (n):

```
The file "dbhome" already exists in /usr/local/bin. Overwrite it? (y/n) [n]:
The file "oraenv" already exists in /usr/local/bin. Overwrite it? (y/n) [n]:
The file "coraenv" already exists in /usr/local/bin. Overwrite it? (y/n) [n]:
```

### A.10.2 Oracle ASM Library Driver Issues

The following is a list of Oracle ASM driver library error messages, and how to address these errors:

Asmtool: Unable to clear device "devicepath": Input/output error

Cause: This is a write access error that can have several causes

Action: If the disk is mounted, then unmount it. For example: `umount /dev/sdb1`. Make sure that the group and user that owns the device is the Oracle Grid Infrastructure installation owner and the oraInventory group. For example: `chown grid:oinstall`.

Unable to open ASMLib; Unable to find candidate disks 'ORCL:\*'

Cause: If you have created disks but you cannot discover candidate disks from Oracle Universal Installer, this could be due to a variety of configuration errors that prevent access to Oracle ASM storage.

Action: As the Oracle Grid Infrastructure installation owner, enter the command `/usr/sbin/oracleasm-discover`, using the ASM disk path asm\_diskstring. For example:
```
[grid@node1]$ /usr/sbin/oracleasm-discover 'ORCL:*'
```

If you do not have `/usr/sbin/oracleasm-discover`, then you do not have `oracleasmlib` installed. If you do have the command, then you should be able to determine if ASMLib is enabled, if disks are created, and if other tasks to create candidate disks are completed.

If you have resolved the issue, then you should see output similar to the following when you enter the command:

```
[grid@node1]$ /usr/sbin/oracleasm-discover 'ORCL:*'
 
Using ASMLib from /opt/oracle/extapi/64/asm/orcl/1/libasm.so
 
[ASM Library - Generic Linux, version 2.0.4 (KABI_V2)]
Discovered disk: ORCL:DISK1 [78140097 blocks (40007729664 bytes), maxio 512]
Discovered disk: ORCL:DISK2 [78140097 blocks (40007729664 bytes), maxio 512]
Discovered disk: ORCL:DISK3 [78140097 blocks (40007729664 bytes), maxio 512]
```

## A.11 Completing an Installation Before Finishing Running Scripts

When the `root.sh` script completes, you must click OK in OUI to finish the installation, and to start the configuration assistants. If OUI exits before the `root.sh` script has been run or has finished running, then the Oracle Grid Infrastructure installation is incomplete.

To complete an interrupted installation, as the `grid` user, on the node where the installation was started, run the following command:

`$` `Grid_home` `/cfgtoollogs/configToolAllCommands`

Run this command on only the first node. Running this command completes the Oracle Grid Infrastructure installation. If the `configToolAllCommands` file does not exist, then contact My Oracle Support for assistance in creating the file manually.