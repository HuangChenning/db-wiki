---
title: "查询所有未完成的任务"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975933.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查询所有未完成的任务

本文档介绍如何查询集群中所有未完成的任务。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/task/dag/unfinish

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

GET 10.10.10.1:2886/api/v1/task/dag/unfinish

### 返回示例

示例中展示了一个正在创建租户的集群，表示集群中只存在一个未完成的创建租户的任务，各个节点不存在未完成的本地任务。

``` json
{
  "successful": true,
  "timestamp": "2025-09-03T11:54:27.020028685+08:00",
  "duration": 14,
  "status": 200,
  "traceId": "450f80d22315c1e9",
  "data": {
    "contents": [
      {
        "id": "11000003",
        "dag_id": 1000003,
        "name": "Create tenant t2",
        "stage": 1,
        "max_stage": 2,
        "maintenance_type": 3,
        "maintenance_key": "t2",
        "state": "RUNNING",
        "operator": "RUN",
        "start_time": "2025-09-03T11:54:24.191718+08:00",
        "end_time": "2025-09-03T11:54:23.854307+08:00",
        "additional_data": {},
        "nodes": [
          {
            "id": "11000005",
            "node_id": 1000005,
            "name": "Create tenant",
            "state": "RUNNING",
            "operator": "RUN",
            "start_time": "2025-09-03T11:54:24.201981+08:00",
            "end_time": "2025-09-03T11:54:24.201981+08:00",
            "additional_data": null,
            "sub_tasks": [
              {
                "id": "11000005",
                "task_id": 1000005,
                "name": "Create tenant",
                "state": "RUNNING",
                "operator": "RUN",
                "start_time": "2025-09-03T11:54:24.22218+08:00",
                "end_time": "2025-09-03T11:54:23.869532+08:00",
                "additional_data": null,
                "execute_times": 1,
                "execute_agent": {
                  "ip": "10.10.10.1",
                  "port": 2886
                },
                "task_logs": [
                  "Create resource pool: {t2_zone1_1756871663 zone1 s1 1}",
                  "Create resource pool t2_zone1_1756871663 success",
                  "Create tenant sql: CREATE TENANT `t2` resource_pool_list=(\"t2_zone1_1756871663\"), LOCALITY = \"FULL@zone1\", PRIMARY_ZONE = `RANDOM` SET ob_tcp_invited_nodes = ``, ob_compatibility_mode = `MYSQL`"
                ]
              }
            ]
          },
          {
            "id": "11000006",
            "node_id": 1000006,
            "name": "Modify tenant whitelist",
            "state": "PENDING",
            "operator": "RUN",
            "start_time": "2025-09-03T11:54:23.870257+08:00",
            "end_time": "2025-09-03T11:54:23.870257+08:00",
            "additional_data": null,
            "sub_tasks": [
              {
                "id": "11000006",
                "task_id": 1000006,
                "name": "Modify tenant whitelist",
                "state": "PENDING",
                "operator": "RUN",
                "start_time": "2025-09-03T11:54:23.871326+08:00",
                "end_time": "2025-09-03T11:54:23.871326+08:00",
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

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查询所有未完成的任务](2300-get-all-unfinish-task-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查询所有未完成的任务](2300-get-all-unfinish-task-of-go.md)。
