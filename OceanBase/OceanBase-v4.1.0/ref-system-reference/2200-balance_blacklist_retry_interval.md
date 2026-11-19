---
title: balance_blacklist_retry_interval
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002173606.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# balance_blacklist_retry_interval

balance_blacklist_retry_interval 
=====================================================

`balance_blacklist_retry_interval` 用于设置副本迁移等后台任务被放入黑名单后的重试时间间隔。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |    **描述**    |
|------------------|--------------|
| 参数类型             | 时间类型         |
| 默认值              | 30m，表示 30 分钟 |
| 取值范围             | \[0s, 180m\] |
| 是否重启 OBServer 节点生效 | 否            |
