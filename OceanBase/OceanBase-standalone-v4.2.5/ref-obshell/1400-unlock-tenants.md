---
title: "解锁租户"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286759.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 解锁租户

本文介绍如何通过 API 解锁被锁定的租户。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

DELETE /api/v1/tenant/:name/lock

### 返回结果

[TABLE]

## 示例

### 请求示例

DELETE 10.10.10.1:2886/api/v1/tenant/t1/lock

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T10:36:09.901853967+08:00",
    "duration": 56,
    "status": 200,
    "traceId": "8c80798010e1b469"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [解锁租户](1400-unlock-tenants-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [解锁租户](1400-unlock-tenants-of-go.md)。
