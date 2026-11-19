---
title: READ_RAW
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287033.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# READ_RAW

`READ_RAW` 用于读取 HTTP 响应体中的二进制数据。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.READ_RAW(
   r     IN OUT NOCOPY resp,
   data  OUT NOCOPY RAW,
   len   IN PLS_INTEGER DEFAULT NULL);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|HTTP 请求|
|data|HTTP 响应体中读取到的二进制格式数据|
|len|读取数据的字节数，默认为空，代表读取尽可能多的字符到 data|
