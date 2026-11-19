---
title: "获取公钥"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975938.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取公钥

本文介绍如何获取指定节点的公钥。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/secret

### 返回结果

[TABLE]

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/secret

### 返回示例

``` json
{
  "successful": true,
  "timestamp": "2024-01-09T17:29:04.826345518+08:00",
  "duration": 0,
  "status": 200,
  "traceId": "672cc42c132a4b90",
  "data": {
    "ip": "10.10.10.1",
    "port": 2886,
    "public_key": "xxxxxxxxxxx"
  }
}
```
