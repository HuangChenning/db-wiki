---
title: "物理备份与恢复概述"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577392.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 物理备份与恢复概述

#### 注意

在进行物理备份操作时，需要先开启日志归档模式后，才能执行数据备份。

#### 说明

数据备份会备份系统变量和租户配置项，但不会备份集群级配置项以及私有系统表数据。

#### 注意

通过快速恢复方式恢复出来的租户不支持手动发起合并，不支持数据备份，也不支持 Switchover/Failover 成主库，只能作为备库存在。

#### 说明

尽管 AWS S3 及以兼容 S3 协议访问的备份介质与 OSS、NFS、Azure Blob 等备份介质的日志归档目录结构不相同，但将这些备份介质上的备份文件通过跨云拷贝到 OSS、NFS、Azure Blob 等备份介质上后，仍然支持恢复。例如，将 AWS S3 归档的数据拷贝到 OSS 上，使用该 OSS 路径，仍然可以成功恢复。
