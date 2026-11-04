---
title: Adding and Deleting Oracle RAC from Nodes on Windows Systems
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/adddelwin.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## 11 Adding and Deleting Oracle RAC from Nodes on Windows Systems

This chapter describes how to extend an existing Oracle Real Application Clusters (Oracle RAC) home to other nodes and instances in the cluster, and delete Oracle RAC from nodes and instances in the cluster. This chapter provides instructions for Windows systems.

Notes:

In this chapter, the entries for `Grid_home` refer to the full path name for the Oracle Grid Infrastructure home, and the entries for `Oracle_home` refer to substitutes for environment variables for the Oracle home with Oracle RAC.

If your goal is to clone an existing Oracle RAC home to create multiple new Oracle RAC installations across the cluster, then use the cloning procedures that are described in [Chapter 8, "Cloning Oracle RAC to Nodes in a New Cluster"](clonerac.md).

This chapter includes the following topics:

- Adding Oracle RAC to Nodes with Oracle Clusterware Installed
- Deleting Oracle RAC from a Cluster Node

Notes:

- Ensure that you have a current backup of Oracle Cluster Registry (OCR) before adding or deleting Oracle RAC by running the `ocrconfig -showbackup` command.
- Using Oracle Enterprise Manager to add and delete nodes and instances is not supported on Windows.
- For all of the add node and delete node procedures, temporary directories such as `%TEMP%` or `C:\Temp` should not be shared directories. If your temporary directories are shared, then set your temporary environment variable, such as `%TEMP%`, to a location on a local node. In addition, use a directory path that exists on all of the nodes.

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=TDPRC009) for additional information about configuring a new Oracle RAC cluster or adding to and deleting nodes from an existing Oracle RAC cluster.

## Adding Oracle RAC to Nodes with Oracle Clusterware Installed

Before beginning this procedure, ensure that your existing nodes have the correct path to the `Grid_home` and that the `Oracle_home` environment variables are set correctly.

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD1167) for information about adding nodes to a cluster

To add Oracle RAC database instances to nodes that already have Oracle Clusterware installed, you must extend the Oracle RAC home that is on an existing node (`node1` in this procedure) of the cluster to the target nodes.

1. Navigate to the `Oracle_home` `\oui\bin` directory on `node1` and run the `addNode.bat` script using the following syntax, where `node2` is the name of the node you are adding:
	```
	addNode.bat "CLUSTER_NEW_NODES={node2}"
	```
2. If you store your policy-managed database on Oracle Automatic Storage Management (Oracle ASM), [Oracle Managed Files](rac_glossary.md) is enabled, and if there is space in a server pool for `node2`, then `crsd` adds the Oracle RAC database instance to `node2` and no further action is necessary. If Oracle Managed Files is not enabled, then you must manually add undo and redo logs.
	If there is no space in a server pool, then `node2` moves into the Free server pool. Use the `srvctl modify srvpool` command to increase the cardinality of the server pool to accommodate `node2`, after which time `node2` moves out of the Free server pool and into the modified server pool, and `crsd` adds the Oracle RAC database instance to `node2`.
3. If you have an administrator-managed database, then add a new instance on `node2` as described in "Adding Administrator-Managed Oracle RAC Database Instances to Target Nodes".

Note:

Oracle recommends that you back up your voting disk and Oracle Cluster Registry (OCR) files after you complete the node addition process.

### Adding Administrator-Managed Oracle RAC Database Instances to Target Nodes

Before adding an Oracle RAC database instance, run the following command on an existing node to configure Oracle Enterprise Manager on the node where you plan to add the database instance:

```
C:\>emca -addNode db
```

The Oracle Enterprise Manager Configuration Assistant prompts you for database and node information.

See Also:

[Oracle Real Application Clusters Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e48195/toc.htm) for more information about configuring Oracle Enterprise Manager

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

To add a database instance to a target node using DBCA in interactive mode, perform the following steps:

1. Ensure that your existing nodes have the Oracle home environment variable set correctly.
2. Start DBCA by entering `dbca` at the system prompt from the `Oracle_home` `\bin` directory on an existing node.
	DBCA performs certain CVU checks while running. However, you can also run CVU from the command line to perform various verifications.
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/cvu.htm#CWADD1100) for more information about CVU
	DBCA displays the Welcome page for Oracle RAC. Click Help on any DBCA page for additional information.
3. Select Oracle Real Application Clusters database, click Next, and DBCA displays the Operations page.
4. Select Instance Management, click Next, and DBCA displays the Instance Management page.
5. Select Add Instance and click Next. DBCA displays the List of Cluster Databases page that shows the databases and their current status, such as `ACTIVE` or `INACTIVE`.
6. From the List of Cluster Databases page, select the active Oracle RAC database to which you want to add an instance. Enter the user name and password for a database user that has `SYSDBA` privileges. Click Next and DBCA displays the List of Cluster Database Instances page showing the names of the existing instances for the Oracle RAC database that you selected.
7. Click Next to add a new instance and DBCA displays the Adding an Instance page.
8. On the Adding an Instance page, enter the instance name in the field at the top of this page if the instance name that DBCA provides does not match your existing instance naming scheme. Then select the new node name from the list, click Next, and DBCA displays the Services Page.
9. Enter the services information for the new node's instance, click Next, and DBCA displays the Instance Storage page.
10. If you are using Oracle ASM or a cluster file system, then click Finish on the Instance Storage page.
11. Review the information on the Summary dialog and click OK or click Cancel to end the instance addition operation. The DBCA displays a progress dialog showing DBCA performing the instance addition operation. When DBCA completes the instance addition operation, DBCA displays a dialog asking whether you want to perform another operation.
12. After you terminate your DBCA session, run the following command to verify the administrative privileges on the new node and obtain detailed information about these privileges where nodelist consists of the newly added nodes:
	```
	cluvfy comp admprv -o db_config -d oracle_home -n nodelist [-verbose]
	```
13. Perform any necessary service configuration procedures, as described in [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md).

#### Using DBCA in Silent Mode to Add Database Instances to Target Nodes

You can use DBCA in silent mode to add instances to nodes on which you have extended an Oracle Clusterware home and an Oracle Database home. Use the following syntax:

```
dbca -silent -addInstance -nodeList node_name -gdbName gdb_name
[-instanceName instance_name -sysDBAUserName sysdba -sysDBAPassword password]
```

See Also:

[Table 10-1](adddelunix.md) for definitions of the variables used in the preceding syntax

Perform any necessary service configuration procedures, as described in [Chapter 5, "Introduction to Automatic Workload Management"](hafeats.md).

## Deleting Oracle RAC from a Cluster Node

To remove Oracle RAC from a cluster node, you must delete the database instance and the Oracle RAC software prior to removing the node from the cluster.

Note:

If there are no database instances on the node you want to delete, then proceed to "Removing Oracle RAC".

This section includes the following procedures to delete nodes from clusters in an Oracle RAC environment:

- Deleting Instances from Oracle RAC Databases
- Removing Oracle RAC
- Deleting Nodes from the Cluster

### Deleting Instances from Oracle RAC Databases

The procedures for deleting instances are different for policy-managed and administrator-managed databases. Deleting a policy-managed database instance involves reducing the size of the server pool in which the database instance resides. Deleting an administrator-managed database instance involves using DBCA to delete the database instance.

Deleting Policy-Managed Databases

If you plan to delete the node on which the database resides from the cluster, then, before deleting the database instance, run the following command on a node that you are not deleting to deconfigure Oracle Enterprise Manager on the node you plan to delete:

```
emca -deleteNode db
```

The Oracle Enterprise Manager Configuration Assistant prompts you for database and node information.

To delete a policy-managed database, decrease the size of the server pool in which a database instance resides. This effectively removes the instance without having to remove the Oracle RAC software from the node or the node from the cluster.

For example, you can delete a policy-managed database by running the following commands on any node in the cluster:

```
srvctl stop instance -d db_unique_name -n node_name
srvctl relocate server -n node_name -g Free
```

The first command stops on the instance on a particular node and the second command moves the node out of its current server pool and into the Free server pool.

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

1. Verify there is a current backup of OCR.
	Run the `ocrconfig -showbackup` command to ensure there is a valid backup.
2. Start DBCA.
	Start DBCA on a node other than the node that hosts the instance that you want to delete. The database and the instance that you plan to delete should continue to be started and running during this step.
3. On the DBCA Welcome page select Oracle Real Application Clusters Database, click Next, and DBCA displays the Operations page.
4. On the DBCA Operations page, select Instance Management, click Next, and DBCA displays the Instance Management page.
5. On the Instance Management page, select Delete Instance, click Next, and DBCA displays the List of Cluster Databases page.
6. Select an Oracle RAC database from which to delete an instance. Enter a user name and password for the database user that has `SYSDBA` privileges. Click Next and DBCA displays the List of Cluster Database Instances page. The List of Cluster Database Instances page shows the instances that are associated with the Oracle RAC database that you selected and the status of each instance.
7. On the List of Cluster Databases page, select the Oracle RAC database from which to delete the instance, as follows:
	1. On the List of Cluster Database Instances page, DBCA displays the instances that are associated with the Oracle RAC database that you selected and the status of each instance. Select the cluster database from which you will delete the instance. Click Finish.
		2. Click OK on the Confirmation dialog to proceed to delete the instance.
		3. Click OK on the next Confirmation dialog to delete the instance and related Optimal Flexible Architecture (OFA) directory structure.
		DBCA displays a progress dialog showing that DBCA is deleting the instance. During this operation, DBCA removes the instance and the instance's Oracle Net configuration. When DBCA completes this operation, DBCA displays a dialog asking whether you want to perform another operation.
		Click No and exit DBCA or click Yes to perform another operation. If you click Yes, then DBCA displays the Operations page.
8. Verify that the dropped instance's redo thread has been removed using SQL\*Plus to query the `V$LOG` view from an existing instance. If the redo thread is not disabled, then disable the thread. For example:
	```
	SQL> ALTER DATABASE DISABLE THREAD 2;
	```
9. Verify that the instance has been removed from OCR by running the following command, where `db_unique_name` is the name of the database:
	```
	srvctl config database -d db_unique_name
	```
10. If you are deleting more than one node, then repeat these steps to delete the instances from all the nodes that you are going to delete.

#### Using DBCA in Silent Mode to Delete Instances from Nodes

You can use DBCA in silent mode to delete a database instance from a node.

Run the following command, where the variables are the same as those shown in [Table 10-1](adddelunix.md) for the DBCA command to add an instance. Provide a node name only if you are deleting an instance from a node other than the one on where DBCA is running as shown in the following example where `password` is the SYSDBA password:

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

This procedure removes the Oracle RAC software from the node you are deleting from the cluster and updates inventories on the remaining nodes.

1. If there is a listener in the Oracle RAC home on the node you are deleting, then you must disable and stop it before deleting the Oracle RAC software. Run the following commands on any node in the cluster, specifying the name of the listener and the name of the node you are deleting:
	```
	srvctl disable listener -l listener_name -n name_of_node_to_delete
	srvctl stop listener -l listener_name -n name_of_node_to_delete
	```
2. Run the following command from `%ORACLE_HOME%\oui\bin` on the node that you are deleting to update the inventory on that node:
	```
	setup.exe -updateNodeList ORACLE_HOME=Oracle_home_location
	"CLUSTER_NODES={name_of_node_to_delete}" -local
	```
3. Depending on whether you have a shared or nonshared Oracle home, complete one of the following two procedures:
	- For a shared home, detach the node instead of deinstalling it by running the following command from the `Oracle_home` `\oui\bin` directory on each of the nodes that you want to delete:
		```
		setup.exe –detachHome ORACLE_HOME=Oracle_home
		```
		- For a nonshared home, deinstall the Oracle home from the node that you are deleting by running the following command from the `Oracle_home` `\deinstall` directory:
		```
		deinstall -local
		```
4. Run the following command from the `Oracle_home` `\oui\bin` directory on any one of the remaining nodes in the cluster to update the inventories of those nodes, specifying a comma-delimited list of remaining node names:
	```
	setup.exe -updateNodeList ORACLE_HOME=Oracle_home_location
	"CLUSTER_NODES={remaining_node_list}"
	```

### Deleting Nodes from the Cluster

After you delete the instance, you can begin the process of deleting the node from the cluster. You accomplish this by running scripts on the node you want to delete to remove the Oracle Clusterware installation and you run scripts on the remaining nodes to update the node list.

See Also:

- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD90992) for information about deleting nodes from the cluster
- [Oracle Grid Infrastructure Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm) for more information about removing Oracle Clusterware and Oracle ASM