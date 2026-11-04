---
title: "What's New in Oracle Grid Infrastructure Installation and Configuration?"
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/whatsnew.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

This section describes new features as they pertain to the installation and configuration of Oracle Grid Infrastructure (Oracle Clusterware and Oracle Automatic Storage Management), and Oracle Real Application Clusters (Oracle RAC). This guide replaces Oracle Clusterware Installation Guide. The topics in this section are:

## New Features for Release 2 (11.2.0.4)

The following is a list of new features for Release 2 (11.2.0.4):

### Cluster and Oracle RAC Diagnosability Tools Enhancements

Starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4), the Trace File Analyzer and Collector is installed automatically with Oracle Grid Infrastructure installation. The Trace File Analyzer and Collector is a diagnostic collection utility to simplify diagnostic data collection on Oracle Clusterware, Oracle Grid Infrastructure, and Oracle RAC systems.

Note:

The Trace File Analyzer and Collector is available starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4).

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/troubleshoot.htm#CWADD92407) for information about using Trace File Analyzer and Collector

### Oracle Database Health Checks and Best Practice Recommendation

Oracle RAC Configuration Audit tool (RACcheck) is available with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4) for assessment of single instance and Oracle RAC database installations for known configuration issues, best practices, regular health checks, and pre- and post upgrade best practices.

Note:

The Oracle RAC Configuration Audit tool is available starting with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4).

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm#RACAD8365)

## Desupported Options for Release 2 (11.2.0.4)

The following features are no longer supported with Oracle Grid Infrastructure 11g Release 2 (11.2.0.4):

### Block and Raw Devices Not Supported with OUI

With this release, OUI no longer supports installation of Oracle Clusterware files on block or raw devices. Install Oracle Clusterware files either on Oracle Automatic Storage Management disk groups, or in a supported shared file system.

### Deprecation of -cleanupOBase

The `-cleanupOBase` flag of the deinstallation tool is deprecated in this release. There is no replacement for this flag.

## New Features for Release 2 (11.2.0.3)

The following is a list of new features for Release 2 (11.2.0.3):

### Oracle ACFS and ADVM Support for Oracle Linux (UEK)

Oracle ASM 11g release 2 (11.2.0.3) for Linux on x86-64 bit systems provides support for Oracle Automatic Storage Management Cluster File System (ACFS) and Oracle ASM Dynamic Volume Manager (ADVM) on Oracle Linux kernels UEK5-2.6.32-100.34.1 and subsequent updates to 2.6.32-100 kernels for supported Oracle Linux kernels.

### Oracle ACFS and ADVM Support for SUSE Enterprise Linux 11

Oracle ASM 11g release 2 (11.2.0.3) for Linux on x86-64 bit systems provides support for Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (ADVM) on SUSE Enterprise Linux 11 Service Pack 1 (SLES11 SP1), 64 bit only.

### Oracle Clusterware Upgrade Configuration Force Feature

If nodes become unreachable in the middle of an upgrade, starting with release 11.2.0.3, you can run the `rootupgrade.sh` script with the `-force` flag to force an upgrade to complete.

## New Features for Release 2 (11.2.0.2)

The following is a list of new features for Release 2 (11.2.0.2):

### Configuration Wizard for the Oracle Grid Infrastructure Software

The Oracle Grid Infrastructure Configuration Wizard enables you to configure the Oracle Grid Infrastructure software after performing a software-only installation. You no longer have to manually edit the `config_params` configuration file as this wizard takes you through the process, step by step.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD92094) for more information about the configuration wizard.

### Enhanced Patch Set Installation

Starting with the release of the 11.2.0.2 patch set for Oracle Grid Infrastructure 11g Release 2 (Oracle Clusterware and Oracle Automatic Storage Management), Oracle Grid Infrastructure patch sets are full installations of the Oracle Grid Infrastructure software. Note the following changes with the new patch set packaging:

- Direct upgrades from previous releases (11.x, 10.x) to the most recent patch set are supported.
- Out-of-place patch set upgrades only are supported. An out-of-place upgrade is one in which you install the patch set into a new, separate home.
- New installations consist of installing the most recent patch set, rather than installing a base release and then upgrading to a patch release.

See Also:

My Oracle Support note 1189783.1, "Important Changes to Oracle Database Patch Sets Starting With 11.2.0.2", available from the following URL:

`https://support.oracle.com`

### Oracle ACFS and ADVM Support for SUSE Enterprise Linux

Oracle ASM 11g release 2 (11.2.0.2) and later for Linux on x86-64 bit systems provides support for Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (ADVM) on SUSE Enterprise Linux 10 Service Pack 3 (SLES10 SP3) and later SLES10 service packs (64 bit only).

### Cluster Health Monitor Included with Oracle Clusterware

Cluster Health Monitor gathers operating system metrics in real time, and stores them in its repository for later analysis, so that it can determine the root cause of many Oracle Clusterware and Oracle RAC issues with the assistance of Oracle Support.

Cluster Health Monitor also works in conjunction with Oracle Database Quality of Service Management (QoS) by providing metrics to detect memory over-commitment on a node. QoS Management can shut down services on overloaded nodes to relieve stress and preserve existing workloads.

To support QoS Management, Oracle Database Resource Manager and metrics have been enhanced to support fine-grained performance metrics, and also can manage workloads with user-defined performance classes.

Note:

Cluster Health Monitor is not available with IBM: Linux on System z.

### Grid Installation Owner and ASMOPER

During installation, in the Privileged Operating System Groups window, it is now optional to designate a group as the OSOPER for ASM group. If you choose to create an OSOPER for ASM group, then you can enter a group name configured on all cluster member nodes for the OSOPER for ASM group. In addition, the Oracle Grid Infrastructure installation owner no longer is required to be a member.

### New Software Updates Option

Use the Software Updates feature to dynamically download and apply software updates as part of the Oracle Database installation. You can also download the updates separately using the `downloadUpdates` option and later apply them during the installation by providing the location where the updates are present.

### Redundant Interconnect Usage

In previous releases, to make use of redundant networks for the interconnect, bonding, trunking, teaming, or similar technology was required. Oracle Grid Infrastructure and Oracle RAC can now make use of redundant network interconnects, without the use of other network technology, to enhance optimal communication in the cluster. This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).

Redundant Interconnect Usage enables load-balancing and high availability across multiple (up to four) private networks (also known as interconnects).

### Oracle Database Quality of Service Management

The Database Quality of Service (QoS) Management Server allows system administrators to manage application service levels hosted in Oracle Database clusters by correlating accurate run-time performance and resource metrics and analyzing with an expert system to produce recommended resource adjustments to meet policy-based performance objectives.

Oracle Database Quality of Service Management is not available for Linux on System z.

See Also:

[Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/toc.htm)

## New Features for Release 2 (11.2)

The following is a list of new features for installation of Oracle Clusterware and Oracle ASM 11g release 2 (11.2):

### Oracle Automatic Storage Management and Oracle Clusterware Installation

With Oracle Grid Infrastructure 11g release 2 (11.2), Oracle Automatic Storage Management (Oracle ASM) and Oracle Clusterware are installed into a single home directory, which is referred to as the Grid Infrastructure home. Configuration assistants start after the installer interview process that configures Oracle ASM and Oracle Clusterware.

The installation of the combined products is called Oracle Grid Infrastructure. However, Oracle Clusterware and Oracle Automatic Storage Management remain separate products.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for Linux for information about how to install Oracle Grid Infrastructure (Oracle ASM and Oracle Clusterware binaries) for a standalone server. This feature helps to ensure high availability for single-instance servers

### Oracle Automatic Storage Management and Oracle Clusterware Files

With this release, Oracle Cluster Registry (OCR) and voting disks can be placed on Oracle Automatic Storage Management (Oracle ASM).

This feature enables Oracle ASM to provide a unified storage solution, storing all the data for the clusterware and the database, without the need for third-party volume managers or cluster filesystems.

For new installations, OCR and voting disk files can be placed either on Oracle ASM, or on a cluster file system or NFS system. Installing Oracle Clusterware files on raw or block devices is no longer supported, unless an existing system is being upgraded.

### Oracle Automatic Storage Management Cluster File System (Oracle ACFS)

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is a new multi-platform, scalable file system and storage management design that extends Oracle Automatic Storage Management (Oracle ASM) technology to support all application data. Oracle ACFS provides dynamic file system resizing, and improved performance using the distribution, balancing and striping technology across all available disks, and provides storage reliability through the mirroring and parity protection Oracle ASM provides.

### Oracle ASM Job Role Separation Option with SYSASM

The SYSASM privilege that was introduced in Oracle ASM 11g release 1 (11.1) is now fully separated from the SYSDBA privilege. If you choose to use this optional feature, and designate different operating system groups as the OSASM and the OSDBA groups, then the SYSASM administrative privilege is available only to members of the OSASM group. The SYSASM privilege also can be granted using password authentication on the Oracle ASM instance.

You can designate OPERATOR privileges (a subset of the SYSASM privileges, including starting and stopping Oracle ASM) to members of the OSOPER for ASM group.

Providing system privileges for the storage tier using the SYSASM privilege instead of the SYSDBA privilege provides a clearer division of responsibility between Oracle ASM administration and database administration, and helps to prevent different databases using the same storage from accidentally overwriting each other's files.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

### Cluster Time Synchronization Service

Cluster node times should be synchronized. With this release, Oracle Clusterware provides Cluster Time Synchronization Service (CTSS), which ensures that there is a synchronization service in the cluster. If Network Time Protocol (NTP) is not found during cluster configuration, then CTSS is configured to ensure time synchronization.

### Oracle Enterprise Manager Database Control Provisioning

Oracle Enterprise Manager Database Control 11g provides the capability to automatically provision Oracle Grid Infrastructure and Oracle RAC installations on new nodes, and then extend the existing Oracle Grid Infrastructure and Oracle RAC database to these provisioned nodes. This provisioning procedure requires a successful Oracle RAC installation before you can use this feature.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for information about this feature

### Fixup Scripts and Grid Infrastructure Checks

With Oracle Clusterware 11g release 2 (11.2), Oracle Universal Installer (OUI) detects when minimum requirements for installation are not completed, and creates shell script programs, called fixup scripts, to resolve many incomplete system configuration requirements. If OUI detects an incomplete task that is marked "fixable", then you can easily fix the issue by generating the fixup script by clicking the Fix & Check Again button.

The fixup script is generated during installation. You are prompted to run the script as `root` in a separate terminal session. When you run the script, it raises kernel values to required minimums, if necessary, and completes other operating system configuration tasks.

You also can have Cluster Verification Utility (CVU) generate fixup scripts before installation.

### Grid Plug and Play

In the past, adding or removing servers in a cluster required extensive manual preparation. With this release, you can continue to configure server nodes manually, or use Grid Plug and Play to configure them dynamically as nodes are added or removed from the cluster.

Grid Plug and Play reduces the costs of installing, configuring, and managing server nodes by starting a grid naming service within the cluster to allow each node to perform the following tasks dynamically:

- Negotiating appropriate network identities for itself
- Acquiring additional information it needs to operate from a configuration profile
- Configuring or reconfiguring itself using profile data, making host names and addresses resolvable on the network

Because servers perform these tasks dynamically, the number of steps required to add or delete nodes is minimized.

### Improved Input/Output Fencing Processes

Oracle Clusterware 11g release 2 (11.2) replaces the `oprocd` and Hangcheck processes with the cluster synchronization service daemon Agent and Monitor to provide more accurate recognition of hangs and to avoid false termination.

### Intelligent Platform Management Interface (IPMI) Integration

Intelligent Platform Management Interface (IPMI) is an industry standard management protocol that is included with many servers today. IPMI operates independently of the operating system, and can operate even if the system is not powered on. Servers with IPMI contain a baseboard management controller (BMC) which is used to communicate to the server.

If IPMI is configured, then Oracle Clusterware uses IPMI when node fencing is required and the server is not responding.

### Oracle Clusterware Out-of-place Upgrade

With this release, you can install a new version of Oracle Clusterware into a separate home from an existing Oracle Clusterware installation. This feature reduces the downtime required to upgrade a node in the cluster. When performing an out-of-place upgrade, the old and new version of the software are present on the nodes at the same time, each in a different home location, but only one version of the software is active.

### Oracle Clusterware Administration with Oracle Enterprise Manager

With this release, you can use Oracle Enterprise Manager Cluster Home page to perform full administrative and monitoring support for both standalone database and Oracle RAC environments, using High Availability Application and Oracle Cluster Resource Management.

When Oracle Enterprise Manager is installed with Oracle Clusterware, it can provide a set of users that have the Oracle Clusterware Administrator role in Oracle Enterprise Manager, and provide full administrative and monitoring support for High Availability application and Oracle Clusterware resource management. After you have completed installation and have Oracle Enterprise Manager deployed, you can provision additional nodes added to the cluster using Oracle Enterprise Manager.

### SCAN for Simplified Client Access

With this release, the Single Client Access Name (SCAN) is the host name to provide for all clients connecting to the cluster. The SCAN is a domain name registered to at least one and up to three IP addresses, either in the domain name service (DNS) or the Grid Naming Service (GNS). The SCAN eliminates the need to change clients when nodes are added to or removed from the cluster. Clients using the SCAN can also access the cluster using EZCONNECT.

### SRVCTL Command Enhancements for Patching

With this release, you can use the server control utility SRVCTL to shut down all Oracle software running within an Oracle home, in preparation for patching. Oracle Grid Infrastructure patching is automated across all nodes, and patches can be applied in a multi-node, multi-patch fashion.

### Typical Installation Option

To streamline cluster installations, especially for those customers who are new to clustering, Oracle introduces the Typical Installation path. Typical installation defaults as many options as possible to those recommended as best practices.

### Voting Disk Backup Procedure Change

In prior releases, backing up the voting disks using a `dd` command was a required postinstallation task. With Oracle Clusterware release 11.2 and later, backing up and restoring a voting disk using the `dd` command is not supported.

Backing up voting disks manually is no longer required, because voting disks are backed up automatically in the OCR as part of any configuration change. Voting disk data is automatically restored to any added voting disks.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/votocr.htm#CWADD833)

## New Features for Release 1 (11.1)

The following is a list of new features for release 1 (11.1)

### Changes in Installation Documentation

With Oracle Database 11g release 1, Oracle Clusterware can be installed or configured as an independent product, and additional documentation is provided on storage administration. For installation planning, note the following documentation:

#### Oracle Database 2 Day + Real Application Clusters Guide

This book provides an overview and examples of the procedures to install and configure a two-node Oracle Clusterware and Oracle RAC environment.

#### Oracle Clusterware Installation Guide

This book (the guide that you are reading) provides procedures either to install Oracle Clusterware as a standalone product, or to install Oracle Clusterware with either Oracle Database, or Oracle RAC. It contains system configuration instructions that require system administrator privileges.

#### Oracle Real Application Clusters Installation Guide

This platform-specific book provides procedures to install Oracle RAC after you have completed an Oracle Clusterware installation. It contains database configuration instructions for database administrators.

#### Oracle Database Storage Administrator's Guide

This book provides information for database and storage administrators who administer and manage storage, or who configure and administer Oracle Automatic Storage Management (Oracle ASM).

#### Oracle Clusterware Administration and Deployment Guide

This is the administrator's reference for Oracle Clusterware. It contains information about administrative tasks, including those that involve changes to operating system configurations and cloning Oracle Clusterware.

#### Oracle Real Application Clusters Administration and Deployment Guide

This is the administrator's reference for Oracle RAC. It contains information about administrative tasks. These tasks include database cloning, node addition and deletion, Oracle Cluster Registry (OCR) administration, use of SRVCTL and other database administration utilities, and tuning changes to operating system configurations.

### Release 1 (11.1) Enhancements and New Features for Installation

The following is a list of enhancements and new features for Oracle Database 11g release 1 (11.1):

#### New SYSASM Privilege and OSASM operating system group for Oracle ASM Administration

This feature introduces a new SYSASM privilege that is specifically intended for performing Oracle ASM administration tasks. Using the SYSASM privilege instead of the SYSDBA privilege provides a clearer division of responsibility between Oracle ASM administration and database administration.

OSASM is a new operating system group that is used exclusively for Oracle ASM. Members of the OSASM group can connect as SYSASM using operating system authentication and have full access to Oracle ASM.

### Oracle Preinstallation RPM (formerly Oracle Validated RPM)

The Oracle Preinstallation RPM can be installed on servers using Red Hat Enterprise Linux or Oracle Linux operating systems. It is available from the Unbreakable Linux Network (ULN). This RPM completes most preinstallation configuration tasks required for installing Oracle Clusterware, including setting kernel parameters and adding required kernel RPMs. It also prepares a server for installation of Oracle RAC. To register your server on the Unbreakable Linux Network, or to find out more information, refer to the following URL:

`https://linux.oracle.com`