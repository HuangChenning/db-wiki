---
title: Advanced Installation Oracle Grid Infrastructure for a Cluster Preinstallation Tasks
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/prelinux.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## 2 Advanced Installation Oracle Grid Infrastructure for a Cluster Preinstallation Tasks

This chapter describes the system configuration tasks that you must complete before you start Oracle Universal Installer (OUI) to install Oracle Grid Infrastructure for a cluster, and that you may need to complete if you intend to install Oracle Real Application Clusters (Oracle RAC) on the cluster.

This chapter contains the following topics:

## 2.1 About Installing the Linux Operating System

Note:

Ensure you have minimum hardware configuration completed before installing the operating system.

This section provides information about installing a supported Linux distribution. It contains the following topics:

- Completing a Minimal Linux Installation
- Completing a Default Linux Installation
- About Oracle Linux and the Unbreakable Enterprise Kernel
- About the Oracle Preinstallation and Oracle Validated RPMs
- Installing the Oracle Preinstallation or Oracle Validated RPM with ULN Support
- Installing the Oracle Preinstallation RPM From DVDs or Images
- Using Ksplice to Perform a Zero Downtime Update

### 2.1.1 Completing a Minimal Linux Installation

To complete a minimal Linux installation, select one of the minimal installation options (either a custom installation where you select the Minimal option from Package Group Selection, or where you deselect all packages except for the Base pack). This installation lacks many RPMs required for database installation, so you must use an RPM package for your Oracle Linux release to install the required packages. The package you use depends on your Linux release, and your support status with Unbreakable Linux Network (ULN).

Note:

The Oracle Preinstallation RPM installs the X11 client libraries, but it does not install the X Window System server packages. To use graphical user interfaces such as OUI, configuration assistants, and Oracle Enterprise Manager, set the display to a system with X Window System server packages.

Refer to the following URL for documentation regarding installation of a reduced set of packages:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=728346.1`

Note:

If you are not a member of Unbreakable Linux Network or Red Hat Support network, and you are a My Oracle Support customer, then you can download instructions to configure a script that documents installation of a reduced set of packages:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=579101.1`

You can also search for "Linux reduced set of packages" to locate the instructions.

SSH is required for Oracle Grid Infrastructure installation. OpenSSH should be included in the Linux distribution minimal installation. To confirm that SSH packages are installed, enter the following command:

```
# rpm -qa |grep ssh
```

If you do not see a list of SSH packages, then install those packages for your Linux distribution.

Note:

The Oracle Preinstallation RPM installs the X11 client libraries, but does not install the X Window System server packages. To use graphical user interfaces such as OUI, configuration assistants, and Oracle Enterprise Manager, set the display to a system with X Window System server packages.

### 2.1.2 Completing a Default Linux Installation

If you do not install the Oracle Preinstallation RPM, then Oracle recommends that you install your Linux operating system with the default software packages (RPMs). This installation includes most of the required packages and helps you limit manual verification of package dependencies. Oracle recommends that you do not customize the RPMs during installation.

For information about a default installation, log on to My Oracle Support:

`https://support.oracle.com`

Search for "default rpms linux installation," and look for your Linux distribution. For example:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=ID 401167.1`

After installation, review system requirements for your distribution to ensure that you have all required kernel packages installed, and complete all other configuration tasks required for your distribution and system configuration.

### 2.1.3 About Oracle Linux and the Unbreakable Enterprise Kernel

Oracle's Unbreakable Enterprise Kernel delivers the latest innovations from upstream development to customers who run Red Hat Enterprise Linux (RHEL) 5 or Oracle Linux 5 in the data center. The Unbreakable Enterprise Kernel is included and enabled by default starting with Oracle Linux 5 Update 6.

The Unbreakable Enterprise Kernel is based on a recent stable mainline development Linux kernel, and also includes optimizations developed in collaboration with Oracle Database, Oracle middleware, and Oracle hardware engineering teams to ensure stability and optimal performance for the most demanding enterprise workloads.

Oracle highly recommends deploying the Oracle Unbreakable Enterprise Kernel in your Linux environment, especially if you run enterprise applications. However, using Oracle Unbreakable Enterprise Kernel is optional. If you require strict RHEL kernel compatibility, then Oracle Linux also includes a kernel compatible with the RHEL Linux kernel, compiled directly from the RHEL source code.

You can obtain more information about the Oracle Unbreakable Enterprise Kernel for Linux at the following URL:

```
http://www.oracle.com/us/technologies/linux
```

The Oracle Unbreakable Enterprise Kernel for Linux is the standard kernel used with Oracle products. The build and QA systems for Oracle Database and other Oracle products use the Oracle Unbreakable Enterprise Kernel for Linux exclusively. The Oracle Unbreakable Enterprise Kernel for Linux is also the kernel used in Oracle Exadata and Oracle Exalogic systems. Oracle Unbreakable Enterprise Kernel for Linux is used in all benchmark tests on Linux in which Oracle participates, as well as in the Oracle Preinstallation RPM program for x86-64.

Ksplice, which is part of Oracle Linux, updates the Linux operating system (OS) kernel, while it is running, without requiring restarts or any interruption. Ksplice is available only with Oracle Linux.

### 2.1.4 About the Oracle Preinstallation and Oracle Validated RPMs

If your Linux distribution is Oracle Linux and you are an Oracle Linux customer, then you can complete most preinstallation configuration tasks by using the Oracle Preinstallation RPM or Oracle Validated RPM for your release, which is available from the Oracle Linux Network, or available on the Oracle Linux DVDs. Using the Oracle Preinstallation RPM is not required, but Oracle recommends you use it to save time in setting up your cluster servers.

When it is installed, the Oracle Preinstallation RPM or Oracle Validated RPM does the following:

- Automatically downloads and installs any additional RPM packages needed for installing Oracle Grid Infrastructure and Oracle Database, and resolves any dependencies
- Creates an `oracle` user, and creates the oraInventory (`oinstall`) and OSDBA (`dba`) groups for that user
- As needed, sets `sysctl.conf` settings, system startup parameters, and driver parameters to values based on recommendations from the Oracle Preinstallation RPM program
- Sets hard and soft resource limits
- Sets other recommended parameters, depending on your kernel version

To become an Oracle Linux Network customer, contact your sales representative, or purchase a license from the Oracle Linux store:

`https://shop.oracle.com/product/oraclelinux`

To register your server on the Unbreakable Linux Network, or to find out more information, see the following URL:

`https://linux.oracle.com`

If you are using Oracle Linux 5.2 and higher, then the Oracle Preinstallation RPM is included on the install media.

Note:

The Oracle Preinstallation RPM designated for each Oracle Database release sets kernel parameters and resource limits only for the user account `oracle`. To use multiple software account owners, you must perform system configuration for other accounts manually.

You can obtain Linux kernels from the Oracle Linux public Yum repository. The public Yum repository for Oracle Linux 4, Oracle Linux 5 and Oracle Linux 6 is available at the following URL:

`http://public-yum.oracle.com/`

To become an Unbreakable Linux Network customer, contact your sales representative, or purchase a license from the Unbreakable Linux store:

`https://shop.oracle.com/product/oraclelinux`

To register your server on the Unbreakable Linux Network, or to find out more information, refer to the following URL:

`https://linux.oracle.com`

If you are using Oracle Linux 4.7 and higher, or Oracle Linux 5.2 and higher, then the Oracle Preinstallation or Oracle Validated RPM is included on the install media.

Note:

The Oracle Preinstallation RPM sets kernel parameters and resource limits only for the user account `oracle`. To use multiple software account owners, you must perform system configuration for other accounts manually.

In addition, users and groups are created using the next available ID numbers. If server group and user IDs are not identical on the cluster nodes where you run the Oracle Preinstallation RPM, then it is possible that these ids will be different on the nodes, and the different group and user IDs will cause installation to fail.

To avoid this issue, run the command `id` `user` on all nodes, where `user` is the software owner user account. If group or user IDs are not identical on all the nodes, then change them as necessary to ensure that they are identical.

### 2.1.5 Installing the Oracle Preinstallation or Oracle Validated RPM with ULN Support

Use the following procedure to subscribe to Unbreakable Linux Network (ULN) Oracle Linux channels, and to add the Oracle Linux channel that distributes the Oracle Preinstallation RPM or Oracle Validated RPM for your release:

1. Register your server with Unbreakable Linux Network (ULN). By default, you are registered for the Oracle Linux Latest channel for your operating system and hardware.
2. Log in to Unbreakable Linux Network:
	`https://linux.oracle.com`
3. Click the Systems tab, and in the System Profiles list, select a registered server. The System Details window opens and displays the subscriptions for the server.
4. Click Manage Subscriptions. The System Summary window opens.
5. From the Available Channels list, select the Linux installation media copy and update patch channels corresponding to your Oracle Linux distribution. For example, if your distribution is Oracle Linux 5 Update 6 for x86\_64, then select the following:
	- Oracle Linux 5 Update 6 installation media copy (x86\_64)
		- Oracle Linux 5 Update 6 Patch (x86\_64)
6. Click Subscribe.
7. Start a terminal session and enter the following command as `root`, depending on your platform.
	Oracle Linux 6:
	```
	# yum install oracle-rdbms-server-11gR2-preinstall
	```
	Oracle Linux 5 or Oracle Linux 4:
	```
	# yum install oracle-validated
	```
	You should see output indicating that you have subscribed to the Oracle Linux channel, and that packages are being installed. For example:
	```
	el5_u6_i386_base
	el5_u6_x86_64_patch
	```
	Oracle Linux automatically creates a standard (not role-allocated) Oracle installation owner and groups, and sets up other kernel configuration settings as required for Oracle installations.
8. Repeat steps 1 through 8 on all other servers in your cluster.
	Note:
	Check the RPM log file to review the system configuration changes. For example:
	Oracle Linux 6:
	```
	/var/log/oracle-rdbms-server-11gR2-preinstall/results/orakernel.log
	```
	Oracle Linux 5 and Oracle Linux 4:
	```
	/var/log/oracle-validated/results/orakernel.log
	```

### 2.1.6 Installing the Oracle Preinstallation RPM From DVDs or Images

Use the following procedure to install the Oracle Preinstallation RPM from the Oracle Linux distribution:

1. Obtain Oracle Linux disks either by ordering the Oracle Linux media pack from Oracle Store, or by downloading disk images from the Oracle Software Delivery Cloud website for Oracle Linux and Oracle VM.
	Oracle Store:
	```
	https://shop.oracle.com
	```
	Oracle Software Delivery Cloud website:
	```
	http://edelivery.oracle.com/linux
	```
2. Start the Oracle Linux installation.
3. Review the first software selection screen, which lists task-specific software options. At the bottom of the screen, there is an option to customize now or customize later. Select Customize now, and click Next.
4. Select Base System on the Customization page, in the list on the left side of the screen, and then select System Tools on the right side of the screen. Then click Optional Packages.
	The Packages in System Tools window opens.
5. Select the Oracle Preinstallation RPM package box from the package list, and click Next.
6. Complete the other screens to finish installing Oracle Linux.
	Oracle Linux automatically creates a standard (not role-allocated) Oracle installation owner and groups, and sets up other kernel configuration settings as required for Oracle installations.
7. Repeat steps 2 through 6 on all other cluster member nodes.

### 2.1.7 Using Ksplice to Perform a Zero Downtime Update

Ksplice Uptrack updates provide Linux security and bug fix updates, repackaged in a form that allows these updates to be applied without restarting the kernel.

To use Ksplice Uptrack:

1. Obtain or verify your Oracle Linux premium support subscription from Unbreakable Linux Network:
	`https://linux.oracle.com`
2. Log in as root.
3. Ensure that you have access to the Internet on the server where you want to use Ksplice. For example, if you are using a proxy server, then set the proxy server and port values in the shell with commands similar to the following:
	```
	# export http_proxy=http://proxy.example.com:port
	# export https_proxy=http://proxy.example.com:port
	```
4. Download the Ksplice Uptrack repository RPM package:
	`https://www.ksplice.com/yum/uptrack/ol/ksplice-uptrack-release.noarch.rpm`
5. Run the following commands:
	```
	rpm -i ksplice-uptrack-release.noarch.rpm
	yum -y install uptrack
	```
6. Open `/etc/uptrack/uptrack.conf` with a text editor, enter your premium support access key, and save the file. You must use the same access key for all of your systems.
7. Run the following command to carry out a zero downtime update of your kernel:
	```
	uptrack-upgrade -y
	```
	See Also:
	- The Oracle Ksplice Uptrack website for more information:
		`http://www.ksplice.com`
	- Oracle Ksplice for Oracle Linux:
		`http://oss.oracle.com/ksplice/docs/ksplice-quickstart.pdf`

## 2.2 Reviewing Upgrade Best Practices

Caution:

Always create a backup of existing databases before starting any configuration change.

If you have an existing Oracle installation, then record the version numbers, patches, and other configuration information, and review upgrade procedures for your existing installation. Review Oracle upgrade documentation before proceeding with installation, to decide how you want to proceed.

You can upgrade Oracle Automatic Storage Management (Oracle ASM) 11g release 1 (11.1) without shutting down an Oracle RAC database by performing a rolling upgrade either of individual nodes, or of a set of nodes in the cluster. However, if you have a standalone database on a cluster that uses Oracle ASM, then you must shut down the standalone database before upgrading. If you are upgrading from Oracle ASM 10g, then you must shut down the entire Oracle ASM cluster to perform the upgrade.

If you have an existing Oracle ASM installation, then review Oracle upgrade documentation. The location of the Oracle ASM home changes in this release, and you may want to consider other configuration changes to simplify or customize storage administration. If you have an existing Oracle ASM home from a previous release, then it should be owned by the same user that you plan to use to upgrade Oracle Clusterware.

During rolling upgrades of the operating system, Oracle supports using different operating system binaries when both versions of the operating system are certified with the Oracle Database release you are using.

Note:

Using mixed operating system versions is only supported for the duration of an upgrade, over the period of a few hours. Oracle Clusterware does not support nodes that have processors with different instruction set architectures (ISAs) in the same cluster. Each node must be binary compatible with the other nodes in the cluster. For example, you cannot have one node using an Intel 64 processor and another node using an IA-64 (Itanium) processor in the same cluster. You could have one node using an Intel 64 processor and another node using an AMD64 processor in the same cluster because the processors use the same x86-64 ISA and run the same binary version of Oracle software.

Your cluster can have nodes with CPUs of different speeds or sizes, but Oracle recommends that you use nodes with the same hardware configuration.

To find the most recent software updates, and to find best practices recommendations about preupgrade, postupgrade, compatibility, and interoperability, refer to "Oracle Upgrade Companion." "Oracle Upgrade Companion" is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com`

## 2.3 Installation Fixup Scripts

With Oracle Clusterware 11g release 2, Oracle Universal Installer (OUI) detects when the minimum requirements for an installation are not met, and creates shell scripts, called fixup scripts, to finish incomplete system configuration steps. If OUI detects an incomplete task, then it generates fixup scripts (`runfixup.sh`). You can run the fixup script after you click the Fix and Check Again Button.

You also can have CVU generate fixup scripts before installation.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for information about using the `cluvfy` command

The Fixup script does the following:

- If necessary sets kernel parameters to values required for successful installation, including:
	- Shared memory parameters.
		- Open file descriptor and UDP send/receive parameters.
- Sets permissions on the Oracle Inventory (central inventory) directory.
- Reconfigures primary and secondary group memberships for the installation owner, if necessary, for the Oracle Inventory directory and the operating system privileges groups.
- Sets shell limits if necessary to required values.

If you have SSH configured between cluster member nodes for the user account that you will use for installation, then you can check your cluster configuration before installation and generate a fixup script to make operating system changes before starting the installation.

To do this, log in as the user account that will perform the installation, navigate to the staging area where the runcluvfy command is located, and use the following command syntax, where node is a comma-delimited list of nodes you want to make cluster members:

$./runcluvfy.sh stage -pre crsinst -n node -fixup -verbose

For example, if you intend to configure a two-node cluster with nodes node1 and node2, enter the following command:

```
$ ./runcluvfy.sh stage -pre crsinst -n node1,node2 -fixup -verbose
```

## 2.4 Logging In to a Remote System Using X Terminal

During installation, you are required to perform tasks as root or as other users on remote terminals. Complete the following procedure for user accounts that you want to enable for remote display.

Note:

If you log in as another user (for example, `oracle`), then repeat this procedure for that user as well.

To enable remote display, complete one of the following procedures:

- If you are installing the software from an X Window System workstation or X terminal, then:
	1. Start a local terminal session, for example, an X terminal (`xterm`).
		2. If you are installing the software on another system and using the system as an X11 display, then enter a command using the following syntax to enable remote hosts to display X applications on the local X server:
		```
		# xhost + RemoteHost
		```
		where `RemoteHost` is the fully qualified remote host name. For example:
		```
		# xhost + somehost.example.com
		somehost.example.com being added to the access control list
		```
		3. If you are not installing the software on the local system, then use the `ssh` command to connect to the system where you want to install the software:
		```
		# ssh -Y RemoteHost
		```
		where `RemoteHost` is the fully qualified remote host name. The `-Y` flag ("yes") enables remote X11 clients to have full access to the original X11 display.For example:
		```
		# ssh -Y somehost.example.com
		```
		4. If you are not logged in as the `root` user, then enter the following command to switch the user to `root`:
		```
		$ su - root
		password:
		#
		```
- If you are installing the software from a PC or other system with X server software installed, then:
	Note:
	If necessary, refer to your X Window System documentation for more information about completing this procedure. Depending on the X software that you are using, you may need to complete the tasks in a different order.
	1. Start the X Window System software.
		2. Configure the security settings of the X Window System software to permit remote hosts to display X applications on the local system.
		3. Connect to the remote system where you want to install the software as the Oracle Grid Infrastructure for a cluster software owner (`grid`, `oracle`) and start a terminal session on that system; for example, an X terminal (`xterm`).
		4. Open another terminal on the remote system, and log in as the `root` user on the remote system, so you can run scripts as `root` when prompted.

## 2.5 Creating Groups, Users and Paths for Oracle Grid Infrastructure

Log in as `root`, and use the following instructions to locate or create the Oracle Inventory group and a software owner for Oracle Grid Infrastructure.

- Determining If the Oracle Inventory and Oracle Inventory Group Exists
- Creating the Oracle Inventory Group If an Oracle Inventory Does Not Exist
- Creating the Oracle Grid Infrastructure User
- Creating the Oracle Base Directory Path
- Creating Job Role Separation Operating System Privileges Groups and Users
- Example of Creating Standard Groups, Users, and Paths
- Example of Creating Role-allocated Groups, Users, and Paths

Note:

During an Oracle Grid Infrastructure installation, both Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) are installed. You no longer can have separate Oracle Clusterware installation owners and Oracle ASM installation owners.

### 2.5.1 Determining If the Oracle Inventory and Oracle Inventory Group Exists

When you install Oracle software on the system for the first time, OUI creates the `oraInst.loc` file. This file identifies the name of the Oracle Inventory group (by default, `oinstall`), and the path of the Oracle Central Inventory directory. An `oraInst.loc` file has contents similar to the following:

```
inventory_loc=central_inventory_location
inst_group=group
```

In the preceding example, `central_inventory_location` is the location of the Oracle central inventory, and `group` is the name of the group that has permissions to write to the central inventory (the OINSTALL group privilege).

If you have an existing Oracle central inventory, then ensure that you use the same Oracle Inventory for all Oracle software installations, and ensure that all Oracle software users you intend to use for installation have permissions to write to this directory.

To determine if you have an Oracle central inventory directory (`oraInventory`) on your system:

Enter the following command:

```
# more /etc/oraInst.loc
```

If the `oraInst.loc` file exists, then the output from this command is similar to the following:

```
inventory_loc=/u01/app/oracle/oraInventory
inst_group=oinstall
```

In the previous output example:

- The `inventory_loc` group shows the location of the Oracle Inventory.
- The `inst_group` parameter shows the name of the Oracle Inventory group (in this example, `oinstall`).

Use the command `grep` `groupname` `/etc/group` to confirm that the group specified as the Oracle Inventory group still exists on the system. For example:

```
$ grep oinstall /etc/group
oinstall:x:1000:grid,oracle
```

### 2.5.2 Creating the Oracle Inventory Group If an Oracle Inventory Does Not Exist

If the `oraInst.loc` file does not exist, then create the Oracle Inventory group by entering a command similar to the following:

```
# /usr/sbin/groupadd -g 1000 oinstall
```

The preceding command creates the oraInventory group `oinstall`, with the group ID number 1000. Members of the oraInventory group are granted privileges to write to the Oracle central inventory (`oraInventory`).

By default, if an oraInventory group does not exist, then the installer lists the primary group of the installation owner for the Oracle Grid Infrastructure for a Cluster software as the oraInventory group. Ensure that this group is available as a primary group for all planned Oracle software installation owners.

Note:

Group and user IDs must be identical on all nodes in the cluster. Check to make sure that the group and user IDs you want to use are available on each cluster member node, and confirm that the primary group for each Oracle Grid Infrastructure for a Cluster installation owner has the same name and group ID.

### 2.5.3 Creating the Oracle Grid Infrastructure User

You must create a software owner for Oracle Grid Infrastructure in the following circumstances:

- If an Oracle software owner user does not exist; for example, if this is the first installation of Oracle software on the system
- If an Oracle software owner user exists, but you want to use a different operating system user, with different group membership, to separate Oracle Grid Infrastructure administrative privileges from Oracle Database administrative privileges.
	In Oracle documentation, a user created to own only Oracle Grid Infrastructure software installations is called the `grid` user. A user created to own either all Oracle installations, or only Oracle database installations, is called the `oracle` user.

#### 2.5.3.1 Understanding Restrictions for Oracle Software Installation Owners

If you intend to use multiple Oracle software owners for different Oracle Database homes, then Oracle recommends that you create a separate software owner for Oracle Grid Infrastructure software (Oracle Clusterware and Oracle ASM), and use that owner to run the Oracle Grid Infrastructure installation.

If you plan to install Oracle Database or Oracle RAC, then Oracle recommends that you create separate users for the Oracle Grid Infrastructure and the Oracle Database installations. If you use one installation owner, then when you want to perform administration tasks, you must change the value for `$ORACLE_HOME` to the instance you want to administer (Oracle ASM, in the Oracle Grid Infrastructure home, or the database in the Oracle home), using command syntax such as the following example, where `/u01/app/11.2.0/grid` is the Oracle Grid Infrastructure home:

`$ ORACLE_HOME=/u01/app/11.2.0/grid; export ORACLE_HOME`

If you try to administer an instance using `sqlplus`, `lsnrctl`, or `asmcmd` commands while `$ORACLE_HOME` is set to a different binary path, then you will encounter errors. When starting srvctl from a database home, `$ORACLE_HOME` should be set or `srvctl` fails. But if you are using SRVCTL in the Oracle Grid Infrastructure home, then `$ORACLE_HOME` is ignored, and the oracle home path does not affect `srvctl` commands. You always have to change `$ORACLE_HOME` to the instance that you want to administer.

To create separate Oracle software owners to create separate users and separate operating system privileges groups for different Oracle software installations, note that each of these users must have the Oracle central inventory group (oraInventory group) as their primary group. Members of this group have write privileges to the Oracle central inventory (`oraInventory`) directory, and are also granted permissions for various Oracle Clusterware resources, OCR keys, directories in the Oracle Clusterware home to which DBAs need write access, and other necessary privileges. In Oracle documentation, this group is represented as `oinstall` in code examples.

Each Oracle software owner must be a member of the same central inventory group. Oracle recommends that you do not have more than one central inventory for Oracle installations. If an Oracle software owner has a different central inventory group, then you may corrupt the central inventory.

Caution:

For Oracle Grid Infrastructure for a Cluster installations, note the following restrictions for the Oracle Grid Infrastructure binary home (Grid home):
- It must not be placed under one of the Oracle base directories, including the Oracle base directory of the Oracle Grid Infrastructure installation owner.
- It must not be placed in the home directory of an installation owner

During installation, ownership of the path to the Grid home is changed to `root`. This change causes permission errors for other installations.

#### 2.5.3.2 Determining if an Oracle Software Owner User Exists

To determine whether an Oracle software owner user named `oracle` or `grid` exists, enter a command similar to the following (in this case, to determine if `oracle` exists):

```
# id oracle
```

If the user exists, then the output from this command is similar to the following:

```
uid=501(oracle) gid=501(oinstall) groups=502(dba),503(oper)
```

Determine whether you want to use the existing user, or create another user. The user and group ID numbers must be the same on each node you intend to make a cluster member node.

To use the existing user, ensure that the user's primary group is the Oracle Inventory group (`oinstall`). If this user account will be used for Oracle Database installations, then ensure that the Oracle account is also a member of the group you plan to designate as the OSDBA for ASM group (the group whose members are permitted to write to Oracle ASM storage).

#### 2.5.3.3 Creating or Modifying an Oracle Software Owner User for Oracle Grid Infrastructure

If the Oracle software owner (`oracle`, `grid`) user does not exist, or if you require a new Oracle software owner user, then create it. If you want to use an existing user account, then modify it to ensure that the user ID and group IDs are the same on each cluster member node. The following procedures use `grid` as the name of the Oracle software owner, and `dba` as the OSASM group. To create separate system privilege groups to separate administration privileges, complete group creation before you create the user, as described in Section 2.5.5, "Creating Job Role Separation Operating System Privileges Groups and Users,".

1. To create a grid installation owner account where you have an existing system privileges group (in this example, `dba`), whose members you want to have granted the SYSASM privilege to administer the Oracle ASM instance, enter a command similar to the following:
	```
	# /usr/sbin/useradd -u 1100 -g oinstall -G dba grid
	```
	In the preceding command:
	- The `-u` option specifies the user ID. Using this command flag is optional, as you can allow the system to provide you with an automatically generated user ID number. However, you must make note of the user ID number of the user you create for Oracle Grid Infrastructure, as you require it later during preinstallation, and you must have the same user ID number for this user on all nodes of the cluster.
		- The `-g` option specifies the primary group, which must be the Oracle Inventory group. For example: `oinstall`.
		- The `-G` option specified the secondary group, which in this example is `dba`.
		The secondary groups must include the OSASM group, whose members are granted the SYSASM privilege to administer the Oracle ASM instance. You can designate a unique group for the SYSASM system privileges, separate from database administrator groups, or you can designate one group as the OSASM and OSDBA group, so that members of that group are granted the SYSASM and SYSDBA privileges to grant system privileges to administer both the Oracle ASM instances and Oracle Database instances. In code examples, this group is `asmadmin`.
		If you are creating this user to own both Oracle Grid Infrastructure and an Oracle Database installation, then this user must have the OSDBA for ASM group as a secondary group. In code examples, this group name is `asmdba`. Members of the OSDBA for ASM group are granted access to Oracle ASM storage. You must create an OSDBA for ASM group if you plan to have multiple databases accessing Oracle ASM storage, or you must use the same group as the OSDBA for all databases, and for the OSDBA for ASM group.
	Use the `usermod` command to change existing user ID numbers and groups.
	For example:
	```
	# id oracle
	uid=501(oracle) gid=501(oracle) groups=501(oracle)
	# /usr/sbin/usermod -u 1001 -g 1000 -G 1000,1001 oracle
	# id oracle
	uid=1001(oracle) gid=1000(oinstall) groups=1000(oinstall),1001(oracle)
	```
2. Set the password of the user that will own Oracle Grid Infrastructure. For example:
	```
	# passwd grid
	```
3. Repeat this procedure on all of the other nodes in the cluster.

Note:

If necessary, contact your system administrator before using or modifying an existing user.

Oracle recommends that you do not use the UID and GID defaults on each node, as group and user IDs likely will be different on each node. Instead, provide common assigned group and user IDs, and confirm that they are unused on any node before you create or modify groups and users.

### 2.5.4 Creating the Oracle Base Directory Path

The Oracle base directory for the grid installation owner is the location where diagnostic and administrative logs, and other logs associated with Oracle ASM and Oracle Clusterware are stored.

If you have created a path for the Oracle Clusterware home that is compliant with Oracle Optimal Flexible Architecture (OFA) guidelines for Oracle software paths then you do not need to create an Oracle base directory. When OUI finds an OFA-compliant path, it creates the Oracle base directory in that path.

For OUI to recognize the path as an Oracle software path, it must be in the form u\[00-99\]/app, and it must be writable by any member of the oraInventory (`oinstall`) group. The OFA path for the Oracle base is `/u01/app/` `user`, where `user` is the name of the software installation owner.

Oracle recommends that you create an Oracle Grid Infrastructure Grid home and Oracle base homes manually, particularly if you have separate Oracle Grid Infrastructure for a cluster and Oracle Database software owners, so that you can separate log files.

For example:

```
# mkdir -p  /u01/app/11.2.0/grid
# mkdir -p /u01/app/grid
# mkdir -p /u01/app/oracle
# chown grid:oinstall /u01/app/11.2.0/grid
# chown grid:oinstall /u01/app/grid
# chown oracle:oinstall /u01/app/oracle
# chmod -R 775 /u01/
# chown -R grid:oinstall /u01
```

Note:

Placing Oracle Grid Infrastructure for a cluster binaries on a cluster file system is not supported.

If you plan to install an Oracle RAC home on a shared OCFS2 location, then you must upgrade OCFS2 to at least version 1.4.1, which supports shared writable `mmap` s.

### 2.5.5 Creating Job Role Separation Operating System Privileges Groups and Users

A job role separation privileges configuration of Oracle ASM is a configuration with groups and users that divide administrative access privileges to the Oracle ASM installation from other administrative privileges users and groups associated with other Oracle installations. Administrative privileges access is granted by membership in separate operating system groups, and installation privileges are granted by using different installation owners for each Oracle installation.

Note:

This configuration is optional, to restrict user access to Oracle software by responsibility areas for different administrator users.

If you prefer, you can allocate operating system user privileges so that you can use one administrative user and one group for operating system authentication for all system privileges on the storage and database tiers.

For example, you can designate the `oracle` user to be the installation owner for all Oracle software, and designate `oinstall` to be the group whose members are granted all system privileges for Oracle Clusterware, Oracle ASM, and all Oracle Databases on the servers, and all privileges as installation owners. This group must also be the Oracle Inventory group.

Oracle recommends that you use at least two groups: A system privileges group whose members are granted administrative system privileges, and an installation owner group (the oraInventory group) to provide separate installation privileges (the `OINSTALL` privilege). To simplify using the defaults for Oracle tools such as Cluster Verification Utility, if you do choose to use a single operating system group to grant all system privileges and the right to write to the oraInventory, then that group name should be `oinstall`.

- Overview of Creating Job Role Separation Groups and Users
- Creating Database Groups and Users with Job Role Separation

Note:

To use a directory service, such as Network Information Services (NIS), refer to your operating system documentation for further information.

#### 2.5.5.1 Overview of Creating Job Role Separation Groups and Users

This section provides an overview of how to create users and groups to use job role separation. Log in as `root` to create these groups and users.

- Users for Oracle Installations with Job Role Separation
- Database Groups for Job Role Separation Installations
- Oracle ASM Groups for Job Role Separation Installations

##### 2.5.5.1.1 Users for Oracle Installations with Job Role Separation

Oracle recommends that you create the following operating system groups and users for all installations where you create separate software installation owners:

One software owner to own each Oracle software product (typically, `oracle`, for the database software owner user, and `grid` for Oracle Grid Infrastructure.

You must create at least one software owner the first time you install Oracle software on the system. This user owns the Oracle binaries of the Oracle Grid Infrastructure software, and you can also make this user the owner of the Oracle Database or Oracle RAC binaries.

Oracle software owners must have the Oracle Inventory group as their primary group, so that each Oracle software installation owner can write to the central inventory (`oraInventory`), and so that OCR and Oracle Clusterware resource permissions are set correctly. The database software owner must also have the OSDBA group and (if you create it) the OSOPER group as secondary groups. In Oracle documentation, when Oracle software owner users are referred to, they are called `oracle` users.

Oracle recommends that you create separate software owner users to own each Oracle software installation. Oracle particularly recommends that you do this if you intend to install multiple databases on the system.

In Oracle documentation, a user created to own the Oracle Grid Infrastructure binaries is called the `grid` user. This user owns both the Oracle Clusterware and Oracle Automatic Storage Management binaries.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about the OSDBA, OSASM and OSOPER groups and the SYSDBA, SYSASM and SYSOPER privileges

##### 2.5.5.1.2 Database Groups for Job Role Separation Installations

The following operating system groups and user are required if you are installing Oracle Database:

- The OSDBA group (typically, `dba`)
	You must create this group the first time you install Oracle Database software on the system. This group identifies operating system user accounts that have database administrative privileges (the SYSDBA privilege). If you do not create separate OSDBA, OSOPER and OSASM groups for the Oracle ASM instance, then operating system user accounts that have the SYSOPER and SYSASM privileges must be members of this group. The name used for this group in Oracle code examples is `dba`. If you do not designate a separate group as the OSASM group, then the OSDBA group you define is also by default the OSASM group.
	To specify a group name other than the default `dba` group, then you must choose the Advanced installation type to install the software or start Oracle Universal Installer (OUI) as a user that is not a member of this group. In this case, OUI prompts you to specify the name of this group.
	Members of the OSDBA group formerly were granted SYSASM privileges on Oracle ASM instances, including mounting and dismounting disk groups. This privileges grant is removed with Oracle Grid Infrastructure 11g release 2, if different operating system groups are designated as the OSDBA and OSASM groups. If the same group is used for both OSDBA and OSASM, then the privilege is retained.
- The OSOPER group for Oracle Database (typically, `oper`)
	This is an optional group. Create this group if you want a separate group of operating system users to have a limited set of database administrative privileges (the `SYSOPER` privilege). By default, members of the OSDBA group also have all privileges granted by the `SYSOPER` privilege.
	To use the OSOPER group to create a database administrator group with fewer privileges than the default `dba` group, then you must choose the Advanced installation type to install the software or start OUI as a user that is not a member of the `dba` group. In this case, OUI prompts you to specify the name of this group. The usual name chosen for this group is `oper`.

##### 2.5.5.1.3 Oracle ASM Groups for Job Role Separation Installations

SYSASM is a new system privilege that enables the separation of the Oracle ASM storage administration privilege from SYSDBA. With Oracle Automatic Storage Management 11g Release 2 (11.2), members of the database OSDBA group are not granted SYSASM privileges, unless the operating system group designated as the OSASM group is the same group designated as the OSDBA group.

Select separate operating system groups as the operating system authentication groups for privileges on Oracle ASM. Before you start OUI, create the following groups and users for Oracle ASM:

- The Oracle Automatic Storage Management Group (typically `asmadmin`)
	This is a required group. Create this group as a separate group if you want to have separate administration privilege groups for Oracle ASM and Oracle Database administrators. In Oracle documentation, the operating system group whose members are granted privileges is called the OSASM group, and in code examples, where there is a group specifically created to grant this privilege, it is referred to as `asmadmin`.
	If you have multiple databases on your system, and use multiple OSDBA groups so that you can provide separate SYSDBA privileges for each database, then you should create a separate OSASM group, and use a separate user from the database users to own the Oracle Grid Infrastructure installation (Oracle Clusterware and Oracle ASM). Oracle ASM can support multiple databases.
	Members of the OSASM group can use SQL to connect to an Oracle ASM instance as SYSASM using operating system authentication. The SYSASM privileges permit mounting and dismounting disk groups, and other storage administration tasks. SYSASM privileges provide no access privileges on an RDBMS instance.
- The ASM Database Administrator group (OSDBA for ASM, typically `asmdba`)
	Members of the ASM Database Administrator group (OSDBA for ASM) are granted read and write access to files managed by Oracle ASM. The Oracle Grid Infrastructure installation owner and all Oracle Database software owners must be a member of this group, and all users with OSDBA membership on databases that have access to the files managed by Oracle ASM must be members of the OSDBA group for ASM.
- Members of the ASM Operator Group (OSOPER for ASM, typically `asmoper`)
	This is an optional group. Create this group if you want a separate group of operating system users to have a limited set of Oracle ASM instance administrative privileges (the SYSOPER for ASM privilege), including starting up and stopping the Oracle ASM instance. By default, members of the OSASM group also have all privileges granted by the SYSOPER for ASM privilege.
	To use the Oracle ASM Operator group to create an Oracle ASM administrator group with fewer privileges than the default `asmadmin` group, then you must choose the Advanced installation type to install the software, In this case, OUI prompts you to specify the name of this group. In code examples, this group is `asmoper`.

#### 2.5.5.2 Creating Database Groups and Users with Job Role Separation

The following sections describe how to create the required operating system user and groups:.

- Creating the OSDBA Group to Prepare for Database Installations
- Creating an OSOPER Group for Database Installations
- Creating the OSASM Group
- Creating the OSOPER for ASM Group
- Creating the OSDBA for ASM Group for Database Access to Oracle ASM
- When to Create the Oracle Software Owner User
- Determining if an Oracle Software Owner User Exists
- Creating an Oracle Software Owner User
- Modifying an Existing Oracle Software Owner User
- Creating Identical Database Users and Groups on Other Cluster Nodes

##### 2.5.5.2.1 Creating the OSDBA Group to Prepare for Database Installations

If you intend to install Oracle Database to use with the Oracle Grid Infrastructure installation, then you must create an OSDBA group in the following circumstances:

- An OSDBA group does not exist; for example, if this is the first installation of Oracle Database software on the system
- An OSDBA group exists, but you want to give a different group of operating system users database administrative privileges for a new Oracle Database installation

If the OSDBA group does not exist, or if you require a new OSDBA group, then create it as follows. Use the group name `dba` unless a group with that name already exists:

```
# /usr/sbin/groupadd -g 1031 dba
```

##### 2.5.5.2.2 Creating an OSOPER Group for Database Installations

Create an OSOPER group only if you want to identify a group of operating system users with a limited set of database administrative privileges (SYSOPER operator privileges). For most installations, it is sufficient to create only the OSDBA group. To use an OSOPER group, then you must create it in the following circumstances:

- If an OSOPER group does not exist; for example, if this is the first installation of Oracle Database software on the system
- If an OSOPER group exists, but you want to give a different group of operating system users database operator privileges in a new Oracle installation

If you require a new OSOPER group, then create it as follows. Use the group name `oper` unless a group with that name already exists.

```
# /usr/sbin/groupadd -g 1032 oper1
```

##### 2.5.5.2.3 Creating the OSASM Group

If the OSASM group does not exist or if you require a new OSASM group, then create it as follows. Use the group name `asmadmin` unless a group with that name already exists:

```
# /usr/sbin/groupadd -g 1020 asmadmin
```

##### 2.5.5.2.4 Creating the OSOPER for ASM Group

Create an OSOPER for ASM group if you want to identify a group of operating system users, such as database administrators, whom you want to grant a limited set of Oracle ASM storage tier administrative privileges, including the ability to start up and shut down the Oracle ASM storage. For most installations, it is sufficient to create only the OSASM group, and provide that group as the OSOPER for ASM group during the installation interview.

If you require a new OSOPER for ASM group, then create it as follows. In the following, use the group name `asmoper` unless a group with that name already exists:

```
# /usr/sbin/groupadd -g 1022 asmoper
```

##### 2.5.5.2.5 Creating the OSDBA for ASM Group for Database Access to Oracle ASM

You must create an OSDBA for ASM group to provide access to the Oracle ASM instance. This is necessary if OSASM and OSDBA are different groups.

If the OSDBA for ASM group does not exist or if you require a new OSDBA for ASM group, then create it as follows. Use the group name `asmdba` unless a group with that name already exists:

```
# /usr/sbin/groupadd -g 1021 asmdba
```

##### 2.5.5.2.6 When to Create the Oracle Software Owner User

You must create an Oracle software owner user in the following circumstances:

- If an Oracle software owner user exists, but you want to use a different operating system user, with different group membership, to give database administrative privileges to those groups in a new Oracle Database installation.
- If you have created an Oracle software owner for Oracle Grid Infrastructure, such as `grid`, and you want to create a separate Oracle software owner for Oracle Database software, such as `oracle`.

##### 2.5.5.2.7 Determining if an Oracle Software Owner User Exists

To determine whether an Oracle software owner user named `oracle` or `grid` exists, enter a command similar to the following (in this case, to determine if `oracle` exists):

```
# id oracle
```

If the user exists, then the output from this command is similar to the following:

```
uid=501(oracle) gid=501(oinstall) groups=502(dba),503(oper)
```

Determine whether you want to use the existing user, or create another user. To use the existing user, ensure that the user's primary group is the Oracle Inventory group and that it is a member of the appropriate OSDBA and OSOPER groups. Refer to one of the following sections for more information:

- To modify an existing user, refer to Section 2.5.5.2.9, "Modifying an Existing Oracle Software Owner User."
- To create a user, refer to Section 2.5.5.2.8, "Creating an Oracle Software Owner User."

Note:

If necessary, contact your system administrator before using or modifying an existing user.

Oracle recommends that you do not use the UID and GID defaults on each node, as group and user IDs likely will be different on each node. Instead, provide common assigned group and user IDs, and confirm that they are unused on any node before you create or modify groups and users.

##### 2.5.5.2.8 Creating an Oracle Software Owner User

If the Oracle software owner user does not exist, or if you require a new Oracle software owner user, then create it as follows. Use the user name `oracle` unless a user with that name already exists.

1. To create an `oracle` user, enter a command similar to the following:
	```
	# /usr/sbin/useradd -u 1101 -g oinstall -G dba,asmdba oracle
	```
	In the preceding command:
	- The `-u` option specifies the user ID. Using this command flag is optional, as you can allow the system to provide you with an automatically generated user ID number. However, you must make note of the `oracle` user ID number, as you require it later during preinstallation.
		- The `-g` option specifies the primary group, which must be the Oracle Inventory group--for example, `oinstall`
		- The `-G` option specifies the secondary groups, which must include the OSDBA group, the OSDBA for ASM group, and, if required, the OSOPER for ASM group. For example: `dba`, `asmdba`, or `dba`, `asmdba`, `asmoper`
2. Set the password of the `oracle` user:
	```
	# passwd oracle
	```

##### 2.5.5.2.9 Modifying an Existing Oracle Software Owner User

If the `oracle` user exists, but its primary group is not `oinstall`, or it is not a member of the appropriate OSDBA or OSDBA for ASM groups, then enter a command similar to the following to modify it. Specify the primary group using the `-g` option and any required secondary group using the `-G` option:

```
# /usr/sbin/usermod -g oinstall -G dba,asmdba oracle
```

Repeat this procedure on all of the other nodes in the cluster.

##### 2.5.5.2.10 Creating Identical Database Users and Groups on Other Cluster Nodes

Oracle software owner users and the Oracle Inventory, OSDBA, and OSOPER groups must exist and be identical on all cluster nodes. To create these identical users and groups, you must identify the user ID and group IDs assigned them on the node where you created them, and then create the user and groups with the same name and ID on the other cluster nodes.

Note:

You must complete the following procedures only if you are using local users and groups. If you are using users and groups defined in a directory service such as NIS, then they are already identical on each cluster node.

Identifying Existing User and Group IDs

To determine the user ID (`uid`) of the `grid` or `oracle` users, and the group IDs (`gid`) of the existing Oracle groups, follow these steps:

1. Enter a command similar to the following (in this case, to determine a user ID for the `oracle` user):
	```
	# id oracle
	```
	The output from this command is similar to the following:
	```
	uid=502(oracle) gid=501(oinstall) groups=502(dba),503(oper),506(asmdba)
	```
2. From the output, identify the user ID (`uid`) for the user and the group identities (`gid` s) for the groups to which it belongs. Ensure that these ID numbers are identical on each node of the cluster. The user's primary group is listed after `gid`. Secondary groups are listed after `groups`.

Creating Users and Groups on the Other Cluster Nodes

To create users and groups on the other cluster nodes, repeat the following procedure on each node:

1. Log in to the next cluster node as `root`.
2. Enter commands similar to the following to create the `oinstall`, `asmadmin`, and `asmdba` groups, and if required, the `asmoper`, `dba`, and `oper` groups. Use the `-g` option to specify the correct group ID for each group.
	```
	# /usr/sbin/groupadd -g 1000 oinstall
	# /usr/sbin/groupadd -g 1020 asmadmin
	# /usr/sbin/groupadd -g 1021 asmdba
	# /usr/sbin/groupadd -g 1022 asmoper
	# /usr/sbin/groupadd -g 1031 dba
	# /usr/sbin/groupadd -g 1032 oper
	```
	Note:
	If the group already exists, then use the `groupmod` command to modify it if necessary. If you cannot use the same group ID for a particular group on this node, then view the `/etc/group` file on all nodes to identify a group ID that is available on every node. You must then change the group ID on all nodes to the same group ID.
3. To create the `oracle` or Oracle Grid Infrastructure (`grid`) user, enter a command similar to the following (in this example, to create the `oracle` user):
	```
	# /usr/sbin/useradd -u 1101 -g oinstall -G asmdba,dba oracle
	```
	In the preceding command:
	- The `-u` option specifies the user ID, which must be the user ID that you identified in the previous subsection.
		- The `-g` option specifies the primary group, which must be the Oracle Inventory group, for example `oinstall`.
		- The `-G` option specifies the secondary groups, which can include the OSASM, OSDBA, OSDBA for ASM, and OSOPER or OSOPER for ASM groups. For example:
		- A grid installation owner: OSASM (`asmadmin`), whose members are granted the SYSASM privilege.
				- An Oracle Database installation owner without SYSASM privileges access: OSDBA (`dba`), OSDBA for ASM (`asmdba`), OSOPER for ASM (`asmoper`).
		Note:
		If the user already exists, then use the `usermod` command to modify it if necessary. If you cannot use the same user ID for the user on every node, then view the `/etc/passwd` file on all nodes to identify a user ID that is available on every node. You must then specify that ID for the user on all of the nodes.
4. Set the password of the user. For example:
	```
	# passwd oracle
	```
5. Complete user environment configuration tasks for each user as described in the section Configuring Grid Infrastructure Software Owner User Environments.

### 2.5.6 Example of Creating Standard Groups, Users, and Paths

The following is an example of how to create the Oracle Inventory group (`oinstall`), and a single group (`dba`) as the OSDBA, OSASM and OSDBA for Oracle ASM groups. In addition, it shows how to create the Oracle Grid Infrastructure software owner (`grid`), and one Oracle Database owner (`oracle`) with correct group memberships. This example also shows how to configure an Oracle base path compliant with OFA structure with correct permissions:

```
# groupadd -g 1000 oinstall
# groupadd -g 1031 dba
# useradd -u 1100 -g oinstall -G dba grid
# useradd -u 1101 -g oinstall -G dba oracle
# mkdir -p  /u01/app/11.2.0/grid
# mkdir -p /u01/app/grid
# chown -R grid:oinstall /u01
# mkdir /u01/app/oracle
# chown oracle:oinstall /u01/app/oracle
# chmod -R 775 /u01/
```

After running these commands, you have the following groups and users:

- An Oracle central inventory group, or oraInventory group (`oinstall`). Members who have the central inventory group as their primary group, are granted the OINSTALL permission to write to the `oraInventory` directory.
- A single system privileges group that is used as the OSASM, OSDBA, OSDBA for ASM, and OSOPER for ASM group (`dba`), whose members are granted the SYSASM and SYSDBA privilege to administer Oracle Clusterware, Oracle ASM, and Oracle Database, and are granted SYSASM and OSOPER for ASM access to the Oracle ASM storage.
- An Oracle grid installation for a cluster owner (`grid`), with the oraInventory group as its primary group, and with the OSASM group as the secondary group, with its Oracle base directory `/u01/app/grid`.
- An Oracle Database owner (`oracle`) with the oraInventory group as its primary group, and the OSDBA group as its secondary group, with its Oracle base directory `/u01/app/oracle`.
- `/u01/app` owned by `grid:oinstall` with 775 permissions before installation, and by root after the root.sh script is run during installation. This ownership and permissions enables OUI to create the Oracle Inventory directory, in the path `/u01/app/oraInventory`.
- `/u01` owned by `grid:oinstall` before installation, and by `root` after the `root.sh` script is run during installation.
- `/u01/app/11.2.0/grid` owned by `grid:oinstall` with 775 permissions. These permissions are required for installation, and are changed during the installation process.
- `/u01/app/grid` owned by grid:oinstall with 775 permissions before installation, and 755 permissions after installation.
- `/u01/app/oracle` owned by `oracle:oinstall` with 775 permissions.

### 2.5.7 Example of Creating Role-allocated Groups, Users, and Paths

The following is an example of how to create role-allocated groups and users that is compliant with an Optimal Flexible Architecture (OFA) deployment:

```
# groupadd -g 1000 oinstall
# groupadd -g 1020 asmadmin
# groupadd -g 1021 asmdba
# groupadd -g 1031 dba1
# groupadd -g 1041 dba2
# groupadd -g 1022 asmoper
# useradd -u 1100 -g oinstall -G asmadmin,asmdba grid
# useradd -u 1101 -g oinstall -G dba1,asmdba oracle1
# useradd -u 1102 -g oinstall -G dba2,asmdba oracle2
# mkdir -p  /u01/app/11.2.0/grid
# mkdir -p /u01/app/grid
# chown -R grid:oinstall /u01
# mkdir -p /u01/app/oracle1
# chown oracle1:oinstall /u01/app/oracle1
# mkdir -p /u01/app/oracle2
# chown oracle2:oinstall /u01/app/oracle2
# chmod -R 775 /u01
```

After running these commands, you have the following groups and users:

- An Oracle central inventory group, or oraInventory group (`oinstall`), whose members that have this group as their primary group are granted permissions to write to the `oraInventory` directory.
- A separate OSASM group (`asmadmin`), whose members are granted the SYSASM privilege to administer Oracle Clusterware and Oracle ASM.
- A separate OSDBA for ASM group (`asmdba`), whose members include `grid`, `oracle1` and `oracle2`, and who are granted access to Oracle ASM.
- A separate OSOPER for ASM group (`asmoper`), whose members are granted limited Oracle ASM administrator privileges, including the permissions to start and stop the Oracle ASM instance.
- An Oracle grid installation for a cluster owner (`grid`), with the oraInventory group as its primary group, and with the OSASM (`asmadmin`), OSDBA for ASM (asmdba) group as a secondary group.
- Two separate OSDBA groups for two different databases (`dba1` and `dba2`) to establish separate SYSDBA privileges for each database.
- Two Oracle Database software owners (`oracle1` and `oracle2`), to divide ownership of the Oracle database binaries, with the OraInventory group as their primary group, and the OSDBA group for their database (`dba1` or `dba2`) and the OSDBA for ASM group (`asmdba`) as their secondary groups.
- An OFA-compliant mount point `/u01` owned by `grid:oinstall` before installation.
- An Oracle base for the grid installation owner `/u01/app/grid` owned by `grid:oinstall` with 775 permissions, and changed during the installation process to 755 permissions.
- An Oracle base `/u01/app/oracle` 1 owned by `oracle1:oinstall` with 775 permissions.
- An Oracle base `/u01/app/oracle` 2 owned by `oracle2:oinstall` with 775 permissions.
- A Grid home `/u01/app/11.2.0/grid` owned by `grid:oinstall` with 775 (`drwxdrwxr-x`) permissions. These permissions are required for installation, and are changed during the installation process to `root:oinstall` with 755 permissions (`drwxr-xr-x`).
- `/u01/app/oraInventory`. This path remains owned by `grid:oinstall`, to enable other Oracle software owners to write to the central inventory.

## 2.6 Checking the Hardware Requirements

Review the following requirements:

- General Server Requirements
- Server Hardware Requirements
- Server Memory Requirements
- Checking Server Hardware and Memory Configuration

### 2.6.1 General Server Requirements

- Ensure that the server is started with run level 3 or run level 5.
- Ensure servers run the same operating system binary. Oracle Grid Infrastructure installations and Oracle Real Application Clusters (Oracle RAC) support servers with different hardware in the same cluster.

### 2.6.2 Server Hardware Requirements

Each system must meet the following minimum hardware requirements:

- At least 1024 x 768 display resolution, so that OUI displays correctly.
- 1 GB of space in the `/tmp` directory.
- 6.6 GB of space for the Oracle Grid Infrastructure for a Cluster home (Grid home) This includes Oracle Clusterware and Oracle ASM files and log files, ACFS log files, and includes the Cluster Health Monitor repository, if available for your platform.
- Upto 10 GB of additional space in the Oracle base directory of the Grid Infrastructure owner for diagnostic collections generated by Trace File Analyser and Collector.
- On Linux x86 platforms, if you intend to install Oracle Database, then allocate 4 GB of space for the Oracle base.
- For Linux x86\_64 platforms, if you intend to install Oracle Database, then allocate 4.6 GB of disk space for the Oracle base.

Note:

If you intend to install Oracle Databases or an Oracle RAC database on the cluster, be aware that the size of the `/dev/shm` mount area on each server must be greater than the system global areal (SGA) and the program global area (PGA) of the databases on the servers. Review expected SGA and PGA sizes with database administrators, to ensure that you do not have to increase `/dev/shm` after databases are installed on the cluster.

If you are installing Oracle Database, then you require additional space, either on a file system or in an Oracle Automatic Storage Management disk group, for the Fast Recovery Area if you choose to configure automated database backups.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

### 2.6.3 Server Memory Requirements

Ensure that your system meets the following requirements, depending on your system architecture

- 64-bit System and Linux on System z Memory Requirements
- Memory Requirements

Note:

On Linux, the Hugepages feature allocates non-swappable memory with large page tables using memory-mapped files. If you enable Hugepages, then you should deduct the memory allocated to HugePages from the available RAM before calculating swap space.

If you encounter an OUI error indicating inadequate swap space size, but your swap space meets the requirements listed here, then you can ignore that error.

#### 2.6.3.1 64-bit System and Linux on System z Memory Requirements

Each system must meet the following memory requirements:

- At least 2.5 GB of RAM for Oracle Grid Infrastructure for a Cluster installations, including installations where you plan to install Oracle RAC.
- Swap space equivalent to the multiple of the available RAM, as indicated in the following table:
	Table 2-1 Swap Space Required for 64-bit Linux and Linux on System z
	| Available RAM | Swap Space Required |
	| --- | --- |
	| Between 2.5 GB and 32 GB | Equal to the size of RAM |
	| More than 16 GB | 16 GB of RAM |

#### 2.6.3.2 Memory Requirements

Each system must meet the following memory requirements:

- At least 2.5 GB of RAM for Oracle Grid Infrastructure for a Cluster installations, including installations where you plan to install Oracle RAC.
- Swap space equivalent to the multiple of the available RAM, as indicated in the following table:
	Table 2-2 Swap Space Required for Linux
	| Available RAM | Swap Space Required |
	| --- | --- |
	| Between 2.5 GB and 16 GB | Equal to the size of RAM |
	| More than 16 GB | 16 GB |

### 2.6.4 Checking Server Hardware and Memory Configuration

To ensure that each system meets these requirements, follow these steps:

1. To determine the physical RAM size, enter the following command:
	```
	# grep MemTotal /proc/meminfo
	```
	If the size of the physical RAM installed in the system is less than the required size, then you must install more memory before continuing.
2. To determine the size of the configured swap space, enter the following command:
	```
	# grep SwapTotal /proc/meminfo
	```
	If necessary, refer to your operating system documentation for information about how to configure additional swap space.
3. To determine the amount of space available in the `/tmp` directory, enter the following command:
	```
	# df -k /tmp
	```
	This command displays disk space in 1 kilobyte blocks. On most systems, you can use the `df` command with the `-h` flag (`df -h`) to display output in "human-readable" format, such as "24G" and "10M." If there is less than 1 GB of disk space available in the `/tmp` directory (less than 1048576 1-k blocks), then complete one of the following steps:
	- Delete unnecessary files from the `/tmp` directory to make available the space required.
		- Extend the file system that contains the `/tmp` directory. If necessary, contact your system administrator for information about extending file systems.
4. To determine the amount of free RAM and disk swap space on the system, enter the following command:
	```
	# free
	```
	Note:
	- Oracle recommends that you take multiple values for the available RAM and swap space before finalizing a value. This is because the available RAM and swap space keep changing depending on the user interactions with the computer.
	- Contact your operating system vendor for swap space allocation guidance for your server. The vendor guidelines supersede the swap space requirements listed in this guide.
5. To determine if the system architecture can run the software, enter the following command:
	```
	# uname -m
	```
	Note:
	This command displays the processor type. If you intend to install on a 64-bit architecture, then the output should be `x86_64`.

## 2.7 Checking the Network Requirements

Review the following sections to check that you have the networking hardware and internet protocol (IP) addresses required for an Oracle Grid Infrastructure for a cluster installation:

- Network Hardware Requirements
- IP Address Requirements
- Broadcast Requirements for Networks Used by Oracle Grid Infrastructure
- Multicast Requirements for Networks Used by Oracle Grid Infrastructure
- DNS Configuration for Domain Delegation to Grid Naming Service
- Manual IP Address Configuration Example
- Grid Naming Service Configuration Example
- Network Interface Configuration Options
- Multiple Private Interconnects and Enterprise Linux
- Enabling the Name Service Cache Daemon

Note:

For the most up-to-date information about supported network protocols and hardware for Oracle RAC installations, refer to the Certify pages on the My Oracle Support Web site at the following URL:
```
https://support.oracle.com
```

### 2.7.1 Network Hardware Requirements

The following is a list of requirements for network configuration:

- Each node must have at least two network adapters or network interface cards (NICs): one for the public network interface, and one for the private network interface (the interconnect).
	With Redundant Interconnect Usage, you should identify multiple interfaces to use for the cluster private network, without the need of using bonding or other technologies. This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).
	When you define multiple interfaces, Oracle Clusterware creates from one to four highly available IP (HAIP) addresses. Oracle RAC and Oracle ASM instances use these interface addresses to ensure highly available, load-balanced interface communication between nodes. The installer enables Redundant Interconnect Usage to provide a high availability private network.
	By default, Oracle Grid Infrastructure software uses all of the HAIP addresses for private network communication, providing load-balancing across the set of interfaces you identify for the private network. If a private interconnect interface fails or become non-communicative, then Oracle Clusterware transparently moves the corresponding HAIP address to one of the remaining functional interfaces.
	Note:
	If you define more than four interfaces as private network interfaces, be aware that Oracle Clusterware activates only four of the interfaces at a time. However, if one of the four active interfaces fails, then Oracle Clusterware transitions the HAIP addresses configured to the failed interface to one of the reserve interfaces in the defined set of private interfaces.
	When you upgrade a node to Oracle Grid Infrastructure 11g release 2 (11.2.0.2) and later, the upgraded system uses your existing network classifications.
	To configure multiple public interfaces, use a third-party technology for your platform to aggregate the multiple public interfaces before you start installation, and then select the single interface name for the combined interfaces as the public interface. Oracle recommends that you do not identify multiple public interface names during Oracle Grid Infrastructure installation. Note that if you configure two network interfaces as public network interfaces in the cluster without using an aggregation technology, the failure of one public interface on a node does not result in automatic VIP failover to the other public interface.
	Oracle recommends that you use the Redundant Interconnect Usage feature to make use of multiple interfaces for the private network. However, you can also use third-party technologies to provide redundancy for the private network.
- If you install Oracle Clusterware using OUI, then the public interface names associated with the network adapters for each network must be the same on all nodes, and the private interface names associated with the network adaptors should be the same on all nodes. This restriction does not apply if you use cloning, either to create a new cluster, or to add nodes to an existing cluster.
	For example: With a two-node cluster, you cannot configure network adapters on `node1` with `eth0` as the public interface, but on `node2` have `eth1` as the public interface. Public interface names must be the same, so you must configure `eth0` as public on both nodes. You should configure the private interfaces on the same network adapters as well. If `eth1` is the private interface for `node1`, then `eth1` should be the private interface for `node2`.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/clonecluster.htm#CWADD03202) for information about how to add nodes using cloning
- For the public network, each network adapter must support TCP/IP.
- For the private network, the interface must support the user datagram protocol (UDP) using high-speed network adapters and switches that support TCP/IP (minimum requirement 1 Gigabit Ethernet).
	Note:
	UDP is the default interface protocol for Oracle RAC, and TCP is the interconnect protocol for Oracle Clusterware. You must use a switch for the interconnect. Oracle recommends that you use a dedicated switch.
	Oracle does not support token-rings or crossover cables for the interconnect.
- Each node's private interface for interconnects must be on the same subnet, and those subnets must connect to every node of the cluster. For example, if the private interfaces have a subnet mask of 255.255.255.0, then your private network is in the range 192.168.0.0--192.168.0.255, and your private addresses must be in the range of 192.168.0.\[0-255\]. If the private interfaces have a subnet mask of 255.255.0.0, then your private addresses can be in the range of 192.168.\[0-255\].\[0-255\].
	For clusters using Redundant Interconnect Usage, each private interface should be on a different subnet. However, each cluster member node must have an interface on each private interconnect subnet, and these subnets must connect to every node of the cluster. For example, you can have private networks on subnets 192.168.0 and 10.0.0, but each cluster member node must have an interface connected to the 192.168.0 and 10.0.0 subnets.
- For the private network, the endpoints of all designated interconnect interfaces must be completely reachable on the network. There should be no node that is not connected to every private network interface. You can test if an interconnect interface is reachable using `ping`.

### 2.7.2 IP Address Requirements

Before starting the installation, you must have at least two interfaces configured on each node: One for the private IP address and one for the public IP address.

You can configure IP addresses with one of the following options:

- Dynamic IP address assignment using Oracle Grid Naming Service (GNS). If you select this option, then network administrators assign static IP address for the physical host name and dynamically allocated IPs for the Oracle Clusterware managed VIP addresses. In this case, IP addresses for the VIPs are assigned by a DHCP and resolved using a multicast domain name server configured as part of Oracle Clusterware within the cluster. If you plan to use GNS, then you must have the following:
	- A DHCP service running on the public network for the cluster
		- Enough addresses on the DHCP to provide 1 IP address for each node's virtual IP, and 3 IP addresses for the cluster used by the Single Client Access Name (SCAN) for the cluster
- Static IP address assignment. If you select this option, then network administrators assign a fixed IP address for each physical host name in the cluster and for IPs for the Oracle Clusterware managed VIPs. In addition, domain name server (DNS) based static name resolution is used for each node. Selecting this option requires that you request network administration updates when you modify the cluster.

Note:

Oracle recommends that you use a static host name for all server node public hostnames.

Public IP addresses and virtual IP addresses must be in the same subnet.

Oracle only supports DHCP-assigned networks for the default network, not for any subsequent networks.

#### 2.7.2.1 IP Address Requirements with Grid Naming Service

If you enable Grid Naming Service (GNS), then name resolution requests to the cluster are delegated to the GNS, which is listening on the GNS virtual IP address. You define this address in the domain name server (DNS) domain before installation. The DNS must be configured to delegate resolution requests for cluster names (any names in the subdomain delegated to the cluster) to the GNS. When a request comes to the domain, GNS processes the requests and responds with the appropriate addresses for the name requested.

To use GNS, before installation the DNS administrator must establish DNS Lookup to direct DNS resolution of a subdomain to the cluster. If you enable GNS, then you must have a DHCP service on the public network that allows the cluster to dynamically allocate the virtual IP addresses as required by the cluster.

Note:

The following restrictions apply to vendor configurations on your system:
- If you have vendor clusterware installed, then you cannot choose to use GNS, because the vendor clusterware does not support it.
- You cannot use GNS with another multicast DNS. If you want to use GNS, then disable any third party mDNS daemons on your system.

#### 2.7.2.2 IP Address Requirements for Manual Configuration

If you do not enable GNS, then the public and virtual IP addresses for each node must be static IP addresses, configured before installation for each node, but not currently in use. Public and virtual IP addresses must be on the same subnet.

Oracle Clusterware manages private IP addresses in the private subnet on interfaces you identify as private during the installation interview.

The cluster must have the following addresses configured:

- A public IP address for each node, with the following characteristics:
	- Static IP address
		- Configured before installation for each node, and resolvable to that node before installation
		- On the same subnet as all other public IP addresses, VIP addresses, and SCAN addresses
- A virtual IP address for each node, with the following characteristics:
	- Static IP address
		- Configured before installation for each node, but not currently in use
		- On the same subnet as all other public IP addresses, VIP addresses, and SCAN addresses
- A Single Client Access Name (SCAN) for the cluster, with the following characteristics:
	- Three Static IP addresses configured on the domain name server (DNS) before installation so that the three IP addresses are associated with the name provided as the SCAN, and all three addresses are returned in random order by the DNS to the requestor
		- Configured before installation in the DNS to resolve to addresses that are not currently in use
		- Given a name that does not begin with a numeral
		- On the same subnet as all other public IP addresses, VIP addresses, and SCAN addresses
		- Conforms with the RFC 952 standard, which allows alphanumeric characters and hyphens ("-"), but does not allow underscores ("\_").
- A private IP address for each node, with the following characteristics:
	- Static IP address
		- Configured before installation, but on a separate, private network, with its own subnet, that is not resolvable except by other cluster member nodes

The SCAN is a name used to provide service access for clients to the cluster. Because the SCAN is associated with the cluster as a whole, rather than to a particular node, the SCAN makes it possible to add or remove nodes from the cluster without needing to reconfigure clients. It also adds location independence for the databases, so that client configuration does not have to depend on which nodes are running a particular database. Clients can continue to access the cluster in the same way as with previous releases, but Oracle recommends that clients accessing the cluster use the SCAN.

Note:

In a Typical installation, the SCAN you provide is also the name of the cluster, so the SCAN name must meet the requirements for a cluster name. In an Advanced installation, The SCAN and cluster name are entered in separate fields during installation, so cluster name requirements do not apply to the SCAN name.

You can use the nslookup command to confirm that the DNS is correctly associating the SCAN with the addresses. For example:

```
root@node1]$ nslookup mycluster-scan
Server:         dns.example.com
Address:        192.0.2.001
 
Name:   mycluster-scan.example.com
Address: 192.0.2.201
Name:   mycluster-scan.example.com
Address: 192.0.2.202
Name:   mycluster-scan.example.com
Address: 192.0.2.203
```

After installation, when a client sends a request to the cluster, the Oracle Clusterware SCAN listeners redirect client requests to servers in the cluster.

Note:

Oracle strongly recommends that you do not configure SCAN VIP addresses in the hosts file. Use DNS resolution for SCAN VIPs. If you use the hosts file to resolve SCANs, then you will only be able to resolve to one IP address and you will have only one SCAN address.

Configuring SCANs in a DNS or a hosts file is the only supported configuration. Configuring SCANs in a Network Information Service (NIS) is not supported.

See Also:

[Appendix D](concepts.md), ["Understanding Network Addresses"](concepts.md) for more information about network addresses

### 2.7.3 Broadcast Requirements for Networks Used by Oracle Grid Infrastructure

Broadcast communications (ARP and UDP) must work properly across all the public and private interfaces configured for use by Oracle Grid Infrastructure release 2 patchset 1 (11.2.0.2) and later releases.

The broadcast must work across any configured VLANs as used by the public or private interfaces.

### 2.7.4 Multicast Requirements for Networks Used by Oracle Grid Infrastructure

With Oracle Grid Infrastructure release 2 (11.2), on each cluster member node, the Oracle mDNS daemon uses multicasting on all interfaces to communicate with other nodes in the cluster.

With Oracle Grid Infrastructure release 2 patchset 1 (11.2.0.2) and later releases, multicasting is required on the private interconnect. For this reason, at a minimum, you must enable multicasting for the cluster:

- Across the broadcast domain as defined for the private interconnect
- On the IP address subnet ranges 224.0.0.0/24 and 230.0.1.0/24

You do not need to enable multicast communications across routers.

### 2.7.5 DNS Configuration for Domain Delegation to Grid Naming Service

If you plan to use GNS, then before Oracle Grid Infrastructure installation, you must configure your domain name server (DNS) to send to GNS name resolution requests for the subdomain GNS serves, which are the cluster member nodes. The following is an overview of what needs to be done for domain delegation. Your actual procedure may be different from this example.

Configure the DNS to send GNS name resolution requests using delegation:

1. In the DNS, create an entry for the GNS virtual IP address, where the address uses the form gns-server.CLUSTERNAME.DOMAINNAME. For example, where the cluster name is `mycluster`, and the domain name is `example.com`, and the IP address is 192.0.2.1, create an entry similar to the following:
	```
	mycluster-gns.example.com  A  192.0.2.1
	```
	The address you provide must be routable.
2. Set up forwarding of the GNS subdomain to the GNS virtual IP address, so that GNS resolves addresses to the GNS subdomain. To do this, create a BIND configuration entry similar to the following for the delegated domain, where `cluster01.example.com` is the subdomain you want to delegate:
	```
	cluster01.example.com  NS  mycluster-gns.example.com
	```
3. When using GNS, you must configure `resolve.conf` on the nodes in the cluster (or the file on your system that provides resolution information) to contain name server entries that are resolvable to corporate DNS servers. The total timeout period configured—a combination of options attempts (retries) and options timeout (exponential backoff)—should be less than 30 seconds. For example, where xxx.xxx.xxx.42 and xxx.xxx.xxx.15 are valid name server addresses in your network, provide an entry similar to the following in `/etc/resolv.conf`:
	```
	options attempts: 2
	options timeout: 1
	search cluster01.example.com example.com
	nameserver xxx.xxx.xxx.42
	nameserver xxx.xxx.xxx.15
	```
	`/etc/nsswitch.conf` controls name service lookup order. In some system configurations, the Network Information System (NIS) can cause problems with Oracle SCAN address resolution. Oracle recommends that you place the `nis` entry at the end of the search list. For example:
	```
	/etc/nsswitch.conf
	     hosts:    files   dns   nis
	```
	Note:
	Be aware that use of NIS is a frequent source of problems when doing cable pull tests, as host name and username resolution can fail.

### 2.7.6 Grid Naming Service Configuration Example

If you use GNS, then you need to specify a static IP address for the GNS VIP address, and delegate a subdomain to be delegated to that static GNS IP address.

As nodes are added to the cluster, your organization's DHCP server can provide addresses for these nodes dynamically. These addresses are then registered automatically in GNS, and GNS provides resolution within the subdomain to cluster node addresses registered with GNS.

Because allocation and configuration of addresses is performed automatically with GNS, no further configuration is required. Oracle Clusterware provides dynamic network configuration as nodes are added to or removed from the cluster. The following example is provided only for information.

With a two node cluster where you have defined the GNS VIP, after installation you might have a configuration similar to the following for a two-node cluster, where the cluster name is `mycluster`, the GNS parent domain is `example.com`, the subdomain is `grid.example.com`, 192.0.2 in the IP addresses represent the cluster public IP address network, and 192.168.0 represents the private IP address subnet:

Table 2-3 Grid Naming Service Example Network

| Identity | Home Node | Host Node | Given Name | Type | Address | Address Assigned By | Resolved By |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GNS VIP | None | Selected by Oracle Clusterware | `mycluster-gns`.example.com | virtual | 192.0.2.1 | Fixed by net administrator | DNS |
| Node 1 Public | Node 1 | `node1` | `node1` <sup>Foot 1</sup> | Public | 192.0.2.101 | Fixed | GNS |
| Node 1 VIP | Node 1 | Selected by Oracle Clusterware | `node1-vip` | Virtual | 192.0.2.104 | DHCP | GNS |
| Node 1 Private | Node 1 | `node1` | `node1-priv` | Private | 192.168.0.1 | Fixed or DHCP | GNS |
| Node 2 Public | Node 2 | `node2` | `node2` <sup>Footref 1</sup> | Public | 192.0.2.102 | Fixed | GNS |
| Node 2 VIP | Node 2 | Selected by Oracle Clusterware | `node2-vip` | Virtual | 192.0.2.105 | DHCP | GNS |
| Node 2 Private | Node 2 | `node2` | `node2-priv` | Private | 192.168.0.2 | Fixed or DHCP | GNS |
| SCAN VIP 1 | none | Selected by Oracle Clusterware | `mycluster-scan.cluster01.example.com` | virtual | 192.0.2.201 | DHCP | GNS |
| SCAN VIP 2 | none | Selected by Oracle Clusterware | `mycluster-scan.cluster01.example.com` | virtual | 192.0.2.202 | DHCP | GNS |
| SCAN VIP 3 | none | Selected by Oracle Clusterware | `mycluster-scan.cluster01.example.com` | virtual | 192.0.2.203 | DHCP | GNS |

<sup>Footnote 1</sup> Node host names may resolve to multiple addresses, including VIP addresses currently running on that host.

### 2.7.7 Manual IP Address Configuration Example

If you choose not to use GNS, then before installation you must configure public, virtual, and private IP addresses. Also, check that the default gateway can be accessed by a `ping` command. To find the default gateway, use the `route` command, as described in your operating system's help utility.

For example, with a two node cluster where each node has one public and one private interface, and you have defined a SCAN domain address to resolve on your DNS to one of three IP addresses, you might have the configuration shown in the following table for your network interfaces:

Table 2-4 Manual Network Configuration Example

| Identity | Home Node | Host Node | Given Name | Type | Address | Address Assigned By | Resolved By |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Node 1 Public | Node 1 | `node1` | `node1` <sup>Foot 1</sup> | Public | 192.0.2.101 | Fixed | DNS |
| Node 1 VIP | Node 1 | Selected by Oracle Clusterware | `node1-vip` | Virtual | 192.0.2.104 | Fixed | DNS and hosts file |
| Node 1 Private | Node 1 | `node1` | `node1-priv` | Private | 192.168.0.1 | Fixed | DNS and hosts file, or none |
| Node 2 Public | Node 2 | `node2` | `node2` <sup>Footref 1</sup> | Public | 192.0.2.102 | Fixed | DNS |
| Node 2 VIP | Node 2 | Selected by Oracle Clusterware | `node2-vip` | Virtual | 192.0.2.105 | Fixed | DNS and hosts file |
| Node 2 Private | Node 2 | `node2` | `node2-priv` | Private | 192.168.0.2 | Fixed | DNS and hosts file, or none |
| SCAN VIP 1 | none | Selected by Oracle Clusterware | mycluster-scan | virtual | 192.0.2.201 | Fixed | DNS |
| SCAN VIP 2 | none | Selected by Oracle Clusterware | mycluster-scan | virtual | 192.0.2.202 | Fixed | DNS |
| SCAN VIP 3 | none | Selected by Oracle Clusterware | mycluster-scan | virtual | 192.0.2.203 | Fixed | DNS |

<sup>Footnote 1</sup> Node host names may resolve to multiple addresses.

You do not need to provide a private name for the interconnect. If you want name resolution for the interconnect, then you can configure private IP names in the hosts file or the DNS. However, Oracle Clusterware assigns interconnect addresses on the interface defined during installation as the private interface (`eth1`, for example), and to the subnet used for the private subnet.

The addresses to which the SCAN resolves are assigned by Oracle Clusterware, so they are not fixed to a particular node. To enable VIP failover, the configuration shown in the preceding table defines the SCAN addresses and the public and VIP addresses of both nodes on the same subnet, 192.0.2.

Note:

All host names must conform to the RFC 952 standard, which permits alphanumeric characters. Host names using underscores ("\_") are not allowed.

### 2.7.8 Network Interface Configuration Options

The precise configuration you choose for your network depends on the size and use of the cluster you want to configure, and the level of availability you require.

If certified Network-attached Storage (NAS) is used for Oracle RAC and this storage is connected through Ethernet-based networks, then you must have a third network interface for NAS I/O. Failing to provide three separate interfaces in this case can cause performance and stability problems under load.

### 2.7.9 Multiple Private Interconnects and Enterprise Linux

In kernel 2.6.31 and above, which also includes Oracle Unbreakable Enterprise Kernel 2.6.32, a bug has been fixed in the Reverse Path Filtering. As a consequence of this correction, Oracle RAC systems that use multiple NICs for the private interconnect now require specific settings for the `rp_filter` parameter. This requirement also applies to all Exadata systems that are running Linux kernel 2.6.32 and above. Without these `rp_filter` parameter settings systems, interconnect packets can be blocked or discarded.

The `rp_filter` values set the Reverse Path filter to no filtering (`0`), to strict filtering (`1`), or to loose filtering (`2`). Set the `rp_filter` value for the private interconnects to either `0` or `2`. Setting the private interconnect NIC to `1` can cause connection issues on the private interconnect. It is not considered unsafe to disable or relax this filtering, because the private interconnect should be on a private and isolated network.

For example, where `eth1` and `eth2` are the private interconnect NICs, and `eth0` is the public network NIC, set the `rp_filter` of the private address to `2` (loose filtering), the public address to `1` (strict filtering), using the following entries in `/etc/sysctl.conf`:

```
net.ipv4.conf.eth2.rp_filter = 2
net.ipv4.conf.eth1.rp_filter = 2
net.ipv4.conf.eth0.rp_filter = 1
```

Enterprise Linux 5.6 (Enterprise Linux 5 Update 6) includes a fix using `initscripts-8.45.33-1.0.4.el5.i386.rpm`, which sets the kernel parameter `net.ipv4.conf.default.rp_filter` to `2` (relaxed mode). For that reason, after you apply Unbreakable Linux Kernel on top of Enterprise Linux 5.6, you may not need to make manual changes, because the `rp_filter` value of all NICs is set to `2`. If you require more strict reverse path filtering on the public network, then set the public NIC `rp_filter` to `1`.

See Also:

My Oracle Support note 1286796.1 rp\_filter for multiple private interconnects and Linux Kernel 2.6.32+, which is available at the following URL:
```
https://support.oracle.com
```

### 2.7.10 Enabling the Name Service Cache Daemon

To allow Oracle Clusterware to better tolerate network failures with NAS devices or NFS mounts, enable the Name Service Cache Daemon (`nscd`).

To check to see if nscd is set to load when the system is restarted, enter the command `chkconfig --list nscd`. For example:

```
# chkconfig --list nscd
nscd                      0:off  1:off  2:off  3:on   4:off  5:off   6:off
```

In the preceding example, `nscd` is turned on for run level 3, and turned off for run level 5. The `nscd` should be turned on for both run level 3 and run level 5.

To change the configuration to ensure that `nscd` is on for both run level 3 and run level 5, enter one of the following command as `root`:

On Red Hat and Oracle Linux 4 and 5:

```
# chkconfig --level 35 nscd on
```

On SUSE SLES10 and11:

```
# chkconfig --level 35 nscd on
```

To start up `nscd` in the current session, enter the command as `root`:

```
# service nscd start
```

To restart `nscd` with the new setting, enter the following command as `root`:

```
# service nscd restart
```

## 2.8 Identifying Software Requirements

Depending on the products that you intend to install, verify that the following operating system software is installed on the system. To check these requirements refer to the section "Checking the Software Requirements", following this section.

Requirements listed here are current as of the initial release date. To obtain the most current information about kernel requirements, refer to the online version on the Oracle Technology Network (OTN) at the following URL:

```
http://www.oracle.com/technetwork/indexes/documentation/index.html
```

OUI performs checks your system to verify that it meets the listed operating system package requirements. To ensure that these checks complete successfully, verify the requirements before you start OUI.

Oracle recommends that you install your Linux operating system with the default software packages (RPMs), unless you specifically intend to perform a minimal installation, and follow the directions for performing such an installation to ensure that you have all required packages for Oracle software.

Oracle recommends that you do not customize RPMs during a default operating system installation. A default installation includes most required packages, and will help you to limit manual checks of package dependencies

Note:

Oracle does not support running different operating system versions on cluster members, unless an operating system is being upgraded. You cannot run different operating system version binaries on members of the same cluster, even if each operating system is supported.

Starting with Oracle Database 11g Release 2 (11.2), the Security Enhanced Linux (SELinux) feature is supported for Oracle Linux 4, Red Hat Enterprise Linux 4, Oracle Linux 5, Oracle Linux 6, Red Hat Enterprise Linux 5, and Red Hat Enterprise Linux 6.

The following is the list of supported Linux versions and requirements at the time of release:

- Software Requirements List for x86 Linux Platforms
- Software Requirements List for x86-64 Linux Platforms
- Software Requirements list for IBM: Linux on System z

### 2.8.1 Software Requirements List for x86 Linux Platforms

For installations of Oracle Grid Infrastructure, ensure that you have the kernel versions and packages listed in Table 2-5 and Table 2-6.

Ensure that OpenSSH is installed on your servers. OpenSSH is the required SSH software.

If you intend to install Oracle Database or Oracle RAC in addition to Oracle Grid Infrastructure, then check Table 2-7 to determine if you must install additional packages for the features you plan to use.

Note:

For Asianux Server, Oracle Linux, and Red Hat Enterprise Linux, system requirements are identical by kernel version. Specifically:

Oracle Linux 4 and Red Hat Enterprise Linux 4 requirements are the same.

Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 requirements are the same.

Asianux Server 4, Red Hat Enterprise Linux 6 requirements are the same.

Table 2-5 Linux x86 Operating System Kernel Requirements

| Linux Distribution | Requirements |
| --- | --- |
| Asianux Distributions | - Asianux Server 3, Service Pack 2 (SP2), kernel 2.6.18 or later - Asianux Server 4, Service Pack 3 (SP3), kernel 2.6.32-71 or later |
| Oracle Linux Distributions | - Oracle Linux 4, Update 7, kernel 2.6.9 or later - Oracle Linux 5, Update 2, kernel 2.6.18 or later - Oracle Linux 6, kernel 2.6.32-100 or later |
| Red Hat Enterprise Linux Distributions | - Red Hat Enterprise Linux 4, Update 7, kernel 2.6.9 or later - Red Hat Enterprise Linux 5, Update 2, kernel 2.6.18, and later - Red Hat Enterprise Linux 6, kernel 2.6.32-71 or later |
| SUSE Linux Enterprise Distributions | - SUSE Linux Enterprise Server 10, kernel 2.6.16.21 or later - SUSE Linux Enterprise Server 11, kernel 2.6.27.19 or later |

Table 2-6 Linux x86 Grid Infrastructure and Oracle RAC Package Requirements

| Item | Requirements |
| --- | --- |
| Oracle Linux 4, and Red Hat Enterprise Linux 4 | The following packages (or later versions) must be installed:  ``` binutils-2.15.92.0.2 compat-libstdc++-33-3.2.3 elfutils-libelf-0.97 elfutils-libelf-devel-0.97 gcc-3.4.6 gcc-c++-3.4.6 glibc-2.3.4-2.41 glibc-common-2.3.4 glibc-devel-2.3.4 glibc-headers-2.3.4 libaio-devel-0.3.105 libaio-0.3.105 libgcc-3.4.6 libstdc++-3.4.6 libstdc++-devel-3.4.6 make-3.80 numactl-0.6.4.i386 pdksh-5.2.14 sysstat-5.0.5 unixODBC-2.2.11 unixODBC-devel-2.2.11 ``` |
| Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 | The following packages (or later versions) must be installed:  ``` binutils-2.17.50.0.6 compat-libstdc++-33-3.2.3 elfutils-libelf-0.125 elfutils-libelf-devel-0.125 elfutils-libelf-devel-static-0.125 gcc-4.1.2 gcc-c++-4.1.2 glibc-2.5-24 glibc-common-2.5 glibc-devel-2.5 glibc-headers-2.5 kernel-headers-2.6.18 ksh-20060214 libaio-0.3.106 libaio-devel-0.3.106  libgcc-4.1.2 libgomp-4.1.2 libstdc++-4.1.2  libstdc++-devel-4.1.2 make-3.81 sysstat-7.0.2 unixODBC-2.2.11 unixODBC-devel-2.2.11 ``` |
| Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4 | The following packages (or later versions) must be installed:  ``` binutils-2.20.51.0.2-5.11.el6.i686 compat-libcap1-1.10-1.i686 compat-libstdc++-33-3.2.3-69.el6.i686 gcc-4.4.4-13.el6.i686 gcc-c++-4.4.4-13.el6.i686 glibc-2.12-1.7.el6.i686 glibc-devel-2.12-1.7.el6.i686 ksh libgcc-4.4.4-13.el6.i686 libstdc++-4.4.4-13.el6.i686 libstdc++-devel-4.4.4-13.el6.i686 libaio-0.3.107-10.el6.i686 libaio-devel-0.3.107-10.el6.i686 make-3.81-19.el6.i686 sysstat-9.0.4-11.el6.i686 ``` |
| SUSE Linux Enterprise Server 10 Packages | The following packages (or later versions) must be installed:  ``` binutils-2.16.91.0.5 compat-libstdc++-5.0.7 gcc-4.1.2 gcc-c++-4.1.2 glibc-2.4-31.63 glibc-devel-2.4.31.63 ksh-93r-12.9 libaio-0.3.104 libaio-devel-0.3.104 libelf-0.8.5 libgcc-4.1.2 libstdc++-4.1.2 libstdc++-devel-4.1.2 make-3.80 sysstat-8.0.4 ``` |
| SUSE Linux Enterprise Server 11 packages | The following packages (or later versions) must be installed:  ``` binutils-2.19 gcc-4.3 gcc-c++-4.3 glibc-2.9 glibc-devel-2.9 ksh-93t libcap1-1.10-6.10 libstdc++33-3.3.3 libstdc++43-4.3.3_20081022 libstdc++43-devel-4.3.3_20081022 libaio-0.3.104 libaio-devel-0.3.104 libgcc43-4.3.3_20081022 libstdc++-devel-4.3 make-3.81 sysstat-8.1.5 ``` |

Note:

The `numa` package link for Linux x86 is `/usr/lib`.

Table 2-7 Linux x86 Oracle Database Features Package Requirements

| Item | Requirement |
| --- | --- |
| LDAP package | If you did not perform a default Linux installation, you intend to use LDAP, and you want to use the scripts `odisrvreg`, `oidca`, or `schemasync`, then install the Korn shell RPM for your Linux distribution. |
| Pluggable Authentication Modules for Linux (Linux PAM) | Install the latest Linux PAM (Pluggable Authentication Modules for Linux) library for your Linux distribution. PAM provides greater flexibility for system administrators to choose how applications authenticate users. On Linux, external scheduler jobs require PAM. |
| Pro\*C/C++, Oracle Call Interface, Oracle C++ Call Interface, Oracle XML Developer's Kit (XDK) | Intel C/C++ Compiler 10.1 or later and the version of GNU C and C++ compilers listed previously for the distribution are supported for use with these products.  Note: Intel C/C++ Compiler v10.1 can be used only with the standard template libraries of the gcc versions mentioned in the Package Requirements to build OCCI applications.  Oracle XML Developer's Kit is supported with the same compilers as OCCI. |
| Oracle ODBC Drivers | If you intend to use Open Database Connectivity (ODBC), then you should install the most recent ODBC Driver Manager for Linux.  You should obtain the most current ODBC driver from your operating system vendor. You can read about ODBC at the following URL:  ``` http://www.unixodbc.org ```  The ODBC RPMs are only needed if you plan on using ODBC. If you do not plan to use ODBC, then you do not need to install the ODBC RPMs for Oracle Clusterware, Oracle ASM, or Oracle RAC.  To use ODBC, you must also install the following additional 32-bit ODBC RPMs, depending on your operating system:  Oracle Linux 4, and Red Hat Enterprise Linux 4:  ``` unixODBC-2.2.11 (32 bit) or later unixODBC-devel-2.2.11 (32 bit) or later ```  Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5:  ``` unixODBC-2.2.11 (32 bit) or laterunixODBC-devel-2.2.11 (32 bit) or later ```  Oracle Linux 6 and Red Hat Enterprise Linux 6, and Asianux Server 4:  ``` unixODBC-2.2.14-11.el6.i686 or laterunixODBC-devel-2.2.14-11.el6.i686 or later ```  SUSE Linux Enterprise Server 10:  ``` unixODBC-32bit-2.2.11 (32 bit) or later unixODBC-devel-32bit-2.2.11 (32 bit) or later ```  SUSE Linux Enterprise Server 11:  ``` unixODBC-32bit-2.2.12 (32-bit) or later unixODBC-devel-32bit-2.2.12 (32 bit) or later ``` |
| Oracle JDBC/OCI Drivers | Use JDK 6 (Java SE Development Kit 1.6.0\_21) or JDK 5 (1.5.0\_24) with the JNDI extension with the Oracle Java Database Connectivity and Oracle Call Interface drivers. JDK 1.5 is installed with this release. |
| Oracle Real Application Clusters | For a cluster file system, use one of the following options:  OCFS2  - Version 1.2.9 or later  If you plan to install an Oracle RAC home on a shared OCFS2 location, then you must upgrade OCFS2 to at least version 1.4.1, which supports shared writable mmaps.  To check your OCFS version, enter the following command:  ``` modinfo ocfs2 ```  To check the version of OCFS2 tools and OCFS2 console, enter the following command:  ``` rpm -qa\| grep ocfs2 ```  Ensure that `ocfs2console` and `ocfs2-tools` are at least version 1.2.9  For information about OCFS2, refer to the following Web site:  ``` http://oss.oracle.com/projects/ocfs2/ ```  For OCFS2 certification status, refer to the Certify page on My Oracle Support. |

### 2.8.2 Software Requirements List for x86-64 Linux Platforms

For installations only of Oracle Grid Infrastructure, ensure that you have the kernel versions and packages listed in Table 2-8 and Table 2-9.

Ensure that OpenSSH is installed on your servers. OpenSSH is the required SSH software.

If you intend to install Oracle Database or Oracle RAC in addition to Oracle Grid Infrastructure, then check Table 2-10 to determine if you must install additional packages for the features you plan to use.

Note:

For Asianux Server, Oracle Linux, and Red Hat Enterprise Linux, system requirements for 2.6 kernels generally are identical by kernel version. Specifically:

Oracle Linux 4, and Red Hat Enterprise Linux 4 requirements are the same.

Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 Update 2 requirements are the same.

Oracle Linux 6 includes the Unbreakable Enterprise Kernel.

Oracle Unbreakable Enterprise Kernel for Linux 5 Update 5 (2.6.32), and Oracle Linux 6, available for x86-64 systems, contain several additional features and performance enhancements not available either with Oracle Linux or with other supported Linux distributions. This kernel can be installed on either Oracle Linux or Red Hat Enterprise Linux distributions. Before installing the Unbreakable Enterprise Kernel, you must have Oracle Linux 5 Update 5 or RHEL5 Update 5 installed on an x86-64 server.

For Oracle Linux 6 the Oracle Validated RPM has been replaced by the Oracle Preinstallation RPM. See Section 2.1.1, "Completing a Minimal Linux Installation" for more information.

Starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.2), all the 32-bit packages listed in the following table, except for gcc-32bit-4.3, are no longer required for installation. Only the 64-bit packages are required. However, for releases before Oracle 11g Release 2 (11.2.0.1), both the 32-bit and 64-bit packages listed in the following table are required.

Table 2-8 Linux x86-64 Operating System Kernel Requirements

| Linux Distribution | Requirements |
| --- | --- |
| Asianux Distributions | - Asianux Server 3, Service Pack 2 (SP2), kernel 2.6.18 or later - Asianux Server 4, Service Pack 3 (SP3), kernel 2.6.32-71.el6.x86\_64 or later |
| Oracle Linux Distributions | - Oracle Linux 4 Update 7, kernel 2.6.9 or later - Oracle Linux 5 Update 2 (with Red Hat Compatible Kernel), kernel 2.6.18, and later - Oracle Linux 5 Update 5 (with Red Hat Compatible Kernel), kernel 2.6.18 or later - Oracle Linux 5 Update 5 (with Oracle Unbreakable Enterprise Kernel for Linux), kernel 2.6.32-100.0.19 or later - Oracle Linux 6 (with Red Hat Compatible Kernel) 2.6.32-71.el6.x86\_64 or later - Oracle Linux 6, kernel 2.6.32-100.28.5.el6.x86\_64 or later - Oracle Linux 7, kernel 3.8.13-33.el7uek.x86\_64 or later - On Oracle Linux 7 with Red Hat Compatible Kernel, 3.10.0-54.0.1.el7.x86\_64 or later |
| Red Hat Enterprise Linux Distributions | - Red Hat Enterprise Linux 4, Update 7, kernel 2.6.9 or later - Red Hat Enterprise Linux 5, Update 5, 2.6.18 or later - Red Hat Enterprise Linux 5 Update 5 with Oracle Unbreakable Enterprise Kernel for Linux 2.6.32 or later - Red Hat Enterprise Linux 6, 2.6.32-71.el6.x86\_64 or later - Red Hat Enterprise Linux 6 with Oracle Unbreakable Enterprise Kernel for Linux, kernel 2.6.32-100.28.5.el6.x86\_64 or later - Red Hat Enterprise Linux 7, kernel 3.10.0-54.0.1.el7.x86\_64 or later - Red Hat Enterprise Linux 7 with Oracle Unbreakable Enterprise Kernel, 3.8.13-33.el7uek.x86\_64 or later |
| SUSE Enterprise Linux Distributions | - SUSE Linux Enterprise Server 10, Service Pack 2 (SP2), kernel 2.6.16.21 or later - SUSE Linux Enterprise Server 11, kernel 2.6.27.19 or later - SUSE Linux Enterprise Server 12, kernel 3.12.49-11 or later |
| NeoKylin Linux Advanced Server | - NeoKylin Linux Advanced Server 6, 2.6.32-431.el6.x86\_64 or later - NeoKylin Linux Advanced Server 7, 3.10.0-327.el7.x86\_64 or later |

Table 2-9 Linux x86-64 Oracle Grid Infrastructure and Oracle RAC Package Requirements

| Item | Requirements |
| --- | --- |
| Oracle Linux 7 and Red Hat Enterprise Linux 7 | The following packages (or later versions) must be installed:  ``` binutils-2.23.52.0.1-12.el7.x86_64  compat-libcap1-1.10-3.el7.x86_64  gcc-4.8.2-3.el7.x86_64  gcc-c++-4.8.2-3.el7.x86_64  glibc-2.17-36.el7.i686  glibc-2.17-36.el7.x86_64  glibc-devel-2.17-36.el7.i686  glibc-devel-2.17-36.el7.x86_64  ksh libaio-0.3.109-9.el7.i686  libaio-0.3.109-9.el7.x86_64  libaio-devel-0.3.109-9.el7.i686  libaio-devel-0.3.109-9.el7.x86_64  libgcc-4.8.2-3.el7.i686  libgcc-4.8.2-3.el7.x86_64  libstdc++-4.8.2-3.el7.i686  libstdc++-4.8.2-3.el7.x86_64  libstdc++-devel-4.8.2-3.el7.i686  libstdc++-devel-4.8.2-3.el7.x86_64  libXi-1.7.2-1.el7.i686  libXi-1.7.2-1.el7.x86_64  libXtst-1.2.2-1.el7.i686  libXtst-1.2.2-1.el7.x86_64  make-3.82-19.el7.x86_64  sysstat-10.1.5-1.el7.x86_64 ``` |
| Oracle Linux 6 (2.6.32-100.28.5.el6.x86\_64 or later) | Subscribe to the Oracle Linux 6 channel on the Unbreakable Linux Network, and then install the Oracle Preinstallation RPM. This installs the Oracle Unbreakable Enterprise Kernel for Linux, and all required kernel packages for Oracle Grid Infrastructure and Oracle Database installations. |
| Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4 | The following packages (or later versions) must be installed:  ``` binutils-2.20.51.0.2-5.11.el6 (x86_64) compat-libcap1-1.10-1 (x86_64) compat-libstdc++-33-3.2.3-69.el6 (x86_64) compat-libstdc++-33-3.2.3-69.el6.i686 gcc-4.4.4-13.el6 (x86_64) gcc-c++-4.4.4-13.el6 (x86_64) glibc-2.12-1.7.el6 (i686) glibc-2.12-1.7.el6 (x86_64) glibc-devel-2.12-1.7.el6 (x86_64) glibc-devel-2.12-1.7.el6.i686 ksh libgcc-4.4.4-13.el6 (i686) libgcc-4.4.4-13.el6 (x86_64) libstdc++-4.4.4-13.el6 (x86_64) libstdc++-4.4.4-13.el6.i686 libstdc++-devel-4.4.4-13.el6 (x86_64) libstdc++-devel-4.4.4-13.el6.i686 libaio-0.3.107-10.el6 (x86_64) libaio-0.3.107-10.el6.i686 libaio-devel-0.3.107-10.el6 (x86_64) libaio-devel-0.3.107-10.el6.i686 make-3.81-19.el6 sysstat-9.0.4-11.el6 (x86_64) ``` |
| Oracle Linux 5 Update 5 (2.6.32-100.0.19 or later) | Subscribe to the Oracle Linux 5 channel on the Unbreakable Linux Network, and then install the Oracle Preinstallation RPM (or Oracle Validated RPM). This installs the Oracle Enterprise Kernel for Linux, and all required kernel packages for Oracle Grid Infrastructure and Oracle Database installations. |
| Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 | The following packages (or later versions) must be installed:  ``` binutils-2.17.50.0.6 compat-libstdc++-33-3.2.3 compat-libstdc++-33-3.2.3 (32 bit) elfutils-libelf-0.125 elfutils-libelf-devel-0.125 gcc-4.1.2 gcc-c++-4.1.2 glibc-2.5-24 glibc-2.5-24 (32 bit) glibc-common-2.5 glibc-devel-2.5 glibc-devel-2.5 (32 bit) glibc-headers-2.5 ksh-20060214 libaio-0.3.106 libaio-0.3.106 (32 bit) libaio-devel-0.3.106 libaio-devel-0.3.106 (32 bit) libgcc-4.1.2 libgcc-4.1.2 (32 bit) libstdc++-4.1.2 libstdc++-4.1.2 (32 bit) libstdc++-devel-4.1.2 make-3.81 sysstat-7.0.2 unixODBC-2.2.11 unixODBC-2.2.11 (32 bit) unixODBC-devel-2.2.11 unixODBC-devel-2.2.11 (32 bit) coreutils-5.97-23.el5_4.1 or later ``` |
| Oracle Linux 4, and Red Hat Enterprise Linux 4 | The following packages (or later versions) must be installed:  ``` binutils-2.15.92.0.2 compat-libstdc++-33-3.2.3 compat-libstdc++-33-3.2.3 (32 bit) elfutils-libelf-0.97 elfutils-libelf-devel-0.97 expat-1.95.7 gcc-3.4.6 gcc-c++-3.4.6 glibc-2.3.4-2.41 glibc-2.3.4-2.41 (32 bit) glibc-common-2.3.4 glibc-devel-2.3.4 glibc-headers-2.3.4 libaio-0.3.105 libaio-0.3.105 (32 bit) libaio-devel-0.3.105 libaio-devel-0.3.105 (32 bit) libgcc-3.4.6 libgcc-3.4.6 (32-bit) libstdc++-3.4.6 libstdc++-3.4.6 (32 bit) libstdc++-devel 3.4.6 make-3.80 numactl-0.6.4.x86_64 pdksh-5.2.14 sysstat-5.0.5 unixODBC-2.2.11 unixODBC-2.2.11 (32 bit) unixODBC-devel-2.2.11 unixODBC-devel-2.2.11 (32 bit) ``` |
| SUSE Linux Enterprise Server 12 | The following packages (or later versions) must be installed:  ``` binutils-2.25.0-13.1 gcc-4.8-6.189 gcc48-4.8.5-24.1 glibc-2.19-31.9 glibc-32bit-2.19-31.9 glibc-devel-2.19-31.9.x86_64 glibc-devel-32bit-2.19-31.9.x86_64 libaio1-0.3.109-17.15 libaio-devel-0.3.109-17.15 libcap1-1.10-59.61 libstdc++48-devel-4.8.5-24.1.x86_64 libstdc++48-devel-32bit-4.8.5-24.1.x86_64 libstdc++6-5.2.1+r226025-4.1.x86_64 libstdc++6-32bit-5.2.1+r226025-4.1.x86_64 libstdc++-devel-4.8-6.189.x86_64 libstdc++-devel-32bit-4.8-6.189.x86_64 libgcc_s1-5.2.1+r226025-4.1.x86_64 libgcc_s1-32bit-5.2.1+r226025-4.1.x86_64 mksh-50-2.13 make-4.0-4.1.x86_64 sysstat-10.2.1-3.1.x86_64 xorg-x11-driver-video-7.6_1-14.30.x86_64 xorg-x11-server-7.6_1.15.2-36.21.x86_64 xorg-x11-essentials-7.6_1-14.17.noarch xorg-x11-Xvnc-1.4.3-7.2.x86_64 xorg-x11-fonts-core-7.6-29.45.noarch xorg-x11-7.6_1-14.17.noarch xorg-x11-server-extra-7.6_1.15.2-36.21.x86_64 xorg-x11-libs-7.6-45.14.noarch xorg-x11-fonts-7.6-29.45.noarch ```  Note: You must download and install patch 18370031. For more information about how to download and install this patch see:  `https://support.oracle.com` |
| SUSE Linux Enterprise Server 11 | The following packages (or later versions) must be installed:  ``` binutils-2.19 gcc-4.3 gcc-32bit-4.3 gcc-c++-4.3 glibc-2.9 glibc-32bit-2.9 glibc-devel-2.9 glibc-devel-32bit-2.9 ksh-93t libaio-0.3.104 libaio-32bit-0.3.104 libaio-devel-0.3.104 libaio-devel-32bit-0.3.104 libstdc++33-3.3.3 libstdc++33-32bit-3.3.3 libstdc++43-4.3.3_20081022 libstdc++43-32bit-4.3.3_20081022 libstdc++43-devel-4.3.3_20081022 libstdc++43-devel-32bit-4.3.3_20081022 libgcc43-4.3.3_20081022 libstdc++-devel-4.3 make-3.81 sysstat-8.1.5 ``` |
| SUSE Linux Enterprise Server 10 | The following packages (or later versions) must be installed:  ``` binutils-2.16.91.0.5 compat-libstdc++-5.0.7 (not needed with IBM:Linux on System z) gcc-4.1.2 gcc-c++-4.1.2 glibc-2.4-31.63 glibc-devel-2.4 glibc-devel-32bit-2.4 ksh-93r-12.9 libaio-0.3.104 libaio-32bit-0.3.104 libaio-devel-0.3.104 libaio-devel-32bit-0.3.104 libelf-0.8.5 libgcc-4.1.2 libstdc++-4.1.2 make-3.80 numactl-0.9.6.x86_64 sysstat-8.0.4 ``` |
| NeoKylin Linux Advanced Server 7 | The following packages (or later versions) must be installed:  ``` binutils-2.23.52.0.1-55.el7.x86_64 compat-libcap1-1.10-7.el7.x86_64 gcc-4.8.5-4.el7.ns7.01.x86_64 gcc-c++-4.8.5-4.el7.ns7.01.x86_64 glibc-2.17-105.el7.ns7.01.i686 glibc-2.17-105.el7.ns7.01.x86_64 glibc-devel-2.17-105.el7.ns7.01.i686 glibc-devel-2.17-105.el7.ns7.01.x86_64 ksh-20120801-22.el7_1.2.x86_64 libaio-0.3.109-13.el7.i686 libaio-0.3.109-13.el7.x86_64 libaio-devel-0.3.109-13.el7.i686 libaio-devel-0.3.109-13.el7.x86_64 libgcc-4.8.5-4.el7.ns7.01.i686 libgcc-4.8.5-4.el7.ns7.01.x86_64 libstdc++-4.8.5-4.el7.ns7.01.i686 libstdc++-4.8.5-4.el7.ns7.01.x86_64 libstdc++-devel-4.8.5-4.el7.ns7.01.i686 libstdc++-devel-4.8.5-4.el7.ns7.01.x86_64 libXi-1.7.4-2.el7.i686 libXi-1.7.4-2.el7.x86_64 libXtst-1.2.2-2.1.el7.i686 libXtst-1.2.2-2.1.el7.x86_64 make-3.82-21.el7.x86_64 sysstat-10.1.5-7.el7.x86_64 ``` |
| NeoKylin Linux Advanced Server 6 | The following packages (or later versions) must be installed:  ``` binutils-2.20.51.0.2-5.36.el6 (x86_64)  compat-libcap1-1.10-1 (x86_64)  compat-libstdc++-33-3.2.3-69.el6 (x86_64)  compat-libstdc++-33-3.2.3-69.el6 (i686)  gcc-4.4.7-4.el6 (x86_64)  gcc-c++-4.4.7-4.el6 (x86_64)  glibc-2.12-1.132.el6 (i686)  glibc-2.12-1.132.el6 (x86_64)  glibc-devel-2.12-1.132.el6 (x86_64)  glibc-devel-2.12-1.132.el6 (i686)  ksh  libgcc-4.4.7-4.el6 (i686)  libgcc-4.4.7-4.el6 (x86_64)  libstdc++-4.4.7-4.el6 (x86_64)  libstdc++-4.4.7-4.el6 (i686)  libstdc++-devel-4.4.7-4.el6 (x86_64)  libstdc++-devel-4.4.7-4.el6 (i686)  libaio-0.3.107-10.el6 (x86_64)  libaio-0.3.107-10.el6 (i686)  libaio-devel-0.3.107-10.el6 (x86_64)  libaio-devel-0.3.107-10.el6 (i686)  make-3.81-20.el6 sysstat-9.0.4-22.el6 (x86_64) ``` |

Note:

The numa package link for Linux x86-64 is `/usr/lib64/`.

Table 2-10 Linux x86-64 Oracle Database Features Package Requirements

| Item | Requirement |
| --- | --- |
| LDAP package | If you did not perform a default Linux installation, you intend to use LDAP, and you want to use the scripts `odisrvreg`, `oidca`, or `schemasync`, then install the Korn shell RPM for your Linux distribution. |
| Pro\*C/C++, Oracle Call Interface, Oracle C++ Call Interface, Oracle XML Developer's Kit (XDK) | Intel C/C++ Compiler 10.1 or later and the version of GNU C and C++ compilers listed previously for the distribution are supported for use with these products.  Note: Intel C/C++ Compiler v10.1 can be used only with the standard template libraries in the supported gcc versions to build Oracle C++ Call Interface (OCCI) applications.  Oracle XML Developer's Kit is supported with the same compilers as OCCI. |
| Pluggable Authentication Modules for Linux (Linux PAM) | Install the latest Linux PAM (Pluggable Authentication Modules for Linux) library for your Linux distribution. PAM provides greater flexibility for system administrators to choose how applications authenticate users. On Linux, external scheduler jobs require PAM. |
| Oracle ODBC Drivers | If you intend to use Open Database Connectivity (ODBC), then you should install the most recent ODBC Driver Manager for Linux.  You should obtain the most current ODBC driver from your operating system vendor. You can read about ODBC at the following URL:  ``` http://www.unixodbc.org ```  The ODBC RPMs are only needed if you plan on using ODBC. If you do not plan to use ODBC, then you do not need to install the ODBC RPMs for Oracle Clusterware, Oracle ASM, or Oracle RAC. |
| Oracle ODBC Drivers RPMs | To use ODBC, you must also install the following additional ODBC RPMs, depending on your operating system:  Oracle Linux 4, and Red Hat Enterprise Linux 4:  ``` unixODBC-2.2.11 (32 bit) or later unixODBC-devel-2.2.11 (64 bit) or later unixODBC-2.2.11 (64 bit ) or later ```  Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5:  ``` unixODBC-devel-2.2.11 (32 bit) or later unixODBC-devel-2.2.11 (64 bit) or later unixODBC-2.2.11 (64 bit) or later ```  Oracle Linux 6 and Red Hat Enterprise Linux 6:  ``` unixODBC-2.2.14-11.el6 (x86_64) or later unixODBC-2.2.14-11.el6.i686 or later unixODBC-devel-2.2.14-11.el6 (x86_64) or later unixODBC-devel-2.2.14-11.el6.i686 or later ```  Oracle Linux 7 and Red Hat Enterprise Linux 7:  ``` unixODBC-2.3.1-6.el7.x86_64 or later unixODBC-2.3.1-6.el7.i686 or later unixODBC-devel-2.3.1-6.el7.x86_64 or later unixODBC-devel-2.3.1-6.el7.i686 or later ```  SUSE Linux Enterprise Server 10:  ``` unixODBC-32bit-2.2.11 (32 bit) or later unixODBC-2.2.11 (64 bit ) or later unixODBC-devel-2.2.11 (64 bit) or later ```  SUSE Linux Enterprise Server 11:  ``` unixODBC-2.2.12 or later unixODBC-devel-2.2.12 or later unixODBC-32bit-2.2.12 (32 bit) or later ```  On NeoKylin Linux Advanced Server 7:  ``` unixODBC-2.3.1-11.el7.i686 or later unixODBC-2.3.1-11.el7.x86_64 or later unixODBC-devel-2.3.1-11.el7.i686 or later unixODBC-devel-2.3.1-11.el7.x86_64 or later ```  On NeoKylin Linux Advanced Server 6:  ``` unixODBC-2.2.14-12.el6_3.i686 or later unixODBC-2.2.14-12.el6_3.x86_64 or later unixODBC-devel-2.2.14-12.el6_3.x86_64 or later unixODBC-devel-2.2.14-12.el6_3.i686 or later ``` |
| Oracle JDBC/OCI Drivers | You can use the following optional JDK version with the Oracle JDBC/OCI drivers; however, it is not required for the installation:  - JDK 6 (Java SE Development Kit `1.6.0_21`) - JDK 1.5.0\_24 (JDK 5.0) with the JNDI extension  Note: By default, JDK 1.5 is installed with this release. |
| Oracle Real Application Clusters | For a cluster file system, use the following option:  OCFS2  - Version 1.2.9 or later  To check your OCFS version, enter the following command:  ``` modinfo ocfs2 ```  To check the version of OCFS2 tools and OCFS2 console, enter the following command:  ``` rpm -qa\| grep ocfs2 ```  Ensure that `ocfs2console` and `ocfs2-tools` are at least version 1.2.7  For information about OCFS2, refer to the following website:  ``` http://oss.oracle.com/projects/ocfs2/ ```  For OCFS2 certification status, refer to the Certify page on My Oracle Support.  ``` http://oss.oracle.com/projects/ocfs2/ ```  For OCFS2 certification status, refer to the Certify page on My Oracle Support. |

### 2.8.3 Software Requirements list for IBM: Linux on System z

Ensure that OpenSSH is installed on your servers. OpenSSH is the required SSH software.

Table 2-11 IBM: Linux on System z Package Requirements

| Item | Requirement |
| --- | --- |
| Operating systems | Red Hat Enterprise Linux 7  Red Hat Enterprise Linux 6  Red Hat Enterprise Linux 5  Red Hat Enterprise Linux 4  SUSE Linux Enterprise Server 11  SUSE Linux Enterprise Server 10 |
| Kernel version | The system must be running the following kernel version for each Linux distribution.  Red Hat Enterprise Linux 7:  3.10.0-229.el7 or later  Red Hat Enterprise Linux 6:  2.6.32-200 or later  Red Hat Enterprise Linux 5:  2.6.18 or later  Red Hat Enterprise Linux 4:  2.6.9 or later  SUSE Linux Enterprise Server 11:  2.6.32.12 or later  SUSE Linux Enterprise Server 10:  2.6.16.60 or later |
| Red Hat Enterprise Linux 7 | The following packages (or later versions) must be installed  ``` binutils-2.23.52.0.1-30.el7.s390x compat-libcap1-1.10-7.el7.s390x cpp-4.8.2-16.el7.s390x gcc-4.8.3-9.el7.s390x gcc-c++-4.8.3-9.el7.s390x glibc-2.17-78.el7.s390 glibc-2.17-78.el7.s390x glibc-devel-2.17-78.el7.s390 glibc-devel-2.17-78.el7.s390x glibc-headers-2.17-55.el7.s390x ksh-20120801-22.el7.s390x libaio-0.3.109-12.el7.s390 libaio-0.3.109-12.el7.s390x libaio-devel-0.3.109-12.el7.s390 libaio-devel-0.3.109-12.el7.s390x libgcc-4.8.3-9.el7.s390 libgcc-4.8.3-9.el7.s390x libstdc++-4.8.3-9.el7.s390 libstdc++-4.8.3-9.el7.s390x libstdc++-devel-4.8.3-9.el7.s390 libstdc++-devel-4.8.3-9.el7.s390x libXi-1.2.2-2.1.el7.s390 libXi-1.2.2-2.1.el7.s390x libXtst-1.2.2-2.1.el7.s390 libXtst-1.2.2-2.1.el7.s390x make-3.82-21.el7.s390x mpfr-3.1.1-4.el7.s390x sysstat-10.1.5-7.el7.s390x ``` |
| Red Hat Enterprise Linux 6 | The following packages (or later versions) must be installed:  ``` binutils-2.20.51.0.2-5.28 (s390x) compat-libstdc++-33-3.2.3-69.el6 (s390) gcc-4.4.6-3.el6 (s390x)  gcc-c++-4.4.6-3.el6 (s390x) glibc-2.12-1.47.el6 (s390) glibc-2.12-1.47.el6 (s390x) glibc-devel-2.12-1.47.el6 (s390) glibc-devel-2.12-1.47.el6 (s390x) ksh libaio-0.3.107-10.el6 (s390) libaio-0.3.107-10.el6 (s390x) libaio-devel-0.3.107-10.el6 (s390x) libgcc-4.4.6-3.el6 (s390) libgcc-4.4.6-3.el6 (s390x) libstdc++-4.4.6-3.el6 (s390x) make-3.81-19.el6 (s390x) sysstat-9.0.4-18.el6 (s390x) unixODBC-2.2.14-11.el6 (s390x) (Only needed if using ODBC) unixODBC-devel-2.2.14-11.el6 (s390x) (Only needed if using ODBC) ``` |
| Red Hat Enterprise Linux 5 | The following packages (or later versions) must be installed:  ``` binutils-2.17.50.0.6-12.el5 (s390x) compat-libstdc++-33-3.2.3-61 (s390) compat-libstdc++-33-3.2.3-61 (s390x) gcc-4.1.2-46.el5 (s390x) gcc-c++-4.1.2-46.el5 (s390x) glibc-2.5-42(s390) glibc-2.5-42 (s390x) glibc-devel-2.5-42 (s390) glibc-devel-2.5-42 (s390x) ksh libaio-0.3.106-3.2 (s390) libaio-0.3.106-3.2 (s390x) libaio-devel-0.3.106-3.2 (s390) libaio-devel-0.3.106-3.2 (s390x) libgcc-4.1.2-46.el5 (s390) libgcc-4.1.2-46.el5 (s390x) libstdc++-4.1.2-46.el5 (s390) libstdc++-4.1.2-46.el5 (s390x) libstdc++-devel-4.1.2-46.el5 (s390x) make-3.81 sysstat-7.0.2-3.el5 (s390x) unixODBC-2.2.11 (Only needed if using ODBC) unixODBC-devel-2.2.11 (Only needed if using ODBC) ``` |
| Red Hat Enterprise Linux 4 | The following packages (or later versions) must be installed:  ``` binutils-2.15.92.0.2-25 (s390x) compat-libstdc++-33-3.2.3-47.3 (s390) compat-libstdc++-33-3.2.3-47.3 (s390x) gcc-3.4.6-11 (s390x) gcc-c++-3.4.6-11 (s390x) glibc-2.3.4-2.43 (s390) glibc-2.3.4-2.43 (s390x) glibc-devel-2.3.4-2.43 (s390) glibc-devel-2.3.4-2.43 (s390x) libaio-0.3.105-2 (s390) libaio-0.3.105-2 (s390x) libaio-devel-0.3.105-2 (s390) libaio-devel-0.3.105-2 (s390x) libgcc-3.4.6-11 (s390) libgcc-3.4.6-11 (s390x) libstdc++-3.4.6-10.0.1 libstdc++-3.4.6-10.0.1 (32-bit) libstdc++-devel-3.4.6-10.0.1 libstdc++-devel-3.4.6-10.0.1 (x86_64) make-3.80 pdksh sysstat-5.0.5-25.el4 (s390x) unixODBC-2.2.11 (Only needed if using ODBC) unixODBC-devel-2.2.11 (Only needed if using ODBC) ``` |
| SUSE Linux Enterprise Server 11 | The following packages (or later versions) must be installed:  ``` binutils-2.20.0-0.7.9 (s390x) gcc-4.3-62.198 (s390x) gcc-c++-4.3-62.198 (s390x) glibc-2.11.1-0.17.4 (s390x) glibc-32bit-2.11.1-0.17.4 (s390x) glibc-devel-2.11.1-0.17.4 (s390x) glibc-devel-32bit-2.11.1-0.17.4 (s390x) ksh libaio-0.3.109-0.1.46 (s390x) libaio-32bit-0.3.109-0.1.46 (s390x) libaio-devel-0.3.109-0.1.46 (s390x) libaio-devel-32bit-0.3.109-0.1.46 (s390x) libstdc++43-4.3.4_20091019-0.7.35 (s390x) libstdc++43-32bit-4.3.4_20091019-0.7.35 (s390x) libstdc++43-devel-4.3.4_20091019-0.7.35 (s390x) libstdc++43-devel-32bit-4.3.4_20091019-0.7.35 (s390x) libgcc43-4.3.4_20091019-0.7.35 make-3.81 sysstat-8.1.5-7.9.56 (s390x) unixODBC-2.2.11 (Only needed if using ODBC) unixODBC-devel-2.2.11 (Only needed if using ODBC) ``` |
| SUSE Linux Enterprise Server 10 | The following packages (or later versions) must be installed:  ``` binutils-32bit-2.16.91.0.5-23.34.33 (s390x) gcc-4.1.2_20070115-0.29.6 (s390x) gcc-c++-4.1.2_20070115-0.29.6 (s390x) glibc-2.4-31.74.1 (s390x) glibc-32bit-2.4-31.74.1 (s390x) glibc-devel-2.4-31.74.1 (s390x) glibc-devel-32bit-2.4-31.74.1 (s390x) ksh libaio-0.3.104-14.2 (s390x) libaio-32bit-0.3.104-14.2 (s390x) libaio-devel-0.3.104-14.2 (s390x) libaio-devel-32bit-0.3.104-14.2 (s390x) libgcc-4.1.2_20070115-0.29.6 (s390x) libstdc++-4.1.2_20070115-0.29.6 (s390x) libstdc++-devel-4.1.2_20070115-0.29.6 (s390x) make-3.80-202.2 (s390x) sysstat-8.0.4-1.7.27 (s390x) unixODBC-2.2.11 (Only needed if using ODBC) unixODBC-devel-2.2.11 (Only needed if using ODBC) ``` |
| IBM WebSphere MQ for Linux | MQ Series 7.0 (Red Hat 5, Red Hat 6, Red Hat 7, SUSE 10, SUSE 11) |
| Micro Focus Server Express | Micro Focus Server Express 5.1 |
| Oracle ODBC Drivers | If you intend to use ODBC, then install OCFS2 1.4 or later.  You can download and install the Driver Manager from the following URL:  ``` http://www.unixodbc.org ```  Linux RPMs are available on the site.  You do not require ODBC Driver Manager to install Oracle Clusterware, Oracle Database, or Oracle RAC.  The following additional ODBC RPMs are required (or later versions):  Red Hat Enterprise Linux 4:  ``` unixODBC-2.2.11 (32 bit) or later unixODBC-devel-2.2.11 (64 bit) or later unixODBC-2.2.11 (64 bit ) or later ```  Red Hat Enterprise Linux 5:  ``` unixODBC-2.2.11 (32 bit) or later unixODBC-devel-2.2.11 (64 bit) or later unixODBC-2.2.11 (64 bit) or later ```  Red Hat Enterprise Linux 6:  ``` unixODBC-2.2.14-11 (32 bit) or later unixODBC-devel-2.2.14-11(64 bit) or later unixODBC-2.2.14-11 (64 bit) or later ```  Red Hat Enterprise Linux 7:  ``` unixODBC-2.3.1-11 (32 bit) or later unixODBC-2.3.1-11 (64 bit) or later unixODBC-devel-2.3.1-11 (32 bit) or later unixODBC-devel-2.3.1-11 (64 bit) or later ```  SUSE Linux Enterprise Server 10:  ``` unixODBC-32bit-2.2.11 (32 bit) or later unixODBC-2.2.11 (64 bit ) or later unixODBC-devel-2.2.11 (64 bit) or later ```  On SUSE Linux Enterprise Server 11:  ``` unixODBC-2.2.12 or later unixODBC-devel-2.2.12 or later unixODBC-32bit-2.2.12 (32 bit) or later ``` |
| Oracle JDBC/OCI Drivers | You can use one of the following optional JDK versions with the Oracle JDBC/OCI drivers; however, they are not required for the installation:  - JDK 6 SR16 FP1 or higher - JDK 5 SR16 FP3 or higher |

## 2.9 Checking the Software Requirements

To ensure that the system meets these requirements, follow these steps:

1. To determine which distribution and version of Linux is installed, enter the following command:
	```
	# cat /proc/version
	```
	Note:
	Only the distributions and versions listed in the previous table are supported. Do not install the software on other versions of Linux.
2. To determine whether the required kernel errata is installed, enter the following command:
	```
	# uname -r
	```
	The following is sample output displayed by running this command on a Red Hat Enterprise Linux 4.0 system:
	```
	2.6.9-55.0.0.0.2.ELsmp
	```
	In this example, the output shows the kernel version (`2.6.9`) and errata level (`55.0.0.0.2.ELsmp`) on the system.
	Review the required errata level for your distribution. If the errata level is previous to the required minimum errata update, then obtain and install the latest kernel update from your Linux distributor.
3. To determine whether the required packages are installed, enter commands similar to the following:
	```
	# rpm -q package_name
	```
	Alternatively, if you require specific system architecture information, then enter the following command:
	```
	# rpm -qa --queryformat "%{NAME}-%{VERSION}-%{RELEASE} (%{ARCH})\n" | grep package_name
	```
	You can also combine a query for multiple packages, and review the output for the correct versions. For example:
	```
	# rpm -q binutils compat-libstdc++ elfutils gcc glibc libaio libgcc libstdc++ \
	make sysstat unixodbc
	```
	If a package is not installed, then install it from your Linux distribution media or download the required package version from your Linux distributor's Web site.
4. To determine if OCFS2 is installed, enter the following command:
	```
	# /sbin/modinfo ocfs2
	```
	To install the Oracle Database files on an OCFS2 file system and the packages are not installed, then download them from the following Web site. Follow the instructions listed with the kit to install the packages and configure the file system:
	```
	http://oss.oracle.com/projects/ocfs2/
	```

## 2.10 Verifying UDP and TCP Kernel Parameters

Set TCP/IP ephemeral port range parameters to provide enough ephemeral ports for the anticipated server workload. Ensure that the lower range is set to at least 9000 or higher, to avoid Well Known ports, and to avoid ports in the Registered Ports range commonly used by Oracle and other server ports. Set the port range high enough to avoid reserved ports for any applications you may intend to use. If the lower value of the range you have is greater than 9000, and the range is large enough for your anticipated workload, then you can ignore OUI warnings regarding the ephemeral port range.

For example, with IPv4, use the following command to check your current range for ephemeral ports:

```
$ cat /proc/sys/net/ipv4/ip_local_port_range
32768 61000
```

In the preceding example, the lowest port (32768) and the highest port (61000) are set to the default range.

If necessary, update the UDP and TCP ephemeral port range to a range high enough for anticipated system workloads, and to ensure that the ephemeral port range starts at 9000 and above. For example:

```
# echo 9000 65500 > /proc/sys/net/ipv4/ip_local_port_range
```

Oracle recommends that you make these settings permanent. For example, as `root`, use a text editor to open `/etc/sysctl.conf`, and add or change to the following: `net.ipv4.ip_local_port_range = 9000 65500`, and then restart the network (`# /etc/rc.d/init.d/network restart`). Refer to your Linux distribution system administration documentation for detailed information about how to automate this ephemeral port range alteration on system restarts.

## 2.11 Network Time Protocol Setting

Oracle Clusterware requires the same time zone setting on all cluster nodes. During installation, the installation process picks up the time zone setting of the Grid installation owner on the node where OUI runs, and uses that on all nodes as the default TZ setting for all processes managed by Oracle Clusterware. This default is used for databases, Oracle ASM, and any other managed processes.

You have two options for time synchronization: an operating system configured network time protocol (NTP), or Oracle Cluster Time Synchronization Service. Oracle Cluster Time Synchronization Service is designed for organizations whose cluster servers are unable to access NTP services. If you use NTP, then the Oracle Cluster Time Synchronization daemon (`ctssd`) starts up in observer mode. If you do not have NTP daemons, then `ctssd` starts up in active mode and synchronizes time among cluster members without contacting an external time server.

Note:

Before starting the installation of Oracle Grid Infrastructure, Oracle recommends that you ensure the clocks on all nodes are set to the same time.

If you have NTP daemons on your server but you cannot configure them to synchronize time with a time server, and you want to use Cluster Time Synchronization Service to provide synchronization service in the cluster, then deactivate and deinstall the NTP.

To deactivate the NTP service, you must stop the existing `ntpd` service, disable it from the initialization sequences and remove the `ntp.conf` file. To complete these step on Oracle Linux, and Asianux systems, run the following commands as the `root` user

```
# /sbin/service ntpd stop
# chkconfig ntpd off
# rm /etc/ntp.conf
```

or, `mv /etc/ntp.conf` to `/etc/ntp.conf.org`.

Also remove the following file:

```
/var/run/ntpd.pid
```

This file maintains the pid for the NTP daemon.

When the installer finds that the NTP protocol is not active, the Cluster Time Synchronization Service is installed in active mode and synchronizes the time across the nodes. If NTP is found configured, then the Cluster Time Synchronization Service is started in observer mode, and no active time synchronization is performed by Oracle Clusterware within the cluster.

To confirm that `ctssd` is active after installation, enter the following command as the Grid installation owner:

```
$ crsctl check ctss
```

If you are using NTP, and you prefer to continue using it instead of Cluster Time Synchronization Service, then you need to modify the NTP configuration to set the `-x` flag, which prevents time from being adjusted backward. Restart the network time protocol daemon after you complete this task.

To do this, on Oracle Linux, Red Hat Linux, and Asianux systems, edit the `/etc/sysconfig/ntpd` file to add the `-x` flag, as in the following example:

```
# Drop root to id 'ntp:ntp' by default.
OPTIONS="-x -u ntp:ntp -p /var/run/ntpd.pid"

# Set to 'yes' to sync hw clock after successful ntpdate
SYNC_HWCLOCK=no

# Additional options for ntpdate
NTPDATE_OPTIONS=""
```

Then, restart the NTP service.

```
# /sbin/service ntp restart
```

On SUSE systems, modify the configuration file `/etc/sysconfig/ntp` with the following settings:

```
NTPD_OPTIONS="-x -u ntp"
```

Restart the daemon using the following command:

```
# service ntp restart
```

## 2.12 Installing the cvuqdisk Package for Linux

Install the operating system package `cvuqdisk`. Without `cvuqdisk`, Cluster Verification Utility cannot discover shared disks, and you receive the error message "Package cvuqdisk not installed" when you run Cluster Verification Utility. Use the `cvuqdisk` rpm for your hardware (for example, `x86_64`, or `i386`).

To install the `cvuqdisk` RPM, complete the following procedure:

1. Locate the `cvuqdisk` RPM package, which is in the directory `rpm` on the installation media. If you have already installed Oracle Grid Infrastructure, then it is located in the directory `grid_home` `/rpm`.
2. Copy the `cvuqdisk` package to each node on the cluster. You should ensure that each node is running the same version of Linux.
3. Log in as `root`.
4. Use the following command to find if you have an existing version of the `cvuqdisk` package:
	```
	# rpm -qi cvuqdisk
	```
	If you have an existing version, then enter the following command to deinstall the existing version:
	```
	# rpm -e cvuqdisk
	```
5. Set the environment variable `CVUQDISK_GRP` to point to the group that will own cvuqdisk, typically `oinstall`. For example:
	```
	# CVUQDISK_GRP=oinstall; export CVUQDISK_GRP
	```
6. In the directory where you have saved the cvuqdisk rpm, use the following command to install the `cvuqdisk` package:
	```
	rpm -iv package
	```
	For example:
	```
	# rpm -iv cvuqdisk-1.0.9-1.rpm
	```

## 2.13 Enabling Intelligent Platform Management Interface (IPMI)

Intelligent Platform Management Interface (IPMI) provides a set of common interfaces to computer hardware and firmware that system administrators can use to monitor system health and manage the system. With Oracle 11g release 2, Oracle Clusterware can integrate IPMI to provide failure isolation support and to ensure cluster integrity.

You can configure node-termination with IPMI during installation by selecting a node-termination protocol, such as IPMI. You can also configure IPMI after installation with `crsctl` commands.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92099) for information about how to configure IPMI after installation

### 2.13.1 Requirements for Enabling IPMI

You must have the following hardware and software configured to enable cluster nodes to be managed with IPMI:

- Each cluster member node requires a Baseboard Management Controller (BMC) running firmware compatible with IPMI version 1.5 or greater, which supports IPMI over LANs, and configured for remote control using LAN.
- Each cluster member node requires an IPMI driver installed on each node.
- The cluster requires a management network for IPMI. This can be a shared network, but Oracle recommends that you configure a dedicated network.
- Each cluster member node's Ethernet port used by BMC must be connected to the IPMI management network.
- Each cluster member must be connected to the management network.
- Some server platforms put their network interfaces into a power saving mode when they are powered off. In this case, they may operate only at a lower link speed (for example, 100 MB, instead of 1 GB). For these platforms, the network switch port to which the BMC is connected must be able to auto-negotiate down to the lower speed, or IPMI will not function properly.

### 2.13.2 Configuring the IPMI Management Network

You can configure the BMC for DHCP, or for static IP addresses. Oracle recommends that you configure the BMC for dynamic IP address assignment using DHCP. To use this option, you must have a DHCP server configured to assign the BMC IP addresses.

Note:

If you configure IPMI, and you use Grid Naming Service (GNS) you still must configure separate addresses for the IPMI interfaces. As the IPMI adapter is not seen directly by the host, the IPMI adapter is not visible to GNS as an address on the host.

### 2.13.3 Configuring the IPMI Driver

For Oracle Clusterware to communicate with the BMC, the IPMI driver must be installed permanently on each node, so that it is available on system restarts. The IPMI driver is available on the Asianux Linux, Oracle Linux, Red Hat Enterprise Linux, and SUSE Enterprise Linux distributions supported with this release.

#### 2.13.3.1 Configuring the Open IPMI Driver

On Linux systems, the OpenIPMI driver is the supported driver for Oracle Clusterware deployments with IPMI.

You can install and configure the driver dynamically by manually loading the required modules. Contact your Linux distribution vendor for information about how to configure IPMI for your distribution.

The following example shows how to configure the Open IPMI driver manually on Oracle Linux:

1. Log in as `root`.
2. Run the following commands:
	```
	# /sbin/modprobe ipmi_msghandler
	# /sbin/modprobe ipmi_si
	# /sbin/modprobe ipmi_devintf
	```
3. (Optional) Run the command `/sbin/lsmod |grep ipmi` to confirm that the IPMI modules are loaded. For example:
	```
	# /sbin/lsmod | grep ipmi
	ipmi_devintf           12617  0
	ipmi_si                33377  0
	ipmi_msghandler        33701  2 ipmi_devintf,ipmi_si
	```
	Note:
	You can install the modules whether or not a BMC is present.
4. Open the `/etc/rc.local` file using a text editor, navigate to the end of the file, and enter lines similar to the following so that the `modprobe` commands in step 2 will be run automatically on system restart:
	```
	# START IPMI ON SYSTEM RESTART
	/sbin/modprobe ipmi_msghandler
	/sbin/modprobe ipmi_si
	/sbin/modprobe ipmi_devintf
	```
	Note:
	On SUSE systems, add the `modprobe` commands above to `/etc/init.d/boot.local`.
5. Check to ensure that the Linux system is recognizing the IPMI device, using the following command:
	```
	ls -l /dev/ipmi0
	```
	If the IPMI device has been dynamically loaded, then the output should be similar to the following:
	```
	# ls -l /dev/ipmi0
	crw-------  1 root root 253, 0 Sep 23 06:29 /dev/ipmi0
	```
	If you do see the device file output, then the IPMI driver is configured, and you can ignore the following step.
	If you do not see the device file output, then the `udevd` daemon is not set up to create device files automatically. Proceed to the next step.
6. Determine the device major number for the IPMI device using the command `grep ipmi /proc/devices`. For example:
	```
	# grep ipmi /proc/devices
	253 ipmidev
	```
	In the preceding example, the device major number is 253.
7. Run the `mknod` command to create a directory entry and i-node for the IPMI device, using the device major number. For example:
	```
	# mknod /dev/ipmi0 c 253 0x0
	```
	The permissions on `/dev/ipmi0` in the preceding example allow the device to be accessible only by `root`. The device should only be accessed by `root`, to prevent a system vulnerability.

#### 2.13.3.2 Configuring the BMC

Configure BMC on each node for remote control using LAN for IPMI-based node fencing to function properly. You can configure BMC from the BIOS prompt, using a distribution-specific management utility, or you can configure BMC using publicly available utilities, such as the following:

IPMItool, which is available for Linux:

`http://ipmitool.sourceforge.net`

IPMIutil, which is available for Linux and Windows:

`http://ipmiutil.sourceforge.net`

Refer to the documentation for the configuration tool you select for details about using the tool to configure the BMC.

When you configure the BMC on each node, you must complete the following

- Enable IPMI over LAN, so that the BMC can be controlled over the management network.
- Enable dynamic IP addressing using DHCP or GNS, or configure a static IP address for the BMC.
- Establish an administrator user account and password for the BMC.
- Configure the BMC for VLAN tags, if you will use the BMC on a tagged VLAN.

The configuration tool you use does not matter, but these conditions must be met for the BMC to function properly.

##### 2.13.3.2.1 Example of BMC Configuration Using IPMItool

The following is an example of configuring BMC using `ipmitool` (version 1.8.6).

1. Log in as `root`.
2. Verify that `ipmitool` can communicate with the BMC using the IPMI driver by using the command `bmc info`, and looking for a device ID in the output. For example:
	```
	# ipmitool bmc info
	Device ID                 : 32
	.
	.
	.
	```
	If `ipmitool` is not communicating with the BMC, then review the section "Configuring the Open IPMI Driver" and ensure that the IPMI driver is running.
3. Enable IPMI over LAN using the following procedure
	1. Determine the channel number for the channel used for IPMI over LAN. Beginning with channel 1, run the following command until you find the channel that displays LAN attributes (for example, the IP address):
		```
		# ipmitool lan print 1
		 
		. . . 
		IP Address Source       : 0x01
		IP Address              : 140.87.155.89
		. . .
		```
		2. Turn on LAN access for the channel found. For example, where the channel is 1:
		```
		# ipmitool lan set 1 access on
		```
4. Configure IP address settings for IPMI using one of the following procedure:
	- Using dynamic IP addressing (DHCP)
		Dynamic IP addressing is the default assumed by Oracle Universal Installer. Oracle recommends that you select this option so that nodes can be added or removed from the cluster more easily, as address settings can be assigned automatically.
		Note:
		Use of DHCP requires a DHCP server on the subnet.
		Set the channel. For example, if the channel is 1, then enter the following command to enable DHCP:
		```
		# ipmitool lan set 1 ipsrc dhcp
		```
		- Using static IP Addressing
		If the BMC shares a network connection with the operating system, then the IP address must be on the same subnet. You must set not only the IP address, but also the proper values for netmask, and the default gateway. For example, assuming the channel is 1:
		```
		# ipmitool lan set 1 ipaddr 192.168.0.55
		# ipmitool lan set 1 netmask 255.255.255.0
		# ipmitool lan set 1 defgw ipaddr 192.168.0.1
		```
		Note that the specified address (`192.168.0.55`) will be associated only with the BMC, and will not respond to normal pings.
5. Establish an administration account with a username and password, using the following procedure (assuming the channel is 1):
	1. Set BMC to require password authentication for ADMIN access over LAN. For example:
		```
		# ipmitool lan set 1 auth ADMIN MD5,PASSWORD
		```
		2. List the account slots on the BMC, and identify an unused slot (a user ID with an empty user name field). For example:
		```
		# ipmitool channel getaccess 1
		. . . 
		User ID              : 4
		User Name            :
		Fixed Name           : No
		Access Available     : call-in / callback
		Link Authentication  : disabled
		IPMI Messaging       : disabled
		Privilege Level      : NO ACCESS
		. . .
		```
		3. Assign the desired administrator user name and password and enable messaging for the identified slot. (Note that for IPMI v1.5 the user name and password can be at most 16 characters). Also, set the privilege level for that slot when accessed over LAN (channel 1) to ADMIN (level 4). For example, where `username` is the administrative user name, and `password` is the password:
		```
		# ipmitool user set name 4 username
		# ipmitool user set password 4 password
		# ipmitool user enable 4
		# ipmitool channel setaccess 1 4 privilege=4
		# ipmitool channel setaccess 1 4 link=on
		# ipmitool channel setaccess 1 4 ipmi=on
		```
		4. Verify the setup using the command lan print 1. The output should appear similar to the following. Note that the items in bold text are the settings made in the preceding configuration steps, and comments or alternative options are indicated within brackets \[\]:
		```
		# ipmitool lan print 1
		Set in Progress         : Set Complete
		Auth Type Support       : NONE MD2 MD5 PASSWORD
		Auth Type Enable        : Callback : MD2 MD5
		                        : User     : MD2 MD5
		                        : Operator : MD2 MD5
		                        : Admin    : MD5 PASSWORD
		                        : OEM      : MD2 MD5
		IP Address Source       : DHCP Address [or Static Address]
		IP Address              : 192.168.0.55
		Subnet Mask             : 255.255.255.0
		MAC Address             : 00:14:22:23:fa:f9
		SNMP Community String   : public
		IP Header               : TTL=0x40 Flags=0x40 Precedence=… 
		Default Gateway IP      : 192.168.0.1
		Default Gateway MAC     : 00:00:00:00:00:00
		.
		.
		.
		# ipmitool channel getaccess 1 4
		Maximum User IDs     : 10
		Enabled User IDs     : 2
		 
		User ID              : 4
		User Name            : username [This is the administration user]
		Fixed Name           : No
		Access Available     : call-in / callback
		Link Authentication  : enabled
		IPMI Messaging       : enabled
		Privilege Level      : ADMINISTRATOR
		```
6. Verify that the BMC is accessible and controllable from a remote node in your cluster using the `bmc info` command. For example, if `node2-ipmi` is the network host name assigned the IP address of `node2` 's BMC, then to verify the BMC on node `node2` from `node1`, with the administrator account `username` and the password `mypassword`, enter the following command on `node1`:
	```
	$ ipmitool -H node2-ipmi -U username -P mypassword bmc info
	```
	If the BMC is correctly configured, then you should see information about the BMC on the remote node. If you see an error message, such as `Error: Unable to establish LAN session`, then you must check the BMC configuration on the remote node.

## 2.14 Automatic SSH Configuration During Installation

To install Oracle software, Secure Shell (SSH) connectivity should be set up between all cluster member nodes. OUI uses the `ssh` and `scp` commands during installation to run remote commands on and copy files to the other cluster nodes. You must configure SSH so that these commands do not prompt for a password.

Note:

Oracle Grid Infrastructure installations require SSH, because Oracle configuration assistants use SSH for configuration options from local to remote nodes. Oracle Enterprise Manager also uses SSH. RSH is no longer supported for internode communication.

You can configure SSH from the OUI interface during installation for the user account running the installation. The automatic configuration creates passwordless SSH connectivity between all cluster member nodes. Oracle recommends that you use the automatic procedure if possible.

To enable the script to run, you must remove `stty` commands from the profiles of any Oracle software installation owners, and remove other security measures that are triggered during a login, and that generate messages to the terminal. These messages, mail checks, and other displays prevent Oracle software installation owners from using the SSH configuration script that is built into the Oracle Universal Installer. If they are not disabled, then SSH must be configured manually before an installation can be run.

In rare cases, Oracle Clusterware installation may fail during the "AttachHome" operation when the remote node closes the SSH connection. To avoid this problem, set the following parameter in the SSH daemon configuration file /etc/ssh/sshd\_config on all cluster nodes to set the timeout wait to unlimited:

```
LoginGraceTime 0
```

See Also:

Preventing Installation Errors Caused by Terminal Output Commands for information about how to remove `stty` commands in user profiles

## 2.15 Configuring Grid Infrastructure Software Owner User Environments

You run the installer software with the Oracle Grid Infrastructure installation owner user account (`oracle` or `grid`). However, before you start the installer, you must configure the environment of the installation owner user account. Also, create other required Oracle software owners, if needed.

This section contains the following topics:

- Environment Requirements for Oracle Grid Infrastructure Software Owner
- Procedure for Configuring Oracle Software Owner Environments
- Check Resource Limits for the Oracle Software Installation Users
- Setting Display and X11 Forwarding Configuration
- Preventing Installation Errors Caused by Terminal Output Commands

### 2.15.1 Environment Requirements for Oracle Grid Infrastructure Software Owner

You must make the following changes to configure the Oracle Grid Infrastructure software owner environment:

- Set the installation software owner user (`grid`, `oracle`) default file mode creation mask (umask) to 022 in the shell startup file. Setting the mask to 022 ensures that the user performing the software installation creates files with 644 permissions.
- Set ulimit settings for file descriptors and processes for the installation software owner (`grid`, `oracle`)
- Set the software owner's environment variable `DISPLAY` environment variables in preparation for the Oracle Grid Infrastructure installation

### 2.15.2 Procedure for Configuring Oracle Software Owner Environments

To set the Oracle software owners' environments, follow these steps, for each software owner (`grid`, `oracle`):

1. Start a new terminal session; for example, start an X terminal (`xterm`).
2. Enter the following command to ensure that X Window applications can display on this system:
	```
	$ xhost + hostname
	```
	The hostname is the name of the local host.
3. If you are not already logged in to the system where you want to install the software, then log in to that system as the software owner user.
4. If you are not logged in as the user, then switch to the software owner user you are configuring. For example, with the `grid` user:
	```
	$ su - grid
	```
5. To determine the default shell for the user, enter the following command:
	```
	$ echo $SHELL
	```
6. Open the user's shell startup file in any text editor:
	- Bash shell (`bash`):
		```
		$ vi .bash_profile
		```
		- Bourne shell (`sh`) or Korn shell (`ksh`):
		```
		$ vi .profile
		```
		- C shell (`csh` or `tcsh`):
		```
		% vi .login
		```
7. Enter or edit the following line, specifying a value of 022 for the default file mode creation mask:
	```
	umask 022
	```
8. If the `ORACLE_SID`, `ORACLE_HOME`, or `ORACLE_BASE` environment variables are set in the file, then remove these lines from the file.
9. Save the file, and exit from the text editor.
10. To run the shell startup script, enter one of the following commands:
	- Bash shell:
		```
		$ . ./.bash_profile
		```
		- Bourne, Bash, or Korn shell:
		```
		$ . ./.profile
		```
		- C shell:
		```
		% source ./.login
		```
11. If you are not installing the software on the local system, then enter a command similar to the following to direct X applications to display on the local system:
	- Bourne, Bash, or Korn shell:
		```
		$ DISPLAY=local_host
		:0.0 ; export DISPLAY
		```
		- C shell:
		```
		% setenv DISPLAY local_host
		:0.0
		```
	In this example, `local_host` is the host name or IP address of the system (your workstation, or another client) on which you want to display the installer.
12. If you determined that the `/tmp` directory has less than 1 GB of free space, then identify a file system with at least 1 GB of free space and set the `TEMP` and `TMPDIR` environment variables to specify a temporary directory on this file system:
	Note:
	You cannot use a shared file system as the location of the temporary file directory (typically `/tmp`) for Oracle RAC installation. If you place `/tmp` on a shared file system, then the installation fails.
	1. Use the `df -h` command to identify a suitable file system with sufficient free space.
		2. If necessary, enter commands similar to the following to create a temporary directory on the file system that you identified, and set the appropriate permissions on the directory:
		```
		$ su - root
		# mkdir /mount_point/tmp
		# chmod 775 /mount_point/tmp
		# exit
		```
		3. Enter commands similar to the following to set the `TEMP` and `TMPDIR` environment variables:
		- Bourne, Bash, or Korn shell:
			```
			$ TEMP=/mount_point/tmp
			$ TMPDIR=/mount_point/tmp
			$ export TEMP TMPDIR
			```
				- C shell:
			```
			% setenv TEMP /mount_point/tmp
			% setenv TMPDIR /mount_point/tmp
			```
13. To verify that the environment has been set correctly, enter the following commands:
	```
	$ umask
	$ env | more
	```
	Verify that the `umask` command displays a value of `22`, `022`, or `0022` and that the environment variables you set in this section have the correct values.

### 2.15.3 Check Resource Limits for the Oracle Software Installation Users

For each installation software owner, check the resource limits for installation, using the following recommended ranges:

Table 2-12 Installation Owner Resource Limit Recommended Ranges

| Resource Shell Limit | Resource | Soft Limit | Hard Limit |
| --- | --- | --- | --- |
| Open file descriptors | nofile | at least 1024 | at least 65536 |
| Number of processes available to a single user | nproc | at least 2047 | at least 16384 |
| Size of the stack segment of the process | stack | at least 10240 KB | at least 10240 KB, and at most 32768 KB |

To check resource limits:

1. Log in as an installation owner.
2. Check the soft and hard limits for the file descriptor setting. Ensure that the result is in the recommended range. For example:
	```
	$ ulimit -Sn
	1024
	$ ulimit -Hn
	65536
	```
3. Check the soft and hard limits for the number of processes available to a user. Ensure that the result is in the recommended range. For example:
	```
	$ ulimit -Su
	2047
	$ ulimit -Hu
	16384
	```
4. Check the soft limit for the stack setting. Ensure that the result is in the recommended range. For example:
	```
	$ ulimit -Ss
	10240
	$ ulimit -Hs
	32768
	```
5. Repeat this procedure for each Oracle software installation owner.

### 2.15.4 Setting Display and X11 Forwarding Configuration

If you are on a remote terminal, and the local node has only one visual (which is typical), then use the following syntax to set the DISPLAY environment variable:

Bourne, Korn, and Bash shells

```
$ export DISPLAY=hostname:0
```

C shell:

```
$ setenv DISPLAY hostname:0
```

For example, if you are using the Bash shell, and if your host name is `node1`, then enter the following command:

```
$ export DISPLAY=node1:0
```

To ensure that X11 forwarding will not cause the installation to fail, create a user-level SSH client configuration file for the Oracle software owner user, as follows:

1. Using any text editor, edit or create the software installation owner's `~/.ssh/config` file.
2. Make sure that the `ForwardX11` attribute is set to `no`. For example:
	```
	Host *
	      ForwardX11 no
	```

### 2.15.5 Preventing Installation Errors Caused by Terminal Output Commands

During an Oracle Grid Infrastructure installation, OUI uses SSH to run commands and copy files to the other nodes. During the installation, hidden files on the system (for example, `.bashrc` or `.cshrc`) will cause makefile and other installation errors if they contain terminal output commands.

To avoid this problem, you must modify these files in each Oracle installation owner user home directory to suppress all output on `STDOUT` or `STDERR` (for example, `stty`, `xtitle`, and other such commands) as in the following examples:

- Bourne, Bash, or Korn shell:
	```
	if [ -t 0 ]; then
	   stty intr ^C
	fi
	```
- C shell:
	```
	test -t 0
	if ($status == 0) then
	   stty intr ^C
	endif
	```
	Note:
	When SSH is not available, the Installer uses the `rsh` and `rcp` commands instead of `ssh` and `scp`.
	If there are hidden files that contain `stty` commands that are loaded by the remote shell, then OUI indicates an error and stops the installation.

## 2.16 Requirements for Creating an Oracle Grid Infrastructure Home Directory

During installation, you are prompted to provide a path to a home directory to store Oracle Grid Infrastructure software. Ensure that the directory path you provide meets the following requirements:

- It should be created in a path outside existing Oracle homes, including Oracle Clusterware homes.
- It should not be located in a user home directory.
- It should be created either as a subdirectory in a path where all files can be owned by `root`, or in a unique path.
- If you create the path before installation, then it should be owned by the installation owner of Oracle Grid Infrastructure (typically `oracle` for a single installation owner for all Oracle software, or `grid` for role-based Oracle installation owners), and set to 775 permissions.

Oracle recommends that you install Oracle Grid Infrastructure on local homes, rather than using a shared home on shared storage.

For installations with Oracle Grid Infrastructure only, Oracle recommends that you create a path compliant with Oracle Optimal Flexible Architecture (OFA) guidelines, so that Oracle Universal Installer (OUI) can select that directory during installation. For OUI to recognize the path as an Oracle software path, it must be in the form u0\[1-9\]/app.

When OUI finds an OFA-compliant path, it creates the Oracle Grid Infrastructure and Oracle Inventory (`oraInventory`) directories for you.

To create an Oracle Grid Infrastructure path manually, ensure that it is in a separate path, not under an existing Oracle base path. For example:

```
# mkdir -p  /u01/app/11.2.0/grid
# chown grid:oinstall /u01/app/11.2.0/grid
# chmod -R 775 /u01/app/11.2.0/grid
```

With this path, if the installation owner is named grid, then by default OUI creates the following path for the Grid home:

```
/u01/app/11.2.0/grid
```

Create an Oracle base path for database installations, owned by the Oracle Database installation owner account. The OFA path for an Oracle base is `/u01/app/` `user`, where `user` is the name of the Oracle software installation owner account. For example, use the following commands to create an Oracle base for the database installation owner account `oracle`:

```
# mkdir -p  /u01/app/oracle
# chown -R oracle:oinstall /u01/app/oracle
# chmod -R 775 /u01/app/oracle
```

Note:

If you choose to create an Oracle Grid Infrastructure home manually, then do not create the Oracle Grid Infrastructure home for a cluster under either the grid installation owner Oracle base or the Oracle Database installation owner Oracle base. Creating an Oracle Clusterware installation in an Oracle base directory will cause succeeding Oracle installations to fail.

Oracle Grid Infrastructure homes can be placed in a local home on servers, even if your existing Oracle Clusterware home from a prior release is in a shared location.

Homes for Oracle Grid Infrastructure for a standalone server (Oracle Restart) can be under Oracle base. Refer to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for more information about Oracle Restart.

## 2.17 Cluster Name Requirements

The cluster name must be at least one character long and no more than 15 characters in length, must be alphanumeric, cannot begin with a numeral, and may contain hyphens (-).

In a Typical installation, the SCAN you provide is also the name of the cluster, so the SCAN name must meet the requirements for a cluster name. In an Advanced installation, The SCAN and cluster name are entered in separate fields during installation, so cluster name requirements do not apply to the SCAN name.