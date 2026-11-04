---
title: OLSNODES Command Reference
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/olsnodes.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## C OLSNODES Command Reference

This appendix describes the syntax and command options for the `olsnodes` command.

This appendix contains the following topics:

## Using OLSNODES

This section contains topics which relate to using the OLSNODES command.

### Overview

The `olsnodes` command provides the list of nodes and other information for all nodes participating in the cluster.

You can use this command to quickly check that your cluster is operational, and all nodes are registered as members of the cluster. This command also provides an easy method for obtaining the node numbers.

### Operational Notes

Usage Information

This command is used by the Cluster Verification Utility (CLUVFY) to obtain a list of node names when the `-n all` option is used.

This command utility is located in the `$ORA_CRS_HOME/bin` directory. You can only use this command if the CRS daemon is started.

Privileges and Security

You can run this command as either the `root` user, the user that installed Oracle Clusterware, or the user that installed Oracle Database.

## Summary of the OLSNODES Command

The `olsnodes` command does not use keywords, but accepts one or more options. The available options are described in Table C-1.

Syntax

```
olsnodes [[-n] [-i] [-s] [-t] [node_name | -l [-p]] | [-c]] [-g] [-v]
```

If you issue the `olsnodes` command without any command parameters, the command returns a listing of the nodes in the cluster:

```
[root@node1]# olsnodes
node1
node2
node3
node4
```

Table C-1 OLSNODES Command Options

| Command | Description |
| --- | --- |
| `-n` | Lists all nodes participating in the cluster and includes the assigned node numbers. |
| `-i` | Lists all nodes participating in the cluster and includes the Virtual Internet Protocol (VIP) address assigned to each node. |
| `-s` | Displays the status of the node: `active` or `inactive`. |
| `-t` | Displays node type: pinned or unpinned. |
| `node_name` | Displays information for a particular node. |
| `-l [-p]` | Lists the local node and includes the private interconnect for the local node. The `-p` option is only valid when you specify along with the `-l` option. |
| `-c` | Displays the name of the cluster. |
| `-g` | Logs cluster verification information with more details. |
| `-v` | Logs cluster verification information in verbose mode. Use in debug mode and only at the direction of My Oracle Support. |

Usage Notes

Examples

Include here the most common uses of this command. For example:

Example 1: List the VIP addresses for all nodes currently in the cluster

To list the VIP addresses for each node that is currently a member of the cluster, use the command:

```
[root@node1]# olsnodes -i
node1    168.92.1.1
node2   168.192.2.1
node3   168.192.3.1
node4   168.192.4.1
```

Example 2: List the node names and node numbers for cluster members

To list the node name and the node number for each node in the cluster, use the command:

```
[root@node1]# olsnodes -n
node1    1
node2    2
node3    3
node4    4
```