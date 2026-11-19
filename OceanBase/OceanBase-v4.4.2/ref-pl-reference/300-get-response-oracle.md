---
title: GET_RESPONSE
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005287025.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# GET_RESPONSE

`GET_RESPONSE` 用于获取 HTTP 请求的响应 response。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该系统包从 V4.4.1 版本开始引入。</p>
</main>

## 语法

```sql
UTL_HTTP.GET_RESPONSE (
   r                       IN OUT NOCOPY req,
   return_info_response    IN BOOLEAN DEFAULT FALSE) 
RETURN resp;
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|r|HTTP 请求|
|return_info_response|是否将 server 端的 100 informational response 返回，默认为否|
