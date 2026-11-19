---
title: "修改租户密码"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975965.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 修改租户密码

本文介绍如何通过 API 修改指定租户的 root 用户密码。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

PUT /api/v1/tenant/:name/password

### 请求参数

| 参数         | 类型   | 必选 | 示例值         | 描述                           |
|--------------|--------|------|----------------|--------------------------------|
| old_password | string | 否   | "\*\*\*\*"     | 租户的 root 用户的旧密码。     |
| new_password | string | 是   | "\*\*\*\*\*\*" | 设置租户的 root 用户的新密码。 |

### 返回结果

[TABLE]

## 示例

### 请求示例

PUT 10.10.10.1:2886/api/v1/tenant/t1/password

``` json
{
    "old_password": "",
    "new_password": "******"
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T11:40:00.696664135+08:00",
    "duration": 120,
    "status": 200,
    "traceId": "66b976ef15984730"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [修改租户密码](300-change-tenant-password-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [修改租户密码](300-change-tenant-password-of-go.md)。
