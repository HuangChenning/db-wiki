---
title: "快速体验 OceanBase AP"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577297.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 快速体验 OceanBase AP

#### 注意

本文旨在帮助快速使用 OceanBase，如需进一步体验 AP 性能，推荐使用 [AP 场景下的参数配置推荐](100-obap-parameter-config.md) 中推荐配置。

#### 说明

当安装 grafana 或 prometheus 时，会输出 grafana 或 prometheus 的访问地址。在阿里云或其他云环境下，可能出现因无法获取公网 IP 而输出内网地址的情况，此 IP 非公网地址，您需要使用正确的地址。

#### 注意

由于安全原因，设置系统变量 \`secure_file_priv\` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000821297)。
