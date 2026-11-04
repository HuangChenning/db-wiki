---
title: "数据库(V9)常见问题（应用开发类-asyncpg）"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree1.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

## 数据库(V9)常见问题（应用开发类-asyncpg）

## asyncpg 概述

asyncpg 是专为 PostgreSQL 数据库和 Python/asyncio 异步编程框架设计的高性能异步数据库接口，相较于传统同步数据库驱动，其在异步场景下具备更优的并发处理能力，核心优势如下：

- 极致性能：采用原生 PostgreSQL 协议实现，性能比主流的 psycopg3 快 5 倍左右
- 广泛协议支持：兼容 PostgreSQL 9.5 至 17 各个版本的核心协议特性
- 明确环境要求：需运行在 Python 3.8 及以上版本环境中
- 安全认证支持：内置支持 md5 和 scram-sha-256 两种主流数据库认证方式

### 1.1 asyncpg 安装

通过 pip 包管理工具可直接完成安装，命令如下：

```bash
pip install asyncpg
```

### 1.2 连接 V9 数据库代码示例

基于 Python asyncio 框架实现异步连接 V9 数据库，包含连接建立、数据查询、连接关闭完整流程：

```python
import asyncio

import asyncpg

async def connect_hgdb_v9():

# 初始化数据库连接（配置信息根据实际环境调整）

conn = await asyncpg.connect(

host="172.20.18.140",

port=5866,

user="highgo",

password="Hello@123",

database="highgo"

)

# 执行查询语句

values = await conn.fetch("select * from test")

# 输出查询结果

print("查询结果：", values)

# 关闭数据库连接

await conn.close()

# 运行异步任务

asyncio.run(connect_hgdb_v9())
```

> 注意：运行前需确保 Python 版本符合要求，且目标 V9 数据库服务已正常启动、网络可通