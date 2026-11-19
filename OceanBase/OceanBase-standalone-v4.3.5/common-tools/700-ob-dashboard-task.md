---
title: "任务管理"
book: "常用工具"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975923.html"
tags:
  - oceanbase
  - standalone
  - common-tools
---

# 任务管理

#### 说明

上述中提到的 **共存** 和 **互斥** 的概念都是针对未完成的任务，以本地任务类型中的全局运维任务为例，当存在未完成的全局运维任务时，无法发起另一个全局运维任务，但可以发起另一个 OBProxy 运维任务。

#### 说明

在任务执行过程中，单击 **定位当前进度**，可快速跳转至正在执行的子任务，方便您关注任务执行状态及相关日志信息；对于 **失败** 的任务，单击 **定位当前进度**，可快速定位执行失败的子任务及任务执行异常信息。
