---
title: "升级 Agent"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077866.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 升级 Agent

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/agent/upgrade

### 请求参数

| 参数       | 类型   | 必选 | 示例值                 | 描述                       |
|------------|--------|------|------------------------|----------------------------|
| version    | string | 是   | 4.2.1.1                | 指定升级的目标版本         |
| release    | string | 是   | 101000062023110109.el7 | 指定升级的目标发行版构建号 |
| upgradeDir | string | 否   | /data/upgrade          | 指定升级任务使用的目录     |

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
"{
  "version":"4.2.0.0", 
   "release": "20240109191841.el7"
}"
```

### 返回示例

``` json
{
  "successful": true,
  "timestamp": "2024-01-09T19:26:25.96275587+08:00",
  "duration": 30,
  "status": 200,
  "traceId": "149cd6425a9d256f",
  "data": {
    "id": "12",
    "dag_id": 2,
    "name": "Upgrade obshell 4.2.0.0-20240109191841.el7",
    "stage": 1,
    "max_stage": 9,
    "state": "READY",
    "operator": "RUN",
    "start_time": "0001-01-01T00:00:00Z",
    "end_time": "0001-01-01T00:00:00Z",
    "additional_data": null,
    "nodes": null
  }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [升级 Agent](1200-upgrade-agent-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [升级 Agent](1200-upgrade-agent-of-go.md)。
