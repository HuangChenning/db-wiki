---
title: END_REQUEST
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287027.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# END_REQUEST

`END_REQUEST` 用于强制关闭一个 request。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.END_RESPONSE (
   r  IN OUT NOCOPY resp);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|需要终止的请求 req|
