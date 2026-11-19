---
title: "查询并行度的选择"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577436.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 查询并行度的选择

#### 注意

- 开启 Auto DOP 后，需要关注调整 `parallel_min_scan_time_threshold` 和 `parallel_degree_limit` 两个相关参数的设置，否则 Auto DOP 可能对 AP 系统有不良影响。

&nbsp;

- Auto DOP 仅根据评估的查询执行开销，以减小 RT 为目标决策开启并行并计算 DOP，如果业务负载中存在用户不关注的慢查询，需要使用资源隔离手段进行处理，否则开启 Auto DOP 后，对所有查询使用 Auto DOP 给定并行度，将对系统造成不良影响。

#### 注意

参数类型为系统变量，全局级别修改变量后，只有新建连接可以生效，已有连接需要断连。

#### 注意

参数类型为系统变量，全局级别修改变量后，只有新建连接可以生效，已有连接需要断连。
