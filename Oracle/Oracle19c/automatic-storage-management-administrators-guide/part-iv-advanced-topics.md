---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iv-advanced-topics.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Part IV Advanced Topics Page

This part introduces advanced Oracle storage and cluster administration topics, including Oracle ACFS concepts and snapshot-based replication, Oracle Flex ASM management, Oracle ASM Filter Driver administration, and creating database files in Oracle ASM with SQL\*Plus.

Read More: Part IV Advanced Topics Page

## Understanding Oracle ACFS Advanced Topics

Oracle ACFS advanced administration covers storage and file-count limits, ADVM volume configuration, error recovery, NFS export requirements, loopback devices, driver and resource management, Oracle Restart limitations, diagnostic commands, plug-in and tagging APIs, and I/O failure troubleshooting. ACFS supports extensive mount, file, directory, and capacity limits governed partly by platform and ASM compatibility; failures require controlled dismount, synchronization, remount, or file-system checking procedures. The guidance explains cloning databases and PDBs efficiently with ACFS snapshots, including control-file, parameter, redo, tempfile, RAC, CRS, and service configuration, and provides NFS tuning recommendations such as dNFS mounts, writer-batch adjustment, increased NFSD processes, and required patches. It also documents driver commands for loading and inspecting ACFS, ADVM, and OKS drivers; Grid Infrastructure resource behavior; Oracle Restart alternatives using manual driver and filesystem management; plug-in metrics and file-ID APIs; tag naming, retrieval, listing, setting, and removal interfaces; and support-oriented diagnostics including filesystem debugging, state dumps, tracing open-file references, lock statistics, logging, metadata capture, and tuning.

Read More: [Understanding Oracle ACFS Advanced Topics](understanding-oracle-acfs-advanced-topics.md)

## Understanding Oracle ACFS Advanced Topics

This page presents advanced Oracle ACFS diagnostics and administration, including lock-statistics reporting, memory and persistent logging, metadata collection and expansion, ACFS and ADVM tuning, I/O failure interpretation, and Grid Infrastructure patch management. It emphasizes privileged access, cautious use of diagnostic options, preserving metadata for support analysis, and verifying that active system drivers match the patched Grid Infrastructure software.

Read More: [Understanding Oracle ACFS Advanced Topics](understanding-oracle-acfs-advanced-topics.md)

## acfsutil log

The `acfsutil log` command retrieves memory diagnostic logs and controls debugging for Oracle ADVM, ACFS, and Oracle Kernel Services. It can query or change log sizes and debug levels, target specific file systems, dump logs across cluster nodes, collect Hang Manager information, and temporarily raise diagnostics with `-o`; logs default to `oks.log`, and execution requires root or Oracle ASM administrator privileges.

Read More: [acfsutil log](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/acfsutil%20log)

## acfsutil meta

The `acfsutil meta` command collects Oracle ACFS metadata into a transferable record-oriented file for diagnostics, optionally using quick scanning, known-good metadata collection, online checking, Copy-on-Write storage, extent offsets, or an accelerator device. For reliable results, the file system should preferably be unmounted or left unmodified, output must be stored outside the source ACFS device, and large outputs may be compressed; collected files can later be expanded into sparse files for `fsck` or `acfschkdsk` analysis.

Read More: [acfsutil meta](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/acfsutil%20meta)

## acfsutil plogconfig

The `acfsutil plogconfig` command configures Oracle ACFS persistent diagnostic logging, including its directory, buffer size, timer interval, watermarks, maximum file size, and file count, and can query or terminate logging. It is intended for Oracle Support-directed diagnostics, requires root or Oracle ASM administrator privileges, and should be used only when configuration changes are specifically requested.

Read More: [acfsutil plogconfig](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/acfsutil%20plogconfig)

## acfsutil tune

The `acfsutil tune` command displays all ACFS tunable parameters, queries an individual parameter, or persistently changes a parameter on the local node. Changes take effect immediately and survive restarts, require root or Windows Administrator privileges, and may be used to adjust parameters such as maximum open or cached files and Hang Manager timing, although normal defaults should generally be retained unless performance or support requirements justify modification.

Read More: [acfsutil tune](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/acfsutil%20tune)

## advmutil tune

The `advmutil tune` command displays all Oracle ADVM parameter values, queries a selected parameter, or sets a new value for a privileged user. Parameters such as `deadlock_timer`, `resilver_power`, and `resilver_regio` affect ADVM behavior and should be changed cautiously, generally under Oracle Support guidance.

Read More: [advmutil tune](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/advmutil%20tune)

## Understanding Oracle ACFS I/O Failure Console Messages

Oracle ACFS reports I/O failures in the operating system event log using a structured message containing the error code, device, operation and transfer type, file entry, offset, length, impact scope, object type, operational context, snapshot status, object identifier, and internal code location. The file entry can be mapped to a file name with `acfsutil info fileid`, while internal context and code-location fields primarily support Oracle troubleshooting of hardware, device, metadata, and data-access failures.

Read More: [Understanding Oracle ACFS I/O Failure Console Messages](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/Understanding%20Oracle%20ACFS%20I/O%20Failure%20Console%20Messages)

## Oracle Patching and Oracle ACFS

Oracle ACFS is delivered with Oracle Grid Infrastructure and patched through OUI and OPatch along with Grid software. Standard patching updates the Grid home, system locations, and loaded drivers during controlled Clusterware restarts, whereas Zero Downtime Grid Infrastructure Patching initially updates only Grid-home content, leaving ACFS system components at their previous active version until they are explicitly loaded or the node reboots with a kernel change; active and available versions should therefore be checked across all nodes.

Read More: [Oracle Patching and Oracle ACFS](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/Oracle%20Patching%20and%20Oracle%20ACFS)

## Overview of Oracle ACFS Patching

Oracle ACFS components reside both in the Grid Infrastructure home and operating-system locations, so patch behavior depends on whether Zero Downtime Grid Infrastructure Patching is used. Standard procedures synchronize and load updated drivers during node-level Clusterware downtime, while zero-downtime procedures can leave active ACFS drivers and tools older than the newly patched Grid-home software; `crsctl query driver` and `acfsdriverstate version -v` identify the active, available, and local-node versions.

Read More: [Overview of Oracle ACFS Patching](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/Overview%20of%20Oracle%20ACFS%20Patching)

## Updating Oracle Grid Infrastructure Files

To load updated ACFS fixes into memory and install corresponding system tools, stop Clusterware on each node, run the Grid Infrastructure `rootcrs.sh -updateosfiles` procedure, and restart Clusterware with waiting enabled. A coordinated kernel-version reboot can perform the update automatically; afterward, active and available driver versions should match, confirming that the system is running the latest Grid-home software.

Read More: [Updating Oracle Grid Infrastructure Files](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/Updating%20Oracle%20Grid%20Infrastructure%20Files)

## Verifying Oracle ACFS Patching

Patch verification requires comparing OPatch inventory with the active and available ACFS driver versions reported by `crsctl query driver activeversion -all`, `crsctl query driver softwareversion -all`, and the local `acfsdriverstate version` command. With standard patching, these versions should agree; after zero-downtime patching, differences indicate that updated ACFS system software remains staged in the Grid home and has not yet been installed or loaded.

Read More: [Verifying Oracle ACFS Patching](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20IV%20Advanced%20Topics/19c/Verifying%20Oracle%20ACFS%20Patching)

## Configuring Oracle ACFS Snapshot-Based Replication

Oracle ACFS snapshot-based replication, available from release 12.2, transfers differences between successive primary snapshots to a standby cluster over SSH, replacing the pre-12.2 continuous replication model. Configuration requires passwordless, bidirectional SSH trust between replication nodes, including appropriate user public keys, remote host keys, permissions, and optional VIP entries in known-hosts files. The acfsreplssh assistant can configure, verify, or remove keys, while manual procedures are also provided, including validation with acfsutil repl info. Windows deployments require supported Cygwin and SSH configuration, suitable domain-based replication users, correct service and file settings, and testing. Upgrades from earlier replication require Flex ASM and password-file preparation, Grid Infrastructure upgrades on both clusters, COMPATIBLE.ADVM set to 12.2, and either reinitialization or the staged acfsutil repl upgrade process; once started, the upgrade cannot be rolled back.

Read More: [Configuring Oracle ACFS Snapshot-Based Replication](configuring-oracle-acfs-snapshot-based-replication.md)

## Managing Oracle Flex ASM

Oracle Flex ASM allows ASM instances to run separately from database servers, consolidating storage management while supporting local clients, remote clients with direct disk access, ACFS and ADVM through ASM proxy instances, and member-cluster access through Oracle IOServer. Flex ASM setup requires selecting dedicated, nonpublic ASM networks, for which ASM listeners are created automatically. Administration uses ASMCA, ASMCMD, CRSCTL, SQL\*Plus, and SRVCTL to inspect Flex ASM status and client connections, set ASM instance cardinality, relocate clients, manage ASM networks and listeners, configure network dependency behavior, and administer member clusters. The INSTANCE\_TYPE parameter identifies ASM proxy instances, while existing initialization parameters should be reviewed for the deployment.

Read More: [Managing Oracle Flex ASM](managing-oracle-flex-asm.md)

## Administering Oracle ASM Filter Driver

Oracle ASM Filter Driver (ASMFD) is a kernel module that validates ASM disk I/O, blocks non-Oracle writes, and provides persistent disk management without rebinding devices after restarts. This page covers configuring ASMFD during or after Grid Infrastructure installation in clustered and standalone environments, including migration from ASMLIB, disk labeling and scanning, discovery-string management through AFD\_DISKSTRING and ASM\_DISKSTRING, status verification, and deconfiguration procedures. It also documents migration workflows for disk groups with or without OCR and voting files, cautions against manually altering ASM disks, explains platform and partition-table considerations, and describes the afdload and afddriverstate utilities for loading, unloading, and inspecting the driver.

Read More: [Administering Oracle ASM Filter Driver](administering-oracle-asm-filter-driver.md)

## Creating Database Files in Oracle ASM Using SQLPlus

Oracle ASM allows SQL\*Plus to create and manage database files with minimal file-system configuration, typically using disk groups through initialization parameters and ASM-managed file naming. The page explains creating databases with data, recovery, control, undo, and redo files; creating permanent and temporary tablespaces with configurable size and autoextend behavior; multiplexing redo logs across disk groups; specifying ASM control files and handling file references differently with NORESETLOGS and RESETLOGS; and placing archived redo logs or recovery files in ASM disk groups using LOG\_ARCHIVE\_DEST, LOG\_ARCHIVE\_DEST\_n, and DB\_RECOVERY\_FILE\_DEST.

Read More: [Creating Database Files in Oracle ASM Using SQLPlus](creating-database-files-in-oracle-asm-using-sqlplus.md)