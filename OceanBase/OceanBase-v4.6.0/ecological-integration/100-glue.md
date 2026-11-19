---
title: AWS Glue
book: "生态集成"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688373.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# AWS Glue

#### 注意

- AWS Glue 不能通过公网 IP 连接数据源，并对网络要求极其严格。因此在使用 AWS Glue 时，在网络配置时需要将 Glue 任务和 OceanBase 实例放在同一子网上。密钥，终端节点也需位于同一节点。
- 使用 AWS Glue 遵循 AWS 的收费规则，并可能产生相应费用。请在继续前，访问其官网或查阅相关文档，确认并接受其收费标准。如不同意，请勿继续操作。

#### 注意

您必须将 us-east-1 替换为您选择的 AWS 区域。
