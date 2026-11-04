---
title: Using Cloning to Extend Oracle RAC to Nodes in the Same Cluster
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/cloneracwithoui.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## 9 Using Cloning to Extend Oracle RAC to Nodes in the Same Cluster

This chapter provides information about using cloning to extend Oracle Real Application Clusters (Oracle RAC) to nodes in an existing cluster. To add Oracle RAC to nodes in a new cluster, see [Chapter 8, "Cloning Oracle RAC to Nodes in a New Cluster"](clonerac.md).

This chapter contains the following topics:

See Also:

- ["Introduction to Cloning Oracle RAC"](clonerac.md) for an overview of cloning and a discussion about the benefits of cloning
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/adddelclusterware.htm#CWADD1167) for information about adding nodes to your cluster

## About Adding Nodes Using Cloning in Oracle RAC Environments

The cloning procedures assume that you have successfully installed and configured an Oracle RAC environment to which you want to add nodes and instances. To add nodes to an Oracle RAC environment using cloning, first extend the Oracle Clusterware configuration, then extend the Oracle Database software with Oracle RAC, and then add the listeners and instances by running the Oracle assistants

The cloning script runs multiple tools, each of which may generate its own log files. After the `clone.pl` script finishes running, you can view log files to obtain more information about the cloning process. See ["Locating and Viewing Log Files Generated During Cloning"](clonerac.md) for more information.

## Cloning Local Oracle Homes on Linux and UNIX Systems

This section explains how to add nodes to existing Oracle RAC environments by cloning a local (non-shared) Oracle home in Linux and UNIX system environments.

Complete the following steps to clone Oracle Database with Oracle RAC software:

1. Follow the steps in the ["Preparing to Clone Oracle RAC"](clonerac.md) to create a copy of an Oracle home that you then use to perform the cloning procedure on one or more nodes.
2. Use the `tar` utility to create an archive of the Oracle home on the existing node and copy it to the new node. If the location of the Oracle home on the source node is `$ORACLE_HOME`, then you must use this same directory as the destination location on the new node.
3. On the new node, configure the environment variables `ORACLE_HOME` and `ORACLE_BASE`. Then go to the `$ORACLE_HOME/clone/bin` directory and run the following command where `existing_node` is the name of the node that you are cloning, `new_node2` and `new_node3` are the names of the new nodes, and `Oracle_home_name` is the name of the Oracle home:
	```
	perl clone.pl '-O"CLUSTER_NODES={existing_node,new_node2,new_node3}"'
	 '-O"LOCAL_NODE=new_node2"' ORACLE_BASE=$ORACLE_BASE ORACLE_HOME=$ORACLE_HOME
	 ORACLE_HOME_NAME=Oracle_home_name '-O-noConfig'
	```
	Note:
	If you run this command on Windows, then do not use the `-O` option.
4. Run the following command to run the configuration assistants to configure Oracle RAC on the new nodes:
	```
	$ORACLE_HOME/cfgtoollogs/configToolFailedCommands
	```
	This script contains all commands that failed, were skipped, or were cancelled during the installation. You can use this script to run the database configuration assistants outside of Oracle Universal Installer. Note that before you run the script you should check the script to see if any passwords within it need to be updated.
5. Run the following command on the existing node from the `$ORACLE_HOME/oui/bin` directory to update the inventory in the Oracle Database home with Oracle RAC, specified by `Oracle_home`, where `existing_node` is the name of the original node that you are cloning and `new_node2` and `new_node3` are the names of the new nodes:
	```
	./runInstaller -updateNodeList ORACLE_HOME=$ORACLE_HOME "CLUSTER_
	NODES={existing_node,new_node2,new_node3}"
	```
6. On each new node, go to the `$ORACLE_HOME` directory and run the following command:
	```
	./root.sh
	```
7. From the node that you cloned, run Database Configuration Assistant (DBCA) to add Oracle RAC database instances on the new nodes.

## Cloning Shared Oracle Homes on Linux and UNIX Systems

This section explains how to add nodes to existing Oracle RAC environments by cloning a shared Oracle home in Linux and UNIX system environments.

Complete the following steps to clone Oracle Database with Oracle RAC software:

1. Follow the steps in the ["Preparing to Clone Oracle RAC"](clonerac.md) to create a copy of an Oracle home that you then use to perform the cloning procedure on one or more nodes.
2. On the new node, configure the environment variables `ORACLE_HOME` and `ORACLE_BASE`. Then go to the `$ORACLE_HOME/clone/bin` directory and run the following command where `existing_node` is the name of the node that you are cloning, `new_node2` and `new_node3` are the names of the new nodes, `Oracle_home_name` is the name of the Oracle home, and the `-O-cfs` option indicates the Oracle home is shared:
	```
	perl clone.pl '-O"CLUSTER_NODES={existing_node,new_node2,new_node3}"'
	'-O"LOCAL_NODE=new_node2"' ORACLE_BASE=$ORACLE_BASE ORACLE_HOME=$ORACLE_HOME
	 ORACLE_HOME_NAME=Oracle_home_name '-O-noConfig' '-O-cfs'
	```
	Note:
	If you run this command on Windows, then do not use the `-O` option.
3. Run the following command to run the configuration assistants to configure Oracle RAC on the new nodes:
	```
	$ORACLE_HOME/cfgtoollogs/configToolFailedCommands
	```
4. Run the following command on the existing node from the `$ORACLE_HOME/oui/bin` directory to update the inventory in the Oracle Database home with Oracle RAC, specified by `Oracle_home`, where `existing_node` is the name of the original node that you are cloning and `new_node2` and `new_node3` are the names of the new nodes:
	```
	./runInstaller -updateNodeList ORACLE_HOME=$ORACLE_HOME "CLUSTER_
	NODES={existing_node,new_node2,new_node3}"
	```
5. On each new node, go to the `$ORACLE_HOME` directory and run the following command:
	```
	./root.sh
	```
6. From the node that you cloned, run Database Configuration Assistant (DBCA) to add Oracle RAC database instances to the new nodes.

## Cloning Oracle Homes on Windows Systems

This section explains how to add nodes to existing Oracle RAC environments by cloning a shared or local Oracle home in Windows system environments.

Complete the following steps to clone Oracle Database with Oracle RAC software:

1. If you have a local Oracle home, then use the ZIP utility to create an archive of the Oracle Database home with Oracle RAC on the existing node and copy it to the new node. Otherwise, proceed to the next step.
	Extract the Oracle Database with Oracle RAC home files from the ZIP file on the new node in the same directory in which the Oracle Database home with Oracle RAC resided on the existing node. For example, assume that the location of the destination Oracle RAC home on the new node is `%ORACLE_HOME%`.
2. On the new node, go to the `%ORACLE_HOME%\clone\bin` directory and run the following command where `Oracle_Home` is the Oracle Database home, `Oracle_Home_Name` is the name of the Oracle Database home, `Oracle_Base` is the Oracle base directory, `existing_node` is the name of the existing node, and `new_node` is the name of the new node:
	```
	perl clone.pl ORACLE_HOME=Oracle_Home ORACLE_BASE=Oracle_Base 
	 ORACLE_HOME_NAME=Oracle_Home_Name -O'"CLUSTER_NODES={existing_node,new_node}"'
	 -O'"LOCAL_NODE=new_node"'
	```
	Note:
	If you run this command on Windows, then do not use the `-O` option.
	If you have a shared Oracle Database home with Oracle RAC, then append the `-cfs` option to the command to indicate that the Oracle home is shared, as shown in the following example:
	```
	perl clone.pl ORACLE_HOME=Oracle_Home ORACLE_BASE=Oracle_Base 
	ORACLE_HOME_NAME=Oracle_Home_Name -O'"CLUSTER_NODES={existing_node,new_node}"'
	-O'"LOCAL_NODE=new_node"' '-O-noConfig' '-O-cfs'
	```
	Note:
	If you run this command on Windows, then do not use the `-O` option.
3. On the existing node, from the `%ORACLE_HOME%\oui\bin` directory run the following command to update the inventory in the Oracle Database home with Oracle RAC, specified by `Oracle_home`, where `existing_node` is the name of the existing node, and `new_node` is the name of the new node:
	```
	setup.exe -updateNodeList ORACLE_HOME=Oracle_home "CLUSTER_NODES={existing_node,new_node}" LOCAL_NODE=existing_node
	```
4. From the node that you cloned, run DBCA to add Oracle RAC database instances to the new nodes.