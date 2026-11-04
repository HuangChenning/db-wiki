---
title: Oracle Grid Infrastructure for a Cluster Installation Concepts
book: Grid Infrastructure Installation Guide for Linux
doc_id: E41961-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41961/concepts.htm
tags:
  - oracle
  - 11g
  - grid-infrastructure-installation-guide-for-linux
---

## D Oracle Grid Infrastructure for a Cluster Installation Concepts

This appendix explains the reasons for preinstallation tasks that you are asked to perform, and other installation concepts.

This appendix contains the following sections:

## D.1 Understanding Preinstallation Configuration

This section reviews concepts about Oracle Grid Infrastructure for a Cluster preinstallation tasks. It contains the following sections:

- Understanding Oracle Groups and Users
- Understanding the Oracle Base Directory Path
- Understanding Network Addresses
- Understanding Network Time Requirements

### D.1.1 Understanding Oracle Groups and Users

This section contains the following topics:

- Understanding the Oracle Inventory Group
- Understanding the Oracle Inventory Directory

#### D.1.1.1 Understanding the Oracle Inventory Group

You must have a group whose members are given access to write to the Oracle Inventory (`oraInventory`) directory, which is the central inventory record of all Oracle software installations on a server. Members of this group have write privileges to the Oracle central inventory (`oraInventory`) directory, and are also granted permissions for various Oracle Clusterware resources, OCR keys, directories in the Oracle Clusterware home to which DBAs need write access, and other necessary privileges. By default, this group is called `oinstall`. The Oracle Inventory group must be the primary group for Oracle software installation owners.

The `oraInventory` directory contains the following:

- A registry of the Oracle home directories (Oracle Grid Infrastructure and Oracle Database) on the system
- Installation logs and trace files from installations of Oracle software. These files are also copied to the respective Oracle homes for future reference.
- Other metadata inventory information regarding Oracle installations are stored in the individual Oracle home inventory directories, and are separate from the central inventory.

You can configure one group to be the access control group for the Oracle Inventory, for database administrators (OSDBA), and for all other access control groups used by Oracle software for operating system authentication. However, if you use one group to provide operating system authentication for all system privileges, then this group must be the primary group for all users to whom you want to grant administrative system privileges.

Note:

If Oracle software is already installed on the system, then the existing Oracle Inventory group must be the primary group of the operating system user (`oracle` or `grid`) that you use to install Oracle Grid Infrastructure. Refer to "Determining If the Oracle Inventory and Oracle Inventory Group Exists" to identify an existing Oracle Inventory group.

#### D.1.1.2 Understanding the Oracle Inventory Directory

The Oracle Inventory directory (`oraInventory`) is the central inventory location for all Oracle software installed on a server.

The first time you install Oracle software on a system, you are prompted to provide an oraInventory directory path.

When you provide an Oracle base path when prompted during installation, or you have set the environment variable `ORACLE_BASE` for the user performing the Oracle Grid Infrastructure installation, OUI creates the Oracle Inventory directory in the path `ORACLE_BASE/../oraInventory`. For example, if `ORACLE_BASE` is set to `/opt/oracle/11`, then the Oracle Inventory directory is created in the path `/opt/oracle/oraInventory`, so that the central inventory for all installations is outside of the Oracle base for this particular Oracle installation user.

If you neither enter a path nor set `ORACLE_BASE`, then the Oracle Inventory directory is placed in the home directory of the user that is performing the installation. For example:

```
/home/oracle/oraInventory
```

As this placement can cause permission errors during subsequent installations with multiple Oracle software owners, Oracle recommends that you do not accept this option, and instead use an OFA-compliant path.

For new installations, Oracle recommends that you either create an Oracle path in compliance with OFA structure, such as `/u01/app/oraInventory`, that is owned by an Oracle software owner, or you set the Oracle base environment variable to an OFA-compliant value.

If you set an Oracle base variable to a path such as `/u01/app/grid` or `/u01/app/oracle`, then the Oracle Inventory is defaulted to the path `u01/app/oraInventory` using correct permissions to allow all Oracle installation owners to write to this central inventory directory.

By default, the Oracle Inventory directory is not installed under the Oracle base directory for the installation owner. This is because all Oracle software installations share a common Oracle Inventory, so there is only one Oracle Inventory for all users, whereas there is a separate Oracle base for each user.

### D.1.2 Understanding the Oracle Base Directory Path

This section contains information about preparing an Oracle base directory.

#### D.1.2.1 Overview of the Oracle Base directory

During installation, you are prompted to specify an Oracle base location, which is owned by the user performing the installation. You can choose a location with an existing Oracle home, or choose another directory location that does not have the structure for an Oracle base directory.

Using the Oracle base directory path helps to facilitate the organization of Oracle installations, and helps to ensure that installations of multiple databases maintain an Optimal Flexible Architecture (OFA) configuration.

#### D.1.2.2 Understanding Oracle Base and Grid Infrastructure Directories

Even if you do not use the same software owner to install Grid Infrastructure (Oracle Clusterware and Oracle ASM) and Oracle Database, be aware that running the `root.sh` script during the Oracle Grid Infrastructure installation changes ownership of the home directory where clusterware binaries are placed to `root`, and all ancestor directories to the root level (`/`) are also changed to `root`. For this reason, the Oracle Grid Infrastructure for a cluster home cannot be in the same location as other Oracle software.

However, Oracle Grid Infrastructure for a standalone database--Oracle Restart--can be in the same location as other Oracle software.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for more information about Oracle Restart

### D.1.3 Understanding Network Addresses

During installation, you are asked to identify the planned use for each network interface that OUI detects on your cluster node. Identify each interface as a public or private interface, or as an interface that you do not want Oracle Clusterware to use. Public and virtual IP addresses are configured on public interfaces. Private addresses are configured on private interfaces.

Refer to the following sections for detailed information about each address type:

- About the Public IP Address
- About the Private IP Address
- About the Virtual IP Address
- About the Grid Naming Service (GNS) Virtual IP Address
- About the SCAN

#### D.1.3.1 About the Public IP Address

The public IP address is assigned dynamically using DHCP, or defined statically in a DNS or in a hosts file. It uses the public interface (the interface with access available to clients).

#### D.1.3.2 About the Private IP Address

Oracle Clusterware uses interfaces marked as private for internode communication. Each cluster node needs to have an interface that you identify during installation as a private interface. Private interfaces need to have addresses configured for the interface itself, but no additional configuration is required. Oracle Clusterware uses interfaces you identify as private for the cluster interconnect. If you identify multiple interfaces during information for the private network, then Oracle Clusterware configures them with Redundant Interconnect Usage. Any interface that you identify as private must be on a subnet that connects to every node of the cluster. Oracle Clusterware uses all the interfaces you identify for use as private interfaces.

For the private interconnects, because of Cache Fusion and other traffic between nodes, Oracle strongly recommends using a physically separate, private network. If you configure addresses using a DNS, then you should ensure that the private IP addresses are reachable only by the cluster nodes.

After installation, if you modify interconnects on Oracle RAC with the `CLUSTER_INTERCONNECTS` initialization parameter, then you must change it to a private IP address, on a subnet that is not used with a public IP address. Oracle does not support changing the interconnect to an interface using a subnet that you have designated as a public subnet.

You should not use a firewall on the network with the private network IP addresses, as this can block interconnect traffic.

#### D.1.3.3 About the Virtual IP Address

The virtual IP (VIP) address is registered in the GNS, or the DNS. Select an address for your VIP that meets the following requirements:

- The IP address and host name are currently unused (it can be registered in a DNS, but should not be accessible by a `ping` command)
- The VIP is on the same subnet as your public interface

#### D.1.3.4 About the Grid Naming Service (GNS) Virtual IP Address

The GNS virtual IP address is a static IP address configured in the DNS. The DNS delegates queries to the GNS virtual IP address, and the GNS daemon responds to incoming name resolution requests at that address.

Within the subdomain, the GNS uses multicast Domain Name Service (mDNS), included with Oracle Clusterware, to enable the cluster to map host names and IP addresses dynamically as nodes are added and removed from the cluster, without requiring additional host configuration in the DNS.

To enable GNS, you must have your network administrator provide a set of IP addresses for a subdomain assigned to the cluster (for example, `grid.example.com`), and delegate DNS requests for that subdomain to the GNS virtual IP address for the cluster, which GNS will serve. The set of IP addresses is provided to the cluster through DHCP, which must be available on the public network for the cluster.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/intro.htm#CWADD91886) for more information about Grid Naming Service

#### D.1.3.5 About the SCAN

Oracle Database 11g release 2 clients connect to the database using SCANs. The SCAN and its associated IP addresses provide a stable name for clients to use for connections, independent of the nodes that make up the cluster. SCAN addresses, virtual IP addresses, and public IP addresses must all be on the same subnet.

The SCAN is a virtual IP name, similar to the names used for virtual IP addresses, such as `node1-vip`. However, unlike a virtual IP, the SCAN is associated with the entire cluster, rather than an individual node, and associated with multiple IP addresses, not just one address.

The SCAN works by being able to resolve to multiple IP addresses in the cluster handling public client connections. When a client submits a request, the SCAN listener listening on a SCAN IP address and the SCAN port is made available to a client. Because all services on the cluster are registered with the SCAN listener, the SCAN listener replies with the address of the local listener on the least-loaded node where the service is currently being offered. Finally, the client establishes connection to the service through the listener on the node where service is offered. All of these actions take place transparently to the client without any explicit configuration required in the client.

During installation listeners are created. They listen on the SCAN IP addresses provided on nodes for the SCAN IP addresses. Oracle Net Services routes application requests to the least loaded instance providing the service. Because the SCAN addresses resolve to the cluster, rather than to a node address in the cluster, nodes can be added to or removed from the cluster without affecting the SCAN address configuration.

The SCAN should be configured so that it is resolvable either by using Grid Naming Service (GNS) within the cluster, or by using Domain Name Service (DNS) resolution. For high availability and scalability, Oracle recommends that you configure the SCAN name so that it resolves to three IP addresses. At a minimum, the SCAN must resolve to at least one address.

If you specify a GNS domain, then the SCAN name defaults to clustername-scan.GNS\_domain. Otherwise, it defaults to clustername-scan.current\_domain. For example, if you start Oracle Grid Infrastructure installation from the server `node1`, the cluster name is `mycluster`, and the GNS domain is `grid.example.com`, then the SCAN Name is `mycluster-scan.grid.example.com`.

Clients configured to use IP addresses for Oracle Database releases prior to Oracle Database 11g release 2 can continue to use their existing connection addresses; using SCANs is not required. When you upgrade to Oracle Clusterware 11g Release 2 (11.2), the SCAN becomes available, and you should use the SCAN for connections to Oracle Database 11g release 2 or later databases. When an earlier version of Oracle Database is upgraded, it registers with the SCAN listeners, and clients can start using the SCAN to connect to that database. The database registers with the SCAN listener through the remote listener parameter in the init.ora file. The REMOTE\_LISTENER parameter must be set to SCAN:PORT. Do not set it to a TNSNAMES alias with a single address with the SCAN as HOST=SCAN.

The SCAN is optional for most deployments. However, clients using Oracle Database 11g release 2 and later policy-managed databases using server pools should access the database using the SCAN. This is because policy-managed databases can run on different servers at different times, so connecting to a particular node virtual IP address for a policy-managed database is not possible.

### D.1.4 Understanding Network Time Requirements

Oracle Clusterware 11g release 2 (11.2) is automatically configured with Cluster Time Synchronization Service (CTSS). This service provides automatic synchronization of all cluster nodes using the optimal synchronization strategy for the type of cluster you deploy. If you have an existing cluster synchronization service, such as NTP, then it will start in an observer mode. Otherwise, it will start in an active mode to ensure that time is synchronized between cluster nodes. CTSS will not cause compatibility issues.

The CTSS module is installed as a part of Oracle Grid Infrastructure installation. CTSS daemons are started up by the OHAS daemon (`ohasd`), and do not require a command-line interface.

## D.2 Understanding Storage Configuration

Understanding Oracle Automatic Storage Management Cluster File System

About Migrating Existing Oracle ASM Instances

About Converting Standalone Oracle ASM Installations to Clustered Installations

### D.2.1 Understanding Oracle Automatic Storage Management Cluster File System

Oracle Automatic Storage Management has been extended to include a general purpose file system, called Oracle Automatic Storage Management Cluster File System (Oracle ACFS). Oracle ACFS is a new multi-platform, scalable file system, and storage management technology that extends Oracle Automatic Storage Management (Oracle ASM) functionality to support customer files maintained outside of the Oracle Database. Files supported by Oracle ACFS include application binaries and application reports. Other supported files are video, audio, text, images, engineering drawings, and other general-purpose application file data.

### D.2.2 About Migrating Existing Oracle ASM Instances

If you have an Oracle ASM installation from a prior release installed on your server, or in an existing Oracle Clusterware installation, then you can use Oracle Automatic Storage Management Configuration Assistant (ASMCA, located in the path Grid\_home/bin) to upgrade the existing Oracle ASM instance to Oracle ASM 11g Release 2 (11.2), and subsequently configure failure groups, Oracle ASM volumes, and Oracle Automatic Storage Management Cluster File System (Oracle ACFS).

Note:

You must first shut down all database instances and applications on the node with the existing Oracle ASM instance before upgrading it.

During installation, if you chose to use Oracle ASM and ASMCA detects that there is a prior Oracle ASM version installed in another home, then after installing the Oracle ASM 11g Release 2 (11.2) binaries, you can start ASMCA to upgrade the existing Oracle ASM instance. You can then choose to configure an Oracle ACFS deployment by creating Oracle ASM volumes and using the upgraded Oracle ASM to create the Oracle ACFS.

On an existing Oracle Clusterware or Oracle RAC installation, if the prior version of Oracle ASM instances on all nodes is Oracle ASM 11g release 1, then you are provided with the option to perform a rolling upgrade of Oracle ASM instances. If the prior version of Oracle ASM instances on an Oracle RAC installation are from an Oracle ASM release prior to Oracle ASM 11g release 1, then rolling upgrades cannot be performed. Oracle ASM is then upgraded on all nodes to 11g Release 2 (11.2).

### D.2.3 About Converting Standalone Oracle ASM Installations to Clustered Installations

If you have an existing standalone Oracle ASM installations on one or more nodes that are member nodes of the cluster, then OUI proceeds to install Oracle Grid Infrastructure for a cluster.

If you place Oracle Clusterware files (OCR and voting disks) on Oracle ASM, then ASMCA is started at the end of the clusterware installation, and provides prompts for you to migrate and upgrade the Oracle ASM instance on the local node, so that you have an Oracle ASM 11g Release 2 (11.2) installation.

On remote nodes, ASMCA identifies any standalone Oracle ASM instances that are running, and prompts you to shut down those Oracle ASM instances, and any database instances that use them. ASMCA then extends clustered Oracle ASM instances to all nodes in the cluster. However, disk group names on the cluster-enabled Oracle ASM instances must be different from existing standalone disk group names.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm)

## D.3 Understanding Server Pools

The following section provides a short overview of server pools. It contains the following topics:

- Overview of Server Pools and Policy-based Management
- How Server Pools Work
- The Free Server Pool
- The Generic Server Pool

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for information about how to configure and administer server pools

### D.3.1 Overview of Server Pools and Policy-based Management

With Oracle Clusterware 11g release 2 (11.2) and later, resources managed by Oracle Clusterware are contained in logical groups of servers called server pools. Resources are hosted on a shared infrastructure and are contained within server pools. The resources are restricted with respect to their hardware resource (such as CPU and memory) consumption by policies, behaving as if they were deployed in a single-system environment.

You can choose to manage resources dynamically using server pools to provide policy-based management of resources in the cluster, or you can choose to manage resources using the traditional method of physically assigning resources to run on particular nodes.

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrator's list.

The Oracle Grid Infrastructure installation owner has permissions to create and configure server pools, using SRVCTL, Oracle Enterprise Manager Database Control, or Oracle Database Configuration Assistant (DBCA).

Policy-based management:

- Enables dynamic capacity assignment when needed to provide server capacity in accordance with the priorities you set with policies
- Enables allocation of resources by importance, so that applications obtain the required minimum resources, whenever possible, and so that lower priority applications do not take resources from more important applications
- Ensures isolation where necessary, so that you can provide dedicated servers in a cluster for applications and databases

Applications and databases running in server pools do not share resources. Because of this, server pools isolate resources where necessary, but enable dynamic capacity assignments as required. Together with role-separated management, this capability addresses the needs of organizations that have a standardized cluster environments, but allow multiple administrator groups to share the common cluster infrastructure.

### D.3.2 How Server Pools Work

Server pools divide the cluster into groups of servers hosting the same or similar resources. They distribute a uniform workload (a set of Oracle Clusterware resources) over several servers in the cluster. For example, you can restrict Oracle databases to run only in a particular server pool. When you enable role-separated management, you can explicitly grant permission to operating system users to change attributes of certain server pools.

Top-level server pools:

- Logically divide the cluster
- Are always exclusive, meaning that one server can only reside in one particular server pool at a certain point in time

Server pools each have three attributes that they are assigned when they are created:

- MIN\_SIZE: The minimum number of servers the server pool should contain. If the number of servers in a server pool is below the value of this attribute, then Oracle Clusterware automatically moves servers from elsewhere into the server pool until the number of servers reaches the attribute value, or until there are no free servers available from less important pools.
- MAX\_SIZE: The maximum number of servers the server pool may contain.
- IMPORTANCE: A number from 0 to 1000 (0 being least important) that ranks a server pool among all other server pools in a cluster.

When Oracle Clusterware is installed, two server pools are created automatically: Generic and Free. All servers in a new installation are assigned to the Free server pool, initially. Servers move from Free to newly defined server pools automatically. When you upgrade Oracle Clusterware, all nodes are assigned to the Generic server pool, to ensure compatibility with database releases before Oracle Database 11g release 2 (11.2).

### D.3.3 The Free Server Pool

The Free server pool contains servers that are not assigned to any other server pools. The attributes of the Free server pool are restricted, as follows:

- SERVER\_NAMES, MIN\_SIZE, and MAX\_SIZE cannot be edited by the user
- IMPORTANCE and ACL can be edited by the user

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91116)

### D.3.4 The Generic Server Pool

The Generic server pool stores pre-11g release 2 (11.2) databases and administrator-managed databases that have fixed configurations. Additionally, the Generic server pool contains servers that match either of the following:

- Servers that you specified in the HOSTING\_MEMBERS attribute of all resources of the application resource type
- Servers with names you specified in the SERVER\_NAMES attribute of the server pools that list the Generic server pool as a parent server pool

The Generic server pool's attributes are restricted, as follows:

- No one can modify configuration attributes of the Generic server pool (all attributes are read-only)
- When you specify a server name in the HOSTING\_MEMBERS attribute, Oracle Clusterware only allows it if the server is:
	- Online and exists in the Generic server pool
		- Online and exists in the Free server pool, in which case Oracle Clusterware moves the server into the Generic server pool
		- Online and exists in any other server pool and the client is either a CRS Administrator (the user role that controls resource administration for server pools) or is allowed to use the server pool's servers, in which case, the server is moved into the Generic server pool
		- Offline and the client is a CRS Administrator
- When you register a child server pool with the Generic server pool, Oracle Clusterware only allows it if the server names pass the same requirements as previously specified for the resources.
	Servers are initially considered for assignment into the Generic server pool at cluster startup time or when a server is added to the cluster, and only after that to other server pools.

## D.4 Understanding Out-of-Place Upgrade

With an out-of-place upgrade, the installer installs the newer version in a separate Oracle Clusterware home. Both versions of Oracle Clusterware are on each cluster member node, but only one version is active.

Rolling upgrade avoids downtime and ensure continuous availability while the software is upgraded to a new version.

If you have separate Oracle Clusterware homes on each node, then you can perform an out-of-place upgrade on all nodes, or perform an out-of-place rolling upgrade, so that some nodes are running Oracle Clusterware from the earlier version Oracle Clusterware home, and other nodes are running Oracle Clusterware from the new Oracle Clusterware home.

An in-place upgrade of Oracle Clusterware 11g release 2 is not supported.

See Also:

[Appendix F, "How to Upgrade to Oracle Grid Infrastructure 11g Release 2"](procstop.md) for instructions on completing rolling upgrades