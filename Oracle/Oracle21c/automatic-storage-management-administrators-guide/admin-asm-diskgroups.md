---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/admin-asm-diskgroups.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Administration of Oracle ASM disk groups includes creating, altering, dropping, mounting, and dismounting tasks.

This chapter describes how to administer Oracle Automatic Storage Management (Oracle ASM) disk groups. This information includes how to create, alter, drop, mount, and dismount Oracle ASM disk groups. The database instances that use Oracle ASM can continue operating while you administer disk groups.

The examples in this chapter use SQL statements. These examples assume that SQL\*Plus is run from the Oracle grid home where Oracle ASM is installed and the Oracle environmental variables are set to this home. The examples also assume that the Oracle ASM instance is running. This chapter contains the following topics:

- [Managing Disk Group Attributes](manage-diskgroup-attributes.md)
- [Creating Disk Groups](create-diskgroups.md)
- [Altering Disk Groups](alter-diskgroups.md)
- [Oracle ASM Disk Discovery](asm-disk-discovery.md)
- [Managing Capacity in Disk Groups](capacity-diskgroups.md)
- [Oracle ASM Mirroring and Disk Group Redundancy](mirroring-diskgroup-redundancy.md)
- [Performance and Scalability Considerations for Disk Groups](performance-scability-diskgroup.md)
- [Disk Group Compatibility](diskgroup-compatibility.md)
- [Managing Oracle ASM File Access Control for Disk Groups](asm-access-control-diskgroups.md)
- [Maintaining Disk Groups](maintain-diskgroups.md)
- [Managing Oracle ASM Flex Disk Groups](asm-filegroups.md)

See Also:

- [About Starting Up an Oracle ASM Instance](admin-asm-instance.md) for information about starting up an Oracle ASM instance
- [Managing Oracle ASM With ASMCA](manage-asm-asmca.md) for information about administering Oracle ASM disk groups with Oracle ASM Configuration Assistant (ASMCA)
- [Managing Oracle ASM with ASMCMD](manage-asm-asmcmd.md) for information about administering Oracle ASM disk groups with ASMCMD
- The Oracle Cloud Storage page on the Oracle Technology Network website at [`http://www.oracle.com/technetwork/database/cloud-storage/index.html`](http://www.oracle.com/technetwork/database/cloud-storage/index.html) for more information about Oracle ASM