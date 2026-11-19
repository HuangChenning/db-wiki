---
title: "日志压缩与解压"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577424.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志压缩与解压

#### 说明

具体磁盘空间大小以硬件规格和实际需求为准，如果想占满整个磁盘可以设置为 0GB。

#### 说明

具体数量以实际需求为准，例如将该值设置为 50，那么四种日志一共有 200 个不压缩的文件，每个 256MB，总大小约为 50GB。
