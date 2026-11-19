---
title: "修改单个租户日志归档状态"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975975.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 修改单个租户日志归档状态

本文介绍如何通过 API 修改单个租户日志归档状态。

## 调用说明

### 接口约束

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

PATCH /api/v1/tenant/:name/backup/log

### 请求参数

| 参数 | 类型 | 必选 | 示例值 | 描述 |
|----|----|----|----|----|
| status | string | 否 | "stop" | 日志归档状态，支持设置为 `stop` 和 `doing`，默认为 `stop`。 |

### 返回结果

[TABLE]

## 示例

### 请求示例

PATCH 10.10.10.1:2886/api/v1/tenant/t1/backup/log

``` json
{
  "status": "stop",
}
```

### 返回示例

``` json
{
  "successful": true,
  "timestamp": "2024-01-09T17:11:43.385889278+08:00",
  "duration": 1,
  "status": 200,
  "traceId": "877fe32b83634153",
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [修改单个租户日志归档状态](1100-modify-individual-tenant-logs-archive-status-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [修改单个租户日志归档状态](1100-modify-individual-tenant-logs-archive-status-of-go.md)。
