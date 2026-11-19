---
title: "修改租户访问白名单"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286767.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 修改租户访问白名单

本文介绍如何通过 API 修改指定租户的访问白名单。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

PUT /api/v1/tenant/:name/whitelist

### 请求参数

| 参数      | 类型   | 必选 | 示例值 | 描述               |
|-----------|--------|------|--------|--------------------|
| whitelist | string | 是   | %      | 租户的访问白名单。 |

### 返回结果

[TABLE]

## 示例

### 请求示例

PUT 10.10.10.1:2886/api/v1/tenant/t1/whitelist

``` json
{
    "whitelist": "%"
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T11:42:12.873282458+08:00",
    "duration": 91,
    "status": 200,
    "traceId": "e425830225b2b611"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [修改租户访问白名单](400-modify-tenant-access-whitelist-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [修改租户访问白名单](400-modify-tenant-access-whitelist-of-go.md)。
