---
title: "基于 OceanBase 构建智能问答机器人"
book: "向量搜索"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577487.html"
tags:
  - oceanbase
  - standalone
  - ob-vector-search
---

# 基于 OceanBase 构建智能问答机器人

#### 注意

- 通义千问 LLM 提供了一定的免费使用额度。使用过程中请关注免费额度使用情况，超出将会产生费用。
- 本教程以通义千问 LLM 为例来介绍问答机器人的搭建，您也可以选择使用其他 LLM 进行搭建，选用其他 LLM 需要更新 `.env` 文件中的 `API_KEY`、`LLM_BASE_URL` 和 `LLM_MODEL`。

#### 注意

此步骤需下载和处理大量 OceanBase 文档，会花费较长时间。

#### 注意

由于本应用基于 OceanBase 文档语料构建，请就 OceanBase 相关问题向您的助手提问。
