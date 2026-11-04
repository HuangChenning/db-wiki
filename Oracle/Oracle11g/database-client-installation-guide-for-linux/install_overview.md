---
title: Overview of Oracle Database Client Installation
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/install_overview.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## 1 Overview of Oracle Database Client Installation

This chapter describes the different installation types of Oracle Database Client and issues to consider before you install Oracle Database Client:

## 1.1 Planning Your Installation

The Oracle Database installation process consists of the following phases:

1. Read the release notes: Read [Oracle Database Release Notes for Linux](https://docs.oracle.com/cd/E11882_01/relnotes.112/e23558/toc.htm) before you begin the installation. The release notes are available with the platform-specific documentation.
	The latest version of the release notes is available at:
	```
	http://docs.oracle.com/
	```
2. Review the licensing information: Although the installation media in your media pack contain many Oracle components, you are permitted to use only those components for which you have purchased licenses.
	Oracle Support Services does not provide support for components for which licenses have not been purchased.
	See Also:
	[Oracle Database Licensing Information](https://docs.oracle.com/cd/E11882_01/license.112/e47877/toc.htm)
3. Plan the installation: This chapter describes the Oracle products that you can install and issues that you must consider before starting the installation.
	You can also refer to [Appendix D](app_faq.md), which covers frequently asked questions about installing Oracle Database components, such as how to install Oracle Database Client if the site uses Oracle applications or if you need multiple Oracle Database Client connections.
4. Complete preinstallation tasks: [Chapter 2](pre_install.md) describes preinstallation tasks that you must complete before installing the product.
5. Install the software: Use the following sections to install Oracle Database:
	- [Chapter 3](inst_task.md) describes how to use Oracle Universal Installer to install Oracle Database Client.
		- [Appendix B](app_gblsupp.md) describes globalization support information.
		- [Appendix A](app_nonint.md) provides information on performing silent installations, which you may want to use if you must perform multiple installations of Oracle Database Client.
		- [Appendix C](app_ts.md) provides troubleshooting advice in case you encounter problems with the installation.
6. Complete postinstallation tasks: [Chapter 4](post_inst_task.md) describes recommended and required postinstallation tasks.

## 1.2 Installation Considerations

This section contains information that you should consider before deciding how to install this product. It contains the following sections:

- Hardware and Software Certification
- Multiple Oracle Homes Support
- About the Oracle Unbreakable Enterprise Kernel for Linux
- Separate 32-Bit Client Software for 64-Bit Platforms

### 1.2.1 Hardware and Software Certification

The platform-specific hardware and software requirements included in this guide were current when this guide was published. However, because new platforms and operating system software versions might be certified after this guide is published, review the certification matrix on the My Oracle Support website for the most up-to-date list of certified hardware platforms and operating system versions. The My Oracle Support website is available at the following URL:

```
https://support.oracle.com/
```

You must register online before using My Oracle Support. After logging in, from the menu options, select the Certifications tab. On the Certifications page, use the Certification Search options to search by Product, Release, and Platform. You can also search using the Certification Quick Link options such as Product Delivery, and Lifetime Support.

### 1.2.2 Multiple Oracle Homes Support

Oracle Database supports multiple Oracle homes. You can install this release or earlier releases of the software more than once on the same system, in different Oracle home directories.

#### 1.2.2.1 Installing the Software on a System with an Existing Oracle Installation

You must install this product into a new Oracle home directory. You cannot install products from one release of Oracle Database into an Oracle home directory of a different release. For example, you cannot install release 11.2 software into an existing Oracle9i Oracle home directory.

Oracle Database Client can be installed in the same Oracle Database home if both products are at the same release level. For example, you can install Oracle Database Client 11g Release 2 (11.2) into an existing Oracle Database 11g Release 2 (11.2) home. If you apply a patch set before installing the client, then you must apply the patch set again.

You can install this release more than once on the same system if each installation is installed in a separate Oracle home directory.

#### 1.2.2.2 Updating the Existing Software with the Current Version

Use the In-Place Upgrade feature to upgrade an existing client installation to the latest release by installing the new client software into an existing client home with the same installation type. For example, if release 11.2.0.1 is installed, then use Oracle Universal Installer to upgrade to release 11.2.0.2.

Consider the following before selecting this option:

- This upgrade is only possible in a client home and not in any other Oracle home that contains non-client installations, such as Database installations.
- This upgrade does not delete files in the client home that are commonly updated by other users. For example, configuration data files.
- This upgrade cannot be performed if processes associated with the Oracle Database Client home are running.

This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

["Performing an In-place Oracle Database Client Upgrade"](inst_task.md)

### 1.2.3 About the Oracle Unbreakable Enterprise Kernel for Linux

The Oracle Unbreakable Enterprise Kernel for Linux is available for x86-64 platforms. It is based on a stable 2.6.32 Linux kernel, and also includes optimizations developed in collaboration with Oracle Database, Oracle middleware, and Oracle hardware engineering teams to ensure stability and optimal performance for the most demanding enterprise workloads.

Oracle highly recommends deploying the Oracle Unbreakable Enterprise Kernel in your Linux environment, especially if you are running Oracle software. However, using Oracle Unbreakable Enterprise Kernel is optional. If you require strict Red Hat Enterprise Linux kernel (RHEL) compatibility, then Oracle Linux also includes a kernel compatible with the RHEL Linux kernel, compiled directly from the Red Hat Enterprise Linux source code.

You can obtain more information about the Oracle Unbreakable Enterprise Kernel for Linux at the following URL:

`http://www.oracle.com/us/technologies/linux`

The Oracle Unbreakable Enterprise Linux kernel installs directly on top of Oracle Linux 6, Oracle Linux 5, Red Hat Enterprise Linux 6, or Red Hat Enterprise Linux 5 starting with Update 5, so you are not required to upgrade to a new major release of the operating system to obtain the benefits and features of this new kernel. You can obtain additional information and download the Oracle Unbreakable Enterprise Kernel for Linux at the following URL:

`http://public-yum.oracle.com/`

The Oracle Unbreakable Enterprise Kernel for Linux is the standard kernel used with Oracle products. The build and QA systems for Oracle Database and other Oracle products use the Oracle Unbreakable Enterprise Kernel for Linux exclusively. The Oracle Unbreakable Enterprise Kernel for Linux is also the kernel used in Oracle Exadata and Oracle Exalogic systems. Oracle Unbreakable Enterprise Kernel for Linux is used in all benchmark tests on Linux in which Oracle participates, and also in the Oracle RDBMS Pre-Install program for x86-64.

Refer to ["Kernel Requirements"](pre_install.md) for Unbreakable Enterprise Kernel requirements.

### 1.2.4 Separate 32-Bit Client Software for 64-Bit Platforms

Refer to ["Separate 32-Bit Client Software for 64-Bit Platforms"](pre_install.md) for more information.

## 1.3 Oracle Database Client Installation Methods

You can choose different installation methods to install Oracle Database Client, as follows:

- Interactive Installation Methods
- Automated Installation Methods Using Response Files

### 1.3.1 Interactive Installation Methods

When you use the interactive method to install Oracle Database Client, Oracle Universal Installer displays a series of screens that enable you to specify all of the required information to install the Oracle Database Client software.

### 1.3.2 Automated Installation Methods Using Response Files

By creating a response file and specifying this file when you start Oracle Universal Installer, you can automate some or all of the Oracle Database installation. These automated installation methods are useful if you must perform multiple installations on similarly configured systems or if the system where you want to install the software does not have X Window system software installed.

When you use a response file, you can run Oracle Universal Installer in the following modes, depending on whether you specify all of the required information or not:

- Silent Mode: Oracle Universal Installer runs in silent mode if you use a response file that specifies all required information, and specify the `-silent` option when starting Oracle Universal Installer. None of the Oracle Universal Installer screens are displayed.
- Response File Mode: Oracle Universal Installer runs in response file mode if you do not specify all required information in the response file.

For more information about these modes and about how to complete an installation using response files, refer to [Appendix A](app_nonint.md).

## 1.4 Oracle Database Client Installation Types

You can choose one of the following installation types when installing Oracle Database Client:

- Instant Client: Enables you to install only the shared libraries required by Oracle Call Interface (OCI), Oracle C++ Call Interface (OCCI), Pro\*C, or Java database connectivity (JDBC) OCI applications. This installation type requires much less disk space than the other Oracle Database Client installation types.
	See Also:
	[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) or [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm) for more information about Instant Client
	Instant Client Light is included in the Instant Client installation and you may want to use Instant Client Light if the applications generate error messages in American English only. Instant Client Light is beneficial to applications that use any of the supported character sets and can accept error messages in American English. The following are the supported character sets:
	- `US7ASCII`
		- `WE8DEC`
		- `WE8ISO8859P1`
		- `WE8EBCDIC37C` for EBCDIC platforms only
		- `WE8EBCDIC1047` for EBCDIC platforms only
		- `WE8MSWIN1252`
		- `UTF8`
		- `AL32UTF8`
		- `AL16UTF16`
	The advantage of using Instant Client Light is that it has a smaller footprint than the regular Instant Client. The shared libraries, which an application must load, are only 34 MB as opposed to the 110 MB that regular Instant Client uses. Therefore, the applications use less memory.
- Administrator: Enables applications to connect to an Oracle Database instance on the local system or on a remote system. It also provides tools that enable you to administer Oracle Database.
- Runtime: Enables applications to connect to an Oracle Database instance on the local system or on a remote system.
- Custom: Enables you to select individual components from the list of Administrator and Runtime components.

## 1.5 Oracle Database Client and Oracle Database Interoperability

For information about interoperability between Oracle Database Client and Oracle Database releases, see Note 207303.1 on the My Oracle Support website at the following URL:

`https://support.oracle.com/`

## 1.6 Simplified Patching of Timestamp with Time Zone Data Type

Starting with Oracle Database 11g Release 2 (11.2), the patching process of `TIMESTAMP WITH TIMEZONE` data type values is simplified.

See Also:

" [Oracle Database 11g Release 2 (11.2) New Features in Globalization](https://docs.oracle.com/cd/E11882_01/server.112/e10729/whatsnew.htm#NLSPG698) " and " [Clients and Servers Operating with Different Versions of Time Zone Files](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG762) " in [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for information about simplified patching process and how certain clients work with server with different time zone files

## 1.7 Software Updates Option

Use the Software Updates feature to dynamically download and apply the latest updates released by Oracle; such as, interim patch updates, critical patch updates, Oracle Universal Installer updates, and the latest patch set updates. This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2).

You can choose to download the latest updates by providing My Oracle Support credentials or you can apply previously downloaded updates. You can also download the updates separately using the `-downloadUpdates` option and later apply them during the installation by providing the location where the updates are present.

See Also:

["Running Oracle Universal Installer"](inst_task.md) for more information on the `-downloadUpdates` option, and dynamically applying software updates during the installation