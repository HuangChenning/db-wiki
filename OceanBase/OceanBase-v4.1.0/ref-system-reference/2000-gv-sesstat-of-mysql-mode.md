---
title: "GV$SESSTAT"
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701982.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# GV$SESSTAT

GV$SESSTAT
===============================

## 功能

展示所有 OBServer 节点的 Session 级别的统计事件信息。

## 字段说明

| **字段名称** | **类型** | **是否可以为 NULL** | **描述** |
| --- | --- | --- | --- |
| SID | bigint(20) | NO | Session 的 ID |
| CON_ID | bigint(20) | NO | 租户 ID |
| SVR_IP | varchar(46) | NO | 信息所在 Server 的 IP |
| SVR_PORT | bigint(20) | NO | 信息所在 Server 的端口号 |
| STATISTICS# | bigint(20) | NO | 统计事件的下标 |
| VALUE | bigint(20) | NO | 统计事件发生的次数 |
