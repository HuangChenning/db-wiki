---
title: "获取任务的详细信息"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286729.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取任务的详细信息

本文档介绍如何获取一个任务（DAG）的详细信息。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/task/dag/{id}

此处的 `id` 需配置为 DAG 的通用 ID。

### 请求参数

| 参数 | 类型 | 必选 | 示例值 | 描述 |
|----|----|----|----|----|
| show_details | bool | 否 | true | 控制是否需要展示 DAG 的详细信息，默认为 `true`，即需要展示。 |

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

GET 10.10.10.1:2886/api/v1/task/dag/1000002

### 返回示例

示例中返回了一个名为 `Create tenant t1`（创建租户）任务的详细内容，执行操作为 `RUN`，执行结果为 `SUCCEED`。

``` json
{
  "successful": true,
  "timestamp": "2025-09-02T20:54:08.659175517+08:00",
  "duration": 15,
  "status": 200,
  "traceId": "8000a8e6dcf643da",
  "data": {
    "id": "11000002",
    "dag_id": 1000002,
    "name": "Create tenant t1",
    "stage": 2,
    "max_stage": 2,
    "maintenance_type": 3,
    "maintenance_key": "t1",
    "state": "SUCCEED",
    "operator": "RUN",
    "start_time": "2025-09-02T20:52:58.732118+08:00",
    "end_time": "2025-09-02T20:53:26.06657+08:00",
    "additional_data": {},
    "nodes": [
      {
        "id": "11000003",
        "node_id": 1000003,
        "name": "Create tenant",
        "state": "SUCCEED",
        "operator": "RUN",
        "start_time": "2025-09-02T20:52:58.738477+08:00",
        "end_time": "2025-09-02T20:53:24.019716+08:00",
        "additional_data": null,
        "sub_tasks": [
          {
            "id": "11000003",
            "task_id": 1000003,
            "name": "Create tenant",
            "state": "SUCCEED",
            "operator": "RUN",
            "start_time": "2025-09-02T20:52:58.750104+08:00",
            "end_time": "2025-09-02T20:53:23.402083+08:00",
            "additional_data": null,
            "execute_times": 1,
            "execute_agent": {
              "ip": "10.10.10.1",
              "port": 2886
            },
            "task_logs": [
              "Create resource pool: {t1_zone1_1756817578 zone1 s1 1}",
              "Create resource pool t1_zone1_1756817578 success",
              "Create tenant sql: CREATE TENANT `t1` resource_pool_list=(\"t1_zone1_1756817578\"), LOCALITY = \"FULL@zone1\", PRIMARY_ZONE = `RANDOM` SET ob_tcp_invited_nodes = ``, ob_compatibility_mode = `MYSQL`",
              "Create tenant success, tenant id: 1004"
            ]
          }
        ]
      },
      {
        "id": "11000004",
        "node_id": 1000004,
        "name": "Modify tenant whitelist",
        "state": "SUCCEED",
        "operator": "RUN",
        "start_time": "2025-09-02T20:53:25.038199+08:00",
        "end_time": "2025-09-02T20:53:26.062323+08:00",
        "additional_data": null,
        "sub_tasks": [
          {
            "id": "11000004",
            "task_id": 1000004,
            "name": "Modify tenant whitelist",
            "state": "SUCCEED",
            "operator": "RUN",
            "start_time": "2025-09-02T20:53:25.054041+08:00",
            "end_time": "2025-09-02T20:53:25.106701+08:00",
            "additional_data": null,
            "execute_times": 1,
            "execute_agent": {
              "ip": "10.10.10.1",
              "port": 2886
            },
            "task_logs": [
              "modify tenant 't1' whitelist to ''"
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

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取任务的详细信息](2000-get-dag-detail-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取任务的详细信息](2000-get-dag-detail-of-go.md)。
