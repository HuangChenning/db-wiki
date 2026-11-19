---
title: "分页查询"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077478.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 分页查询

#### 注意

**分页查询必须使用 `ORDER BY` 子句**，这是 Oracle 数据库的标准规范。如果不使用 `ORDER BY`，分页查询的结果顺序是不确定的，可能导致不同查询返回不同的结果，出现数据重复或遗漏的问题。

#### 注意

- 在**单机非并行场景**下，即使 `ORDER BY` 使用非唯一字段，对于具有相同排序值的行，系统也能保证其顺序的确定性和稳定性，分页结果不会出现数据重复或遗漏。
- 在**并行执行场景**下，如果必须按非唯一字段排序，您需要在 `ORDER BY` 子句中添加唯一字段作为次要排序条件。例如：`ORDER BY department_id, employee_id`，这样可以确保排序结果的唯一性和稳定性。

#### 注意

使用 `ROWNUM` 进行分页查询时， `ROWNUM` 是在数据返回后才分配的，您不能直接在 `WHERE` 子句中使用 `ROWNUM > N` 条件。因此，您要使用子查询来实现分页。
