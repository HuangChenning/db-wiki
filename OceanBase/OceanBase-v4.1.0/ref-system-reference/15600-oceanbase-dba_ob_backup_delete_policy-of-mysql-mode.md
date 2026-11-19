---
title: oceanbase.DBA_OB_BACKUP_DELETE_POLICY
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699309.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_OB_BACKUP_DELETE_POLICY

## 功能
展示租户下为过期清理/自动清理设置的清理策略。
## 字段说明

| 字段名称 | 类型 | 是否可以为 NULL | 描述 |
| --- | --- | --- | --- |
| POLICY_NAME | varchar(256) | NO | 清理策略名 |
| RECOVERY_WINDOW | varchar(64) | NO | 可恢复时间窗口，默认值：0 |
