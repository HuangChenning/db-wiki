---
title: WRITE_LINE
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480124.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# WRITE_LINE

`WRITE_LINE` 用于在 HTTP 请求体中写入一行文本数据。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.WRITE_LINE(
   r     IN OUT NOCOPY req,
   data  IN VARCHAR2 CHARACTER SET ANY_CS);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|HTTP 请求|
|data|要写入的文本数据|
