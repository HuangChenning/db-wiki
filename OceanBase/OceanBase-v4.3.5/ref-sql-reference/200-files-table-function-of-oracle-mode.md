---
title: "FILES 表函数"
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006089277.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# FILES 表函数

## 描述

`FILES(...)` 用于把外部文件位置映射为可查询行集，支持在 `SELECT ... FROM` 中直接读取外部数据。

## 语法

``` sql
FILES(location_expr, format_expr [, pattern_expr])
```

常见写法如下：

``` sql
SELECT * FROM
FILES(
  location = '/data/',
  format (TYPE = 'csv', field_delimiter = ',', parse_header = true),
  pattern = 'datafiles$'
);
```

## 参数说明

- `location_expr`：外部数据位置。
- `format_expr`：文件格式配置，常见为 CSV/PARQUET/ORC。
- `pattern_expr`：可选，用于按文件名模式过滤。

## 使用说明

- `FILES(...)` 可直接用于 `SELECT` 的 `FROM` 子句。
- 在 `LOAD DATA` 场景中，也可通过 `FROM FILES(...)` 指定数据来源。

## 相关文档

- [关于外表与外部文件](../ref-database-object-management/100-about-external-tables-of-oracle-mode.md)
- [CREATE EXTERNAL TABLE](1600-create-external-table-of-oracle-mode.md)
- [创建和查询外表](../ref-database-object-management/200-create-a-external-table-of-oracle-mode.md)
- [SELECT 语句（Oracle 模式）](100-simple-select-of-oracle-mode.md)
- [LOAD DATA 语句（Oracle 模式）](1900-load-data-of-oracle-mode.md)
- [TABLE FUNCTION 概述（Oracle 模式）](100-table-functions-overview-of-oracle-mode.md)
