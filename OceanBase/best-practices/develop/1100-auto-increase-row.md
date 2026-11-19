---
title: "OceanBase 自增列与序列最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003629554.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# OceanBase 自增列与序列最佳实践

#### 说明

序列和自增列的区别：

- 创建序列时，默认为 NOORDER 属性（为了和 Oracle 行为兼容）。
- 创建自增列时，默认为 ORDER 属性（为了和 MySQL 行为兼容）。

#### 说明

该场景下，仅作为 Leader 的 OBServer 节点发生重启或宕机时，才会发生自增值跳变的问题，其他作为 Follower 的 OBServer 节点由于不保存缓存，即使发生了宕机也不会影响自增值生成的连续性。

#### 说明

- 若业务不能容忍跳变，可关闭缓存（NOCACHE），但需接受性能下降。
- 序列在 V4.2.3 后支持 order + cache，也可以避免跳变。

#### 注意

ORDER 模式需跨节点协调，成本高，仅在金融等强有序场景使用。

#### 说明

在单机版本中，ORDER 和 NOORDER 模式的性能差异不明显。然而，在多机（多分区）场景下，NOORDER 模式在高并发情况下的性能优于 ORDER 模式。

#### 说明

在创建序列时，由于默认的 CACHE 值过小，需要手动声明。单机 TPS 为 100 时，CACHE SIZE 建议设置为 360000。

您也可以使用 ORDER + CACHE，每隔 CACHE 个值会操作内部表，可以避免跳变。
