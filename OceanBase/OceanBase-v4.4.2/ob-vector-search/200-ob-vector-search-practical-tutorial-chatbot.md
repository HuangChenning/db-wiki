---
title: "基于 OceanBase 构建智能问答机器人"
book: OceanBase AI
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288642.html"
tags:
  - oceanbase
  - distributed
  - ob-vector-search
---

# 基于 OceanBase 构建智能问答机器人

#### 注意

开通阿里云百炼大模型服务需要您跳转至第三方平台完成。此操作将遵循第三方平台的收费规则，并可能产生相应费用。请在继续前，访问其官网或查阅相关文档，确认并接受其收费标准。如不同意，请勿继续操作。

#### 注意

本教程以通义千问 LLM 为例来介绍问答机器人的搭建，您也可以选择使用其他 LLM 进行搭建，选用其他 LLM 需要更新 `.env` 文件中的 `API_KEY`、`LLM_BASE_URL` 和 `LLM_MODEL`。

#### 注意

此步骤需下载和处理大量 OceanBase 文档，会花费较长时间。

#### 注意

由于本应用基于 OceanBase 文档语料构建，请就 OceanBase 相关问题向您的助手提问。
