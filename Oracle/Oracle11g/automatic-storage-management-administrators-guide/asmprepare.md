---
title: Considerations for Oracle ASM Storage
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmprepare.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## 2 Considerations for Oracle ASM Storage

This chapter discusses some points to consider about the storage subsystem before you configure Oracle Automatic Storage Management (Oracle ASM). When preparing your storage to use Oracle ASM, first determine the storage option for your system and then prepare the disk storage for your specific operating system environment.

When configuring your system's storage, you must consider the initial capacity of the system and your plans for future growth. Oracle ASM simplifies the task of accommodating growth. However, your growth plans can affect choices, such as the size of the Oracle ASM disks. You must also consider that I/O performance depends on the interconnect between the storage and host, not just the storage disks. As you scale up the number of nodes in a cluster, you must also scale up the storage subsystem.

This chapter contains the following topics:

## Storage Resources for Disk Groups

You can create an Oracle ASM disk group using one of the following storage resources:

- Disk Partition
	A disk [partition](ostmg_gloss.md) can be the entire disk drive or a section of a disk drive. However, the Oracle ASM disk cannot be in a partition that includes the partition table because the partition table would be overwritten.
- [Logical Unit Number (LUN)](ostmg_gloss.md)
	A LUN is a disk presented to a computer system by a storage array. Oracle recommends that you use hardware RAID functionality to create LUNs. Storage hardware RAID 0+1 or RAID5, and other RAID configurations, can be provided to Oracle ASM as Oracle ASM disks.
- Logical Volume
	A logical [volume](ostmg_gloss.md) is supported in less complicated configurations where a logical volume is mapped to a LUN, or a logical volume uses disks or raw partitions. Logical volume configurations are not recommended by Oracle because they create a duplication of functionality. Oracle also does not recommended using logical [volume manager](ostmg_gloss.md) s for mirroring because Oracle ASM provides mirroring.
- [Network File System (NFS)](ostmg_gloss.md)
	An Oracle ASM disk group can be created from NFS files, including Oracle Direct NFS (dNFS), as well as whole disks, partitions, and LUNs. The NFS files that are provisioned to a disk group may be from multiple NFS servers to provide better load balancing and flexible capacity planning.
	Direct NFS can be used to store data files, but is not supported for Oracle Clusterware files. To install Oracle Real Application Clusters (Oracle RAC) on Windows using Direct NFS, you must also have access to a shared storage method other than NFS for Oracle Clusterware files.
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your operating system for information about Oracle Direct NFS

Notes:

- Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes and Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file systems are currently not supported on disk groups that have been created from NFS or Common Internet File System (CIFS) files. However, Oracle ACFS file systems may be exported as NFS or CIFS file systems to network clients.
- Mounting loopback file systems over Oracle ACFS files is not supported.
- Block or raw devices are not supported by Oracle Universal Installer (OUI) or Database Configuration Assistant (DBCA). However, manually configured raw or block devices are supported by Oracle, but not recommended.

The procedures for preparing storage resources for Oracle ASM are:

1. Identify or create the storage devices for Oracle ASM by identifying all of the storage resource device names that you can use to create an Oracle ASM disk group. For example, on Linux systems without ASMLib, device names are typically presented from the `/dev` directory with the `/dev/` `device_name_identifier` name syntax.
2. Change the ownership and the permissions on storage device resources.
	For example, the following steps are required on Linux systems:
	- Change the user and group ownership of devices, such as `grid:asmadmin`
		For information about Oracle ASM privileges, see ["About Privileges for Oracle ASM"](asminst.md).
		- Change the device permissions to read/write
	Note:
	To ensure that ownership and permission settings are persistent, use ASMLib or `udev` to ensure that the disks do not revert to root ownership when the systems reboot.

After you have configured Oracle ASM, ensure that disk discovery has been configured correctly by setting the `ASM_DISKSTRING` initialization parameter. For information about the `ASM_DISKSTRING` parameter, see ["ASM\_DISKSTRING"](asminst.md).

Note:

Setting the ownership to `oracle:dba` is one example that corresponds to the default settings. A nondefault installation may require different settings. In general, the owner of the disk devices should be the same as the owner of the Oracle binary software. The group ownership should be OSDBA of the Oracle ASM instance, which is defined at installation. For information about Oracle ASM privileges, see ["About Privileges for Oracle ASM"](asminst.md).

For detailed information about preparing disks for an Oracle ASM installation, refer to your platform-specific installation guide for Oracle Database, Oracle Clusterware, and Oracle Real Application Clusters (Oracle RAC).

See Also:

Oracle Exadata documentation for information about preparing Oracle Exadata storage

## Oracle ASM and Multipathing

Multipathing solutions provide failover by using redundant physical path components. These components include adapters, cables, and switches that reside between the server and the storage subsystem. If one or more of these components fails, then applications can still access their data, eliminating a single point of failure with the [Storage Area Network (SAN)](ostmg_gloss.md), Host Bus Adapter, interface cable, or host port on a multiported storage array.

Multipathing is a software technology implemented at the operating system device driver level. Multipathing creates a pseudo device to facilitate the sharing and balancing of I/O operations across all of the available I/O paths. Multipathing also improves system performance by distributing the I/O load across all available paths, providing a higher level of data availability through automatic failover and failback.

Although Oracle ASM is not designed with multipathing functionality, Oracle ASM does operate with multipathing technologies. Multipathing technologies are available from many sources. Storage vendors offer multipathing products to support their specific storage products, while software vendors usually develop multipathing products to support several server platforms and storage products.

See Also:

Your storage or software vendor multipathing documentation for more information about multipathing options for specific platforms and storage products

With Oracle ASM, you can ensure the discovery of a multipath disk by setting the value of the `ASM_DISKSTRING` initialization parameter to a pattern that matches the pseudo devices that represents the multipath disk. When I/O is sent to the pseudo device, the multipath driver intercepts it and provides load balancing to the underlying subpaths.

If Oracle ASM discovers multiple paths to the same disk device, Oracle ASM then raises an error. Because a single disk can appear multiple times in a multipath configuration, you must configure Oracle ASM to discover only the multipath disk.

When using [ASMLib](ostmg_gloss.md) with Oracle ASM on Linux, you can ensure the discovery of the multipath disk by configuring Oracle ASM to scan the multipath disk first or to exclude the single path disks when scanning.

For information about disk discovery, see ["Oracle ASM Disk Discovery"](asmdiskgrps.md).

See Also:

- Articles at [My Oracle Support](https://support.oracle.com/) (`https://support.oracle.com`) for information about Oracle ASM and Multipathing
- Your platform-specific installation guide for information about configuring multipathing for your system

## Recommendations for Storage Preparation

The following are guidelines for preparing storage for use with Oracle ASM:

- Configure two disk groups, one for data and the other for the fast recovery area.
	See Also:
	- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) for information about configuring the fast recovery area
	- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11103) for information about specifying a fast recovery area
- A minimum of four LUNs (Oracle ASM disks) of equal size and performance is recommended for each disk group.
- Ensure that all Oracle ASM disks in a disk group have similar storage performance and availability characteristics. In storage configurations with mixed speed drives, such as 10K and 15K RPM, I/O performance is constrained by the slowest speed drive.
- Oracle ASM data distribution policy is capacity-based. Ensure that Oracle ASM disks in a disk group have the same capacity to maintain balance.
- Create external redundancy disk groups when using high-end storage arrays. High-end storage arrays generally provide hardware RAID protection. Use Oracle ASM mirroring redundancy when not using hardware RAID, or when you need host-based volume management functionality, such as mirroring across storage systems. You can use Oracle ASM mirroring in configurations when mirroring between geographically-separated sites (extended clusters).
- Minimize I/O contention between Oracle ASM disks and other applications by dedicating disks in Oracle ASM disk groups.
- Choose a hardware RAID stripe size that is a power of 2 and less than or equal to the size of the Oracle ASM allocation unit.
- For Linux, use the Oracle ASMLib feature to provide consistent device naming and permission persistency.
	See Also:
	- The Oracle Cloud Storage page on the Oracle Technology Network Web site at `http://www.oracle.com/technetwork/database/cloud-storage/index.html` for more information about Oracle ASM
	- The Oracle ASMLib page on the Oracle Technology Network Web site at `http://www.oracle.com/technetwork/topics/linux/asmlib/index-101839.html` for information about ASMLib