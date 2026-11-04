---
title: Oracle Database Client Preinstallation Tasks
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/pre_install.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## 2 Oracle Database Client Preinstallation Tasks

This guide contains information required to install Oracle Database Client 11g Release 2 (11.2). Ensure that you review information related to the platform on which you intend to install Oracle Database Client.

This chapter describes the tasks that you must complete before you start Oracle Universal Installer. It includes information about the following tasks:

## 2.1 Logging In to the System as root

Before you install the Oracle software, you must complete several tasks as the `root` user. To log in as the `root` user, complete one of the following procedures:

Note:

Unless you intend to complete a silent-mode installation, you must install the software from an X Window System workstation, an X terminal, or a PC or other system with X server software installed.

For more information about silent-mode installations, refer to [Appendix A](app_nonint.md).

- If you are installing the software from an X Window System workstation or X terminal, then:
	1. Start a local terminal session, for example, an X terminal (`xterm`).
		2. If you are not installing the software on the local system, then enter the following command to enable the remote host to display X applications on the local X server:
		```
		$ xhost fully_qualified_remote_host_name
		```
		For example:
		```
		$ xhost somehost.example.com
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
- If you are installing the software from a PC or other system with X server software installed, then:
	Note:
	If necessary, refer to the X server documentation, or contact your X server vendor or system administrator for more information about completing this procedure. Depending on the X server software that you are using, you may have to complete the tasks in a different order.
	1. Start the X server software.
		2. Configure the security settings of the X server software to permit remote hosts to display X applications on the local system.
		3. Connect to the remote system where you want to install the software and start a terminal session on that system, for example, an X terminal (`xterm`).
		4. If you are not logged in as the `root` user on the remote system, then enter the following command to switch user to `root`:
		```
		$ sudo sh
		password:
		#
		```

## 2.2 Checking the Hardware Requirements

The system must meet the following minimum hardware requirements for Oracle Database Client 11g Release 2:

- Memory Requirements
- System Architecture
- Disk Space Requirements
- Display Requirements
- Recommended Hardware Requirement for SQL Developer

### 2.2.1 Memory Requirements

The following are the memory requirements for Oracle Database Client 11g Release 2 (11.2):

- At least 256 MB of RAM.
	To determine the RAM size, enter the following command:
	```
	# grep MemTotal /proc/meminfo
	```
	If the size of the RAM is less than the required size, then you must install more memory before you continue with the installation.
- The following table describes the relationship between installed RAM and the configured swap space recommendation:
	Note:
	On Linux, the HugePages feature allocates non-swappable memory for large page tables using memory-mapped files. If you enable HugePages, then you should deduct the memory allocated to HugePages from the available RAM before calculating swap space.
	| RAM | Swap Space |
	| --- | --- |
	| 256 MB | 3 times the size of RAM |
	| Between 256 MB and 512 MB | 2 times the size of RAM |
	| Between 512 MB and 2 GB | 1.5 times the size of RAM |
	| Between 2 GB and 16 GB | Equal to the size of RAM |
	| More than 16 GB | 16 GB |

To determine the size of the configured swap space, enter the following command:

```
# grep SwapTotal /proc/meminfo
```

If necessary, refer to the operating system documentation for information about how to configure additional swap space.

To determine the available RAM and swap space, enter the following command:

```
# free
```

IMPORTANT:

- Oracle recommends that you take multiple values for the available RAM and swap space before finalizing on a value. This is because the available RAM and swap space keep changing depending on the user interactions with the computer.
- Contact your operating system vendor for swap space allocation guidance for your server. The vendor guidelines supersede the swap space requirements listed in this guide.

### 2.2.2 System Architecture

To determine whether the system architecture can run the software, enter the following command:

```
# uname -m
```

Note:

Verify that the processor architecture matches the Oracle software release to install. If you do not see the expected output, then you cannot install the software on this system.

### 2.2.3 Disk Space Requirements

The following are the disk space requirements for Oracle Database Client 11g Release 2 (11.2):

- The minimum disk space requirement for a client install in the `/tmp` directory is 400 MB.
	To determine the amount of space available in the `/tmp` directory, enter the following command:
	```
	# df -k /tmp
	```
	If there is less than 400 MB of free space available in the `/tmp` directory, then complete one of the following steps:
	- Delete unnecessary files from the `/tmp` directory to meet the space requirement.
		- Set the `TMP` and `TMPDIR` environment variables when setting the `oracle` user's environment.
		See Also:
		"Configuring Oracle Software Owner Environment" for more information about setting `TMP` and `TMPDIR`
		- Extend the file system that contains the `/tmp` directory. If necessary, contact the system administrator for information about extending file systems.
- The following table describes the disk space requirements for software files for each installation type on Linux:
	| Installation Type | Requirement for Software Files |
	| --- | --- |
	| Instant Client | 221 MB |
	| Administrator | 1.5 GB |
	| Runtime | 1.1 GB |
	| Custom (maximum) | 1.5 GB |
- To determine the amount of free disk space available, enter the following command:
	```
	# df -k
	```

### 2.2.4 Display Requirements

The minimum display requirement for Oracle Database 11g Release 2 (11.2) is a resolution of 1024 x 768 or higher.

### 2.2.5 Recommended Hardware Requirement for SQL Developer

The following are the recommended CPU, Memory and Display requirements for SQL Developer.

| Resource | Recommended |
| --- | --- |
| Memory | 1 GB RAM (recommended), 256 MB RAM (min) |
| Display | 65536 colors, set to at least 1024 X 768 resolution |

## 2.3 Checking the Software Requirements

Depending on the products that you intend to install, verify that the following softwares are installed on the system.

Note:

Oracle Universal Installer performs checks on the system to verify that it meets the listed requirements. To ensure that these checks pass, verify the requirements before you start Oracle Universal Installer.
- Operating System Requirements
- Kernel Requirements
- Package Requirements
- Compiler Requirements
- Additional Software Requirements
- Instant Client Light Requirements

Note:

The platform-specific hardware and software requirements included in this guide were current when this guide was published. However, because new platforms and operating system software versions might be certified after this guide is published, review the certification matrix on the My Oracle Support website for the most up-to-date list of certified hardware platforms and operating system versions:

`https://support.oracle.com/`

### 2.3.1 Operating System Requirements

The following or later versions of the operating system are required for Oracle Database Client 11g Release 2 (11.2):

Note:

- Starting with Oracle Database 11g Release 2 (11.2.0.4), Oracle Linux 7 and Red Hat Enterprise Linux 7 are supported on Linux x86-64.
- Starting with Oracle Database 11g Release 2 (11.2.0.3), Oracle Linux 6 and Red Hat Enterprise Linux 6 are supported on Linux x86 and Linux x86-64.
- Starting with Oracle Database 11g Release 2 (11.2.0.3), Asianux 4 is supported on Linux x86 and Linux x86-64.
- Starting with Oracle Database 11g Release 2 (11.2.0.4), SUSE Linux Enterprise Server 12 is certified on Linux x86-64 systems.
- Starting with Oracle Database 11g Release 2 (11.2.0.4), NeoKylin Linux Advanced Server 6 is certified on Linux x86-64 systems.
- Starting with Oracle Database 11g Release 2 (11.2.0.4), NeoKylin Linux Advanced Server 7 is certified on Linux x86-64 systems.
- Starting with Oracle Database 11g Release 2 (11.2.0.4), Red Hat Enterprise Linux 7 is supported on IBM: Linux on System z.

- On Linux x86
	- Oracle Linux 4 Update 7
		- Oracle Linux 5 Update 2
		- Oracle Linux 6
		- Red Hat Enterprise Linux 4 Update 7
		- Red Hat Enterprise Linux 5 Update 2
		- Red Hat Enterprise Linux 6
		- SUSE Linux Enterprise Server 10 SP2
		- SUSE Linux Enterprise Server 11
		- Asianux Server 3 SP2
		- Asianux Server 4 SP3
- On Linux x86-64
	- Oracle Linux 4 Update 7
		- Oracle Linux 5 Update 2 (with Red Hat Compatible Kernel)
		- Oracle Linux 5 Update 5
		- Oracle Linux 6
		- Oracle Linux 6 (with Red Hat Compatible Kernel)
		- Oracle Linux 7
		- Oracle Linux 7 (with Red Hat Compatible Kernel)
		- Red Hat Enterprise Linux 4 Update 7
		- Red Hat Enterprise Linux 5 Update 2
		- Red Hat Enterprise Linux 6
		- Red Hat Enterprise Linux 7
		- SUSE Linux Enterprise Server 10 SP2
		- SUSE Linux Enterprise Server 11
		- SUSE Linux Enterprise Server 12 SP1
		- Asianux Server 3 SP2
		- Asianux Server 4 SP3
		- NeoKylin Linux Advanced Server 6
		- NeoKylin Linux Advanced Server 7
- On IBM: Linux on System z:
	- Red Hat Enterprise Linux 7 Update 1
		- Red Hat Enterprise Linux 6 Update 2
		- Red Hat Enterprise Linux 4 Update 8
		- Red Hat Enterprise Linux 5 Update 4
		- SUSE Linux Enterprise Server 10 SP3
		- SUSE Linux Enterprise Server 11 SP1

Starting with Oracle Database 11g Release 2 (11.2), the Security Enhanced Linux (SE Linux) feature is supported for Oracle Linux 4, Oracle Linux 5, Oracle Linux 6, Red Hat Enterprise Linux 4, Red Hat Enterprise Linux 5, and Red Hat Enterprise Linux 6.

Note:

Oracle Universal Installer performs checks to verify that the system meets the listed requirements. To ensure that these checks pass, verify the requirements before you start Oracle Universal Installer.

To determine the version of Linux installed, enter the following command:

```
# cat /proc/version
```

Alternatively, on some distributions of Linux, you can also enter the following command:

```
# lsb_release -id
```

Note:

For Asianux Server, Oracle Linux, and Red Hat Enterprise Linux, system requirements are identical by kernel version. Specifically:
- Oracle Linux 4 and Red Hat Enterprise Linux 4 requirements are the same.
- Asianux Server 3, Oracle Linux 5, and Red Hat Enterprise Linux 5 Update 2 requirements are the same.
- Oracle Unbreakable Enterprise Kernel for Linux 5 Update 5 (2.6.32) and above, available for x86-64 systems, contains several additional features and performance enhancements not available either with Oracle Linux or with other supported Linux distributions. This kernel can be installed on either Oracle Linux or Red Hat Enterprise Linux distributions. Before installing the Oracle Unbreakable Enterprise Kernel, you must have Oracle Linux 5 Update 5, Oracle Linux 6, Red Hat Enterprise Linux 5 Update 5 or Red Hat Enterprise Linux 6 installed on an x86-64 server.
- The Oracle Unbreakable Enterprise Kernel for Linux is installed by default with the Oracle Linux 6 installation.

### 2.3.2 Kernel Requirements

The following are the Kernel requirements for Oracle Database Client 11g Release 2.

For Linux x86

- On Oracle Linux 4 and Red Hat Enterprise Linux 4:
	2.6.9 or later
- On Oracle Linux 5, Red Hat Enterprise Linux 5 and Asianux Server 3:
	2.6.18 or later
- On Oracle Linux 6:
	2.6.32.100 or later
- On Red Hat Enterprise Linux 6 and Asianux Server 4:
	2.6.32-71 or later
- On SUSE Linux Enterprise Server 10:
	2.6.16.21 or later
- On SUSE Linux Enterprise Server 11:
	2.6.27.19 or later

For Linux x86-64

- On Oracle Linux 4 and Red Hat Enterprise Linux 4
	2.6.9 or later
- On Oracle Linux 5 Update 2 with Red Hat Compatible Kernel
	2.6.18 or later
- On Oracle Linux 5 Update 5 with Red Hat Compatible Kernel
	2.6.18 or later
- On Oracle Linux 5 Update 5 with Unbreakable Enterprise Kernel
	2.6.32-100.0.19 or later
- On Oracle Linux 6
	2.6.32-100.28.5.el6.x86\_64 or later
- On Oracle Linux 6 with Red Hat Compatible Kernel
	2.6.32-71.el6.x86\_64 or later
- On Oracle Linux 7
	3.8.13-33.el7uek.x86\_64 or later
- On Oracle Linux 7 with Red Hat Compatible Kernel
	3.10.0-54.0.1.el7.x86\_64 or later
- On Red Hat Enterprise Linux 5 Update 2
	2.6.18 or later
- On Red Hat Enterprise Linux 5 Update 5
	2.6.18 or later
- On Red Hat Enterprise Linux 6
	2.6.32-71.el6.x86\_64 or later
- On Red Hat Enterprise Linux 7
	3.10.0-54.0.1.el7.x86\_64 or later
- On Asianux Server 3
	2.6.18 or later
- On Asianux Server 4
	2.6.32-71.el6.x86\_64 or later
- On SUSE Linux Enterprise Server 10
	2.6.16.21 or later
- On SUSE Linux Enterprise Server 11
	2.6.27.19 or later
- On SUSE Linux Enterprise Server 12
	3.12.49-11 or later
- On NeoKylin Linux Advanced Server 6
	2.6.32-431.el6.x86\_64 or later
- On NeoKylin Linux Advanced Server 7
	3.10.0-327.el7.x86\_64 or later

See Also:

["About the Oracle Unbreakable Enterprise Kernel for Linux"](install_overview.md)

For IBM: Linux on System z

- On Red Hat Enterprise Linux 7
	3.10.0-229.el7 or later
- On Red Hat Enterprise Linux 6
	2.6.32-200 or later
- On Red Hat Enterprise Linux 4:
	2.6.9 or later
- On Red Hat Enterprise Linux 5:
	2.6.18 or later
- On SUSE Linux Enterprise Server 10:
	2.6.16.60 or later
- On SUSE Linux Enterprise Server 11:
	2.6.32.12 or later

To determine whether the required Kernel is installed, enter the following command:

```
# uname -r
```

The following is a sample output displayed by running this command on a Red Hat Enterprise Linux 4 system:

```
2.6.9-34.0.1.0.11.ELsmp
```

In this example, the output shows the kernel version (`2.6.``9`) and errata level (`34.0.1.0.11)` on the system.

If the kernel version does not meet the requirement specified earlier in this section, then contact the operating system vendor for information about obtaining and installing kernel updates.

### 2.3.3 Package Requirements

The following are the list of packages required for Oracle Database Client 11g Release 2 (11.2):

- Oracle Database Package Requirements for Linux x86
- Oracle Database Package Requirements Linux x86-64
- Oracle Database Package Requirements for IBM: Linux on System z

Note:

- Oracle recommends that you install your Linux operating system with the default software packages (RPMs), unless you specifically intend to perform a minimal installation, and follow the directions for performing such an installation to ensure that you have all required packages for Oracle software.
- Oracle recommends that you do not customize RPMs during a default operating system installation. A default installation includes most required packages, and helps you to limit manual checks of package dependencies.
- If you did not perform a default Linux installation, you intend to use LDAP, and you want to use the scripts `odisrvreg`, `oidca`, or `schemasync`, then install the Korn shell RPM for the Linux distribution.
- You must install the packages (or later versions) listed in the following table. Also, ensure that the list of RPMs and all of the prerequisites for these RPMs are installed.

Oracle Database Package Requirements for Linux x86

| Item | Requirement |
| --- | --- |
| Packages for Oracle Linux 4 and Red Hat Enterprise Linux 4 | The following packages (or later versions) must be installed: ``` binutils-2.15.92.0.2 compat-libstdc++-33-3.2.3 elfutils-libelf-0.97 elfutils-libelf-devel-0.97 gcc-3.4.6 gcc-c++-3.4.6 glibc-2.3.4-2.41 glibc-common-2.3.4 glibc-devel-2.3.4 libaio-devel-0.3.105 libaio-0.3.105 libgcc-3.4.6 libstdc++-3.4.6 libstdc++-devel-3.4.6 make-3.80 pdksh-5.2.14 sysstat-5.0.5 ``` |
| Packages for Oracle Linux 5, Red Hat Enterprise Linux 5, and Asianux Server 3 | The following packages (or later versions) must be installed: ``` binutils-2.17.50.0.6 compat-libstdc++-33-3.2.3 elfutils-libelf-0.125 elfutils-libelf-devel-0.125 elfutils-libelf-devel-static-0.125 gcc-4.1.2 gcc-c++-4.1.2 glibc-2.5-24 glibc-common-2.5 glibc-devel-2.5 ksh-20060214 libaio-0.3.106 libaio-devel-0.3.106  libgcc-4.1.2 libgomp-4.1.2 libstdc++-4.1.2  libstdc++-devel-4.1.2 make-3.81 sysstat-7.0.2 ``` |
| Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4 | The following packages (or later versions) must be installed: ``` binutils-2.20.51.0.2-5.11.el6.i686 compat-libcap1-1.10-1.i686 compat-libstdc++-33-3.2.3-69.el6.i686 gcc-4.4.4-13.el6.i686 gcc-c++-4.4.4-13.el6.i686 glibc-2.12-1.7.el6.i686 glibc-devel-2.12-1.7.el6.i686 ksh libgcc-4.4.4-13.el6.i686 libstdc++-4.4.4-13.el6.i686 libstdc++-devel-4.4.4-13.el6.i686 libaio-0.3.107-10.el6.i686 libaio-devel-0.3.107-10.el6.i686 make-3.81-19.el6.i686 sysstat-9.0.4-11.el6.i686 ``` |
| SUSE Linux Enterprise Server 10 | The following packages (or later versions) must be installed: ``` binutils-2.16.91.0.5 compat-libstdc++-5.0.7 gcc-4.1.2 gcc-c++-4.1.2 glibc-2.4-31.63 glibc-devel-2.4-31.63 libaio-0.3.104 libaio-devel-0.3.104 libelf-0.8.5 libgcc-4.1.2 libstdc++-4.1.2 libstdc++-devel-4.1.2 make-3.80 sysstat-8.0.4 ``` |
| SUSE Linux Enterprise Server 11 | The following packages (or later versions) must be installed: ``` binutils-2.19 gcc-4.3 gcc-c++-4.3 glibc-2.9 glibc-devel-2.9 libstdc++33-3.3.3 libstdc++43-4.3.3_20081022 libstdc++43-devel-4.3.3_20081022 libaio-0.3.104 libaio-devel-0.3.104 libgcc43-4.3.3_20081022 libstdc++-devel-4.3 make-3.81 sysstat-8.1.5 ``` |

Oracle Database Package Requirements Linux x86-64

IMPORTANT:

- Starting with Oracle Database 11g Release 2 (11.2.0.2), all 32-bit packages, except for `gcc-32bit-4.3`, listed in the following table are not required for installing a database on Linux x86-64. Only the 64-bit packages are required. However, for any Oracle Database 11g release before 11.2.0.2, both the 32-bit and 64-bit packages listed in the following table are required.
	However, when you install the 32-bit client binaries on 64-bit ports, the installer checks for the existence of 32-bit packages.
- If you are using Oracle Unbreakable Enterprise Kernel, then all required kernel packages are installed as part of the Oracle Unbreakable Enterprise Kernel installation
- For Orace Linux 6 the Oracle Validated RPM has been replaced by the Oracle RDBMS Server 11gR2 Pre-install RPM. See the "Completing a Minimal Linux Installation" section in [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm) for more information.

| Item | Requirement |
| --- | --- |
| Packages for Oracle Linux 4 and Red Hat Enterprise Linux 4 | The following packages (or later versions) must be installed: ``` binutils-2.15.92.0.2 compat-libstdc++-33-3.2.3 compat-libstdc++-33-3.2.3 (32 bit) elfutils-libelf-0.97 elfutils-libelf-devel-0.97 expat-1.95.7 gcc-3.4.6 gcc-c++-3.4.6 glibc-2.3.4-2.41 glibc-2.3.4-2.41 (32 bit) glibc-common-2.3.4 glibc-devel-2.3.4 libaio-0.3.105 libaio-0.3.105 (32 bit) libaio-devel-0.3.105 libaio-devel-0.3.105 (32 bit) libgcc-3.4.6 libgcc-3.4.6 (32-bit) libstdc++-3.4.6 libstdc++-3.4.6 (32 bit) libstdc++-devel 3.4.6 make-3.80 sysstat-5.0.5 ``` |
| Packages for Oracle Linux 5, Red Hat Enterprise Linux 5, and Asianux Server 3 | The following packages (or later versions) must be installed: ``` binutils-2.17.50.0.6 compat-libstdc++-33-3.2.3 compat-libstdc++-33-3.2.3 (32 bit) elfutils-libelf-0.125 elfutils-libelf-devel-0.125 gcc-4.1.2 gcc-c++-4.1.2 glibc-2.5-24 glibc-2.5-24 (32 bit) glibc-common-2.5 glibc-devel-2.5 glibc-devel-2.5 (32 bit) libaio-0.3.106 libaio-0.3.106 (32 bit) libaio-devel-0.3.106 libaio-devel-0.3.106 (32 bit) libgcc-4.1.2 libgcc-4.1.2 (32 bit) libstdc++-4.1.2 libstdc++-4.1.2 (32 bit) libstdc++-devel-4.1.2 make-3.81 sysstat-7.0.2 ``` |
| Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4 | The following packages (or later versions) must be installed: ``` binutils-2.20.51.0.2-5.11.el6 (x86_64) compat-libcap1-1.10-1 (x86_64) compat-libstdc++-33-3.2.3-69.el6 (x86_64) compat-libstdc++-33-3.2.3-69.el6.i686 gcc-4.4.4-13.el6 (x86_64) gcc-c++-4.4.4-13.el6 (x86_64) glibc-2.12-1.7.el6 (i686) glibc-2.12-1.7.el6 (x86_64) glibc-devel-2.12-1.7.el6 (x86_64) glibc-devel-2.12-1.7.el6.i686 ksh libgcc-4.4.4-13.el6 (i686) libgcc-4.4.4-13.el6 (x86_64) libstdc++-4.4.4-13.el6 (x86_64) libstdc++-4.4.4-13.el6.i686 libstdc++-devel-4.4.4-13.el6 (x86_64) libstdc++-devel-4.4.4-13.el6.i686 libaio-0.3.107-10.el6 (x86_64) libaio-0.3.107-10.el6.i686 libaio-devel-0.3.107-10.el6 (x86_64) libaio-devel-0.3.107-10.el6.i686 make-3.81-19.el6 sysstat-9.0.4-11.el6 (x86_64) ``` |
| Oracle Linux 7 and Red Hat Enterprise Linux 7 | The following packages (or later versions) must be installed: ``` binutils-2.23.52.0.1-12.el7.x86_64  compat-libcap1-1.10-3.el7.x86_64  compat-libstdc++-33-3.2.3-71.el7.i686 compat-libstdc++-33-3.2.3-71.el7.x86_64 gcc-4.8.2-3.el7.x86_64  gcc-c++-4.8.2-3.el7.x86_64  glibc-2.17-36.el7.i686  glibc-2.17-36.el7.x86_64  glibc-devel-2.17-36.el7.i686  glibc-devel-2.17-36.el7.x86_64  ksh libaio-0.3.109-9.el7.i686  libaio-0.3.109-9.el7.x86_64  libaio-devel-0.3.109-9.el7.i686  libaio-devel-0.3.109-9.el7.x86_64  libgcc-4.8.2-3.el7.i686  libgcc-4.8.2-3.el7.x86_64  libstdc++-4.8.2-3.el7.i686  libstdc++-4.8.2-3.el7.x86_64  libstdc++-devel-4.8.2-3.el7.i686  libstdc++-devel-4.8.2-3.el7.x86_64  libXi-1.7.2-1.el7.i686  libXi-1.7.2-1.el7.x86_64  libXtst-1.2.2-1.el7.i686  libXtst-1.2.2-1.el7.x86_64  make-3.82-19.el7.x86_64  sysstat-10.1.5-1.el7.x86_64 ``` |
| SUSE Linux Enterprise Server 10 | The following packages (or later versions) must be installed: ``` binutils-2.16.91.0.5 compat-libstdc++-5.0.7 gcc-4.1.0 gcc-c++-4.1.2 glibc-2.4-31.63 glibc-devel-2.4-31.63 glibc-devel-32bit-2.4-31.63 libaio-0.3.104 libaio-32bit-0.3.104 libaio-devel-0.3.104 libaio-devel-32bit-0.3.104 libelf-0.8.5 libgcc-4.1.2 libstdc++-4.1.2 libstdc++-devel-4.1.2 make-3.80 sysstat-8.0.4 ``` |
| SUSE Linux Enterprise Server 11 | The following packages (or later versions) must be installed: ``` binutils-2.19 gcc-4.3 gcc-c++-4.3 glibc-2.9 glibc-32bit-2.9 glibc-devel-2.9 glibc-devel-32bit-2.9 libaio-0.3.104 libaio-32bit-0.3.104 libaio-devel-0.3.104 libaio-devel-32bit-0.3.104 libstdc++33-3.3.3 libstdc++33-32bit-3.3.3 libstdc++43-4.3.3_20081022 libstdc++43-32bit-4.3.3_20081022 libstdc++43-devel-4.3.3_20081022 libstdc++43-devel-32bit-4.3.3_20081022 libgcc43-4.3.3_20081022 libstdc++-devel-4.3 make-3.81 sysstat-8.1.5 ``` |
| SUSE Linux Enterprise Server 12 | The following packages (or later versions) must be installed: ``` binutils-2.25.0-13.1 gcc-4.8-6.189 gcc48-4.8.5-24.1 glibc-2.19-31.9 glibc-32bit-2.19-31.9 glibc-devel-2.19-31.9.x86_64 glibc-devel-32bit-2.19-31.9.x86_64 libaio1-0.3.109-17.15 libaio-devel-0.3.109-17.15 libcap1-1.10-59.61 libstdc++48-devel-4.8.5-24.1.x86_64 libstdc++48-devel-32bit-4.8.5-24.1.x86_64 libstdc++6-5.2.1+r226025-4.1.x86_64 libstdc++6-32bit-5.2.1+r226025-4.1.x86_64 libstdc++-devel-4.8-6.189.x86_64 libstdc++-devel-32bit-4.8-6.189.x86_64 libgcc_s1-5.2.1+r226025-4.1.x86_64 libgcc_s1-32bit-5.2.1+r226025-4.1.x86_64 mksh-50-2.13 make-4.0-4.1.x86_64 sysstat-10.2.1-3.1.x86_64 xorg-x11-driver-video-7.6_1-14.30.x86_64 xorg-x11-server-7.6_1.15.2-36.21.x86_64 xorg-x11-essentials-7.6_1-14.17.noarch xorg-x11-Xvnc-1.4.3-7.2.x86_64 xorg-x11-fonts-core-7.6-29.45.noarch xorg-x11-7.6_1-14.17.noarch xorg-x11-server-extra-7.6_1.15.2-36.21.x86_64 xorg-x11-libs-7.6-45.14.noarch xorg-x11-fonts-7.6-29.45.noarch ```  Note: You must download and install patch 18370031. For more information about how to download and install this patch see:  `https://support.oracle.com`  [Oracle Database Release Notes for Linux](https://docs.oracle.com/cd/E11882_01/relnotes.112/e23558/toc.htm) |
| NeoKylin Linux Advanced Server 6 | The following packages (or later versions) must be installed: ``` binutils-2.20.51.0.2-5.36.el6 (x86_64)  compat-libcap1-1.10-1 (x86_64)  compat-libstdc++-33-3.2.3-69.el6 (x86_64)  compat-libstdc++-33-3.2.3-69.el6 (i686)  gcc-4.4.7-4.el6 (x86_64)  gcc-c++-4.4.7-4.el6 (x86_64)  glibc-2.12-1.132.el6 (i686)  glibc-2.12-1.132.el6 (x86_64)  glibc-devel-2.12-1.132.el6 (x86_64)  glibc-devel-2.12-1.132.el6 (i686)  ksh  libgcc-4.4.7-4.el6 (i686)  libgcc-4.4.7-4.el6 (x86_64)  libstdc++-4.4.7-4.el6 (x86_64)  libstdc++-4.4.7-4.el6 (i686)  libstdc++-devel-4.4.7-4.el6 (x86_64)  libstdc++-devel-4.4.7-4.el6 (i686)  libaio-0.3.107-10.el6 (x86_64)  libaio-0.3.107-10.el6 (i686)  libaio-devel-0.3.107-10.el6 (x86_64)  libaio-devel-0.3.107-10.el6 (i686)  make-3.81-20.el6 sysstat-9.0.4-22.el6 (x86_64) ``` |
| NeoKylin Linux Advanced Server 7 | The following packages (or later versions) must be installed: ``` binutils-2.23.52.0.1-55.el7.x86_64 compat-libcap1-1.10-7.el7.x86_64 gcc-4.8.5-4.el7.ns7.01.x86_64 gcc-c++-4.8.5-4.el7.ns7.01.x86_64 glibc-2.17-105.el7.ns7.01.i686 glibc-2.17-105.el7.ns7.01.x86_64 glibc-devel-2.17-105.el7.ns7.01.i686 glibc-devel-2.17-105.el7.ns7.01.x86_64 ksh-20120801-22.el7_1.2.x86_64 libaio-0.3.109-13.el7.i686 libaio-0.3.109-13.el7.x86_64 libaio-devel-0.3.109-13.el7.i686 libaio-devel-0.3.109-13.el7.x86_64 libgcc-4.8.5-4.el7.ns7.01.i686 libgcc-4.8.5-4.el7.ns7.01.x86_64 libstdc++-4.8.5-4.el7.ns7.01.i686 libstdc++-4.8.5-4.el7.ns7.01.x86_64 libstdc++-devel-4.8.5-4.el7.ns7.01.i686 libstdc++-devel-4.8.5-4.el7.ns7.01.x86_64 libXi-1.7.4-2.el7.i686 libXi-1.7.4-2.el7.x86_64 libXtst-1.2.2-2.1.el7.i686 libXtst-1.2.2-2.1.el7.x86_64 make-3.82-21.el7.x86_64 sysstat-10.1.5-7.el7.x86_64 ``` |

Oracle Database Package Requirements for IBM: Linux on System z

| Operating System | Requirement |
| --- | --- |
| Red Hat Enterprise Linux 4 | The following packages (or later versions) must be installed: ``` binutils-2.15.92.0.2-25 (s390x) compat-libstdc++-33-3.2.3-47.3 (s390) compat-libstdc++-33-3.2.3-47.3 (s390x) gcc-3.4.6-11 (s390x) gcc-c++-3.4.6-11 (s390x) glibc-2.3.4-2.43 (s390) glibc-2.3.4-2.43 (s390x) glibc-devel-2.3.4-2.43 (s390) glibc-devel-2.3.4-2.43 (s390x) libaio-0.3.105-2 (s390) libaio-0.3.105-2 (s390x) libaio-devel-0.3.105-2 (s390) libaio-devel-0.3.105-2 (s390x) libgcc-3.4.6-11 (s390) libgcc-3.4.6-11 (s390x) libstdc++-3.4.6-10.0.1 libstdc++-3.4.6-10.0.1 (32-bit) libstdc++-devel-3.4.6-10.0.1 libstdc++-devel-3.4.6-10.0.1 (x86_64) make-3.80 pdksh sysstat-5.0.5-25.el4 (s390x) ``` |
| Red Hat Enterprise Linux 5 | The following packages (or later versions) must be installed: ``` binutils-2.17.50.0.6-12.el5 (s390x) compat-libstdc++-33-3.2.3-61 (s390) compat-libstdc++-33-3.2.3-61 (s390x) gcc-4.1.2-46.el5 (s390x) gcc-c++-4.1.2-46.el5 (s390x) glibc-2.5-42(s390) glibc-2.5-42 (s390x) glibc-devel-2.5-42 (s390) glibc-devel-2.5-42 (s390x) ksh libaio-0.3.106-3.2 (s390) libaio-0.3.106-3.2 (s390x) libaio-devel-0.3.106-3.2 (s390) libaio-devel-0.3.106-3.2 (s390x) libgcc-4.1.2-46.el5 (s390) libgcc-4.1.2-46.el5 (s390x) libstdc++-4.1.2-46.el5 (s390) libstdc++-4.1.2-46.el5 (s390x) libstdc++-devel-4.1.2-46.el5 (s390x) make-3.81 sysstat-7.0.2-3.el5 (s390x) ``` |
| Red Hat Enterprise Linux 6 | The following packages (or later versions) must be installed: ``` binutils-2.20.51.0.2-5.28 (s390x) compat-libstdc++-33-3.2.3-69.el6 (s390x) gcc-4.4.6-3.el6 (s390x) gcc-c++-4.4.6-3.el6 (s390x) glibc-2.12-1.47.el6 (s390) glibc-2.12-1.47.el6 (s390x) glibc-devel-2.12-1.47.el6 (s390) glibc-devel-2.12-1.47.el6 (s390x) libaio-0.3.107-10.el6 (s390) libaio-0.3.107-10.el6 (s390x) libaio-devel-0.3.107-10.el6 (s390x) libgcc-4.4.6-3.el6 (s390) libgcc-4.4.6-3.el6 (s390x) libstdc++-4.4.6-3.el6 (s390x) libstdc++-devel-4.4.6-3.el6 (s390x) make-3.81-19.el6 (s390x) pdksh sysstat-9.0.4-18.el6 (s390x) ``` |
| Red Hat Enterprise Linux 7 | The following packages (or later versions) must be installed: ``` binutils-2.23.52.0.1-30.el7.s390x compat-libcap1-1.10-7.el7.s390x cpp-4.8.2-16.el7.s390x gcc-4.8.3-9.el7.s390x gcc-c++-4.8.3-9.el7.s390x glibc-2.17-78.el7.s390 glibc-2.17-78.el7.s390x glibc-devel-2.17-78.el7.s390 glibc-devel-2.17-78.el7.s390x glibc-headers-2.17-55.el7.s390x ksh-20120801-22.el7.s390x libaio-0.3.109-12.el7.s390 libaio-0.3.109-12.el7.s390x libaio-devel-0.3.109-12.el7.s390 libaio-devel-0.3.109-12.el7.s390x libgcc-4.8.3-9.el7.s390 libgcc-4.8.3-9.el7.s390x libstdc++-4.8.3-9.el7.s390 libstdc++-4.8.3-9.el7.s390x libstdc++-devel-4.8.3-9.el7.s390 libstdc++-devel-4.8.3-9.el7.s390x libXi-1.2.2-2.1.el7.s390 libXi-1.2.2-2.1.el7.s390x libXtst-1.2.2-2.1.el7.s390 libXtst-1.2.2-2.1.el7.s390x make-3.82-21.el7.s390x mpfr-3.1.1-4.el7.s390x sysstat-10.1.5-7.el7.s390x ``` |
| SUSE Linux Enterprise Server 10 | The following packages (or later versions) must be installed: ``` binutils-32bit-2.16.91.0.5-23.34.33 (s390x) gcc-4.1.2_20070115-0.29.6 (s390x) gcc-c++-4.1.2_20070115-0.29.6 (s390x) glibc-2.4-31.74.1 (s390x) glibc-32bit-2.4-31.74.1 (s390x) glibc-devel-2.4-31.74.1 (s390x) glibc-devel-32bit-2.4-31.74.1 (s390x) ksh libaio-0.3.104-14.2 (s390x) libaio-32bit-0.3.104-14.2 (s390x) libaio-devel-0.3.104-14.2 (s390x) libaio-devel-32bit-0.3.104-14.2 (s390x) libstdc++-4.1.2_20070115-0.29.6 (s390x) libstdc++-devel-4.1.2_20070115-0.29.6 (s390x) make-3.80-202.2 (s390x) sysstat-8.0.4-1.7.27 (s390x) ``` |
| SUSE Linux Enterprise Server 11 | The following packages (or later versions) must be installed: ``` binutils-2.20.0-0.7.9 (s390x) gcc-4.3-62.198 (s390x) gcc-c++-4.3-62.198 (s390x) glibc-2.11.1-0.17.4 (s390x) glibc-32bit-2.11.1-0.17.4 (s390x) glibc-devel-2.11.1-0.17.4 (s390x) glibc-devel-32bit-2.11.1-0.17.4 (s390x) ksh libaio-0.3.109-0.1.46 (s390x) libaio-32bit-0.3.109-0.1.46 (s390x) libaio-devel-0.3.109-0.1.46 (s390x) libaio-devel-32bit-0.3.109-0.1.46 (s390x) libstdc++43-4.3.4_20091019-0.7.35 (s390x) libstdc++43-32bit-4.3.4_20091019-0.7.35 (s390x) libstdc++43-devel-4.3.4_20091019-0.7.35 (s390x) libstdc++43-devel-32bit-4.3.4_20091019-0.7.35 (s390x) libgcc43-4.3.4_20091019-0.7.35 (s390x) make-3.81 sysstat-8.1.5-7.9.56 (s390x) ``` |

See "Oracle ODBC Drivers" for information on ODBC packages.

To determine whether the required packages are installed, enter commands similar to the following:

```
# rpm -q package_name
```

If a package is not installed, then install it from the Linux distribution media or download the required package version from the Linux vendor's website.

### 2.3.4 Compiler Requirements

On Linux x86 and Linux x86-64, Intel C++ Compiler 10.1 or later and the version of GNU C and C++ compilers listed under "Package Requirements" are supported with Pro\*C/C++, Oracle Call Interface, Oracle C++ Call Interface, and Oracle XML Developer's Kit (XDK) for Oracle Database 11g Release 2.

Note:

On Linux x86 and Linux x86-64, the Intel C++ Compiler 10.1 can be used only with the standard template libraries of the gcc versions mentioned in the "Package Requirements" section, to build Oracle C++ Call Interface (OCCI) applications.

Oracle XML Developer's Kit is supported with the same compilers as OCCI.

On IBM: Linux on System z the version of GNU C and C++ compilers listed under "Package Requirements" are supported for Oracle Database 11g Release 2.

### 2.3.5 Additional Software Requirements

Depending on the components you want to use, you must ensure that the following software are installed:

- Oracle JDBC/OCI Drivers
- Oracle ODBC Drivers
- Linux-PAM Library
- Separate 32-Bit Client Software for 64-Bit Platforms
- Programming Languages
- Browser Requirements

#### 2.3.5.1 Oracle JDBC/OCI Drivers

You can use the following optional JDK versions with the Oracle JDBC/OCI drivers. However, these are not mandatory for the database installation.

On Linux x86 and Linux x86-64, use JDK 6 (Java SE Development Kit `1.6.0_21`) or JDK 5 (`1.5.0_24`) with the JNDI extension with the Oracle Java Database Connectivity and Oracle Call Interface drivers. However, these are not mandatory for the database installation. Please note that JDK 1.5 is installed with this release.

On IBM: Linux on System z:

- JDK 6 SR16 FP1 or higher
- JDK 5 SR16 FP3 or higher

#### 2.3.5.2 Oracle ODBC Drivers

If you intend to use ODBC, then install the most recent ODBC Driver Manager for Linux. Download and install the Driver Manager from the following URL:

`http://www.unixodbc.org`

Linux RPMs are available on the site.

- On Linux x86
	To use ODBC, you must also install the following additional 32-bit ODBC RPMs, depending on your operating system:
	- On Oracle Linux 4 and Red Hat Enterprise Linux 4:
		```
		unixODBC-2.2.11 (32 bit) or later
		unixODBC-devel-2.2.11 (32 bit) or later
		```
		- On Oracle Linux 5, Red Hat Enterprise Linux 5, and Asianux Server 3:
		```
		unixODBC-2.2.11 (32 bit) or later
		unixODBC-devel-2.2.11 (32 bit) or later
		```
		- On Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4:
		```
		unixODBC-2.2.14-11 (32 bit) or later
		unixODBC-devel-2.2.14-11 (32 bit) or later
		```
		- On SUSE Linux Enterprise Server 10:
		```
		unixODBC-32bit-2.2.11 (32 bit) or later
		unixODBC-devel-32bit-2.2.11 (32 bit) or later
		```
		- On SUSE Linux Enterprise Server 11:
		```
		unixODBC-32bit-2.2.12 (32-bit) or later
		unixODBC-devel-32bit-2.2.12 (32 bit) or later
		```
- On Linux x86-64
	To use ODBC, you must also install the following additional ODBC RPMs, depending on your operating system.
	- On Oracle Linux 4 and Red Hat Enterprise Linux 4:
		```
		unixODBC-2.2.11 (32 bit) or later
		unixODBC-devel-2.2.11 (64 bit) or later
		unixODBC-2.2.11 (64 bit) or later
		```
		- On Oracle Linux 5, Red Hat Enterprise Linux 5, and Asianux Server 3:
		```
		unixODBC-2.2.11 (32 bit) or later
		unixODBC-devel-2.2.11 (64 bit) or later
		unixODBC-2.2.11 (64 bit) or later
		```
		- On Oracle Linux 6, Red Hat Enterprise Linux 6, and Asianux Server 4:
		```
		unixODBC-2.2.14-11.el6 (x86_64) or later
		unixODBC-2.2.14-11.el6.i686 or later
		unixODBC-devel-2.2.14-11.el6 (x86_64) or later
		unixODBC-devel-2.2.14-11.el6.i686 or later
		```
		- On Oracle Linux 7, and Red Hat Enterprise Linux 7:
		```
		unixODBC-2.3.1-6.el7.x86_64 or later
		unixODBC-2.3.1-6.el7.i686 or later
		unixODBC-devel-2.3.1-6.el7.x86_64 or later
		unixODBC-devel-2.3.1-6.el7.i686 or later
		```
		- On SUSE Linux Enterprise Server 10:
		```
		unixODBC-32bit-2.2.11 (32 bit) or later
		unixODBC-2.2.11 (64 bit) or later
		unixODBC-devel-2.2.11 (64 bit) or later
		```
		- On SUSE Linux Enterprise Server 11
		```
		unixODBC-2.2.12 or later
		unixODBC-devel-2.2.12 or later
		unixODBC-32bit-2.2.12 (32 bit) or later
		```
		- On NeoKylin Linux Advanced Server 6
		```
		unixODBC-2.2.14-12.el6_3.i686 or later
		unixODBC-2.2.14-12.el6_3.x86_64 or later
		unixODBC-devel-2.2.14-12.el6_3.x86_64 or later
		unixODBC-devel-2.2.14-12.el6_3.i686 or later
		```
		- On NeoKylin Linux Advanced Server 7
		```
		unixODBC-2.3.1-11.el7.i686 or later
		unixODBC-2.3.1-11.el7.x86_64 or later
		unixODBC-devel-2.3.1-11.el7.i686 or later
		unixODBC-devel-2.3.1-11.el7.x86_64 or later
		```
- On IBM: Linux on System z
	To use ODBC, you must also install the following additional ODBC RPMs, depending on your operating system.
	- On Red Hat Enterprise Linux 4:
		```
		unixODBC-2.2.11 (32 bit) or later
		unixODBC-devel-2.2.11 (64 bit) or later
		unixODBC-2.2.11 (64 bit) or later
		```
		- On Red Hat Enterprise Linux 5:
		```
		unixODBC-2.2.11 (32 bit) or later
		unixODBC-devel-2.2.11 (64 bit) or later
		unixODBC-2.2.11 (64 bit) or later
		```
		- On Red Hat Enterprise Linux 6:
		```
		unixODBC-2.2.14-11 (32 bit) or later
		unixODBC-2.2.14-11 (64 bit) or later
		uunixODBC-devel-2.2.14-11 (64 bit) or later
		```
		- On Red Hat Enterprise Linux 7:
		```
		unixODBC-2.3.1-11 (32 bit) or later
		unixODBC-2.3.1-11 (64 bit) or later
		unixODBC-devel-2.3.1-11 (32 bit) or later
		unixODBC-devel-2.3.1-11 (64 bit) or later
		```
		- On SUSE Linux Enterprise Server 10:
		```
		unixODBC-32bit-2.2.11 (32 bit) or later
		unixODBC-2.2.11 (64 bit) or later
		unixODBC-devel-2.2.11 (64 bit) or later
		```
		- On SUSE Linux Enterprise Server 11
		```
		unixODBC-2.2.12 or later
		unixODBC-devel-2.2.12 or later
		unixODBC-32bit-2.2.12 (32 bit) or later
		```

#### 2.3.5.3 Linux-PAM Library

Install the latest Linux-PAM (Pluggable Authentication Modules for Linux) library to enable the system administrator to choose how applications authenticate users.

#### 2.3.5.4 Separate 32-Bit Client Software for 64-Bit Platforms

Starting with Oracle Database 11g Release 2 (11.2), the 64-bit client software does not contain any 32-bit client binaries. If you require 32-bit client binaries on 64-bit platforms, then install the 32-bit binaries from the respective 32-bit client software into a separate Oracle home.

See Also:

My Oracle Support note 883702.1 for more information:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=883702.1`

However, when you install the 32-bit client binaries on 64-bit platforms, the installer checks for the existence of 32-bit software such as the packages.

See Also:

- "Package Requirements" for Linux x86 package requirements
- "Bit-Length Support for Client Applications" in [Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems](https://docs.oracle.com/cd/E11882_01/server.112/e10839/prcmp_cll_int.htm#UNXAR006)

#### 2.3.5.5 Programming Languages

The following products are certified for use with:

- Pro\* COBOL
	- Micro Focus Server Express 5.1

#### 2.3.5.6 Browser Requirements

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

#### 2.3.5.7 Programming Languages

The following products are certified for use with:

- Pro\* COBOL
	- Micro Focus Server Express 5.1

### 2.3.6 Instant Client Light Requirements

In addition to the requirements described in the preceding section, if you plan to use Instant Client Light, then the applications must use the following languages and character sets:

- Language: Any language that is supported by Oracle
- Territory: Any territory that is supported by Oracle
- Character sets:
	- Single byte
		- US7ASCII
				- WE8DEC
				- WE8MSWIN1252
				- WE8ISO8859P1
		- Unicode
		- UTF8
				- AL16UTF16
				- AL32UTF8
		Instant Client Light can connect to databases having one of the following database character sets:
		- US7ASCII
				- WE8DEC
				- WE8MSWIN1252
				- WE8ISO8859P1
				- WE8EBCDIC37C
				- WE8EBCDIC1047
				- UTF8
				- AL32UTF8

The language, territory, and character sets are determined by the `NLS_LANG` environment variable.

## 2.4 Creating Required Operating System Group and User

Depending on whether this is the first time Oracle software is being installed on this system and on the products that you are installing, you may have to create the following operating system group and user:

- The Oracle Inventory group (typically, `oinstall`)
	You must have a group whose members are given access to write to the Oracle Central Inventory (`oraInventory`).
	Installation logs and trace files from installations of Oracle software. These files are also copied to the respective Oracle homes for future reference.
	Other metadata inventory information regarding Oracle installations are stored in the individual Oracle home inventory directories, and are separate from the Central Inventory.
	For new installations, Oracle recommends that you allow Oracle Universal Installer to create the Central Inventory directory. By default, if you create an Oracle path in compliance with OFA structure, such as `/u01/app`, then the Central Inventory is created in the path `u01/app/oraInventory`, using correct permissions to allow all Oracle installation owners to write to this directory.
- The Oracle software owner user (typically, `oracle`)
	You must create this user the first time you install Oracle software on the system. This user owns all of the software installed during the installation. This user must have the Oracle Inventory group as its primary group. It must also have the OSDBA and OSOPER groups as secondary groups.
	Note:
	- In Oracle documentation, the user created to own the Oracle Database installations is referred to as the `oracle` user.
	- An Oracle Database installation must be owned by the Oracle software owner user (`oracle)` and the primary group of the Oracle software owner user must be the Oracle Inventory group (`oinstall`).

A single Oracle Inventory group is required for all installations of Oracle software on the system. After the first installation of Oracle software, you must use the same Oracle Inventory group for all subsequent Oracle software installations on that system. However, you can choose to create different Oracle software owner users for separate installations.

Note:

The following sections describe how to create local users and groups. As an alternative to creating local users and groups, you could create the appropriate users and groups in a directory service, for example, Network Information Services (NIS). For information about using directory services, contact the system administrator or refer to the operating system documentation.

The following sections describe how to create the required operating system users and groups:

- Creating the Oracle Inventory Group
- Creating the Oracle Software Owner User

### 2.4.1 Creating the Oracle Inventory Group

You must create the Oracle Inventory group if it does not exist. The following sections describe how to determine the Oracle Inventory group name, if it exists, and how to create it if necessary:

- Determining Whether the Oracle Inventory Group Exists
- Creating the Oracle Inventory Group

Determining Whether the Oracle Inventory Group Exists

When you install Oracle software on the system for the first time, Oracle Universal Installer creates the `oraInst.loc` file. This file identifies the name of the Oracle Inventory group (typically, `oinstall`), and the path of the Oracle Inventory directory.

An `oraInst.loc` file has content similar to the following:

```
inventory_loc=central_inventory_location
inst_group=group
```

In the preceding example, `central_inventory_location` is the location of the Oracle Central Inventory, and `group` is the name of the group that has permissions to write to the central inventory.

If you have an existing Oracle Inventory, then ensure that you use the same Oracle Inventory for all Oracle software installations, and ensure that all Oracle software users you intend to use for installation have permissions to write to this directory.

To determine whether the Oracle Inventory group exists, enter the following command:

```
# more /etc/oraInst.loc
```

If the `oraInst.loc` file exists, then the output from this command is similar to the following:

```
inventory_loc=/u01/app/oraInventory
inst_group=oinstall
```

In the previous output example:

- The `inventory_loc` parameter shows the location of the Oracle Inventory
- The `inst_group` parameter shows the name of the Oracle Inventory group (in this example, `oinstall`).

Creating the Oracle Inventory Group

If the `oraInst.loc` file does not exist, then create the Oracle Inventory group as follows:

```
# /usr/sbin/groupadd oinstall
```

### 2.4.2 Creating the Oracle Software Owner User

You must create an Oracle software owner user in the following circumstances:

- If an Oracle software owner user does not exist; for example, if this is the first installation of Oracle software on the system
- If an Oracle software owner user exists, but you want to use a different operating system user

#### 2.4.2.1 Determining If an Oracle Software Owner User Exists

To determine if an Oracle software owner user (`oracle`) exists, enter the following command:

```
# id oracle
```

If the `oracle` user exists, then the output from this command is similar to the following:

```
uid=54321(oracle) gid=54321(oinstall) groups=54322(dba),54323(oper)
```

If the user exists, then determine whether you want to use the existing user or create another `oracle` user. If you want to use the existing user, then ensure that the user's primary group is the Oracle Inventory group. Refer to one of the following sections for more information:

Note:

If necessary, contact the system administrator before using or modifying an existing user.
- If you want to use the existing Oracle software owner user, and the user's primary group is the Oracle Inventory group, then refer to the "Identifying Required Software Directories" section.
- To modify an existing user, refer to the "Modifying an Oracle Software Owner User" section.
- To create a user, refer to the following section.

#### 2.4.2.2 Creating an Oracle Software Owner User

If the Oracle software owner user does not exist or if you require a new Oracle software owner user, then create it as follows. In the following procedure, use the user name `oracle` unless a user with that name exists.

1. To create the `oracle` user, enter a command similar to the following:
	```
	# /usr/sbin/useradd -g oinstall[ -G dba]oracle
	```
	In this command:
	- The `-g` option specifies the primary group, which must be the Oracle Inventory group, for example, `oinstall`
		- The `-G` option specifies optional secondary groups, which must include the OSDBA group and, if required, the OSOPER group. For example, `dba, osoper.`
2. Set the password of the `oracle` user:
	```
	# passwd oracle
	```

Refer to the "Identifying Required Software Directories" section to continue.

#### 2.4.2.3 Modifying an Oracle Software Owner User

If the `oracle` user exists, but its primary group is not `oinstall`, then enter a command similar to the following to modify it:

```
# /usr/sbin/usermod -g oinstall -G dba oracle
```

Specify the primary group using the `-g` option and any required secondary group using the `-G` option.

## 2.5 Identifying Required Software Directories

You must identify or create the following directories for the Oracle software:

- Oracle Base Directory
- Oracle Inventory Directory
- Oracle Home Directory

Note:

Ensure that the paths you select for Oracle software, such as the Oracle home path and the Oracle base path, use only ASCII characters. Because installation owner names are used by default for some paths, this ASCII character restriction applies to user names, file names, and directory names.

### 2.5.1 Oracle Base Directory

The Oracle base directory is a top-level directory for Oracle software installations. On UNIX systems, the Optimal Flexible Architecture (OFA) guidelines recommend that you use a path similar to the following for the Oracle base directory:

```
/mount_point/app/software_owner
```

In this example:

- `mount_point` is the mount point directory for the file system that contains the Oracle software.
	The examples in this guide use `/u01` for the mount point directory.
- `software_owner` is the operating system user name of the software owner installing the Oracle software, for example `oracle`.

You must specify the `ORACLE_BASE` folder that contains all Oracle products.

Note:

If you have an existing Oracle base, then you can select it from the Use existing drop down box. By default, the drop down box contains the existing value for Oracle base selected. Refer to ["Installing the Oracle Database Client Software"](inst_task.md) for information.

If you do not have an Oracle base, then you can create a new one by editing the text in the list box.

You can use the same Oracle base directory for multiple installations or you can create separate Oracle base directories for different installations. If different operating system users install Oracle software on the same system, then each user must create a separate Oracle base directory. The following example Oracle base directories could all exist on the same system:

```
/u01/app/oracle
/u01/app/orauser
```

The following sections describe how to identify existing Oracle base directories that may be suitable for the installation and how to create an Oracle base directory if necessary.

Regardless of whether you create an Oracle base directory or decide to use an existing one, you must set the `ORACLE_BASE` environment variable to specify the full path to this directory.

### 2.5.2 Oracle Inventory Directory

The Oracle Inventory directory (`oraInventory`) stores an inventory of all software installed on the system. It is required, and shared by all Oracle software installations on a single system. If you have an existing Oracle Inventory path, then Oracle Universal Installer continues to use that Oracle Inventory.

The first time you install Oracle software on a system, Oracle Universal Installer provides an OFA-compliant path in the format `/u[01-09]/app`, such as `/u01/app`. The user running the installation has permissions to write to that path. If this is true, then Oracle Universal Installer creates the Oracle Inventory directory in the path `/u[01-09]/app/oraInventory`. For example:

```
/u01/app/oraInventory
```

If you have set `ORACLE_BASE` for the `oracle` user during installation, then Oracle Universal Installer creates the Oracle Inventory directory in the path `ORACLE_BASE/../oraInventory`. For example, if `ORACLE_BASE` is set to `/u01/app/oracle/`, then the Oracle Inventory directory is created in the path `/u01/app/oraInventory`.

If you have created neither an OFA-compliant path nor set `ORACLE_BASE`, then the Oracle Inventory directory is placed in the home directory of the user that is performing the installation. For example:

```
/home/oracle/oraInventory
```

Oracle Universal Installer creates the directory that you specify and sets the correct owner, group, and permissions for it. You do not have to create it.

Note:

- All Oracle software installations rely on this directory. Ensure that you back it up regularly.
- Do not delete this directory unless you have completely removed all Oracle software from the system.
- By default, the Oracle Inventory directory is not installed under the Oracle Base directory. This is because all Oracle software installations share a common Oracle Inventory, so there is only one Oracle Inventory for all users. Whereas, there is a separate Oracle Base for each user.

### 2.5.3 Oracle Home Directory

The Oracle home directory is the directory where you choose to install the software for a particular Oracle product. You must install different Oracle products, or different releases of the same Oracle product, in separate Oracle home directories. When you run Oracle Universal Installer, it prompts you to specify the path to this directory, and a name that identifies it. In accordance with the OFA guidelines, Oracle strongly recommends that the Oracle home directory you specify is a subdirectory of the Oracle base directory for the user account performing the installation. Oracle recommends that you specify a path similar to the following for the Oracle home directory:

```
$ORACLE_BASE/product/11.2.0/client_1
```

Oracle Universal Installer creates the directory path that you specify under the Oracle base directory. It also sets the correct owner, group, and permissions on it. You do not have to create this directory.

Caution:

During installation, you must not specify an existing directory that has predefined permissions applied to it as the Oracle home directory. If you do, then you may experience installation failure due to file and group ownership permission errors.

## 2.6 Identifying or Creating an Oracle Base Directory

Before starting the installation, you must either identify an existing Oracle base directory or if required, create one. This section contains information about the following:

- Identifying an Existing Oracle Base Directory
- Creating an Oracle Base Directory

Note:

You can choose to create an Oracle base directory, even if other Oracle base directories exist on the system.

### 2.6.1 Identifying an Existing Oracle Base Directory

Existing Oracle base directories may not have paths that follow OFA guidelines. However, if you identify an existing Oracle Inventory directory or existing Oracle home directories, then you can usually identify the Oracle base directories, as follows:

- Identifying an existing Oracle Inventory directory
	Enter the following command to view the contents of the `oraInst.loc` file:
	```
	# more /etc/oraInst.loc
	```
	If the `oraInst.loc` file exists, then the output from this command is similar to the following:
	```
	inventory_loc=/u01/app/oraInventory
	inst_group=oinstall
	```
	The `inventory_loc` parameter identifies the Oracle Inventory directory (`oraInventory`). The parent directory of the `oraInventory` directory is typically an Oracle base directory. In the previous example, `/u01/app/oracle` is an Oracle base directory.
- Identifying existing Oracle home directories
	Enter the following command to view the contents of the `oratab` file:
	```
	# more /etc/oratab
	```
	If the `oratab` file exists, then it contains lines similar to the following:
	```
	*:/u03/app/oracle/product/11.2.0/dbhome_1:N
	*:/opt/orauser/infra_904:N
	*:/oracle/9.2.0:N
	```
	The directory paths specified on each line identify Oracle home directories. Directory paths that end with the user name of the Oracle software owner to use are valid choices for an Oracle base directory. If you intend to use the `oracle` user to install the software, then you could choose one of the following directories from the previous example:
	```
	/u03/app/oracle
	/oracle
	```
	Note:
	If possible, choose a directory path similar to the first (`/u03/app/oracle`). This path complies with the OFA guidelines.
- Identifying existing Oracle base directories
	After you have located the Oracle home directory, run a similar command to confirm the location of Oracle base:
	```
	cat /u01/app/oraInventory/ContentsXML/inventory.xml
	```

To continue:

- If an Oracle base directory exists and you want to use it, then refer to the "Configuring Oracle Software Owner Environment" section.
	When you configure the `oracle` user's environment later in this chapter, set the `ORACLE_BASE` environment variable to specify the directory you chose.
- If an Oracle base directory does not exist on the system or to create an Oracle base directory, refer to the following section.

### 2.6.2 Creating an Oracle Base Directory

Before you create an Oracle base directory, you must identify an appropriate file system with disk space.

To identify an appropriate file system:

1. To determine the free disk space on each mounted file system use the following command:
	```
	# df -h
	```
2. From the display, identify a file system that has appropriate free space.
3. Note the name of the mount point directory for the file system that you identified.

To create the Oracle base directory and specify the correct owner, group, and permissions for it:

1. Enter commands similar to the following to create the recommended subdirectories in the mount point directory that you identified and set the appropriate owner, group, and permissions on them:
	```
	# mkdir -p /mount_point/app
	# chown -R oracle:oinstall /mount_point/app
	# chmod -R 775 /mount_point/app/
	```
	For example:
	```
	# mkdir -p /u01/app
	# chown -R oracle:oinstall /u01/app
	# chmod -R 775 /u01/app/
	```
2. When you configure the `oracle` user's environment later in this chapter, set the `ORACLE_BASE` environment variable to specify the Oracle base directory that you have created.

## 2.7 Configuring Oracle Software Owner Environment

You run Oracle Universal Installer from the `oracle` account. However, before you start Oracle Universal Installer you must configure the environment of the `oracle` user. To configure the environment, you must:

- Set the default file mode creation mask (umask) to 022 in the shell startup file.
- Set the `DISPLAY` environment variable.

Note:

Ensure that the `PATH` variable contains `$ORACLE_HOME/bin` before `/usr/X11R6/bin`.

Caution:

Use shell programs supported by your operating system vendor. If you use a shell program that is not supported by your operating system, then you can encounter errors during installation.

To set the `oracle` user's environment:

1. Start a new X terminal session (`xterm`).
2. Enter the following command to ensure that X Window applications can display on this system:
	```
	$ xhost fully_qualified_remote_host_name
	```
	For example:
	```
	$ xhost somehost.example.com
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
7. If you are not installing the software on the local system, then enter a command similar to the following to direct X applications to display on the local system:
	- Bourne, Bash, or Korn shell:
		```
		$ DISPLAY=local_host:0.0
		```
		- C shell:
		```
		% setenv DISPLAY local_host:0.0
		```
	In this example, `local_host` is the host name or IP address of the system to use to display Oracle Universal Installer (your workstation or PC).
8. If you determined that the `/tmp` directory has less than 400 MB of free disk space, then identify a file system with at least 400 MB of free space and set the `TMP` and `TMPDIR` environment variables to specify a temporary directory on this file system:
	1. To determine the free disk space on each mounted file system, use the following command:
		```
		# df -k
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
9. Enter the following commands to ensure that the `ORACLE_HOME` and `TNS_ADMIN` environment variables are not set:
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
		Also, ensure that the `$ORACLE_HOME/bin` path is removed from your `PATH` environment variable.
	Note:
	If the `ORACLE_HOME` environment variable is set, then Oracle Universal Installer uses the value that it specifies as the default path for the Oracle home directory. However, if you set the `ORACLE_BASE` environment variable, then Oracle recommends that you unset the `ORACLE_HOME` environment variable and choose the default path suggested by Oracle Universal Installer.
10. To verify that the environment has been set correctly, enter the following commands:
	```
	$ umask
	$ env | more
	```
	Verify that the `umask` command displays a value of `22`, `022`, or `0022` and the environment variables that you set in this section have the correct values.