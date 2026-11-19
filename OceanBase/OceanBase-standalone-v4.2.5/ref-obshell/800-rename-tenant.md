---
title: "重命名租户"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286770.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 重命名租户

本文介绍如何通过 API 重命名租户。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

PUT /api/v1/tenant/:name/name

### 请求参数

| 参数     | 类型   | 必选 | 示例值 | 描述           |
|----------|--------|------|--------|----------------|
| new_name | string | 是   | t2     | 租户的新名称。 |

### 返回结果

[TABLE]

## 示例

### 请求示例

PUT 10.10.10.1:2886/api/v1/tenant/t1/name

``` json
{
    "new_name": "t2"
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T14:35:22.228258964+08:00",
    "duration": 79,
    "status": 200,
    "traceId": "9495a4d5fff255ce"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [重命名租户](800-rename-tenant-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [重命名租户](800-rename-tenant-of-go.md)。
