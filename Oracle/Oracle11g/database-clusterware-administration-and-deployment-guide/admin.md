---
title: Administering Oracle Clusterware
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## 2 Administering Oracle Clusterware

This chapter describes how to administer Oracle Clusterware and includes the following topics:

## Policy-Based Cluster and Capacity Management

Oracle Clusterware 11g release 2 (11.2) introduces a different method of managing nodes and resources used by a database called policy-based management.

This section contains the following topics:

- Overview of Server Pools and Policy-Based Management
- Server Attributes Assigned by Oracle Clusterware
- Understanding Server Pools
- How Oracle Clusterware Assigns New Servers

### Overview of Server Pools and Policy-Based Management

With Oracle Clusterware 11g release 2 (11.2) and later, [resource](glossary.md) s managed by Oracle Clusterware are contained in logical groups of servers called [server pool](glossary.md) s. Resources are hosted on a shared infrastructure and are contained within server pools. The resources are restricted with respect to their hardware resource (such as CPU and memory) consumption by policies, behaving as if they were deployed in a single-system environment.

You can choose to manage resources dynamically using server pools to provide policy-based management of resources in the cluster, or you can choose to manage resources using the traditional method of physically assigning resources to run on particular nodes.

Policy-based management:

- Enables dynamic capacity assignment when needed to provide server capacity in accordance with the priorities you set with policies
- Enables allocation of resources by importance, so that applications obtain the required minimum resources, whenever possible, and so that lower priority applications do not take resources from more important applications
- Ensures isolation where necessary, so that you can provide dedicated servers in a cluster for applications and databases

Applications and databases running in server pools do not share resources. Because of this, server pools isolate resources where necessary, but enable dynamic capacity assignments as required. Together with role-separated management, this capability addresses the needs of organizations that have standardized cluster environments, but allow multiple administrator groups to share the common cluster infrastructure.

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for more information about resource attributes

Oracle Clusterware efficiently allocates different resources in the cluster. You need only to provide the minimum and maximum number of nodes on which a resource can run, combined with a level of importance for each resource that is running on these nodes.

### Server Attributes Assigned by Oracle Clusterware

Oracle Clusterware assigns each server a set of attributes as soon as you add a server to a cluster. If you remove the server from the cluster, then Oracle Clusterware revokes those settings. Table 2-1 lists and describes server attributes.

Table 2-1 Server Attributes

| Attribute | Description |
| --- | --- |
| ``` NAME ``` | The node name of the server. A server name can contain any platform-supported characters except the exclamation point (!) and the tilde (~). A server name cannot begin with a period, or with ora. This attribute is required. |
| ``` ACTIVE_POOLS ``` | A space-delimited list of the names of the server pools to which a server belongs. Oracle Clusterware manages this list, automatically. |
| ``` STATE ``` | A server can be in one of the following states:  ``` ONLINE ```  The server is a member of the cluster and is available for resource placement.  ``` OFFLINE ```  The server is not currently a member of the cluster. Subsequently, it is not available for resource placement.  ``` JOINING ```  When a server joins a cluster, Oracle Clusterware processes the server to ensure that it is valid for resource placement. Oracle Clusterware also checks the state of resources configured to run on the server. Once the validity of the server and the state of the resources are determined, the server transitions out of this state.  ``` LEAVING ```  When a planned shutdown for a server begins, the state of the server transitions to `LEAVING`, making it unavailable for resource placement.  ``` VISIBLE ```  Servers that have Oracle Clusterware running, but not the Cluster Ready Services daemon (`crsd`), are put into the `VISIBLE` state. This usually indicates an intermittent issue or failure and Oracle Clusterware trying to recover (restart) the daemon. Oracle Clusterware cannot manage resources on servers while the servers are in this state.  ``` RECONFIGURING ```  When servers move between server pools due to server pool reconfiguration, a server is placed into this state if resources that ran on it in the current server pool must be stopped and relocated. This happens because resources running on the server may not be configured to run in the server pool to which the server is moving. As soon as the resources are successfully relocated, the server is put back into the `ONLINE` state.  Use the `crsctl status server` command to obtain server information. |
| ``` STATE_DETAILS ``` | This is a read-only attribute that Oracle Clusterware manages. The attribute provides additional details about the state of a server. Possible additional details about a server state are:  Server state: `ONLINE`:  - `AUTOSTARTING RESOURCES` 	Indicates that the resource autostart procedure (performed when a server reboots or the Oracle Clusterware stack is restarted) is in progress for the server. - `AUTOSTART QUEUED` 	The server is waiting for the resource autostart to commence. Once that happens, the attribute value changes to `AUTOSTARTING RESOURCES`.  Server state: `RECONFIGURING`:  - `STOPPING RESOURCES` 	Resources that are restricted from running in a new server pool are stopping. - `STARTING RESOURCES` 	Resources that can run in a new server pool are starting. - `RECONFIG FAILED` 	One or more resources did not stop and thus the server cannot transition into the `ONLINE` state. At this point, manual intervention is required. You must stop or unregister resources that did not stop. After that, the server automatically transitions into the `ONLINE` state.  Server state: `JOINING`:  - `CHECKING RESOURCES` 	Whenever a server reboots, the Oracle Clusterware stack restarts, or `crsd` on a server restarts, the policy engine must determine the current state of the resources on the server. While that procedure is in progress, this value is returned. |

### Understanding Server Pools

This section contains the following topics:

- How Server Pools Work
- The Free Server Pool
- The Generic Server Pool

#### How Server Pools Work

Server pools divide the cluster into groups of servers hosting the same or similar resources. They distribute a uniform workload (a set of Oracle Clusterware resources) over several servers in the cluster. For example, you can restrict Oracle databases to run only in certain server pools. When you enable role-separated management, you can explicitly grant permission to operating system users to change attributes of certain server pools.

Top-level server pools:

- Logically divide the cluster
- Are always exclusive, meaning that one server can only reside in one particular server pool at a certain point in time

Server pools each have three attributes that they are assigned when they are created:

- `MIN_SIZE`: The minimum number of servers the server pool should contain. If the number of servers in a server pool is below the value of this attribute, then Oracle Clusterware automatically moves servers from elsewhere into the server pool until the number of servers reaches the attribute value.
- `MAX_SIZE`: The maximum number of servers the server pool should contain.
- `IMPORTANCE`: A number from 0 to 1000 (0 being least important) that ranks a server pool among all other server pools in a cluster.
	Table 2-2 lists and describes all server pool attributes.
	Table 2-2 Server Pool Attributes
	| Attribute | Values and Format | Description |
	| --- | --- | --- |
	| ``` ACL ``` | String in the following format:  ``` owner:user:rwx,pgrp:group:rwx,other::r— ``` | Defines the owner of the server pool and which privileges are granted to various operating system users and groups. The server pool owner defines the operating system user of the owner, and which privileges that user is granted.  The value of this optional attribute is populated at the time a server pool is created based on the identity of the process creating the server pool, unless explicitly overridden. The value can subsequently be changed, if such a change is allowed based on the existing privileges of the server pool.  In the string:  - `owner`: The operating system user of the server pool owner, followed by the privileges of the owner - `pgrp`: The operating system group that is the primary group of the owner of the server pool, followed by the privileges of members of the primary group - `other`: Followed by privileges of others - `r`: Read only - `w`: Modify attributes of the pool or delete it - `x`: Assign resources to this pool  By default, the identity of the client that creates the server pool is the `owner`. Also by default, `root`, and the `user` specified in `owner` have full privileges. You can grant required operating system users and operating system groups their privileges by adding the following lines to the `ACL` attribute:  ``` user:username:rwx group:group_name:rwx ``` |
	| ``` ACTIVE_SERVERS ``` | A string of server names in the following format:  ``` server_name1 server_name2 ... ``` | Oracle Clusterware automatically manages this attribute, which contains the space-delimited list of servers that are currently assigned to a server pool. |
	| ``` EXCLUSIVE_POOLS ``` | String | This optional attribute indicates if servers assigned to this server pool are shared with other server pools. A server pool can explicitly state that it is exclusive of any other server pool that has the same value for this attribute. Two or more server pools are mutually exclusive when the sets of servers assigned to them do not have a single server in common. For example, server pools A and B must be exclusive if they both set the value of this attribute to `foo_A_B`.  Top-level server pools are mutually exclusive, by default. |
	| ``` IMPORTANCE ``` | Any integer from 0 to 1000 | Relative importance of the server pool, with `0` denoting the lowest level of importance and `1000`, the highest. This optional attribute is used to determine how to reconfigure the server pools when a node joins or leaves the cluster. The default value is `0`. |
	| ``` MAX_SIZE ``` | Any nonnegative integer or `-1` (no limit) | The maximum number of servers a server pool can contain. This attribute is optional and is set to `-1` (no limit), by default.  Note: A value of `-1` for this attribute spans the entire cluster. |
	| ``` MIN_SIZE ``` | Any nonnegative integer | The minimum size of a server pool. If the number of servers contained in a server pool is below the number you specify in this attribute, then Oracle Clusterware automatically moves servers from other pools into this one until that number is met.  Note: The value of this optional attribute does not set a hard limit. It governs the priority for server assignment whenever the cluster is reconfigured. The default value is `0`. |
	| ``` NAME ``` | String | The name of the server pool, which you must specify when you create the server pool. Server pool names must be unique within the domain of names of user-created entities, such as resources, types, and servers. A server pool name can contain any platform-supported characters except the exclamation point (!) and the tilde (~). A server pool name cannot begin with a period nor with ora. |
	| ``` PARENT_POOLS ``` | A string of space-delimited server pool names in the following format:  ``` sp1 sp2 ... ``` | Use of this attribute makes it possible to create nested server pools. Server pools listed in this attribute are referred to as parent server pools. A server pool included in a parent server pool is referred to as a child server pool. |
	| ``` SERVER_NAMES ``` | A string of space-delimited server names in the following format:  ``` server1 server2 ... ``` | A list of candidate node names that may be associated with a server pool. If this optional attribute is empty, Oracle Clusterware assumes that any server may be assigned to any server pool, to the extent allowed by values of other attributes, such as `PARENT_POOLS`.  The server names identified as candidate node names are not validated to confirm that they are currently active cluster members. Cluster administrators can use this attribute to define servers as candidates that have not yet been added to the cluster. |

You manage server pools that are managing Oracle RAC databases with the Server Control (SRVCTL) utility. Use the Oracle Clusterware Control (CRSCTL) utility to manage all other server pools. Only cluster administrators have permission to create top-level server pools.

When Oracle Clusterware is installed, two server pools are created automatically: Generic and Free. All servers in a new installation are assigned to the Free server pool, initially. Servers move from Free to newly defined server pools automatically. When you upgrade Oracle Clusterware from a previous release, all nodes are assigned to the Generic server pool, to ensure compatibility with database releases before Oracle Database 11g release 2 (11.2).

#### The Free Server Pool

The Free server pool contains servers that are not assigned to any other server pools. The attributes of the Free server pool are restricted, as follows:

- `SERVER_NAMES`, `MIN_SIZE`, and `MAX_SIZE` cannot be edited by the user
- `IMPORTANCE` and `ACL` can be edited by the user

#### The Generic Server Pool

The Generic server pool stores pre-11g release 2 (11.2) Oracle Databases and administrator-managed databases that have fixed configurations. Additionally, the Generic server pool contains servers that match either of the following:

- Servers that you specified in the `HOSTING_MEMBERS` resource attribute of all resources of the `application` resource type
	See Also:
	- ["HOSTING\_MEMBERS"](resatt.md) for more information about this attribute
	- ["Resource Types"](crschp.md) for more information about resource types
- Servers with names you specified in the `SERVER_NAMES` attribute of the server pools that list the Generic server pool as a parent server pool

The Generic server pool's attributes are restricted, as follows:

- No one can modify configuration attributes of the Generic server pool (all attributes are read-only)
- When you specify a server name in the `HOSTING_MEMBERS` resource attribute, Oracle Clusterware only allows it if the server is:
	- Online and exists in the Generic server pool
		- Online and exists in the Free server pool, in which case Oracle Clusterware moves the server into the Generic server pool
		- Online and exists in any other server pool and the client is either a cluster administrator or is allowed to use the server pool's servers, in which case, the server is moved into the Generic server pool
		- Offline and the client is a cluster administrator
- When you register a child server pool with the Generic server pool, Oracle Clusterware only allows it if the server names pass the same requirements as previously specified for the resources.
	Servers are initially considered for assignment into the Generic server pool at cluster startup time or when a server is added to the cluster, and only after that to other server pools.

### How Oracle Clusterware Assigns New Servers

Oracle Clusterware assigns new servers to server pools in the following order:

1. Generic server pool
2. User-created server pool
3. Free server pool

Oracle Clusterware continues to assign servers to server pools until the following conditions are met:

1. Until all server pools are filled in order of importance to their minimum (`MIN_SIZE`).
2. Until all server pools are filled in order of importance to their maximum (`MAX_SIZE`).
3. By default, any servers not placed in a server pool go into the Free server pool.
	You can modify the `IMPORTANCE` attribute for the Free server pool.

When a server joins a cluster, several things occur.

Consider the server pools configured in Table 2-3:

Table 2-3 Sample Server Pool Attributes Configuration

| NAME | IMPORTANCE | MIN\_SIZE | MAX\_SIZE | PARENT\_POOLS | EXCLUSIVE\_POOLS |
| --- | --- | --- | --- | --- | --- |
| ``` sp1 ``` | ``` 1 ``` | ``` 1 ``` | ``` 10 ``` |  |  |
| ``` sp2 ``` | ``` 3 ``` | ``` 1 ``` | ``` 6 ``` |  |  |
| ``` sp3 ``` | ``` 2 ``` | ``` 1 ``` | ``` 2 ``` |  |  |
| ``` sp2_1 ``` | ``` 2 ``` | ``` 1 ``` | ``` 5 ``` | ``` sp2 ``` | ``` S123 ``` |
| ``` sp2_2 ``` | ``` 1 ``` | ``` 1 ``` | ``` 5 ``` | ``` sp2 ``` | ``` S123 ``` |

For example, assume that there are no servers in a cluster; all server pools are empty.

When a server, named `server1`, joins the cluster:

1. Server-to-pool assignment commences.
2. Oracle Clusterware only processes top-level server pools (those that have no parent server pools), first. In this example, the top-level server pools are `sp1`, `sp2`, and `sp3`.
3. Oracle Clusterware lists the server pools in order of `IMPORTANCE`, as follows: `sp2`, `sp3`, `sp1`.
4. Oracle Clusterware assigns `server1` to `sp2` because `sp2` has the highest `IMPORTANCE` value and its `MIN_SIZE` value has not yet been met.
5. Oracle Clusterware processes the remaining two server pools, `sp2_1` and `sp2_2`. The sizes of both server pools are below the value of the `MIN_SIZE` attribute (both server pools are empty and have `MIN_SIZE` values of `1`).
6. Oracle Clusterware lists the two remaining pools in order of `IMPORTANCE`, as follows: `sp2_1`, `sp2_2`.
7. Oracle Clusterware assigns `server1` to `sp2_1` but cannot assign `server1` to `sp2_2` because `sp2_1` is configured to be exclusive with `sp2_2`.

After processing, the cluster configuration appears, as follows

Table 2-4 Post Processing Server Pool Configuration

| Server Pool Name | Assigned Servers |
| --- | --- |
| ``` sp1 ``` |  |
| ``` sp2 ``` | ``` server1 ``` |
| ``` sp3 ``` |  |
| ``` sp2_1 ``` | ``` server1 ``` |
| ``` sp2_2 ``` |  |

#### Servers Moving from Server Pool to Server Pool

If the number of servers in a server pool falls below the value of the `MIN_SIZE` attribute for the server pool (such as when a server fails), based on values you set for the `MIN_SIZE` and `IMPORTANCE` attributes for all server pools, Oracle Clusterware can move servers from other server pools into the server pool whose number of servers has fallen below the value for `MIN_SIZE`. Oracle Clusterware selects servers from other server pools to move into the deficient server pool that meet the following criteria:

- For server pools that have a lower `IMPORTANCE` value than the deficient server pool, Oracle Clusterware can take servers from those server pools even if it means that the number of servers falls below the value for the `MIN_SIZE` attribute.
- For server pools with equal or greater `IMPORTANCE`, Oracle Clusterware only takes servers from those server pools if the number of servers in a server pool is greater than the value of its `MIN_SIZE` attribute.

## Role-Separated Management

This section contains the following topics

- About Role-Separated Management
- Managing CRS Administrators in the Cluster
- Configuring Horizontal Role Separation

### About Role-Separated Management

Role-separated management is a feature you can implement that enables multiple resources to share the same cluster and hardware resources. This is done by setting permissions on server pools or resources, and then using access control lists (ACLs) to provide access. By default, this feature is not enabled during installation. Resource allocation is controlled by a user assigned the [CRS Administrator](glossary.md) role. You can implement role-separated management in one of the following ways:

- Vertical implementation: Access permissions to server pools or resources are granted by assigning ownership of them to different users for each layer in the enterprise architecture, and using ACLs assigned to those users. Oracle ASM provides an even more granular approach using groups. Careful planning is required to enable overlapping tasks.
	See Also:
	[Oracle Grid Infrastructure Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e41961/prelinux.htm#CWLIN205) for more information about using groups
- Horizontal implementation: Access permissions for resources are granted using ACLs assigned to server pools and policy-managed databases or applications.

#### About the CRS Administrator

Caution:

To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

The CRS Administrator is a predefined administrator role in Oracle Clusterware that controls the creation of server pools. Users to whom you grant the CRS Administrator role can grant or revoke access to system resources only for server pools. The CRS Administrator role does not influence administrative rights on the server.

Additionally, the CRS Administrator can create resources with restricted placement, that use the asterisk (`*`) as the value for the `SERVER_POOLS` attribute to control placement, and grant and revoke access to those resources managed by Oracle Clusterware.

The set of users that have the CRS Administrator role is managed by a list of named CRS Administrators within Oracle Clusterware, as opposed to that set of users being members of an operating system group. Sever pool creation enables the CRS Administrator to divide the cluster into groups of servers used by different groups of users in the organization (a horizontal implementation, as described in the preceding section), thereby enabling role-separated management.

By default, after installing Oracle Grid Infrastructure for a cluster, or after an upgrade, all users are CRS Administrators (as denoted by the asterisk (`*`) in the CRS Administrators list), assuming all users sharing the same infrastructure are equally privileged to manage the cluster. This default configuration allows any named operating system user to create server pools within Oracle Clusterware.

Restricting CRS Administrator privileges to the Grid user and `root` can prevent subsequently created policy-managed databases from being automatically created in newly created server pools. If you enable role-separated management, then a CRS Administrator must create the required server pools in advance.

The user (Grid user) that installed Oracle Clusterware in the Grid Infrastructure home (Grid home) and the system superuser (`root` on Linux and UNIX, or Administrator on Windows) are permanent CRS Administrators, and only these two users can add or remove users from the CRS Administrators list, enabling role-separated management.

If the cluster is shared by various users, then the CRS Administrator can restrict access to certain server pools and, consequently, to certain hardware resources to specific users in the cluster. The permissions are stored for each server pool in the `ACL` attribute, described in Table 2-2.

### Managing CRS Administrators in the Cluster

Use the following commands to manage CRS Administrators in the cluster:

- To query the list of users that are CRS Administrators:
	```
	$ crsctl query crs administrator
	```
- To enable role-separated management and grant privileges to non-permanent CRS Administrators, you must add specific users to the CRS Administrators list. As a permanent CRS Administrator, run the following command:
	```
	# crsctl add crs administrator -u user_name
	```
	The default asterisk (`*`) value is replaced by the user or users you add using this command.
- To remove specific users from the group of CRS Administrators:
	```
	# crsctl delete crs administrator -u user_name
	```
- To make all users CRS Administrators, add the asterisk (`*`) value back to the list, as follows:
	```
	# crsctl add crs administrator -u "*"
	```
	The asterisk (`*`) value must be enclosed in double quotation marks (`""`). This value replaces any previously specified users in the CRS Administrators list.

### Configuring Horizontal Role Separation

Use the `crsctl setperm` command to configure horizontal role separation using ACLs that are assigned to server pools, resources, or both. The CRSCTL utility is located in the path `Grid_home` `/bin`, where `Grid_home` is the Oracle Grid Infrastructure home.

The command uses the following syntax, where you can choose to set permissions on either a resource, a resource type, or a server pool:

```
crsctl setperm {resource | type | serverpool} {-u acl_string | 
-x acl_string | -o user_name | -g group_name}
```

The flag options are:

- `-u`: Update the entity ACL
- `-x`: Delete the entity ACL
- `-o`: Change the entity owner
- `-g`: Change the entity primary group

The ACL strings are:

```
{ user:user_name[:readPermwritePermexecPerm] |
     group:group_name[:readPermwritePermexecPerm] |
     other[::readPermwritePermexecPerm] }
```

where:

- `user`: Designates the user ACL (access permissions granted to the designated user)
- `group`: Designates the group ACL (permissions granted to the designated group members)
- `other`: Designates the other ACL (access granted to users or groups not granted particular access permissions)
- `readperm`: Location of the read permission (`r` grants permission and " `-` " forbids permission)
- `writeperm`: Location of the write permission (`w` grants permission and " `-` " forbids permission)
- `execperm`: Location of the execute permission (`x` grants permission, and " `-` " forbids permission)

For example, as the CRS Administrator, you can set permissions on a database server pool called `testadmin` for the `oracle` user and the `oinstall` group, where only the CRS Administrator (owner) has read, write, and execute privileges, and the user, as well as the members of the `oinstall` group, have only read and execute privileges. All other users outside of the group have no access. The following command, run as the CRS Administrator, shows how this is done:

```
# crsctl setperm serverpool ora.testadmin -u user:oracle:r-x,group:oinstall:r-x,
  other::---
```

Note:

The preceding example is an explicitly granted exception of using a CRSCTL command on an Oracle (`ora.*`) resource (the `ora.testadmin` server pool) for the purpose of enabling horizontal role separation.

## Configuring Oracle Grid Infrastructure

After performing a software-only installation of the Oracle Grid Infrastructure, you can configure the software using Configuration Wizard. This wizard assists you with editing the `crsconfig_params` configuration file. Similar to the Oracle Grid Infrastructure installer, the Configuration Wizard performs various validations of the Grid home and inputs before and after you run through the wizard.

Using the Configuration Wizard, you can configure a new Grid Infrastructure on one or more nodes, or configure an upgraded Grid Infrastructure. You can also run the Configuration Wizard in silent mode.

Notes:

- Before running the Configuration Wizard, ensure that the Grid Infrastructure home is current, with all necessary patches applied.
- To launch the Configuration Wizard in the following procedures:
	On Linux and UNIX, run the following command:
	```
	Oracle_home/crs/config/config.sh
	```
	On Windows, run the following command:
	```
	Oracle_home\crs\config\config.bat
	```

This section includes the following topics:

- Configuring a Single Node
- Configuring Multiple Nodes
- Upgrading Grid Infrastructure
- Running the Configuration Wizard in Silent Mode

### Configuring a Single Node

To use the Configuration Wizard to configure a single node:

1. Start the Configuration Wizard, as follows:
	```
	$ Oracle_home/crs/config/config.sh
	```
2. On the Select Installation Option page, select Configure Grid Infrastructure for a Cluster.
3. On the Cluster Node Information page, select only the local node and corresponding VIP name.
4. Continue adding your information on the remaining wizard pages.
5. Review your inputs on the Summary page and click Finish.
6. Run the `root.sh` script as instructed by the Configuration Wizard.

### Configuring Multiple Nodes

To use the Configuration Wizard to configure multiple nodes:

1. Start the Configuration Wizard, as follows:
	```
	$ Oracle_home/crs/config/config.sh
	```
2. On the Select Installation Option page, select Configure Grid Infrastructure for a Cluster.
3. On the Cluster Node Information page, select the nodes you want to configure and their corresponding VIP names. The Configuration Wizard validates the nodes you select to ensure that they are ready.
4. Continue adding your information on the remaining wizard pages.
5. Review your inputs on the Summary page and click Finish.
6. Run the `root.sh` script as instructed by the Configuration Wizard.

### Upgrading Grid Infrastructure

To use the Configuration Wizard to upgrade the Grid Infrastructure:

1. Start the Configuration Wizard, as follows:
	```
	$ Oracle_home/crs/config/config.sh
	```
2. On the Select Installation Option page, select Upgrade Grid Infrastructure.
3. On the Grid Infrastructure Node Selection page, select the nodes you want to upgrade.
4. Continue adding your information on the remaining wizard pages.
5. Review your inputs on the Summary page and click Finish.
6. Run the `rootupgrade.sh` script as instructed by the Configuration Wizard.

### Running the Configuration Wizard in Silent Mode

To use the Configuration Wizard in silent mode to configure or upgrade nodes, start the Configuration Wizard from the command line with `-silent -responseFile` `file_name`. The wizard validates the response file and proceeds with the configuration. If any of the inputs in the response file are found to be invalid, then the Configuration Wizard displays an error and exits. Run the `root` and `configToolAllCommands` scripts as prompted.

## Configuring IPMI for Failure Isolation

This section contains the following topics:

- About Using IPMI for Failure Isolation
- Configuring Server Hardware for IPMI
- Postinstallation Configuration of IPMI-based Failure Isolation Using CRSCTL

### About Using IPMI for Failure Isolation

Failure isolation is a process by which a failed node is isolated from the rest of the cluster to prevent the failed node from corrupting data. The ideal fencing involves an external mechanism capable of restarting a problem node without cooperation either from Oracle Clusterware or from the operating system running on that node. To provide this capability, Oracle Clusterware 11g release 2 (11.2) supports the Intelligent Management Platform Interface specification (IPMI) (also known as Baseboard Management Controller (BMC)), an industry-standard management protocol.

Typically, you configure failure isolation using IPMI during Grid Infrastructure installation, when you are provided with the option of configuring IPMI from the Failure Isolation Support screen. If you do not configure IPMI during installation, then you can configure it after installation using the Oracle Clusterware Control utility (CRSCTL), as described in "Postinstallation Configuration of IPMI-based Failure Isolation Using CRSCTL".

To use IPMI for failure isolation, each cluster member node must be equipped with an IPMI device running firmware compatible with IPMI version 1.5, which supports IPMI over a local area network (LAN). During database operation, failure isolation is accomplished by communication from the evicting Cluster Synchronization Services daemon to the failed node's IPMI device over the LAN. The IPMI-over-LAN protocol is carried over an authenticated session protected by a user name and password, which are obtained from the administrator during installation.

In order to support dynamic IP address assignment for IPMI using DHCP, the Cluster Synchronization Services daemon requires direct communication with the local IPMI device during Cluster Synchronization Services startup to obtain the IP address of the IPMI device. (This is not true for HP-UX and Solaris platforms, however, which require that the IPMI device be assigned a static IP address.) This is accomplished using an IPMI probe command (OSD), which communicates with the IPMI device through an IPMI driver, which you must install on each cluster system.

If you assign a static IP address to the IPMI device, then the IPMI driver is not strictly required by the Cluster Synchronization Services daemon. The driver is required, however, to use `ipmitool` or `ipmiutil` to configure the IPMI device but you can also do this with management consoles on some platforms.

### Configuring Server Hardware for IPMI

Install and enable the IPMI driver, and configure the IPMI device, as described in the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform.

### Postinstallation Configuration of IPMI-based Failure Isolation Using CRSCTL

This section contains the following topics:

- IPMI Postinstallation Configuration with Oracle Clusterware
- Modifying IPMI Configuration Using CRSCTL
- Removing IPMI Configuration Using CRSCTL

#### IPMI Postinstallation Configuration with Oracle Clusterware

When you install IPMI during Oracle Clusterware installation, you configure failure isolation in two phases. Before you start the installation, you install and enable the IPMI driver in the server operating system, and configure the IPMI hardware on each node (IP address mode, admin credentials, and so on), as described in [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN). When you install Oracle Clusterware, the installer collects the IPMI administrator user ID and password, and stores them in an Oracle Wallet in node-local storage, in OLR.

After you complete the server configuration, complete the following procedure on each cluster node to register IPMI administrators and passwords on the nodes.

Note:

If IPMI is configured to obtain its IP address using DHCP, it may be necessary to reset IPMI or restart the node to cause it to obtain an address.
1. Start Oracle Clusterware, which allows it to obtain the current IP address from IPMI. This confirms the ability of the clusterware to communicate with IPMI, which is necessary at startup.
	If Oracle Clusterware was running before IPMI was configured, you can shut Oracle Clusterware down and restart it. Alternatively, you can use the IPMI management utility to obtain the IPMI IP address and then use CRSCTL to store the IP address in OLR by running a command similar to the following:
	```
	crsctl set css ipmiaddr 192.168.10.45
	```
2. Use CRSCTL to store the previously established user ID and password for the resident IPMI in OLR by running the `crsctl set css ipmiadmin` command, and supplying password at the prompt. For example:
	```
	crsctl set css ipmiadmin administrator_name
	IPMI BMC password: password
	```
	This command validates the supplied credentials and fails if another cluster node cannot access the local IPMI using them.
	After you complete hardware and operating system configuration, and register the IPMI administrator on Oracle Clusterware, IPMI-based failure isolation should be fully functional.

#### Modifying IPMI Configuration Using CRSCTL

To modify an existing IPMI-based failure isolation configuration (for example to change IPMI passwords, or to configure IPMI for failure isolation in an existing installation), use CRSCTL with the IPMI configuration tool appropriate to your platform. For example, to change the administrator password for IPMI, you must first modify the IMPI configuration as described in [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN), and then use CRSCTL to change the password in OLR.

The configuration data needed by Oracle Clusterware for IPMI is kept in an Oracle Wallet in OCR. Because the configuration information is kept in a secure store, it must be written by the Oracle Clusterware installation owner account (the Grid user), so you must log in as that installation user.

Use the following procedure to modify an existing IPMI configuration:

1. Enter the `crsctl set css ipmiadmin` `administrator_name` command. For example, with the user `IPMIadm`:
	```
	crsctl set css ipmiadmin IPMIadm
	```
	Provide the administrator password. Oracle Clusterware stores the administrator name and password for the local IPMI in OLR.
	After storing the new credentials, Oracle Clusterware can retrieve the new credentials and distribute them as required.
2. Enter the `crsctl set css ipmiaddr` `bmc_ip_address` command. For example:
	```
	crsctl set css ipmiaddr 192.0.2.244
	```
	This command stores the new IPMI IP address of the local IPMI in OLR, After storing the IP address, Oracle Clusterware can retrieve the new configuration and distribute it as required.
3. Enter the `crsctl get css ipmiaddr` command. For example:
	```
	crsctl get css ipmiaddr
	```
	This command retrieves the IP address for the local IPMI from OLR and displays it on the console.
4. Remove the IPMI configuration information for the local IPMI from OLR and delete the registry entry, as follows:
	```
	crsctl unset css ipmiconfig
	```

See Also:

["Oracle RAC Environment CRSCTL Commands"](crsref.md) for descriptions of these CRSCTL commands

#### Removing IPMI Configuration Using CRSCTL

You can remove an IPMI configuration from a cluster using CRSCTL if you want to stop using IPMI completely or if IPMI was initially configured by someone other than the user that installed Oracle Clusterware. If the latter is true, then Oracle Clusterware cannot access the IPMI configuration data and IPMI is not usable by the Oracle Clusterware software, and you must reconfigure IPMI as the user that installed Oracle Clusterware.

To completely remove IPMI, perform the following steps. To reconfigure IPMI as the user that installed Oracle Clusterware, perform steps [^3] and [^4], then repeat steps [^1] and [^2] in "Modifying IPMI Configuration Using CRSCTL".

1. Disable the IPMI driver and eliminate the boot-time installation, as follows:
	```
	/sbin/modprobe –r
	```
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform for more information about the IPMI driver
2. Disable IPMI-over-LAN for the local IPMI using either `ipmitool` or `ipmiutil`, to prevent access over the LAN or change the IPMI administrator user ID and password.
3. Ensure that Oracle Clusterware is running and then use CRSCTL to remove the IPMI configuration data from OLR by running the following command:
	```
	crsctl unset css ipmiconfig
	```
4. Restart Oracle Clusterware so that it runs without the IPMI configuration by running the following commands as `root`:
	```
	# crsctl stop crs
	# crsctl start crs
	```

## Cluster Time Management

The Cluster Time Synchronization Service (CTSS) is installed as part of Oracle Clusterware and runs in observer mode if it detects a time synchronization service or a time synchronization service configuration, valid or broken, on the system.If CTSS detects that there is no time synchronization service or time synchronization service configuration on any node in the cluster, then CTSS goes into active mode and takes over time management for the cluster.

When nodes join the cluster, if CTSS is in active mode, then it compares the time on those nodes to a reference clock located on one node in the cluster. If there is a discrepancy between the two times and the discrepancy is within a certain stepping limit, then CTSS performs step time synchronization, which is to step the time of the nodes joining the cluster to synchronize them with the reference.

When Oracle Clusterware starts, if CTSS is running in active mode and the time discrepancy is outside the stepping limit (the limit is 24 hours), then CTSS generates an alert in the alert log, exits, and Oracle Clusterware startup fails. You must manually adjust the time of the nodes joining the cluster to synchronize with the cluster, after which Oracle Clusterware can start and CTSS can manage the time for the nodes.

Clocks on the nodes in the cluster become desynchronized with the reference clock (a time CTSS uses as a basis and is on the first node started in the cluster) periodically for various reasons. When this happens, CTSS performs slew time synchronization, which is to speed up or slow down the system time on the nodes until they are synchronized with the reference system time. In this time synchronization method, CTSS does not adjust time backward, which guarantees monotonic increase of the system time.

When performing slew time synchronization, CTSS never runs time backward to synchronize with the reference clock. CTSS periodically writes alerts to the alert log containing information about how often it adjusts time on nodes to keep them synchronized with the reference clock.

To activate CTSS in your cluster, you must stop and deconfigure the vendor time synchronization service on all nodes in the cluster. CTSS detects when this happens and assumes time management for the cluster.

For example, to deconfigure NTP, you must remove or rename the `ntp.conf` file.

Note:

In Windows, CTSS does not check whether the `ntp.conf` file exists, rather, it only detects whether there is a time synchronization service.

Similarly, if you want to deactivate CTSS in your cluster, then do the following:

1. Configure the vendor time synchronization service on all nodes in the cluster. CTSS detects this change and reverts back to observer mode.
2. Use the `crsctl check ctss` command to ensure that CTSS is operating in observer mode.
3. Start the vendor time synchronization service on all nodes in the cluster.
4. Use the `cluvfy comp clocksync -n all` command to verify that the vendor time synchronization service is operating.

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for information about configuring NTP for Oracle Clusterware, or disabling it to use CTSS

## Changing Network Addresses on Manually Configured Networks

This section contains the following topics:

- Understanding When You Must Configure Network Addresses
- Understanding SCAN Addresses and Client Service Connections
- Changing the Virtual IP Addresses
- Changing Oracle Clusterware Private Network Configuration

### Understanding When You Must Configure Network Addresses

An Oracle Clusterware configuration requires at least two interfaces:

- A public network interface, on which users and application servers connect to access data on the database server
- A private network interface for internode communication.

If you use Grid Naming Service and DHCP to manage your network connections, then you may not need to configure address information on the cluster. Using GNS allows public Virtual Internet Protocol (VIP) addresses to be dynamic, DHCP-provided addresses. Clients submit name resolution requests to your network's Domain Name Service (DNS), which forwards the requests to the grid naming service (GNS), managed within the cluster. GNS then resolves these requests to nodes in the cluster.

If you do not use GNS, and instead configure networks manually, then public VIP addresses must be statically configured in the DNS, VIPs must be statically configured in the DNS and hosts file, and private IP addresses require static configuration.

### Understanding SCAN Addresses and Client Service Connections

Public network addresses are used to provide services to clients. If your clients are connecting to the Single Client Access Name (SCAN) addresses, then you may need to change public and virtual IP addresses as you add or remove nodes from the cluster, but you do not need to update clients with new cluster addresses.

SCANs function like a cluster alias. However, SCANs are resolved on any node in the cluster, so unlike a VIP address for a node, clients connecting to the SCAN no longer require updated VIP addresses as nodes are added to or removed from the cluster. Because the SCAN addresses resolve to the cluster, rather than to a node address in the cluster, nodes can be added to or removed from the cluster without affecting the SCAN address configuration.

The SCAN is a fully qualified name (host name+domain) that is configured to resolve to all the addresses allocated for the SCAN. The addresses resolve using Round Robin DNS either on the DNS server, or within the cluster in a GNS configuration. SCAN listeners can run on any node in the cluster. SCANs provide location independence for the databases, so that client configuration does not have to depend on which nodes run a particular database.

Oracle Database 11g release 2 (11.2) and later instances only register with SCAN listeners as remote listeners. Upgraded databases register with SCAN listeners as remote listeners, and also continue to register with all node listeners.

Note:

Because of the Oracle Clusterware installation requirement that you provide a SCAN name during installation, if you resolved at least one IP address using the server `/etc/hosts` file to bypass the installation requirement but you do not have the infrastructure required for SCAN, then, after the installation, you can ignore the SCAN and connect to the databases in the cluster using VIPs.

Oracle does not support removing the SCAN address.

### Changing the Virtual IP Addresses

Clients configured to use public VIP addresses for Oracle Database releases before Oracle Database 11g release 2 (11.2) can continue to use their existing connection addresses. Oracle recommends that you configure clients to use SCANs, but it is not required that you use SCANs. When an earlier version of Oracle Database is upgraded, it is registered with the SCAN, and clients can start using the SCAN to connect to that database, or continue to use VIP addresses for connections.

If you continue to use VIP addresses for client connections, you can modify the VIP address while Oracle Database and Oracle ASM continue to run. However, you must stop services while you modify the address. When you restart the VIP address, services are also restarted on the node.

This procedure cannot be used to change a static public subnet to use DHCP. Only the `srvctl add network -S` command creates a DHCP network.

Note:

The following instructions describe how to change only a VIP address, and assume that the host name associated with the VIP address does not change. Note that you do not need to update VIP addresses manually if you are using GNS, and VIPs are assigned using DHCP.

If you are changing only the VIP address, then update the DNS and the client hosts files. Also, update the server hosts files, if those are used for VIP addresses.

Perform the following steps to change a VIP address:

1. Stop all services running on the node whose VIP address you want to change using the following command syntax, where `database_name` is the name of the database, `service_name_list` is a list of the services you want to stop, and `my_node` is the name of the node whose VIP address you want to change:
	```
	srvctl stop service -d database_name  -s service_name_list -n my_node
	```
	This example specifies the database name (`grid`) using the `-d` option and specifies the services (`sales,oltp`) on the appropriate node (`mynode`).
	```
	$ srvctl stop service -d grid -s sales,oltp -n mynode
	```
2. Confirm the current IP address for the VIP address by running the `srvctl config vip` command. This command displays the current VIP address bound to one of the network interfaces. The following example displays the configured VIP address:
	```
	$ srvctl config vip -n stbdp03
	VIP exists.:stbdp03
	VIP exists.: /stbdp03-vip/192.168.2.20/255.255.255.0/eth0
	```
3. Stop the VIP resource using the `srvctl stop vip` command:
	```
	$ srvctl stop vip -n mynode
	```
4. Verify that the VIP resource is no longer running by running the `ifconfig -a` command on Linux and UNIX systems (or issue the `ipconfig /all` command on Windows systems), and confirm that the interface (in the example it was `eth0:1`) is no longer listed in the output.
5. Make any changes necessary to the `/etc/hosts` files on all nodes on Linux and UNIX systems, or the `%windir%\system32\drivers\etc\hosts` file on Windows systems, and make any necessary DNS changes to associate the new IP address with the old host name.
6. To use a different subnet or NIC for the default network before you change any VIP resource, you must use the `srvctl modify network -S` `subnet` `/` `netmask` `/` `interface` command as `root` to change the network resource, where `subnet` is the new subnet address, `netmask` is the new netmask, and `interface` is the new interface. After you change the subnet, then you must change each node's VIP to an IP address on the new subnet, as described in the next step.
7. Modify the node applications and provide the new VIP address using the following `srvctl modify nodeapps` syntax:
	```
	$ srvctl modify nodeapps -n node_name -A new_vip_address
	```
	The command includes the following flags and values:
	- `-n` `node_name` is the node name
		- `-A` `new_vip_address` is the node-level VIP address: `name` | `ip` `/` `netmask` `/` `[``if1` `[|` `if2` `|...]]`
		For example, issue the following command as the `root` user:
		```
		srvctl modify nodeapps -n mynode -A 192.168.2.125/255.255.255.0/eth0
		```
		Attempting to issue this command as the installation owner account may result in an error. For example, if the installation owner is `oracle`, then you may see the error `PRCN-2018: Current user oracle is not a privileged user`.To avoid the error, run the command as the `root` or system administrator account.
8. Start the node VIP by running the `srvctl start vip` command:
	```
	$ srvctl start vip -n node_name
	```
	The following command example starts the VIP on the node named `mynode`:
	```
	$ srvctl start vip -n mynode
	```
9. Repeat the steps for each node in the cluster.
	Because the SRVCTL utility is a clusterwide management tool, you can accomplish these tasks for any specific node from any node in the cluster, without logging in to each of the cluster nodes.
10. Run the following command to verify node connectivity between all of the nodes for which your cluster is configured. This command discovers all of the network interfaces available on the cluster nodes and verifies the connectivity between all of the nodes by way of the discovered interfaces. This command also lists all of the interfaces available on the nodes which are suitable for use as VIP addresses.
	```
	$ cluvfy comp nodecon -n all -verbose
	```

### Changing Oracle Clusterware Private Network Configuration

This section contains the following topics:

- About Private Networks and Network Interfaces
- Redundant Interconnect Usage
- Consequences of Changing Interface Names Using OIFCFG
- Changing a Network Interface

#### About Private Networks and Network Interfaces

Oracle Clusterware requires that each node is connected through a private network (in addition to the public network). The private network connection is referred to as the cluster interconnect. Table 2-5 describes how the network interface card (NIC) and the private IP address are stored.

Oracle only supports clusters in which all of the nodes use the same network interface connected to the same subnet (defined as a global interface with the `oifcfg` command). You cannot use different network interfaces for each node (node-specific interfaces). Refer to [Appendix D, "Oracle Interface Configuration Tool (OIFCFG) Command Reference"](oifcfg.md) for more information about global and node-specific interfaces.

Table 2-5 Storage for the Network Interface, Private IP Address, and Private Host Name

| Entity | Stored In... | Comments |
| --- | --- | --- |
| Network interface name | Operating system  For example: `eth1` | You can use wildcards when specifying network interface names.  For example: `eth*` |
| Private network Interfaces | Oracle Clusterware, in the Grid Plug and Play (GPnP) Profile | Configure an interface for use as a private interface during installation by marking the interface as Private, or use the `oifcfg setif` command to designate an interface as a private interface.  See Also: ["OIFCFG Commands"](oifcfg.md) for more information about the `oifcfg setif` command |

#### Redundant Interconnect Usage

You can define multiple interfaces for Redundant Interconnect Usage by classifying the interfaces as private either during installation or after installation using the `oifcfg setif` command. When you do, Oracle Clusterware creates from one to four (depending on the number of interfaces you define) highly available IP (HAIP) addresses, which Oracle Database and Oracle ASM instances use to ensure highly available and load balanced communications.

The Oracle software (including Oracle RAC, Oracle ASM, and Oracle ACFS, all 11g release 2 (11.2.0.2), or later), by default, uses these HAIP addresses for all of its traffic, allowing for load balancing across the provided set of cluster interconnect interfaces. If one of the defined cluster interconnect interfaces fails or becomes non-communicative, then Oracle Clusterware transparently moves the corresponding HAIP address to one of the remaining functional interfaces.

Note:

Oracle Clusterware uses at most four interfaces at any given point, regardless of the number of interfaces defined. If one of the interfaces fails, then the HAIP address moves to another one of the configured interfaces in the defined set.

When there is only a single HAIP address and multiple interfaces from which to select, the interface to which the HAIP address moves is no longer the original interface upon which it was configured. Oracle Clusterware selects the interface with the lowest numerical subnet to which to add the HAIP address.

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform for information about defining interfaces

#### Consequences of Changing Interface Names Using OIFCFG

The consequences of changing interface names depend on which name you are changing, and whether you are also changing the IP address. In cases where you are only changing the interface names, the consequences are minor. If you change the name for the public interface that is stored in OCR, then you also must modify the node applications for the cluster. Therefore, you must stop the node applications for this change to take effect.

See Also:

My Oracle Support (formerly Oracle) note 276434.1 for more details about changing the node applications to use a new public interface name, available at the following URL:
```
https://metalink.oracle.com
```

#### Changing a Network Interface

You can change a network interface and its associated subnet address using the following procedure. You must perform this change on all nodes in the cluster.

This procedure changes the network interface and IP address on each node in the cluster used previously by Oracle Clusterware and Oracle Database.

Caution:

The interface that the Oracle RAC (RDBMS) interconnect uses must be the same interface that Oracle Clusterware uses with the host name. Do not configure the private interconnect for Oracle RAC on a separate interface that is not monitored by Oracle Clusterware.
1. Ensure that Oracle Clusterware is running on all of the cluster nodes by running the following command:
	```
	$ olsnodes -s
	```
	The command returns output similar to the following, showing that Oracle Clusterware is running on all of the nodes in the cluster:
	```
	./olsnodes -s
	myclustera Active
	myclusterc Active
	myclusterb Active
	```
2. Ensure that the replacement interface is configured and operational in the operating system on all of the nodes. Use the `ifconfig` command (or `ipconfig` on Windows) for your platform. For example, on Linux, use:
	```
	$ /sbin/ifconfig..
	```
3. Add the new interface to the cluster as follows, providing the name of the new interface and the subnet address, using the following command:
	```
	$ oifcfg setif -global if_name/subnet:cluster_interconnect
	```
	You can use wildcards with the interface name. For example, `oifcfg setif -global "eth*/192.168.0.0:cluster_interconnect` is valid syntax. However, be careful to avoid ambiguity with other addresses or masks used with other cluster interfaces. If you use wildcards, then the command returns a warning similar to the following:
	```
	eth*/192.168.0.0 global cluster_interconnect
	PRIF-29: Warning: wildcard in network parameters can cause mismatch
	among GPnP profile, OCR, and system
	```
	Note:
	Legacy network configuration does not support wildcards; thus wildcards are resolved using current node configuration at the time of the update.
	See Also:
	[Appendix D, "Oracle Interface Configuration Tool (OIFCFG) Command Reference"](oifcfg.md) for more information about using OIFCFG commands
4. After the previous step completes, you can remove the former subnet, as follows, by providing the name and subnet address of the former interface:
	```
	oifcfg delif -global if_name/subnet
	```
	For example:
	```
	$ oifcfg delif -global eth1/10.10.0.0
	```
	Caution:
	This step should be performed only after a replacement interface is committed into the Grid Plug and Play configuration. Simple deletion of cluster interfaces without providing a valid replacement can result in invalid cluster configuration.
5. Verify the current configuration using the following command:
	```
	oifcfg getif
	```
	For example:
	```
	$ oifcfg getif
	eth2 10.220.52.0 global cluster_interconnect
	eth0 10.220.16.0 global public
	```
6. Stop Oracle Clusterware on all nodes by running the following command as `root` on each node:
	```
	# crsctl stop crs
	```
	Note:
	With cluster network configuration changes, the cluster must be fully stopped; do not use rolling stops and restarts.
7. When Oracle Clusterware stops, deconfigure the deleted network interface in the operating system using the `ifconfig` command. For example:
	```
	$ ifconfig down
	```
	At this point, the IP address from network interfaces for the former subnet is deconfigured from Oracle Clusterware. This command does not affect the configuration of the IP address on the operating system.
	You must update the operating system configuration changes, because changes made using `ifconfig` are not persistent.
	See Also:
	Your operating system documentation for more information about how to make `ifconfig` commands persistent
8. Restart Oracle Clusterware by running the following command on each node in the cluster as the `root` user:
	```
	# crsctl start crs
	```
	The changes take effect when Oracle Clusterware restarts.
	If you use the `CLUSTER_INTERCONNECTS` initialization parameter, then you must update it to reflect the changes.

[^1]: Enter the `crsctl set css ipmiaddr` `bmc_ip_address` command. For example:

```
crsctl set css ipmiaddr 192.0.2.244
```

This command stores the new IPMI IP address of the local IPMI in OLR, After storing the IP address, Oracle Clusterware can retrieve the new configuration and distribute it as required.

[^2]: Enter the `crsctl get css ipmiaddr` command. For example:

```
crsctl get css ipmiaddr
```

This command retrieves the IP address for the local IPMI from OLR and displays it on the console.

[^undefined]: Remove the IPMI configuration information for the local IPMI from OLR and delete the registry entry, as follows:

```
crsctl unset css ipmiconfig
```

[^3]: Ensure that Oracle Clusterware is running and then use CRSCTL to remove the IPMI configuration data from OLR by running the following command:

```
crsctl unset css ipmiconfig
```

[^4]: Restart Oracle Clusterware so that it runs without the IPMI configuration by running the following commands as `root`:

```
# crsctl stop crs
# crsctl start crs
```