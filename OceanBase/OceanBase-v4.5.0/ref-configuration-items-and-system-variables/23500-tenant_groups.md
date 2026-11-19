---
title: tenant_groups
book: "配置项和系统变量"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479053.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# tenant_groups

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本中不再支持租户组功能，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`tenant_groups` 用于设置负载均衡策略中使用的租户组。

## 属性说明

|      **属性**      | **描述** |
|------------------|--------|
| 参数类型                      | String  |
| 默认值              | 空值     |
| 是否重启 OBServer 节点生效 | 否      |
