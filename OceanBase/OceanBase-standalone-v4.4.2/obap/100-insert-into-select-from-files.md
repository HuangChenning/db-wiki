---
title: INSERT INTO SELECT FROM FILES
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006338108.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# INSERT INTO SELECT FROM FILES

#### 说明

一般情况下，`enable_parallel_dml` Hint 和 `parallel` Hint 必须配合使用才能开启并行 DML。不过，当目标表的 Schema 上指定了表级别的并行度时，仅需指定 `enable_parallel_dml` Hint。

#### 说明

一般情况下，`enable_parallel_dml` Hint 和 `parallel` Hint 必须配合使用才能开启并行 DML。不过，当目标表的 Schema 上指定了表级别的并行度时，仅需指定 `enable_parallel_dml` Hint。
