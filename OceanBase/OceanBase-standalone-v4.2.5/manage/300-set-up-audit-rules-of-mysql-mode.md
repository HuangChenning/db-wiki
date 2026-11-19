---
title: "设置审计规则"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702013.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 设置审计规则

#### 说明

先开启审计再修改输出路径的情况，修改 `audit_log_path` 后不会立即切换到新目录，需等待当前 `audit.log` 写满并触发轮转（由 `audit_log_rotate_on_size` 控制，参见下文`设置日志归档`）后，新生成的日志才会写入新路径。

#### 说明

仅压缩归档后的文件，`audit.log` 文件是不压缩的。
