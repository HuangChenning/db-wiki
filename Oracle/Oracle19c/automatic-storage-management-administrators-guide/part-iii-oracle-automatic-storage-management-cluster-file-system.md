---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iii-oracle-automatic-storage-management-cluster-file-system.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Part III Oracle Automatic Storage Management Cluster File System

Part III discusses Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM), in the following chapters:

## Introducing Oracle ACFS and Oracle ADVM

Oracle ACFS is a scalable, POSIX-compliant, general-purpose clustered file system integrated with Oracle ASM, Oracle ADVM, and Oracle Clusterware for managing database and application files across standalone and clustered environments. It provides dynamic resizing, ASM-based striping, mirroring, load distribution, snapshots, sparse files, high availability, shared namespaces, native API and operating-system access, NAS protocols, and support for large files and directories. Oracle ADVM presents ASM-backed dynamic volumes through standard operating-system block-device interfaces, enabling ACFS and other applications to use ASM storage. ACFS concepts include hierarchical namespaces, clusterwide or node-local mounts, driver-based operation, persistent mount registry management, database-file and database-home support, ASM integration, online backup through snapshots, and optional remote service for member clusters. Administration uses ASMCA, SRVCTL, ASMCMD, SQL\*Plus, and ACFS command-line tools, with Clusterware resources controlling drivers, volumes, mounts, dependencies, monitoring, and recovery. Compatibility attributes determine availability of capabilities such as snapshots, encryption, replication, compression, automatic resizing, sparse files, accelerator volumes, 4K sectors, snapshot duplication, and database storage. Security and encryption provide layered access controls and data-at-rest protection, although several features—including ACFS on Windows, Vault security, auditing, member-cluster remote service, and some encryption platforms—are deprecated or desupported in applicable releases. Proper privileges, resource dependencies, performance settings, controlled shutdown procedures, and platform-specific restrictions are required for reliable operation.

Read More: [Introducing Oracle ACFS and Oracle ADVM](introducing-oracle-acfs-and-oracle-advm.md)

## Introducing Oracle ACFS and Oracle ADVM

Oracle ACFS provides enterprise file-system capabilities including asynchronous compression for general-purpose files, auditing, snapshot-based replication, tagging, security, encryption, plugins, and accelerated metadata storage; feature availability depends on platform, release, and ASM/ADVM compatibility settings. Auditing records file access, privilege use, and command results in per-file-system trails with separated manager and auditor responsibilities, although ACFS Security and Auditing are deprecated from 19c. Replication asynchronously transfers snapshot contents and changes from a primary to one standby, supports tagging, role reversal, failover, SSH authentication, and integration with auditing, encryption, and security, but requires careful capacity, identity, compatibility, and wallet configuration. Accelerator volumes improve metadata performance when placed on faster storage, while ACFS NAS/MAX supplies highly available NFS and SMB services through Oracle Clusterware and virtual IPs, with platform and locking restrictions. ACFS remote service provides iSCSI-based storage access for supported member clusters from a Domain Services Cluster, requiring isolated transports, repositories, exports, appropriate performance capacity, and dedicated Clusterware resources; this feature and member clusters are deprecated. Oracle ADVM supplies dynamically managed virtual block devices backed by ASM volumes, enabling ACFS and other non-database file systems and applications, with volumes created and resized on demand when ASM and ADVM compatibility is at least 11.2.

Read More: [Introducing Oracle ACFS and Oracle ADVM](introducing-oracle-acfs-and-oracle-advm.md)

## Using Views to Display Oracle ACFS Information

Oracle ACFS and Oracle ADVM dynamic performance views provide information about file systems, volumes, encryption, security administrators, rules, rulesets, realms, snapshots, tags, replication, availability, capacity, and volume statistics. These views are accessible from the Oracle ASM instance, or from an ASM proxy instance in Flex ASM configurations, with Windows space values treated as approximate. Oracle ACFS also supports selected Oracle Database file-mapping views—V$MAP\_FILE, V$MAP\_FILE\_EXTENT, V$MAP\_ELEMENT, and V$MAP\_FILE\_IO\_STACK—after FILE\_MAPPING is enabled and DBMS\_STORAGE\_MAP.MAP\_ALL is executed; mapping is unavailable on Windows and V$MAP\_SUBELEMENT is unsupported.

Read More: [Using Views to Display Oracle ACFS Information](using-views-to-display-oracle-acfs-information.md)

## Administering Oracle ACFS with Oracle Enterprise Manager

Oracle Enterprise Manager Cloud Control provides GUI-based administration and monitoring for Oracle ACFS file systems, Oracle ADVM volumes, snapshots, security, encryption, and tagging, using the Oracle ASM home page and an ASM proxy instance when Flex ASM is configured. Administrators can create, mount, dismount, resize, delete, register, and inspect volumes and file systems; create and manage read-only, read-write, and child snapshots; initialize and configure security and encryption; manage administrators, rules, rulesets, and realms; and add, remove, or search file tags. Operations requiring host-level changes may generate commands and require root, administrator, or other appropriate credentials.

Read More: [Administering Oracle ACFS with Oracle Enterprise Manager](administering-oracle-acfs-with-oracle-enterprise-manager.md)

## Managing Oracle ACFS and Oracle ADVM With ASMCA

Oracle ASM Configuration Assistant supports GUI and command-line management of Oracle ADVM volumes and Oracle ACFS file systems, including creation, enabling, disabling, resizing, deletion, mounting, snapshots, security, encryption, and database-oriented file systems. Disk groups require appropriate ASM and ADVM compatibility attributes, and database file systems should use ASMCMD or SQL volume creation to preserve column striping of one. ASMCA can generate privileged operating-system commands, supports Windows administrator requirements, and provides silent commands for creating or deleting snapshots, creating volumes, and creating ACFS file systems; the command-line file-system creation operation does not mount the resulting file system.

Read More: [Managing Oracle ACFS and Oracle ADVM With ASMCA](managing-oracle-acfs-and-oracle-advm-with-asmca.md)

## Managing Oracle ADVM with ASMCMD

ASMCMD provides Oracle ADVM volume-management commands for creating, deleting, enabling, disabling, inspecting, resizing, configuring, and monitoring volumes in mounted ASM disk groups. The local ASM instance must be running, and required disk groups must be mounted. Key commands include `volcreate`, which defines volume size, striping, redundancy, and placement; `voldelete`, which removes volumes after associated file systems are stopped; `voldisable` and `volenable`, which control device availability; `volinfo`, which displays volume metadata and device details; `volresize`, which changes volume size but requires `acfsutil size` for ACFS volumes; `volset`, which manages usage and mount-path metadata; and `volstat`, which reports I/O counters and errors. Volumes are enabled automatically upon creation, have platform-specific naming and length restrictions, and should generally use disk-group redundancy; unprotected volumes are not recommended for production because storage failures can cause data loss. Active file systems must be dismounted before disabling, deleting, or certain resizing operations.

Read More: [Managing Oracle ADVM with ASMCMD](managing-oracle-advm-with-asmcmd.md)

## Managing Oracle ACFS with Command-Line Tools

Oracle ACFS and ADVM are managed through ASMCMD, SRVCTL, SQL\*Plus, ASMCA, operating-system commands, and acfsutil, with platform-specific support for Linux, Solaris, AIX, and Windows. Core workflows include creating ADVM volumes and ACFS file systems, registering, mounting, validating, accessing them across cluster nodes, and safely dismounting or removing them. The documentation also covers acfsutil privileges, help, version and trace-file management; snapshots; security realms, rules, administrators, auditing, and metadata backups; encryption and key management; extended-attribute tagging; snapshot-based replication with SSH, standby configuration, monitoring, pausing, resuming, failover, and capacity planning; and compression, cluster-domain operations, and command utilities. Linux guidance includes ACFS-specific mount options and offline or online fsck, while AIX guidance details mkfs, mount, and umount syntax, compatibility requirements, metadata block sizes, security options, and operational constraints. Disk-group compatibility, appropriate administrative privileges, consistent cluster mount points, and careful handling of encryption keys, snapshots, replication storage, and repair operations are essential throughout.

Read More: [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md)

## Managing Oracle ACFS with Command-Line Tools

Oracle ACFS file systems can be dismounted with the Solaris `umount` command by specifying either the Oracle ADVM volume device, such as `/dev/asm/volume1-123`, or the mounted file-system path, such as `/acfsmounts/acfs1`.

Read More: [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md)

## Oracle ACFS Command-Line Tools for the Solaris Environment

This topic summarizes Solaris-specific Oracle ACFS commands: `fsck` checks and repairs file systems, `mkfs` creates them, `mount` attaches them, and `umount` or `umountall` detaches them. Solaris extends these commands with ACFS options; forcibly dismounted disk groups may leave ADVM device files until the disk group is remounted.

Read More: [Oracle ACFS Command-Line Tools for the Solaris Environment](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20the%20Solaris%20Environment)

## fsck

On Solaris, `fsck -F acfs` checks a dismounted Oracle ACFS file system and requires root privileges and a loaded ACFS driver. It reports errors by default, while `-o a` repairs them; `-n` or `-y` suppresses prompts, and verbose, force, and help options are available. Temporary working files may be created during checking, and unrecoverable objects are placed in `/lost+found` with identifier-based names.

Read More: [fsck](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/fsck)

## mkfs

Solaris `mkfs -F acfs` creates an Oracle ACFS file system on an ADVM volume without requiring root privileges, provided the user owns the device. Options support forced formatting, naming, verbose output, metadata block sizes of 512 or 4096 bytes, sizing, and release compatibility. Minimum sizes are 200 MB for 512-byte metadata and 512 MB for 4 KB metadata; compatibility and sector-size requirements govern 4 KB formatting.

Read More: [mkfs](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/mkfs)

## mount

Solaris `mount -F acfs` attaches a formatted Oracle ACFS volume to an existing directory, requires root privileges, and supports read-only/read-write, device, execution, set-ID, verbose, and automatic mounting of registered file systems. A file system should use one consistent mount point across cluster members, and the `all` option mounts registered file systems whose automatic-start setting is enabled.

Read More: [mount](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/mount)

## umount/umountall

Solaris `umount` detaches an Oracle ACFS file system specified by its mount point or ADVM volume device, while `umountall -F acfs` detaches all ACFS file systems on the current node. Both commands require root privileges, wait for completion, and fail if a file system is busy; `-V` can validate an `umount` command line without executing it.

Read More: [umount/umountall](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/umount/umountall)

## fsck

On AIX, `fsck -V acfs` checks and repairs a dismounted Oracle ACFS file system using an ADVM volume device. Root privileges and a loaded ACFS driver are required; checking is the default, while `-o a` repairs errors, `-n` and `-y` answer prompts automatically, and force and verbose modes are available. Temporary files support the operation, and unrecoverable objects may be placed in `/lost+found`.

Read More: [fsck](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/fsck)

## umount/umountall

AIX `umount` detaches an Oracle ACFS file system by mount point or ADVM volume device, and `umountall -F acfs` detaches all ACFS file systems on the current node. The commands require root privileges, wait until dismounting completes, and fail when the target file system is busy.

Read More: [umount/umountall](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/umount/umountall)

## Oracle ACFS Command-Line Tools for the AIX Environment

This topic summarizes AIX Oracle ACFS commands and explains the `oracle_devmgmt` security role, which authorizes ACFS and ADVM device configuration, removal, and definition. The role is assigned to the Grid Infrastructure and ASM administrators; users may need to activate it with `swrole` or open a new shell. AIX force-dismounted disk groups can leave ADVM device files until remounting.

Read More: [Oracle ACFS Command-Line Tools for the AIX Environment](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20the%20AIX%20Environment)

## fsck

On AIX, `fsck -V acfs` checks and repairs a dismounted Oracle ACFS file system using an ADVM volume device. Root privileges and a loaded ACFS driver are required; checking is the default, while `-o a` repairs errors, `-n` and `-y` answer prompts automatically, and force and verbose modes are available. Temporary files support the operation, and unrecoverable objects may be placed in `/lost+found`.

Read More: [fsck](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/fsck)

## mkfs

AIX `mkfs -V acfs` creates the on-disk structure for an Oracle ACFS file system on an ADVM device without inherently requiring root privileges. It supports naming, sizing, forced formatting, verbose output, 512- or 4096-byte metadata blocks, and release compatibility. The minimum sizes, compatibility rules, driver requirement, and 4 KB sector behavior parallel Solaris ACFS formatting.

Read More: [mkfs](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/mkfs)

## mount

AIX `mount -v acfs` attaches a formatted Oracle ACFS volume to an existing directory and requires root privileges. It supports read-only/read-write, security-related, device, verbose, and automatic mounting options; the `all` option mounts registered file systems configured for automatic startup. Mount points should be unique per file system and consistent across cluster members.

Read More: [mount](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/mount)

## umount/umountall

AIX `umount` detaches an Oracle ACFS file system using its mount point or ADVM volume device, while `umountall -F acfs` detaches all ACFS file systems on the current node. Root privileges are required, commands wait for complete dismounting, and busy file systems cause failure.

Read More: [umount/umountall](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/umount/umountall)

## Oracle ACFS Command-Line Tools for the AIX Environment

This topic summarizes AIX Oracle ACFS commands and explains the `oracle_devmgmt` security role, which authorizes ACFS and ADVM device configuration, removal, and definition. The role is assigned to the Grid Infrastructure and ASM administrators; users may need to activate it with `swrole` or open a new shell. AIX force-dismounted disk groups can leave ADVM device files until remounting.

Read More: [Oracle ACFS Command-Line Tools for the AIX Environment](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20the%20AIX%20Environment)

## fsck

On AIX, `fsck -V acfs` checks and repairs a dismounted Oracle ACFS file system using an ADVM volume device. Root privileges and a loaded ACFS driver are required; checking is the default, while `-o a` repairs errors, `-n` and `-y` answer prompts automatically, and force and verbose modes are available. Temporary files support the operation, and unrecoverable objects may be placed in `/lost+found`.

Read More: [fsck](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/fsck)

## mkfs

AIX `mkfs -V acfs` creates the on-disk structure for an Oracle ACFS file system on an ADVM device without inherently requiring root privileges. It supports naming, sizing, forced formatting, verbose output, 512- or 4096-byte metadata blocks, and release compatibility. The minimum sizes, compatibility rules, driver requirement, and 4 KB sector behavior parallel Solaris ACFS formatting.

Read More: [mkfs](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/mkfs)

## mount

AIX `mount -v acfs` attaches a formatted Oracle ACFS volume to an existing directory and requires root privileges. It supports read-only/read-write, security-related, device, verbose, and automatic mounting options; the `all` option mounts registered file systems configured for automatic startup. Mount points should be unique per file system and consistent across cluster members.

Read More: [mount](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/mount)

## umount/umountall

AIX `umount` detaches an Oracle ACFS file system using its mount point or ADVM volume device, while `umountall -F acfs` detaches all ACFS file systems on the current node. Root privileges are required, commands wait for complete dismounting, and busy file systems cause failure.

Read More: [umount/umountall](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/umount/umountall)

## Oracle ACFS Command-Line Tools for Windows Environments

This topic lists Windows commands for checking, formatting, mounting, dismounting, and detaching Oracle ACFS, along with `advmutil` commands for non-ACFS file systems on ADVM volumes. Oracle ACFS on Windows is deprecated beginning with ACFS 19c 19.5 and may be removed in a future release; migration options include ASM, DBFS, or Windows shares.

Read More: [Oracle ACFS Command-Line Tools for Windows Environments](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20Windows%20Environments)

## acfschkdsk

Windows `acfschkdsk` checks and repairs an Oracle ACFS file system that has been dismounted clusterwide. It requires the ACFS driver and normally ensures exclusive access; `/a` repairs errors, `/n` or `/y` handles prompts, `/f` forces mountable state, and `/v` enables progress reporting. Working files are temporary, and unrecoverable objects are placed in `\lost+found`, accessible only to Administrators.

Read More: [acfschkdsk](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfschkdsk)

## acfsdismount

Windows `acfsdismount` removes the namespace attachment and dismounts an Oracle ACFS file system by drive letter, full mount path, or `/all` for every file system on the node. Administrator privileges are required, verbose output is available, and open references from applications such as scanners or management tools can prevent dismounting.

Read More: [acfsdismount](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsdismount)

## acfsformat

Windows `acfsformat` quickly creates the on-disk structure required for an Oracle ACFS file system and requires Administrator privileges and a loaded ACFS driver. It supports verbose output, forced formatting, file-system labels, 512- or 4096-byte metadata blocks, selected device capacity, and release compatibility, subject to minimum-size, sector, and compatibility constraints.

Read More: [acfsformat](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsformat)

## acfsmountvol

Windows `acfsmountvol` mounts a formatted Oracle ACFS volume to a drive letter or empty directory, can mount all registry-defined file systems, and lists mounted file systems when invoked without arguments. Administrator privileges are required; mount points may be nested but each file system should use only one consistent mount point across cluster members.

Read More: [acfsmountvol](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsmountvol)

## acfsutil detach

Windows `acfsutil detach` unregisters Oracle ACFS as a base file system and removes driver device objects so the ACFS driver can be unloaded after all volumes are dismounted. Only the Windows Administrator can run it, and Oracle shutdown scripts invoke it automatically.

Read More: [acfsutil detach](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20detach)

## advmutil dismount

Windows `advmutil dismount` removes access to non-ACFS file systems on Oracle ADVM volumes by drive letter, directory, all registered volumes, or a specified disk group. The optional `/unregister` removes the device and drive-letter registration from the system registry. ASM must be running with the required disk groups mounted and volumes enabled.

Read More: [advmutil dismount](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20dismount)

## advmutil list

Windows `advmutil list /registry` displays registered non-ACFS ADVM volume devices and their associated drive letters from the system registry. The local ASM instance must be running, required disk groups must be mounted, and volumes must be enabled.

Read More: [advmutil list](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20list)

## advmutil mount

Windows `advmutil mount` exposes non-ACFS ADVM volumes through a drive letter or directory, optionally registering the mapping for automatic recreation, or mounts all registered volumes. ASM, mounted disk groups, and enabled volumes are prerequisites; drive-letter mounting is required before formatting an ADVM volume with NTFS.

Read More: [advmutil mount](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20mount)

## Oracle ACFS Command-Line Tools for Tagging

Oracle ACFS tagging commands display, add, and remove tags on files and directories. Tags can be applied recursively, but Solaris symbolic-link tags are not preserved by backup, restore, copy, move, tar, or pax operations. Tagging behavior is subject to file permissions and security-realm browse permissions.

Read More: [Oracle ACFS Command-Line Tools for Tagging](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20Tagging)

## acfsutil tag info

`acfsutil tag info` displays paths of tagged Oracle ACFS files and directories, optionally recursively, filtered by an exact or case-insensitive partial tag name. With no paths, it searches all ACFS mount points. Users need read access, and security-realm restrictions can suppress results without appropriate browse permissions.

Read More: [acfsutil tag info](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20tag%20info)

## acfsutil tag set

`acfsutil tag set` assigns a tag to one or more files or directories, optionally recursively and with progress output. Tags support limited ASCII characters and names up to 32 characters; `all` is reserved. Existing tags remain, new files inherit parent-directory tags, and users need permission to modify the targets.

Read More: [acfsutil tag set](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20tag%20set)

## acfsutil tag unset

`acfsutil tag unset` removes a specified tag or all tags from files and directories, optionally recursively with progress reporting. Other tags remain when one tag is removed, and the command requires permission to modify targets plus appropriate browse access within protected security realms.

Read More: [acfsutil tag unset](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20tag%20unset)

## Oracle ACFS Command-Line Tools for Replication

This topic summarizes snapshot-based Oracle ACFS replication commands for controlling background processing, initializing and synchronizing replication, comparing data, pausing or resuming activity, performing failover or role changes, terminating replication, tracing operations, updating metadata, and upgrading existing replication installations.

Read More: [Oracle ACFS Command-Line Tools for Replication](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20Replication)

## acfsutil repl bg

`acfsutil repl bg` starts, stops, or reports on the replication background process for a replicated mount point or snapshot. Replication requires this clusterwide process on the primary cluster; initialization starts and registers it with Clusterware so it can restart automatically after reboot or failure.

Read More: [acfsutil repl bg](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20repl%20bg)

## Managing Oracle ACFS with Command-Line Tools

Oracle ACFS command-line tools support comprehensive snapshot-based replication management, including monitoring background processes, comparing primary and standby contents, initializing and updating replication, pausing and resuming operations, synchronizing data, performing planned switchovers or failovers, reversing roles, terminating replication, tracing activity, and upgrading legacy replication. The commands also provide auditing functions to initialize, enable, disable, inspect, archive, read, and purge audit trails, although ACFS auditing and security are deprecated from Oracle ACFS 19c Release 19.5. Security commands manage administrators, passwords, batch operations, file-system and realm security, and security metadata. Operational considerations include correct primary/standby sequencing, SSH configuration, replication-user privileges, quiescing applications before role changes or final synchronization, appropriate handling of unmounts and failovers, and restricting administrative commands to authorized roles.

Read More: [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md)

## Managing Oracle ACFS with Command-Line Tools

This page summarizes Oracle ACFS command-line administration for security, encryption, keystores, and snapshots. Security commands initialize and prepare file systems, inspect realms and secured files, save or load metadata, create, clone, edit, audit, and destroy realms, rules, and rule sets, and add or remove users, groups, command filters, and protected paths; these operations generally require a security administrator. Encryption commands initialize key storage, inspect encryption status, enable or disable encryption, set algorithms and key lengths, rekey volumes or files, back out encryption, and migrate between SSO and PKCS keystores, with administrative privileges required for system-wide operations. Snapshot commands provide operations to convert snapshot modes and, as summarized, create, delete, duplicate, inspect, link, quota-manage, remaster, and rename snapshots. The documented options support recursive processing, AES encryption with 128-, 192-, or 256-bit keys, audit authorization and violation tracking, policy replication, and controlled access based on users, groups, applications, hosts, times, and file-system operations.

Read More: [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md)

## Managing Oracle ACFS with Command-Line Tools

Oracle ACFS command-line tools manage snapshots, compression, cluster-domain services, exports, transports, compatibility, defragmentation, and file-system operations. Snapshot commands support creation, deletion, duplication, inspection, linking, quotas, remastering, and renaming, with access and migration restrictions varying by operation; compression commands control file compression and reporting; cluster-domain utilities manage remote-service status, credentials, exports, sessions, and transports; general utilities handle acceleration volumes, compatibility, defragmentation, freezing, and related administration. Administrative or root privileges are commonly required.

Read More: [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md)

## acfsutil snap delete

Deletes a named snapshot from a mounted Oracle ACFS file system and removes its representation under `.ACFS/snaps`. Open files and directory references do not prevent deletion, but associated storage is reclaimed asynchronously after references close; pending cleanup is visible through snapshot information. The operation fails during rolling migration and requires administrator privileges or membership in the Oracle ASM administrator group.

Read More: [acfsutil snap delete](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20delete)

## acfsutil snap duplicate apply

Applies a snapshot duplication stream from standard input to the mounted file system or a specified writable target snapshot. Initial applies require an empty target, while incremental applies require contents matching the prior source snapshot; concurrent changes cause failure, and an identical stream returns status 2 without modifying the target. Optional backup snapshots preserve the last successful target state, while exit statuses 0, 1, and 2 indicate success, fatal failure, and duplicate-stream no-op respectively; root privileges are required.

Read More: [acfsutil snap duplicate apply](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20duplicate%20apply)

## acfsutil snap duplicate create

Creates a snapshot duplication stream on standard output for transfer to another compatible Oracle ACFS file system. Supplying only a new snapshot produces an initial stream containing the complete snapshot, while specifying an old snapshot produces an incremental stream containing differences; parent and restart options support common snapshot ancestry and interrupted transfers. The command normally feeds `acfsutil snap duplicate apply`, requires root privileges, and returns status 0 on success or 1 on fatal failure.

Read More: [acfsutil snap duplicate create](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20duplicate%20create)

## acfsutil snap info

Displays metadata for one or all snapshots, including name, type, parent, creation time, location, storage usage, quota data, replication or duplication status, and deletion progress. The `-t` option presents snapshot relationships as a tree, while pending deletion states identify snapshots awaiting open-file closure or background cleanup. Usage statistics include metadata and may be temporarily inaccurate because ACFS updates them asynchronously.

Read More: [acfsutil snap info](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20info)

## acfsutil snap link

Creates or deletes one specialized snapshot link that exposes a snapshot through an alternate path outside `.ACFS/snaps`. Links can be created only in the primary file system, require `COMPATIBLE.ADVM` 18.0 or later, and must be managed with `acfsutil snap link` rather than ordinary file-system commands; each snapshot supports only one link, which can be recreated at another location or name.

Read More: [acfsutil snap link](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20link)

## acfsutil snap quota

Sets, increases, or decreases the storage limit for a specified snapshot using byte or K/M/G/T/P units. The quota establishes an upper bound on storage added to the snapshot rather than reserving space, applies to eligible snapshots created with `COMPATIBLE.ADVM` 12.2 or later, and can be used for both read-only and read-write snapshots. Warnings occur near 90 percent utilization, while writes exceeding the limit fail with `EDQUOT` or possibly `ENOSPC`; root privileges are required.

Read More: [acfsutil snap quota](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20quota)

## acfsutil snap remaster

Replaces the base of an unmounted Oracle ACFS file system with the point-in-time state of an existing snapshot, reintegrating its extents and leaving no snapshots. The operation is irreversible, requires administrator privileges, and can resume an interrupted remaster with `-c`; it cannot run while replication, security, encryption, or plug-ins are enabled.

Read More: [acfsutil snap remaster](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20remaster)

## acfsutil snap rename

Safely renames an existing Oracle ACFS snapshot while preserving its contents and handling open references similarly to a parent-directory rename. The operation requires administrator privileges but is unsupported for snapshots associated with pluggable databases or replication, because renaming can create inconsistencies.

Read More: [acfsutil snap rename](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20snap%20rename)

## Oracle ACFS Command-Line Tools for Compression

Oracle ACFS compression commands provide a compact administrative interface for copying files with compression, inspecting compression usage, enabling compression, and disabling compression. Compression applies by default to files created after activation, while existing files retain their current state; Oracle ACFS compression is not supported for Oracle Database files.

Read More: [Oracle ACFS Command-Line Tools for Compression](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20Compression)

## acfsutil compress copy

Copies files into a target directory while optionally compressing them, selecting a compression unit, recursively copying directories, preserving uncompressed copies with `-n`, displaying verbose output, and overwriting existing targets with `-f`. Without `-f`, the operation stops when an existing target is encountered; copying to a compression-capable file system with compression disabled requires the `-n` option.

Read More: [acfsutil compress copy](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20compress%20copy)

## acfsutil compress info

Reports compression details for a specified file, including compression-unit size, disk space used, space saved, and compressed usage as a percentage of the uncompressed size. It is intended for assessing the effectiveness and storage impact of Oracle ACFS compression.

Read More: [acfsutil compress info](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20compress%20info)

## acfsutil compress off

Disables Oracle ACFS compression for a mounted file system. Files created afterward are uncompressed, while files already compressed remain compressed; root or system-administrator privileges are required.

Read More: [acfsutil compress off](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20compress%20off)

## acfsutil compress on

Enables Oracle ACFS compression for a mounted file system, optionally selecting the compression algorithm; `lzo` is currently the only and default algorithm. New files are compressed by default, existing uncompressed files remain unchanged, and root or system-administrator privileges are required. Compression should not be enabled for file systems intended to contain Oracle Database files.

Read More: [acfsutil compress on](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20compress%20on)

## Oracle ACFS Command-Line Tools for Oracle ACFS in the Cluster Domain

Cluster-domain utilities manage Oracle ACFS remote service prerequisites, credentials, cluster state, remote file attributes, exports, sessions, and network transports. The command set includes node support, installation, and loading checks; credential and cluster information management; remote-file protection; Domain Services Cluster export lifecycle operations; member-cluster session monitoring; and transport configuration.

Read More: [Oracle ACFS Command-Line Tools for Oracle ACFS in the Cluster Domain](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Tools%20for%20Oracle%20ACFS%20in%20the%20Cluster%20Domain)

## acfsremote installed

Checks whether Oracle ACFS remote-service drivers and applicable system transports are installed on the current node. It supports member-cluster and Domain Services Cluster checks, optional tracing, and explicit cluster-role selection.

Read More: [acfsremote installed](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsremote%20installed)

## acfsremote loaded

Checks whether Oracle ACFS remote-service resources and transports are loaded and running. A transport that is unused or unconfigured may correctly report as not loaded even when the remote service itself is operational; the command applies to both member and Domain Services Clusters.

Read More: [acfsremote loaded](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsremote%20loaded)

## acfsremote supported

Determines whether the current node meets the kernel, package, and transport requirements for Oracle ACFS remote service. It supports member-cluster and Domain Services Cluster checks, optional tracing, and transport-specific capability reporting.

Read More: [acfsremote supported](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsremote%20supported)

## acfsutil cluster credential

Generates, lists, updates, removes, and imports Oracle ACFS remote-service credentials, including operating-system user and group permissions. It supports member-cluster registration and manifest exchange, applies across cluster types, and is generally used by setup procedures rather than directly by end users.

Read More: [acfsutil cluster credential](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20cluster%20credential)

## acfsutil cluster info

Displays cluster type and internal state used to verify synchronization between the Oracle ACFS kernel cluster and Oracle ASM. Output includes node membership, rebuild master, incarnation, cluster state, remote-service mode, storage mode, DLM status, and node addresses; the command applies to all cluster types.

Read More: [acfsutil cluster info](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20cluster%20info)

## acfsutil remote clear

Removes the Oracle ACFS remote attribute from a specified file, allowing a system administrator to remove or truncate the file on disk.

Read More: [acfsutil remote clear](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20remote%20clear)

## acfsutil remote set

Sets the Oracle ACFS remote attribute on a specified file, preventing a system administrator from removing or truncating the file on disk.

Read More: [acfsutil remote set](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20remote%20set)

## advmutil export create

Creates a Domain Services Cluster export, allocates a fully provisioned backing file, and associates it with a member cluster and ACFS storage repository. The export name becomes the member-cluster volume name; `-f` permits reuse of an existing backing file. Export snapshots are created on the Domain Services Cluster and can be exposed through snapshot links and reused export mappings.

Read More: [advmutil export create](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20export%20create)

## advmutil export list

Queries Domain Services Cluster exports and member-cluster information using configurable filters, grouping, output fields, active-only selection, and header suppression. It supports grouping by cluster name, cluster GUID, or storage repository and is suitable for both administration and scripting.

Read More: [advmutil export list](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20export%20list)

## advmutil export lsof

Lists active files associated with exports across repositories or within a specified repository path. The command can restrict output to active exports and applies only to the Domain Services Cluster, supporting investigation of export usage and activity.

Read More: [advmutil export lsof](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20export%20lsof)

## advmutil export mapping

Reexports all configured exports or those belonging to a specified member cluster. It is used to restore export accessibility after administrative actions remove access and applies only to the Domain Services Cluster.

Read More: [advmutil export mapping](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20export%20mapping)

## advmutil export remove

Removes export configuration metadata for a member cluster and repository mapping. The backing file remains by default and can later be reused with `-f`; `-b` removes it and releases repository space, while `-f` and `-y` control forced removal and confirmation behavior.

Read More: [advmutil export remove](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20export%20remove)

## advmutil export resize

Adds storage to an export’s backing file and correspondingly resizes the member-cluster device. The member cluster must resize its ACFS file system with `acfsutil size` to use the additional capacity unless automatic resize is configured; shrinking requires resizing the member file system first. The command applies only to the Domain Services Cluster.

Read More: [advmutil export resize](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20export%20resize)

## advmutil session list

Displays current Oracle ACFS remote-service transport sessions on a member cluster, optionally filtered by node or transport and expanded with verbose XML output. Session states include `ONLINE`, `REFRESH`, and `RESCAN`, making the command useful for operational diagnostics.

Read More: [advmutil session list](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20session%20list)

## advmutil transport create

Creates a Domain Services Cluster transport for a member cluster using a transport VIP, network number, or alternate resource identifier. Multiple transports can support multipathing and failover, VIPs may be shared, and each transport receives a cluster, type, and sequence-based identifier.

Read More: [advmutil transport create](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20transport%20create)

## advmutil transport list

Displays configured transports on the Domain Services Cluster, optionally filtered by member-cluster name, cluster GUID, or transport ID. Verbose mode provides full configuration details, while sequence numbers and transport IDs can be used for targeted member-cluster diagnostics.

Read More: [advmutil transport list](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20transport%20list)

## advmutil transport remove

Removes a specified transport from a member cluster on the Domain Services Cluster. If it is the last transport using an associated VIP resource, that resource is also removed.

Read More: [advmutil transport remove](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20transport%20remove)

## Oracle ACFS Command-Line Utilities

Oracle ACFS command-line utilities cover accelerator replacement, compatibility management, directory and file defragmentation, file-system freezing and thawing, information and storage reporting, plug-in control, mount registration, file-system removal, scrubbing, resizing, version reporting, and Oracle ADVM volume inspection. They provide the principal administrative interface for maintaining ACFS and related ADVM resources.

Read More: [Oracle ACFS Command-Line Utilities](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Oracle%20ACFS%20Command-Line%20Utilities)

## acfsutil accel replace

Replaces an existing accelerator volume with a new volume, which must be at least as large as the current accelerator. The file system must be unmounted on every node, and a larger replacement requires a subsequent resize operation after remounting; root or Oracle ASM administrator privileges are required.

Read More: [acfsutil accel replace](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20accel%20replace)

## acfsutil compat get

Displays the Oracle ACFS file-system compatibility level and the disk group’s `COMPATIBLE.ADVM` setting for a mounted file system. It identifies the effective feature compatibility established during file-system creation or by a prior compatibility change.

Read More: [acfsutil compat get](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20compat%20get)

## acfsutil compat set

Raises the compatibility level of an Oracle ACFS file system to a specified release version subject to `COMPATIBLE.ADVM` and the running Grid Infrastructure release. Compatibility cannot be downgraded, and increasing it may prevent mounting with older Grid Infrastructure releases.

Read More: [acfsutil compat set](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20compat%20set)

## acfsutil defrag dir

Defragments files in a specified directory, optionally traversing subdirectories with `-r`. The caller must have write access to affected files and administrator privileges or Oracle ASM administrator-group membership.

Read More: [acfsutil defrag dir](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20defrag%20dir)

## acfsutil defrag file

Defragments one or more specified files, with the optional `-i` mode estimating the possible reduction in extents without performing the operation. Write access is required for defragmentation, read access for estimation, and administrator privileges are required.

Read More: [acfsutil defrag file](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20defrag%20file)

## acfsutil freeze

Temporarily halts modification activity on a mounted Oracle ACFS file system, optionally flushing pending data first with `-f`. It supports point-in-time image creation without stopping applications; normal activity resumes with the corresponding thaw operation.

Read More: [acfsutil freeze](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20freeze)

## Managing Oracle ACFS with Command-Line Tools

Use Oracle ACFS command-line tools cautiously, especially `acfsutil freeze`, which can cause application timeouts, database instance termination after prolonged freezing, and replication interruptions. Frozen replicated file systems may block reverse, synchronization, or termination operations, so administrative actions should be brief and coordinated with database and replication activity.

Read More: [Managing Oracle ACFS with Command-Line Tools](managing-oracle-acfs-with-command-line-tools.md)

## acfsutil info file

The `acfsutil info file` command displays detailed information about one or more Oracle ACFS files, including ownership, size, allocation, timestamps, tags, and extent mappings from ACFS to ASM devices. Options provide detailed extent data, metadata extents, usage and snapshot inheritance information, or extent counts only; read access to the file is required.

Read More: [acfsutil info file](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20info%20file)

## acfsutil info fs

The `acfsutil info fs` command reports Oracle ACFS file-system configuration, status, capacity, volumes, snapshots, replication, compression, encryption, security, fragmentation, and operational statistics. It supports querying individual properties, monitoring change rates at intervals, and displaying fragmentation details; states such as Available, Offline, and Corrupt indicate whether the file system is operational or requires repair.

Read More: [acfsutil info fs](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20info%20fs)

## acfsutil info id

The `acfsutil info id` command translates an internal Oracle ACFS file identifier into its corresponding path at a specified mount point. This is useful for investigating driver-reported I/O errors, and requires administrator privileges or membership in the Oracle ASM administrator group.

Read More: [acfsutil info id](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20info%20id)

## acfsutil info storage

The `acfsutil info storage` command provides platform-independent storage-consumption information across Oracle ASM disk groups, ADVM volumes, ACFS file systems, and snapshots. It supports selectable units, summary or detailed output, disk-group filtering, redundancy-aware free-space calculations, and requires root or `asmadmin` privileges.

Read More: [acfsutil info storage](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20info%20storage)

## acfsutil plugin disable

The `acfsutil plugin disable` command stops Oracle ACFS plug-in metric collection and communication with the associated plug-in application for a mounted file system. Administrator privileges or membership in the Oracle ASM administrator group is required.

Read More: [acfsutil plugin disable](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20plugin%20disable)

## acfsutil plugin enable

The `acfsutil plugin enable` command activates ACFS plug-in monitoring for selected tagged files or all files, using predefined metric types such as `acfsmetric1` and `acfsmetric2`. Metrics may be delivered through application polling or periodic posting, with configurable intervals up to 60 minutes; collection covers user file I/O but excludes internal ACFS operations and replication files.

Read More: [acfsutil plugin enable](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20plugin%20enable)

## acfsutil plugin info

The `acfsutil plugin info` command displays the plug-in state, metric type, enabled tags, delivery method, and posting interval for a mounted Oracle ACFS file system. Administrator privileges or membership in the Oracle ASM administrator group is required.

Read More: [acfsutil plugin info](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20plugin%20info)

## acfsutil registry

The `acfsutil registry` command manages persistent Oracle ACFS mount registrations used for automatic mounting at startup. Administrators can add, modify, delete, list, or query entries, specify mount options, eligible nodes, descriptions, and permitted users, while any user may display registry contents; registration changes require root or `asmadmin` privileges and are unsupported in Oracle Restart configurations.

Read More: [acfsutil registry](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20registry)

## acfsutil rmfs

The `acfsutil rmfs` command removes a dismounted Oracle ACFS file system by disabling its superblock, requiring root or `asmadmin` privileges. The operation clears associated volume mount and usage metadata, but the file system may be recoverable with repair tools and the device can later be reformatted.

Read More: [acfsutil rmfs](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20rmfs)

## acfsutil scrub

The `acfsutil scrub` command checks Oracle ACFS directory metadata, file metadata, and user data for mirror inconsistencies and reports affected paths, offsets, lengths, and volume locations. It supports metadata-only, recursive, quiet, extension-exclusion, snapshot-exclusion, error-limit, I/O-load, and trace-level controls, and requires root privileges on supported Linux and AIX systems.

Read More: [acfsutil scrub](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20scrub)

## acfsutil size

The `acfsutil size` command grows or shrinks an Oracle ACFS file system or configures automatic resizing through minimum-free-space increments and maximum-size limits. It can estimate data movement, resize a specific volume, and automatically respond to low or fragmented space, but operations may be time-consuming, partially succeed, alter fragmentation, or require compatible ADVM settings and sufficient ASM capacity.

Read More: [acfsutil size](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20size)

## acfsutil thaw

The `acfsutil thaw` command resumes file-system activity previously suspended with `acfsutil freeze`. It accepts the mounted file-system path and should be used promptly after maintenance to avoid blocked applications and related service disruption.

Read More: [acfsutil thaw](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20thaw)

## acfsutil version

The `acfsutil version` command displays the installed Oracle ACFS release, while `-v` provides verbose kernel and command build information, including full versions, hashes, and bug identifiers. Administrator privileges or membership in the Oracle ASM administrator group is required.

Read More: [acfsutil version](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/acfsutil%20version)

## advmutil canonical

The `advmutil canonical` command converts an Oracle ADVM volume-device identifier into its normalized canonical form. It is particularly useful in scripts and on Windows, where device names may include alternate prefixes that other utilities do not accept consistently.

Read More: [advmutil canonical](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20canonical)

## advmutil volinfo

The `advmutil volinfo` command displays Oracle ADVM volume properties such as device name, size, resize increment, redundancy, striping, disk group, volume name, and compatibility level. Default output is human-readable, while `-l` produces colon-separated fields and `-L` produces space-separated output suitable for scripting.

Read More: [advmutil volinfo](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/advmutil%20volinfo)

## Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems

An ACFS file system can be deregistered to prevent automatic mounting, dismounted independently for maintenance or checking, and have its underlying volume disabled only after dismounting. These actions do not destroy file-system data, but deregistered or dismounted file systems must be explicitly mounted again, and disabled volumes must be re-enabled before access.

Read More: [Deregistering, Dismounting, and Disabling Volumes and Oracle ACFS File Systems](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Deregistering%2C%20Dismounting%2C%20and%20Disabling%20Volumes%20and%20Oracle%20ACFS%20File%20Systems)

## Removing an Oracle ACFS File System and a Volume

Permanent removal requires deregistering the file system, dismounting it from every cluster node, removing it with `acfsutil rmfs` when necessary, optionally disabling the volume, and deleting the volume with ASMCMD. This sequence destroys the file-system data and should be performed only after confirming that the volume and its contents are no longer required.

Read More: [Removing an Oracle ACFS File System and a Volume](https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/OSTMG%2019c/Part%20III%20Oracle%20Automatic%20Storage%20Management%20Cluster%20File%20System/19c/Removing%20an%20Oracle%20ACFS%20File%20System%20and%20a%20Volume)