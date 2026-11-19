---
title: "修改租户系统变量"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286768.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 修改租户系统变量

本文介绍如何通过 API 设置指定租户的系统变量，支持一次性设置指定租户的多个系统变量。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

PUT /api/v1/tenant/:name/variables

### 请求参数

[TABLE]

### 返回结果

[TABLE]

## 示例

### 请求示例

PUT 10.10.10.1:2886/api/v1/tenant/t1/variables

``` json
{
    "variables": {
        "max_connections": 1000,
        "recyclebin": true
    }
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T11:13:36.467293708+08:00",
    "duration": 74,
    "status": 200,
    "traceId": "39ff86cca62a9ec0"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [修改租户系统变量](600-modify-tenant-system-variables-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [修改租户系统变量](600-modify-tenant-system-variables-of-go.md)。
