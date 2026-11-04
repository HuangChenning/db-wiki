---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-i-introduction/exploring-considerations-for-oracle-asm-storage.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Exploring Considerations for Oracle ASM Storage

Several issues should be considered about the storage subsystem before you configure Oracle Automatic Storage Management (Oracle ASM).

When preparing your storage to use Oracle ASM, first determine the storage option for your system and then prepare the disk storage for your specific operating system environment.

When configuring your system's storage, you must consider the initial capacity of the system and your plans for future growth. Oracle ASM simplifies the task of accommodating growth. However, your growth plans can affect choices, such as the size of the Oracle ASM disks. You must also consider that I/O performance depends on the interconnect between the storage and host, not just the storage disks. As you scale up the number of nodes in a cluster, you must also scale up the storage subsystem.

## Storage Resources for Disk Groups

There are various storage resources that can be used to create Oracle ASM disk groups.

You can create an Oracle ASM disk group using one of the following storage resources:

- Disk Partition
	A disk partition can be the entire disk drive or a section of a disk drive. However, the Oracle ASM disk cannot be in a partition that includes the partition table because the partition table would be overwritten.
- Logical Unit Number (LUN)
	A LUN is a disk presented to a computer system by a storage array. Oracle recommends that you use hardware RAID functionality to create LUNs. Storage hardware RAID 0+1 or RAID5, and other RAID configurations, can be provided to Oracle ASM as Oracle ASM disks.
- Logical Volume
	A logical volume is supported in less complicated configurations where a logical volume is mapped to a LUN, or a logical volume uses disks or raw partitions. Logical volume configurations are not recommended by Oracle because they create a duplication of functionality. Oracle also does not recommended using logical volume manager s for mirroring because Oracle ASM provides mirroring.
- Network File System (NFS)
	An Oracle ASM disk group can be created from NFS files, including Oracle Direct NFS (dNFS). The NFS files that are provisioned to a disk group may be from multiple NFS servers to provide better load balancing and flexible capacity planning.
	You can use NFS, with or without Direct NFS, to store data files. However, NFS is not supported for Oracle Clusterware files. To install Oracle Real Application Clusters (Oracle RAC) on Windows using NFS, you must also have access to a shared storage method other than NFS for Oracle Clusterware files.
	NFS-based quorum disks (quorum failure groups) should not use Direct NFS (dNFS) because dNFS does not support soft mounts. Instead, use a soft mount of a NFS mount point for quorum disks. When using a soft mount, Oracle ASM handles an I/O failure gracefully, and sets only the associated quorum disk offline.
	With hard mounts, the Oracle ASM or the database instance may hang if the NFS server becomes unavailable. Note that these hang situations can occur whether or not Direct NFS is used and whether or not Oracle ASM is used for mirroring.
	See also
	[Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWLIN) for your operating system for information about Oracle Direct NFS and storage requirements for Oracle ASM

Note:

- Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes and Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file systems are currently not supported on disk groups that have been created from NFS or Common Internet File System (CIFS) files. However, Oracle ACFS file systems may be exported as NFS or CIFS file systems to network clients in some cases. Samba/CIFS clients on Windows cannot use ACLs when interfacing with Oracle ACFS Linux, Solaris, or AIX servers.
- Mounting loopback file systems over Oracle ACFS files is not supported.
- Block or raw devices are not supported by Oracle Universal Installer (OUI) or Database Configuration Assistant (DBCA).

The procedures for preparing storage resources for Oracle ASM are:

- Identify or create the storage devices for Oracle ASM by identifying all of the storage resource device names that you can use to create an Oracle ASM disk group. For example, on Linux systems device names are typically presented from the `/dev` directory with the `/dev/` *device\_name\_identifier* name syntax.
- Change the ownership and the permissions on storage device resources.
	For example, the following steps are required on Linux systems:
	- Change the user and group ownership of devices, such as `grid:asmdba`
		For information about Oracle ASM privileges, see [About Privileges for Oracle ASM](administering-oracle-asm-instances.md).
		- Change the device permissions to read/write
	Note:
	To ensure that ownership and permission settings are persistent, you can use `udev` to ensure that the disks do not revert to root ownership when the systems restart.

After you have configured Oracle ASM, ensure that disk discovery has been configured correctly by setting the `ASM_DISKSTRING` initialization parameter. For information about the `ASM_DISKSTRING` parameter, see [ASM\_DISKSTRING](administering-oracle-asm-instances.md).

Note:

Setting the ownership to `oracle:dba` is one example that corresponds to the default settings. A nondefault installation may require different settings. In general, the owner of the disk devices should be the same as the owner of the Oracle binary software. The group ownership should be OSDBA of the Oracle ASM instance, which is defined at installation. For information about Oracle ASM privileges, see [About Privileges for Oracle ASM](administering-oracle-asm-instances.md).

For detailed information about preparing disks for an Oracle ASM installation, refer to your platform-specific installation guide for Oracle Database, Oracle Clusterware, and Oracle Real Application Clusters (Oracle RAC).

See also

Oracle Exadata documentation for information about preparing Oracle Exadata storage

## Oracle ASM and Multipathing

Multipathing solutions provide failover by using redundant physical path components.

These redundant physical path components include adapters, cables, and switches that reside between the server and the storage subsystem. If one or more of these components fails, then applications can still access their data, eliminating a single point of failure with the Storage Area Network (SAN), Host Bus Adapter, interface cable, or host port on a multiported storage array.

Multipathing is a software technology implemented at the operating system device driver level. Multipathing creates a pseudo device to facilitate the sharing and balancing of I/O operations across all of the available I/O paths. Multipathing also improves system performance by distributing the I/O load across all available paths, providing a higher level of data availability through automatic failover and failback.

Although Oracle ASM is not designed with multipathing functionality, Oracle ASM does operate with multipathing technologies. Multipathing technologies are available from many sources. Storage vendors offer multipathing products to support their specific storage products, while software vendors usually develop multipathing products to support several server platforms and storage products.

See also

Your storage or software vendor multipathing documentation for more information about multipathing options for specific platforms and storage products

With Oracle ASM, you can ensure the discovery of a multipath disk by setting the value of the `ASM_DISKSTRING` initialization parameter to a pattern that matches the pseudo devices that represents the multipath disk. When I/O is sent to the pseudo device, the multipath driver intercepts it and provides load balancing to the underlying subpaths.

If Oracle ASM discovers multiple paths to the same disk device, Oracle ASM then raises an error. Because a single disk can appear multiple times in a multipath configuration, you must configure Oracle ASM to discover only the multipath disk.

See also

- [Oracle ASM Disk Discovery](administering-oracle-asm-disk-groups.md) for information about disk discovery
- [My Oracle Support](https://support.oracle.com/) ([https://support.oracle.com](https://support.oracle.com/)) for articles with information about Oracle ASM and Multipathing
- Your platform-specific installation guide for information about configuring multipathing for your system

## Recommendations for Storage Preparation

Recommendations for storage preparation with Oracle ASM are discussed in this topic.

The following are guidelines for preparing storage for use with Oracle ASM:

- Configure a separate disk group for the following:
- Oracle Cluster Registry (OCR) and voting files
	- Grid Infrastructure Management Repository (GIMR) files
		- Database data files
		- Fast recovery area
- The number of LUNs (Oracle ASM disks) for each disk group should be at least equal to four times the number of active I/O paths. For example, if a disk group has two active I/O paths, then minimum of eight LUNs should be used. The LUNs should be of equal size and performance for each disk group.
	An I/O path is a distinct channel or connection between storage presenting LUNs and the server. An *active* I/O path is an I/O path in which the I/O load on a LUN is multiplexed through multipathing software.
- Ensure that all Oracle ASM disks in a disk group have similar storage performance and availability characteristics. In storage configurations with mixed speed drives, such as flash memory and hard disk drives (HDD), I/O performance is constrained by the slowest speed drive.
- Oracle ASM data distribution policy is capacity-based. Ensure that Oracle ASM disks in a disk group have the same capacity to maintain balance.
- Configure a minimum of three failure groups for normal redundancy disk groups and five failure groups for high redundancy disk groups to maintain the necessary number of copies of the Partner Status Table (PST) to ensure robustness with respect to storage hardware failures.
- Create external redundancy disk groups when using high-end storage arrays. High-end storage arrays generally provide hardware RAID protection. Use Oracle ASM mirroring redundancy when not using hardware RAID, or when you need host-based volume management functionality, such as mirroring across storage systems. You can use Oracle ASM mirroring in configurations when mirroring between geographically-separated sites (extended clusters).
- Minimize I/O contention between Oracle ASM disks and other applications by dedicating disks in Oracle ASM disk groups.
- Choose a hardware RAID stripe size that is a power of 2 and less than or equal to the size of the Oracle ASM allocation unit.
- Use the Oracle ASM Filter Driver feature to provide consistent device naming and permission persistency.

See also

- [Creating Disk Groups for a New Oracle Installation](administering-oracle-asm-disk-groups.md) for information about configuring disk groups for a new installation
- The Oracle Cloud Storage page on the Oracle Technology Network website at [https://www.oracle.com/database/technologies/asm/](https://www.oracle.com/database/technologies/asm/) for more information about Oracle ASM
- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=BRADV8183) for information about configuring the fast recovery area
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=ADMIN11103) for information about specifying a fast recovery area
- [Oracle ASM Failure Groups](administering-oracle-asm-disk-groups.md) for information about failure groups
- [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md) for Information about Oracle ASM Filter Driver

## Storage Device Path and Permission Persistence

Before installation, or before configuring new storage devices to use with Oracle ASM, administrators must configure storage device names and ownership to ensure that storage paths and ownership persist after system restarts.

Use Oracle ASM Filter Driver to maintain permissions and manage device paths. On Oracle Solaris, you can also use the Solaris I/O multipathing features to maintain permissions and device paths.

See also

[Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=CWLIN) for your operating system for more information about configuring storage devices for path and permission persistence.