---
title: "租户扩缩容介绍"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077594.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 租户扩缩容介绍

随着用户业务的发展或衰退，同时业务在不同时段的峰值往往也不同，需要数据库提供弹性的服务能力，OceanBase 数据库通过租户扩缩容功能来支持业务的弹性服务能力。

租户扩/缩容可以提升/降低计算能力和存储容量，OceanBase 数据库提供了提高/降低资源规格、增加/减少服务节点两种途径来实现扩缩容：

- 提高单节点的服务能力：调大租户的资源规格（Unit Config），从而达到单节点的服务能力提升。

  详细信息，参见 [通过调整资源规格实现租户扩缩容](200-adjust-resource-specifications.md)。

- 增加服务节点：通过将 OceanBase 集中式数据库扩展为分布式，从而增加服务节点，达到租户总服务能力的提升。详细操作，请咨询 OceanBase。

缩容是扩容的反操作，本质上是降低租户的服务能力，包括计算能力和存储容量。可以是调小资源规格，从而降低单节点的服务能力。
