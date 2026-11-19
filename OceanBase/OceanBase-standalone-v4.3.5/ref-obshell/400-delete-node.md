---
title: "在集群初始化前删除节点"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975943.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 在集群初始化前删除节点

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

DELETE /api/v1/agent

POST /api/v1/agent/remove

### 请求参数

| 参数 | 类型   | 必选 | 示例值     | 描述                       |
|------|--------|------|------------|----------------------------|
| ip   | string | 是   | 10.10.10.1 | 希望删除的 obshell 的 IP   |
| port | int    | 是   | 2886       | 希望删除的 obshell 的 Port |

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

``` json
  {
   "ip":"10.10.10.1", 
   "port":2886
  }
```

### 返回示例

``` json
{
  "successful": true,
  "timestamp": "2024-01-09T11:53:04.340558805+08:00",
  "duration": 1,
  "status": 200,
  "traceId": "1a4ef28ea713c837",
  "data": {
    "id": "22130706433028869",
    "dag_id": 2,
    "name": "Remove all agents",
    "stage": 1,
    "max_stage": 2,
    "state": "READY",
    "operator": "RUN",
    "start_time": "2024-01-09T11:53:04.339374213+08:00",
    "end_time": "2024-01-09T11:53:04.339374213+08:00",
    "additional_data": null,
    "nodes": null
  }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [在集群初始化前删除节点](400-delete-node-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [在集群初始化前添加节点](400-delete-node-of-go.md)。
