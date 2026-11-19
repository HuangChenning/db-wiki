---
title: "获取租户会话统计信息"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077851.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取租户会话统计信息

本文介绍如何通过 API 获取租户会话的统计信息，包括按数据库、用户和客户端 IP 的统计。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/tenant/:name/sessions/stats

### 请求参数

| 参数 | 类型   | 必选 | 示例值 | 描述                               |
|------|--------|------|--------|------------------------------------|
| name | string | 是   | t1     | 租户名称。该参数通过路径参数指定。 |

### 返回结果

[TABLE]

TenantSessionStats 的数据结构：

[TABLE]

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/tenant/t1/sessions/stats

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2025-10-14T15:16:01.277047628+08:00",
    "duration": 30,
    "status": 200,
    "traceId": "e6f64ba7f54e7a49",
    "data": {
        "total_count": 10,
        "active_count": 5,
        "max_active_time": 3600.5,
        "db_stats": [
            {
                "db_name": "test",
                "total_count": 8,
                "active_count": 4
            },
            {
                "db_name": "sys",
                "total_count": 2,
                "active_count": 1
            }
        ],
        "user_stats": [
            {
                "user_name": "root",
                "total_count": 7,
                "active_count": 3
            },
            {
                "user_name": "admin",
                "total_count": 3,
                "active_count": 2
            }
        ],
        "client_stats": [
            {
                "client_ip": "10.10.10.100",
                "total_count": 6,
                "active_count": 3
            },
            {
                "client_ip": "10.10.10.101",
                "total_count": 4,
                "active_count": 2
            }
        ]
    }
}
```
