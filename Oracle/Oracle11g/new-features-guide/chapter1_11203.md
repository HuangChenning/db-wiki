---
title: Oracle Database 11g Release 2 (11.2.0.3) New Features
book: New Features Guide
doc_id: E41360-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41360/chapter1_11203.htm
tags:
  - oracle
  - 11g
  - new-features-guide
---

## 2 Oracle Database 11g Release 2 (11.2.0.3) New Features

This chapter contains descriptions of all of the features that are new to Oracle Database 11g Release 2 (11.2.0.3).

## 2.1 General

The following sections describe the new features for Oracle Database 11g Release 2 (11.2.0.3).

### 2.1.1 Support Hybrid Columnar Compression on Pillar Axiom and Sun ZFSSA

Oracle's Hybrid Columnar Compression (HCC) technology is a new (to Oracle Database 11g Release 2) method for organizing data within a database block. HCC utilizes a combination of both row and columnar methods for storing data. A logical construct called the compression unit is used to store a set of HCC-compressed rows. When data is loaded, groups of rows are stored in columnar format, with the values for a given column stored and compressed together. After the column data for a set of rows has been compressed, it is fit into the compression unit. Storing column data together, with the same data type and similar characteristics, dramatically increases the storage savings achieved from compression. This feature extends Hybrid Columnar Compression to Pillar Axiom and Sun ZFS Storage Appliance (ZFSSA) storage.

The support of Hybrid Columnar Compression on Pillar and ZFSSA enables Oracle Database users to utilize Oracle's Hybrid Columnar Compression on Pillar Axiom and Sun ZFS Storage Appliance (ZFSSA) storage hardware. This provides the storage benefits of Oracle's Hybrid Columnar Compression, which had previously been exclusive to the Oracle Exadata platform, to Oracle Database users who use Pillar Axiom or Sun ZFSSA storage (or both), enabling compression ratios of 10x to 50x, depending on the data and the compression level chosen by the user.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for details

### 2.1.2 Support for SHA-2 Certificate Signatures

With this new feature, the database can handle SHA-2 (256 bit) signed certificates in addition to older SHA-1 signed certificates. These certificates are issued by a separate certificate authority and are exchanged between the database and a client when a secure database connection is being established (for example, where certificate-based network encryption and authentication are being used).

This enhancement is particularly critical for customers who are facing deadlines for when their certificate authorities will stop issuing older SHA-1 signed certificates.

### 2.1.3 TDE Hardware Acceleration for Solaris

Transparent Data Encryption (TDE) can automatically detect whether the database host machine includes specialized cryptographic silicon that accelerates the encryption or decryption processing. When detected, TDE uses the specialized silicon for cryptographic processing accelerating the overall cryptographic performance significantly.

In prior releases, cryptographic hardware acceleration for TDE was only available on Intel Xeon, and only for Linux. With release 11.2.0.3 and later releases, it works with the current versions of Solaris 11 running on both SPARC T-Series and Intel Xeon.

### 2.1.4 Support for Multiple Certificates on Smart Card

Consider the scenario, a database user inserts a card containing one or more digital certificates into a card reader device and manually enters a corresponding personal identification number (PIN). Oracle has supported card-based authentication to the database and, starting with release 11.2.0.3, can now handle situations where multiple certificates are contained on the card. The database attempts to intelligently select which certificate to read and, if it cannot figure out which one to read, a selection box pops up on the Windows client machine.

This is an important enhancement for customers who use card-based, two-factor authentication to log in to Oracle Database. In August 2004, the Homeland Security Presidential Directive Number 12 (HSPD-12) was issued to unify the government's identification badge systems. The new guidelines are dictating the deployment of Common Access Cards (CAC) that contain digital certificates.

### 2.1.5 QoS Management Support for Oracle RAC Enterprise Edition

Oracle Database Quality of Service (QoS) Management allows system administrators to directly measure application service levels hosted on Oracle RAC Enterprise Edition databases. Using a policy-based architecture, QoS Management correlates accurate run-time performance and resource metrics based on user-defined workload classes. QoS Management then presents them in an integrated Enterprise Manager dashboard to review real-time performance of consolidated applications. In conjunction with Cluster Health Monitor (CHM), QoS Management's memory guard detects nodes that are at risk of failure due to the over commitment of memory. QoS Management responds by automatically preventing new connections thus preserving existing workloads and restores connectivity once sufficient memory is available again.

The benefits of this feature aids in the schema and database consolidation of applications within Oracle Real Application Clusters yielding information technology efficiency and cost savings. This feature also actively protects application availability under high memory conditions with memory guard.

### 2.1.6 QoS Management Support for Instance Caging on Oracle Exadata

Oracle Database Quality of Service (QoS) Management allows system administrators to directly measure application service levels hosted on Oracle RAC Enterprise Edition databases. Using a policy-based architecture, QoS Management correlates accurate run-time performance and resource metrics based on user-defined workload classes, analyzes this data with its expert system to identify bottlenecks, and produces recommended resource adjustments to meet and maintain performance objectives under dynamic load conditions. QoS Management then presents the findings in an integrated Enterprise Manager dashboard to review real-time performance of consolidated applications. Along with moving the server between server pools, QoS Management now also supports moving CPUs between databases within the same pool to better manage performance in consolidated Oracle Exadata deployments.

This new support manages service-level agreements (SLA) for Online Transaction Processing (OLTP) database applications consolidated on Oracle Exadata yielding information technology efficiency and cost savings.

### 2.1.7 Oracle ACFS Snapshot Enhancements

The read/write snapshot feature for Oracle Automatic Storage Management Cluster File System (Oracle ACFS) adds support for fast creation of an Oracle ACFS snapshot image that can be both read and written without impacting the state of the Oracle ACFS primary file system hosting the snapshot images.

With this enhancement, you can test new versions of application software on production file data reflected in the read/write snapshot image without modifying the original production file system.

You can also run what-if scenarios on a real data set without modifying the original file system.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for details

### 2.1.8 Oracle ACFS Security and Encryption Features

The Oracle Automatic Storage Management Cluster File System (Oracle ACFS) security feature provides realm-based security for Oracle ACFS.

The Oracle ACFS encryption feature enables data stored on disk (data-at-rest) to be encrypted.

Oracle ACFS security feature provides the ability to create realms to specify security policies for users or groups for accessing file system objects. The Oracle ACFS security feature provides finer-grained access control on top of the access control provided by the operating system.

Oracle ACFS encryption feature provides the ability to keep data in an Oracle ACFS file system in encrypted format to prevent unauthorized use of data in the case of data loss or theft.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for details

### 2.1.9 Support for ACFS Replication and Tagging on Windows

Support for replication and tagging functionality is now available on the Windows platform.

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) replication enables replication of Oracle ACFS file systems across the network to a remote site, providing disaster recovery capability for the file system.

Oracle ACFS tagging assigns a common naming attribute to a group of files. Oracle ACFS replication can use this tag to select files with a unique tag name for replication to a different remote cluster site. The tagging option avoids having to replicate an entire Oracle ACFS file system.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for details

### 2.1.10 Oracle LogMiner Support for Binary XML

This feature extends Oracle LogMiner data type support to include support for XMLType columns and tables stored in binary format.

Oracle LogMiner can now be used with applications having XML stored using binary format.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for details

### 2.1.11 SQL Apply Support for Binary XML

This feature extends SQL Apply data type support to include support for XMLType columns and tables stored in binary format.

SQL Apply can now be used with applications having XML stored using binary format.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for details

### 2.1.12 Oracle LogMiner Support for Object Relational Model

This feature extends Oracle LogMiner data type support to include support for XMLType columns and tables stored using the Object Relational (O/R) model.

Oracle LogMiner can now be used with applications having Oracle XML stored using the O/R model.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/toc.htm) for details

### 2.1.13 SQL Apply Support for Object Relational Model

This feature extends SQL Apply data type support to include support for XMLType columns and tables stored using the Object Relational (O/R) model.

SQL Apply can now be used with applications having XML stored using the O/R model.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for details

### 2.1.14 Deprecation of Obsolete Oracle XML DB Functions and Packages

The following Oracle XML DB constructs are deprecated in Oracle Database 11g Release 2 (11.2.0.3):

- PL/SQL procedure `DBMS_XDB_ADMIN.createRepositoryXMLIndex`
- PL/SQL procedure `DBMS_XDB_ADMIN.XMLIndexAddPath`
- PL/SQL procedure `DBMS_XDB_ADMIN.XMLIndexRemovePath`
- PL/SQL procedure `DBMS_XDB_ADMIN.dropRepositoryXMLIndex`
- XML schema annotation (attribute) `csx:encodingType`
- XMLIndex index on `CLOB` portions of hybrid XMLType storage, that is, on `CLOB` data that is embedded within object relational storage

These constructs are still supported in 11.2.0.3 for backward compatibility, but Oracle recommends that you do not use them in new applications.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for details

### 2.1.15 Oracle Warehouse Builder Support for Partition DML

In this release, Oracle Warehouse Builder (OWB) can now generate DML specific to manipulating database partitions. This allows OWB users to perform extract, transform, and load (ETL) operations with all types of partitioned tables.

This feature enables fuller exploitation of database resources and capabilities, and improves developer and DBA productivity by making these capabilities available from within OWB.

For additional information, see the Oracle Warehouse Builder documentation.

### 2.1.16 Enhanced Partitioning Support in Oracle Warehouse Builder

In this release, Oracle Warehouse Builder (OWB) exposes the full range of database partitioning types available up through Oracle Database 11g Release 2 (11.2.0.2). This allows OWB users to design and perform extract, transform, and load (ETL) operations with all types of partitioned tables.

This feature improves developer productivity by making these capabilities available from within OWB and enables fuller exploitation of database resources and capabilities.

For additional information, see the Oracle Warehouse Builder documentation.

### 2.1.17 Oracle Warehouse Builder External Table Data Pump Support

In this release, Oracle Warehouse Builder (OWB) exposes the database support for the `ORACLE_DATAPUMP` access driver. This enables OWB to use external tables to unload data to Data Pump export files and load from Data Pump export files through external tables in extract, transform, and load (ETL) mappings.

Use of Data Pump export files for moving bulk data is the recommended best practice for ETL into an Oracle data warehouse because it is faster than other methods (such as using database links) of moving data between Oracle databases.

For additional information, see the Oracle Warehouse Builder documentation.

### 2.1.18 Oracle Warehouse Builder External Table Preprocessor Support

In this release, Oracle Warehouse Builder (OWB) exposes the database support for the external table preprocessor.

The external table preprocessor enables more flexible handling of external table source files, such as compressed flat files or multiple files, from within extract, transform, and load (ETL) mappings.

For additional information, see the Oracle Warehouse Builder documentation.

### 2.1.19 Compressed Table and Partition Support in Oracle Warehouse Builder

In this release, Oracle Warehouse Builder (OWB) exposes the table-level and partition-level compression options of all Oracle Database releases up to Oracle Database 11g Release 2 (11.2.0.2). This allows OWB users to manage the compression of tables and individual partitions as part of the design of their sources and targets.

This feature improves developer productivity by eliminating the need to manage these options outside of OWB and enables fuller exploitation of database resources.

For additional information, see the Oracle Warehouse Builder documentation.

### 2.1.20 Support for PL/SQL Native Compilation

Oracle Warehouse Builder (OWB) now supports PL/SQL native compilation. With PL/SQL native compilation enabled, the PL/SQL statements in a PL/SQL unit are compiled into native code and stored in the catalog. The native code need not be interpreted at run time, therefore it runs faster.

PL/SQL native compilation provides the greatest performance gains for computation-intensive procedural operations, such as certain data warehouse computations that are usually not performed in set-based SQL.

For additional information, see the Oracle Warehouse Builder documentation.