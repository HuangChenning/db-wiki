---
title: "使用 obdiag 一键收集并行 SQL/慢 SQL 诊断信息最佳实践"
book: "诊断"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489658.html"
tags:
  - oceanbase
  - best-practices
  - diagnostic
---

# 使用 obdiag 一键收集并行 SQL/慢 SQL 诊断信息最佳实践

#### 说明

- obdiag 部署简单，可以部署到任一台能够连接到集群各节点的服务器上，并不局限于 OBServer 节点。
- obdiag 具备集中式收集的特点，程序单点部署，无需每台服务器部署。使用时只需要在部署机器上执行收集、巡检或分析命令即可。

#### 说明

OceanBase 数据库 V4.0.0 以下版本可从 `GV$SQL_AUDIT` 查看 trace_id，OceanBase 数据库 V4.0.0 及以上版本可从 `GV$OB_SQL_AUDIT` 查看 trace_id。

#### 说明

需确保待诊断 SQL 为执行 `SELECT last_trace_id();` 命令的前一条 SQL。

#### 说明

需要确保已经在 obdiag 配置文件 `config.yml` 中配置好需要收集的集群 sys 连接信息。关于 obdiag 配置相关的更多信息，请参见 [obdiag 配置](https://www.oceanbase.com/docs/common-obdiag-cn-1000000001102502)。

#### 说明

使用浏览器打开时，需将 **resources** 文件夹一并放到目录下，否则打开的结果中看不到前端样式。

#### 说明

关于 Hint 的更多内容，请参考 [Optimizer Hint](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001053019)。
