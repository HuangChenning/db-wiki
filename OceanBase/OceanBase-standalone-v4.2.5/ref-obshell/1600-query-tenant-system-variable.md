---
title: "查询指定的租户系统变量"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286761.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查询指定的租户系统变量

本文介绍如何通过 API 指定查询租户的系统变量。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/tenant/:name/variable/:variable

### 返回结果

[TABLE]

CdbObSysVariable 的数据结构：

| 参数  | 类型   | 说明             |
|-------|--------|------------------|
| name  | string | 系统变量名称。   |
| value | string | 系统变量的值。   |
| info  | string | 系统变量的信息。 |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/tenant/t1/variable/max_connections

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T15:16:28.044579876+08:00",
    "duration": 20,
    "status": 200,
    "traceId": "3702684711dd0e7b",
    "data": {
        "name": "max_connections",
        "value": "1000",
        "info": ""
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查询租户系统变量](1600-query-tenant-system-variable-of-python.md) 中的 **查询指定的租户系统变量**。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查询租户系统变量](1600-query-tenant-system-variable-of-go.md) 中的 **查询指定的租户系统变量**。
