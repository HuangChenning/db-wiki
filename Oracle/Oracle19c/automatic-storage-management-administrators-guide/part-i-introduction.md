---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-i-introduction.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Part I Introduction

Part I provides an overview of Oracle Automatic Storage Management (Oracle ASM), Oracle ASM Cluster File System (Oracle ACFS), and Oracle ASM Dynamic Volume Manager (Oracle ADVM) concepts and features in the following chapters:

## Introducing Oracle Automatic Storage Management

This chapter presents Oracle ASM as an integrated volume manager and file system for single-instance databases and Oracle RAC, using disk groups to distribute, mirror, and manage database files with minimal downtime. It explains Oracle ASM and Flex ASM instances, disk groups, disks, allocation units, files, extents, striping, templates, failure groups, and redundancy options, and describes storage administration activities including disk discovery, mounting, adding and dropping disks, and online rebalancing. It also introduces Oracle ACFS and ADVM as extensions for managing general-purpose files and volumes.

Read More: [Introducing Oracle Automatic Storage Management](introducing-oracle-automatic-storage-management.md)

## Exploring Considerations for Oracle ASM Storage

This chapter describes how to plan and prepare storage for Oracle ASM, covering supported resources such as partitions, LUNs, logical volumes, and NFS, along with device ownership, permissions, discovery configuration, and platform-specific preparation. It explains multipathing requirements, recommends separating disk groups by workload, using similarly sized and performing disks, selecting suitable redundancy and failure groups, minimizing contention, aligning RAID stripe sizes with allocation units, and using ASM Filter Driver or platform multipathing to preserve device paths and permissions across restarts.

Read More: [Exploring Considerations for Oracle ASM Storage](exploring-considerations-for-oracle-asm-storage.md)