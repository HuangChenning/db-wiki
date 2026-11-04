---
title: Adding and Deleting Cluster Nodes
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## 4 Adding and Deleting Cluster Nodes

This chapter describes how to add nodes to an existing cluster, and how to delete nodes from clusters. This chapter provides procedures for these tasks for Linux, UNIX, and Windows systems.

Notes:

- Unless otherwise instructed, perform all add and delete node steps as the user that installed Oracle Clusterware.
- Oracle recommends that you use the cloning procedure described in [Chapter 5, "Cloning Oracle Clusterware"](clonecluster.md) to create clusters.

The topics in this chapter include the following:

## Prerequisite Steps for Adding Cluster Nodes

Note:

Ensure that you perform the preinstallation tasks listed in [Oracle Grid Infrastructure Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e41961/prelinux.htm#CWLIN168) before adding a node to a cluster.

Do not install Oracle Clusterware. The software is copied from an existing node when you add a node to the cluster.

Complete the following steps to prepare nodes to add to the cluster:

1. Make physical connections.
	Connect the nodes' hardware to the network infrastructure of your cluster. This includes establishing electrical connections, configuring network interconnects, configuring shared disk subsystem connections, and so on. See your hardware vendor documentation for details about this step.
2. Install the operating system.
	Install a cloned image of the operating system that matches the operating system on the other nodes in your cluster. This includes installing required service patches, updates, and drivers. See your operating system vendor documentation for details about this process.
	Note:
	Oracle recommends that you use a cloned image. However, if the installation fulfills the installation requirements, then install the operating system according to the vendor documentation.
3. Create Oracle users.
	You must create all Oracle users on the new node that exist on the existing nodes. For example, if you are adding a node to a cluster that has two nodes, and those two nodes have different owners for the Grid Infrastructure home and the Oracle home, then you must create those owners on the new node, even if you do not plan to install an Oracle home on the new node.
	Note:
	Perform this step only for Linux and UNIX systems.
	As `root`, create the Oracle users and groups using the same user ID and group ID as on the existing nodes.
4. Ensure that SSH is configured on the node.
	Note:
	SSH is configured when you install Oracle Clusterware 11g release 2 (11.2). If SSH is not configured, then see [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for information about configuring SSH.
5. Verify the hardware and operating system installations with the Cluster Verification Utility (CVU).
	After you configure the hardware and operating systems on the nodes you want to add, you can run the following command to verify that the nodes you want to add are reachable by other nodes in the cluster. You can also use this command to verify user equivalence to all given nodes from the local node, node connectivity among all of the given nodes, accessibility to shared storage from all of the given nodes, and so on.
	From the `Grid_home` `/bin` directory on an existing node, run the CVU command to obtain a detailed comparison of the properties of the reference node with all of the other nodes that are part of your current cluster environment. Replace `ref_node` with the name of a node in your existing cluster against which you want CVU to compare the nodes to be added. Specify a comma-delimited list of nodes after the `-n` option. In the following example, `orainventory_group` is the name of the Oracle Inventory group, and `osdba_group` is the name of the OSDBA group:
	```
	$ cluvfy comp peer [-refnode ref_node] -n node_list
	[-orainv orainventory_group] [-osdba osdba_group] [-verbose]
	```
	Note:
	For the reference node, select a cluster node against which you want CVU to compare, for example, the nodes that you want to add that you specify with the `-n` option.

After completing the procedures in this section, you are ready to add the nodes to the cluster.

Note:

Avoid changing host names after you complete the Oracle Clusterware installation, including adding or deleting domain qualifications. Nodes with changed host names must be deleted from the cluster and added back with the new name.

## Adding and Deleting Cluster Nodes on Linux and UNIX Systems

This section explains cluster node addition and deletion on Linux and UNIX systems. The procedure in the section for adding nodes assumes that you have performed the steps in the "Prerequisite Steps for Adding Cluster Nodes" section.

The last step of the node addition process includes extending the Oracle Clusterware home from an Oracle Clusterware home on an existing node to the nodes that you want to add.

This section includes the following topics:

- Adding a Cluster Node on Linux and UNIX Systems
- Deleting a Cluster Node on Linux and UNIX Systems

Note:

Beginning with Oracle Clusterware 11g release 1 (11.1), Oracle Universal Installer defaults to silent mode when adding nodes.

### Adding a Cluster Node on Linux and UNIX Systems

This procedure describes how to add a node to your cluster. This procedure assumes that:

- There is an existing cluster with two nodes named `node1` and `node2`
- You are adding a node named `node3` using a virtual node name, `node3-vip`, that resolves to an IP address, if you are not using Grid Naming Service (GNS)
- You have successfully installed Oracle Clusterware on `node1` and `node2` in a local (non-shared) home, where `Grid_home` represents the successfully installed home

To add a node:

1. Ensure that you have successfully installed Oracle Clusterware on at least one node in your cluster environment. To perform the following procedure, `Grid_home` must identify your successfully installed Oracle Clusterware home.
	See Also:
	[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for Oracle Clusterware installation instructions
2. Verify the integrity of the cluster and `node3`:
	```
	$ cluvfy stage -pre nodeadd -n node3 [-fixup [-fixupdir fixup_dir]] [-verbose]
	```
	You can specify the `-fixup` option and a directory into which CVU prints instructions to fix the cluster or node if the verification fails.
3. To extend the Grid Infrastructure home to the `node3`, navigate to the `Grid_home` `/oui/bin` directory on `node1` and run the `addNode.sh` script as the user that installed Oracle Clusterware using the following syntax, where `node3` is the name of the node that you are adding and `node3-vip` is the VIP name for the node:
	If you are using Grid Naming Service (GNS), run the following command:
	```
	$ ./addNode.sh "CLUSTER_NEW_NODES={node3}"
	```
	If you are not using GNS, run the following command:
	```
	$ ./addNode.sh "CLUSTER_NEW_NODES={node3}" "CLUSTER_NEW_VIRTUAL_
	HOSTNAMES={node3-vip}"
	```
	Note:
	You can specify multiple nodes for the `CLUSTER_NEW_NODES` and the `CLUSTER_NEW_VIRTUAL_HOSTNAMES` parameters by entering a comma-separated list of nodes between the braces. For example:
	```
	"CLUSTER_NEW_NODES={node3,node4,node5}"
	"CLUSTER_NEW_VIRTUAL_HOSTNAMES={node3-vip,node4-vip,node5-vip}"
	```
	Alternatively, you can specify the entries shown in Example 4-1 in a response file, where `file_name` is the name of the file, and run the `addNode.sh` script, as follows:
	```
	$ ./addNode.sh -responseFile file_name
	```
	Example 4-1 Response File Entries for Adding Oracle Clusterware Home
	```
	RESPONSEFILE_VERSION=2.2.1.0.0
	CLUSTER_NEW_NODES={node3}
	CLUSTER_NEW_VIRTUAL_HOSTNAMES={node3-vip}
	```
	See Also:
	Oracle Universal Installer and OPatch User's Guide for details about how to configure command-line response files
	Notes:
	- If you are not using Oracle Grid Naming Service (GNS), then you must add the name and IP address of `node3` to DNS.
	- Command-line values always override response file values.
4. If you have an Oracle RAC or Oracle RAC One Node database configured on the cluster and you have a local Oracle home, then do the following to extend the Oracle database home to `node3`:
	1. Navigate to the `Oracle_home` `/oui/bin` directory on `node1` and run the `addNode.sh` script as the user that installed Oracle RAC using the following syntax:
		```
		$ ./addNode.sh "CLUSTER_NEW_NODES={node3}"
		```
		2. Run the `Oracle_home` `/root.sh` script on `node3` as `root`, where `Oracle_home` is the Oracle RAC home.
	If you have a shared Oracle home that is shared using Oracle Automatic Storage Management Cluster File System (Oracle ACFS), then do the following as the user that installed Oracle RAC to extend the Oracle database home to `node3`:
	1. Run the `Grid_home` `/root.sh` script on `node3` as `root`, where `Grid_home` is the Oracle Grid Infrastructure home.
		2. Start the Oracle ACFS resource on the new node by running the following command as `root` from the `Grid_home` `/bin` directory:
		```
		# srvctl start filesystem -d volume_device_name [-n node_name]
		```
		Note:
		.Make sure the Oracle ACFS resources, including Oracle ACFS registry resource and Oracle ACFS file system resource where the ORACLE\_HOME is located, are online on the newly added node.
		3. Navigate to the `Oracle_home` `/oui/bin` directory on `node1` and run the `addNode.sh` script as the user that installed Oracle RAC using the following syntax:
		```
		$ ./addNode.sh -noCopy "CLUSTER_NEW_NODES={node3}"
		```
		Note:
		Use the `-noCopy` option because the Oracle home on the destination node is already fully populated with software.
	If you have a shared Oracle home on a shared file system that is not Oracle ACFS, then you must first create a mount point for the Oracle RAC database home on the target node, mount and attach the Oracle RAC database home, and update the Oracle Inventory, as follows:
	1. Run the `srvctl config db -d` `db_name` command on an existing node in the cluster to obtain the mount point information.
		2. Run the following command as `root` on `node3` to create the mount point:
		```
		# mkdir -p mount_point_path
		```
		3. Mount the file system that hosts the Oracle RAC database home.
		4. Run the following command as the user that installed Oracle RAC from the `Oracle_home` `/oui/bin` directory on the node you are adding to add the Oracle RAC database home:
		```
		$ ./runInstaller -attachHome ORACLE_HOME="ORACLE_HOME" "CLUSTER
		_NODES={node_list}" LOCAL_NODE="node_name"
		```
		5. Update the Oracle Inventory as the user that installed Oracle RAC, as follows:
		```
		$ ./runInstaller -updateNodeList ORACLE_HOME=mount_point_path "CLUSTER
		_NODES={node_list}"
		```
		In the preceding command, `node_list` refers to a list of all nodes where the Oracle RAC database home is installed, including the node you are adding.
5. Run the `Grid_home` `/root.sh` script on the `node3` as `root` and run the subsequent script, as instructed.
6. Run the following CVU command as the user that installed Oracle Clusterware to check cluster integrity. This command verifies that any number of specified nodes has been successfully added to the cluster at the network, shared storage, and clusterware levels:
	```
	$ cluvfy stage -post nodeadd -n node3 [-verbose]
	```
	See Also:
	`"cluvfy stage [-pre | -post] nodeadd"` for more information about this CVU command

Check whether either a policy-managed or administrator-managed Oracle RAC database is configured to run on `node3` (the newly added node). If you configured an administrator-managed Oracle RAC database, you may need to use DBCA to add an instance to the database to run on this newly added node.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelunix.htm#RACAD070) for more information about using DBCA to add administrator-managed Oracle RAC database instances
- [Oracle Real Application Clusters Administration and Deployment Guide to add an Oracle RAC database instance to the target node if you configured a policy-managed Oracle RAC database](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelunix.htm#RACAD8316)

### Deleting a Cluster Node on Linux and UNIX Systems

This section describes the procedure for deleting a node from a cluster.

Notes:

- You can remove the Oracle RAC database instance from the node before removing the node from the cluster but this step is not required. If you do not remove the instance, then the instance is still configured but never runs. Deleting a node from a cluster does not remove a node's configuration information from the cluster. The residual configuration information does not interfere with the operation of the cluster.
	See Also: [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelunix.htm#RACAD7358) for more information about deleting an Oracle RAC database instance
- If you run a dynamic Grid Plug and Play cluster using DHCP and GNS, then you need only perform step [^1] (remove VIP resource), step [^2] (delete node), and step [^3] (update inventory on remaining nodes).
	Also, in a Grid Plug and Play cluster, if you have nodes that are unpinned, Oracle Clusterware forgets about those nodes after a time and there is no need for you to remove them.
- If one creates node-specific configuration for a node (such as disabling a service on a specific node, or adding the node to the candidate list for a server pool) that node-specific configuration is not removed when the node is deleted from the cluster. Such node-specific configuration must be removed manually.
- Voting disks are automatically backed up in OCR after any changes you make to the cluster.

To delete a node from a cluster:

## Adding and Deleting Cluster Nodes on Windows Systems

This section explains cluster node addition and deletion on Windows systems. This section includes the following topics:

- Adding a Node to a Cluster on Windows Systems
- Deleting a Cluster Node on Windows Systems

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for more information about deleting an entire cluster

### Adding a Node to a Cluster on Windows Systems

Ensure that you complete the prerequisites listed in "Prerequisite Steps for Adding Cluster Nodes" before adding nodes.

This procedure describes how to add a node to your cluster. This procedure assumes that:

- There is an existing cluster with two nodes named `node1` and `node2`
- You are adding a node named `node3`
- You have successfully installed Oracle Clusterware on `node1` and `node2` in a local home, where `Grid_home` represents the successfully installed home

Note:

Do not use the procedures described in this section to add cluster nodes in configurations where the Oracle database has been upgraded from Oracle Database 10g release 1 (10.1) on Windows systems.

To add a node:

1. Verify the integrity of the cluster and `node3`:
	```
	C:\>cluvfy stage -pre nodeadd -n node3 [-fixup [-fixupdir fixup_dir]] [-verbose]
	```
	You can specify the `-fixup` option and a directory into which CVU prints instructions to fix the cluster or node if the verification fails.
2. On `node1`, go to the `Grid_home` `\oui\bin` directory and run the `addNode.bat` script, as follows:
	```
	C:\>addNode.bat "CLUSTER_NEW_NODES={node3}"
	"CLUSTER_NEW_VIRTUAL_HOSTNAMES={node3-vip}"
	```
	You can alternatively specify the entries shown in Example 4-2 in a response file and run `addNode.bat` as follows:
	```
	C:\>addNode.bat -responseFile filename
	```
	Example 4-2 Response File Entries for Adding a Node
	```
	CLUSTER_NEW_NODES={"node3"}
	CLUSTER_NEW_VIRTUAL_HOSTNAMES={"node3-vip"}
	```
	Command-line values always override response file values.
	See Also:
	[Oracle Universal Installer and OPatch User's Guide](https://docs.oracle.com/cd/E11882_01/em.112/e12255/toc.htm) for details about how to configure command-line response files
3. Run the following command on the new node:
	```
	C:\>Grid_home\crs\config\gridconfig.bat
	```
4. Run the following command to verify the integrity of the Oracle Clusterware components on all of the configured nodes, both the preexisting nodes and the nodes that you have added:
	```
	C:\>cluvfy stage -post crsinst -n all [-verbose]
	```

After you complete the procedure in this section for adding nodes, you can optionally extend Oracle Database with Oracle Real Application Clusters (Oracle RAC) components to the new nodes, making them members of an existing Oracle RAC database.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelunix.htm#RACAD7348) for more information about extending Oracle Database with Oracle RAC to new nodes

### Deleting a Cluster Node on Windows Systems

This section describes how to delete a cluster node on Windows systems. This procedure assumes that Oracle Clusterware is installed on `node1`, `node2`, and `node3`, and that you are deleting `node3` from the cluster.

Notes:

- Oracle does not support using Oracle Enterprise Manager to delete nodes on Windows systems.
- Oracle recommends that you back up your voting disk and OCRs after you complete any node addition or deletion procedures.
- You can remove the Oracle RAC database instance from the node before removing the node from the cluster but this step is not required. If you do not remove the instance, then the instance is still configured but never runs. Deleting a node from a cluster does not remove a node's configuration information from the cluster. The residual configuration information does not interfere with the operation of the cluster.
	See Also: [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelwin.htm#RACAD8200) for more information about deleting an Oracle RAC database instance

To delete a cluster node on Windows systems:

1. Before you delete a node, you must disable the Oracle Clusterware applications and services running on the node.
	On the node you want to delete, run the `rootcrs.pl -deconfig` script as a member of the Administrators groups, as follows:
	```
	C:\>Grid_home\perl\bin\perl -I$Grid_home\perl\lib -I$Grid_home\crs\install
	Grid_home\crs\install\rootcrs.pl -deconfig -force
	```
	If you are deleting multiple nodes, then run this script on each node that you are deleting.
2. On a node that you are not deleting, run the following command:
	```
	C:\>Grid_home\bin\crsctl delete node -n node_to_be_deleted
	```
3. Only if you have a local home, on the node you want to delete, run the following command with `-local` option to update the node list:
	```
	C:\>Grid_home\oui\bin\setup.exe -updateNodeList ORACLE_HOME=Grid_home "CLUSTER_NODES=
	{node_to_be_deleted}" CRS=TRUE -local
	```
4. Run the deinstall tool located in the `Grid_home` `\deinstall` directory to deinstall and deconfigure the Oracle Clusterware home, as follows:
	```
	C:\>deinstall.bat
	```
5. On any node that you are not deleting, run the following command from the `Grid_home` `\oui\bin` directory where `remaining_nodes_list` is a comma-delimited list of the nodes that are going to remain part of your cluster:
	```
	C:\>setup.exe –updateNodeList ORACLE_HOME=Grid_home
	"CLUSTER_NODES={remaining_nodes_list}" CRS=TRUE -silent
	```
	Notes:
	- You must run this command a second time where `ORACLE_HOME=` `ORACLE_HOME`, and `CRS=TRUE -silent` is omitted from the syntax, as follows:
		```
		C:\>setup.exe -updateNodeList ORACLE_HOME=ORACLE_HOME
		 "CLUSTER_NODES={remaining_nodes_list}"
		```
	- If you have a shared Oracle Grid Infrastructure home, then append the `-cfs` option to the command example in this step and provide a complete path location for the cluster file system.
6. Run the following CVU command to verify that the specified nodes have been successfully deleted from the cluster:
	```
	C:\>cluvfy stage -post nodedel -n node_list [-verbose]
	```
	See Also:
	`"cluvfy stage -post nodedel"`

[^1]: Disable the Oracle Clusterware applications and daemons running on the node. Run the `rootcrs.pl` script as `root` from the `Grid_home` `/crs/install` directory on the node to be deleted, as follows:

Note:

Before you run this command, you must stop the `EMAGENT`, as follows:
```
$ emctl stop dbconsole
```

```
# ./rootcrs.pl -deconfig -force
```

If you are deleting multiple nodes, then run the `rootcrs.pl` script on each node that you are deleting.

If you are deleting all nodes from a cluster, then append the `-lastnode` option to the preceding command to clear OCR and the voting disks, as follows:

```
# ./rootcrs.pl -deconfig -force -lastnode
```

Caution:

Only use the `-lastnode` option if you are deleting all cluster nodes because that option causes the `rootcrs.pl` script to clear OCR and the voting disks of data.

Note:

If you do not use the `-force` option in the preceding command or the node you are deleting is not accessible for you to execute the preceding command, then the VIP resource remains running on the node. You must manually stop and remove the VIP resource using the following commands as `root` from any node that you are not deleting:
```
# srvctl stop vip -i vip_name -f
# srvctl remove vip -i vip_name -f
```

Where `vip_name` is the VIP for the node to be deleted. If you specify multiple VIP names, then separate the names with commas and surround the list in double quotation marks (`""`).

[^2]: From any node that you are not deleting, run the following command from the `Grid_home` `/bin` directory as `root` to delete the node from the cluster:

```
# crsctl delete node -n node_to_be_deleted
```

[^undefined]: On the node you want to delete, run the following command as the user that installed Oracle Clusterware from the `Grid_home` `/oui/bin` directory where `node_to_be_deleted` is the name of the node that you are deleting:

```
$ ./runInstaller -updateNodeList ORACLE_HOME=Grid_home "CLUSTER_NODES=
{node_to_be_deleted}" CRS=TRUE -silent -local
```

Caution:

Before you proceed to the next step, check the `inventory.xml` to ensure that it has not been updated. If you perform this step and mistakenly update the `inventory.xml` file, or you fail to complete this step and move on to the next step, then the next step will deinstall the entire cluster.

[^3]: On any node other than the node you are deleting, run the following command from the `Grid_home` `/oui/bin` directory where `remaining_nodes_list` is a comma-delimited list of the nodes that are going to remain part of your cluster:

```
$ ./runInstaller -updateNodeList ORACLE_HOME=Grid_home "CLUSTER_NODES=
{remaining_nodes_list}" CRS=TRUE -silent
```

Notes:

- You must run this command a second time where `ORACLE_HOME=` `ORACLE_HOME`, and `CRS=TRUE -silent` is omitted from the syntax, as follows:
	```
	$ ./runInstaller -updateNodeList ORACLE_HOME=ORACLE_HOME
	 "CLUSTER_NODES={remaining_nodes_list}"
	```
- If you have a shared Oracle Grid Infrastructure home, then append the `-cfs` option to the command example in this step and provide a complete path location for the cluster file system.

[^undefined]: Run the following CVU command to verify that the specified nodes have been successfully deleted from the cluster:

```
$ cluvfy stage -post nodedel -n node_list [-verbose]
```

See Also:

`"cluvfy stage -post nodedel"` for more information about this CVU command