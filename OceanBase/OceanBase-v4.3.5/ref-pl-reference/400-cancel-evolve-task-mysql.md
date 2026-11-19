---
title: CANCEL_EVOLVE_TASK
book: "PL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003273180.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# CANCEL_EVOLVE_TASK

`CANCEL_EVOLVE_TASK` 过程用于取消一个正在演进的任务。

## 语法

```sql
DBMS_SPM.CANCEL_EVOLVE_TASK  (
  database_name     VARCHAR(65535),
  task_name         VARCHAR(65535));
```


## 参数说明

| **参数名称** | **描述** |
| --- | --- |
| database_name | 数据库名称，仅 MySQL 模式下需要指定该参数。 |
| task_name | 任务名称，即当前 OceanBase 数据库中使用 `SQL_ID` 所表示的演进任务名称。 |


## 示例

```sql
BEGIN
  DBMS_SPM.CANCEL_EVOLVE_TASK ('SYS_AUTO_SPM_EVOLVE_TASK');
END;
```
