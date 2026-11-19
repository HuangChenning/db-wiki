---
title: "删除指定的资源池"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077921.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 删除指定的资源池

本文介绍如何通过 API 删除指定的未被使用的资源池。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

DELETE /api/v1/resource-pool/:name

### 返回结果

[TABLE]

## 示例

### 请求示例

DELETE 10.10.10.1:2886/api/v1/resource-pool/p1

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T15:46:12.947201503+08:00",
    "duration": 13,
    "status": 200,
    "traceId": "b3792e6360025da5"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [删除资源池](200-delete-the-specified-rp-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [删除资源池](200-delete-the-specified-rp-of-go.md)。
