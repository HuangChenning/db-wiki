---
title: max_kept_major_version_number
book: "配置项和系统变量"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479138.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# max_kept_major_version_number

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于该配置项会保留旧的基线版本，进而占用额外的存储空间，且用户的整体使用率较低，从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`max_kept_major_version_number` 用于设置数据保留的冻结版本数量。

## 属性说明

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | Int        |
| 默认值              | 2         |
| 取值范围             | \[1, 16\] |
| 是否重启 OBServer 节点生效 | 否         |
