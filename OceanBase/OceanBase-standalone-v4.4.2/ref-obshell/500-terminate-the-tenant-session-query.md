---
title: "终止租户会话查询"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077853.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 终止租户会话查询

本文介绍如何通过 API 终止指定租户会话正在执行的查询，但保持会话连接。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

DELETE /api/v1/tenant/:name/sessions/queries

### 请求参数

| 参数        | 类型    | 必选 | 示例值           | 描述                               |
|-------------|---------|------|------------------|------------------------------------|
| name        | string  | 是   | t1               | 租户名称。该参数通过路径参数指定。 |
| session_ids | \[\]int | 是   | \[12345, 12346\] | 要终止的会话 ID 列表。             |

### 返回结果

[TABLE]

## 示例

### 请求示例

DELETE 10.10.10.1:2886/api/v1/tenant/t1/sessions/queries

``` json
{
    "session_ids": [3221588508, 3221588509]
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2025-10-14T15:18:01.277047628+08:00",
    "duration": 20,
    "status": 200,
    "traceId": "e6f64ba7f54e7a51"
}
```
