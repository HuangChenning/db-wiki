---
title: END_RESPONSE
book: "PL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005686690.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# END_RESPONSE

`END_RESPONSE` 用于在完成 HTTP 请求后终止 HTTP 请求的响应 response。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.END_RESPONSE（
   r IN OUT NOCOPY resp）;
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|HTTP 请求|
