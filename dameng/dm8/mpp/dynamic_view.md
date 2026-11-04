---
title: "动态视图"
book: "DM8 大规模并行处理MPP"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dynamic_view.html
tags:
  - dameng
  - dm8
  - mpp
---

DM MPP 提供一系列动态视图供用户查看当前的系统运行状况。

## 7.1 V$MPP\_CFG\_SYS

显示系统全局配置信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SYS\_STATE | VARCHAR(128) | 系统状态 |
| 2 | N\_SITE | INTEGER | 总站点数 |
| 3 | N\_ERR\_SITE | INTEGER | 故障站点数 |
| 4 | SELF\_EP\_SEQNO | INTEGER | 当前站点序号 |

## 7.2 V$MPP\_CFG\_ITEM

显示当前站点配置信息。

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | SERVICE\_NAME | VARCHAR(128) | 服务名 |
| 2 | INST\_NAME | VARCHAR(128) | 实例名 |
| 3 | EP\_SEQNO | INTEGER | 站点序号 |
| 4 | STATE | VARCHAR (128) | 站点状态 |