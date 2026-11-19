---
title: "获取 Node 的详细信息"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077860.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取 Node 的详细信息

本文档介绍如何获取一个 Node 的详细信息。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/task/node/{id}

此处的 `id` 需配置为 Node 的通用 ID。

### 返回结果

[TABLE]

NodeDetailDTO 信息的数据结构如下：

| 参数 | 类型 | 说明 |
|----|----|----|
| id | string | Node 通用 ID |
| node_id | int | Node id，是记录在 OceanBase 数据库中的主键 |
| name | string | Node 名称 |
| state | string | Node 执行状态 |
| operator | string | Node 执行操作类型 |
| start_time | time.Time | Node 执行起始时间 |
| end_time | time.Time | Node 执行结束时间 |
| additional_data | map\[string\]any | Node 其他数据 |
| sub_tasks | \[\]TaskDetailDTO | Node 内的所有 subTask 信息，详细介绍请参见下文 **TaskDetailDTO 信息的数据结构** |

TaskDetailDTO 信息的数据结构如下：

[TABLE]

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/task/node/11

### 返回示例

示例中展示了名为 `Integrate server config` 的 Node 的信息，执行操作为 `RUN`，执行结果为 `SUCCEED`。

``` json
{
    "successful": true,
    "timestamp": "2024-01-09T21:18:19.721587522+08:00",
    "duration": 10,
    "status": 200,
    "traceId": "cd6c87efd848bb02",
    "data": {
        "id": "11",
        "node_id": 1,
        "name": "Integrate server config",
        "state": "SUCCEED",
        "operator": "RUN",
        "start_time": "2024-01-09T20:40:01.718882+08:00",
        "end_time": "2024-01-09T20:40:02.751743+08:00",
        "additional_data": null,
        "sub_tasks": [
            {
                "id": "11",
                "task_id": 1,
                "name": "Integrate server config",
                "state": "SUCCEED",
                "operator": "RUN",
                "start_time": "2024-01-09T20:40:01.74723+08:00",
                "end_time": "2024-01-09T20:40:01.76717+08:00",
                "additional_data": null,
                "execute_times": 1,
                "execute_agent": {
                    "ip": "10.10.10.1",
                    "port": 2886
                },
                "task_logs": []
            }
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取 Node 的详细信息](2100-get-node-detail-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取 Node 的详细信息](2100-get-node-detail-of-go.md)。
