---
title: tenant_task_queue_size
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702112.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# tenant_task_queue_size

## 功能描述

`tenant_task_queue_size` 用于设置每个租户的请求队列大小。

## 属性描述

|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | Int          |
| 默认值              | 16384 <main id="notice" type='explain'><h4>说明</h4><p>该配置项从 V4.1.0 版本开始默认值由 65536 调整为 16384。</p></main>      |
| 取值范围             | \[1024, +∞) |
| 是否可修改           | 是，支持通过 `ALTER SYSTEM SET` 语句修改。|
| 是否重启 OBServer 节点生效 | 否           |

## 配置示例

设置每个租户的请求队列大小 1024。

```shell
obclient> ALTER SYSTEM SET tenant_task_queue_size = 1024;
```
