---
title: trx_try_wait_lock_timeout
book: "配置项和系统变量"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015824.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# trx_try_wait_lock_timeout

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>由于功能调整，该配置项从 V3.1.0 版本开始删除。</p>
</main>

## 功能描述

`trx_try_wait_lock_timeout` 用于设置语句执行过程行锁的等待时长。

## 属性说明

|      **属性**      |     **描述**     |
|------------------|----------------|
| 参数类型             | Time           |
| 默认值               | 0ms            |
| 取值范围             | [0ms, 100ms] |
| 是否重启 OBServer 节点生效 | 否              |
