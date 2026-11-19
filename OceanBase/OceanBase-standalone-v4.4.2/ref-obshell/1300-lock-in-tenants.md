---
title: "锁定租户"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077879.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 锁定租户

本文介绍如何通过 API 锁定指定的租户。租户被锁定后，不能在该租户上创建新的连接，已有连接保持不变。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/tenant/:name/lock

### 返回结果

[TABLE]

## 示例

### 请求示例

POST 10.10.10.1:2886/api/v1/tenant/t1/lock

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T10:29:49.199126252+08:00",
    "duration": 59,
    "status": 200,
    "traceId": "0f40c14342ff2e32"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [锁定租户](1300-lock-in-tenants-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [锁定租户](1300-lock-in-tenants-of-go.md)。
