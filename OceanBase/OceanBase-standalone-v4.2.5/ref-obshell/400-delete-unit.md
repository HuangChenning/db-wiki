---
title: "删除资源规格"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286753.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 删除资源规格

本文介绍如何通过 API 删除指定的 unit 资源规格。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

DELETE /api/v1/unit/config/:name

### 返回结果

[TABLE]

## 示例

### 请求示例

DELETE 10.10.10.1:2886/api/v1/unit/config/s1

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T16:14:51.852430189+08:00",
    "duration": 14,
    "status": 200,
    "traceId": "f44c8455e0a8b1a1"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [删除资源规格](400-delete-unit-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [删除资源规格](400-delete-unit-of-go.md)。
