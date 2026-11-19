---
title: "系统内存不足/泄漏"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077585.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 系统内存不足/泄漏

在 OceanBase 中，除了业务租户的 MEMstore 内存满导致写入阻塞的场景，还有一些其他模块的内存不足或泄漏导致的写入或者查询问题，例如 500 租户、sys 租户等。本文介绍系统模块内存不足或泄漏的应急处理方法。

## 应急处理方法

对于 OB 系统模块内存不足或泄漏，一般原因是遇到特殊场景或者触发了软件 bug，应急处理时一般处理方法为隔离或重启问题节点。

### 重启 OBServer 节点

对于系统内部模块的内存问题，一般考虑重启 OBServer 节点解决。建议您通过 OCP 执行指定节点的重启操作，重启 OBServer 节点详细信息请参见 [重启 OBServer 节点](https://www.oceanbase.com/docs/enterprise-oceanbase-ocp-cn-10000000002101077)。
