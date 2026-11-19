---
title: "查询 Agent 未完成的任务"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286733.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查询 Agent 未完成的任务

本文档介绍如何查询指定节点未完成的本地任务。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/task/dag/agent/unfinish

### 请求参数

| 参数 | 类型 | 必选 | 示例值 | 描述 |
|----|----|----|----|----|
| show_detail | bool | 否 | true | 控制是否需要展示 subTask 的详细信息，默认为 `true`，即需要展示。 |

### 返回结果

[TABLE]

DagDetailDTO 信息的数据结构如下：

| 参数 | 类型 | 说明 |
|----|----|----|
| id | string | DAG 通用 ID。 |
| dag_id | int | DAG id，是记录在 OceanBase 数据库中的主键。 |
| name | string | DAG 名称。 |
| stage | int | DAG 的当前执行阶段。 |
| max_stage | int | DAG 执行过程中的总阶段数。 |
| state | string | DAG 执行状态。 |
| operator | string | DAG 执行操作类型。 |
| start_time | time.Time | DAG 执行起始时间。 |
| end_time | time.Time | DAG 执行结束时间。 |
| additional_data | map\[string\]any | DAG 其他数据。 |
| nodes | \[\]NodeDetailDTO | DAG 内的所有 Node 信息，详见 [获取 Node 的详细信息](2100-get-node-detail.md)。 |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/task/dag/agent/unfinish

### 返回示例

示例中展示了指定节点中未完成的 `Update observer config` 任务。

``` json
{
    "successful": true,
    "timestamp": "2024-01-10T11:42:16.770290833+08:00",
    "duration": 0,
    "status": 200,
    "traceId": "6f10ba950d302e27",
    "data": {
        "contents": [
            {
                "id": "22130706433028869",
                "dag_id": 5,
                "name": "Update observer config",
                "stage": 1,
                "max_stage": 1,
                "state": "READY",
                "operator": "RUN",
                "start_time": "2024-01-10T11:42:16.568658722+08:00",
                "end_time": "2024-01-10T11:42:16.568658722+08:00",
                "additional_data": null,
                "nodes": [
                    {
                        "id": "22130706433028869",
                        "node_id": 5,
                        "name": "Update observer config",
                        "state": "PENDING",
                        "operator": "RUN",
                        "start_time": "2024-01-10T11:42:16.568940443+08:00",
                        "end_time": "2024-01-10T11:42:16.568940443+08:00",
                        "additional_data": null,
                        "sub_tasks": [
                            {
                                "id": "22130706433028869",
                                "task_id": 5,
                                "name": "Update observer config",
                                "state": "PENDING",
                                "operator": "RUN",
                                "start_time": "2024-01-10T11:42:16.569166163+08:00",
                                "end_time": "2024-01-10T11:42:16.569166163+08:00",
                                "additional_data": null,
                                "execute_times": 0,
                                "execute_agent": {
                                    "ip": "10.10.10.1",
                                    "port": 2886
                                },
                                "task_logs": null
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查询 Agent 未完成的任务](2400-get-agent-unfinish-task-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查询 Agent 未完成的任务](2400-get-agent-unfinish-task-of-go.md)。
