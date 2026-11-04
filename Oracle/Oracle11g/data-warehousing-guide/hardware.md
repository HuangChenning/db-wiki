---
title: Hardware and I/O Considerations in Data Warehouses
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/hardware.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

## 4 Hardware and I/O Considerations in Data Warehouses

This chapter explains some of the hardware and I/O issues in a data warehousing environment and includes the following topics:

- Overview of Hardware and I/O Considerations in Data Warehouses
- Storage Management

## Overview of Hardware and I/O Considerations in Data Warehouses

I/O performance should always be a key consideration for data warehouse designers and administrators. The typical workload in a data warehouse is especially I/O intensive, with operations such as large data loads and index builds, creation of materialized views, and queries over large volumes of data. The underlying I/O system for a data warehouse should be designed to meet these heavy requirements.

In fact, one of the leading causes of performance issues in a data warehouse is poor I/O configuration. Database administrators who have previously managed other systems will likely need to pay more careful attention to the I/O configuration for a data warehouse than they may have previously done for other environments.

This chapter provides the following five high-level guidelines for data-warehouse I/O configurations:

The I/O configuration used by a data warehouse depends on the characteristics of the specific storage and server capabilities, so the material in this chapter is only intended to provide guidelines for designing and tuning an I/O system.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for additional information on I/O configurations and tuning

### Configure I/O for Bandwidth not Capacity

Storage configurations for a data warehouse should be chosen based on the I/O bandwidth that they can provide, and not necessarily on their overall storage capacity. Buying storage based solely on capacity has the potential for making a mistake, especially for systems less than 500GB is total size. The capacity of individual disk drives is growing faster than the I/O throughput rates provided by those disks, leading to a situation in which a small number of disks can store a large volume of data, but cannot provide the same I/O throughput as a larger number of small disks.

As an example, consider a 200GB data mart. Using 72GB drives, this data mart could be built with as few as six drives in a fully-mirrored environment. However, six drives might not provide enough I/O bandwidth to handle a medium number of concurrent users on a 4-CPU server. Thus, even though six drives provide sufficient storage, a larger number of drives may be required to provide acceptable performance for this system.

While it may not be practical to estimate the I/O bandwidth that is required by a data warehouse before a system is built, it is generally practical with the guidance of the hardware manufacturer to estimate how much I/O bandwidth a given server can potentially utilize, and ensure that the selected I/O configuration will be able to successfully feed the server. There are many variables in sizing the I/O systems, but one basic rule of thumb is that your data warehouse system should have multiple disks for each CPU (at least two disks for each CPU at a bare minimum) to achieve optimal performance.

### Stripe Far and Wide

The guiding principle in configuring an I/O system for a data warehouse is to maximize I/O bandwidth by having multiple disks and channels access each database object. You can do this by striping the datafiles of the Oracle Database. A striped file is a file distributed across multiple disks. This striping can be managed by software (such as a logical volume manager), or within the storage hardware. The goal is to ensure that each tablespace is striped across a large number of disks (ideally, all of the disks) so that any database object can be accessed with the highest possible I/O bandwidth.

### Use Redundancy

Because data warehouses are often the largest database systems in a company, they have the most disks and thus are also the most susceptible to the failure of a single disk. Therefore, disk redundancy is a requirement for data warehouses to protect against a hardware failure. Like disk-striping, redundancy can be achieved in many ways using software or hardware.

A key consideration is that occasionally a balance must be made between redundancy and performance. For example, a storage system in a RAID-5 configuration may be less expensive than a RAID-0+1 configuration, but it may not perform as well, either. Redundancy is necessary for any data warehouse, but the approach to redundancy may vary depending upon the performance and cost constraints of each data warehouse.

### Test the I/O System Before Building the Database

The most important time to examine and tune the I/O system is before the database is even created. Once the database files are created, it is more difficult to reconfigure the files. Some logical volume managers may support dynamic reconfiguration of files, while other storage configurations may require that files be entirely rebuilt to reconfigure their I/O layout. In both cases, considerable system resources must be devoted to this reconfiguration.

When creating a data warehouse on a new system, the I/O bandwidth should be tested before creating all of the database datafiles to validate that the expected I/O levels are being achieved. On most operating systems, this can be done with simple scripts to measure the performance of reading and writing large test files.

### Plan for Growth

A data warehouse designer should plan for future growth of a data warehouse. There are many approaches to handling the growth in a system, and the key consideration is to be able to grow the I/O system without compromising on the I/O bandwidth. You cannot, for example, add four disks to an existing system of 20 disks, and grow the database by adding a new tablespace striped across only the four new disks. A better solution would be to add new tablespaces striped across all 24 disks, and over time also convert the existing tablespaces striped across 20 disks to be striped across all 24 disks.

## Storage Management

Two features to consider for managing disks are Oracle Managed Files and Automatic Storage Management. Without these features, a database administrator must manage the database files, which, in a data warehouse, can be hundreds or even thousands of files. Oracle Managed Files simplifies the administration of a database by providing functionality to automatically create and manage files, so the database administrator no longer needs to manage each database file. Automatic Storage Management provides additional functionality for managing not only files but also the disks. With Automatic Storage Management, the database administrator would administer a small number of disk groups. Automatic Storage Management handles the tasks of striping and providing disk redundancy, including rebalancing the database files when new disks are added to the system.

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for more details