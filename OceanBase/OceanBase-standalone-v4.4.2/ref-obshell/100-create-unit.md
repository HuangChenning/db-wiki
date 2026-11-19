---
title: "创建资源规格"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077919.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 创建资源规格

本文介绍如何通过 API 创建 unit 资源规格。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/unit/config

### 请求参数

[TABLE]

### 返回结果

[TABLE]

## 示例

### 请求示例

``` json
{
    "name":"s1", 
    "memory_size": "5GB",
    "max_cpu": 3,
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-09-24T19:59:04.310305176+08:00",
    "duration": 10,
    "status": 200,
    "traceId": "7d9bd52cc65cd449"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [创建资源规格](100-create-unit-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [创建资源规格](100-create-unit-of-go.md)。
