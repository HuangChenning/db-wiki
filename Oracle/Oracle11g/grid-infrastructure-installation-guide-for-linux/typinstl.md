---
title: Typical Installation for Oracle Grid Infrastructure for a Cluster
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/typinstl.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## 1 Typical Installation for Oracle Grid Infrastructure for a Cluster

This chapter describes the difference between a Typical and Advanced installation for Oracle Grid Infrastructure for a cluster, and describes the steps required to complete a Typical installation.

This chapter contains the following sections:

## 1.1 Typical and Advanced Installation

There are two installation options for Oracle Grid Infrastructure installations:

- Typical Installation: The Typical installation option is a simplified installation with a minimal number of manual configuration choices. Oracle recommends that you select this installation type for most cluster implementations.
- Advanced Installation: The Advanced Installation option is an advanced procedure that requires a higher degree of system knowledge. It enables you to select particular configuration choices, including additional storage and network choices, use of operating system group authentication for role-based administrative privileges, integration with IPMI, or more granularity in specifying Oracle Automatic Storage Management roles.

## 1.2 Preinstallation Steps Completed Using Typical Installation

With Oracle Clusterware 11g Release 2 (11.2), during installation Oracle Universal Installer (OUI) generates Fixup scripts (`runfixup.sh`) that you can run to complete required preinstallation steps.

Fixup scripts are generated during installation. You are prompted to run scripts as `root` in a separate terminal session. When you run scripts, they complete the following configuration tasks:

- If necessary, sets kernel parameters required for installation and runtime to at least the minimum value.
- Reconfigures primary and secondary group memberships for the installation owner, if necessary, for the Oracle Inventory directory and the operating system privileges groups.
- Sets shell limits if necessary to required values.

## 1.3 Preinstallation Steps Requiring Manual Tasks

Complete the following manual configuration tasks

- Verify System Requirements
- Check Network Requirements
- Check Operating System Packages
- Create Groups and Users
- Check Storage
- Prepare Storage for Oracle Automatic Storage Management
- Install Oracle Grid Infrastructure Software

See Also:

[Chapter 2, "Advanced Installation Oracle Grid Infrastructure for a Cluster Preinstallation Tasks"](prelinux.md) and [Chapter 3, "Configuring Storage for Oracle Grid Infrastructure for a Cluster and Oracle RAC"](storage.md) if you need any information about how to complete these tasks

### 1.3.1 Verify System Requirements

Enter the following commands to check available memory:

```
grep MemTotal /proc/meminfo
grep SwapTotal /proc/meminfo
```

Ensure that swap space is greater than or equal to the minimum size required for installation as described in the following tables:

Table 1-1 Swap Space Required for 64-bit Linux and Linux on System z

| Available RAM | Swap Space Required |
| --- | --- |
| Between 2.5 GB and 32 GB | Equal to the size of RAM |
| More than 32 GB | 32 GB of RAM |

If the swap space and the Grid home are on the same filesystem, then add together their respective requirements for the total minimum space required.

```
df -h
```

This command checks the available space on file systems. If you use normal redundancy for Oracle Clusterware files, which is three Oracle Cluster Registry (OCR) locations and three voting disk locations, then you should have at least 2 GB of file space available on shared storage volumes reserved for Oracle Grid Infrastructure files.

Note:

You cannot install OCR or voting disk files (Oracle Clusterware files) on raw partitions. You can install only on Oracle ASM, or on a supported storage option. The only use for raw devices is as Oracle ASM disks.

If you plan to install on Oracle ASM, then to ensure high availability of OCR or voting disk files on Oracle ASM, you need to have at least 2 GB of for Oracle Clusterware files in three separate failure groups, with at least three physical disks. Each disk must have at least 1 GB of capacity to ensure that there is sufficient space to create Oracle Clusterware files.

Ensure you have at least 6.5 GB of space for the Oracle Grid Infrastructure for a Cluster home (Grid home). This includes Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) files and log files, ACFS log files, and includes the Cluster Health Monitor repository.

```
df -h /tmp
```

Ensure that you have at least 1 GB of space in `/tmp`. If this space is not available, then increase the size, or delete unnecessary files in `/tmp`.

Note:

Cluster Health Monitor is not available with IBM: Linux on System z.

See Also:

[Section 2.6, "Checking the Hardware Requirements"](prelinux.md) for more information

### 1.3.2 Check Network Requirements

Ensure that you have the following available:

- Single Client Access Name (SCAN) for the Cluster
- IP Address Requirements
- Redundant Interconnect Usage
- Intended Use of Network Interfaces

#### 1.3.2.1 Single Client Access Name (SCAN) for the Cluster

During Typical installation, you are prompted to confirm the default Single Client Access Name (SCAN), which is used to connect to databases within the cluster irrespective of which nodes they are running on. By default, the name used as the SCAN is also the name of the cluster. The default value for the SCAN is based on the local node name. If you change the SCAN from the default, then the name that you use must be globally unique throughout your enterprise.

In a Typical installation, the SCAN is also the name of the cluster. The SCAN and cluster name must be at least one character long and no more than 15 characters in length, must be alphanumeric, cannot begin with a numeral, and may contain hyphens (-).

For example:

```
NE-Sa89
```

If you require a SCAN that is longer than15 characters, then be aware that the cluster name defaults to the first 15 characters of the SCAN.

#### 1.3.2.2 IP Address Requirements

Before starting the installation, you must have at least two interfaces configured on each node: One for the private IP address and one for the public IP address.

##### 1.3.2.2.1 IP Address Requirements for Manual Configuration

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

Note:

Oracle strongly recommends that you do not configure SCAN VIP addresses in the hosts file. Use DNS resolution for SCAN VIPs. If you use the hosts file to resolve SCANs, then you will only be able to resolve to one IP address and you will have only one SCAN address.

See Also:

[Appendix D](concepts.md), ["Understanding Network Addresses"](concepts.md) for more information about network addresses

#### 1.3.2.3 Redundant Interconnect Usage

In previous releases, to make use of redundant networks for the interconnect, bonding, trunking, teaming, or similar technology was required. Oracle Grid Infrastructure and Oracle RAC can now make use of redundant network interconnects, without the use of other network technology, to enhance optimal communication in the cluster. This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).

Redundant Interconnect Usage enables load-balancing and high availability across multiple (up to 4) private networks (also known as interconnects).

#### 1.3.2.4 Intended Use of Network Interfaces

During installation, you are asked to identify the planned use for each network interface that OUI detects on your cluster node. You must identify each interface as a public or private interface, or as "do not use." For interfaces that you plan to have used for other purposes—for example, an interface dedicated to a network file system—you must identify those instances as "do not use" interfaces, so that Oracle Clusterware ignores them.

Redundant Interconnect Usage cannot protect interfaces used for public communication. If you require high availability or load balancing for public interfaces, then use a third party solution. Typically, bonding, trunking or similar technologies can be used for this purpose.

You can enable Redundant Interconnect Usage for the private network by selecting multiple interfaces to use as private interfaces. Redundant Interconnect Usage creates a redundant interconnect when you identify more than one interface as private. This functionality is available starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.2).

### 1.3.3 Check Operating System Packages

Refer to the tables listed in [Section 2.8, "Identifying Software Requirements"](prelinux.md) for the list of required packages for your operating system, or use a system configuration script such as the Oracle Preinstallation RPM, as described in [Section 2.1, "About Installing the Linux Operating System"](prelinux.md).

### 1.3.4 Create Groups and Users

Enter the following commands to create default groups and users:

One system privileges group for all operating system-authenticated administration privileges, including Oracle RAC (if installed):

```
# groupadd -g 1000 oinstall
# groupadd -g 1031 dba
# useradd -u 1101 -g oinstall -G dba oracle
# mkdir -p  /u01/app/11.2.0/grid
# mkdir -p /u01/app/oracle
# chown -R oracle:oinstall /u01
# chmod -R 775 /u01/
```

This set of commands creates a single installation owner, with required system privileges groups to grant the OraInventory system privileges (oinstall), and to grant the OSASM/SYSASM and OSDBA/SYSDBA system privileges. It also creates the Oracle base for both Oracle Grid Infrastructure and Oracle RAC, `/u01/app/oracle`. It creates the Grid home (the location where Oracle Grid Infrastructure binaries are stored), `/u01/app/11.2.0/grid`.

### 1.3.5 Check Storage

You must have space available on Oracle ASM for Oracle Clusterware files (voting disks and Oracle Cluster Registries), and for Oracle Database files, if you install standalone or Oracle Real Application Clusters Databases. Creating Oracle Clusterware files on block or raw devices is no longer supported for new installations.

Note:

When using Oracle ASM for either the Oracle Clusterware files or Oracle Database files, Oracle creates one Oracle ASM instance on each node in the cluster, regardless of the number of databases.

### 1.3.6 Prepare Storage for Oracle Automatic Storage Management

Install the Linux ASMLIB RPMs to simplify storage administration. ASMLIB provides persistent paths and permissions for storage devices used with Oracle ASM, eliminating the need for updating `udev` or `devlabel` files with storage device paths and permissions.

If you cannot install the ASMLIB RPMs, or choose to configure your storage devices manually, then review the relevant sections in Chapter 3.

See Also:

[Chapter 3, "Configuring Storage for Oracle Grid Infrastructure for a Cluster and Oracle RAC"](storage.md) if you require detailed storage configuration information, or require more information about ASMLIB

ASMLIB 2.0 is delivered as a set of three Linux packages:

- `oracleasmlib-2.0` - the Oracle ASM libraries
- `oracleasm-support-2.0` - utilities needed to administer ASMLIB
- `oracleasm` - a kernel module for the Oracle ASM library

Each Linux distribution has its own set of ASMLIB 2.0 packages, and within each distribution, each kernel version has a corresponding `oracleasm` package.

#### 1.3.6.1 Installing ASMLIB Packages Automatically with ULN

If you are registered with the Oracle Unbreakable Linux Network (ULN), then you can download and install ASMLIB packages for your system automatically. To install ASMLIB from ULN:

1. Log in as `root`.
2. Run the following command:
	```
	# up2date -i oracleasm-support oracleasmlib oracleasm-'uname -r'
	```
	This command installs the support tools, the library, and the kernel driver for the Linux kernel version running on your system.

#### 1.3.6.2 Installing ASMLIB Packages Manually

If you are not a member of ULN, or are using a Red Hat or SUSE Linux kernel, then complete the following procedures on each node that you intend to make a member of the cluster:

- Determine the Correct Oracleasm Package
- Download and Install the Oracleasm Package
- Configure ASMLIB

##### 1.3.6.2.1 Determine the Correct Oracleasm Package

Determine which kernel you are using by logging in as `root` and running the following command:

```
uname -rm
```

For example:

```
# uname –rm
2.6.9-5.ELsmp i686
```

The example shows that this is a 2.6.9-5 kernel for an SMP (multiprocessor) server using Intel i686 CPUs.

##### 1.3.6.2.2 Download and Install the Oracleasm Package

After you determine the kernel version for your system, complete the following task:

1. Open a Web browser using the following URL:
	```
	http://www.oracle.com/technetwork/server-storage/linux/downloads/index-088143.html
	```
2. Click Linux Drivers for Automatic Storage Management, and select the ASMLIB link for your version of Linux.
3. Download the `oracleasmlib` and `oracleasm-support` packages for your version of Linux.
4. Download the `oracleasm` package corresponding to your kernel version.
5. Log in as `root` and install the Oracle ASM packages.

##### 1.3.6.2.3 Configure ASMLIB

Log in as `root`, and enter the following command:

```
# oracleasm configure -i
```

Provide information as prompted for your system. the `oracleasm` command by default is in the path `/usr/sbin`. If you enter the command `oracleasm configure` without the `-i` flag, then you are shown the current configuration.

See Also:

[Section 3.3.1.4.1, "Installing and Configuring the Oracle ASM Library Driver Software"](storage.md) for additional information about configuration

#### 1.3.6.3 Mark Oracle ASM Candidate Disk Partitions

For OUI to recognize partitions as Oracle ASM disk candidates, you must log in as `root` and mark the disk partitions that Oracle ASM can use. To mark a disk for use by Oracle ASM, enter the following command syntax, where `ASM_DISK_NAME` is the name of the Oracle ASM disk group, and `candidate_disk` is the name of the disk device that you want to assign to that disk group:

```
oracleasm createdisk ASM_DISK_NAME candidate_disk
```

For example:

```
# oracleasm createdisk data1 /dev/sdf
```

### 1.3.7 Install Oracle Grid Infrastructure Software

1. Start OUI from the root level of the installation media. For example:
	```
	./runInstaller
	```
2. Select Install and Configure Grid Infrastructure for a Cluster, then select Typical Installation. In the installation screens that follow, enter the configuration information as prompted.
	If you receive an installation verification error that cannot be fixed using a fixup script, then review [Chapter 2, "Advanced Installation Oracle Grid Infrastructure for a Cluster Preinstallation Tasks"](prelinux.md) to find the section for configuring cluster nodes. After completing the fix, continue with the installation until it is complete.

See Also:

[Section 4.1, "Preparing to Install Oracle Grid Infrastructure with OUI."](crsunix.md)