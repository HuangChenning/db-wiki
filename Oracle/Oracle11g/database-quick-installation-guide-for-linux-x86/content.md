---
title: "Oracle® Database Quick Installation Guide"
book: Database Quick Installation Guide for Linux x86
doc_id: E24324-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24324/toc.htm
tags:
  - oracle
  - 11g
  - database-quick-installation-guide-for-linux-x86
---

## Oracle® Database

Quick Installation Guide

11g Release 2 (11.2) for Linux x86

E24324-06

This guide describes how to quickly install Oracle Database 11g Release 2 (11.2) on Linux x86 systems. It includes information about the following:

## 1 Reviewing Information About This Guide

This guide describes how to install Oracle Database by using the default installation options.

Tasks Described in This Guide

The procedures in this guide describe how to:

- Configure your system to support Oracle Database
- Install Oracle Database on a local file system by using the Typical Installation option
- Configure a general-purpose Oracle Database installation that uses the local file system for database file storage

Results of a Successful Installation

After you successfully install Oracle Database:

- The database that you created and the default Oracle Net listener process run on the system.
- Oracle Enterprise Manager Database Control run on the system and can be accessed by using a web browser.

Tasks Not Described in This Guide

This guide covers the Typical Installation scenario and does not describe how to complete the following tasks:

- Using the Advanced Installation option to install the software
- Installing the software on a system that has an existing Oracle software installation
- Installing Oracle Clusterware and Oracle Real Application Clusters on a cluster
- Enabling Enterprise Manager e-mail notifications or automated backups
- Enabling core file creation
- Verifying UDP and TCP kernel parameters
- Using alternative storage options such as Oracle Automatic Storage Management
- Installing and configuring Oracle Grid Infrastructure

Where to Get Additional Installation Information

For more information about installing Oracle Database, including information about the tasks not described in this guide, refer to one of the following guides:

- If you want to install the software on a single system, then refer to [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm).
- If you want to install Oracle Grid Infrastructure for a standalone server, then refer to the [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/oraclerestart.htm#LADBI999).
- If you want to perform an Oracle Real Application Clusters installation, then refer to [Oracle Grid Infrastructure Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e41961/toc.htm) and [Oracle Real Application Clusters Installation Guide for Linux and UNIX](https://docs.oracle.com/cd/E11882_01/install.112/e41962/toc.htm). These guides describe how to install Oracle Clusterware and Oracle Real Application Clusters. Oracle clusterware is a prerequisite for Oracle Real Application Clusters installations.

All these guides are available on the product disc. To access them, use a web browser to open the `welcome.htm` file located in the top-level directory of the media. Platform-specific documentation is available in PDF and HTML formats in the Documentation section..

## 2 Logging In to the System as root

Before you install the Oracle software, you must complete several tasks as the `root` user. To log in as the `root` user, complete one of the following procedures:

Note:

You must install the software from an X Window System workstation, an X terminal, or a PC or other system with X server software installed.
- Following are the steps for installing the software from an X Window System workstation, or X terminal:
	1. Start a local terminal session, for example, an X terminal (`xterm`).
		2. If you are not installing the software on the local system, then enter the following command to enable the remote host to display X applications on the local X server:
		```
		$ xhost fully_qualified_remote_host_name
		```
		For example:
		```
		$ xhost somehost.us.example.com
		```
		3. If you are not installing the software on the local system, then use the `ssh`, `rlogin`, or `telnet` command to connect to the system where you want to install the software:
		```
		$ telnet fully_qualified_remote_host_name
		```
		4. If you are not logged in as the `root` user, then enter the following command to switch user to `root`:
		```
		$ sudo sh
		password:
		#
		```
- Following are the steps for installing the software from a PC or other system with X server software:
	Note:
	If necessary, refer to your X server documentation for more information about completing this procedure. Depending on the X server software that you are using, you may have to complete the tasks in a different order.
	1. Start the X server software.
		2. Configure the security settings of the X server software to permit remote hosts to display X applications on the local system.
		3. Connect to the remote system where you want to install the software and start a terminal session on that system, for example, an X terminal (`xterm`).
		4. If you are not logged in as the `root` user on the remote system, then enter the following command to switch user to `root`:
		```
		$ sudo sh
		password:
		#
		```

## 3 Checking the Hardware Requirements

The system must meet the following minimum hardware requirements:

- Memory Requirements
- Disk Space Requirements
- System Architecture
- Display Requirements

### 3.1 Memory Requirements

The following are the memory requirements for installing Oracle Database 11g Release 2 (11.2):

- Minimum: 1 GB of RAM
	Recommended: 2 GB of RAM or more
	To determine the RAM size, enter the following command:
	```
	# grep MemTotal /proc/meminfo
	```
	If the size of the RAM is less than the required size, then you must install more memory before continuing.
- The following table describes the relationship between installed RAM and the configured swap space recommendation:
	Note:
	On Linux, the HugePages feature allocates non-swappable memory for large page tables using memory-mapped files. If you enable HugePages, then you should deduct the memory allocated to HugePages from the available RAM before calculating swap space.
	| Available RAM | Swap Space Required |
	| --- | --- |
	| Between 1 GB and 2 GB | 1.5 times the size of the RAM |
	| Between 2 GB and 16 GB | Equal to the size of the RAM |
	| More than 16 GB | 16 GB |
- To determine whether the system architecture can run the software, enter the following command:
	```
	# uname -m
	```
	Note:
	This command displays the processor type. Verify that the processor architecture matches the Oracle software release to install. If you do not see the expected output, then you cannot install the software on this system.

To determine the size of the configured swap space, enter the following command:

```
# grep SwapTotal /proc/meminfo
```

If necessary, refer to the operating system documentation for information about how to configure additional swap space.

To determine the available RAM and swap space, enter the following command:

```
# free
```

Note:

- Oracle recommends that you take multiple values for the available RAM and swap space before finalizing a value. This is because the available RAM and swap space keep changing depending on the user interactions with the computer.
- Contact your operating system vendor for swap space allocation guidance for your server. The vendor guidelines supersede the swap space requirements listed in this guide.

Automatic Memory Management

Starting with Oracle Database 11g, the Automatic Memory Management feature requires more shared memory (`/dev/shm)` and file descriptors. The shared memory should be sized to be at least the greater of `MEMORY_MAX_TARGET` and `MEMORY_TARGET` for each Oracle instance on that computer.

To determine the amount of shared memory available, enter the following command:

```
# df -h /dev/shm/
```

Note:

`MEMORY_MAX_TARGET` and `MEMORY_TARGET` cannot be used when `LOCK_SGA` is enabled or with HugePages on Linux.

### 3.2 Disk Space Requirements

The following are the disk space requirements for installing Oracle Database 11g Release 2 (11.2):

- 1 GB of disk space in the `/tmp` directory.
	To determine the amount of disk space available in the `/tmp` directory, enter the following command:
	```
	# df -h /tmp
	```
	If there is less than 1 GB of free disk space available in the `/tmp` directory, then complete one of the following steps:
	- Delete unnecessary files from the `/tmp` directory to meet the disk space requirement.
		- Set the `TMP` and `TMPDIR` environment variables when setting the `oracle` user's environment.
		See Also:
		"Configuring the oracle User's Environment" for more information about setting `TMP` and `TMPDIR`
		- Extend the file system that contains the `/tmp` directory. If necessary, contact the system administrator for information about extending file systems.
- To determine the amount of free disk space on the system, enter the following command:
	```
	# df -h
	```
- The following tables describe the disk space requirements for software files, and data files for each installation type on Linux x86:
	| Installation Type | Requirement for Software Files (GB) |
	| --- | --- |
	| Enterprise Edition | 4.5 |
	| Standard Edition | 4.4 |
	| Installation Type | Requirement for Data Files (GB) |
	| --- | --- |
	| Enterprise Edition | 1.7 |
	| Standard Edition | 1.5 |
	Additional disk space, either on a file system or on an Oracle Automatic Storage Management disk group is required for the fast recovery area if you choose to configure automated backups.

### 3.3 System Architecture

To determine if the system architecture can run the software, enter the following command:

```
# uname -m
```

Verify that the processor architecture matches the Oracle software release to install. If you do not see the expected output, then you cannot install the software on this system

### 3.4 Display Requirements

The minimum resolution for Oracle Database 11g Release 2 (11.2) is 1024 x 768 or higher.

## 4 Checking the Software Requirements

Depending on the products that you intend to install, verify that the following software are installed on the system.

- Operating System Requirements
- Kernel Requirements
- Package Requirements
- Compiler Requirements
- Additional Software Requirements

Note:

Oracle Universal Installer (OUI) performs checks on the system to verify that it meets the listed requirements. To ensure that these checks pass, verify the requirements before you start Oracle Universal Installer.

### 4.1 Operating System Requirements

The following or later versions of the operating system are required for Oracle Database 11g Release 2 (11.2):

- Asianux Server 3 SP2
- Asianux Server 4 SP3
- Oracle Linux 4 Update 7
- Oracle Linux 5 Update 2
- Oracle Linux 6
- Red Hat Enterprise Linux 4 Update 7
- Red Hat Enterprise Linux 5 Update 2
- Red Hat Enterprise Linux 6
- SUSE Linux Enterprise Server 10 SP2
- SUSE Linux Enterprise Server 11

Starting with Oracle Database 11g Release 2 (11.2), the Security Enhanced Linux (SE Linux) feature is supported for Oracle Linux 4, Red Hat Enterprise Linux 4, Oracle Linux 5, and Red Hat Enterprise Linux 5.

Note:

For Asianux Server, Oracle Linux, and Red Hat Enterprise Linux, system requirements are identical by kernel version. Specifically:
- Oracle Linux 4 and Red Hat Enterprise Linux 4 requirements are the same.
- Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 requirements are the same.

To determine the distribution and version of Linux installed, enter the following command:

`# cat` `/proc/version`

Note:

Only the distributions and versions listed in the earlier list are supported. Do not install the software on other versions of Linux.

### 4.2 Kernel Requirements

The following are the Kernel requirements for Oracle Database 11g Release 2 (11.2):

- For Oracle Linux 4 and Red Hat Enterprise Linux 4:
	2.6.9 or later
- For Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5:
	2.6.18 or later
- For Oracle Linux 6:
	2.6.32.100 or later
- For Red Hat Enterprise Linux 6 and Asianux Server 4:
	2.6.32-71 or later
- For SUSE Linux Enterprise Server 10:
	2.6.16.21 or later
- On SUSE Linux Enterprise Server 11:
	2.6.27.19 or later

To determine whether the required kernel is installed, enter the following command:

```
# uname -r
```

The following is a sample output displayed by running this command on an Oracle Linux 5.0 system:

```
2.6.18-128.el5PAE
```

In this example, the output shows the kernel version (`2.6.18`) and errata level (`-128.el5PAE`) on the system.

If the kernel version does not meet the requirement specified earlier in this section, then contact the operating system vendor for information about obtaining and installing kernel updates.

### 4.3 Package Requirements

The following are the list of packages required for Oracle Database 11g Release 2 (11.2):

Note:

- Oracle recommends that you install your Linux operating system with the default software packages (RPMs), unless you specifically intend to perform a minimal installation, and follow the directions for performing such an installation to ensure that you have all required packages for Oracle software.
- Oracle recommends that you do not customize RPMs during a default operating system installation. A default installation includes most required packages, and helps you to limit manual checks of package dependencies.
- If you did not perform a default Linux installation, you intend to use LDAP, and you want to use the scripts `odisrvreg`, `oidca`, or `schemasync`, then install the Korn shell RPM for your Linux distribution.
- You must install the packages (or later versions) listed in the following table. Also, ensure that the list of RPMs and all the prerequisites for these RPMs are installed.

- The following or later version of packages for Oracle Linux 4 and Red Hat Enterprise Linux 4 should be installed:
	```
	binutils-2.15.92.0.2
	compat-libstdc++-33-3.2.3
	elfutils-libelf-0.97
	elfutils-libelf-devel-0.97
	gcc-3.4.6
	gcc-c++-3.4.6
	glibc-2.3.4-2.41
	glibc-common-2.3.4
	glibc-devel-2.3.4
	glibc-headers-2.3.4
	libaio-devel-0.3.105
	libaio-0.3.105
	libgcc-3.4.6
	libstdc++-3.4.6
	libstdc++-devel-3.4.6
	make-3.80
	numactl-0.6.4.i386
	pdksh-5.2.14
	sysstat-5.0.5
	```
- The following or later version of packages for Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 should be installed:
	```
	binutils-2.17.50.0.6
	compat-libstdc++-33-3.2.3
	elfutils-libelf-0.125
	elfutils-libelf-devel-0.125
	elfutils-libelf-devel-static-0.125
	gcc-4.1.2
	gcc-c++-4.1.2
	glibc-2.5-24
	glibc-common-2.5
	glibc-devel-2.5
	glibc-headers-2.5
	kernel-headers-2.6.18
	ksh-20060214
	libaio-0.3.106
	libaio-devel-0.3.106 
	libgcc-4.1.2
	libgomp-4.1.2
	libstdc++-4.1.2 
	libstdc++-devel-4.1.2
	make-3.81
	sysstat-7.0.2
	```
- The following or later version of packages for Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4 should be installed:
	```
	binutils-2.20.51.0.2-5.11.el6.i686
	compat-libcap1-1.10-1.i686
	compat-libstdc++-33-3.2.3-69.el6.i686
	gcc-4.4.4-13.el6.i686
	gcc-c++-4.4.4-13.el6.i686
	glibc-2.12-1.7.el6.i686
	glibc-devel-2.12-1.7.el6.i686
	ksh
	libgcc-4.4.4-13.el6.i686
	libstdc++-4.4.4-13.el6.i686
	libstdc++-devel-4.4.4-13.el6.i686
	libaio-0.3.107-10.el6.i686
	libaio-devel-0.3.107-10.el6.i686
	make-3.81-19.el6.i686
	sysstat-9.0.4-11.el6.i686
	```
- The following or later version of packages for SUSE Linux Enterprise Server 10 should be installed:
	```
	binutils-2.16.91.0.5
	compat-libstdc++-5.0.7
	gcc-4.1.2
	gcc-c++-4.1.2
	glibc-2.4-31.63
	glibc-devel-2.4-31.63
	ksh-93r-12.9
	libaio-0.3.104
	libaio-devel-0.3.104
	libelf-0.8.5
	libgcc-4.1.2
	libstdc++-4.1.2
	libstdc++-devel-4.1.2
	make-3.80
	sysstat-8.0.4
	```
- The following or later version of packages for SUSE Linux Enterprise Server 11 should be installed:
	```
	binutils-2.19
	gcc-4.3
	gcc-c++-4.3
	glibc-2.9
	glibc-devel-2.9
	ksh-93t
	libstdc++33-3.3.3
	libstdc++43-4.3.3_20081022
	libstdc++43-devel-4.3.3_20081022
	libaio-0.3.104
	libaio-devel-0.3.104
	libgcc43-4.3.3_20081022
	libstdc++-devel-4.3
	make-3.81
	sysstat-8.1.5
	```

Note:

- The `kernel-headers-2.6.18` package is not mandatory for database installations on Linux x86. You can ignore the OUI or Cluster Verification Utility (CVU) warning to install this package.
- The `numa` package link for Linux x86 is `/usr/lib`.

To determine whether the required packages are installed, enter commands similar to the following:

```
# rpm -q package_name
```

If a package is not installed, then install it from the Linux distribution media or download the required package version from the Linux vendor's website.

### 4.4 Compiler Requirements

The following are the compiler requirements for Pro\*C/C++, Oracle Call Interface, Oracle C++ Call Interface, and Oracle XML Developer's Kit (XDK) with Oracle Database 11g Release 2 (11.2):

Intel C++ Compiler 10.1 or later and the version of GNU C and C++ compilers listed under "Package Requirements" are supported with these products.

Note:

Intel Compiler v10.1 can be used only with the standard template libraries of the gcc versions mentioned in "Package Requirements", to build Oracle C++ Call Interface (OCCI) applications.

Oracle XML Developer's Kit is supported with the same compilers as OCCI.

### 4.5 Additional Software Requirements

Depending on the components you want to use, you must ensure that the following software are installed:

- Oracle ODBC Drivers
- Oracle JDBC/OCI Drivers
- Linux-PAM Library
- Oracle Messaging Gateway
- Programming Languages
- Browser Requirements

#### 4.5.1 Oracle ODBC Drivers

You should install ODBC Driver Manager for UNIX. You can download and install the Driver Manager from the following URL:

`http://www.unixodbc.org`

To use ODBC, you must also install the following additional 32-bit ODBC RPMs, depending on your operating system:

- On Oracle Linux 4 and Red Hat Enterprise Linux 4:
	- `unixODBC-2.2.11 (32-bit)` or later
		- `unixODBC-devel-2.2.11 (32-bit)` or later
- On Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5:
	- `unixODBC-2.2.11 (32-bit)` or later
		- `unixODBC-devel-2.2.11 (32-bit)` or later
- On Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4:
	```
	unixODBC-2.2.14-11.el6.i686 or later
	unixODBC-devel-2.2.14-11.el6.i686 or later
	```
- On SUSE Linux Enterprise Server 10:
	- `unixODBC-32bit-2.2.11 (32-bit)` or later
		- `unixODBC-devel-32bit-2.2.11 (32-bit)` or later
- On SUSE Linux Enterprise Server 11:
	- `unixODBC-32bit-2.2.12 (32-bit)` or later
		- `unixODBC-devel-32bit-2.2.12 (32-bit)` or later

#### 4.5.2 Oracle JDBC/OCI Drivers

Use JDK 6 (Java SE Development Kit `1.6.0_21`) or JDK 5 (`1.5.0_24`) with the JNDI extension with the Oracle Java Database Connectivity and Oracle Call Interface drivers. However, these are not mandatory for the database installation. `IBM JDK 1.5` is installed with this release.

#### 4.5.3 Linux-PAM Library

Install the latest Linux-PAM (Pluggable Authentication Modules for Linux) library to enable the system administrator to choose how applications authenticate users.

#### 4.5.4 Oracle Messaging Gateway

Oracle Messaging Gateway supports the integration of Oracle Streams Advanced Queuing (AQ) with the following software:

- IBM WebSphere MQ V7.0, client and server:
	```
	MQSeriesClient
	MQSeriesServer
	MQSeriesRuntime
	```
- TIBCO Rendezvous 7.3

If you require a CSD for WebSphere MQ, then refer to the following website for download and installation information:

`http://www-947.ibm.com/support/entry/portal/Downloads/Software/WebSphere/WebSphere_MQ`

#### 4.5.5 Programming Languages

The following products are certified for use with:

- Pro\* COBOL
	Micro Focus Server Express 5.1

#### 4.5.6 Browser Requirements

You do not require a web browser to install Oracle Database. However, browsers are required to access documentation, and if you intend to use Oracle Enterprise Manager Database Control and Oracle Application Express. Web browsers must support JavaScript, and the HTML 4.0 and CSS 1.0 standards.

Oracle Enterprise Manager Database Control supports the following browsers:

- Microsoft Internet Explorer 10.0 (supports Oracle Enterprise Manager Database Control 11.2.0.3 and higher)
- Microsoft Internet Explorer 9.0
- Microsoft Internet Explorer 8.0
- Microsoft Internet Explorer 7.0 SP1
- Microsoft Internet Explorer 6.0 SP2
- Firefox 21.0 (supports Oracle Enterprise Manager Database Control 11.2.0.4)
- Firefox 17.0.6 ESR (supports Oracle Enterprise Manager Database Control 11.2.0.4)
- Firefox 3.6
- Firefox 3.5
- Firefox 3.0.7
- Firefox 2.0
- Safari 4.0.x
- Safari 3.2
- Safari 3.1
- Google Chrome 27.0 (supports Oracle Enterprise Manager Database Control 11.2.0.4)
- Google Chrome 4.0
- Google Chrome 3.0
- Netscape Navigator 9.0
- Netscape Navigator 8.1

See Also:

[Oracle Application Express Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e12196/pre_require.htm#HTMIG380)

## 5 Creating Required Operating System Groups and Users

The following local operating system groups and users are required if you are installing Oracle Database:

- The Oracle Inventory group (typically, `oinstall`)
- The OSDBA group (typically, `dba`)
- The Oracle software owner (typically, `oracle`)
- The OSOPER group (optional. Typically, `oper`)

To determine whether these groups and users exist, and if necessary, to create them, follow these steps:

1. To determine whether the `oinstall` group exists, enter the following command:
	```
	# more /etc/oraInst.loc
	```
	If the output of this command shows the `oinstall` group name, then the group exists.
	If the `oraInst.loc` file exists, then the output from this command is similar to the following:
	```
	inventory_loc=/u01/app/oraInventory
	inst_group=oinstall
	```
	The `inst_group` parameter shows the name of the Oracle Inventory group, `oinstall`.
2. To determine whether the `dba` group exists, enter the following command:
	```
	# grep dba /etc/group
	```
	If the output from this commands shows the `dba` group name, then the group exists.
3. If necessary, enter the following commands to create the `oinstall` and `dba` groups:
	```
	# /usr/sbin/groupadd oinstall
	# /usr/sbin/groupadd dba
	```
4. To determine whether the `oracle` user exists and belongs to the correct groups, enter the following command:
	```
	# id oracle
	```
	If the `oracle` user exists, then this command displays information about the groups to which the user belongs. The output should be similar to the following, indicating that `oinstall` is the primary group and `dba` is a secondary group:
	```
	uid=440(oracle) gid=200(oinstall) groups=201(dba),202(oper)
	```
5. If necessary, complete one of the following actions:
	- If the `oracle` user exists, but its primary group is not `oinstall` or it is not a member of the `dba` group, then enter the following command:
		```
		# /usr/sbin/usermod -g oinstall -G dba oracle
		```
		- If the `oracle` user does not exist, enter the following command to create it:
		```
		# /usr/sbin/useradd -g oinstall -G dba oracle
		```
		This command creates the `oracle` user and specifies `oinstall` as the primary group and `dba` as the secondary group.
6. Enter the following command to set the password of the `oracle` user:
	```
	# passwd oracle
	```

## 6 Configuring Kernel Parameters and Resource Limits

Verify that the kernel parameters shown in the following table are set to values greater than or equal to the minimum value shown. The procedure following the table describes how to verify and set the values.

Note:

The kernel parameter and shell limit values in this section are minimum values only. For production database systems, Oracle recommends that you tune these values to optimize the performance of the system. Refer to your operating system documentation for more information about tuning kernel parameters.

| Parameter | Minimum Value | File |
| --- | --- | --- |
| `semmsl`  `semmns`  `semopm`  `semmni` | 250  32000  100  128 | `/proc/sys/kernel/sem` |
| `shmall` | 2097152 | `/proc/sys/kernel/shmall` |
| `shmmax` | Minimum: 536870912  Maximum: A value that is 1 byte less than 4 GB, or 4294967295  Recommended: More than half the physical memory  See My Oracle Support Note 567506.1 for additional information about configuring `shmmax`. | `/proc/sys/kernel/shmmax` |
| `shmmni` | 4096 | `/proc/sys/kernel/shmmni` |
| `file` - `max` | 6815744 | `/proc/sys/fs/file-max` |
| `ip_local_port_range` | Minimum: 9000  Maximum: 65500 | `/proc/sys/net/ipv4/ip_local_port_range` |
| `rmem_default` | 262144 | `/proc/sys/net/core/rmem_default` |
| `rmem_max` | 4194304 | `/proc/sys/net/core/rmem_max` |
| `wmem_default` | 262144 | `/proc/sys/net/core/wmem_default` |
| `wmem_max` | 1048576 | `/proc/sys/net/core/wmem_max` |
| `aio-max-nr` | 1048576  Note: This value limits concurrent outstanding requests and should be set to avoid I/O subsystem failures. | `/proc/sys/fs/aio-max-nr` |

Note:

If the current value of any parameter is higher than the value listed in this table, then do not change the value of that parameter.

To view the current value specified for these kernel parameters and to change them if necessary:

- Enter commands similar to the following to view the current values of the kernel parameters:
	Note:
	Make a note of the current values and identify any values that you must change.
	| Parameter | Command |
	| --- | --- |
	| `semmsl`, `semmns`, `semopm`, and `semmni` | `# /sbin/sysctl -a \| grep sem`  This command displays the value of the semaphore parameters in the order listed. |
	| `shmall`, `shmmax`, and `shmmni` | `# /sbin/sysctl -a \| grep shm` |
	| `file-max` | `# /sbin/sysctl -a \| grep file-max` |
	| `ip_local_port_range` | `# /sbin/sysctl -a \| grep ip_local_port_range` |
	| `rmem_default` | `# /sbin/sysctl -a \| grep rmem_default` |
	| `rmem_max` | `# /sbin/sysctl -a \| grep rmem_max` |
	| `wmem_default` | `# /sbin/sysctl -a \| grep wmem_default` |
	| `wmem_max` | `# /sbin/sysctl -a \| grep wmem_max` |
- If the value of any kernel parameter is different from the recommended value, then complete the following steps:
	1. Using any text editor, create or edit the `/etc/sysctl.conf` file, and add or edit lines similar to the following:
		Note:
		Include lines only for the kernel parameter values to change. For the semaphore parameters (`kernel.sem`), you must specify all four values. However, if any of the current values are larger than the minimum value, then specify the larger value.
		```
		fs.aio-max-nr = 1048576
		fs.file-max = 6815744
		kernel.shmall = 2097152
		kernel.shmmax = 536870912
		kernel.shmmni = 4096
		kernel.sem = 250 32000 100 128
		net.ipv4.ip_local_port_range = 9000 65500
		net.core.rmem_default = 262144
		net.core.rmem_max = 4194304
		net.core.wmem_default = 262144
		net.core.wmem_max = 1048576
		```
		By specifying the values in the `/etc/sysctl.conf` file, they persist when you restart the system. However, on SUSE Linux Enterprise Server systems, enter the following command to ensure that the system reads the `/etc/sysctl.conf` file when it restarts:
		```
		# /sbin/chkconfig boot.sysctl on
		```
		2. Enter the following command to change the current values of the kernel parameters:
		```
		# /sbin/sysctl -p
		```
		Review the output from this command to verify that the values are correct. If the values are incorrect, edit the /etc/sysctl.conf file, then enter this command again.
		3. Enter the command `/sbin/sysctl -a` to confirm that the values are set correctly.
		4. On SUSE Linux Enterprise Server systems only, enter the following command to cause the system to read the `/etc/sysctl.conf` file when it restarts:
		```
		# /sbin/chkconfig boot.sysctl on
		```
		5. On SUSE Linux Enterprise Server systems only, you must enter the GID of the oinstall group as the value for the parameter `/proc/sys/vm/hugetlb_shm_group`. Doing this grants members of oinstall a group permission to create shared memory segments.
		For example, where the oinstall group GID is 501:
		```
		# echo 501 > /proc/sys/vm/hugetlb_shm_group
		```
		After running this command, use `vi` to add the following text to `/etc/sysctl.conf`, and enable the `boot.sysctl` script to run on system restart:
		```
		vm.hugetlb_shm_group=501
		```
		Note:
		Only one group can be defined as the `vm.hugetlb_shm_group`.
		6. After updating the values of kernel parameters in the `/etc/sysctl.conf` file, either restart the computer, or run the command `sysctl -p` to make the changes in the `/etc/sysctl.conf` file available in the active kernel memory.

Check Resource Limits for the Oracle Software Installation Users

For each installation software owner, check the resource limits for installation, using the following recommended ranges:

Table 1 Installation Owner Resource Limit Recommended Ranges

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
	4096
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

If necessary, update the resource limits in the `/etc/security/limits.conf` configuration file for the installation owner. However, note that the configuration file is distribution specific. Contact your system administrator for distribution specific configuration file information.

Note:

If the `grid` or `oracle` users are logged in, then changes in the limits.conf file do not take effect until you log these users out and log them back in. You must do this before you use these accounts for installation.

## 7 Creating Required Directories

Create directories with names similar to the following, and specify the correct owner, group, and permissions for them:

- The Oracle base directory
- An optional Oracle data file directory

The Oracle base directory must have 4 GB of free disk space, or 6 GB of free disk space if you choose not to create a separate Oracle data file directory.

Note:

If you do not want to create a separate Oracle data file directory, then you can install the data files in a subdirectory of the Oracle base directory. However, this is not recommended for production databases.

To create the Oracle base directory:

1. Enter the following command to display information about all mounted file systems:
	```
	# df -h
	```
	This command displays information about all the file systems mounted on the system, including:
	- The physical device name
		- The total amount, used amount, and available amount of disk space
		- The mount point directory for that file system
2. From the display, identify either one or two file systems that meet the disk space requirements mentioned earlier in this section.
3. Note the name of the mount point directory for each file system that you identified.
4. Enter commands similar to the following to create the recommended subdirectories in the mount point directory that you identified and set the appropriate owner, group, and permissions on them:
	```
	# mkdir -p /mount_point
	/app/
	# chown -R oracle:oinstall /mount_point/app/
	# chmod -R 775 /mount_point
	/app/
	```
	For example:
	```
	# mkdir -p /u01/app/
	# chown -R oracle:oinstall /u01/app/
	# chmod -R 775 /u01/app/
	```

## 8 Configuring the oracle User's Environment

You run Oracle Universal Installer from the `oracle` account. However, before you start Oracle Universal Installer, you must configure the environment of the `oracle` user. To configure the environment, you must:

- Set the default file mode creation mask (`umask`) to `022` in the shell startup file.
- Set the `DISPLAY` environment variable.

To set the `oracle` user's environment:

1. Start a new terminal session, for example, an X terminal (`xterm`).
2. Enter the following command to ensure that X Window applications can display on this system:
	```
	$ xhost fully_qualified_remote_host_name
	```
	For example:
	```
	$ xhost somehost.us.example.com
	```
3. If you are not logged in to the system where you want to install the software, then log in to that system as the `oracle` user.
4. If you are not logged in as the `oracle` user, then switch user to `oracle`:
	```
	$ su - oracle
	```
5. To determine the default shell for the `oracle` user, enter the following command:
	```
	$ echo $SHELL
	```
6. To run the shell startup script, enter one of the following commands:
	- Bash shell:
		```
		$ . ./.bash_profile
		```
		- Bourne or Korn shell:
		```
		$ . ./.profile
		```
		- C shell:
		```
		% source ./.login
		```
7. If you are not installing the software on the local computer, then run the following command on the remote computer to set the `DISPLAY` variable:
	- Bourne, Bash or Korn shell:
		```
		$ export DISPLAY=local_host:0.0
		```
		- C shell:
		```
		% setenv DISPLAY local_host:0.0
		```
	In this example, `local_host` is the host name or IP address of the local computer to use to display Oracle Universal Installer.
	Run the following command on the remote computer to check if the shell and the DISPLAY environmental variable are set correctly:
	```
	echo $SHELL
	echo $DISPLAY
	```
	Now to enable X applications, run the following commands on the local computer:
	```
	$ xhost + fully_qualified_remote_host_name
	```
	To verify that X applications display is set properly, run a X11 based program that comes with the operating system such as `xclock`:
	```
	$ xclock
	```
	In this example, you can find `xclock` at `/usr/X11R6/bin/xclocks`. If the `DISPLAY` variable is set properly, then you can see `xclock` on your computer screen.
	See Also:
	PC-X Server or operating system vendor documents for further assistance
8. If you determined that the `/tmp` directory has less than 1 GB of free disk space, then identify a file system with at least 1 GB of free space and set the `TMP` and `TMPDIR` environment variables to specify a temporary directory on this file system:
	1. To determine the free disk space on each mounted file system use the following command:
		```
		# df -h /tmp
		```
		2. If necessary, enter commands similar to the following to create a temporary directory on the file system that you identified, and set the appropriate permissions on the directory:
		```
		$ sudo mkdir /mount_point/tmp
		$ sudo chmod a+wr /mount_point/tmp
		# exit
		```
		3. Enter commands similar to the following to set the `TMP` and `TMPDIR` environment variables:
		- Bourne, Bash, or Korn shell:
			```
			$ TMP=/mount_point/tmp
			$ TMPDIR=/mount_point/tmp
			$ export TMP TMPDIR
			```
				- C shell:
			```
			% setenv TMP /mount_point/tmp
			% setenv TMPDIR /mount_point/tmp
			```
9. Enter commands similar to the following to set the `ORACLE_BASE` `and ORACLE_SID` environment variables:
	- Bourne, Bash, or Korn shell:
		```
		$ ORACLE_BASE=/u01/app/oracle
		$ ORACLE_SID=sales
		$ export ORACLE_BASE ORACLE_SID
		```
		- C shell:
		```
		% setenv ORACLE_BASE /u01/app/oracle
		% setenv ORACLE_SID sales
		```
	In this example, `/u01/app/oracle` is the Oracle base directory that you created or identified earlier and `sales` is the database name (typically no more than five characters).
10. Enter the following commands to ensure that the `ORACLE_HOME` and `TNS_ADMIN` environment variables are not set:
	- Bourne, Bash, or Korn shell:
		```
		$ unset ORACLE_HOME
		$ unset TNS_ADMIN
		```
		- C shell:
		```
		% unsetenv ORACLE_HOME
		% unsetenv TNS_ADMIN
		```
	Note:
	If the `ORACLE_HOME` environment variable is set, then Oracle Universal Installer uses the value that it specifies as the default path for the Oracle home directory. However, if you set the `ORACLE_BASE` environment variable, then Oracle recommends that you unset the `ORACLE_HOME` environment variable and choose the default path suggested by Oracle Universal Installer.

## 9 Mounting the Product Disc

On most Linux systems, the product disc mounts automatically when you insert it into the drive. If the disc does not mount automatically, then follow these steps to mount it:

1. Enter a command similar to the following to eject the currently mounted disc, then remove it from the drive:
	- Asianux, Oracle Linux, and Red Hat Enterprise Linux:
		```
		$ sudo eject /mnt/dvd
		```
		- SUSE Linux Enterprise Server:
		```
		# eject /media/dvd
		```
	In these examples, `/mnt/dvd` and `/media/dvd` are the mount point directories for the disc drive.
2. Insert the DVD into the disc drive.
3. To verify that the disc mounted automatically, enter a command similar to the following:
	- Asianux, Oracle Linux, and Red Hat Enterprise Linux:
		```
		# ls /mnt/dvd
		```
		- SUSE Linux Enterprise Server:
		```
		# ls /media/dvd
		```
4. If this command fails to display the contents of the disc, then enter a command similar to the following:
	- Asianux, Oracle Linux, and Red Hat Enterprise Linux:
		```
		# mount -t iso9660 /dev/dvd /mnt/dvd
		```
		- SUSE Linux Enterprise Server:
		```
		# mount -t iso9660 /dev/dvd /media/dvd
		```
	In these examples, `/mnt/dvd` and `/media/dvd` are the mount point directories for the disc drive.

## 10 Installing Oracle Database

After configuring the `oracle` user's environment, start Oracle Universal Installer and install Oracle Database as follows:

1. To start Oracle Universal Installer, enter the following command:
	```
	$ /mount_point/db/runInstaller
	```
	If Oracle Universal Installer does not start, then refer to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about how to troubleshoot X Window display problems.
2. The following table describes the recommended action for each Oracle Universal Installer screen. Use the following guidelines to complete the installation:
	- If you need more assistance, or if you want to choose an option that is not a default, then click Help for additional information.
		- If you encounter errors while installing or linking the software, then refer to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about troubleshooting.
	Note:
	If you have completed the tasks listed previously, then you can complete the installation by choosing the default values on most screens.
	| Screen | Recommended Action |
	| --- | --- |
	| Configure Security Updates | Enter your e-mail address, preferably your My Oracle Support e-mail address or user name in the Email field.  You can select the I wish to receive security updates via My Oracle Support check box to receive security updates.  Enter your My Oracle Support password in the My Oracle Support Password field.  Click Next. |
	| Download Software Updates | Starting with Oracle Database 11g Release 2 (11.2.0.2), you can use the Software Updates feature to dynamically download and apply latest updates. Select one of the following options and click Next: - Use My Oracle Support credentials for download: Select this option to download and apply the latest software updates. 	Click Proxy Settings to configure a proxy for Oracle Universal Installer to use to connect to the Internet. Provide the proxy server information for your site, along with a user account that has access to the local area network through which the server is connecting. Starting with Oracle Database 11g Release 2 (11.2.0.3), you can enter the Proxy Realm information if required. The proxy realm information is case-sensitive. 	Click Test Connection to ensure that your proxy settings are correctly entered, and the installer can download the updates. - Use pre-downloaded software updates: Select this option to apply previously downloaded software updates. - Skip Software Updates: Select this option if you do not want to apply any updates. |
	| Apply Software Updates | This screen is displayed if you select to download the software updates or provide the pre-downloaded software downloads location.  If you selected Use My Oracle Support credentials for download in the previous screen, select Download and apply all updates, and then click Next.  If you selected Use pre-downloaded software updates in the previous screen, select Apply all updates, and then click Next. |
	| Select Installation Option | Select Create and configure a database from the following list of available options, then click Next: - Create and configure a database - Install database software only - Upgrade an existing database |
	| System Class | Select Server Class from the following options to install the database, and click Next. - Desktop Class: Choose this option if you are installing on a laptop or desktop class system. - Server Class: Choose this option if you are installing on a server class system, such as what you would use when deploying Oracle in a production data center. |
	| Grid Installation Options | Select Single instance database installation for the type of database installation you want to perform, and click Next. - Single instance database installation: This option installs the database and the listener. - Real Application Clusters database installation: This option installs Oracle Real Application Clusters. - Oracle RAC One Node database installation: This option installs the Oracle RAC One Node database. 	Note: Oracle RAC One Node is supported only with Oracle Clusterware. |
	| Select Install Type | Select Typical Install as the installation type from the following options, and click Next: - Typical Install: This installation method is selected by default. It lets you quickly install Oracle Database using minimal input. - Advanced Install: This installation method enables to perform more complex installations. |
	| Typical Install Configuration | Enter the following information according to your requirements:  Oracle base: The Oracle base path appears by default. You can change the path based on your requirement.  Software location: In the Software Location section, accept the default value or enter the Oracle home directory path in which you want to install Oracle components. The directory path should not contain spaces.  Storage Type: Select File System, or Oracle Automatic Storage Management as the database storage option.  Database file location: If you select File System as your storage type, then click Browse and specify a database file location.  ASMSNMP Password: If you select Oracle Automatic Storage Management as your Storage Type, then specify the password for the ASMSNMP user.  Database edition: Select the database edition to install.  OSDBA Group: The OSDBA group is selected by default. You can also select the OSDBA group from the list.  Global database name: Specify the Global Database Name using the following syntax:  ``` database_name.domain ```  For example, `sales.us.example.com`  Administrative password: Enter the password for the privileged database account.  Confirm Password: Reenter, and confirm the password for the privileged database account.  Click Next to continue. |
	| Create Inventory | This screen is displayed only during the first installation of Oracle products on a system.  Specify the full path of the Oracle Inventory directory. Ensure that the operating system group selected is `oinstall`. Click Next to continue. |
	| Perform Prerequisite Checks | Verify that all the prerequisite checks succeed, and then click Next.  Oracle Universal Installer checks the system to verify that it is configured correctly to run Oracle software. If you have completed all the preinstallation steps in this guide, all the checks should pass.  If a check fails, then review the cause of the failure listed for that check on the screen. If possible, rectify the problem and rerun the check. Alternatively, if you are satisfied that your system meets the requirements, then you can select the check box for the failed check to manually verify the requirement.  Note: Oracle recommends that you use caution in checking the Ignore All option. If you check this option, then Oracle Universal Installer may not confirm if your system can install Oracle Database successfully. |
	| Summary | Review the information displayed on this screen, and then click Install.  Note: Starting with Oracle Database 11g Release 2 (11.2), you can save all the installation steps into a response file by clicking Save Response File. Later, this file can be used for a silent installation. |
	| Install Product | This screen states the progress of a database installation. After the database is installed, you are prompted to execute some root configuration script for new inventory as the `root` user. Click Next.  This screen then displays the status information for the configuration assistants that configure the software and create a database.  Finally, a message is displayed at the end of Database Configuration Assistant process, and click OK.  Execute the `root.sh` script as the `root` user to complete the installation and click OK. |
	| Finish | This screen is shown automatically when all the configuration tools are successful.  Click Close. |

## 11 Installing Oracle Database Examples

If you plan to use the following products or features, then download and install the products from the Oracle Database Examples media:

- Oracle JDBC Development Drivers
- Oracle Database Examples
- Various Oracle product demonstrations

For information about installing software and various Oracle product demonstrations from the Oracle Database Examples media, refer to [Oracle Database Examples Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e24501/toc.htm).

## 12 What to Do Next?

To become familiar with this release of Oracle Database, it is recommended that you complete the following tasks:

- Log in to Oracle Enterprise Manager Database Control using a web browser.
	Oracle Enterprise Manager Database Control is a web-based application that you can use to manage a single Oracle Database installation. The default URL for Database Control is similar to the following:
	```
	http://host.domain:1158/em/
	```
	To log in, use the user name `SYS` and connect as `SYSDBA`. Use the password that you specified for this user during the Oracle Database 11g installation.
- Refer to [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm) for information about required and optional postinstallation tasks, depending on the products to use.
- Refer to [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm) for information about how to use Database Control to learn about the configuration of your installed database.
- To learn more about using Oracle Enterprise Manager Database Control to administer a database, refer to [Oracle Database 2 Day DBA](https://docs.oracle.com/cd/E11882_01/server.112/e10897/toc.htm).
	This guide, designed for new Oracle DBAs, describes how to use Database Control to manage all aspects of an Oracle Database installation. It also provides information about how to enable e-mail notifications and automated backups, which you might not have configured during the installation.

## 13 Additional Information

This section contains information about the following:

- Product Licenses
- Purchasing Licenses and Version Updates
- Contacting Oracle Support Services
- Locating Product Documentation

Product Licenses

You are welcome to install and evaluate the products included in this media pack for 30 days under the terms of the Trial License Agreement. However, you must purchase a program license if you want to continue using any product after the 30 day evaluation period. See the following section for information about purchasing program licenses.

Purchasing Licenses and Version Updates

You can purchase program licenses and updated versions of Oracle products from the Oracle Store website:

`https://shop.oracle.com`

Contacting Oracle Support Services

If you have purchased Oracle Product Support, you can call Oracle Support Services for assistance 24 hours a day, seven days a week. For information about purchasing Oracle Product Support or contacting Oracle Support Services, go to the Oracle Support Services website:

`http://www.oracle.com/us/support/index.html`

Locating Product Documentation

Product documentation includes information about configuring, using, or administering Oracle products on any platform. The product documentation for Oracle Database products is available in both HTML and PDF formats online on the Oracle Technology Network (OTN) website:

`http://www.oracle.com/technetwork/indexes/documentation/index.html`

## 14 Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers that have purchased support have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

---

Oracle Database Quick Installation Guide, 11g Release 2 (11.2) for Linux x86

E24324-06

Copyright © 2015, Oracle and/or its affiliates. All rights reserved.

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, then the following notice is applicable:

U.S. GOVERNMENT END USERS: Oracle programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, delivered to U.S. Government end users are "commercial computer software" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, use, duplication, disclosure, modification, and adaptation of the programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, shall be subject to license terms and license restrictions applicable to the programs. No other rights are granted to the U.S. Government.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Xeon are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Opteron, the AMD logo, and the AMD Opteron logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information about content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services unless otherwise set forth in an applicable agreement between you and Oracle. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services, except as set forth in an applicable agreement between you and Oracle.