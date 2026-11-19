---
title: "备份目录结构"
book: "系统原理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577981.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 备份目录结构

#### 说明

尽管 AWS S3 与 NFS、OSS、Azure Blob 等备份介质的日志归档目录结构不相同，但 AWS S3 上的备份文件通过跨云拷贝到其他备份介质上后，仍然支持恢复。例如，将 AWS S3 归档的数据拷贝到 OSS 上，使用该 OSS 路径，仍然可以成功恢复。
