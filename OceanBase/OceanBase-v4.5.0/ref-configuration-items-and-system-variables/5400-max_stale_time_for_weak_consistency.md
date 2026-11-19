---
title: max_stale_time_for_weak_consistency
book: "配置项和系统变量"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004478895.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# max_stale_time_for_weak_consistency

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该配置项从 V1.4 版本开始引入。</p>
</main>

## 功能描述

`max_stale_time_for_weak_consistency` 用于设置弱一致性读允许读到多旧的数据。

## 权限要求

* 查询配置项

  `sys` 租户和所有用户租户均可以使用 `SHOW PARAMETERS` 语句或视图 `GV$OB_PARAMETERS` 查询该配置项。

* 修改配置项

  `sys` 租户和用户租户均可修改该配置项。

## 属性说明

|      **属性**      |    **描述**    |
|------------------|--------------|
| 参数类型             | Time      |
| 默认值               | 5s        |
| 取值范围             | [5s, +∞) |
| 是否可修改           | 是，支持通过 `ALTER SYSTEM SET` 语句修改。|
| 是否重启 OBServer 节点生效 | 否，设置后立即生效。     |

## 配置示例

设置弱一致性读模式下读取的数据最多落后主副本（Leader）的时长不超过为 5s。

```shell
obclient> ALTER SYSTEM SET max_stale_time_for_weak_consistency= '5s';
```
