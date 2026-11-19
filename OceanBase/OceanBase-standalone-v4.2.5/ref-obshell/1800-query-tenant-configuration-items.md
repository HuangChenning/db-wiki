---
title: "查询指定的租户配置项"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286763.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查询指定的租户配置项

本文介绍如何通过 API 指定查询租户配置项。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/tenant/:name/parameter/:parameter

### 返回结果

[TABLE]

GvObParameter 的数据结构：

| 参数       | 类型   | 说明               |
|------------|--------|--------------------|
| name       | string | 配置项名称。       |
| value      | string | 配置项的值。       |
| data_type  | string | 配置项的数据类型。 |
| info       | string | 配置项的信息。     |
| edit_level | string | 配置项的修改级别。 |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/tenant/t1/parameter/max_partition_num

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T15:19:46.214458368+08:00",
    "duration": 25,
    "status": 200,
    "traceId": "7fed9977fe59a58f",
    "data": {
        "name": "max_partition_num",
        "value": "8192",
        "data_type": "",
        "info": "set max partition num in mysql mode",
        "edit_level": "DYNAMIC_EFFECTIVE"
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查询租户配置项](1700-query-tenant-configuration-items-of-python.md) 中 **查询指定的租户配置项**。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查询租户配置项](1700-query-tenant-configuration-items-of-go.md) 中 **查询指定的租户配置项**。
