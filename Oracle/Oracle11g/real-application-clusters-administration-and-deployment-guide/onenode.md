---
title: Administering Oracle RAC One Node
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/onenode.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## 4 Administering Oracle RAC One Node

Oracle Real Application Clusters One Node (Oracle RAC One Node) is a single instance of an Oracle Real Application Clusters (Oracle RAC) database that runs on one node in a cluster. This option adds to the flexibility that Oracle offers for database consolidation. You can consolidate many databases into one cluster with minimal overhead while also providing the high availability benefits of failover protection, online rolling patch application, and rolling upgrades for the operating system and Oracle Clusterware.

This chapter includes the following topics:

## Overview of Oracle Real Application Clusters One Node

You can limit the CPU consumption of individual database instances per server within the cluster through Resource Manager Instance Caging and dynamically change this limit if needed. With Oracle RAC One Node, there is no limit to server scalability and if applications grow to require more resources than a single node can supply, then you can easily upgrade your applications online to Oracle RAC. If the node that is running Oracle RAC One Node becomes overloaded, then you can relocate the instance to another node in the cluster using the online database relocation utility with no downtime for application users.

Oracle RAC One Node is supported on all platforms on which Oracle RAC is certified. Similar to Oracle RAC, Oracle RAC One Node is certified on Oracle Virtual Machine (Oracle VM). Using Oracle RAC or Oracle RAC One Node with Oracle VM increases the benefits of Oracle VM with the high availability and scalability of Oracle RAC.

Using Oracle RAC One Node online database relocation, you can relocate the Oracle RAC One Node instance to another server, if the current server is running short on resources or requires maintenance operations, such as operating system patches. You can use the same technique to relocate Oracle RAC One Node instances to high capacity servers to accommodate changes in workload, for example, depending on the resources available in the cluster. In addition, Resource Manager Instance Caging or memory optimization parameters can be set dynamically to further optimize the placement of the Oracle RAC One Node instance on the new server.

Using the Single Client Access Name (SCAN) to connect to the database, clients can locate the service independently of the node on which it is running. Relocating an Oracle RAC One Node instance is therefore mostly transparent to the client, depending on the client connection. Oracle recommends to use either Oracle Fast Application Notification or Transparent Application Failover to minimize the impact of a relocation on the client.

Oracle RAC One Node databases are administered slightly differently from Oracle RAC or noncluster databases. For administrator-managed Oracle RAC One Node databases, you must monitor the candidate node list and make sure a server is always available for failover, if possible. Candidate servers reside in the Generic server pool and the database and its services will fail over to one of those servers.

For policy-managed Oracle RAC One Node databases, you must ensure that the server pools are configured such that a server will be available for the database to fail over to in case its current node becomes unavailable. Also, for policy-managed Oracle RAC One Node databases, the destination node for online database relocation must be located in the database's server pool.

Note:

In order to cover all failure scenarios, you must add at least one dynamic database service (Oracle Clusterware-managed database service) to an Oracle RAC One Node database.

See Also:

Oracle Real Application Clusters Installation Guide for Linux and UNIX for information about installing Oracle RAC One Node databases

## Adding an Oracle RAC One Node Database

Use the `srvctl add database` command to add an Oracle RAC One Node database to your cluster. For example:

```
srvctl add database -c  RACONENODE [-e server_list] [-i instance_name] [-w timeout]
```

Use the `-e` option and the `-i` option when adding an administrator-managed Oracle RAC One Node database.

Using DBCA to create an Oracle RAC One Node database adds the newly created database to the cluster.

See Also:

- `"srvctl add database"` for usage information
- ["Using DBCA in Interactive Mode to Add Database Instances to Target Nodes"](adddelunix.md) for information adding an Oracle RAC One Node database

Each service on an Oracle RAC One Node database is configured by using the same value for the `SERVER_POOLS` attribute as the underlying database. When you add services to an Oracle RAC One Node database, the Server Control Utility (SRVCTL) does not accept any placement information, but instead configures those services using the value of the `SERVER_POOLS` attribute.

Note:

When adding an administrator-managed Oracle RAC One Node database, you can optionally supply an instance prefix with the `-i` `instance_name` option of the `srvctl add database` command. The name of the instance will then be `prefix` `_1`. If you do not specify an instance prefix, then the first 12 characters of the unique name of the database becomes the prefix. The instance name changes to `prefix` `_2` during an online database relocation and reverts back to `prefix` `_1` during a subsequent online database relocation. The same instance name is used on failover.

## Converting Databases

Using SRVCTL, you can convert an Oracle RAC database with one instance to an Oracle RAC One Node database and vice versa.

This section includes the following topics:

- Converting a Database from Oracle RAC to Oracle RAC One Node
- Converting a Database from Oracle RAC One Node to Oracle RAC

### Converting a Database from Oracle RAC to Oracle RAC One Node

You can convert an Oracle RAC database with one instance to an Oracle RAC One Node database using the `srvctl convert database` command, as follows:

```
srvctl convert database -d db_unique_name -c RACONENODE [-i instance_name
-w timeout]
```

See Also:

`"convert"` for more information about the `srvctl convert database` command

Note:

An Oracle RAC database that you want to convert to Oracle RAC One Node must either use Oracle Managed Files (to enable automatic thread allocation) or have at least two redo threads.

Prior to converting an Oracle RAC database to an Oracle RAC One Node database, you must first ensure that the Oracle RAC database has only one instance.

If the Oracle RAC database is administrator managed, then you must change the configuration of all services to set the preferred instance to the instance that you want to keep as an Oracle RAC One Node database after conversion. If any service had a `PRECONNECT TAF` policy, then its TAF policy must be updated to `BASIC` or `NONE` before starting the conversion process. These services must no longer have any available instance.

If the Oracle RAC database is policy managed, then you must change the configuration of all services so that they all use the same server pool before you convert the Oracle RAC database to an Oracle RAC One Node database.

### Converting a Database from Oracle RAC One Node to Oracle RAC

You can convert a database from Oracle RAC One Node to Oracle RAC using the `srvctl convert database` command, as follows:

```
srvctl convert database -d db_unique_name -c RAC [-n node_name]
```

If the database is up and running and you do not specify the node where the database is running, then the command returns an error instructing you to specify the node.

If you are relocating the database you want to convert to Oracle RAC using online database relocation, or an online database relocation has failed, then you must either abort or complete the relocation before you run the `srvctl convert database` command.

See Also:

`"convert"` for more information

Converting an administrator-managed Oracle RAC One Node database to an Oracle RAC database sets all database services so that the single instance is preferred. After you convert the database, you can add instances using DBCA.

Converting a policy-managed Oracle RAC One Node database to an Oracle RAC database sets all database services to UNIFORM cardinality. It also results in reusing the server pool in which the database currently runs. The conversion reconfigures the database to run on all nodes in the server pool. The command does not start any additional instances but running the `srvctl start database` command starts the database on all nodes in the server pool.

## Online Database Relocation

You can relocate an Oracle RAC One Node database to another node while still maintaining service availability using the online database relocation utility. Only during a planned online database relocation is a second instance of an Oracle RAC One Node database created, so that any database sessions can continue while the database is relocated to a new node.

If your Oracle RAC One Node database is administrator managed, then the target node to which you want to relocate the database must be in the candidate list or in the Free server pool. If the target node is in the Free server pool, then the node is added to the candidate list.

Note:

When you relocate a database instance to a target node that is not currently in the candidate server list for the database, you must copy the password file, if configured, to the target node.

When you use password file-based authentication for remote management of Oracle RAC One Node databases without any shared password file, you must have two password files on each node where the database can run: one named `SID_prefix` `_1` and the other named `SID_prefix` `_2`. You must recopy both of these files to all candidate nodes every time you update the password file. This is true for both policy-managed and administrator-managed databases.

Oracle recommends using OS authentication, instead, or using Oracle Clusterware to start and stop the database, and defining users in the data dictionary for other management.

Use the `srvctl relocate database` command to initiate relocation of an Oracle RAC One Node database. For example:

```
srvctl relocate database -d rac1 -n node7
```

See Also:

`"srvctl relocate database"` for more information