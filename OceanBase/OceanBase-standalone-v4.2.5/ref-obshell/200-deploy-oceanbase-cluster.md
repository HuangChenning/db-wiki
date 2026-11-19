---
title: "部署 OceanBase 集中式数据库"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286687.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 部署 OceanBase 集中式数据库

#### 说明

通过命令行命令调用 API 时，需注意以下信息：

- 以下 API 调用后会创建异步任务，因此需要确认任务完成后才可进行下一步。详细步骤可参见 [获取任务的详细信息](2000-get-dag-detail.md)。

- obshell 会对被调用的 API 进行安全校验。因此，您在每次调用 API 之前都需先参考 [API 混合加密](20-api-hybrid-encryption.md) 一文对请求进行加密，并在 curl 命令中配置加密后的请求头部（`${request_headers}`）和请求体（`${request_body}`）。
