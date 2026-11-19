---
title: SET_TRANSFER_TIMEOUT
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480120.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# SET_TRANSFER_TIMEOUT

`SET_TRANSFER_TIMEOUT` 用于设置 HTTP 传输数据的超时时间上限。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.SET_TRANSFER_TIMEOUT (
   timeout  IN PLS_INTEGER DEFAULT 60);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|timeout|要设置的超时时间上限，单位为秒|
