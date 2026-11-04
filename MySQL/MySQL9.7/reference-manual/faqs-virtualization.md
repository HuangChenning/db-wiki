---
title: "A.18 MySQL 9.7 FAQ: Virtualization Support"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/faqs-virtualization.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

A.18.1. Is MySQL supported on virtualized environments such as Oracle VM, VMWare, Docker, Microsoft Hyper-V, or others?

| **A.18.1.** | Is MySQL supported on virtualized environments such as Oracle VM, VMWare, Docker, Microsoft Hyper-V, or others? |
| --- | --- |
|  | MySQL is supported on virtualized environments, but is certified only for [Oracle VM](http://www.oracle.com/technetwork/server-storage/vm/index.html). Contact Oracle Support for more information.  Be aware of potential problems when using virtualization software. The usual ones are related to performance, performance degradations, slowness, or unpredictability of disk, I/O, network, and memory. |