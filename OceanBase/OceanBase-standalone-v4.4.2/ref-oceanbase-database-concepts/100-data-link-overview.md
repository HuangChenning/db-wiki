---
title: "数据链路概述"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077371.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 数据链路概述

OceanBase 数据链路提供了从客户端到数据库端的最佳数据访问能力，对用户屏蔽 OceanBase 分布式数据库的感知，提供分布式数据库的可扩展、高性能和高可用的服务能力。数据链路包含两个部分：数据库代理和数据库驱动。

## 数据库驱动

数据库驱动程序由数据库厂商或者其他一些专门开发数据库驱动程序的厂商提供，它们提供给外部应用程序一个访问该数据库的接口。OceanBase 数据库目前提供了 MySQL 模式数据库（兼容 MySQL ）和 Oracle 模式数据库（兼容 Oracle ）。在 OceanBase MySQL 模式下，用户可以直接使用 MySQL 官方提供的 Connector 来使用 OceanBase 数据库。在 OceanBase Oracle 模式下，需要使用 OceanBase 自研的数据库驱动。OceanBase 数据库驱动同时支持 OceanBase 的 MySQL 和 Oracle 两种模式，在使用时可以自动识别 OceanBase 的运行模式是 MySQL 还是 Oracle，无需额外设置。

OceanBase 数据库支持各类语言的数据库驱动，主要有如下产品：

- **OBCI**

  兼容 OCI 接口，支持 OceanBase Oracle 模式的 C 语言驱动。

  有关 OBCI 的详细介绍，请参见 [OBCI](200-OBCI.md)。

- **OceanBase Connector/C**

  兼容 ODBC 接口，支持 OceanBase MySQL 和 OceanBase Oracle 模式的 C 语言驱动。

  有关 OceanBase Connector/C 的详细介绍，请参见 [OceanBase Connector/C](400-about-oceanbase-connector-c.md)。

- **OceanBase Connector/J**

  兼容 JDBC 接口，支持 OceanBase MySQL 和 OceanBase Oracle 模式的 Java 语言驱动。

  有关 OceanBase Connector/J 的详细介绍，请参见 [OceanBase Connector/J](300-oceanbase-connector-j_concepts.md)。

有关数据库驱动的详细内容，请参见 [数据库驱动](100-database-driver-overview.md)。
