---
title: "修改租户配置项"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077874.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 修改租户配置项

本文介绍如何通过 API 设置指定租户的配置项，支持一次性设置指定租户的多个配置项。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

PUT /api/v1/tenant/:name/parameters

### 请求参数

[TABLE]

### 返回结果

[TABLE]

## 示例

### 请求示例

PUT 10.10.10.1:2886/api/v1/tenant/t1/parameters

``` json
{
    "parameters": {
        "backup_data_file_size": "2G",
        "arbitration_timeout": "10s"
    }
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T11:27:13.084193081+08:00",
    "duration": 67,
    "status": 200,
    "traceId": "5932e4b9b304ad3d"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [修改租户配置项](700-modify-tenant-configuration-items-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [修改租户配置项](700-modify-tenant-configuration-items-of-go.md)。
