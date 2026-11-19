---
title: STOP_COVERAGE
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286854.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# STOP_COVERAGE

`STOP_COVERAGE` 用于关闭覆盖率统计，关闭后将结果汇总到数据统计表。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包子程序从 V4.4.1 版本开始支持。</code>。</p>
</main>

## 语法

```sql
DBMS_PLSQL_CODE_COVERAGE.STOP_COVERAGE;
```

## 示例

关闭覆盖率信息统计:

```sql
call DBMS_PLSQL_CODE_COVERAGE.stop_coverage();
```
