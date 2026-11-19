---
title: C3P0
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702178.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# C3P0

#### 说明

本文档运行代码使用的工具是 Eclipse IDE for Java Developers 2022-03 版本，您也可以根据个人喜好选择适合自己的工具运行的示例代码。

#### 说明

本文中给出的操作步骤是在 Windows 环境下使用 Eclipse IDE for Java Developers 2022-03 编译和运行该项目的步骤。如果您使用的是其他操作系统环境或编译器，那么操作步骤可能会略有不同。

#### 说明

当使用 Eclipse 导入 Maven 项目时，Eclipse 会自动检测项目中的 `pom.xml` 文件，并根据文件中描述的依赖关系自动下载所需的依赖库，并将它们添加到项目中。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DELETE`、`UPDATE` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

Java 1.8 和 Java 8 是同一个版本的不同命名方式。

#### 说明

本部分代码定义项目所依赖组件是 MySQL Connector/J 的 8.0.25 版本，如果需要了解其他版本的信息，请参见 [MySQL Connector/J](https://downloads.mysql.com/archives/c-j/)。

#### 说明

有关 MySQL Connector/J 实现类的名称信息，请参见 [Driver/Datasource Class Name](https://dev.mysql.com/doc/connector-j/8.1/en/connector-j-reference-driver-name.html)。

#### 注意

具体的属性（参数）配置取决于项目需求和数据库的特点，建议您根据实际情况进行调整和配置。更多 C3P0 连接池配置参数信息，请参见 [C3P0](https://www.mchange.com/projects/c3p0/)。

#### 注意

自动提交事务可能会导致数据不一致或丢失的情况。因此，应在确保事务完整性的情况下谨慎使用 `autoCommitOnClose`。在大多数情况下，建议手动管理事务，确保事务的提交或回滚发生在适当的时机。

#### 说明

如果在连接池中同时配置了 `automaticTestTable` 和 `preferredTestQuery`，C3P0 会优先使用 `preferredTestQuery` 来执行测试查询，而忽略 `automaticTestTable` 的设置。

#### 说明

- 如果 `maxStatements` 和 `maxStatementsPerConnection` 都为 0，则不会启用语句缓存。
- 如果 `maxStatements` 为 0，但 `maxStatementsPerConnection` 为非零值，则会启用语句缓存，但不会强制执行全局限制，只有每个连接的最大限制生效。
- `maxStatements` 控制连接池中所有连接的缓存语句的总数。如果设置了 `maxStatements`，它应该是一个相当大的数量，因为每个连接池中的连接都需要自己独立的、不同的缓存语句集合。

#### 说明

- 如果 `maxStatements` 和 `maxStatementsPerConnection` 都为 0，则不会启用语句缓存。
- 如果 `maxStatementsPerConnection` 为 0，但 `maxStatements` 为非零值，则会启用语句缓存，并强制执行全局限制，但对于单个连接不会设置缓存语句的数量限制。

#### 说明

- 辅助线程的数量越多，可以并行处理的任务就越多，从而提高连接池的处理能力和响应速度。
- 设置过多的辅助线程可能会导致系统资源的过度消耗，因此应根据系统的硬件配置和性能测试来合理地设置 `numHelperThreads` 的值。

#### 注意

测试的表必须在初始数据源的时候就存在。

#### 说明

虽然执行连接测试可以确保连接是有效的，但也会增加一定的额外开销。因此，应根据具体的应用需求和性能要求来决定是否启用连接测试。如果应用程序对连接的可用性要求较高，可以启用连接测试。但如果连接池中的连接经常被频繁地获取和释放，可能会导致连接测试过于频繁，从而影响性能。

#### 说明

尽管执行连接测试可以确保连接是有效的，但这也会增加一定的额外开销。因此，应根据具体的应用需求和性能要求来决定是否启用连接测试。如果应用程序对连接的可用性要求较高，可以启用连接测试。但如果连接池中的连接被频繁地获取和归还，可能会导致连接测试过于频繁，从而影响性能。
