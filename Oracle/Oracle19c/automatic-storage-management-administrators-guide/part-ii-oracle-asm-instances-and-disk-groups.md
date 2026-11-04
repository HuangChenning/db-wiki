---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-ii-oracle-asm-instances-and-disk-groups.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Part II Oracle ASM Instances and Disk Groups

Part II discusses the administration of Oracle ASM instances and disk groups in the following chapters:

## Administering Oracle ASM Instances

Oracle ASM administration resembles database administration and can be performed with SQL\*Plus, ASMCMD, ASMCA, and SRVCTL. This material covers release compatibility, initialization parameters and parameter-file management, automatic memory management, disk discovery, disk-group startup, rebalancing, preferred reads, process and memory sizing, Oracle Restart, instance startup and shutdown, restricted mode, SRVCTL administration, configuration, upgrades, patching, and Active Session History. It also explains authentication through SYSASM, SYSDBA, SYSOPER, operating-system groups, password files, shared password files, and privilege separation; migration of database files to ASM using RMAN; and ASM audit-trail management through Syslog, operating-system auditing, and unified auditing. ASM supports older database releases subject to compatibility constraints, while clustered environments provide rolling upgrades and patches; parameter and password files can be backed up, copied, moved, or stored in ASM disk groups with appropriate compatibility settings.

Read More: [Administering Oracle ASM Instances](administering-oracle-asm-instances.md)

## Administering Oracle ASM Instances

Oracle Database 23ai introduces the static ASM initialization parameters `ASM_UNIFIED_AUDIT_LEVEL`, which audits either all actions or only `CONNECT`, `SHUTDOWN`, and `STARTUP` by default, and `ASM_UNIFIED_AUDIT_DESTINATION`, which writes records to spillover files or the system log by default; both apply to ASM, ASM Proxy, and Remote ASM and require an instance restart after changes. System-log auditing uses `UNIFIED_AUDIT_SYSTEMLOG`, now modifiable in ASM instances, while ASM unified auditing mandatorily records `CONNECT` and `SHUTDOWN` and does not retain full audit copies in OS files when redirected to syslog. Audit files support configurable maximum sizes of 1 KB–2,000,000 KB, maximum ages of 1–497 days, and purge intervals of 1–999 hours. For database instances supporting ASM without automatic memory management, Oracle recommends increasing `PROCESSES` by 16, `LARGE_POOL_SIZE` by 600 KB, and sizing `SHARED_POOL_SIZE` according to the aggregate ASM-resident datafile, redo, and online tempfile capacity and disk-group redundancy: approximately 1 MB per 100 GB plus 2 MB for external redundancy, per 50 GB plus 4 MB for normal redundancy, or per 33 GB plus 6 MB for high redundancy; automatic memory management is strongly recommended.

Read More: [Administering Oracle ASM Instances](administering-oracle-asm-instances.md)

## Administering Oracle ASM Disk Groups

Oracle ASM disk group administration covers creating, altering, mounting, dismounting, monitoring, and maintaining disk groups while database instances remain operational. Administrators manage attributes such as redundancy, compatibility, sector size, access control, repair intervals, content checking, preferred reads, thin provisioning, and storage type; create groups with defined disks, failure groups, quorum configuration, allocation units, and compatibility levels; and store database, recovery, OCR, and voting files appropriately. Disk groups can be modified online by adding, replacing, renaming, resizing, dropping, or undropping disks, managing ADVM volumes, and controlling automatic or manual rebalancing with power, wait, and phase options. Oracle ASM also provides disk discovery, capacity management, scrubbing for corruption detection and repair, sector-size validation, and monitoring through dynamic performance views and ASMCMD, with special considerations for Exadata, extended clusters, Flex disk groups, and compatibility requirements.

Read More: [Administering Oracle ASM Disk Groups](administering-oracle-asm-disk-groups.md)

## Administering Oracle ASM Disk Groups

Oracle ASM disk discovery uses paths defined by `ASM_DISKSTRING` and occurs during instance startup, disk-group mount, disk operations, relevant queries, ASMCA actions, and ASMCMD commands; discovered disks are classified as `MEMBER`, `CANDIDATE`, `PROVISIONED`, `FORMER`, or `FOREIGN`, with discovery limited to 10,000 disks and subject to partition, duplicate-path, and duplicate-header rules. Restricting `ASM_DISKSTRING` can improve discovery and mount performance, but multipathing, ASM Filter Driver, and ASMLIB conventions must be respected. Disk groups require sufficient free capacity to restore mirroring after failure; `REQUIRED_MIRROR_FREE_MB`, `USABLE_FILE_MB`, `TOTAL_MB`, and `FREE_MB` provide capacity guidance, with negative usable space indicating increased risk. Redundancy options include external, normal, high, flex, and extended, while failure groups isolate hardware risks and determine mirror placement, failure tolerance, and recovery behavior. ASM handles read and write I/O errors through mirror recovery, disk offlining, remapping, and possible dismounts; fast mirror resync tracks changes during transient outages, controlled by `DISK_REPAIR_TIME`, and preferred read failure groups can improve locality in extended clusters. Disk groups should contain similarly sized and performing disks, generally separate database files from recovery storage, and observe limits on disk groups, disks, files, capacity, and file sizes. Compatibility attributes— `COMPATIBLE.ASM`, `COMPATIBLE.RDBMS`, and `COMPATIBLE.ADVM` —enable release-specific features, must be advanced in the proper order, and cannot be reduced without creating a new disk group and moving files. ASM File Access Control restricts file access by database user, group, ownership, and permissions through disk-group attributes and `ALTER DISKGROUP` operations. Maintenance includes mounting, dismounting, restricted operation, consistency checks, dropping, renaming, and force-mounting groups with missing disks; force mounts leave unavailable disks offline until repaired or removed after the repair interval.

Read More: [Administering Oracle ASM Disk Groups](administering-oracle-asm-disk-groups.md)

## Administering Oracle ASM Disk Groups

Oracle ASM disk groups can be force-mounted with reduced redundancy when disks are temporarily unavailable, provided at least one extent copy for every file remains accessible; inaccessible disks are taken offline and may be dropped after `DISK_REPAIR_TIME` expires. Administrators can validate metadata consistency with `ALTER DISKGROUP ... CHECK`, optionally repair detected issues, and can drop disk groups—with `INCLUDING CONTENTS` or, cautiously, `FORCE` for unmountable groups—when files are no longer needed or redundancy must be changed. Cloned disk groups can be renamed using the two-phase `renamedg` utility, although Clusterware resources and database references require separate updates. Flex disk groups provide database- and file-group-level storage management, configurable redundancy, quotas, rebalancing, access control, and point-in-time PDB cloning; extended disk groups build on these capabilities for stretch clusters by distributing redundancy across data sites and a quorum site. File groups organize files by database, PDB, volume, or cluster and support properties such as redundancy, striping, priority, power limits, quotas, ownership, and user groups, while quota groups enforce physical-space limits across file groups within a disk group. Point-in-time cloning uses prepared mirror copies, file-group splitting, status monitoring, optional cleanup, and rebalance recovery after failures. Normal or high redundancy groups can be migrated to flex redundancy after meeting compatibility, failure-group, capacity, and template requirements, followed by conversion, rebalance, and verification of file redundancy.

Read More: [Administering Oracle ASM Disk Groups](administering-oracle-asm-disk-groups.md)

## Administering Oracle ASM Files, Directories, and Templates

Oracle ASM administration covers supported database file types, system-generated and alias file names, file creation and referencing methods, default disk-group locations, online data-file movement, file mapping, aliases, directories, XML DB access through `/sys/asm`, DBMS\_FILE\_TRANSFER operations, and templates. ASM supports most database files but not certain administrative files such as trace files and alert logs; fully qualified names identify existing files, while incomplete names and templates support managed creation. Aliases and user directories provide friendly references but are not Oracle Managed Files and may require manual cleanup. Templates define striping and redundancy, with system defaults based on file type and disk-group redundancy, and can be added, modified, or removed for customized file attributes.

Read More: [Administering Oracle ASM Files, Directories, and Templates](administering-oracle-asm-files-directories-and-templates.md)

## Using Views to Display Oracle ASM Information

Oracle ASM dynamic performance views provide operational, configuration, storage, file, client, template, and access-control information. Key views include `V$ASM_DISKGROUP` and `V$ASM_DISK` for disk-group and disk details, their lower-overhead `STAT` counterparts for monitoring, `V$ASM_FILE`, `V$ASM_ALIAS`, `V$ASM_TEMPLATE`, `V$ASM_ATTRIBUTE`, `V$ASM_CLIENT`, and `V$ASM_OPERATION` for files, aliases, templates, attributes, clients, and active operations. Disk-group numbers are mount-specific rather than persistent. File Access Control details are exposed through `V$ASM_USER`, `V$ASM_USERGROUP`, `V$ASM_USERGROUP_MEMBER`, and `V$ASM_FILE`, enabling administrators to inspect users, groups, memberships, permissions, and file ownership.

Read More: [Using Views to Display Oracle ASM Information](using-views-to-display-oracle-asm-information.md)

## Administering Oracle ASM with Oracle Enterprise Manager

Oracle Enterprise Manager Cloud Control provides a centralized interface for administering Oracle ASM, including accessing ASM status and capacity information, configuring initialization parameters, managing users, disk groups, disks, templates, files, aliases, access controls, and ASM Filter Driver provisioning. It supports disk group creation and maintenance, disk online/offline operations, rebalance control, compatibility and repair settings, scrubbing, performance monitoring, integrity checks, bad-block recovery, ASM file migration, alert and incident analysis through Support Workbench, and Oracle Flex ASM monitoring.

Read More: [Administering Oracle ASM with Oracle Enterprise Manager](administering-oracle-asm-with-oracle-enterprise-manager.md)

## Performing Oracle ASM Data Migration with RMAN

RMAN supports migrating databases, recovery areas, and individual data files between Oracle ASM and alternative storage. Migration generally involves preparing the database, creating backups or copies, configuring Oracle Managed Files and ASM destinations, restoring and switching files, recovering the database, recreating temporary and redo files, and optionally moving recovery-area contents. The procedures also cover reversing migration from ASM, handling standby and primary databases, disabling or restoring features such as Flashback Database and block change tracking when required, and relocating active data files between ASM disk groups using RMAN backup copies, switching, recovery, and cleanup.

Read More: [Performing Oracle ASM Data Migration with RMAN](performing-oracle-asm-data-migration-with-rman.md)

## Managing Oracle ASM With ASMCA

Oracle ASM Configuration Assistant (ASMCA) provides GUI and silent command-line tools for installing, configuring, and managing Oracle ASM instances, disk groups, ASM Filter Driver labels, file groups, quota groups, Oracle ADVM volumes, and Oracle ACFS file systems. The GUI starts with the asmca command from the Grid Infrastructure home, connects to the +ASM instance, and can start it when necessary. ASMCA supports creating instances with SYS and ASMSNMP credentials, registering listeners, adjusting initialization parameters, and managing disk groups by adding or dropping disks, configuring redundancy, failure and quorum groups, compatibility and allocation-unit settings, attributes, templates, labels, mounting state, and deletion. Its command-line mode uses asmca -silent with commands for configuring or deleting instances, setting parameters, creating disk groups, adding disks, editing attributes, managing Filter Driver labels, and creating or removing file and quota groups; options specify discovery paths, disks, failure groups, redundancy, passwords, compatibility, and related settings. Availability of some features depends on the deployment environment, such as Oracle RAC.

Read More: [Managing Oracle ASM With ASMCA](managing-oracle-asm-with-asmca.md)

## Managing Oracle ASM with ASMCMD

ASMCMD is Oracle ASM’s command-line utility for administering ASM instances, disk groups, files, directories, aliases, templates, volumes, access control, member clusters, ASM Filter Driver, audit trails, and related configuration. It supports interactive shell usage and noninteractive execution for scripts, with SYSASM as the default privilege and SYSDBA available for limited database operations. Users must configure the appropriate Oracle home, SID, authentication, and mounted disk groups, while understanding ASM fully qualified paths, relative and absolute paths, aliases, directory navigation, and wildcard behavior. Core instance commands manage discovery strings, clients, operations, password files, cluster state, patches, shutdown and startup, and SPFILE backup, copying, movement, and registration. Member-cluster commands create, modify, list, and remove cluster configurations and manifests. ASM Filter Driver commands configure filtering, manage disk discovery and labels, control data integrity, scan and refresh disks, and report driver state. Audit-management commands clean OS and unified audit files, configure retention properties and timestamps, create and manage purge jobs, and display audit configuration. ASMCMD also provides command-specific help, verbosity and diagnostic logging, version display, current-directory prompts, and documented return codes for automation. veloped identifiers that require quoting should be avoided because they may not work consistently across ASM management tools.

Read More: [Managing Oracle ASM with ASMCMD](managing-oracle-asm-with-asmcmd.md)

## Managing Oracle ASM with ASMCMD

This page documents ASMCMD audit, file-management, and disk-group-management commands. Audit operations create, drop, configure, monitor, enable, disable, and schedule purge jobs for OS or Unified audit trails, including file size, age, and archive timestamp settings. File commands support extraction, navigation, copying, space analysis, searching, listing, open-file inspection, block mapping, alias and directory management, and deletion while documenting wildcard, alias, redundancy, and remote-copy behavior. Disk-group commands provide capabilities to create, modify, check, repair, mount, dismount, drop, rebalance, monitor, and inspect disk groups, disks, attributes, open devices, and I/O statistics. XML-driven commands configure or alter disk groups, while metadata backup and restore commands preserve and recover ASM and selected ACFS configuration metadata; additional commands manage disk and failure-group availability, disk labels, sparse-file parents, and disk remapping.

Read More: [Managing Oracle ASM with ASMCMD](managing-oracle-asm-with-asmcmd.md)

## Managing Oracle ASM with ASMCMD

This page summarizes ASMCMD commands for administering Oracle ASM disk groups, file groups, quota groups, templates, file access control, and ASM Filter Driver. Disk operations include offlining and onlining disks or failure groups, controlling rebalance power and phases, remapping damaged block ranges, setting sparse-file parents, changing disk-group attributes, stamping and displaying disk labels, and dismounting disk groups. File-group and quota-group commands create, modify, list, move, and remove groups or files, with XML-based configuration supported for file groups. Template commands create, modify, list, and delete templates with configurable striping and redundancy. File access control commands manage ownership, groups, permissions, users, and passwords, subject to SYSASM, ownership, and operating-system identity requirements. ASM Filter Driver commands configure or deconfigure AFD, manage data integrity and filtering, set discovery strings, label or unlabel disks, scan and refresh devices, list labeled disks, and report driver state, with several operations requiring root privileges or stopped clusterware.

Read More: [Managing Oracle ASM with ASMCMD](managing-oracle-asm-with-asmcmd.md)