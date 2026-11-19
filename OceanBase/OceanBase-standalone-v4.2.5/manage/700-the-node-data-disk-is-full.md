---
title: "节点数据盘空间满"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702043.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 节点数据盘空间满

OceanBase 数据盘空间满的情况一般比较少见，但是在写满后也会导致无法转储、无法合并、内存无法释放的问题，进而导致集群无法写入。

## 应急处理流程

处理数据盘空间满的几个策略如下：

- 调大 OceanBase 集群磁盘最大空间百分比。

  ``` sql
  ALTER system SET datafile_disk_percentage = 98;
  ```

  该参数默认值为 `90`，应急时调大可以临时释放一部分空间。

- 删除部分可删除的数据、表、冗余索引等，并清空回收站中的数据。回收站的数据清理后就无法恢复，清理数据请您反复确认无误后才可执行。
