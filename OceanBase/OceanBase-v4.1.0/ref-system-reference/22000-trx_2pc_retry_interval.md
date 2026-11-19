---
title: trx_2pc_retry_interval
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702116.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# trx_2pc_retry_interval

trx_2pc_retry_interval 用于设置两阶段提交失败时候自动重试的时间间隔。


|      **属性**      |     **描述**      |
|------------------|-----------------|
| 参数类型             | 时间类型            |
| 默认值              | 100ms           |
| 取值范围             | \[1ms, 5000ms\] |
| 是否重启 OBServer 节点生效 | 否               |
