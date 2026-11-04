---
title: Adding and Deleting Oracle RAC from Nodes on Linux and UNIX Systems
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelunix.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## 10 Adding and Deleting Oracle RAC from Nodes on Linux and UNIX Systems

This chapter describes how to extend an existing Oracle Real Application Clusters (Oracle RAC) home to other nodes and instances in the cluster, and delete Oracle RAC from nodes and instances in the cluster. This chapter provides instructions for Linux and UNIX systems.

If your goal is to clone an existing Oracle RAC home to create multiple new Oracle RAC installations across the cluster, then use the cloning procedures that are described in [Chapter 8, "Cloning Oracle RAC to Nodes in a New Cluster"](clonerac.md).

The topics in this chapter include the following:

- Adding Oracle RAC to Nodes with Oracle Clusterware Installed
- Deleting Oracle RAC from a Cluster Node

Notes:

- Ensure that you have a current backup of Oracle Cluster Registry (OCR) before adding or deleting Oracle RAC by running the `ocrconfig -showbackup` command.
- The phrase "target node" as used in this chapter refers to the node to which you plan to extend the Oracle RAC environment.

See Also:

- [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/addnodes.htm#TDPRC394) for additional information about configuring a new Oracle RAC cluster or scaling up an existing Oracle RAC cluster
- [Chapter 11, "Adding and Deleting Oracle RAC from Nodes on Windows Systems"](adddelwin.md)

## Adding Oracle RAC to Nodes with Oracle Clusterware Installed

Before beginning this procedure, ensure that your existing nodes have the correct path to the `Grid_home` and that the `$ORACLE_HOME` environment variable is set to the Oracle RAC home.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD1167) for information about extending the Oracle Clusterware home to new nodes in a cluster

If you are using a local (non-shared) Oracle home, you must extend the Oracle RAC database home that is on an existing node (`node1` in this procedure) to a target node (`node3` in this procedure).

1. Navigate to the `$ORACLE_HOME/oui/bin` directory on `node1` and run the `addNode.sh` script using the following syntax:
	```
	$ ./addNode.sh -silent "CLUSTER_NEW_NODES={node3}"
	```
2. Run the `$ORACLE_HOME/root.sh` script on `node3` as `root`.

If you are using a shared Oracle home (such as storing the Oracle home on Oracle Automatic Storage Management Cluster File System (Oracle ACFS)), then you do not have to extend the Oracle RAC database home to the target nodes because the home is shared across the nodes in the cluster.

Instead, you must first create a mount point for the Oracle RAC database home on the target node, mount and attach the Oracle home, and update the Oracle inventory, as follows:

1. Run the `srvctl config db -d` `db_name` command on an existing node in the cluster to obtain the mount point information.
2. Run the following command as `root` on `node3` to create the mount point:
	```
	# mkdir -p mount_point_path
	```
3. Mount the file system that hosts the Oracle RAC database home.
4. Run the following command from the `Oracle_home` `/oui/bin` directory on the node you are adding to add the Oracle RAC database home:
	```
	$ ./runInstaller -attachHome ORACLE_HOME="ORACLE_HOME""CLUSTER
	_NODES={node_list}" LOCAL_NODE="node_name"
	```
5. Update the Oracle Inventory, as follows:
	```
	$ ./runInstaller -updateNodeList ORACLE_HOME=mount_point_path "CLUSTER
	_NODES={node_list}"
	```
	In the preceding command, `node_list` refers to a list of all nodes where the Oracle RAC database home is installed, including the node you are adding.
6. Run the `Grid_home` `/root.sh` script on the `node3` as `root` and run the subsequent script, as instructed.

Note:

Oracle recommends that you back up the OCR after you complete the node addition process.

You can now add an Oracle RAC database instance to the target node using either of the procedures in the following sections.

- Adding Policy-Managed Oracle RAC Database Instances to Target Nodes
- Adding Administrator-Managed Oracle RAC Database Instances to Target Nodes

### Adding Policy-Managed Oracle RAC Database Instances to Target Nodes

Before adding an Oracle RAC database instance, run the following command on an existing node to configure Oracle Enterprise Manager on the node where you plan to add the database instance:

```
$ emca -addNode db
```

The Oracle Enterprise Manager Configuration Assistant prompts you for database and node information.

See Also:

[Oracle Real Application Clusters Installation Guide for Linux and UNIX](https://docs.oracle.com/cd/E11882_01/install.112/e41962/toc.htm) for more information about configuring Oracle Enterprise Manager

You must manually add undo and redo logs, unless you store your policy-managed database on Oracle Automatic Storage Management (Oracle ASM) and [Oracle Managed Files](rac_glossary.md) is enabled.

If there is space in a server pool to add a node and the database has been started at least once, then Oracle Clusterware adds the Oracle RAC database instance to the newly added node and no further action is necessary.

Note:

The database must have been started at least once before you can add the database instance to the newly added node.

If there is no space in any server pool, then the newly added node moves into the Free server pool. Use the `srvctl modify srvpool` command to increase the cardinality of a server pool to accommodate the newly added node, after which the node moves out of the Free server pool and into the modified server pool, and Oracle Clusterware adds the Oracle RAC database instance to the node.

### Adding Administrator-Managed Oracle RAC Database Instances to Target Nodes

Note:

The procedures in this section only apply to administrator-managed databases. Policy-managed databases use nodes when the nodes are available in the databases' server pool.

You can use either Oracle Enterprise Manager or DBCA to add Oracle RAC database instances to the target nodes. To add a database instance to a target node with Oracle Enterprise Manager, see the [Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for complete information.

This section describes using DBCA to add Oracle RAC database instances under the following topics:

- Using DBCA in Interactive Mode to Add Database Instances to Target Nodes
- Using DBCA in Silent Mode to Add Database Instances to Target Nodes

These tools guide you through the following tasks:

- Creating a new database instance on each target node
- Creating and configuring high availability components
- Creating the Oracle Net configuration for a non-default listener from the Oracle home
- Starting the new instance
- Creating and starting services if you entered services information on the Services Configuration page

After adding the instances to the target nodes, you should perform any necessary service configuration procedures, as described in [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md).

#### Using DBCA in Interactive Mode to Add Database Instances to Target Nodes

To add a database instance to a target node with DBCA in interactive mode, perform the following steps:

1. Ensure that your existing nodes have the `$ORACLE_HOME` environment variable set to the Oracle RAC home.
2. Start DBCA by entering `dbca` at the system prompt from the `Oracle_home` `/bin` directory.
	DBCA performs certain CVU checks while running. However, you can also run CVU from the command line to perform various verifications.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for more information about CVU
	DBCA displays the Welcome page for Oracle RAC. Click Help on any DBCA page for additional information.
3. Select Oracle Real Application Clusters (RAC) database, click Next, and DBCA displays the Operations page.
4. Select Instance Management, click Next, and DBCA displays the Instance Management page.
5. Select Add Instance and click Next. DBCA displays the List of Cluster Databases page that shows the databases and their current status, such as `ACTIVE` or `INACTIVE`.
6. From the List of Cluster Databases page, select the active Oracle RAC database to which you want to add an instance. Enter user name and password for the database user that has `SYSDBA` privileges. Click Next and DBCA displays the List of Cluster Database Instances page showing the names of the existing instances for the Oracle RAC database that you selected.
7. Click Next to add a new instance and DBCA displays the Adding an Instance page.
8. On the Adding an Instance page, enter the instance name in the field at the top of this page if the instance name that DBCA provides does not match your existing instance naming scheme.
9. Review file locations for undo tablespaces and redo log groups of the new instance and click Finish on the Instance Storage page.
10. Review the information on the Summary dialog and click OK or click Cancel to end the instance addition operation. DBCA displays a progress dialog showing DBCA performing the instance addition operation. When DBCA completes the instance addition operation, DBCA displays a dialog asking whether you want to perform another operation.
11. After you terminate your DBCA session, run the following command to verify the administrative privileges on the target node and obtain detailed information about these privileges where `nodelist` consists of the names of the nodes on which you added database instances:
	```
	cluvfy comp admprv -o db_config -d Oracle_home -n nodelist [-verbose]
	```
12. Perform any necessary service configuration procedures, as described in [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md).

#### Using DBCA in Silent Mode to Add Database Instances to Target Nodes

You can use DBCA in silent mode to add instances to nodes on which you have extended an Oracle Clusterware home and an Oracle Database home. Before you run the `dbca` command, ensure that you have set the `ORACLE_HOME` environment variable correctly on the existing nodes. Run DBCA, supplying values for the variables described in Table 10-1,as follows:

```
dbca -silent -addInstance -nodeList node_name -gdbName gdb_name
[-instanceName instance_name -sysDBAUserName sysdba -sysDBAPassword password]
```

Table 10-1 Variables in the DBCA Silent Mode Syntax

| Variable | Description |
| --- | --- |
| `node_name` | The node on which you want to add (or delete) the instance. |
| `gdb_name` | Global database name. |
| `instance_name` | Name of the instance. Provide an instance name only if you want to override the Oracle naming convention for Oracle RAC instance names. |
| `sysdba` | Name of the Oracle user with `SYSDBA` privileges. |
| `password` | Password for the `SYSDBA` user. |

Perform any necessary service configuration procedures, as described in [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md).

## Deleting Oracle RAC from a Cluster Node

To remove Oracle RAC from a cluster node, you must delete the database instance and the Oracle RAC software before removing the node from the cluster.

Note:

If there are no database instances on the node you want to delete, then proceed to "Removing Oracle RAC".

This section includes the following procedures to delete nodes from clusters in an Oracle RAC environment:

- Deleting Instances from Oracle RAC Databases
- Removing Oracle RAC
- Deleting Nodes from the Cluster

### Deleting Instances from Oracle RAC Databases

The procedures for deleting database instances are different for policy-managed and administrator-managed databases. Deleting a policy-managed database instance involves reducing the number of servers in the server pool in which the database instance resides. Deleting an administrator-managed database instance involves using DBCA to delete the database instance.

Deleting Policy-Managed Database Instances

If you plan to delete the node on which the database instance resides from the cluster, then, before deleting the database instance, run the following command on a remaining node to deconfigure Oracle Enterprise Manager on the node you plan to delete:

```
$ emca -deleteNode db
```

The Oracle Enterprise Manager Configuration Assistant prompts you for database and node information.

To delete a policy-managed database, reduce the number of servers in the server pool in which a database instance resides by relocating the server on which the database instance resides to another server pool. This effectively removes the instance without having to remove the Oracle RAC software from the node or the node from the cluster.

For example, you can delete a policy-managed database by running the following commands on any node in the cluster:

```
$ srvctl stop instance -d db_unique_name -n node_name
$ srvctl relocate server -n node_name -g Free
```

The first command stops the database instance on a particular node and the second command moves the node out of its current server pool and into the Free server pool.

See Also:

"Removing Oracle RAC" for information about removing the Oracle RAC software from a node

Deleting Instances from Administrator-Managed Databases

Note:

Before deleting an instance from an Oracle RAC database, use either SRVCTL or Oracle Enterprise Manager to do the following:
- If you have services configured, then relocate the services
- Modify the services so that each service can run on one of the remaining instances
- Ensure that the instance to be removed from an administrator-managed database is neither a preferred nor an available instance of any service

The procedures in this section explain how to use DBCA in interactive or silent mode, to delete an instance from an Oracle RAC database.

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/addnodes.htm#TDPRC401) for information about how to delete a database instance from a target node with Oracle Enterprise Manager

This section includes the following topics:

- Using DBCA in Interactive Mode to Delete Instances from Nodes
- Using DBCA in Silent Mode to Delete Instances from Nodes

#### Using DBCA in Interactive Mode to Delete Instances from Nodes

To delete an instance using DBCA in interactive mode, perform the following steps:

1. Start DBCA.
	Start DBCA on a node other than the node that hosts the instance that you want to delete. The database and the instance that you plan to delete should be running during this step.
2. On the DBCA Welcome page select Oracle Real Application Clusters Database, click Next. DBCA displays the Operations page.
3. On the DBCA Operations page, select Instance Management and click Next. DBCA displays the Instance Management page.
4. On the DBCA Instance Management page, select the instance to be deleted, select Delete Instance, and click Next.
5. On the List of Cluster Databases page, select the Oracle RAC database from which to delete the instance, as follows:
	1. On the List of Cluster Database Instances page, DBCA displays the instances that are associated with the Oracle RAC database that you selected and the status of each instance. Select the cluster database from which you will delete the instance.
		2. Enter a user name and password for the database user that has `SYSDBA` privileges. Click Next.
		3. Click OK on the Confirmation dialog to proceed to delete the instance.
		DBCA displays a progress dialog showing that DBCA is deleting the instance. During this operation, DBCA removes the instance and the instance's Oracle Net configuration. When DBCA completes this operation, DBCA displays a dialog asking whether you want to perform another operation.
		Click No and exit DBCA or click Yes to perform another operation. If you click Yes, then DBCA displays the Operations page.
6. Verify that the dropped instance's redo thread has been removed by using SQL\*Plus on an existing node to query the `GV$LOG` view. If the redo thread is not disabled, then disable the thread. For example:
	```
	SQL> ALTER DATABASE DISABLE THREAD 2;
	```
7. Verify that the instance has been removed from OCR by running the following command, where `db_unique_name` is the database unique name for your Oracle RAC database:
	```
	srvctl config database -d db_unique_name
	```
8. If you are deleting more than one node, then repeat these steps to delete the instances from all the nodes that you are going to delete.

#### Using DBCA in Silent Mode to Delete Instances from Nodes

You can use DBCA in silent mode to delete a database instance from a node.

Run the following command, where the variables are the same as those shown in Table 10-1 for the DBCA command to add an instance. Provide a node name only if you are deleting an instance from a node other than the one on where DBCA is running as shown in the following example where `password` is the password:

```
dbca -silent -deleteInstance [-nodeList node_name] -gdbName gdb_name
-instanceName instance_name -sysDBAUserName sysdba -sysDBAPassword password
```

At this point, you have accomplished the following:

- Deregistered the selected instance from its associated Oracle Net Services listeners
- Deleted the selected database instance from the instance's configured node
- Removed the Oracle Net configuration
- Deleted the Oracle Flexible Architecture directory structure from the instance's configured node.

### Removing Oracle RAC

This procedure removes Oracle RAC software from the node you are deleting from the cluster and updates inventories on the remaining nodes.

1. If there is a listener in the Oracle RAC home on the node you are deleting, then you must disable and stop it before deleting the Oracle RAC software. Run the following commands on any node in the cluster, specifying the name of the listener and the name of the node you are deleting:
	```
	$ srvctl disable listener -l listener_name -n name_of_node_to_delete
	$ srvctl stop listener -l listener_name -n name_of_node_to_delete
	```
2. Run the following command from `$ORACLE_HOME/oui/bin` on the node that you are deleting to update the inventory on that node:
	```
	$ ./runInstaller -updateNodeList ORACLE_HOME=Oracle_home_location
	"CLUSTER_NODES={name_of_node_to_delete}" -local
	```
3. Depending on whether you have a shared or nonshared Oracle home, complete one of the following two procedures to remove the Oracle RAC software:
	- For a shared home, detach the node instead of deinstalling it by running the following command from the `$ORACLE_HOME/oui/bin` directory on each of the nodes that you want to delete:
		```
		$ ./runInstaller -detachHome ORACLE_HOME=Oracle_home_location
		```
		- For a nonshared home, deinstall the Oracle home from the node that you are deleting by running the following command:
		```
		$ORACLE_HOME/deinstall/deinstall -local
		```
		See Also:
		[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD1167) for more information about deleting nodes
4. Run the following command from the `$ORACLE_HOME/oui/bin` directory on any one of the remaining nodes in the cluster to update the inventories of those nodes, specifying a comma-delimited list of remaining node names:
	```
	$ ./runInstaller -updateNodeList ORACLE_HOME=Oracle_home_location
	"CLUSTER_NODES={remaining_node_list}"
	```
	If you have a shared Oracle Grid Infrastructure home, then append the `-cfs` option to the command example in this step and provide a complete path location for the cluster file system.

### Deleting Nodes from the Cluster

After you delete the database instance and the Oracle RAC software, you can begin the process of deleting the node from the cluster. You accomplish this by running scripts on the node you want to delete to remove the Oracle Clusterware installation and then you run scripts on the remaining nodes to update the node list.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD90992) for information about deleting nodes from the cluster