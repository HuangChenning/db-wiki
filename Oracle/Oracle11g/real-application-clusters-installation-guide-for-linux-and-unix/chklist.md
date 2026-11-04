---
title: Preinstallation Checklist
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/chklist.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 1 Preinstallation Checklist

Most Oracle Real Application Clusters (Oracle RAC) installation errors are due to a failure to complete all of the steps that are required before starting Oracle Universal Installer.

This chapter is intended for database administrators to use in consultation with system and storage administrators to coordinate the installation and plan the tasks for Oracle Clusterware, in preparation for completing an installation of Oracle RAC. This chapter contains the following topics:

## 1.1 Before You Start: Planning Your Installation

This section provides a list of tasks that Oracle recommends you complete before starting Oracle Clusterware and Oracle RAC installation. Whether your location is a Tier IV data center with a large project team of system administrators, storage administrators, network administrators, database administrators, and third-party hardware and software vendors, or you are a project team of one, planning is important to help ensure that your installation proceeds smoothly.

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

Before you decide whether you want to install Oracle Database 11g release 2 (11.2) on existing hardware, or decide what server and storage hardware to purchase for an installation, log on to My Oracle Support:

`https://support.oracle.com`

Click the Certify tab. Check the Certification Matrix for Oracle RAC for the operating system platform on which you intend to install, to ensure that your hardware configuration is supported for use with Oracle Clusterware and Oracle RAC. You can receive guidance about supported hardware options that can assist you with your purchasing decisions.

To access to the Certification Matrix:

1. Log on to My Oracle Support.
2. Click the Certifications tab.
3. Provide information about your platform to obtain certification information.

In addition to specific certified hardware configurations, the Certify page provides support and patch information, and general advice about how to proceed with an Oracle Clusterware or Oracle Clusterware with Oracle RAC 11g release 2 (11.2) installation, including important information about vendor clusterware and other configuration issues.

Contact your Oracle Sales Representative if you do not have a My Oracle Support account.

Also, you may want to refer to Oracle.com (`http://www.oracle.com`) for additional resources about planning for specific implementation scenarios, best practices, and other information that can help you with your installation plan. In particular, refer to the Oracle Real Application Clusters pages on the Oracle Technology Network:

`http://www.oracle.com/technology/products/database/clustering/index.html`

The Oracle RAC Technologies Certification Matrix provides details about supported technology that you can use to deploy Oracle RAC.

### 1.1.2 Consider Using Software Updates Option

OUI can install critical patch updates, system requirement updates for supported operating systems, and other significant updates that can ensure that your installation succeeds. Oracle recommends that you enable the Software Updates option during installation.

If you choose to enable the Software Updates option, then you must provide a valid My Oracle Support user name and password, so that OUI can download the latest updates, or you must provide a path to the location of a Software Updates option package that you have downloaded previously.

In addition, if you have a proxy realm, then be prepared to provide the destination proxy realm, and the user authentication (user name and password) required to authenticate access through that realm to the Internet, so that OUI can obtain software updates. Check with your network administrator before installation if you do not have this information.

If you plan to run the installation in a secured data center, then you can download updates before starting the installation by starting OUI on a system that has Internet access. To start OUI to download updates only, enter the following command:

```
$ ./runInstaller -downloadUpdates
```

Provide the My Oracle Support user name and password, and provide proxy settings if needed. After you download updates, transfer the update file to a directory on the server where you plan to run the installation.

### 1.1.3 Check Oracle Technology Network

The Oracle Technology Network (OTN) contains white papers about deployment options, capacity planning, best practices on various NFS platforms, and extended clusters deployments, which are not addressed in this guide. You can review available papers at the following Web site:

`http://www.oracle.com/technology/products/database/clustering/index.html`

### 1.1.4 Review Installation Steps for Oracle RAC

Installing Oracle RAC consists of the following steps:

1. Prepare servers (system, storage, and network administration):
	- Install the operating system and install the operating system packages and patches to the required version.
		- Create the required groups, users, and software homes.
		- Set up the domain name forwarding for Grid Naming Service (GNS) if you plan to deploy GNS, and set up the network addresses in the DNS and on the server as needed.
		- Set up the required storage.
		- (optional) Stage all of the software on one node for installation (the "local node").
	Note:
	During Oracle Grid Infrastructure installation, you can select multiple interconnects for private network use. This feature is called Redundant Interconnect Usage.
	This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).
	With Redundant Interconnect Usage, Oracle Clusterware can define multiple interfaces to use for the cluster interconnect network, without the need of using bonding or other technologies.
	When you define multiple interconnects, either during the installation interview or afterward using the Oracle Interface Configuration (OIFCFG) command line utility, Oracle Clusterware creates from one to four highly available IP (HAIP) addresses. Oracle RAC and Oracle ASM instances use these interconnect addresses to ensure highly available, load-balanced interconnect communication between nodes.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for more information about using OIFCFG to modify interconnects
2. Install Oracle Grid Infrastructure for a cluster, which includes Oracle Clusterware and Oracle Automatic Storage Management (system and storage administration):
	- Install Oracle Grid Infrastructure for a cluster. During installation, Fixup scripts perform additional configuration of operating system parameters, secure shell (SSH) for installation and user environment variables.
		- Patch Oracle Clusterware and Oracle Automatic Storage Management to the latest patchset.
3. Install Oracle RAC (database administration):
	- Install Oracle Real Application Clusters.
		- Patch Oracle RAC to the latest patchset.
		- Complete the postinstallation configuration of the Oracle RAC database.

### 1.1.5 Review How to Use Cluster Verification Utility (CVU)

Before installing Oracle Clusterware or Oracle RAC, use CVU to ensure that your cluster is prepared for an installation. CVU is incorporated into Oracle Universal Installer, so CVU runs when you start an Oracle RAC installation. However, you can use CVU to ensure that any packages or configuration information that is required for Oracle RAC are in place before you begin your Oracle RAC installation.

Oracle provides CVU to perform system checks in preparation for an installation, patch updates, or other system changes. In addition, CVU can generate fixup scripts, which are scripts run by the `root` user that can change many kernel parameters to at least the minimum settings required for a successful installation.

Using CVU can help system administrators, storage administrators, and database administrators to ensure that everyone has completed the system configuration and preinstallation steps, so that installations, updates, or patches complete successfully. You can obtain the latest version of CVU at the following URL:

`http://www.oracle.com/technology/products/database/clustering/cvu/cvu_download_homepage.html`

If you have a vendor who is performing hardware or operating system configuration steps, then ask the vendor to complete the relevant CVU check of the cluster after they complete their work to ensure that your system is configured correctly. Database administrators should refer to the section "Confirming Cluster Readiness for Oracle RAC Installation with CVU" to confirm that their system is prepared for installation before they start an Oracle RAC installation.

### 1.1.6 Review and Back Up Existing Oracle Installations

If you have an existing Oracle installation, then document version numbers, patches, and other configuration information, and review upgrade procedures for your existing installation. Review the Oracle upgrade documentation before proceeding with installation, to decide how you want to proceed.

Oracle RAC 11g release 2 (11.2), you must have Oracle Clusterware and Oracle ASM 11g release 2 (11.2) installed on your cluster. The Oracle Clusterware release version must be equal to or greater than the Oracle RAC version that you want to install.

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN)

For late-breaking updates and best practices about pre-upgrade, post-upgrade, compatibility, and interoperability discussions, refer to "Oracle Upgrade Companion." "Oracle Upgrade Companion" is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com/`

For upgrades, note the following:

- You can have only one version of Oracle Clusterware running on a cluster at a time. The Oracle Clusterware version must be the most recent release of any software (Oracle Clusterware, Oracle Database, Oracle RAC and Oracle Automatic Storage Management) running on the cluster.
- You can have multiple Oracle homes of Oracle Databases on your cluster. However, the Oracle RAC database software in these homes must be from a version that is equal to or prior to the version of Oracle Clusterware that is installed; you cannot have a version of Oracle Database running on Oracle Clusterware that was released after the version of Oracle Clusterware that you are running.
	For example:
	If you have Oracle Clusterware 11g release 2 installed as your clusterware, then you can have an Oracle Database 10g release 1 single-instance database running on one node, and separate Oracle RAC 10g release 1, release 2, and Oracle RAC 11g release 1 or release 2 databases also running on the cluster.
	However, you cannot have Oracle Clusterware 10g release 2 installed on your cluster, and install Oracle RAC 11g.
- Starting with release 10.1.0.6 and 10.2.0.3, you can use Database Upgrade Assistant (DBUA) for patch set upgrades with Oracle RAC. You can also use DBUA to upgrade between major point releases of Oracle RAC (for example, from 10.1 to 10.2, or 10.2 to 11g).
- You cannot change the owner of the Oracle Database home during an upgrade. You must use the same Oracle software owner that owns the existing Oracle Database home.
- As with any system change, back up your existing database before installing new software.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm)

### 1.1.7 Review Globalization Requirements

Before you start an installation on which you want to support languages other than English, review Oracle Database Globalization Support Guide.

Note the following:

- Oracle recommends that you use Unicode AL32UTF8 as the database character set.
	Unicode is the universal character set that supports most of the currently spoken languages. Unicode also supports many historical scripts (alphabets). Unicode is the native encoding of many technologies, including Java, XML, XHTML, ECMAScript, and LDAP. Unicode is ideally suited for databases that support the Internet and the global economy.
- The locale setting of your operating system session determines the language of the user interface and the globalization behavior for components such as Oracle Universal Installer, Oracle Net Configuration Assistant, and Database Configuration Assistant. The locale setting also determines the globalization behavior of Oracle Database sessions created by a user application through Oracle JDBC driver, unless overridden by the application.
- The `NLS_LANG` environment variable determines the language of the user interface and the globalization behavior for components such as SQL\*Plus, `exp`, and `imp`. This variable also sets the language and territory used by the client application and the database. The variable also declares the character set for entering and displaying data by the client application.

Note:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform contains a fuller discussion of database character sets used with different languages, and provides further information about installing and configuring Oracle Database globalization support.

### 1.1.8 Review Documentation

Before installing Oracle Clusterware, review the Oracle Grid Infrastructure Installation Guide for your operating system platform, particularly the Preinstallation, and the Storage chapters, to complete all of the required steps needed for an installation.

The Oracle Grid Infrastructure Installation Guide also contains most tasks requiring root privileges or storage administrator privileges that need to be completed before starting an Oracle RAC installation.

In addition, review the Release Notes and My Oracle Support (`https://support.oracle.com`) to ensure that you have the most current information about system requirements and other information that can affect your installation. The small time that this review takes can save a much greater amount of time required to track down causes of installation errors later. Also check to make sure that you have the most current version of this document; Oracle Documentation is updated after release.

Oracle recommends that you install a Web browser on your cluster nodes, both to enable Oracle Enterprise Manager and Oracle Application Express, if you install Oracle RAC, and to access online documentation as needed. Online documentation is available in PDF and HTML formats.

Note:

Refer to Oracle Database Concepts for an overview of Oracle Database, and Oracle Real Application Clusters Administration and Deployment Guide for additional information about Oracle Clusterware or Oracle RAC configuration and deployment. The [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform contains server and storage configuration information for Oracle RAC.

## 1.2 Overview of Server Hardware, Network and Operating System

Oracle Clusterware must be installed successfully before attempting to install Oracle RAC. To complete installations successfully, ensure that required hardware, network, and operating system preinstallation steps for Oracle software are complete. Failure to complete required preinstallation steps is the most common reason for failed installations.

Before Oracle Clusterware is installed as part of an Oracle Grid Infrastructure for a Cluster installation, you should already have completed installing and configuring CPUs, memory, shared storage, network cards, host bus adaptors, interconnects, and any other networking or server hardware. You should also have installed the operating system, and any vendor clusterware. Review your vendor documentation to complete these tasks, and if relevant, work with your vendor to complete the Oracle preinstallation steps that are listed in this document to confirm that the vendor hardware and software is correctly configured.

During Oracle Grid Infrastructure for a Cluster installation, the person completing the installation identifies the planned use for each global interface, identifying each interface as a Public interface type (used with public IP addresses and virtual IP addresses), a Private interface type (used with interconnects between cluster member nodes), or a Do not use interface type, which Oracle Clusterware and Oracle RAC should ignore. For example, an interface used as a dedicated interface for a network file system should be marked as a Do not use interface type.

Additional network configuration is not required during a Oracle RAC configuration.

Server and network preparation for installation include the following:

- Review Server Hardware and Software Requirements
- Overview of Server Environment Configuration
- Overview of Oracle Base
- Overview of Network Connection Requirements
- Overview of Secure Shell (SSH) Configuration
- Overview of Browser Requirement
- Overview of Platform-Specific Server Configuration

### 1.2.1 Review Server Hardware and Software Requirements

The following is a summary of server hardware and software configuration.

Oracle Requires

Each node in a cluster requires the following:

- Supported server hardware, including processors and system configuration.
	Review My Oracle Support before starting an installation on your current hardware, and before purchasing new hardware, to ensure that the hardware is supported with Oracle Clusterware with Oracle RAC 11g release 2 (11.2).
	Note:
	You must use the same operating system on each node in the cluster. In addition, Oracle strongly recommends that you use the same software configurations on each node of the cluster.
- Operating system packages listed in system requirements.
	Customized operating system package installations are not supported, because they may not include required packages. You can add additional packages as needed, but if you subtract packages from the default packages set, then you may encounter what are called failed dependencies errors for required software packages.
- A supported interconnect software protocol on each node, to support Oracle Clusterware voting disk polling, and to support Cache Fusion with Oracle RAC. Your interconnect must be certified by Oracle for your platform.

Oracle Recommends: System Administrator Tasks

Oracle recommends the following to simplify server installation and maintenance, and to prevent service issues

- Utilizing a time protocol that ensures all nodes in the cluster use the same reference time. With Oracle Clusterware 11g release 2 (11.2), if the network time protocol is not enabled at installation, then the Oracle Clusterware installation enables the cluster time synchronization service.
- Configuring redundant switches, for all cluster sizes.
- Using identical server hardware on each node, to simplify server maintenance.

Additional Options: System Administrators and Vendors

- Though you do not need to use vendor clusterware with Oracle Clusterware, Oracle supports the use of many vendor clusterware options. However, you must install Oracle Clusterware to use Oracle RAC. Be aware that when you use vendor clusterware, Oracle Clusterware defers to the vendor clusterware for some tasks, such as node membership decisions.
- You may require third-party vendor clusterware if you use a non-ethernet interconnect.

After you have set up server hardware, review "Checking Hardware Requirements" in the preinstallation chapter to ensure that your system has enough RAM, that the `TMP` and `TEMP_DIR` locations have enough available space for the installation, and that your system meets other hardware requirements.

### 1.2.2 Overview of Server Environment Configuration

Configure the Oracle software groups and users, and configure user environments, as described in the The Oracle Grid Infrastructure Installation Guide for your platform preinstallation chapters. These include the following:

- Creating and configuring the Oracle RAC installation owner (typically `oracle`); this is the user account that you should use for installation.
- Creating an OSDBA operating system group whose members are granted the SYSDBA privilege through operating system authentication (typically `dba`).
- Creating binary and storage installation paths.

See Also:

[The Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform

### 1.2.3 Overview of Oracle Base

The Oracle base location is the location where Oracle Database binaries are stored. During installation, you are prompted for the Oracle base path. Typically, an Oracle base path for the database is created during an Oracle Grid Infrastructure installation.

Every Oracle home can have its own Oracle base. Typically, the Oracle base path is based on the installation owner name. If you have separate installation owners for the Oracle Grid Infrastructure installation and the Oracle RAC installation, then you have two Oracle base paths that are in accordance with Optimal Flexible Architecture (OFA) guidelines. For example, if the user `grid` is the installation owner of the Oracle Grid infrastructure installation, and the user `oracle` is the installation owner of the Oracle Database installation, then you have two Oracle base directories:

- `/u01/app/grid` --the Oracle base for the user `grid`, which owns the Oracle Grid Infrastructure binaries
- `/u01/app/oracle` --the Oracle base for the user `oracle`, which owns the Oracle Database binaries

In preparation for installation, Oracle recommends that you only set the `ORACLE_BASE` environment variable to define paths for Oracle binaries and configuration files. Oracle Universal Installer (OUI) creates other paths and environment variables as necessary, in accordance with the Optimal Flexible Architecture (OFA) rules for well-structured Oracle software environments.

For example, with Oracle Database 11g, Oracle recommends that you do not set an Oracle home environment variable, and instead enable OUI to create it. If the Oracle base path is `/u01/app/oracle`, then by default, OUI creates the following Oracle home path:

```
/u01/app/oracle/product/11.2.0/dbhome_1
```

Ensure that the paths that you select for Oracle software, such as Oracle home paths and the Oracle base path, use only ASCII characters. Because installation owner names are used by default for some path, this ASCII character restriction applies to user names, file names, and directory names.

Note:

If you are upgrading from an existing Oracle RAC installation, then you must use the same type of Oracle home that you have in your existing installation. For example, if you have a shared Oracle home in your existing installation, then you must upgrade to a shared Oracle home with Oracle RAC 11g release 2 (11.2). Similarly, if you have local Oracle homes on cluster nodes, then you must upgrade to local Oracle homes on cluster nodes.

### 1.2.4 Overview of Network Connection Requirements

The following is an overview of network configuration requirements for Grid Naming Service (GNS) in a Grid Plug and Play configuration, and in a manual network configuration. Network administrators and system administrators can refer to the Preinstallation chapter in the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform for detailed configuration information.

The network configuration for Oracle Clusterware and Oracle RAC requires several addresses. The following is a list of those addresses:

- GNS virtual IP address (GNS installations only): A static IP address configured in the GNS. The GNS virtual IP listener forwards queries to nodes in the subdomain on the cluster managed by GNS.
	Within the subdomain, the GNS uses multicast Domain Name Service (mDNS) to enable the cluster to map hostnames and IP addresses dynamically as nodes are added and removed from the cluster, without requiring additional host configuration in the DNS.
	To enable GNS, you must have your network administrator provide a set of IP addresses for a subdomain that is assigned to the cluster (for example, `grid.example.com`), and forward DNS requests for that subdomain to the GNS virtual IP address for the cluster, which GNS will serve.
- Single Client Access Name (SCAN): A domain name that resolves to all the addresses allocated for the SCAN. Oracle recommends that you allocate three addresses to the SCAN. During Oracle Grid Infrastructure installation, listeners are created for each of the SCAN addresses, and Oracle Clusterware controls which server responds to a SCAN address request.
	For high availability, you should provide at least three IP addresses in the DNS to use for SCAN mapping. A SCAN domain name must be unique within your corporate network.
- Virtual IP address: A public internet protocol (IP) address for each node, to be used as the Virtual IP address (VIP) for client connections. If a node fails, then Oracle Clusterware fails over the VIP address to an available node.
	During installation, if you do not use Grid Naming Service (which provides the VIP automatically), then you provide VIP addresses. The VIP for each node is associated with the same interface name on every node that is part of your cluster. If you have a domain name server (DNS), then your network administrator should register the host names for the VIP with the DNS, so that the DNS is resolvable from any client, as well as the cluster nodes. The VIP should not be in use at the time of the installation, because this is an IP address that Oracle Clusterware manages.
- Public IP address: A public host name address for each node, assigned by GNS, or assigned by the system administrator during initial system configuration for manual configurations. The public IP address name must be resolvable to the hostname. Register both the public IP and the VIP address with the DNS. If you do not have a DNS, then you must make sure that both public IP addresses are in the node `/etc/hosts` file (for all cluster nodes).
- Private IP address: A private IP address for each node to serve as the private interconnect address, dedicated exclusively to internode cluster communication. GNS configures the address automatically. If you select manual configuration, then you must ensure that the following is true for each private IP address. The private IP address must be:
	- Separate from the public network
		- Accessible on the same network interface on each node
		- Connected to a network switch between the nodes for the private network; crosscable interconnects are not supported
	The private interconnect is used for internode communication by both Oracle Clusterware and Oracle RAC. If you use manual configuration, then the private IP address must be available in each node's `/etc/hosts` file. Oracle recommends that the private network interconnects ar configured on dedicated switches that are not connected to anything other than the nodes in the same cluster.
	Note:
	All host names must conform to the RFC 952 standard, which permits alphanumeric characters. Host names using underscores ("\_") are not enabled.

Table 1-1 and the content following provides an overview of IP address requirements for manual network connections.

If you choose not to use GNS, then before installation your network administrator must configure SCAN, public, virtual, and private IP addresses. Your network administrator also must reconfigure the network when nodes are added or removed from the cluster.

For example, with a two node cluster where each node has one public and one private interface, and you have defined a SCAN domain address to resolve on your DNS to one of three IP addresses, you might have the configuration shown in the following table for your network interfaces:

Table 1-1 Manual Network Configuration Example

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

<sup>Footnote 1</sup> Node hostnames may resolve to multiple addresses.

### 1.2.5 Overview of Secure Shell (SSH) Configuration

Secure Shell (SSH) configuration is required for Oracle Clusterware and Oracle RAC.

System administrators can follow the procedure described in "Configuring SSH on All Cluster Nodes" in the Preinstallation chapter of Oracle Grid Infrastructure Installation Guide for your operating system, to configure SSH access for each node on the cluster to all other nodes of the cluster.

Oracle recommends that you ask your system administrator to permit SSH connections on all cluster member nodes for the user account that will own the Oracle RAC installation. When this is enabled, you can use a script within the Oracle Universal Installer to set up SSH configuration for installation. If this script is not able to run because of environment restrictions for the user account you use for installation, then you or your system administrator will need to set up SSH manually for installation.

In addition, note that any messages displayed to the terminal, such as a "message of the day," can disable SSH configuration. Ask your system administrator to review the SSH section in the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform.

### 1.2.6 Overview of Browser Requirement

You need a web browser to access documentation, and to use Oracle Enterprise Manager and Oracle Application Express. Web browsers must support JavaScript and the HTML 4.0 and CSS 1.0 standard.

Oracle Enterprise Manager supports the following browsers:

- Microsoft Internet Explorer 10 (supports Oracle Enterprise Manager Database Control 11.2.0.3 or higher)
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

For a list of browsers supported with Oracle Application Express, see [Oracle Application Express Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e12196/pre_require.htm#HTMIG380).

Note:

You do not require a browser to install Oracle RAC.

### 1.2.7 Overview of Platform-Specific Server Configuration

Oracle Clusterware and Oracle RAC are tested with specific operating system kernels, and specific operating system components. Oracle requires that you use the operating system kernel and components that are certified for this release.

Oracle recommends that you or your system administrator review the system requirements carefully in Oracle Grid Infrastructure Installation Guide before beginning installation, to ensure that your system meets these requirements. If your system does not meet minimum operating system kernel and component requirements, then your installation may fail to complete, or other errors may develop during Oracle Clusterware or Oracle Database runtime.

In addition to the standard system requirements configuration, deployment on specific server hardware can include additional operating system configuration steps. Review the Preinstallation chapter, and check the My Oracle Support Certify page to ensure that you are aware of any additional requirements or recommendations for your specific hardware platform configuration.

## 1.3 Overview of Oracle RAC Storage

To install Oracle RAC, you need to have configured shared storage for the database files. Review the following sections for storage planning:

- Where to Review Storage System Requirements
- Overview of Oracle Automatic Storage Management Cluster File System
- Overview of Oracle Database and Recovery File Options
- General Storage Considerations for Oracle RAC
- Using Logical Volume Managers with Oracle Grid Infrastructure and Oracle RAC

### 1.3.1 Where to Review Storage System Requirements

Refer to the "Configuring Storage for Grid Infrastructure for a Cluster and Oracle Real Application Clusters (Oracle RAC)" chapter in Oracle Grid Infrastructure Installation Guide for your operating system to review storage options for installation planning. Storage and system administrators can refer to this chapter to configure storage for Oracle Database files on Oracle RAC. Note that when Database Configuration Assistant (DBCA) configures automatic disk backup, DBCA uses a database recovery area that must be shared.

### 1.3.2 Overview of Oracle Automatic Storage Management Cluster File System

With Oracle Database and Oracle Grid Infrastructure release 11.2 and later, Oracle Automatic Storage Management (Oracle ASM) has been extended to include a general purpose file system (Oracle Automatic Storage Management File System, or ACFS), which can be used for any files that you cannot place directly on Oracle ASM, such as database homes, or application files. At the time of this release, this feature is available on Linux, but not available on UNIX platforms.

See Also:

The Certify page on My Oracle Support for the most current information about storage options:
```
https://support.oracle.com
```

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for an overview of storage configuration administration

### 1.3.3 Overview of Oracle Database and Recovery File Options

There are two ways of storing Oracle Database and recovery files:

Note:

Installing files on raw or block devices is not supported. Install files on a shared file system or on Oracle ASM. Upgrading existing raw or block devices is supported.
- Oracle Automatic Storage Management: Oracle Automatic Storage Management (Oracle ASM) is an integrated, high-performance database file system and disk manager for Oracle Database files. It performs striping and mirroring of database files automatically.
	Note:
	For Standard Edition Oracle Database installations using Oracle RAC, Oracle ASM is the only supported storage option.
- A supported shared file system: Supported file systems include the following:
	- A supported cluster file system: Note that if you intend to use a cluster file system for your data files, then you should create partitions large enough for the database files when you create partitions for Oracle Clusterware.
		See Also:
		The Certify page on My Oracle Support for supported cluster file systems
		- NAS Network File System (NFS) listed on Oracle Certify: Note that if you intend to use NFS for your data files, then you should create partitions large enough for the database files when you create partitions for Oracle Clusterware.
	See Also:
	The Certify page on My Oracle Support for supported Network Attached Storage (NAS) devices, and supported cluster file systems
	Note:
	Oracle RAC software can be installed on OCFS2. However, it cannot be installed on Oracle Cluster File System (OCFS). Oracle RAC and Oracle Grid Infrastructure software can be installed on network-attached storage (NAS).
	For OCFS2 certification status, refer to the Certify page on My Oracle Support.

### 1.3.4 General Storage Considerations for Oracle RAC

For all installations, you must choose the storage option that you want to use for Oracle Database files, or for Oracle Clusterware with Oracle RAC (Oracle RAC). If you want to enable automated backups during the installation, then you must also choose the storage option that you want to use for recovery files (the Fast Recovery Area). You do not have to use the same storage option for each file type.

Table 1-2 shows the storage options supported for storing Oracle Database files and Oracle Database recovery files. Oracle Database files include data files, control files, redo log files, the server parameter file, and the password file.

Note:

For up-to-date information about supported storage options for Oracle RAC installations, refer to the Certify pages on the My Oracle Support Web site:
```
https://support.oracle.com
```

Table 1-2 Supported Storage Options for Oracle Database and Recovery Files

<table><thead><tr><th rowspan="2">Storage Option</th><th>File Types Supported</th><th></th></tr><tr><th headers="r1c1-t21 r1c1-t21">Database</th><th headers="r1c1-t21 r2c1-t21 r1c2-t21">Recovery</th></tr></thead><tbody><tr><td headers="r1c1-t21 r2c1-t21"><p>Oracle Automatic Storage Management</p></td><td headers="r3c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p></td><td headers="r3c1-t21 r1c3-t21"><p>Yes</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>OCFS2</p></td><td headers="r4c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p></td><td headers="r4c1-t21 r1c3-t21"><p>Yes</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Local storage</p></td><td headers="r5c1-t21 r1c2-t21 r2c2-t21"><p>No</p></td><td headers="r5c1-t21 r1c3-t21"><p>No</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>NFS file system</p><p>Note: Requires a certified NAS device</p></td><td headers="r6c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p></td><td headers="r6c1-t21 r1c3-t21"><p>Yes</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Shared raw devices being used with existing installation</p></td><td headers="r7c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p><p>for upgrades only, or as a manual configuration</p></td><td headers="r7c1-t21 r1c3-t21"><p>No</p></td></tr><tr><td headers="r1c1-t21 r2c1-t21"><p>Shared block devices being used with existing installations</p></td><td headers="r8c1-t21 r1c2-t21 r2c2-t21"><p>Yes</p><p>for upgrades only, or as a manual configuration</p></td><td headers="r8c1-t21 r1c3-t21"><p>No</p></td></tr></tbody></table>

Use the following guidelines when choosing the storage options that you want to use for each file type:

- You can choose any combination of the supported storage options for each file type if you satisfy all requirements listed for the chosen storage options.
- Oracle recommends that you choose Oracle Automatic Storage Management (Oracle ASM) as the storage option for database and recovery files.
- For Standard Edition Oracle RAC installations, Oracle ASM is the only supported storage option for database or recovery files.
- If you intend to upgrade an existing Oracle RAC database, or an Oracle RAC database with Oracle ASM instances, then you must ensure that your system meets the following conditions:
	- Oracle Universal Installer (OUI) and Database Configuration Assistant (DBCA) are run on the node where the Oracle RAC database or Oracle RAC database with Oracle ASM instance is located.
		- The Oracle RAC database or Oracle RAC database with an Oracle ASM instance is running on the same nodes that you intend to make members of the new cluster installation. For example, if you have an existing Oracle RAC database running on a three-node cluster, then you must install the upgrade on all three nodes. You cannot upgrade only two nodes of the cluster, removing the third node in the upgrade.
	See Also:
	[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about how to prepare for upgrading an existing database
- If you do not have a storage option that provides external file redundancy, then you must configure at least three voting disk areas to provide voting disk redundancy.

### 1.3.5 Using Logical Volume Managers with Oracle Grid Infrastructure and Oracle RAC

Oracle Grid Infrastructure and Oracle RAC only support cluster-aware volume managers. To confirm that a volume manager you want to use is supported, look under the Certifications tab on My Oracle Support, which is available at the following URL:

```
https://support.oracle.com
```

## 1.4 Additional Information to Prepare for Installation

This section contains additional information about Oracle Clusterware, Oracle Automatic Storage Management (Oracle ASM), and Oracle RAC, that may be helpful for your installation plan team to read to decide how you want to configure your installation. It contains the following topics:

- Oracle ASM is Installed with Oracle Grid Infrastructure
- Obtain the Oracle ASM ASMSNMP Password for Oracle Enterprise Manager
- Oracle Clusterware and Vendor Clusterware
- Shared Components of Oracle RAC Installations
- Simplified Upgrade of TIMESTAMP WITH TIME ZONE Data
- Ensure an External Jobs User Is Created for HP-UX
- Oracle Database 11g Real Application Clusters Release Compatibility

### 1.4.1 Oracle ASM is Installed with Oracle Grid Infrastructure

In past releases, Oracle ASM was installed as part of the Oracle Database installation. With Oracle Database 11g release 2 (11.2), Oracle ASM is part of an Oracle Grid Infrastructure installation. If you want to upgrade an existing Oracle ASM installation, then you must upgrade Oracle ASM by running an Oracle Grid Infrastructure upgrade.

If you did not select Oracle ASM as the storage option for the Oracle Clusterware files, then you must first use Oracle ASM Configuration Assistant (ASMCA) to configure Oracle ASM, create an Oracle ASM instance, and create a disk group to use for your Oracle Database storage.

### 1.4.2 Obtain the Oracle ASM ASMSNMP Password for Oracle Enterprise Manager

Obtain the ASMSNMP from the Oracle Grid Infrastructure administrator.

During Oracle Grid Infrastructure for a cluster installation, the ASMSNMP account is created and its status is set to OPEN. It is granted the SYSDBA for ASM privilege. Oracle Enterprise Manager requires access to the ASMSNMP account to monitor Oracle ASM instances and retrieve data from ASM-related data dictionary views.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG94093) for additional information about the ASMSNMP account

### 1.4.3 Oracle Clusterware and Vendor Clusterware

Oracle Clusterware provides clustering services. You do not require vendor clusterware when you use Oracle Clusterware. If you intend to install Oracle RAC, then you must install Oracle Clusterware.

### 1.4.5 Simplified Upgrade of TIMESTAMP WITH TIME ZONE Data

As part of an installation of Oracle Database 11g release 2 (11.2), time zone version files from 1 to 11 are installed in the path `$ORACLE_HOME/oracore/zoneinfo/`. You can continue to use the current time zone version or upgrade to the latest version. Oracle recommends that you upgrade the server to the latest time zone version. Upgrading to a new time zone version may cause existing TIMESTAMP WITH TIME ZONE (TSTZ) data to become stale. Using the newly provided DBMS\_DST PL/SQL packages, you can update the TSTZ data transparently with minimal manual procedures and system downtime.

All instances of an Oracle RAC database must use the same time zone. The Oracle RAC database time zone defaults to the time zone setting of the Oracle Grid Infrastructure Grid user, except when an instance is started with SQL\*Plus. When you use SQL\*Plus, you must be sure to use the same time zone setting for the database instance that is used for Oracle Clusterware. You can change the time zone Oracle Clusterware uses for a database by using the following command, where `time zone` is the time zone to which you want to change:

```
srvctl setenv database -T 'TZ=time zone
```

Time zone version files are also installed on the clients. Starting with Oracle Database 11g release 2, you no longer need to upgrade Client time zone files immediately. Upgrades can be done at a time when it is most convenient to the system administrator. However, there could be a small performance penalty when client and server use different time zone versions.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for information about preparing to upgrade Timestamp with Time Zone data, [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for information about how to upgrade the Time Zone file and Timestamp with Time Zone data, and [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for information about performance effects of clients and servers operating with different versions of Time Zone files

### 1.4.6 Ensure an External Jobs User Is Created for HP-UX

If you are installing Oracle Real Application Clusters on HP-UX, then ensure that there is a low-privileged user created to own external jobs, and be aware that you must set this user as the external jobs user by logging in as the root user and modifying `$ORACLE_HOME/rdbms/admin/externaljob.ora` after installation. Only the root user can modify this file.

### 1.4.7 Oracle Database 11g Real Application Clusters Release Compatibility

You can install and operate different releases of Oracle Database software on the same computer:

- When you have Oracle Clusterware installed with different release versions of Oracle software, the Oracle Clusterware version must be greater than or equal to the Oracle Database software version. Oracle Clusterware and Oracle Automatic Storage Management are both upgraded with an Oracle Grid Infrastructure 11g release 2 (11.2) installation.
- If you have an existing Oracle home, then you can create a new Oracle home and install Oracle Database 11g release 2 (11.2) into the new Oracle home. You should ensure that Oracle Clusterware is in a separate Oracle Grid Infrastructure home. Oracle Grid Infrastructure for a Cluster installations cannot be installed in the Oracle base directory for Oracle Database.
- If you are running the Oracle9i release of Oracle RAC, and you want to continue to use that release, then you must run cluster software that is compatible with that release, such as Oracle Cluster Manager or a third party cluster software. Oracle Clusterware release 11g can be installed on the same system as Oracle9i database software, but Oracle9i software cannot be supported by Oracle Clusterware 11g.
	Note:
	If you want to remove third party cluster software after upgrading your database to Oracle Database 10g or Oracle Database 11g, then you must first remove the third party cluster software, and then re-install Oracle Clusterware.
- If OUI detects a previous database release, then OUI asks you about your upgrade preferences. You have the option to upgrade one of the previous release databases with DBUA or to create a new database using DBCA. The information collected during this dialog is passed to DBUA or DBCA after the software is installed.
	If OUI detects a previous Oracle Clusterware release, then you are asked to upgrade the existing Oracle Clusterware installation. Only one Oracle Clusterware version can exist on a server, and servers must be members of one cluster only.
	You cannot install Oracle Grid Infrastructure for a standalone server and then install Oracle Grid Infrastructure for a cluster. If you have Oracle Grid Infrastructure for a standalone server installed, then you must remove that installation before you can install Oracle Grid Infrastructure for a cluster.
	Note:
	Do not move Oracle binaries from the Oracle home to another location. Doing so can cause dynamic link failures.

## 1.5 Confirming Cluster Readiness for Oracle RAC Installation with CVU

Before you start your installation, use CVU to ensure that your system is prepared for Oracle RAC installation. If any checks fail, then fix the errors reported, either manually or by using a generated fixup script, or contact your system or storage administrator to have the cause of the errors addressed.

CVU is available in the Grid home, in the `bin` directory. For example, if the Oracle Grid Infrastructure for a cluster home is `/u01/crs`, then the path is `/u01/crs/bin`. To start CVU, navigate to the Grid home `bin` directory, and use a command similar to the following:

cluvfy stage -pre dbinst -fixup -n nodelist -r release -osdba OSDBA -verbose

In the preceding command, `-fixup` and `-osdba` are optional flags.

For example, for a two node cluster with nodeA and nodeB, where you are testing the cluster to prepare to install Oracle Database 11g with Oracle RAC, and your OSDBA group is `dba`, the following command checks for system readiness:

```
$ ./cluvfy stage -pre dbinst -fixup -n nodea,nodeb -osdba dba -verbose
```

For more information about CVU commands, enter `./cluvfy -help`.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for detailed information about CVU

## 1.6 Stopping Existing Oracle Processes for Upgrades or Coexisting Databases

If you are planning an installation on a system where you have an existing Oracle RAC or Oracle Database installation, then you must perform additional tasks to prepare your system for installation.

Table 1-3 provides an overview of what you need to do if you have an existing Oracle Database installation. Review the table, and perform tasks as required.

See Also:

[Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) for additional information about preparing for and performing upgrades

Table 1-3 Overview of System Preparation for Upgrades or Co-existing Databases

| Installation Scenario | What you need to do |
| --- | --- |
| Upgrading from Oracle Database 10g release 1 (10.1) to 11g release 2 (11.2) | No additional tasks. Refer to Installing Oracle Database 11g on a System with Oracle Database 10g |
| Installing Oracle Database 11g release 2 (11.2) on a system to coexist with Oracle Database 10g release 1 (10.1) | No additional tasks. Refer to Installing Oracle Database 11g on a System with Oracle Database 10g |
| Upgrading from Oracle9i release 9.2 to Oracle Database 11g release 2 (11.2) | Shut down the Global Service Daemon, and shut down a default listener on port 1521, if present. Refer to Installing Oracle 11g Database on a System with Oracle9i Database Release 2 |
| Installing Oracle Database 11g release 2 (11.2) on a system to co-exist with Oracle9i release 9.2 | Shut down a default listener on port 1521, if present, and shut down the Global Service Daemon. Refer to Installing Oracle 11g Database on a System with Oracle9i Database Release 2 |

Installing Oracle Database 11g on a System with Oracle Database 10g

If your system has an Oracle Database 10g installation, and you install Oracle Database 11g release 2 (11.2) either to coexist with or to upgrade the Oracle Database 10g installation, then most installation types configure and start a default Oracle Net listener using TCP/IP port 1521 and the IPC key value `EXTPROC`. One of the following occurs:

- During a co-existing installation, Database Configuration Assistant (DBCA) automatically migrates the listener and related files from the Oracle Database 10g Oracle home to the Oracle Database 11g Oracle home.
- During an upgrade, Oracle Database Upgrade Assistant (DBUA) automatically locates the Oracle Database10g listener, and migrates the listener to Oracle Database 11g.
	Note:
	For Oracle Database 11g release 2 (11.2) to coexist with Oracle Database 10g release 1 (10.1) databases using Oracle ASM, the 10.1 database must be release 10.1.0.3 or later.

Installing Oracle 11g Database on a System with Oracle9i Database Release 2

Explanation of Tasks If you are installing an Oracle Database 11g release 2 (11.2) on a system with an existing Oracle9i Database release 2 (9.2), and the Oracle Net listener process is using the same port or key value as the default used with the Oracle Database 11g release 2 (11.2) installation, port 1521, then OUI can only configure the new listener; it cannot start it. To ensure that the new listener process starts during the installation, you must shut down any existing listeners before starting OUI. To do this, refer to "Shutting Down the Listener"

You must shut down the Global Services Daemon (GSD), because otherwise, during Oracle Database 11g installation, the Oracle Database 9i release 9.2 SRVM shared data is upgraded into an Oracle Cluster Registry that the 9.2 GSD will not be able to use. The Oracle Grid Infrastructure installation starts an 11g release 2 (11.2) GSD to serve the Oracle9i 9.2 clients. To do this, refer to "Shutting down the Global Services Daemon"

Shutting Down the Listener To determine if an existing Oracle Database 9i listener process is running and to shut it down if necessary, follow these steps:

1. Switch user to the software owner user. For example:
	```
	# su - oracle
	```
2. Enter the following command to determine if an Oracle Database 9i listener process is running and to identify its name and the Oracle home directory in which it is installed:
	```
	$ ps -ef | grep tnslsnr
	```
	This command displays information about the Oracle Net listeners running on the system:
	```
	... oracle_home1/bin/tnslsnr LISTENER -inherit
	```
	In this example, `oracle_home1` is the Oracle home directory where the listener is installed and `LISTENER` is the listener name.
3. Set the ORACLE\_HOME environment variable to specify the appropriate Oracle home directory for the listener:
	- Bourne, Bash, or Korn shell:
		```
		$ ORACLE_HOME=oracle_home1
		$ export ORACLE_HOME
		```
		- C or tcsh shell:
		```
		% setenv ORACLE_HOME oracle_home1
		```
4. Enter the following command to identify the TCP/IP port number and IPC key value that the listener is using:
	```
	$ $ORACLE_HOME/bin/lsnrctl status listenername
	```
	Note:
	If the listener uses the default name LISTENER, then you do not have to specify the listener name in this command.
5. Enter a command similar to the following to stop the listener process:
	```
	$ $ORACLE_HOME/bin/lsnrctl stop listenername
	```
6. Repeat this procedure to stop all listeners running on this system and on all other nodes in the cluster.

Shutting down the Global Services Daemon As the database installation software owner (for example, `oracle`), on each node of the cluster, use the following syntax to shut down the GSD:

```
$ cd 92_Oracle_home
$ bin/gsdctl stop
```

In the preceding syntax example, the variable `92_Oracle_home` is the Oracle Database 9i release 2 (9.2) home.