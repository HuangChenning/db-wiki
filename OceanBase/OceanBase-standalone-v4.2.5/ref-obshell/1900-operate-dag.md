---
title: "操作任务"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286728.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 操作任务

本文档介绍如何操作指定的任务。支持的操作包括回滚、重试、取消和跳过。

## 调用说明

### 接口约束

- 只有状态是 `FAILED` 的任务支持回滚、重试和跳过。

- 只有未完成的任务支持取消。

- obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/task/dag/{id}

### 请求参数

[TABLE]

### 返回结果

[TABLE]

## 示例

### 请求示例

POST 10.10.10.1:2886/api/v1/task/22130706433028869

``` json
{
    "operator": "ROLLBACK"
}
```

22130706433028869 是一个 `Initialize cluster` 任务的通用 ID，该任务已经失败。

### 返回示例

示例中返回了操作请求成功的结果，但任务操作结果未知，需要通过查询任务获取。

``` json
{
    "successful": true,
    "timestamp": "2024-01-10T14:44:28.366402356+08:00",
    "duration": 1,
    "status": 200,
    "traceId": "7e77b2ba9ee2fa66"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [操作任务](1900-operate-dag-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [操作任务](1900-operate-dag-of-go.md)。
