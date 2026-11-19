---
title: PRINT_BACKTRACE
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480220.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# PRINT_BACKTRACE

`PRINT_BACKTRACE` 函数用于打印当前执行堆栈的回溯列表。仅当程序正在运行时才应调用此函数。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版暂不支持。</p>
  </main>

## 语法

```sql
DBMS_DEBUG.PRINT_BACKTRACE (
listing IN OUT VARCHAR);
```

## 参数解释

| **参数**  |     **解释**      |
|---------|-----------------|
| listing | 嵌入换行符的格式化字符缓冲区。 |
