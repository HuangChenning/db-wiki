---
title: "Oracle® Database Examples Installation Guide"
book: Database Examples Installation Guide
doc_id: E24501-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24501/toc.htm
tags:
  - oracle
  - 11g
  - database-examples-installation-guide
---

## Oracle® Database

Examples Installation Guide

11g Release 2 (11.2)

E24501-04

This document describes how to install and configure the products available on the Oracle Database Examples media. It includes the following sections:

## 1 New Screen in Oracle Database 11g Release 2 (11.2.0.3)

Starting with Oracle Database 11g Release 2 (11.2.0.3), Oracle Universal Installer displays a new screen, Grid Installation Options, which helps in the installation of the examples software on an Oracle RAC database. The examples software is installed in the selected Oracle RAC home on all the nodes where it exists.

## 2 New Feature in Oracle Database 11g Release 2 (11.2.0.2)

This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2). Oracle Universal Installer helps in the installation of critical patch updates, system requirement updates for supported operating systems, and other significant updates to ensure successful installation. Oracle recommends that you enable Software Updates during installation.

If you choose to enable Software Updates, then you must provide a valid My Oracle Support user name and password during installation, so that Oracle Universal Installer (OUI) can download the latest updates. You can also provide the path to the previously downloaded Software Updates package location.

## 3 Products Available on the Oracle Database Examples Media

The following sections describe the products that are installed. You must install these products in an existing Oracle Database 11g Release 2 (11.2) Oracle home:

- Oracle Database Examples
- Oracle JDBC Development Drivers
- Oracle Text Knowledge Base

Note:

The Summary screen provides a detailed list of Oracle Examples to be installed into an existing Oracle Database 11g Oracle home.

### 3.1 Oracle Database Examples

Oracle Database Examples include a variety of examples and product demonstrations that you can use to learn about the products, options, and features of Oracle Database. Many of these examples are designed to work with the Sample Schemas, which you can install in any Oracle Database. Many of the documents in the Oracle Documentation Library use the example programs and scripts provided with the Oracle Database Examples.

This section contains the following topics:

- Required Products
- Oracle COM Automation Feature Demos
- Oracle Data Mining Demos
- Oracle Globalization Support Demos
- Oracle Message Gateway Common Companion Files
- Oracle Multimedia Demos
- Oracle Precompiler Demos
- Oracle Spatial Demos
- Oracle SQLJ Demos
- Oracle Internet Directory Client Demos
- Oracle XML Demos
- Oracle Call Interface Demos
- Oracle C++ Call Interface Demos
- Oracle ODBC Companion

#### 3.1.1 Required Products

Before you can use the Oracle Database Examples, you must install the Sample Schemas in an Oracle Database. When you install Oracle Database, or use Database Configuration Assistant to create a database, you can choose to include the Sample Schemas when you create the database. You can also manually install the Sample Schemas in an existing database.

See Also:

[Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm) for information about manually installing the Sample Schemas in an existing database

#### 3.1.2 Oracle COM Automation Feature Demos

Oracle COM Automation Feature for PL/SQL and Java includes examples that demonstrate how to use the feature to build solutions. These demos provide base functionality and can serve as a foundation to build more customized, complex applications that use COM Automation. The demos are based on the human resources schema available with the sample schema. Each demo exposes a core set of APIs that enables you to do simple operations using COM Automation. Each COM Automation server, such as Word and Excel, provides more advanced capabilities than what is offered through the demo APIs. To take advantage of these advanced features, you must design and code your own PL/SQL procedures or Java classes.

See Also:

[Chapter 4, "Oracle COM Automation PL/SQL Demos"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10591/ch4plsql.htm#COMDG005) and [Chapter 5, "Oracle COM Automation Java Demos"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10591/ch5java.htm#COMDG006) in Oracle COM Automation Feature Developer's Guide for Microsoft Windows for more information about these demos

#### 3.1.3 Oracle Data Mining Demos

Oracle Data Mining Demos include Data Mining sample programs that can help you in learning about Oracle Data Mining APIs. The programs illustrate typical approaches to data preparation, algorithm selection, algorithm tuning, testing, and scoring. Each program creates a mining model in the database. All the programs include extensive inline comments to help you understand the code.

See Also:

[Chapter 7, "The Data Mining Sample Programs"](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009) in Oracle Data Mining Administrator's Guide for more information about these demos

#### 3.1.4 Oracle Globalization Support Demos

Oracle Globalization Demos showcase the features and APIs of the Oracle Globalization Development Kit (GDK), which offers a complete framework to ease the development of globalized internet applications. The GDK Example demo illustrates individual functionalities such as locale-sensitive data formatting, linguistic sorting, locale mapping, locale determination, and language detection. The Oracle Store demo illustrates how the GDK features can be integrated to build a complete multilingual J2EE web application that serves users with vastly different locale preferences.

See Also:

[Chapter 8, "Oracle Globalization Development Kit"](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch8gdk.htm#NLSPG008) in Oracle Database Globalization Support Guide for more information about these demos

#### 3.1.5 Oracle Message Gateway Common Companion Files

Oracle Messaging Gateway enables communication between applications based on non-Oracle messaging systems and Oracle Streams AQ. Oracle Streams AQ provides propagation between two Oracle Streams AQ queues to enable e-business (HTTP through IDAP). Messaging Gateway extends this to applications based on non-Oracle messaging systems. The samples provided for Messaging Gateway illustrate message propagating with Oracle AQ, WebSphere MQ Series, and Tibco Rendezvous using message formats that include JMS, LCR, and XML.

There are seven different samples provided with Messaging Gateway, each located in their own subdirectory. Each sample includes a README file that contains detailed information for setting up and executing the samples.

#### 3.1.6 Oracle Multimedia Demos

Oracle Multimedia (formerly Oracle interMedia) is a feature that enables Oracle Database to store, manage, and retrieve images, audio, video, or other heterogenous media data in an integrated fashion with other enterprise information. Oracle Multimedia extends Oracle Database reliability, availability, and data management to multimedia content in traditional, Internet, electronic commerce, and media-rich applications. It includes many scripts and sample applications that you can use. These consist of OCI, SQL, Java, PL/SQL, and ASP/VBScript sample applications (demos).

See Also:

[Appendix A, "Oracle Multimedia Sample Applications"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10777/ap_demos.htm#IMURG10000) in Oracle Multimedia User's Guide for more information about these demos

#### 3.1.7 Oracle Precompiler Demos

Oracle Precompiler Demos show application programmers how to embed SQL operations in C/C++ and COBOL code in a way that is compatible with ANSI standard. A Pro\*C program is a C program containing embedded SQL statements. Oracle Pro\*C/C++ and Pro\*COBOL Demos offer extensions to support dynamic SQL operations, which are operations that can change in real time. It is also possible to use dynamic SQL operations through PL/SQL code (known as anonymous PL/SQL block) with a Pro\*C/C++ and Pro\*COBOL application. Typical applications contain much more static SQL than dynamic SQL. The precompiler translates each embedded SQL statement into calls to the Precompiler run-time library (SQLLIB).

See Also:

- Appendix G, "Sample Programs" in [Pro\*C/C++ Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10825/toc.htm)
- "Sample Programs" in [Pro\*COBOL Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10826/toc.htm)

#### 3.1.8 Oracle Spatial Demos

Oracle Spatial is an integrated set of functions and procedures that enables spatial data to be stored, accessed, and analyzed quickly and efficiently in an Oracle database. Spatial data represents the essential location characteristics of real or conceptual objects as those objects relate to the real or conceptual space in which they exist. Oracle Spatial Demos provide SQL schema and functions that facilitate the storage, retrieval, update, and query of collections of spatial features in an Oracle database.

See Also:

- ["Spatial Examples"](https://docs.oracle.com/cd/E11882_01/appdev.112/e11830/sdo_intro.htm#SPATL484) in Oracle Spatial Developer's Guide
- ["GeoRaster PL/SQL and Java Demo Files"](https://docs.oracle.com/cd/E11882_01/appdev.112/e11827/geor_intro.htm#GEORS951) in Oracle Spatial GeoRaster Developer's Guide
- ["Network Data Model Tutorial and Other Resources"](https://docs.oracle.com/cd/E11882_01/appdev.112/e11831/sdo_net_concepts.htm#TOPOL713) in Oracle Spatial Topology and Network Data Models Developer's Guide

#### 3.1.9 Oracle SQLJ Demos

Oracle SQLJ Demos show application programmers how to embed SQL operations in Java code in a way that is compatible with the Java design philosophy. A SQLJ program is a Java program containing embedded SQL statements. Oracle SQLJ Demos offer extensions to support dynamic SQL operations, which are operations that can change in real time. It is also possible to use dynamic SQL operations through JDBC code or PL/SQL code within a SQLJ application. Typical applications contain much more static SQL than dynamic SQL. SQLJ consists of both a translator and a run-time component and is smoothly integrated into the development environment.

See Also:

[Oracle Database SQLJ Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10590/toc.htm) for more information about these demos

#### 3.1.10 Oracle Internet Directory Client Demos

Oracle Internet Directory Client Demos show application programmers how to use LDAP C and PL/SQL APIs. All LDAP operations based on the C API, require clients to establish an LDAP session with the LDAP server. For LDAP operations based on the PL/SQL API, a database session must first initialize and open an LDAP session. The DBMS\_LDAP package enables PL/SQL applications to access data located in LDAP servers. The names and syntax of the function calls are similar to those of the C API.

See Also:

["Sample C API Usage"](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIMAD2299) in Oracle Fusion Middleware Application Developer's Guide for Oracle Identity Management

#### 3.1.11 Oracle XML Demos

Oracle XML Demos showcase the features of the Oracle XML Developer's Kit (XDK), which is a versatile set of components that enables you to build and deploy C, C++, and Java software programs that process XML.

See Also:

- ["Running the JavaBean Demo Programs"](https://docs.oracle.com/cd/E11882_01/appdev.112/e23582/adx_j_beans.htm#ADXDK19372) in Oracle XML Developer's Kit Programmer's Guide
- ["Using the XML C++ Class Generator Examples"](https://docs.oracle.com/cd/E11882_01/appdev.112/e23582/adx_cp_classgen.htm#ADXDK19946) in Oracle XML Developer's Kit Programmer's Guide
- ["Using the XML Parser Command-Line Utility: Example"](https://docs.oracle.com/cd/E11882_01/appdev.112/e23582/adx_c_parser.htm#ADXDK19765) in Oracle XML Developer's Kit Programmer's Guide

#### 3.1.12 Oracle Call Interface Demos

Oracle Call Interface (OCI) demos include sample C programs to build the OCI APIs. These programs provide examples of the data types, calling conventions, syntax, and semantics of C. The installed demos illustrate the use of OCI features.

See Also:

["OCI Demonstration Programs"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/ociabdem.htm#LNOCI280) in Oracle Call Interface Programmer's Guide for more information about these demos

#### 3.1.13 Oracle C++ Call Interface Demos

Oracle C++ Call Interface (OCCI) demos provide database access APIs for applications written in C++. The control classes enable the applications to connect to the database and create resources like statements and resultsets. The data classes contain various types of data. The object classes and methods provide a navigational interface to access and manipulate objects. The Object Type Translator (OTT) can be used to generate the C++ class headers for the data types defined in Oracle database. The installed demos illustrate the use of classes and methods for OTT and OCCI.

See Also:

["Building OCCI Demos"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10764/introduction.htm#LNCPP20075) in Oracle C++ Call Interface Programmer's Guide for more information about these demos

#### 3.1.14 Oracle ODBC Companion

Oracle ODBC Driver demos provide basic structure of an ODBC application which can be extended to make a full-fledged ODBC application. ODBC being a standard, plenty of sample applications may be found in books which discuss the concept of ODBC driver. For Oracle ODBC Driver specific options, see Help while setting up Data Source Name on Windows.

See Also:

["Using Oracle ODBC Driver"](https://docs.oracle.com/cd/E11882_01/server.112/e10839/app_odbc.htm#UNXAR014) in Oracle Database Administrator's Reference for Linux and UNIX-Based Operating Systems for more information about these demos

### 3.2 Oracle JDBC Development Drivers

Oracle provides a set of JDBC drivers that you can use for debugging the code and other deployment scenarios. These drivers can access Oracle Database release 8.1.7 or later.

### 3.3 Oracle Text Knowledge Base

Oracle Database Examples media installs two Oracle Text knowledge bases, English and French. You can extend the supplied knowledge bases depending on your requirements. Alternatively, you can create your own knowledge bases, in languages other than English and French.

See Also:

[Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm) for more information about creating and extending knowledge bases

## 4 Requirements for Oracle Database Examples

The requirements for installing Oracle Database Examples are as follows:

- Access to Oracle Database
- Free Disk Space

### 4.1 Access to Oracle Database

Before you install products from the Oracle Database Examples media, you must ensure that your system has access to an Oracle Database 11g Release 2 (11.2) Oracle home. If required, you must first install or upgrade to this release of Oracle Database.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about installing Oracle Database

Identify the Oracle home directory used by the Oracle Database installation.

On UNIX platforms, check the contents of the `oratab` file by using the following command:

```
# more /etc/oratab
```

On Windows platforms:

1. From the Start menu, choose Programs, then Oracle - HOME\_NAME, then Oracle Installation Products, then Universal Installer.
2. When the Welcome screen appears, click Installed Products.
	The Inventory screen appears, listing all of the Oracle homes on the system and the products installed in each Oracle home.
3. On the Inventory screen, expand each Oracle home and locate Oracle Database 11g.
4. Click Close and then Cancel to exit Oracle Universal Installer.

### 4.2 Free Disk Space

Verify that the file system that contains the Oracle home directory has at least 650 MB of free disk space on UNIX and at least 575 MB of free disk space on Windows.

On UNIX platforms:

Use the `df -k` `oracle_home_path` command to check that the Oracle home directory has enough space.

`oracle_home_path` is the directory where Oracle home is installed.

On Windows:

1. Double-click My Computer.
2. Right-click the drive where the Oracle software is to be installed.
3. Select Properties.

## 5 Download Oracle Database Examples

This section describes how to download Oracle Database Examples on your computer to a location other than Oracle Database 11g Release 2 (11.2) Oracle home.

1. Go to the Oracle Database 11g download page on Oracle Technology Network:
	`http://www.oracle.com/technetwork/database/enterprise-edition/downloads/index.html`
2. Select the See All link, and then select the Oracle Database Examples zip file under the heading Oracle Database 11g Examples (formerly Companion).
	For example, for Linux x86, select `linux_11gR2_examples.zip`.

Install Oracle Database Examples

You must install Oracle Database Examples in an existing Oracle Database 11g Release 2 (11.2) Oracle home.

To install Oracle Database Examples:

1. Log in as Administrator on the computer where Oracle Database is installed.
	On UNIX platforms, log in as the Oracle software owner user (`oracle`) and set the `DISPLAY` environment variable.
	On Windows platforms, log in as a member of the Administrators group to the computer on which you want to install Oracle components.
	If you are installing on a Primary Domain Controller (PDC) or a Backup Domain Controller (BDC), log on as a member of the Domain Administrators group.
2. Verify that the Oracle Database that you plan to use is accessible as described in "Access to Oracle Database".
3. Navigate to the directory where you downloaded the installation files and run the following command to start Oracle Universal Installer:
	On UNIX platforms:
	```
	$ ./runInstaller
	```
	On Windows platforms:
	Double-click `setup.exe.`
4. Downloading Updates Before Installation
	Starting with Oracle Database 11g Release 2 (11.2.0.2), if you plan to run the installation in a secured data center, then you can download updates before starting the installation by starting Oracle Universal Installer on a system that has Internet access in update download mode. In Download Software Updates screen, you have the following options to choose from:
	- Use My Oracle Support credentials for download: Select this option to download and apply the latest software updates.
		Click Proxy Settings to configure a proxy for Oracle Universal Installer to use to connect to the Internet. Provide the proxy server information for your site, along with a user account that has access to the local area network through which the server is connecting. Starting with Oracle Database 11g Release 2 (11.2.0.3), you can enter the Proxy Realm information. The proxy realm information is case-sensitive. If you do not have a proxy realm, then you do not need to provide an entry for the Proxy Username, Proxy Password, and Proxy Realm fields.
		Click Test Connection to ensure that your proxy settings are correctly entered, and the installer can download the updates.
		- Use pre-downloaded software updates: In the Location field, enter the path where you have the pre-downloaded patch updates.
		Note:
		To run the installation in a secured data center, download updates before starting the installation by starting Oracle Universal Installer on a system that has Internet access.
		To use this option perform the following steps:
		- Use the `-downloadUpdates` flag in `runInstaller` or `setup.exe`:
			```
			./runInstaller -downloadUpdates
			```
				- Provide My Oracle Support user name and password along with proxy settings, if required, on the Provide My Oracle Support credentials screen.
				- Then, enter the Download location and click Download on the Download software updates screen.
				- If updates are available, then they are downloaded in the location provided. The Finish Updates screen shows the successful download of the updates. Click Close.
				- Download the updates to a directory on a server, where the Oracle Universal Installer runs.
				- Once the download completes, restart Oracle Universal Installer and use that download location in the location field of the Use pre-downloaded software updates option.
			Note:
			For an example installation done earlier with software updates enabled, user can reuse the download location of that install.
		- Skip software updates: Choose this option, if you do not want any software updates.
	Click Next to continue.
5. The Apply Software Updates screen, lists out the updates available. It displays the following details:
	- Patch Numbers
		- Description
		- Related Notes
	If Use My Oracle Support credentials for download option is chosen in the previous screen, select the Download and apply all updates check box. This downloads and applies the latest updates during the installation. However, you can also change the location to where you want to download the latest updates.
	If Use pre-downloaded software updates option is chosen in the previous screen, select the Apply all updates check box. This applies the updates during the installation.
	Click Next to continue.
6. On the Specify Installation Location screen, enter the following:
	- Oracle Base: The Oracle base directory is a top-level directory for Oracle software installations. The Oracle base path appears by default. You can change the path based on your requirement.
		- Software Location: In the Software Location field, enter the full path where you want to install Oracle Database Examples. You must install Oracle Database Examples in an existing Oracle home.
	See Also:
	"Access to Oracle Database" for information about finding the Oracle home
	If Oracle Real Application Clusters (Oracle RAC) is installed in the Oracle home that you select, then Oracle Universal Installer displays the Grid Installation Options screen. The examples software will be installed in the selected Oracle RAC home on all the nodes where it exists. The nodes listed in the table are the nodes on which the Oracle Inventory has registered an installed Oracle RAC home.
	Check to ensure that each node listed is up and running before clicking Next.
	Note:
	On an Oracle RAC installation, the software is installed on all the cluster nodes.
7. On the Perform Prerequisite Checks screen, check for and correct any errors that may have occurred while Oracle Universal Installer was checking your system. If you click Check Again, then you can run the prerequisite check again to see if the minimum requirements are met to carry on with the installation. Click Fix & Check Again, if you want the installer to fix the problem and check the system requirements again.
	Note:
	The Fix & Check Again option generates a script (UNIX only) that sets some system parameters to Oracle-recommended values. You must run the script as the `root` user. Oracle recommends that you do not modify the contents of this script.
	From the list, select an option:
	- Show Failed: To get a list of prerequirement checks that failed.
		- Show All: To get a list of all the prerequirement checks run.
		- Show Succeeded: To get a list of the prerequirement checks that were successful.
8. Review the information displayed on the Summary screen. Click Save Response File to save all the installation steps into a response file.
	Click Finish.
9. The Install Product screen appears when the product is installing. Installation operations include executing actions such as file copy and adding services on Windows systems and linking on UNIX systems, and executing decision points and calculations.
10. The Finish screen appears when the installation is completed.
	Click Close to exit from Oracle Universal Installer.

## 6 Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility Program website at `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=docacc`.

Access to Oracle Support

Oracle customers have access to electronic support through My Oracle Support. For information, visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=info` or visit `http://www.oracle.com/pls/topic/lookup?ctx=acc&id=trs` if you are hearing impaired.

---

Oracle Database Examples Installation Guide, 11g Release 2 (11.2)

E24501-04

Copyright © 2013, Oracle and/or its affiliates. All rights reserved.

This software and related documentation are provided under a license agreement containing restrictions on use and disclosure and are protected by intellectual property laws. Except as expressly permitted in your license agreement or allowed by law, you may not use, copy, reproduce, translate, broadcast, modify, license, transmit, distribute, exhibit, perform, publish, or display any part, in any form, or by any means. Reverse engineering, disassembly, or decompilation of this software, unless required by law for interoperability, is prohibited.

The information contained herein is subject to change without notice and is not warranted to be error-free. If you find any errors, please report them to us in writing.

If this is software or related documentation that is delivered to the U.S. Government or anyone licensing it on behalf of the U.S. Government, the following notice is applicable:

U.S. GOVERNMENT END USERS: Oracle programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, delivered to U.S. Government end users are "commercial computer software" pursuant to the applicable Federal Acquisition Regulation and agency-specific supplemental regulations. As such, use, duplication, disclosure, modification, and adaptation of the programs, including any operating system, integrated software, any programs installed on the hardware, and/or documentation, shall be subject to license terms and license restrictions applicable to the programs. No other rights are granted to the U.S. Government.

This software or hardware is developed for general use in a variety of information management applications. It is not developed or intended for use in any inherently dangerous applications, including applications that may create a risk of personal injury. If you use this software or hardware in dangerous applications, then you shall be responsible to take all appropriate fail-safe, backup, redundancy, and other measures to ensure its safe use. Oracle Corporation and its affiliates disclaim any liability for any damages caused by use of this software or hardware in dangerous applications.

Oracle and Java are registered trademarks of Oracle and/or its affiliates. Other names may be trademarks of their respective owners.

Intel and Intel Xeon are trademarks or registered trademarks of Intel Corporation. All SPARC trademarks are used under license and are trademarks or registered trademarks of SPARC International, Inc. AMD, Opteron, the AMD logo, and the AMD Opteron logo are trademarks or registered trademarks of Advanced Micro Devices. UNIX is a registered trademark of The Open Group.

This software or hardware and documentation may provide access to or information on content, products, and services from third parties. Oracle Corporation and its affiliates are not responsible for and expressly disclaim all warranties of any kind with respect to third-party content, products, and services. Oracle Corporation and its affiliates will not be responsible for any loss, costs, or damages incurred due to your access to or use of third-party content, products, or services.