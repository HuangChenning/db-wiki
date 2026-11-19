---
title: WRITE_RAW
book: "PL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005686687.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# WRITE_RAW

`WRITE_RAW` 用于在 HTTP 请求体中写入二进制数据。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.WRITE_RAW(
   r     IN OUT NOCOPY REQ,
   data  IN            RAW);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|HTTP 请求|
|data|要写入的二进制数据|
