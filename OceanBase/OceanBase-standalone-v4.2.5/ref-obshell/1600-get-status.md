---
title: "查询状态"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286727.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查询状态

本文介绍如何查询节点当前状态，包括节点的身份、进程信息和服务状态等内容。

## 调用说明

### 接口约束

obshell Server 会对该 API 进行安全校验，详细介绍可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/status

### 返回结果

[TABLE]

AgentStatus 信息的数据结构：

[TABLE]

节点的身份标识：

| 标识                                    | 介绍                     |
|-----------------------------------------|--------------------------|
| `SINGLE`                                | 节点不属于任何集群       |
| `FOLLOWER`/`MASTER`                     | 节点归属于未初始化的集群 |
| `CLUSTER AGENT`                         | 节点归属于已初始化的集群 |
| `TAKE OVER MASTER`/`TAKE OVER FOLLOWER` | 节点正处于接管状态中     |
| `UNIDENTIFIED`                          | 节点未定义               |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/status

### 返回示例

示例中返回了一个身份为 `CLUSTER AGENT` 节点的状态，表示当前节点能够正常提供服务，并且不处于运维状态中。

``` json
{
  "successful": true,
  "timestamp": "2024-01-09T20:01:52.466963232+08:00",
  "duration": 3,
  "status": 200,
  "traceId": "",
  "data": {
    "agent": {
        "ip": "10.10.10.1",
        "port": 2886,
        "identity": "CLUSTER AGENT"
    },
    "state": 2,
    "version": "4.2.1.0-0",
    "pid": 74314,
    "startAt": 1704801582437828890,
    "port": 2886,
    "obState": 3,
    "underMaintenance": false
  }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查询状态](1600-get-status-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查询状态](1600-get-status-of-go.md)。
