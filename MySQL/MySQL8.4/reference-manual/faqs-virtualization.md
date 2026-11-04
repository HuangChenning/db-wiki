---
title: "A.18 MySQL 8.4 FAQ: Virtualization Support"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/faqs-virtualization.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

A.18.1. Is MySQL supported on virtualized environments such as Oracle VM, VMWare, Docker, Microsoft Hyper-V, or others?

| **A.18.1.** | Is MySQL supported on virtualized environments such as Oracle VM, VMWare, Docker, Microsoft Hyper-V, or others? |
| --- | --- |
|  | MySQL is supported on virtualized environments, but is certified only for [Oracle VM](http://www.oracle.com/technetwork/server-storage/vm/index.html). Contact Oracle Support for more information.  Be aware of potential problems when using virtualization software. The usual ones are related to performance, performance degradations, slowness, or unpredictability of disk, I/O, network, and memory. |