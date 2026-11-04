---
title: Oracle Interface Configuration Tool (OIFCFG) Command Reference
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/oifcfg.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## D Oracle Interface Configuration Tool (OIFCFG) Command Reference

The Oracle Interface Configuration Tool (OIFCFG) command-line interface helps you to define and administer network interfaces. You can use OIFCFG commands Oracle Clusterware environments to:

- Allocate and deallocate network interfaces to components
- Direct components to use specific network interfaces
- Retrieve component configuration information

This appendix includes the following topics:

- Starting the OIFCFG Command-Line Interface
- Summary of the OIFCFG Usage

## Starting the OIFCFG Command-Line Interface

Before you invoke OIFCFG, ensure that you have started Oracle Clusterware on at least the local node and preferably on all nodes if you intend to include the `-global` option on the command.

Note:

To change the global network interface, Oracle Clusterware must be running on all cluster nodes.

Run OIFCFG from the `Grid_home` `/bin/` directory as the user who installed the Oracle Clusterware software. For example:

```
$ ./oifcfg
```

Run the `oifcfg -help` command to display online help for OIFCFG.

```
$ ./oifcfg -help

Name:  oifcfg - Oracle Interface Configuration Tool.

Usage:  oifcfg iflist [-p [-n]]
        oifcfg setif {-node nodename | -global} {if_name/subnet:if_type}...
        oifcfg getif [-node nodename | -global] [ -if if_name[/subnet] [-type if_type]
]
        oifcfg delif {{-node nodename | -global} [if_name[/subnet]] [-force] | -force}
        oifcfg [-help]
 
 nodename       - name of the host, as known to a communications network
 if_name        - name by which the interface is configured in the system
 subnet         - subnet address of the interface
 if_type        - type of the interface {cluster_interconnect | public}
```

## Summary of the OIFCFG Usage

This section contains the following topics:

OIFCFG Command Format

```
oifcfg iflist [-p [-n]]
oifcfg setif {-node nodename | -global} {if_name/subnet:if_name}...
oifcfg getif [-node nodename | -global] [ -if if_name[/subnet] [-type if_type]]
oifcfg delif {{-node nodename | -global} [ -if if_name[/subnet]] [-force] | -force}
oifcfg [-help]
```

OIFCFG Commands

You can enter any of the OIFCFG commands listed in Table D-1.

Table D-1 OIFCFG Commands

| Command | Description |
| --- | --- |
| `oifcfg iflist [-p [-n]]` | Shows the available interfaces that you can configure with `setif`. The `iflist` command queries the operating system to find which network interfaces are present on this node. You can specify two options with this command:  - `-p`: Displays a heuristic assumption of the interface type (PRIVATE, PUBLIC, or UNKNOWN) - `-n`: Displays the netmask |
| `oifcfg setif` | Sets an interface type (public or cluster interconnect) for an interface. |
| `oifcfg getif` | Displays the interfaces for which an interface type has been defined with the `setif` command, along with the type for that interface. |
| `oifcfg delif` | Deletes the stored network configuration for global or node-specific interfaces. You can use the `-force` option without specifying the `-node` or `-global` options to delete the stored network configurations from all nodes in the cluster. |

OIFCFG Command Parameters

This section lists the parameters for the OIFCFG commands. Note that some parameters are optional, depending on which command you run.

\-node nodename

The name of the Oracle Clusterware node as listed in the output from the `olsnodes` command. [Appendix C, "OLSNODES Command Reference"](olsnodes.md) describes the `OLSNODES` command.

\-global

A network interface can be stored as a global interface (as reported by the `iflist` command) or as a node-specific interface:

- An interface is stored as a global interface when all of the nodes of an Oracle Real Application Clusters (Oracle RAC) cluster have the same interface connected to the same subnet. The global interface (and configuring all nodes with the same network interface for each public subnet and the same network interface for each private subnet) is not only the recommended configuration, but it is also the default installation configuration.
- An interface can be stored as a node-specific (local) interface.
	Note:
	Oracle currently does not support having different network interfaces for each node in the cluster. The best practice is to configure all nodes with the same network interface for each public subnet and the same network interface for each private subnet.

\-if if\_name

The name by which the interface is configured in the system.

subnet

The subnet number of the interface.

\-type if\_type

The type of interface: `public` or `cluster_interconnect`.

\-help

Display online help for OIFCFG commands.

OIFCFG Usage Notes

- A network interface specification takes the following form:
	```
	if_name
	/subnet
	:if_type
	```
	The specification uniquely identifies the network interface using the:
	- Interface name
		When using the `oifcfg setif` command, you can specify interface names that contain wildcard characters, such as an asterisk (\*), which matches any string. However, you must surround interface names that contain wildcards with double quotation marks (`""`).
		Note:
		If you use wildcards on pre-Oracle Database 11g release 2 (11.2.0.2) databases, then Oracle resolves the interface name by expanding the wildcard on the local node. Therefore, using wildcards is not recommended on clusters with pre-Oracle Database 11g release 2 (11.2.0.2) databases. If you use wildcards with pre-Oracle Database 11g release 2 (11.2.0.2) databases, then those databases must use the `CLUSTER_INTERCONNECTS` parameter instead.
		- Associated subnet
		- Interface type
		The interface type indicates the purpose for which the network is configured. The supported interface types are:
		- `public`: An interface that can be used for communication with components external to Oracle RAC instances, such as Oracle Net and Virtual Internet Protocol (VIP) addresses.
				- `cluster_interconnect`: A private interface used for the cluster interconnect to provide interinstance or Cache Fusion <sup>Foot 1</sup> communication.
		If you set the interface type to `cluster_interconnect`, then it affects instances as they start and changes do not take effect until you restart the instances.
	For example, the following specification identifies `qfe0` as a cluster interconnect located at the address 204.152.65.0:
	```
	qfe0/204.152.65.0:cluster_interconnect
	```
- The Oracle Universal Installer uses OIFCFG to identify and display available interfaces.
- The effect of changing the interface names depends on which name you are changing, and whether you are also changing the IP address. In cases where you change only the interface names, the ramifications are minor. If you change the name for the public interface that is stored in the Oracle Cluster Registry (OCR), you must modify the nodeapps for each node. Therefore, you must stop the nodeapps for this change to take effect.
- You must restart Oracle Clusterware on all members of the cluster when you make global changes. For local changes, you need only to perform a node restart. Interconnect changes for the database occur at instance startup. However, the interconnect for Oracle Clusterware might be different.
- Because interconnects are chosen when instances start, just issuing OIFCFG commands does not have an immediate effect on the running system. Instead, changes take effect after restarting the component that might be affected by the command.
- Changes you make to cluster-wide network classifications with OIFCFG require all known cluster nodes to be up so that their Grid Plug and Play profiles can be updated.

OIFCFG Examples

The following examples show some common uses for the OIFCFG commands.

Example 1 Listing the Names of Network Interfaces

You can use OIFCFG to list the interface names and the subnets of all of the interfaces available on the local node by executing the `iflist` keyword, as shown in this example:

```
oifcfg iflist
eth0     172.19.141.0
eth1     172.21.65.0
```

Example 2 Retrieving Network Information

You can also retrieve specific OIFCFG information with a `getif` command.

For example, after you install Oracle Clusterware, you can verify that the public and cluster interconnect have been set to the desired values by entering the following command:

```
$ oifcfg getif
```

This command returns values for global `public` and global `cluster_interconnect`, similar to the following:

```
eth0 172.19.141.0 global public
eth1 172.21.65.0 global cluster_interconnect
```

Example 3 Storing a Global Interface

To store an interface, use the `setif` keyword. For example, to store the interface `eth0`, with the subnet 172.19.141.0, as a global interface (to be used as an interconnect for all of the Oracle RAC instances in your cluster and Oracle Clusterware), use the command:

```
oifcfg setif -global eth0/172.19.141.0:cluster_interconnect
```

Note:

Ensure that all nodes are running when you run the `setif` command because Oracle cannot update Grid Plug and Play profiles on nodes that are not running.

Example 4 Deleting the Stored Interface

Use the `oifcfg delif` command to delete the stored configuration for global or node-specific interfaces. A specific node-specific or global interface can be deleted by supplying the interface name, with an optional subnet, on the command line.

Note:

If you only enter `oifcfg delif`, with no other arguments given on the command line, then OIFCFG deletes all interfaces on all nodes in the cluster.

For example, the following command deletes the global interface named `eth1` for the subnet 172.21.65.0:

```
oifcfg delif -global eth1/172.21.65.0
```

The following command deletes all of the global interfaces assigned with OIFCFG:

```
oifcfg delif -global
```

---

Footnote Legend

Footnote 1: Cache Fusion is a diskless cache coherency mechanism that provides copies of blocks directly from a holding instance's memory cache to a requesting instance's memory cache.