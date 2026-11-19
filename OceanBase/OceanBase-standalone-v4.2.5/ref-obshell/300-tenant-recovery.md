---
title: "发起租户恢复"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286694.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 发起租户恢复

#### 说明

obshell 会对被调用的 API 进行安全校验。因此，您在每次调用 API 之前都需先参考 [API 混合加密](20-api-hybrid-encryption.md) 一文对请求进行加密，并在 curl 命令中配置加密后的请求头部（`${request_headers}`）和请求体（`${request_body}`）。
