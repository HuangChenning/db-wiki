---
title: GET_TRANSFER_TIMEOUT
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480121.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# GET_TRANSFER_TIMEOUT

`GET_TRANSFER_TIMEOUT` 用于获取当前的 HTTP 传输数据的超时时间上限。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.GET_TRANSFER_TIMEOUT (
   timeout  OUT PLS_INTEGER);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|timeout|获取到的当前超时时间上限，单位为秒|
