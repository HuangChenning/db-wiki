---
title: "清除回收站中的租户"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286791.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 清除回收站中的租户

本文介绍如何通过 API 清除回收站中的指定租户。清除指定租户后，该租户所占用的资源池也将被回收。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

DELETE /api/v1/resource-pool/:name

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

DELETE 10.10.10.1:2886/api/v1/resource-pool/t1

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T16:06:06.123724431+08:00",
    "duration": 92,
    "status": 200,
    "traceId": "7790b10d488d0d39",
    "data": {
        "id": "19",
        "dag_id": 9,
        "name": "Wait tenant purge finished",
        "stage": 1,
        "max_stage": 2,
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

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [清除回收站中的租户](300-clear-tenants-from-the-recycle-bin-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [清除回收站中的租户](300-clear-tenants-from-the-recycle-bin-of-go.md)。
