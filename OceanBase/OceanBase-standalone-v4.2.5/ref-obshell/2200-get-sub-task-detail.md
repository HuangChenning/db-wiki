---
title: "获取 subTask 的详细信息"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286731.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取 subTask 的详细信息

本文档介绍如何获取一个 subTask 的详细信息。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/task/sub_task/{id}

此处的 `id` 需配置为 subTask 的通用 ID。

### 返回结果

[TABLE]

TaskDetailDTO 信息的数据结构如下：

[TABLE]

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/task/sub_task/12

### 返回示例

示例中展示了名为 `Create local scale out dag` 的 subTask 的信息，执行操作为 `RUN`，执行结果为 `SUCCEED`。

``` json
{
    "successful": true,
    "timestamp": "2024-01-09T21:29:37.372338686+08:00",
    "duration": 6,
    "status": 200,
    "traceId": "638aa02fc5b50051",
    "data": {
        "id": "12",
        "task_id": 2,
        "name": "Create local scale out dag",
        "state": "SUCCEED",
        "operator": "RUN",
        "start_time": "2024-01-09T20:40:03.796683+08:00",
        "end_time": "2024-01-09T20:40:03.836712+08:00",
        "additional_data": null,
        "execute_times": 1,
        "execute_agent": {
            "ip": "10.10.10.1",
            "port": 2886
        },
        "task_logs": [
            "create local scale out dag success, genericID:22130706433028869"
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取 SubTask 的详细信息](2200-get-sub-task-detail-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取 SubTask 的详细信息](2200-get-sub-task-detail-of-go.md)。
