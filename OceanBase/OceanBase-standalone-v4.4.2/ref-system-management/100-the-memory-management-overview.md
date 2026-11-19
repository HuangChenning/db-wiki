---
title: "内存管理概述"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077388.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 内存管理概述

OceanBase 集中式数据库是一个支持多租户架构的准内存级的数据库，这对大容量内存的管理和使用提出了很高的要求。OceanBase 数据库采取占据服务器的大部分内存并进行统一管理的方式来管理内存。

当有新业务需要上线时为其创建一个新租户，其中内存是从租户可分配内存中划分资源，租户 CPU 和内存的大小取决于业务规模。当可分配的 CPU 和内存资源不足时，应水平扩展 OceanBase 集群，为不断扩展的业务规模提供可持续的服务能力。

本章节将分篇介绍内存管理相关的以下内容：

- [内存结构](200-memory-structure.md)

- [数据库内存上限](300-maximum-database-memory.md)

- [系统内部内存管理](400-system-internal-memory-management.md)

- [租户内部内存管理](500-memory-management-within-a-tenant.md)

- [执行计划缓存内存管理](600-execution-plan-cache-memory-management.md)

- [基于常态化 Memleak 的内存泄露诊断机制](700-use-memleak.md)

- [查看内存的使用信息](800-view-memory-usage.md)

- [常见内存问题](900-common-memory-problems.md)
