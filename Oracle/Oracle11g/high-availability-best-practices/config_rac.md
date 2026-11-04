---
title: Configuring Oracle Database with Oracle RAC
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/config_rac.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 7 Configuring Oracle Database with Oracle RAC

This chapter contains the following topics:

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD802)

## 7.1 Configuring Oracle Database with Oracle RAC

The best practices discussed in this section apply to Oracle Database 11g with Oracle Real Application Clusters (Oracle RAC). These best practices build on the Oracle Database 11g configuration best practices described in [Chapter 5, "Configuring Oracle Database"](config_db.md) and [Chapter 6, "Configuring Oracle Database with Oracle Clusterware."](config_cw.md) These best practices are identical for the primary and standby databases if they are used with Data Guard in Oracle Database 11g with Oracle RAC and Data Guard—MAA. Some best practices may use your system resources more aggressively to reduce or eliminate downtime. This can, in turn, affect performance service levels, so be sure to assess the impact in a test environment before implementing these practices in a production environment.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/storage.htm#RACAD802)

### 7.1.1 Optimize Instance Recovery Time

Instance recovery is the process of recovering the redo thread from the failed instance. Instance recovery is different from crash recovery, which occurs when all instances accessing a database have failed. Crash recovery is the only type of recovery when an instance fails using a single-instance Oracle Database.

When using Oracle RAC, the SMON process in one surviving instance performs instance recovery of the failed instance.

In both Oracle RAC and single-instance environments, checkpointing is the internal mechanism used to bound Mean Time To Recover (MTTR). Checkpointing is the process of writing dirty buffers from the buffer cache to disk. With more aggressive checkpointing, less redo is required for recovery after a failure. Although the objective is the same, the parameters and metrics used to tune MTTR are different in a single-instance environment versus an Oracle RAC environment.

In a single-instance environment, you can set the `FAST_START_MTTR_TARGET` initialization parameter to the number of seconds the crash recovery should take. Note that crash recovery time includes the time to startup, mount, recover, and open the database.

Oracle provides several ways to help you understand the MTTR target your system is currently achieving and what your potential MTTR target could be, given the I/O capacity.

See Also:

The MAA white paper "Best Practices for Optimizing Availability During Unplanned Outages Using Oracle Clusterware and Oracle Real Application Clusters" for more information from the MAA Best Practices area for Oracle Database at

`http://www.oracle.com/goto/maa`

### 7.1.2 Maximize the Number of Processes Performing Transaction Recovery

The [`FAST_START_PARALLEL_ROLLBACK`](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams091.htm#REFRN10059) parameter determines how many processes are used for transaction recovery, which is done after redo application. Optimizing transaction recovery is important to ensure an efficient workload after an unplanned failure. If the system is not CPU bound, setting this parameter to `HIGH` is a best practice. This causes Oracle to use four times the `CPU_COUNT` (4 X CPU\_COUNT) parallel processes for transaction recovery. The default setting for this parameter is `LOW`, or two times the `CPU_COUNT` (2 X CPU\_COUNT). Set the parameter as follows:

```
ALTER SYSTEM SET FAST_START_PARALLEL_ROLLBACK=HIGH SCOPE=BOTH;
```

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/parallel005.htm#VLDBG1504) for information about Parameters Affecting Resource Consumption for Parallel DML and Parallel DDL

### 7.1.3 Ensure Asynchronous I/O Is Enabled

Using asynchronous I/O is a best practice that is recommended for all Oracle Databases. For more information, see [Section 5.1.7, "Set DISK\_ASYNCH\_IO Initialization Parameter"](config_db.md).

### 7.1.4 Redundant Dedicated Connection Between the Nodes

Use redundant dedicated connections and sufficient bandwidth for public traffic, Oracle RAC interconnects, and I/O.

In Oracle terms, an extended cluster is a two or more node configuration where the nodes are separated in two physical locations. For an extended cluster and for other Oracle RAC configurations, separate dedicated channels on one fibre may be needed, or you can optionally configure Dense Wavelength Division Multiplexing (DWDM) to allow communication between the sites without using repeaters and to allow greater distances, greater than 10 km, between the sites. However, the disadvantage is that DWDM can be prohibitively expensive.

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/preparing.htm#TDPRC123) for more information About Network Hardware Requirements

## 7.2 Configuring Oracle Database with Oracle RAC One Node

Oracle RAC One Node is a single instance of an Oracle Real Application Clusters (Oracle RAC) database that runs on one node in a cluster with an option to failover or migrate to other nodes in the same cluster. This option adds to the flexibility that Oracle offers for database consolidation. You can consolidate many databases into one cluster with minimal overhead while also providing the high availability benefits of failover protection, online rolling patch application, and rolling upgrades for the operating system and Oracle Clusterware.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/onenode.htm#RACAD7894) for more information about Administering Oracle RAC One Node

## 7.3 Configuring Oracle Database with Oracle RAC on Extended Clusters

An Oracle RAC extended cluster is an architecture that provides extremely fast recovery from a site failure and allows for all nodes, at all sites, to actively process transactions as part of single database cluster. An extended cluster provides greater high availability than a local Oracle RAC cluster, but because the sites are typically in the same metropolitan area, this architecture may not fulfill all disaster recovery requirements for your organization.

The best practices discussed in this section apply to Oracle Database 11g with Oracle RAC on extended clusters, and build on the best practices described in Section 7.1, "Configuring Oracle Database with Oracle RAC."

Use the following best practices when configuring an Oracle RAC database for an extended cluster environment:

- Spread the Workload Evenly Across the Sites in the Extended Cluster
- Add a Third Voting Disk to Host the Quorum Disk
- Configure the Nodes to Be Within the Proximity of a Metropolitan Area
- Use Host-Based Storage Mirroring with Oracle ASM Normal or High Redundancy
- Additional Deployment Considerations for Extended Clusters

See Also:

- The white paper about extended clusters on the Oracle Real Application Clusters website at `http://www.oracle.com/technetwork/database/clustering/overview/index.html`
- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/unplanned.htm#HAOVW119) for a high-level overview, benefits, and configuration examples for Oracle RAC

### 7.3.1 Spread the Workload Evenly Across the Sites in the Extended Cluster

A typical Oracle RAC architecture is designed primarily as a scalability and availability solution that resides in a single data center. To build and deploy an Oracle RAC extended cluster, the nodes in the cluster are separated by greater distances. When configuring an Oracle RAC database for an extended cluster environment, you must:

- Configure one set of nodes at Site A and another set of nodes at Site B.
- Spread the cluster workload evenly across both sites to avoid introducing additional contention and latency into the design. For example, avoid client/server application workloads that run across sites, such that the client component is in site A and the server component is in site B.

### 7.3.2 Add a Third Voting Disk to Host the Quorum Disk

Most extended clusters have only two storage systems (one at each site). During normal processing each node writes and reads a disk heartbeat at regular intervals, but if the heartbeat cannot complete, all affected nodes are evicted from the cluster forcing them to restart their processes and retry to acquire access to the shared resources safely as a member. Thus, the site that houses the majority of the voting disks is a potential single point of failure for the entire cluster. For availability reasons, you should add a third site that can act as the arbitrator in case either: one site fails, or a communication failure occurs between the sites.

In some cases, you can also use standard NFS to support a third voting disk on an extended cluster. You can configure the quorum disk on inexpensive, low end, standard NFS mounted device somewhere on the network. Oracle recommends putting the NFS voting disk on a dedicated server which belongs to a production environment.

If you have an extended cluster and do not configure a third site, you must find out which of the two sites is the primary site. Then, if the primary site fails, you must manually restart the secondary site.

Note:

Oracle Clusterware supports NFS, iSCSI, Direct Attached Storage (DAS), Storage Area Network (SAN) storage, and Network Attached Storage (NAS). If your system does not support NFS, use an alternative. For example, on Windows systems you can use iSCSI.

See Also:

For more information, see the Technical Article "Using standard NFS to support a third voting file for extended cluster configurations" at

`http://www.oracle.com/technetwork/database/clustering/overview/index.html`

### 7.3.3 Configure the Nodes to Be Within the Proximity of a Metropolitan Area

Extended clusters provide the highest level of availability for server and site failures when data centers are in close enough proximity to reduce latency and complexity. The preferred distance between sites in an extended cluster is within a metropolitan area. High internode and interstorage latency can have a major effect on performance and throughput. Performance testing is mandatory to assess the impact of latency. In general, distances of 50 km or less are recommended.

Testing has shown the distance (greatest cable stretch) between Oracle RAC cluster nodes generally affects the configuration, as follows:

- Distances less than 10 km can be deployed using normal network cables.
- Distances equal to or more than 10 km require Dense Wavelength Division Multiplexing (DWDM) links.
- Distances from 10 to 50 km require storage area network (SAN) buffer credits to minimize the performance impact due to the distance. Otherwise, the performance degradation due to the distance can be significant.
- For distances greater than 50 km, there are not yet enough proof points to indicate the effect of deployments. More testing is needed to identify what types of workloads could be supported and what the effect of the chosen distance would have on performance.

### 7.3.4 Use Host-Based Storage Mirroring with Oracle ASM Normal or High Redundancy

Use host-based mirroring with Oracle ASM normal or high redundancy configured disk groups so that a storage array failure does not affect the application and database availability.

Oracle recommends host-based mirroring using Oracle ASM to internally mirror across the two storage arrays. Implementing mirroring with Oracle ASM provides an active/active storage environment in which system write I/Os are propagated to both sets of disks, making the disks appear as a single set of disks that is independent of location. Do not use array-based mirroring because only one storage site is active, which makes the architecture vulnerable to this single point of failure and longer recovery times.

The Oracle ASM volume manager provides flexible host-based mirroring redundancy options. You can choose to use external redundancy to defer the mirroring protection function to the hardware RAID storage subsystem. The Oracle ASM normal and high-redundancy options allow two-way and three-way mirroring, respectively.

Note:

Array based mirroring can be used in an Oracle RAC extended cluster. Using this approach has the result that the two mirror sites will be in an active-passive configuration and this will result in a complete outage if one site fails. Service becomes available if the remaining mirror site is brought up. For this reason array based mirroring is not recommended from an HA perspective. To work with two active sites, host based mirroring is recommended.

Beginning with Oracle Database Release 11g, Oracle ASM includes a preferred read capability that ensures that a read I/O accesses the local storage instead of unnecessarily reading from a remote failure group. When you configure Oracle ASM failure groups in extended clusters, you can specify that a particular node reads from a failure group extent that is closest to the node, even if it is a secondary extent. This is especially useful in extended clusters where remote nodes have asymmetric access for performance, thus leading to better usage and lower network loading. Using preferred read failure groups is most useful in extended clusters.

The `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter value is a comma-delimited list of strings that specifies the failure groups that should be preferentially read by the given instance. This parameter is instance specific, and it is generally used only for clustered Oracle ASM instances. It's value can be different on different nodes. For example:

```
diskgroup_name1.failure_group_name1, ...
```

See Also:

- [Section 4.2, "Use Automatic Storage Management (Oracle ASM) to Manage Database Files"](config_storage.md)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG10047) for information about configuring preferred read failure groups with the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter

### 7.3.5 Additional Deployment Considerations for Extended Clusters

Consider the following additional factors when implementing an extended cluster architecture:

- Network, storage, and management costs increase.
- Write performance incurs the overhead of network latency. Test the workload performance to assess impact of the overhead.
- Because this is a single database without Oracle Data Guard, there is no protection from data corruption or data failures.
- The Oracle release, the operating system, and the clusterware used for an extended cluster all factor into the viability of extended clusters.
- When choosing to mirror data between sites:
	- Host-based mirroring requires a clustered logical volume manager to allow active/active mirrors and thus a primary/primary site configuration. Oracle recommends using Oracle ASM as the clustered logical volume manager.
		- Array-based mirroring allows active/passive mirrors and thus a primary/secondary configuration.
- Extended clusters need additional destructive testing, covering
- For full disaster recovery, complement the extended cluster with a remote Data Guard standby database, because this architecture:
	- Maintains an independent physical replica of the primary database
		- Protects against regional disasters
		- Protects against data corruption and other potential failures
		- Provides options for performing rolling database upgrades and patch set upgrades