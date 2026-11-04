---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asmcmd-cluster-commands.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

This topic provides a summary of the ASMCMD client cluster management commands that are used with Oracle ASM remote instances.

Unless otherwise specified, the ASMCMD cluster management commands should be executed in the Oracle ASM-CSS cluster.

For information about Oracle Flex ASM, refer to " [Managing Oracle Flex ASM](manage-flex-asm.md) ".

Table 10-38 lists the ASMCMD client cluster management commands with brief descriptions.

Table 10-38 Summary of ASMCMD client cluster management commands

| Command | Description |
| --- | --- |
| chcc | Modifies a configuration for a client cluster. |
| mkcc | Creates a configuration for a client cluster. |
| lscc | Lists the configured client clusters. |
| rmcc | Removes the configuration for a client cluster. |

See Also:

- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about installing clusters and cluster name requirements
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD-GUID-6BA197F8-44D4-4663-8191-1CB24EF5F117) for information about client clusters

### chcc

Purpose

Modifies the configuration for a client cluster.

Syntax and Description

```
chcc cluster_name [--direct | --indirect]
     [--version client_cluster_version]
```

The following table lists the options for the `chcc` command.

Table 10-39 Options for the chcc command

| Option | Description |
| --- | --- |
| `cluster_name` | Specifies the name of the client cluster. |
| `--direct` | Specifies direct storage access. |
| `--indirect` | Specifies indirect storage access. |
| `--version` `client_cluster_version` | Specifies the five digit client cluster version if it is different than the storage server version. The storage server version is used if not specified. |

To modify the storage access method of a client cluster, you perform the following steps.

1. As the Oracle Grid Infrastructure user at the Domain Services Cluster (DSC), change the client cluster storage access configuration with the `chcc` command.
2. As the Oracle Grid Infrastructure user at the Domain Services Cluster (DSC), export the client cluster configuration into a new cluster manifest file with the `mkcc` command.
	You can ignore the warning messages reported when the `mkcc` command is issued.
3. After you have exported the new cluster manifest file, as the root user on the nodes of client cluster you copy the new cluster manifest file to the nodes with the `rootcrs.sh` script.

Examples

The following examples show how to modify the storage access method from direct to indirect Oracle ASM storage for the client cluster `—–asm` and `––gimr` components.

Example 10-48 Using the ASMCMD chcc command

As the Oracle Grid Infrastructure user at the Domain Services Cluster (DSC), run the following commands:

```
$ asmcmd chcc clientCluster1 --indirect

$ asmcmd mkcc clientCluster1 /export/cluster_manifest_new.xml --asm --gimr
```

As the root user at the client cluster, copy the new cluster manifest file to the client cluster with the following commands.

1. Run the `rootcrs.sh` script on every node in the client cluster.
	```
	# rootcrs.sh --convertcluster STORAGE_ACCESS -manifestfile cluster_manifest_new.xml
	```
2. Run the `rootcrs.sh` script with the `-lastnode` option on last node in the client cluster.
	```
	# rootcrs.sh --convertcluster STORAGE_ACCESS -manifestfile cluster_manifest_new.xml -lastnode
	```

### lscc

Purpose

Lists the configured client clusters.

Syntax and Description

```
lscc [--suppressheader] [-l] [cluster_name | --file wrap]
```

The following table lists the options for the `lscc` command.

Table 10-40 Options for the lscc command

| Option | Description |
| --- | --- |
| `–suppressheader` | Suppresses column headings from the output. |
| `-l` | Displays all details. |
| `cluster_name` | Specifies the name of the client cluster. |
| `--file` | Displays information about the contents of the cluster manifest file. |
| `wrap` | Specifies the full path of the XML file to export the credentials. |

Examples

The following example lists the configured client clusters.

Example 10-49 Using the ASMCMD lscc command

```
ASMCMD [+] > lscc
--------------------------------------------------------------------------------
           NAME        VERSION GUID
================================================================================
 clientCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4
 clientCluster2     12.2.0.0.0 3de3bbd75e9a7f17bfe027b477b5bcae
================================================================================

ASMCMD [+] > lscc -l
--------------------------------------------------------------------------------
           NAME        VERSION GUID                             ASM GIMR TFA ACFS RHP
=====================================================================================   
 clientCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4 YES  YES YES  YES YES
 clientCluster2     12.2.0.0.0 3de3bbd75e9a7f17bfe027b477b5bcae YES  YES YES  YES  NO
=====================================================================================

ASMCMD [+] > lscc clientCluster1 --suppressheader
 clientCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4

ASMCMD [+] > lscc clientCluster1 --suppressheader -l
 clientCluster1     12.2.0.0.0 78015b1e78756f88bf119fd8e5146df4 ASM,GIMR,TFA,ACFS,RHP
```

### mkcc

Purpose

Creates the configuration for a client cluster.

Syntax and Description

```
mkcc cluster_name manifest_file [--direct]
     [--version client_cluster_version]
     [--guid client_cluster_guid]
     [--gimr gimr_pdb/export_dir]
     [--asm] [--gimr] [--rhp] [--acfs] [--tfa]
```

The following table lists the options for the `mkcc` command.

Table 10-41 Options for the mkcc command

| Option | Description |
| --- | --- |
| `cluster_name` | Specifies the name of the client cluster. |
| `manifest_file` | Specifies the full path of the XML file to export the credentials. |
| `--direct` | Specifies direct storage access. If not specified, the storage access is indirect. |
| `--version` `client_cluster_version` | Specifies the five digit client cluster version if it is different than the storage server version. The storage server version is used if not specified. |
| `--guid` `client_cluster_guid` | Specifies the 32-character, globally unique identifier for the client cluster. When this option is specified, `mkcc` does not generate a new GUID. If there is a cluster already configured with the specified GUID, then the command fails. |
| `--gimr` `gimr_pdb/export_dir` | Specifies the directory from which to import the GIMR PDB when converting a standalone cluster to a client cluster. |
| `--asm` | Generate credentials and configuration for an Oracle ASM cluster. |
| `–-gimr` | Generate credentials and configuration for an Oracle GIMR cluster. |
| `–-rhp` | Generate credentials and configuration for an Oracle RHP cluster. |
| `–-acfs` | Generate credentials and configuration for an Oracle ACFS cluster. |
| `--tfa` | Generate credentials and configuration for an Oracle TFA cluster. |

The client cluster name must conform to the same rules as a cluster name. The name must be unique across your enterprise, must be at least one character long and no more than 15 characters in length, must be alphanumeric, cannot begin with a numeral, and may contain hyphens (-). Underscore characters (\_) are not allowed.

If no client cluster component options are specified, the default is to configure all of the components and store their credentials in the same manifest file.

GNS credentials are not generated by the `asmcmd` `mkcc` command. To configure the client cluster as a GNS Client, run the following command as a privileged user to export the GNS instance client data configuration to the cluster manifest file:

```
srvctl export gns -clientdata manifest_file -role CLIENT
```

Examples

The following example creates credentials for the client cluster `—–asm` and `––gimr` components and exports the credentials to a cluster manifest file.

Example 10-50 Using the ASMCMD mkcc command

```
ASMCMD [+] > mkcc clientCluster1 /tmp/client_cluster1.xml --version 12.2.0.0.0 --asm --gimr
```

### rmcc

Purpose

Removes the configuration for a client cluster.

Syntax and Description

```
rmcc cluster_name [-f]
```

The following table lists the options for the `rmcc` command.

Table 10-42 Options for the rmcc command

| Option | Description |
| --- | --- |
| `cluster_name` | Specifies the name of the client cluster. |
| `-f` | Specifies to force the removal of client cluster credentials. |

Examples

The following example removes the configuration for a client cluster.

Example 10-51 Using the ASMCMD rmcc command

```
ASMCMD [+] > rmcc clientCluster1
```