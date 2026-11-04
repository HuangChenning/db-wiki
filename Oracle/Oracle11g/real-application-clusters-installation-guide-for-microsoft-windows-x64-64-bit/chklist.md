---
title: Preinstallation Checklist
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/chklist.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 1 Preinstallation Checklist

Most Oracle Real Application Clusters (Oracle RAC) installation errors are due to a failure to complete all the required steps before starting Oracle Universal Installer (OUI).

This chapter assists database administrators and the system and storage administrators with coordinating the installation and planning the installation tasks in preparation for a complete installation of Oracle RAC.

This chapter contains the following topics:

## 1.1 Before You Start: Planning Your Installation

Oracle recommends that you complete the following list of tasks before you start an Oracle RAC installation. Whether your location is a Tier IV data center with a large project team of system, storage, network, and database administrators and third-party hardware and software vendors, or you are a project team of one, planning is important to help ensure that your installation proceeds smoothly.

It is beyond the scope of this documentation set to advise how to determine hardware sizing or capacity planning for your installation. Note that with Oracle Clusterware and Oracle RAC, you can add nodes and instances as needed in response to testing, or in response to increased workloads.

Review and complete the following steps as part of your installation plan:

- Check My Oracle Support
- Consider Using Software Updates Option
- Check Oracle Technology Network
- Review Installation Steps for Oracle RAC
- Review How to Use Cluster Verification Utility (CVU)
- Review and Back Up Existing Oracle Installations
- Review Globalization Requirements
- Review Documentation

### 1.1.1 Check My Oracle Support

Before you decide whether you want to install Oracle Database 11g release 2 (11.2) on existing hardware or purchase additional server and storage hardware for an installation, log on to My Oracle Support:

`https://support.oracle.com`

My Oracle Support contains guidance about supported hardware options that can assist you with your purchasing decisions and installation planning. The My Oracle Support certifications page contains more detailed information about certified hardware and has information specific to each release and platform. My Oracle Support is available at the following URL:

`http://support.oracle.com/`

You must register online before using My Oracle Support. Use the following steps to locate the certification information for your platform:

1. After logging in, click the Certifications tab.
2. In Certification Search box, enter information about your software and hardware. For example, you might use the following:
	- Product: Oracle Database
		- Release: 11.2.0.3
		- Platform: Microsoft Windows x64 (64-bit) 2008 R2
	After entering the required information, press Search. A new window appears with the product certification details.
3. On the Certification Details page, click the links to view certification information and ensure that your hardware configuration is supported for use with Oracle Clusterware and Oracle RAC.

Note:

Contact your Oracle sales representative if you do not have a My Oracle Support account.

Also, you may want to visit Oracle.com (`http://www.oracle.com`) for additional resources about planning for specific implementation scenarios, best practices, and other information that can help you with your installation plan. In particular, see the Oracle Real Application Clusters pages on the Oracle Technology Network:

`http://www.oracle.com/technetwork/database/clustering/overview/`

The Oracle RAC Technologies Certification Matrix provides details about supported technology that you can use to deploy Oracle RAC.

### 1.1.2 Consider Using Software Updates Option

OUI can install critical patch updates, system requirement updates for supported operating systems, and other significant updates that can ensure that your installation succeeds. Oracle recommends that you enable the Software Updates option during installation.

If you choose to enable the Software Updates option, then during installation you must provide a valid My Oracle Support user name and password, so that OUI can download the latest updates, or you must provide a path to the location of a Software Updates option package that you have downloaded previously.

In addition, if you have a proxy realm, then be prepared to provide the destination proxy realm, and the user authentication (user name and password) required to authenticate access through that realm to the Internet, so that OUI can obtain software updates. Check with your network administrator before installation if you do not have this information.

If you plan to run the installation in a secured data center, then you can download updates before starting the installation by starting OUI on a system that has Internet access. To start OUI to download updates only, enter the following command:

```
setup.exe -downloadUpdates
```

Provide the My Oracle Support user name and password, and provide proxy settings if needed. After you download updates, transfer the update file to a directory on the server where you plan to run the installation.

### 1.1.3 Check Oracle Technology Network

Oracle Technology Network (OTN) contains white papers about deployment options, capacity planning, best practices, and extended clusters deployments, which are not addressed in this guide. You can review available papers at the following web site:

`http://www.oracle.com/technetwork/database/clustering/overview/`

### 1.1.4 Review Installation Steps for Oracle RAC

Installing Oracle RAC consists of the following steps:

1. Prepare servers (system, storage, and network administration):
	- Install the operating system, operating system packages, and patches to the required version.
		- Create the required groups, users, and software homes.
		- Set up the domain name forwarding for Grid Naming Service (GNS) if you plan to deploy GNS, and set up the network addresses in the domain name service (DNS) and on the server as needed.
		- Set up the required storage.
		- (optional) Stage all the software on one node for installation (also called the local node).
		See Also:
		[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for more information about using OIFCFG to modify interconnects
2. Install Oracle Grid Infrastructure for a cluster, which includes Oracle Clusterware and Oracle Automatic Storage Management (system and storage administration):
	- Install Oracle Grid Infrastructure for a cluster.
		- Patch Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) to the latest patchset.
3. Install Oracle RAC (database administration):
	- Install Oracle RAC.
		- Patch Oracle RAC to the latest patchset.
		- Complete the postinstallation configuration of the Oracle RAC database.

### 1.1.5 Review How to Use Cluster Verification Utility (CVU)

Oracle provides Cluster Verification Utility (CVU) to perform system checks in preparation for an installation, patch updates, or other system changes.

Before installing Oracle Clusterware or Oracle RAC, use CVU to ensure that your cluster is prepared for an installation. CVU is incorporated into OUI, so CVU performs its checks when you start an Oracle RAC installation. However, you can use CVU to ensure that any packages or configuration information that is required for Oracle RAC are in place before you begin your Oracle RAC installation.

Using CVU can help system, storage, and database administrators ensure that all system configuration and preinstallation steps are completed, so that installations, updates, or patches also complete successfully. You can obtain the latest version of CVU at the following URL:

`http://www.oracle.com/technetwork/database/options/clustering/downloads/cvu-download-homepage-099973.html`

If you have vendors performing hardware or operating system configuration steps, then ask the vendors to complete the relevant CVU checks of the cluster after they complete their work to ensure that your system is configured correctly. Database administrators should review "Confirming Cluster Readiness Using Cluster Verification Utility" to confirm that their system is prepared for installation before they start an Oracle RAC installation.

### 1.1.6 Review and Back Up Existing Oracle Installations

If you have an existing Oracle installation, then document version numbers, patches, and other configuration information, and review upgrade procedures for your existing installation. Review the Oracle upgrade documentation before proceeding with your installation, to decide how you want to proceed.

As with any system change, back up your existing database before attempting to install new software.

Note that to install Oracle RAC 11g release 2 (11.2), you must have Oracle Clusterware and Oracle ASM 11g release 2 (11.2) installed on your cluster. The Oracle Clusterware version must be equal to or more recent than the Oracle RAC version that you plan to install.

See Also:

[Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm)

For the most current information and best practices about pre-upgrade, post-upgrade, compatibility, and interoperability discussions, see "Oracle Upgrade Companion", which is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com/`

For upgrades, note the following:

- You can have only one version of Oracle Clusterware running on a cluster at a time. The Oracle Clusterware version must be the most recent release of any software (Oracle Clusterware, Oracle Database, Oracle RAC, and Oracle ASM) running on the cluster. Before upgrading your database to Oracle Database 11g release 2, all nodes in the cluster must be upgraded to Oracle Clusterware and Oracle ASM 11g release 2 (11.2).
- You can have multiple Oracle homes for Oracle databases on your cluster. However, the Oracle RAC database software in these homes must be from a version that is equal to or prior to the version of Oracle Clusterware that is installed; you cannot have a version of Oracle Database running on Oracle Clusterware that was released after the version of Oracle Clusterware that you are running.
	For example:
	- If you have Oracle Clusterware 11g release 2 installed as your clusterware, then you can have an Oracle Database 10g release 2 single-instance database running on one node, and separate Oracle RAC 10g release 1, release 2, and Oracle RAC 11g release 1 or release 2 databases also running on the cluster.
		- You cannot have Oracle Clusterware 10g release 2 installed on your cluster, and install Oracle RAC 11g.
- Starting with releases 10.1.0.6 and 10.2.0.3, you can use Database Upgrade Assistant (DBUA) for patch set upgrades with Oracle RAC. You can also use DBUA to upgrade between major point releases of Oracle RAC (for example, from 10.2 to 11g, or 11.1 to 11.2).
- You cannot change the owner of the Oracle Database home during an upgrade. You must use the same Oracle software owner that owns the existing Oracle Database home.
- For the Oracle RAC database being upgraded, each cluster member node that hosts an instance of the database must be a member of the upgraded installation. For example, if you have an existing Oracle RAC database running on a three-node cluster, then you must upgrade Oracle RAC on all three nodes. You cannot upgrade only two nodes of the cluster, and then remove the third node and instance in the upgrade.

Note:

If you are upgrading an existing Oracle RAC installation, then you must use the same type of Oracle home that you have in your existing installation. For example, if you have a shared Oracle home in your existing installation, then you must upgrade to a shared Oracle home with Oracle RAC 11g release 2 (11.2).

Similarly, if you have local Oracle homes on cluster nodes, then you must upgrade to local Oracle homes on cluster nodes.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about how to prepare for upgrading an existing database

### 1.1.7 Review Globalization Requirements

Before you start an installation on which you want to support languages other than English, review Oracle Database Globalization Support Guide.

Note the following:

- Oracle recommends that you use Unicode AL32UTF8 as the database character set.
	Unicode is the universal character set that supports most of the currently spoken languages. Unicode also supports many historical scripts (alphabets). Unicode is the native encoding of many technologies, including Java, XML, XHTML, ECMAScript, and LDAP. Unicode is ideally suited for databases connected to the Internet and the global economy.
- The locale setting of your operating system session determines the language of the user interface and the globalization behavior for components such as OUI, Oracle Net Configuration Assistant (NETCA), and Oracle Database Configuration Assistant (DBCA). The locale setting also determines the globalization behavior of Oracle Database sessions created by a user application through the JDBC driver, unless overridden by the application.
- The character set specified by the `NLS_LANG` environment variable determines the language of the user interface and the globalization behavior for components such as SQL\*Plus, `exp`, and `imp`. This variable also sets the language and territory used by the client application and the database. The `NLS_LANG` environment variable also declares the character set for entering and displaying data by the client application.
	The `NLS_LANG` environment variable should reflect the setting of the operating system character set of the client. For example, if the database character set is AL32UTF8 and the client is running on a Windows operating system, then you should not set the NLS\_LANG environment variable to AL32UTF8 because there are no UTF-8 WIN32 clients. Instead, the `NLS_LANG` setting should reflect the code page of the client. For example, on an English Windows client, the code page is 1252, so an appropriate setting for `NLS_LANG` is `AMERICAN_AMERICA.WE8MSWIN1252`.

Note:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform contains a more detailed discussion of database character sets used with different languages, and provides more information about installing and configuring Oracle Database globalization support.

### 1.1.8 Review Documentation

Before installing Oracle RAC, review the Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit), particularly the preinstallation, and the storage chapters, to complete all the required steps for an installation.

Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit) also contains most tasks requiring Administrator privileges or storage administrator privileges that must be completed before starting an Oracle RAC installation.

In addition, review the Release Notes and My Oracle Support (`https://support.oracle.com`) to ensure that you have the most current information about system requirements and other information that can affect your installation. The small amount of time that this review takes can save a much greater amount of time required to track down causes of installation errors later. Also, verify that you have the most current version of this document; Oracle documentation is updated after the initial release and posted to the following web site:

```
http://docs.oracle.com/
```

Oracle recommends that you install a web browser on at least one of your cluster nodes to enable Oracle Enterprise Manager and Oracle Application Express for Oracle RAC, and to access online documentation as needed. Online documentation is available in PDF and HTML formats and can be downloaded.

See Also:

- Oracle Database Concepts for an overview of Oracle Database
- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admcon.htm#RACAD1111) for additional information about Oracle Clusterware or Oracle RAC configuration and deployment
- [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) for server and storage configuration information for Oracle RAC

## 1.2 Overview of Server Hardware, Network, and Operating System

Oracle Clusterware must be installed successfully as part of an Oracle Grid Infrastructure for a cluster installation before attempting to install Oracle RAC. To complete installations successfully, ensure that required hardware, network, and operating system preinstallation steps for Oracle software are performed as required. Failure to complete the required preinstallation steps is the most common reason for unsuccessful installations.

Before Oracle Clusterware is installed as part of an Oracle Grid Infrastructure for a cluster installation, you must have completed installing and configuring CPUs, memory, shared storage, local disks, network cards, host bus adapters, interconnects, and any other networking or server hardware. You should also have installed the operating system, and any required packages or third-party software. Review your vendor documentation to complete these tasks, and if relevant, work with your vendor to complete the Oracle preinstallation steps that are listed in this document to confirm that the vendor hardware and software is correctly configured.

Server and network preparation for installation includes the following:

- Review Server Hardware and Software Requirements
- Overview of Server Environment Configuration
- Overview of Oracle Base
- Overview of Network and Internet Configuration
- Overview of Platform-Specific Server Configuration

### 1.2.1 Review Server Hardware and Software Requirements

The following summary of server hardware and software configuration requirements and recommendations will enable you to prepare for a successful installation of Oracle RAC.

Required for Oracle RAC

Each node in a cluster requires the following:

- Supported server hardware, including processors and system configuration.
	Review My Oracle Support before starting an installation on your current hardware and before purchasing new hardware to ensure that the hardware is supported by Oracle Clusterware with Oracle RAC 11g release 2 (11.2).
	Also review the preinstallation chapters in [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit) f](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) or more details about the supported configurations.
	Note:
	You must use the same operating system on each node in the cluster. Oracle strongly recommends that you use the same software configurations on each node of the cluster. Oracle Clusterware and Oracle RAC do not support heterogeneous platforms (each server must run the same Oracle software binaries) in the same cluster.
- Operating system updates listed in the system requirements.
	Oracle may require updates to the operating system, such as service packs and individual patches. If such requirements exist, then they are stated in the Release Notes for a particular release. You can also apply other operating system patches as recommended by Microsoft, if there are no "certification exceptions" listed in the Release Notes.
- A supported interconnect software protocol on each node, to support Oracle Clusterware voting disk polling, and to support Cache Fusion with Oracle RAC. Your interconnect must be certified by Oracle for your platform.

Recommended for Oracle RAC: System Administrator Tasks

Oracle recommends the following tasks to simplify server installation and maintenance, and to prevent service issues:

- Utilizing a time protocol, such as Network Time Protocol (NTP), to ensure that all nodes in the cluster use the same reference time. With Oracle Clusterware 11g release 2 (11.2), if neither the Network Time Protocol or Windows Time Service is enabled at installation, then the Oracle Clusterware installation enables the Cluster Time Synchronization Service (CTSS).
- Configuring redundant switches, for all cluster sizes.
- Using identical server hardware on each node, to simplify server maintenance.
- Avoiding resource contention issues by not installing Oracle RAC on a primary domain controller or backup domain controller.

Additional Options: System Administrators and Vendors

After you have set up server hardware, review "Checking the Hardware Requirements" in Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit) to ensure that your system has enough RAM, that the `TEMP` environment variable points to a location that has enough available space for the installation, and that your system meets other hardware requirements.

### 1.2.2 Overview of Server Environment Configuration

Configure the users and user environments as described in the preinstallation chapters of [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm). These include the following tasks:

- Creating operating system users to install Oracle software
- Configuring the Oracle software owner user environments

See Also:

[Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/external.htm#NTQRF130) for information about creating user groups

To install the Oracle software, you must be a user that is a member of the Administrators group. If you use a local user account for the installation, then the user account must exist on all nodes in the cluster and the user name and password must be the same on all nodes.

If you use a domain account for the installation, then the domain user must be explicitly declared as a member of the local Administrators group on each node in the cluster. It is not sufficient if the domain user has inherited membership from another group. The user performing the installation must be in the same domain on each node. For example, you cannot have a `dba1` user on the first node in the `DBADMIN` domain and a `dba1` user on the second node in the `RACDBA` domain.

Assume that you have one Oracle installation owner, and the user name for this Oracle installation owner is `oracle`. The `oracle` user must be either a local Administrator user or a domain user, and the same user must exist (same user name, password, and domain) on each node in the cluster.

When installing the Oracle Database software, the user performing the installation is automatically added to the `ORA_DBA` group. If you use a domain user, then after installation you must ensure that the domain user on each node is a member of the local Administrator's group and the `ORA_DBA` group.

Members of the local `ORA_DBA` group automatically receive the SYSDBA and SYSASM privileges.

Note:

If you use a domain user to perform the installation, then in some cases you must manually add the user to `ORA_DBA` group of the remote nodes after installation completes.

Oracle strongly recommends the use of domain users for Oracle RAC installations.

See Also:

[Oracle Database Installation Guide for Microsoft Windows](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about the `ORA_DBA` group

### 1.2.3 Overview of Oracle Base

The Oracle base directory is the location where Oracle software and configuration files are stored. By default, the Oracle software binary files are installed by version and Oracle home name in a subdirectory of the Oracle base directory. An Oracle base directory can be used for multiple installations.

Every Oracle home can have its own Oracle base. Typically, the Oracle base path is based on the installation owner name. If you have separate installation owners for the Oracle Grid Infrastructure installation and the Oracle RAC installation, then you have two Oracle base paths that are in accordance with Optimal Flexible Architecture (OFA) guidelines. For example, if the user `grid` is the installation owner of the Oracle Grid infrastructure installation and the user `oracle` is the installation owner of the Oracle Database installation, then you have two Oracle base directories:

- `X:\app\grid` —the Oracle base for the user `grid`, which owns the Oracle Grid Infrastructure binaries
- `X:\app\oracle` —the Oracle base for the user `oracle`, which owns the Oracle Database binaries

In preparation for installation, Oracle recommends that you only set the `ORACLE_BASE` environment variable to define paths for Oracle binaries and configuration files. Oracle Universal Installer (OUI) creates other paths and environment variables as necessary, in accordance with the Optimal Flexible Architecture (OFA) rules for well-structured Oracle software environments.

For example, with Oracle Database 11g, Oracle recommends that you do not set an Oracle home environment variable, and instead enable OUI to create it. If the Oracle base path is `E:\app\oracle`, then by default, OUI creates the following Oracle home path:

```
X:\app\oracle\product\11.2.0\dbhome_n
```

The variable n is the Oracle home number. The first time you create an Oracle home as the oracle user, the default Oracle home location is `C:\app\oracle\product\11.2.0\dbhome_1`.

Ensure that the paths that you select for Oracle software, such as Oracle home paths and the Oracle base path, use only ASCII characters. Because installation user names are used by default for some path, this ASCII character restriction applies to user names, file names, and directory names.

### 1.2.4 Overview of Network and Internet Configuration

You must configure each server so it can communicate with the other nodes in the cluster. Also, you should configure one or more nodes to access the internet and support a web browser.

#### 1.2.4.1 Overview of Network Interface Configuration

During the installation of Oracle Grid Infrastructure for a cluster, the person completing the installation identifies the planned use for each global interface, identifying each interface as a Public interface type (used with public IP addresses and virtual IP addresses), a Private interface type (used with interconnects between cluster member nodes), or a Do not use interface type, which Oracle Clusterware and Oracle RAC should ignore. For example, an interface used as a dedicated interface for a network file system should be marked as a Do not use interface type.

Additional network configuration is not required during an Oracle RAC configuration.

#### 1.2.4.2 Overview of Configuring Internode Communication

The Oracle software is installed on one node in the cluster and then OUI copies the software to the other nodes in the cluster. Verify that each node in your cluster can communicate with the other nodes using the `net use` command, for example, on `node1` you would use the following command:

```
C:\> net use \\node2\c$
The command completed successfully.
```

On node2, you would use the following command:

```
C:\> net use \\node1\c$
The command completed successfully.
```

#### 1.2.4.3 Overview of Browser Requirements

You need a web browser to access documentation, and to use Oracle Enterprise Manager and Oracle Application Express. Web browsers must support JavaScript and the HTML 4.0 and Cascading Style Sheets (CSS) 1.0 standards. The following browsers meet these requirements:

- Microsoft Internet Explorer 10 (supports Oracle Enterprise Manager Database Control 11.2.0.3 or higher)
- Microsoft Internet Explorer 9.0
- Microsoft Internet Explorer 8.0
- Microsoft Internet Explorer 7.0 SP1
- Microsoft Internet Explorer 6.0 SP2
- Firefox 21.0 (supports Oracle Enterprise Manager Database Control 11.2.0.4)
- Firefox 17.0.6 ESR (supports Oracle Enterprise Manager Database Control 11.2.0.4)
- Firefox 3.6
- Firefox 3.5
- Safari 4.0.x
- Safari 3.2
- Safari 3.1
- Google Chrome 27.0 (supports Oracle Enterprise Manager Database Control 11.2.0.4)
- Google Chrome 4.0
- Google Chrome 3.0

For a list of browsers supported with Oracle Application Express, see [Oracle Application Express Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e12196/pre_require.htm#HTMIG380).

Note:

You do not require a browser to install Oracle RAC.

### 1.2.5 Overview of Platform-Specific Server Configuration

Oracle Clusterware and Oracle RAC are tested with specific operating system versions, and specific operating system components. Oracle requires that you use the operating system versions and components that are certified for this release.

Oracle recommends that you or your system administrator review the system requirements carefully in [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) before beginning installation, to ensure that your system meets these requirements. If your system does not meet minimum hardware, operating system version, and component requirements, then your installation may fail to complete, or other errors may develop during Oracle Clusterware or Oracle Database run time.

In addition to the standard system requirements configuration, deployment on specific server hardware can include additional operating system configuration steps. Review the preinstallation chapter in [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm), and check the My Oracle Support Certify page to ensure that you are aware of any additional requirements or recommendations for your specific hardware and platform configuration.

## 1.3 Overview of Oracle RAC Storage

For both the Enterprise and Standard Editions of Oracle RAC, the hard disk requirements for Oracle Database components include 32 MB required to install Java Runtime Environment (JRE) and OUI on the disk partition where the operating system is installed. If sufficient space is not detected, then the installation fails and an error message appears. Table 1-1 lists the hard disk space requirements, including the requirements for a starter database.

Table 1-1 Hard Disk Space Requirements for Oracle RAC

| Installation Type | TEMP space | %SYSTEMDRIVE%\\Program Files\\Oracle | Oracle Database Home | Data Files | Total |
| --- | --- | --- | --- | --- | --- |
| Standard Edition | 500 MB | 100 MB | 5 GB | 3 GB | 8.6 GB |
| Enterprise Edition | 500 MB | 100 MB | 5.5 GB | 3 GB | 9.1 GB |

In Table 1-1, the Data Files column refers to the contents of the `admin`, `flash_recovery_area`, and `oradata` directories in the Oracle base directory. The actual size of these files can be greater than what is specified in the table, depending on the installation options selected, such as languages or additional components. If you later plan to install Oracle Database and Oracle Real Application Clusters with automated backups enabled, then include at least an additional 2 GB for data file disk space.

To install Oracle RAC, you must configure shared storage for the database files and optionally the recovery files. If you instruct DBCA to configure automatic backups, the backups require a database recovery area that must be shared.

See Chapter 3 [in Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) to review storage options for installation planning. Storage and system administrators can see this chapter to configure storage for database files for an Oracle RAC database.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11103) for information about recovery areas

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is a new multiplatform, scalable file system, and storage management technology that extends Oracle ASM functionality to support customer files maintained outside of the Oracle Database. Files supported by Oracle ACFS include database and application executable files, trace files, alert logs, application reports, BFILEs, and configuration files. Oracle ACFS leverages Oracle ASM functionality to enable the following:

- Oracle ACFS dynamic file system resizing
- Maximized performance through direct access to Oracle ASM disk group storage
- Balanced distribution of Oracle ACFS across Oracle ASM disk group storage for increased I/O parallelism
- Data reliability through Oracle ASM mirroring protection mechanisms

The Oracle ASM Dynamic Volume Manager (Oracle ADVM) provides volume management services for disks and a standard disk device driver interface to clients (users and applications). File systems and other disk-based applications issue I/O requests to Oracle ADVM volume devices as they would to other storage devices on a vendor operating system. Oracle ADVM extends Oracle ASM by providing a disk driver interface to Oracle ASM storage allocated as Oracle ASM volume files. You can use Oracle ADVM to create virtual disks that contain file systems. These file systems contained on Oracle ASM volumes can support files beyond Oracle database files, such as executable files, report files, trace files, alert logs, and other application data files.

See Also:

- The Certify page on My Oracle Support for the most current information about storage options:
	```
	https://support.oracle.com
	```
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for an overview of storage configuration administration

### 1.3.1 General Storage Considerations for Oracle RAC

For all installations, you must choose the storage option to use for Oracle RAC database files. To enable automated backups during the installation, you must also choose the shared storage option to use for recovery files (the fast recovery area). You do not have to use the same storage option for each file type.

Use the following guidelines when choosing the storage options to use for each file type. You can choose any combination of the supported shared storage options for each file type if you satisfy all requirements listed for the chosen storage options

- Oracle recommends that you choose Oracle ASM as the shared storage option for database and recovery files.
- For Standard Edition Oracle RAC installations, Oracle ASM is the only supported shared storage option for database or recovery files.
- If you do not have a storage option that provides external file redundancy, then you must configure at least three voting disk areas to provide voting disk redundancy.
- If you intend to use Oracle ASM with Oracle RAC and you did not use Oracle ASM for the Oracle Clusterware files (Oracle Cluster Registry (OCR) and voting disk), then you must configure the Oracle ASM instance with Oracle ASM Configuration Assistant (ASMCA) before starting OUI. All nodes in the cluster must have the Oracle Database 11g release 2 version of Oracle Grid Infrastructure installed (Oracle Clusterware and Oracle ASM).
- If you intend to upgrade an existing Oracle RAC database, then you must ensure that your system meets the following conditions:
	- OUI and DBCA are run on the node where the Oracle RAC database instance is located.
		- The Oracle RAC database instance is running on the same nodes that you intend to make members of the new cluster installation. For example, if you have an existing Oracle RAC database running on a three-node cluster, then you must install the upgrade on all three nodes. You cannot upgrade only two nodes of the cluster, removing the third instance in the upgrade.
	See Also:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD12385) for information about how to prepare for upgrading an existing database

### 1.3.2 Overview of Oracle Database and Recovery File Options

There are two ways of storing Oracle Database and recovery files:

Note:

When creating a new Oracle RAC database using OUI, storing data files and recovery files on raw devices (unformatted partitions) is not supported. Place data files and recovery files on a shared file system or on Oracle ASM. If you are upgrading a database that uses raw devices, they are still supported with Oracle Database 11g release 2.
- Oracle Automatic Storage Management: Oracle ASM is an integrated, high-performance database file system and disk manager for Oracle Database files. It performs striping and mirroring of database files automatically.
	Note:
	For Standard Edition Oracle Database installations using Oracle RAC, Oracle ASM is the only supported storage option.
- A supported shared file system: Supported file systems include the following:
	- Oracle Cluster File System (OCFS) for Windows: Note that if you intend to use OCFS for Windows for your database files, then you should create partitions large enough for the all the database and recovery files when you create partitions for use by Oracle Database.
		Note:
		To have a shared Oracle Database home directory for all nodes, you must use a supported cluster file system.
		- Direct Network File Systems (NFS): You can configure Oracle Database to access NFS version 3 (NFSv3) servers directly using Direct NFS. Direct NFS is an optimized NFS client that provides faster and more scalable access to NFS storage located on NAS storage devices (accessible over TCP/IP). Direct NFS is built directly into the database kernel and provides faster performance than what can be provided by the operating system's NFS driver. When accessing NFS servers, Oracle Database bypasses the operating system and generates exactly the requests it needs (no user configuration or tuning required).

Table 1-2 shows the storage options supported for storing Oracle Database files and Oracle Database recovery files. Oracle Database files include data files, control files, redo log files, the server parameter file (SPFILE), and the password file.

Table 1-2 Supported Storage Options for Oracle Database and Recovery Files

<table><thead><tr><th rowspan="2">Storage Option</th><th colspan="2">File Types Supported</th></tr><tr><th headers="r1c1-t21 r1c1-t21">Database</th><th headers="r1c1-t21 r2c1-t21 r1c2-t21">Recovery</th></tr></thead><tbody><tr><td headers="r1c1-t21 r2c1-t21"><p>Oracle ASM</p></td><td headers="r3c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p></td><td headers="r3c1-t21 r1c2-t21"><p>Yes</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Oracle ASM Cluster File System (Oracle ACFS)</p></td><td headers="r4c1-t21 r1c2-t21 r2c2-t21"><p>No</p></td><td headers="r4c1-t21 r1c2-t21"><p>No</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>OCFS for Windows</p></td><td headers="r5c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p></td><td headers="r5c1-t21 r1c2-t21"><p>Yes</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Direct NFS</p></td><td headers="r6c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p></td><td headers="r6c1-t21 r1c2-t21"><p>Yes</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Local storage</p></td><td headers="r7c1-t21 r1c2-t21 r2c2-t21"><p>No</p></td><td headers="r7c1-t21 r1c2-t21"><p>No</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Shared unformatted partitions</p></td><td headers="r8c1-t21 r1c2-t21 r2c2-t21"><p>Not supported by OUI or ASMCA, but supported by Oracle RAC. Raw partitions can be added or removed after installation.</p></td><td headers="r8c1-t21 r1c2-t21"><p>Not supported by OUI or ASMCA, but supported by Oracle RAC. Raw partitions can be added or removed after installation.</p></td></tr></tbody></table>

## 1.4 Requirements for the Oracle Database Vault Option

Oracle Database Vault requires the following:

- An Oracle Database Enterprise Edition installation. Oracle Database Vault cannot be used with Oracle Database Standard Edition.
- The initialization parameter `db_block_size` for the database set to 4096 or higher
	You can specify the initial value for this parameter during installation.
- Oracle Enterprise Manager Database Control.
- Oracle Clusterware installed and running.
- The password file authentication parameter, `REMOTE_LOGIN_PASSWORDFILE`, set set to `EXCLUSIVE` or `SHARED` for the database
	You can specify the initial value for this parameter during installation, or in the Oracle Database initialization file. To create and manage password files, use the `orapwd` utility.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about creating and maintaining a password file

You can install Oracle Database Vault more than once on the same system, in different Oracle homes for different databases.

## 1.5 Additional Information to Prepare for Installation

The following information about Oracle Clusterware, Oracle ASM, and Oracle RAC may be helpful to your installation planning team when deciding how you want to configure your installation. It contains the following topics:

- Oracle ASM Is Installed with Oracle Grid Infrastructure
- Obtain the Oracle ASM ASMSNMP Password for Oracle Enterprise Manager
- Oracle Clusterware and Vendor Clusterware
- Shared Components of Oracle RAC Installations
- Simplified Upgrade of TIMESTAMP WITH TIME ZONE Data
- Oracle Database 11g Real Application Clusters Release Compatibility

### 1.5.1 Oracle ASM Is Installed with Oracle Grid Infrastructure

In past releases, Oracle ASM was installed as part of the Oracle Database installation. With Oracle Database 11g release 2 (11.2), Oracle ASM is part of an Oracle Grid Infrastructure installation. To upgrade an existing Oracle ASM installation, you must upgrade Oracle ASM by running an Oracle Grid Infrastructure upgrade.

If you did not select Oracle ASM as the storage option for the Oracle Clusterware files, then you must first use Oracle ASM Configuration Assistant (ASMCA) to configure Oracle ASM, create an Oracle ASM instance, and create a disk group to use for your Oracle Database storage.

### 1.5.2 Obtain the Oracle ASM ASMSNMP Password for Oracle Enterprise Manager

Obtain the password for the Oracle ASM user ASMSNMP from the Oracle Grid Infrastructure administrator.

During Oracle Grid Infrastructure for a cluster installation, the ASMSNMP account is created and its status is set to OPEN. It is granted the SYSDBA for ASM privilege. Oracle Enterprise Manager requires access to the ASMSNMP account to monitor Oracle ASM instances and retrieve data from ASM-related data dictionary views.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asm_em.htm#OSTMG22700) for additional information about the ASMSNMP account

### 1.5.3 Oracle Clusterware and Vendor Clusterware

Oracle Clusterware provides clustering services. Currently, there are no supported clusterware products other than Oracle Clusterware for the Microsoft Windows platforms. If you intend to install Oracle RAC, then you must first install Oracle Clusterware.

### 1.5.5 Simplified Upgrade of TIMESTAMP WITH TIME ZONE Data

As part of the installation of Oracle Database 11g release 2 (11.2), time zone files from versions 1 to 11 are installed in the path `Oracle_home` `\oracore\zoneinfo`. You can continue to use the current time zone file or upgrade to the latest version. Oracle recommends that you upgrade the server to the latest version of the time zone file. Upgrading to a new version of the time zone file may cause existing TIMESTAMP WITH TIME ZONE (TSTZ) data to become stale. Using the newly provided DBMS\_DST PL/SQL package, you can update the TSTZ data transparently, with minimal manual procedures and system downtime.

All instances of an Oracle RAC database must use the same time zone. The Oracle RAC database time zone defaults to the time zone setting of the Oracle Grid Infrastructure `grid` user, unless an instance is started with SQL\*Plus. When you use SQL\*Plus, you must be sure to use the same time zone setting for the database instance that is used for Oracle Clusterware. You can change the time zone Oracle Clusterware uses for a database by using the following command, where `time zone` is the time zone to which you want to change:

```
srvctl setenv database -T "TZ=time zone"
```

Time zone files are also installed on the client computers. Starting with Oracle Database 11g release 2, you no longer have to upgrade Oracle Client time zone files immediately. Upgrades can be done at a time when it is most convenient to the system administrator. However, there could be a small performance penalty when client and server use different time zone versions.

See Also:

- [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD12399) for information about preparing to upgrade TSTZ data
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG259) for information about how to upgrade the time zone file and TSTZ data
- [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/oci10new.htm#LNOCI16761) for information about performance effects of clients and servers operating with different versions of time zone files

### 1.5.6 Oracle Database 11g Real Application Clusters Release Compatibility

You can install and operate different releases of Oracle Database software on the same computer when all the following conditions are met:

- If you have Oracle Clusterware installed and different releases of other Oracle software installed, then the Oracle Clusterware release must be later than or equal to the Oracle Database software release. Oracle Clusterware and Oracle ASM are both upgraded to release 11.2.0.1 when you perform an Oracle Grid Infrastructure 11g release 2 (11.2) installation.
- If you have an existing Oracle Database home, then you can create a new Oracle Database home and install Oracle Database 11g release 2 (11.2) into the new Oracle home. You should ensure that Oracle Clusterware is in a separate Oracle Grid Infrastructure home (referred to as the Grid home). Oracle Grid Infrastructure installations cannot be installed in the Oracle base directory for Oracle Database.
- If you are running the Oracle9i release of Oracle RAC, and you want to continue to use that release, then you must run cluster software that is compatible with that release, such as Oracle Cluster Manager. Oracle Clusterware release 11g can be installed on the same system as Oracle9i Database software, but Oracle9i Database software cannot be supported by Oracle Clusterware 11g.
- If OUI detects a previous database release, then OUI asks you about your upgrade preferences. You have the option to upgrade a previous release database with DBUA or to create a new database using DBCA. The information collected during this OUI dialog is passed to DBUA or DBCA after the software is installed.
	If OUI detects a previous Oracle Clusterware release, then you are asked to upgrade the existing Oracle Clusterware installation. Only one Oracle Clusterware version can be active on a server, and a server must be a member of only one cluster.
	Note:
	Do not move Oracle binaries from the Oracle home to another location. Doing so can cause dynamic link failures.
- You cannot install Oracle Grid Infrastructure for a standalone server (Oracle Restart) and then install Oracle Grid Infrastructure for a cluster. If you have Oracle Restart installed, then you must remove that installation before you can install Oracle Grid Infrastructure for a cluster.
	Note:
	Do not move Oracle executable files from the directory in which they were installed to another location. To move the executable files to a new location, you must reinstall the software.
- You can run different releases of Oracle Database and Oracle ASM. For example, you can use Oracle ASM release 11g release 2 (11.2) with an Oracle Database 10g release 2 (10.2) database.
	Note:
	When using different Oracle ASM and Oracle Database releases, the functionality of each is dependent on the functionality of the earlier software release. For example, an Oracle Database 10g release 10.2 database using an Oracle ASM 11g release 2 (11.2) instance is not able to use new features available for Oracle ASM 11g release 2 (11.2) release, but instead it can use only Oracle ASM 10.2 features.

See Also:

- [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) for information about using earlier Oracle Database releases with Oracle Grid Infrastructure

## 1.6 Confirming Cluster Readiness Using Cluster Verification Utility

Before you start your Oracle RAC installation, use CVU to ensure that your system is prepared for installing Oracle RAC. If any checks fail, then fix the errors reported, or contact your system or storage administrator to have the cause of the errors addressed.

CVU is available in the Grid home, in the `bin` directory. For example, if the Grid home is `C:\app\11.2.0\grid`, then CVU is located in the `C:\app\11.2.0\grid\bin` directory. To start CVU, go to the `bin` directory in the Grid home, and use a command similar to the following:

```
cluvfy.bat stage -pre dbinst -fixup -n nodelist -r release -verbose
```

In the preceding command, `nodelist` is a comma-delimited list of node names and `release` is the version of the Oracle Database software being installed. The `-fixup` and `-verbose` flags are optional.

For example, for a two node cluster with `node1` and `node2`, where you are testing the cluster to prepare to install Oracle Database 11g release 2 (11.2) with Oracle RAC, the following command checks for system readiness:

```
cluvfy.bat stage -pre dbinst -fixup -n node1,node2 -r 11gR2 -verbose
```

For more information about CVU commands, run the command `cluvfy.bat -help`.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for detailed information about CVU

## 1.7 Installing Oracle Database 11g Release 2 on Systems with Existing Databases

If you are planning an installation on a system where you have an existing Oracle RAC or Oracle Database installation, then you must perform additional tasks to prepare your system for installation.

If your system has an Oracle Database 10g installation, and you install Oracle Database 11g release 2 (11.2) either to coexist with or to upgrade the Oracle Database 10g release 2 (10.2) installation, then most installation types configure and start a default Oracle Net listener using TCP/IP port 1521 and the Inter-process communication (IPC) key value `EXTPROC`. One of the following actions occurs:

- During a coexisting installation, DBCA automatically migrates the listener and related files from the Oracle Database 10g Oracle home to the Oracle Database 11g Oracle home.
- During an upgrade, DBUA automatically locates the Oracle Database 10g listener, and migrates the listener to Oracle Database 11g.
	Note:
	For Oracle Database 11g release 2 (11.2) to coexist with Oracle Database 10g release 1 (10.2) databases using Oracle ASM, the 10.2 database must be release 10.2.0.2 or later.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/upgrade.htm#UPGRD003) for additional information about preparing for and performing upgrades