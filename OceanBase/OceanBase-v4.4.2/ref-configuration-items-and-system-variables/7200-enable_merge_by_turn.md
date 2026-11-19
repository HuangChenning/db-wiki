---
title: enable_merge_by_turn
book: "配置项和系统变量"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285888.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# enable_merge_by_turn

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本中不再支持轮转合并功能，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`enable_merge_by_turn` 用于设置是否开启轮转合并策略。

## 属性说明

|      **属性**      |                          **描述**                            |
|------------------|------------------------------------------------------------------|
| 参数类型             | Bool                                                         |
| 默认值              | False                                                            |
| 取值范围             | <ul><li>True：开启 </li><li>False：不开启 </li></ul>     |
| 是否重启 OBServer 节点生效 | 否                                                      |
