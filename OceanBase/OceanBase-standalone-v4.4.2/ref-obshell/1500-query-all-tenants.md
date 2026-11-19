---
title: "获取所有租户概览"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077877.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取所有租户概览

本文介绍如何通过 API 获取所有租户的概览。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/tenants/overview

### 返回结果

[TABLE]

DbaObTenant 的数据结构：

| 参数          | 类型      | 说明                   |
|---------------|-----------|------------------------|
| tenant_id     | int       | 租户 ID。              |
| tenant_name   | string    | 租户名称。             |
| mode          | string    | 租户模式。             |
| status        | string    | 租户状态。             |
| locked        | string    | 租户是否被锁定。       |
| primary_zone  | string    | 租户的 Primary Zone。  |
| locality      | string    | 租户的副本信息。       |
| in_recyclebin | string    | 租户是否位于回收站中。 |
| created_time  | time.Time | 租户被创建的时间。     |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/tenants/overview

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T11:53:10.9102776+08:00",
    "duration": 16,
    "status": 200,
    "traceId": "73e93b51e1600be9",
    "data": {
        "contents": [
            {
                "tenant_id": 1,
                "tenant_name": "sys",
                "mode": "MYSQL",
                "status": "NORMAL",
                "locked": "NO",
                "primary_zone": "RANDOM",
                "locality": "FULL{1}@zone1",
                "in_recyclebin": "NO",
                "created_time": "2024-10-14T10:24:57.999108+08:00"
            },
            {
                "tenant_id": 1002,
                "tenant_name": "t1",
                "mode": "MYSQL",
                "status": "NORMAL",
                "locked": "NO",
                "primary_zone": "RANDOM",
                "locality": "FULL{1}@zone1",
                "in_recyclebin": "NO",
                "created_time": "2024-10-14T10:26:55.086821+08:00"
            }
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取所有租户概览](1500-query-all-tenants-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取所有租户概览](1500-query-all-tenants-of-go.md)。
