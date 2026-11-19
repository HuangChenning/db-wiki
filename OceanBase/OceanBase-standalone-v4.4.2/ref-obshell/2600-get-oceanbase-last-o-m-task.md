---
title: "查询 OceanBase 集群的最后一个运维任务"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077861.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查询 OceanBase 集群的最后一个运维任务

本文档介绍如何查询 OceanBase 集群的最后一个集群运维任务。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/task/dag/maintain/ob

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

GET /api/v1/task/dag/maintain/ob

### 返回示例

示例中返回了的集群的最后一个运维任务 `Drop tenant` 的详细内容，执行操作为 `RUN`，执行结果为 `SUCCEED`。

``` json
{
  "successful": true,
  "timestamp": "2025-09-03T11:59:18.644419629+08:00",
  "duration": 21,
  "status": 200,
  "traceId": "d351674e293a9cde",
  "data": {
    "id": "11000004",
    "dag_id": 1000004,
    "name": "Drop tenant",
    "stage": 2,
    "max_stage": 2,
    "maintenance_type": 3,
    "maintenance_key": "t2",
    "state": "SUCCEED",
    "operator": "RUN",
    "start_time": "2025-09-03T11:57:57.203314+08:00",
    "end_time": "2025-09-03T11:58:00.270197+08:00",
    "additional_data": {},
    "nodes": [
      {
        "id": "11000007",
        "node_id": 1000007,
        "name": "Drop tenant",
        "state": "SUCCEED",
        "operator": "RUN",
        "start_time": "2025-09-03T11:57:57.209677+08:00",
        "end_time": "2025-09-03T11:57:58.227403+08:00",
        "additional_data": null,
        "sub_tasks": [
          {
            "id": "11000007",
            "task_id": 1000007,
            "name": "Drop tenant",
            "state": "SUCCEED",
            "operator": "RUN",
            "start_time": "2025-09-03T11:57:57.221353+08:00",
            "end_time": "2025-09-03T11:57:57.322226+08:00",
            "additional_data": null,
            "execute_times": 1,
            "execute_agent": {
              "ip": "10.10.10.1",
              "port": 2886
            },
            "task_logs": [
              "Drop tenant t2",
              "Resource pool list: [t2_zone1_1756871663]"
            ]
          }
        ]
      },
      {
        "id": "11000008",
        "node_id": 1000008,
        "name": "Drop resource pools",
        "state": "SUCCEED",
        "operator": "RUN",
        "start_time": "2025-09-03T11:57:59.245192+08:00",
        "end_time": "2025-09-03T11:58:00.265971+08:00",
        "additional_data": null,
        "sub_tasks": [
          {
            "id": "11000008",
            "task_id": 1000008,
            "name": "Drop resource pools",
            "state": "SUCCEED",
            "operator": "RUN",
            "start_time": "2025-09-03T11:57:59.260121+08:00",
            "end_time": "2025-09-03T11:57:59.272864+08:00",
            "additional_data": null,
            "execute_times": 1,
            "execute_agent": {
              "ip": "10.10.10.1",
              "port": 2886
            },
            "task_logs": [
              "Drop resource pool t2_zone1_1756871663"
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

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查询 OceanBase 集群的最后一个运维任务](2600-get-oceanbase-last-o-m-task-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查询 OceanBase 集群的最后一个运维任务](2600-get-oceanbase-last-o-m-task-of-go.md)。
