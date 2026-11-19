---
title: "ODPS 外部表"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006362380.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# ODPS 外部表

#### 说明

若需访问整个 MaxCompute 项目下的多张表且无需逐表建外表，可使用 [ODPS Catalog](100-odps-catalog.md)。本文介绍单表级别的 ODPS 外部表。

#### 说明

`AS (external$tablecolx)` 用于指定映射到 MaxCompute 表的第 x 列普通列（非分区列），序号从 1 开始。若未指定生成列，则按列定义顺序自动递增编号。

#### 说明

- `metadata$partition_list_colx` 用于映射 MaxCompute 表的第 x 个分区列，序号从 1 开始，不可省略。
- MaxCompute 表的分区列与 OceanBase 外表的分区列须一一对应，个数一致。

#### 说明

V4.3.5 BP2 及更高版本支持自动创建 MaxCompute 表中不存在的分区；更低版本须预先在 MaxCompute 侧创建目标分区。
