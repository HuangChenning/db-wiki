---
title: "OceanBase 数据库社区版"
book: "版本发布记录"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001874606.html"
tags:
  - oceanbase
  - distributed
  - release-notes
---

# OceanBase 数据库社区版

本文主要介绍 OceanBase 数据库社区版所有版本的发版说明。

## V5.0.1_CE

[**点击查看 V5.0.1_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V5.0.1)

**版本信息：**

- 发布时间：2026 年 08 月 06 日
- 版本号：5.0.1_CE
- RPM 版本号：oceanbase-ce_5.0.1.0-100000012026072916

**版本概述：**

OceanBase 数据库 V5.0.1 是 OceanBase 数据库 V4.6.0 的延续版本，持续对数据库的能力进行完善，其中包括：

- DDL 能力增强：

  - 新增支持加列、删列以及分区操作的并行 DDL。
  - 支持列存转行存、行列混存转行存的延迟在线 DDL，从而完善了行存、列存以及行列混存三种存储格式的相互 Online 转换。
  - 新增支持表模式（`partial_update`、`delete_insert` 和 `append_only`）在线切换；且增强了 Compaction TTL 能力，支持定义用户列为 TTL 列，且支持 `partial_update` 表定义 TTL 属性，能覆盖更多的业务场景。
  - 新增支持创建随机分布表，在数据写入时自动均匀打散到集群各节点，无需用户自定义分区，系统会自动切换，提升易用性。

- 负载均衡能力的增强：新增支持 Zone 级表组和 `SUBPARTITION` 表组，更多维度的控制分区的聚集和均衡策略。

- 对物化视图功能从监控诊断、增量刷新性能和使用易用性以及功能稳定性全方面做了能力提升。

- AI 能力上，AI Function 支持对图片类型的处理，并且做了并发请求的优化。

- 提供了 Database 级资源隔离（CPU/IO）的能力，允许将每个 Database 映射到独立的资源组，实现 CPU 和 IO 的细粒度隔离。

## V4.6.0_CE

[**点击查看 V4.6.0_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.6.0)

**版本信息：**

- 发布时间：2026 年 7 月 17 日
- 版本号：V4.6.0
- RPM 版本号：oceanbase-ce-4.6.0.0-100000162026071511

**版本概述：**

OceanBase V4.6.0 是一次面向现代化数据处理的重要版本升级，全面提升了 AI 混合搜索、向量数据库、HTAP 混合负载等核心能力。新版本推出原生 SQL 混合检索接口，支持多模态融合查询，并增强 HNSW 和 IVF 索引性能，构建端到端的“RAG all in One”知识库解决方案。列存副本智能路由与强一致性读、PX 并行计划优化及 Skip Index 等功能进一步提升 HTAP 负载效率。优化器与执行器增强包括谓词推导、窗口函数流式计算和 Join Order 自适应算法，存储引擎引入 Append-Only 表与 Compaction TTL 模型以提升复杂分析性能。兼容性方面扩展了 Recursive CTE、物化视图、Iceberg 格式支持及 REST Catalog 协议。系统性能方面，在国产化大规格机器上实现显著提升，复制表查询性能提高 14 倍，内存分配性能提升 168%。OBKV 数据模型新增弱读、TTL 限速优化与时序模型改进，OBCDC 支持增量同步与虚拟生成列实时计算。安全与可靠性方面新增 caching_sha2_password 认证、备库读优化及备份完整性校验。运维管理能力也得到增强，包括 SQLSTAT/ASH 架构重构、Plan Cache 内存优化及异构 Zone 支持，为企业大规模生产环境提供更高效、稳定、安全的数据管理体验。

## V4.5.0_CE

[**点击查看 V4.5.0_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.5.0)

**版本信息：**

- 发布时间：2025 年 12 月 03 日
- 版本号：V4.5.0_CE
- RPM 版本号：oceanbase-ce-4.5.0.0-100000012025112711

**版本概述：**

OceanBase V4.5.0 是面向 AI 场景的敏捷迭代版本，对内核 AI 能力进行了大的升级。新版本从构建、查询、DML 和易用性四个维度对 IVF/IVF_PQ 索引进行了全面优化。同时支持了内存稀疏向量索引，提供更加优异的稀疏向量检索性能。新版本的混合搜索能力也得到了大幅增强，支持了多路向量的混合搜索，并支持多路向量查询结果集采用加权方式进行融合重排。同时基于内置的 Embedding 能力，新版本支持用户基于文本列创建语义索引，简化用户使用向量索引的流程。

## V4.4.2_CE

### V4.4.2_CE_BP2

[**点击查看 V4.4.2_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.4.2)

**版本信息：**

- 发布时间：2026 年 07 月 16 日
- 版本号：V4.4.2_CE_BP2
- RPM 版本号：oceanbase-ce-4.4.2.2-102000022026071514

**版本概述：**

OceanBase V4.4.2_CE_BP2 为 V4.4.x 系列的稳定补丁版本，聚焦高可用架构完善、企业级兼容性扩展及大规模场景性能优化。高可用领域正式支持主备库强同步（RPO=0），新增最大保护与最大可用两种保护模式，并引入延迟备库能力以降低误操作传播风险；同步链路可观测性通过 per-LS 粒度监控视图与历史位点快照得到显著增强。数据同步架构实现重大升级，OBCDC 优化 UPDATE 拆分合并逻辑以保障下游 CDC 语义一致性。MySQL 模式则引入 `caching_sha2_password` 认证插件与全角转半角函数。SQL/PL 执行层优化覆盖硬解析内存管理、Plan Cache 诊断、JSON/Trigger 性能及全局索引访问路径；存储管理强化包括备份数据完整性校验、归档启停性能优化及回收站任务调度精细化。基础设施层面引入 Python UDF 沙箱隔离及分库分表 Outline 自动绑定，全面提升了系统的可运维性与生产环境稳定性。

### V4.4.2_CE_BP1

[**点击查看 V4.4.2_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.4.2)

**版本信息：**

- 发布时间：2026 年 05 月 08 日
- 版本号：V4.4.2_CE_BP1
- RPM 版本号：oceanbase-ce-4.4.2.1-101000022026050611

**版本概述：**

V4.4.2_CE_BP1 是 V4.4.2_CE（LTS 版本）的首个 BP 版本，在原有支持 V4.2.5_CE_BP7 平滑升级至 V4.4.2_CE 的基础上，新增支持 V4.3.5_CE_BP6 平滑升级至 V4.4.2_CE_BP1。该版本面向 TP/AP 业务，补充了多项关键特性，进一步提升系统性能与稳定性。

### V4.4.2_CE

[**点击查看 V4.4.2_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.4.2)

**版本信息：**

- 发布时间：2026 年 03 月 05 日
- 版本号：V4.4.2_CE
- RPM 版本号：oceanbase-ce-4.4.2.0-100000032026021017

**版本概述：**

OceanBase V4.4.2 是面向混合负载的 TP/AP 大融合 LTS 版本，深度集成 4.2.5 LTS 的事务处理能力与 4.3.5 LTS 的分析处理能力，在数据管理、兼容性、系统安全和运维诊断等多维度系统性增强内核能力，为关键交易负载与复杂分析负载提供更强大、更稳定的技术支撑。

在 TP 场景下，新版本支持二级分区表的一级分区与普通一级分区表进行交换，极大简化大规模数据分区管理和数据重组；新增 Session 级私有临时表，完善临时表体系。OBCDC 支持表级恢复后的增量数据同步，并支持同步 virtual 生成列，更好地满足下游系统对表级增量数据和生成列的消费需求。

KV 场景下，持续完善 OBKV 能力，新增弱读、TTL 支持索引扫描、热 Key 查询优化等特性，并完成对 OBKV‑HBase 监控项的治理，在高并发 KV 与时序场景下提供更低时延与更强可观测性。

性能方面，V4.4.2 面向细分场景进行了专项优化：串行建表性能在同等场景下提升约 60%。针对国产化大规格 CPU 环境，PDML 性能提升约 25%，复制表 Follower 查询性能提升约 14 倍，逼近 Leader 查询能力，显著增强系统横向扩展能力。同时，引入 PX 自适应任务切分机制，自动识别并切分长尾任务，实现并行查询负载重均衡，加速查询完成。

在安全与运维诊断方面，优化死锁检测机制，增强 Active Session History (ASH) 数据完整性，并重构 SQLSTAT 统计信息，为数据库管理员定位性能瓶颈和异常 SQL 提供更精细、更可靠的诊断工具。

V4.4.2 作为 LTS 版本，推荐 TP、AP 和 HTAP 业务使用。

## V4.4.1_CE

[**点击查看 V4.4.1_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.4.1)

**版本信息：**

- 发布时间：2025 年 10 月 24 日
- 版本号：V4.4.1_CE
- RPM 版本号：oceanbase-ce-4.4.1.0-100000032025101610

**版本概述：**

OceanBase V4.4.1 作为开源的第一个 V4.4.x 版本，在多个维度实现了显著提升。

V4.4.1 版本拓展了 AP 能力，支持了全文短语精确匹配、扩展了 JAVA UDF 功能、打通数据归档 HDFS 的路径 ，并优化了外表查询、UDF 执行、PS Cursor Fetch 数据的性能 ，增强了 CSV 导入诊断能力、支持 RPC IO 线程配置项动态生效等，提升系统易用性。

V4.4.1 版本对向量检索能力进行了升级，支持 Hybrid Search 混合检索，提升召回效果。新增 AI function 能力，支持 SQL 访问大模型。此外通过适配 ARM 架构、无主键表优化、IVF 索引优化等手段进一步提高向量检索的性能。新增视图展示向量索引内存占用和异步任务状态，提升易用性。

V4.4.1 版本全面优化外表查询、旁路导入、存储层读写、PL 硬解析、UDF 执行、SQL 硬解析、Batch DML 及 DDL 性能。PL 硬解析耗时降低 14%，UDF 性能提升 15%-26%，旁路导入排序算法升级显著提升导入效率。

在兼容性方面，V4.4.1 版本在 MySQL 租户模式新增 Python UDF。

V4.4.1 版本支持手动备份数据清理、设置执行备份任务的节点范围、消费归档日志适配强关归档场景。此外支持了 HMS Catalog、OBCDC 支持同步备租户、LOB 大对象的前镜像输出、外表支持 JDBC 插件、备库支持 flashback 接入新主库、SQL 关键字限流、Database 内用户表聚合等关键能力。

## V4.3.5

### V4.3.5_CE_BP6

[**点击查看 V4.3.5_CE_BP6 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2026 年 04 月 14 日
- 版本号：V4.3.5_CE_BP6
- RPM 版本号：oceanbase-ce-4.3.5.6-106000012026040916

**关键缺陷修复：**

- 修复指定 Hint 多值索引查询报错 1235 不支持的问题。
- 修复了重建向量索引（rebuild）时可能发生的 coredump 问题。
- 修复了 `HNSW` 索引在 `LATENCY_FIRST` 模式下查询报 -7605 错误及 `IVF` 索引内存爆的问题。
- 修复了向量索引 `adapter` 双重释放（double free）导致异常的问题。
- 修复了 `IVF` 缓存管理器内存泄漏的问题。
- 修复了 `HNSW` 索引并行补全数据时数据丢失的问题。
- 修复了删除向量索引在离线 DDL 失败后挂起（hung）的问题。
- 修复了向量索引 DDL 与后台任务缺少互斥逻辑导致 DDL 挂起的问题。
- 修复了带生成列的向量索引扫描返回空结果的问题。
- 修复了向量索引内存数据同步（memdata sync）异常的问题。
- 修复了 Hash Join 在 nestloop 模式下能发生的 coredump 问题。
- 修复了锁等待管理器（lock wait mgr）漏唤醒导致事务挂起的问题。

### V4.3.5_CE_BP5_HF2

[**点击查看 V4.3.5_CE_BP5_HF2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2026 年 01 月 28 日
- 版本号：V4.3.5_CE_BP5_HF2
- RPM 版本号：oceanbase-ce-4.3.5.5-105020072026012721

**关键缺陷修复：**

- 修复向量索引 rebuild 失败，未删除 lob meta 的问题。
- 修复大数据量分区表场景下，可能出现的创建向量索引报错 invalid timestamp 的问题。
- 支持通过 `dbms_vector.set_attribute` 的方式，设置向量索引自动 rebuild 并行度和执行周期。
- 修复 CDC 处理 LOB 存储数据时可能卡住的问题。
- 修复当表包含 `NOORDER` 自增列，且租户节点没有刷过 Leader Location，`DROP TABLE` 会报错 4038 的问题。
- 修复 obkv 场景下，OBKV-HBase 对同一个 Key Qualify 进行频繁更新时，可能导致 RT 升高的问题。
- 修复向量化 2.0 month_name 表达式优化引入的，计算到的月份大于 12 时访问越界导致 core 的问题。
- 修复 SQL 执行消耗了较大的内存且途中触发了 Inner sql 切换租户时，可能出现的查询报错内存不足的问题。
- 修复部分场景下查询物化视图，且不包含任何基表。使用较小 `LIMIT` 查询慢的问题。
- 修复部分场景下，Buffer 表导致的执行计划异常跳变的问题。

### V4.3.5_CE_BP5_HF1

[**点击查看 V4.3.5_CE_BP5_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 12 月 15 日
- 版本号：V4.3.5_CE_BP5_HF1
- RPM 版本号：oceanbase-ce-4.3.5.5-105010032025121323

**关键缺陷修复：**

- 修复在 `drop`/`rebuild` 向量索引场景下，向量索引磁盘占用空间异常膨胀的问题。
- 修复向量增量索引数据完整情况下 也会读主表补索引，导致查询RT增加的问题。
- 修复租户级别锁导致导致查询 RT 尖刺问题。
- 修复向量升级过程中，follower 不加载场景下，可能产生的内存爆的问题。
- 修复向量在难以找到匹配的记录情况下，迭代式过滤迭代的时间较久的问题。
- 修复并发写 IVF cache 概率可能导致的 core 问题。
- 修复多分区表并行执行建 IVF 索引可能出现的 core 问题。
- 修复部分开启 cgroup 场景下，线程切换 mtl 后导致其他租户 cpu 波动的问题。
- 修复对分区表和非分区表进行联合操作时，可能出现的查询结果不正确的问题。
- 修复 OBKV HBASE 的 Rowkey TTL 开启后，IO 异常升高的问题。
- 修复在两表 `join` 场景下，两表的数据没有重复值，且数据总量很多的场景下可能出现的 4013 问题。

### V4.3.5_CE_BP5

[**点击查看 V4.3.5_CE_BP5 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 11 月 19 日
- 版本号：V4.3.5_CE_BP5
- RPM 版本号：oceanbase-ce-4.3.5.5-105000012025111711

**版本概述：**

OceanBase 数据库 V4.3.5 BP5 版本围绕性能优化、功能增强与可靠性提升三大方向进行了全面升级。在向量搜索方面，新增 `similarity` 函数及 IVF 索引性能优化，支持通过相似度阈值过滤结果，并通过 Kmeans 并行化、迭代式过滤算法等技术显著提升向量查询与索引构建效率。针对大规模数据处理，引入 Delete-Insert 表的 Skip Index 裁剪机制，结合笛卡尔积计算性能优化，有效降低 LSM-Tree 查询开销。物化视图功能进一步增强，支持复杂聚合、嵌套视图、非基本列函数及 Minimal 刷新模式，提升数据预处理灵活性。分区管理扩展至 List 分区表交换，实现近瞬时数据迁移。SQL 与查询优化方面，新增 Union Distinct RCTE 支持、OBCDC 行外 LOB 数据完善、SQL STAT 诊断指标（如 `multi_query`、`full_table_scan`）及 ASH REPORT 生成加速，强化实时分析与故障排查能力。兼容性 方面，MySQL 模式新增 array\<\> 定义、JSON 类型转换等语法，并优化 DBLink 超时机制，适配复杂嵌套场景。此外，可靠性层面优化日志流迁移策略，确保副本选择稳定性。该版本全面覆盖金融级高并发、HTAP 混合负载及 AI 向量化场景需求，助力企业实现更高效的数据管理与智能化决策。

**关键缺陷修复：**

- Fix ObExprUserCanAccessObj param type bug.
- If group id not changed, do not repeatedly add tid to cgroup file.
- Add some transaction error code to inner error code.
- Fix push subquery bug.
- Fix mock lock/unlock user for standby tenant.
- Fix the issue where specifying LOCAL has no effect when adding a unique constraint.
- Fix vector prune non-vec index bug.
- Fix ObBatchRpc singleton analysis core when observer exits.
- Fix memory dynamic leak of inner call stmt.
- Fix sum ps information when its input type is string.
- Opt last_value() over half sliding window.
- Disable complex rescan path pruning.
- Remove remove_const expr during aggr subquery pullup.
- Fix regexp exec error 'U_REGEX_TIME_OUT'.
- Fix v\$open_cursor add display other user's cursors.
- Fix force enable plan tracing error 4016.
- Ignore normal nl path for connect_by join.
- Fix win func topn partition sort plan gen.
- Fix unstreaming cursor fill result without switch memory context.
- Fix print hostname of reverse link bug.
- Fix misssing constraint after add not null lob.
- Fix DataStoreVecExtraResult not destroy mem_context for sorting in destructor.
- Fix set system time zone bug.
- Recover when pid is moved out of cgroup dir.
- Block bugFix -4377 after before update trigger.
- Fix cg scanner projector after add column.
- Do not count IO traffic when IO request is canceled.
- Fix dynamic memory leak.
- Fix refine json path cache memory use.
- Add generate three stage group by constraint.
- Fix 0 can be inserted into date column in strict mode.
- Fix sql audit of PS Cursor fetch, add more informations.
- Fix dbms lob_read 4002 beacase of lob payload_size not update.
- Semistruct Fix merge 4016.
- Fix memory expend on unnest expr.
- Fix tmp file always flush_all after write buffer pool shrinking is aborted.
- Fix the problem that the division precision of number is inconsistent with mysql.
- Fix no_cost_based_query_transformation should allow heuristic semi_to_inner.
- Fix alter routine compile will create multi same name object.
- Fix batch insert optimization failure after disabling PS parameterization.
- Fix ObRowStore do not free buffer when occur exception.
- Fix lose semi info of inner query when pulling up subquery.
- Optimize tablet_id related hotspot in sql compile.
- Get min active snapshot version from all sessions.
- Fix old query range bug when merge key part after range condition.
- Fix old query range phy rowid cause hang.
- Modify first_exe_time of the streaming cursor to time from open to the end of fetch.
- Set prefix gen column nullable when create prefix index.
- Fix collect range graph infos cause too much time.
- Fix profiler use wrong key_id as unit_id for type and trigger.
- Restrict redundancy removal during predicate deduction.
- Use WaitGuard in SendMsgResponse::wait().
- Keep order for right child of merge right outer join.
- Fix incorrect update order of table stat info in exchange partition.
- Fix select distinct order by bug.
- Fix disable late materialization after it happened.
- Fix the recyclebin-bug of create hidden table.
- BUGFIX optimize the cost of \_\_all_virtual_ls_info.
- Fix incorrect pre-calc cache hit after freeing temp expr factory.
- Relax the strict deterministic check for char type.
- To avoid the session mistakenly thinking that its fd is open due to the reuse of closed fd.
- Fix bug generated column can not match index.
- Add fb_snapshot in lob locator tx snapshot.
- Adjust hash join left rows output method.
- Restrict query range extraction of 'not in' expr.
- Fix shared part expr bug.
- Enable post-groupby subquery join-first unnesting for stmt with group by but no unique key.
- Skip disk hung check when device is object storage.
- Meta tenant does not update throttle limit adaptively.
- Optimizing the performance of nested loop join operator in Cartesian product scenarios.
- Call mysql_close to release resource when mysql_real_connect failed.
- Feat user-friendly err msg when PL Debug without CAP_SYS_PTRACE.
- Fix recover many small table issue.
- Fix remove use less sys schema change check.
- Fix index merge with push down distinct using block gi.

### V4.3.5_CE_BP4

[**点击查看 V4.3.5_CE_BP4 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 09 月 16 日
- 版本号：V4.3.5_CE_BP4
- RPM 版本号：oceanbase-ce-4.3.5.4-104000042025090916

**版本概述：**

OceanBase 数据库 V4.3.5 BP4 版本在兼容性、性能与功能体验方面进行了多项重要升级。MySQL 模式下恢复支持 Session 级别私有临时表操作（创建/修改/删除及索引管理），并新增 GIS 函数 ST_AsGeoJSON() 支持生成列。物化视图优化支持增量刷新时排除维度表刷新（通过 `AS OF PROCTIME()` 语法），单表聚合场景支持 `MIN()`/`MAX()` 聚合函数，且实现 MLOG 表的自动管理（创建/替换/清理）。向量索引优化 VSGA 锁机制，HNSW_BQ 索引新增 cosine 和 ip 距离计算，支持弱读及超大规模分区表（10M/100M/1B 向量数据）。引入租户级 PS 参数化开关 `enable_ps_parameterize`，支持灵活控制常量参数化策略。SQL 实时内存监控功能新增 `[G]V$OB_PROCESSLIST` 视图，支持 TOP N SQL 实时分析。Full Schema 刷新机制升级为 Server 级更新，解决高并发 DDL 场景下的性能抖动问题。AP 参数模板默认关闭全量旁路导入，优化资源分配策略。

**关键缺陷修复：**

- 优化并发数和压力大场景事务超时的问题。
- 修复源表新增 `skip index` 后，导致备份防御失败报错的问题。
- 修复 `const` 表达式出现在 `UPDATE` 和 `GROUP BY` 中，被标记成共享表达式，下压到 table scan 中，导致在聚合中填了 `NULL` 值导致结果错误的问题。
- 修复迁移等操作导致单机出现多个日志流，线程打满问题。
- 修复链路不指定 database、绑定 outline、remote 执行场景 RT 抖动的问题。
- 修复增大插入 batch 场景下，锁冲突然变高，SQL 反复重试导致 CPU 被打爆的问题。
- 修复 `GROUP BY` 包含 `JOIN` 两侧的表达式，执行报错 4016 的问题。
- 修复 ps cursor 执行的 SQL 路由到非 Leader 节点时不会触发二次路由走 remote 计划的问题。
- 修复使用 cs encoding, 对于使用整型存储的列，如果有 filter 下压，可能会发生查询少行或者多行的问题。
- 修复系统表有 outrow lob 数据，`UPDATE` 或者 `DELETE` 时，outrow lob 的 lob 辅助表没有被删除的问题。
- 修复批量写入过程中，冲突行回滚后，回滚的 `tx_node` 被覆盖写掉，导致 `memtable` 遍历 `B+tree` 的叶节点链表时出错导致的 4377 问题。
- 修复使用有问题的驱动发通过二合一协议 253 长度的 SQL 到 Server 导致 observer crash 的问题。
- 修复 `MIN()`/`MAX()` 执行性能不优的问题。
- 优化统计信息收集问题。
- 修复使用序列 nextval 值时 unique constraint 冲突的问题。
- 修复 `LAG` 函数的 igore nulls 在存储过程中和 SQL 中表现不一致的问题。
- 修复物化视图刷新 SQL 计划生成时，没有初始化获取 `parallel_degree_limit` 的值，最终 auto dop 使用默认行为限制刷新 SQL 的 dop 问题。

### V4.3.5_CE_BP3_HF2

[**点击查看 V4.3.5_CE_BP3_HF2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 12 月 08 日
- 版本号：V4.3.5_CE_BP3_HF2
- RPM 版本号：oceanbase-ce-4.3.5.3-103020012025120120

**关键缺陷修复：**

- 修复分区交换前，分区表被收集了统计信息，分区交换后统计信息更新失败的问题。
- 支持一级 List 分区表与非分区表的分区交换。
- 修复分区数很多时，批量冻结 dag 积压，导致合并卡住的问题。
- 修复备份清理筛选 `piece` 不应该使用 `checkpoint_scn` 的问题。
- 修复使用 unnest 表达式展开嵌套 Array 时，数据量较大会导致内存膨胀的问题。
- 优化 json 路径内存使用的问题。
- 修复列存表加列后，全量合并之前，查询访问新列导致 OBServer Crash 的问题。
- 优化外表中的 `LD_LIBRARY_PATH` 设置问题。
- 修复 `GROUP BY` 包含 `JOIN` 两侧的表达式，`FUNCTION TABLE` 中依赖左侧传递的 exec param，且两表没有连接条件在 `ON` 和 `WHERE` 中时，SQL 执行报错 -4016 的问题。
- 修复在 `UPDATE` 带聚合的关联子查询中写常量表达式，写入的数据是 `NULL` 而不是常量值时，执行结果不符合预期的问题。
- 修复 V4.2.5 BP3 及之后版本使用原生 MySQL 驱动执行 PL 时，若用户无 `SELECT ON .` 权限可能触发报错的问题。
- 修复租户内存不足，向量 rebuild index 失败后无法正常删除辅助表，导致 `drop table` 任务卡住的问题。
- 修复 cosine 距离函数在 arm 的机器没有做 simd 优化的问题。
- 优化 minor merge 策略。
- 修复 `SELECT *` 方式查询 HDFS 外部表时，执行报错 -4002 的问题。

### V4.3.5_CE_BP3_HF1

[**点击查看 V4.3.5_CE_BP3_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 09 月 04 日
- 版本号：V4.3.5_CE_BP3_HF1
- RPM 版本号：oceanbase-ce-4.3.5.3-103010012025090210

**关键缺陷修复：**

- 修复部分场景下列存合并场景 memtable 无法释放的问题。
- 修复批量写入场景下，冲突行回滚可能导致 4377 的问题。
- 修复部分场景下扩容期间 RT 上涨的问题。
- 修复自动分区分裂正交 bufffer 表场景下分裂 meta major 卡住的问题。
- 修复 `SELECT UNION ALL` 存在精度缺失的问题。
- 修复列存场景下，对于使用整型存储的列，如果有 filter 下压，可能会发生查询少行或者多行的问题。
- 修复向量索引场景下的若干内存问题，优化内存占用。
- 修复全局索引自动分裂选择了 `null` 作为分裂键，查询条件带 `is null` 时可能结果不对的问题。
- 修复 `lower_case_table_names = 0` 的场景下，部分分区的分裂任务可能正常无法发起的问题。

### V4.3.5_CE_BP3

[**点击查看 V4.3.5_CE_BP3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 08 月 13 日
- 版本号：V4.3.5_CE_BP3
- RPM 版本号：oceanbase-ce-4.3.5.3-103000092025080818

**版本概述：**

OceanBase 数据库 V4.3.5 BP3 在性能优化、兼容性扩展及多模态能力等方面实现全面升级。在性能方面，通过适配 ODPS Storage API 提升外表访问效率，优化并行执行（PX）负载均衡、rescan 流程及 Batch DML 冲突处理，使查询与写入性能显著提升（如 Batch DML 全冲突场景性能最高提升 42%）；扩展性与兼容性上，新增 Azure Blob 对象存储支持，增强 OBKV-HBase 的共享存储模式与 Hive/Spark/Flink 兼容性，并支持 JSON 数据类型及 RoaringBitmap 聚合函数优化；系统稳定性方面，引入 SQL 关键字限流能力，通过精细化流量控制避免资源争抢，同时优化物化视图的级联刷新、增量刷新及稳定性问题。此外，向量数据库能力进一步增强，适配 ARM 架构，优化 IVF 索引构建与查询性能，支持小规格 HNSW 索引加速，并新增内存管理与索引参数控制功能，满足 PB 级 IOT 场景需求。

**关键缺陷修复：**

- 修复 SQL 中有非常量的 `convert_tz`，`convert_tz` 执行慢的问题。
- 修复特定场景下向量数据库索引重建期间不可用问题。
- 修复带全局索引的表执行 PDML，无法走到 DAS 层的攒批，导致的性能问题。
- 修复 query range 抽取在表达式计算时使用了 `exec_ctx` 的 allocator，造成动态内存泄露的问题。
- 优化列存表合并重整数据耗时较大的问题。
- 修复字符序 `CS_TYPE_UTF8MB4_BIN` 下，使用 `find_in_set` 函数返回值不符合预期问题。
- 修复硬解析过程中对多分区表频繁多次拉取统计信息，导致硬解析慢的问题。
- 修复 `beng` 分词器对空格的识别不正确导致出现两个分词，全文索引创建失败的问题。
- 修复行存索引列存表回表代价计算偏大的问题。
- 修复 `decimal int` 与 PL 正交场景的 core 问题。
- 修复在数据量大的场景，分裂采样的 SQL 耗时较高，导致建索引执行慢的问题。
- 修复内部表 filter 顺序被优化器交换，导致 `user_can_access_obj` 函数参数出现了 `NULL` 值，查询 `all_indexes` 表概率性执行报错的问题。
- 修复 `unpivot` 语句新生成列的长度推导处理有问题导致语句报错的问题。
- 修复动态语句执行过程中反拼 SQL 没有拼接 `ORA_ROWSCN` 的 table 信息，导致 resolve 报错的问题。
- 修复改写的索引匹配检查没有考虑到前缀索引，能匹配前缀索引的 or 分支被判定为无法匹配索引，导致没有尝试做 or 展开的问题。
- 修复开 IO 隔离，并且用户查询期间有迁移复制场景下 RT 抖动问题。
- 修复 SQL 语句结果 `count(distinct)` 包含多列时，结果不正确的问题。

### V4.3.5_CE_BP2_HF4

[**点击查看 V4.3.5_CE_BP2_HF4 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 08 月 20 日
- 版本号：V4.3.5_CE_BP2_HF4
- RPM 版本号：oceanbase-ce-4.3.5.2-102040012025081510

**缺陷修复：**

- 修复部分场景下列存合并场景 MemTable 无法释放的问题。
- 修复部分场景下扩容期间 RT 上涨的问题。
- 修复外表 `INSERT OVERWRTIE SELECT` 无法使用到多并发能力的问题。
- 修复 Query Range 抽取在表达式计算时使用了 `exec_ctx` 的 `allocator`，造成动态内存泄露的问题。
- 修复自动分裂调度器错误码误判的问题。
- 修复使用 `rb_to_string` 表达式合并场景数据不一致的问题。
- 修复自动分区分裂正交 Buffer 表场景下分裂 meta major 卡住的问题。

### V4.3.5_CE_BP2_HF3

[**点击查看 V4.3.5_CE_BP2_HF3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 08 月 04 日
- 版本号：V4.3.5_CE_BP2_HF3
- RPM 版本号：oceanbase-ce-4.3.5.2-102030022025073116

**缺陷修复：**

- 修复特定场景下自动分裂没有发起的问题。
- 修复分区表构建全文索引，且分批构建 sstable 场景下，未设置错误码导致全文索引任务卡住的问题。
- 修复隐式 cast 写在连接条件中不走索引，进行全表扫描，导致查询慢的问题。
- 修复 SQL 语句结果 `count(distinct)` 包含多列时候，结果可能不正确的问题。
- 修复向量化 2.0 的 `MIN`/`MAX` 在计算变长类型时没有复用 buffer，导致动态内存泄露的问题。
- 修复内部死锁记录表时间显示异常的问题。
- 修复字符序 `CS_TYPE_UTF8MB4_BIN` 下，使用 `find_in_set` 函数返回值不符合预期问题。
- 修复访问归档介质有权限问题报错后概率 core 问题。
- 修复阿里云 al8 系统 ODPS 外表创建失败的问题。
- 修复部分复制表场景下，SQL 执行计划不符合预期的问题。

### V4.3.5_CE_BP2_HF2

[**点击查看 V4.3.5_CE_BP2_HF2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 07 月 07 日
- 版本号：V4.3.5_CE_BP2_HF2
- RPM 版本号：oceanbase-ce-4.3.5.2-102020032025070315

**缺陷修复：**

- 修复 `HNSW_BQ` 索引在 Leader 上占用内存过多的问题。
- 修复 `substring` 字符分割中文异常的问题。
- 优化部分场景下，后建全文索引时间过长的问题。
- 修复向量索引并发查询和重建的场景下，可能无法走索引扫描的问题。
- 修复部分自动分区分裂场景下，预分裂和补数据相关的问题。
- 修复 `last_insert_id` 和 MySQL 的兼容性问题。
- 修复部分场景下对空格的处理不正确，导致全文索引创建失败问题。
- 修复向量索引重建设置 `extra_info_max_size` 不生效的问题。

### V4.3.5_CE_BP2_HF1

[**点击查看 V4.3.5_CE_BP2_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 05 月 29 日
- 版本号：V4.3.5_CE_BP2_HF1
- RPM 版本号：oceanbase-ce-4.3.5.2-102010012025052715

**缺陷修复：**

- 修复在大数据量场景下，分裂采样的 SQL 性能耗时较高，导致建索引执行慢的问题。
- 修复 V4.3.1 升级到 V4.3.3 或后续版本，可能出现的 meta 租户 clog 盘满的问题。
- 修复带 extra info 的向量表查询可能报错 4016 和 4377 的问题。
- 修复在向量查询在过滤率较小的场景下，查询结果可能不准确的问题。
- 修复部分删租户场景下，VIndexVsagADP 模块内存泄漏的问题。
- 修复向量索引后台任务报错 4016 的问题。
- 修复 Schema 较多的场景下，合并时间过长的问题。

### V4.3.5_CE_BP2

[**点击查看 V4.3.5_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 05 月 16 日
- 版本号：V4.3.5_CE_BP2
- RPM 版本号：oceanbase-ce-4.3.5.2-102000112025051418

**版本概述：**

OceanBase 数据库社区版 V4.3.5 BP2 版本围绕数据安全、性能优化、功能扩展及运维便利性进行了全面升级。主要包括：在存储与合规方面，新增对阿里云 OSS WORM 特性的适配，同时支持动态更新访问密钥提升安全性；数据管理能力增强，表级恢复扩展至列存表，新增分区伪列简化分区信息查询，动态分区管理实现自动预创建和清理分区，快速删列功能大幅缩短 DDL 耗时。性能优化层面，通过硬解析热点函数优化、Plan Cache 自适应策略、CSV 解析效率翻倍提升、Batch DML 存储层批量接口优化等手段显著提升处理效率。功能扩展覆盖多维度：支持 Map 和稀疏向量数据类型，强化 JSON 半结构化存储压缩率，引入 `HNSW_BQ` 量化向量索引，新增事件调度器实现数据库内定时任务管理，并通过 ODPS Catalog 简化跨数据源查询。系统可用性方面，解耦资源隔离配置，优化大规格国产 CPU 的 NUMA 扩展性，增强物化视图资源管控，同时改进诊断能力如 ASH Report 可读性提升。产品行为变更统一系统视图会话 ID 为全局 Client Session ID，强化全链路会话追踪能力。

该版本通过深度 HTAP 能力融合，为高并发事务处理与复杂分析场景提供更安全、高效、智能的分布式数据库解决方案。

**缺陷修复：**

- 修复调整 Compaction DAG 队列配置后可能导致合并卡住问题。
- 修复向量索引查询和升级兼容性相关的问题。
- 修复旁路导入场景 TLD_MemChunk 模块内存膨胀导致 4013 问题。
- 修复物化视图增量刷新导致 CPU 持续飙高问题。
- 修复大量 trigger 触发调度慢的问题。
- 修复弱网环境下备库恢复速度可能较慢的问题。
- 修复 arm 环境下查询可能出现非预期的 NULL 值的问题。
- 修复特定场景下 json 类型表现与 MySQL 不一致问题。

### V4.3.5_CE_BP1_HF2

[**点击查看 V4.3.5_CE_BP1_HF2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 06 月 18 日
- 版本号：V4.3.5_CE_BP1_HF2
- RPM 版本号：oceanbase-ce-4.3.5.1-101020012025061620

**缺陷修复：**

- 修复 V4.3.1 升级到 V4.3.3 或后续版本，可能出现的 meta 租户 clog 盘满的问题。
- 修复 arm 环境下查询可能出现非预期的 NULL 值的问题。
- 修复多分区表大量空分区场景下，可能出现的频繁拉取统计信息全表的问题。
- 修复 rebuild 向量索引时可能出现的卡住超时的问题。
- 修复向量索引在 rebuild 索引过程中，查询不走向量索引的问题。
- 修复分区分裂场景下，可能出现的合并 4016 的问题。
- 修复在大数据量场景下，分裂采样的 SQL 性能耗时较高，导致建索引执行慢的问题。
- 重建 ivf 索引后 replace into 报错 ERROR 5500 的问题。

### V4.3.5_CE_BP1_HF1

[**点击查看 V4.3.5_CE_BP1_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 04 月 30 日
- 版本号：V4.3.5_CE_BP1_HF1
- RPM 版本号：oceanbase-ce-4.3.5.1-101010042025042417

**缺陷修复：**

- 修复部分向量场景下的查询问题和升级兼容性问题。
- 修复部分使用 `HNSW_SQ` 索引时可能存在的内存问题。
- 修复 ARM 环境的宽表场景下，CPU 原子操作容易成为热点的性能问题。
- 修复部分全文索引场景下的内存膨胀和 core 问题。
- 修复部分 LOB 场景下，回放慢导致合并卡的问题。
- 修复 `SELECT INTO` 导出到 s3 报错 4016 的问题。
- 修复物化视图增量刷新导致 CPU 负载高的问题。
- 修复部分外表场景下的兼容性问题和报错问题。

### V4.3.5_CE_BP1

[**点击查看 V4.3.5_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 03 月 21 日
- 版本号：V4.3.5_CE_BP1
- RPM 版本号：oceanbase-ce-4.3.5.1-101000042025031818

**版本概述：**

OceanBase 数据库 V4.3.5 BP1 版本带来了多项功能增强或变动。其中包括堆组织表模式的增加支持，新增了 `STRING` 数据类型以满足 AP 业务需求；针对向量索引进行了优化，并增加了堆表带唯一索引的增量旁路导入功能；改进了表级恢复性能和资源优化，还增强了租户级容灾。此外，还新增了字符集、MySQL 类型系统改进、外表支持读取 HDFS 文件、全文索引特性增强、URL 外表、物化视图增强等功能。同时还对 PX 计算节点与数据节点解耦、`CAST`/`IN`/逻辑表达式性能优化、MySQL invisible column、外键功能优化等进行了增强和优化。新版本的 MySQL 非法日期类型兼容、PL 功能增强、复制表属性变更、小规格 OLTP 性能优化以及 SQL Query Interface 的增强等功能也将带来更好的用户体验和性能提升。

**缺陷修复：**

- 修复 reset 连接场景下，可能出现的系统变量设置失效的问题。
- 修复分区表行列混存场景下，收集统计信息可能报错 4016 的问题。
- 修复部分全文索引场景下，查询数据异常的问题。
- 修复旁路导入使用 `insert overwrite` 写入大量数据与写统计信息锁冲突导致旁路导入性能变差问题。
- 调整 freeze cnt 数值在每日合并后重置。
- 修复部分列存合并场景读不到事务数据导致合并超时问题。
- 修复部分场景下 sql audit 淘汰失败的问题。
- 修复物化视图中包含 array 等没有精度的数据类型刷新报错问题。
- 修复 rescan 场景下 HashPartInfra 内存膨胀的问题。
- 修复部分 obkv 场景 batch get 场景下，查询数据异常的问题。
- 修复部分全文索引场景下，使用 `REPLACE INTO` 报错 4019 的问题。

### V4.3.5_CE

[**点击查看 V4.3.5_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.5)

**版本信息：**

- 发布时间：2025 年 01 月 06 日
- 版本号：V4.3.5_CE
- RPM 版本号：oceanbase-ce-4.3.5.0-100000202024123117

**版本概述：**

OceanBase 数据库 V4.3.5 是面向 AP 场景第一个 LTS 版本。在 V4.3.4 的基础上，新版本继续完善产品能力，新增了对嵌套物化视图的支持，并完善了全文索引和向量索引功能。此外，数据导入导出的能力也得到了增强：支持指定分区旁路导入、外表支持读取 ORC 格式文件，以及 `SELECT INTO OUTFILE` 现在支持导出 Parquet 和 ORC 格式。优化器能力的增强包括基于基线优先策略的 SPM 演进、优化器估行系统的改进、递归公用表表达式 (CTE) 的抽取与 INLINE 代价验证优化，此外，对 Query Range 提取能力也进行了强化。

在性能优化方面，V4.3.5 对表级恢复性能、旁路导入性能、DML 性能以及 DDL 性能都做了不同程度的优化，新版本不仅支持行存与列存的在线转换，还实现了快速中间加列，并且扩展了并行 DDL 操作。同时，通过将统计信息和 CLOG 日志提交集成到资源隔离机制中，并实现了 IO 层级的隔离，进一步增强了 OceanBase 数据库的资源隔离机制。此外，新版本还支持 SQL 级别的内存使用限制，并优化了存储过程的内存使用，以及通过共享线程池来减少租户的内存资源消耗，提升了多种场景下的稳定性。在易用性方面，对 ASH 和 WR 的诊断能力做了增强，支持日志流副本并行迁移优化，以及通过实现日志传输链路的监控视图来增强日志同步链路的可观测性，让 OceanBase 数据库更加好用。新版本支持了更丰富的 `ARRAY` 和 XML 表达式，对 JSON/XML/GIS 类型数据执行过程中内存占用进行了优化。同时对 OBKV-HBase 和 HBase 的兼容能力做了增强，并支持了 OBKV 的 P95/P99 指标观测。

## V4.3.4

### V4.3.4_CE_BP1

[**点击查看 V4.3.4_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.4)

**版本信息：**

- 发布时间：2024 年 12 月 20 日
- 版本号：V4.3.4_CE_BP1
- RPM 版本号：oceanbase-ce-4.3.4.1-101000032024121814

**特性增强：**

响应时间统计直方图：当前已支持基于不同 SQL 类别的平均响应时间/最大响应时间指标，但缺乏更细粒度的反映某个分位 SQL 执行性能的指标展示。新版本增加响应时间直方图功能，可基于 `[G]V$OB_QUERY_RESPONSE_TIME_HISTOGRAM` 系统视图计算和监控不同类型 SQL 不同分位的响应时间统计。

**缺陷修复：**

- 修复创建物化视图时偶发快照保留记录漏维护的问题。
- 修复物化视图依赖的基表增量数据较多时，实时物化视图查询性能较差的问题。
- 修复部分场景下 431 升级 434 后，节点启动失败的问题。
- 修复 OBKV-Hbase scan 时，limit 不生效的问题。
- 修复部分场景下列存副本下合并报错 4103 的问题。
- 修复部分分区分裂场景下，ddl 报错 4002 的问题。
- 修复部分场景下向量索引 VIndexVsagADP 模块内存超过 ob_vector_memory_limit_percentage 限制的问题。
- 修复部分场景下，向包含向量索引的表添加分区失败的问题。
- 修复部分场景下 not in 性能不佳的问题。

### V4.3.4_CE

[**点击查看 V4.3.4_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.4)

**版本信息：**

- 发布时间：2024 年 11 月 8 日
- 版本号：V4.3.4_CE
- RPM 版本号：oceanbase-ce-4.3.4.0-100000162024110717

**版本概述：**

OceanBase V4.3.4 是面向 AP 业务的 GA 版本，在第一个 GA 版本 V4.3.3 的基础上，新增多个重要特性。完善多值索引能力，丰富全文索引场景，提升查询性能；完善旁路导入功能，优化主键表写临时文件开销，提高数据导入效率；新增自动分区分裂功能、Format Outline 功能、租户级全局控制导数走旁路导入功能，提升产品易用性；同时对 OBKV 支持全局索引、OBKV-HBase 能力增强等 V4.2.5 及之前版本的大部分特性，进行了补充支持。

## V4.3.3

### V4.3.3_CE_BP1

[**点击查看 V4.3.3_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.3)

**版本信息：**

- 发布时间：2024 年 10 月 25 日
- 版本号：V4.3.3_CE_BP1
- RPM 版本号：oceanbase-ce-4.3.3.1-101000012024102216

**版本概述：**

- 新增从 V4.2.4_CE 版本 patch 的 “SQL实时诊断” 特性。
- 修复一些 BUG 和稳定性问题。

### V4.3.3_CE

[**点击查看 V4.3.3_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.3)

**版本信息：**

- 发布时间：2024 年 10 月 9 日
- 版本号：V4.3.3_CE
- RPM 版本号：oceanbase-ce-4.3.3.0-100000142024101215

**版本概述：**

OceanBase V4.3.3 作为 4.3 系列的第一个 GA 版本发布，在几个关键场景完成了突破。一是在关系型数据库基础上支持了适用于 AI 类分析处理的向量类型及索引；二是更好满足 HTAP 混合负载场景下，TP、AP 资源物理强隔离诉求的全新的列存副本形态；三是面向 AP 类查询任务的整体可观的性能提升。除此之外，新增 `ARRAY` 复杂类型支持、优化 Roaringbitmap 类型计算性能，强化物化视图改写刷新等能力，扩展外表功能、提高外表导入性能，优化 AP 类 SQL 的计划生成和执行策略，加快面向 OLAP 负载的产品化能力提升。新版本还支持了一种只需恢复日志无需恢复数据到本地即可提供读服务的快速恢复能力，也支持了 QUERY 级别的资源组设定，提升了系统的可靠性和易用性。同时，V4.2.4 及之前版本的大部分特性已经在 V4.3.3 补充支持，后续也会推出同样可应用于 OLTP 业务生产的全新融合版本。

## V4.3.2

### V4.3.2_CE_BP1

[**点击查看 V4.3.2_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.2)

**版本信息：**

- 发布时间：2024 年 8 月 16 日
- 版本号：V4.3.2_CE_BP1
- RPM 版本号：oceanbase-ce-4.3.2.1-100000102024081217

**版本概述：**

- **异步任务调度：**

  OceanBase 数据库目前已支持 insert overwrite、insert select、create table as、load data 等多种数据导入命令，来支撑数据实时入库。但实时导入的方式需要在导入过程中等待导入完成，不能中断会话，这在大规模数据导入的场景比较不易用。

  新版本提供了异步任务调度能力，用户可通过 submit job、show job status 和 cancel job 等命令实现异步导入任务的创建、状态查询和任务取消。

- **`SELECT INTO OUTFILE` 分区导出：**

  OceanBase 数据库目前已支持通过 `SELECT INTO OUTFILE` 导出多文件，但尚未支持对数据分区后按分区导出。

  新版本增加按分区导出能力，以得到更清晰的目录结构。在此基础上还可以将文件目录构造为带分区的外表，通过分区路径裁剪，提高外表的查询效率。

### V4.3.2_CE_BETA

[**点击查看 V4.3.2_CE_BETA Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.2)

**版本信息：**

- 发布时间：2024 年 7 月 30 日
- 版本号：V4.3.2_CE_BETA
- RPM 版本号：oceanbase-ce-4.3.2.0-100000092024072912

**版本概述：**

OceanBase V4.3.2 是面向 AP 业务的性能增强版本，数据读取、数据分发、数据计算、向量化处理、计划选择全方位改进，AP 类基准测试性能整体提升 10%-15%。引入 Roaringbitmap 数据类型及相关计算表达式，给大数据集合运算和去重场景提供了更优选择。丰富增量旁路导入功能、提升全量旁路导入性能，扩展支持 Parquet 文件外表，加速大规模数据的处理速度。作为一款一体化数据库，新版本也针对 `express oltp`、`complex oltp`、`olap`、`htap`、`kv` 等 5 类场景分别梳理了场景化参数模版，配合部署工具，让初始配置就适合每一种业务类型。此外，新版本还融合了 V4.2.x 系列前序版本的诸多兼容性增强和用户体验改进特性，并合入了TP 类 SQL 的性能改进，致力于满足各类应用场景对产品的诉求。

## V4.3.1

### V4.3.1_CE_BETA

[**点击查看 V4.3.1_CE_BETA Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.1)

**版本信息：**

- 发布时间：2024 年 5 月 22 日
- 版本号：V4.3.1_CE_BETA
- RPM 版本号：oceanbase-ce-4.3.1.0-100000032024051615

**版本概述：**

OceanBase V4.3.1 在 V4.3.0 基础上，新增全文索引特性提升文档检索效率，扩展实时物化视图、物化视图改写、主键物化视图等功能以满足多场景的分析需求。引入分区管理新机制，如分区交换、外表分区、MySQL 模式分区键数据类型扩展等，提升大规模数据的处理能力。多模特性（含 JSON、XML、GIS）功能升级，增加 JSON 多值索引、JSON 部分更新的能力支持，促进异构数据的迁移与融合。MySQL 兼容性持续增强，支持 Lateral Derived Tables、 MySQL 锁函数等，以便融入生态。提供增量旁路导入能力，提升了多次导入场景的入库性能，同时优化了多局部索引场景下的 DML 性能，提高了基础统计信息收集效率，并在行采样、小规格 TP 场景取得了显著的性能提升。新版本也进一步优化了资源使用，支持了 CLOG 日志缓存、SQL 临时结果压缩、系统日志压缩等特性。补充完善了 MySQL 权限体系、支持了操作系统配置检查，加固系统安全。一如既往地关注用户体验，增加资源规格估算能力，增强备份透明度，提供 IPV6 格式支持，赋能数据库管理与运维。

V4.3.1 定位为 Beta 版本，推荐实时数仓或联机交易业务测试使用，下半年将发布推荐用于生产的 GA 版本。

## V4.3.0

### V4.3.0_CE_BETA

[**点击查看 V4.3.0_CE_BETA Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.3.0)

**版本信息：**

- 发布时间：2024 年 3 月 28 日
- 版本号：V4.3.0_CE_BETA
- RPM 版本号：oceanbase-ce-4.3.0.1-100000242024032211
- 版本说明：Beta 版本解决了大部分缺陷，并趋于稳定。推荐测试环境使用。

**版本概述：**

OceanBase 重磅推出 V4.3.0 版本，深入典型 AP 场景，不再局限于 TP + 轻量化 AP 的版本定位。基于 LSM-Tree 架构推出列存引擎，实现行存、列存数据存储一体化，同时推出基于 Column 数据格式描述的新版向量化引擎和基于列存的代价模型，支持高效处理大宽表，显著提升 AP 场景查询性能，并兼顾 TP 业务场景。新增物化视图功能，通过预计算存储视图的查询结果提升实时查询性能，支撑快速报表生成和数据分析场景。新版本内核也扩展了 Online DDL、支持了租户克隆等功能，优化 PDML、节点重启性能，提升 `LOB` 类型旁路导入效率，增加 S3 备份恢复介质支持，优化系统资源使用，并增加索引使用监控、客户端本地导入等功能提升系统易用性。推荐用于复杂分析、实时报表、实时数仓或联机交易等混合负载场景。

## V4.2.5

### V4.2.5_CE_BP7_HF1

[**点击查看 V4.2.5_CE_BP7_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2026 年 03 月 06 日
- 版本号：V4.2.5_CE_BP7_HF1
- RPM 版本号：oceanbase-ce-4.2.5.7-107010012026030415

**版本概览：**

- 修复旁路导入未适配快速删除列，类型转换时内存访问越界导致 Core 的问题。
- 修复执行 PL 函数时，如果执行环境与 PL 函数编译时的环境不一致，导致每次执行都会进行重新 Store/Reset 导致 PL 函数执行慢的问题。
- 修复部分场景下 SQL 执行由于硬解析超时的问题。
- 修复当 JOIN 的两张表数据没有重复值，且能 JOIN 上的数据总量很多。在主键列、Unique 索引列上的 Merge JOIN 可能触发的内存膨胀问题。
- 修复当表包含 Noorder 自增列，且租户节点没有刷过 Leader Location，Drop Table 会报错 4038 的问题。
- 修复频繁对单分区表 Truncate 场景下，通过 OCP 的统计信息收集情况页面访问内部表，可能出现的 OBServer CPU 使用高的问题。
- 修复升级脚本 `-t` 参数设置异常的问题。
- 修复部分场景下临时文件落盘存在的内存泄漏问题。
- 修复部分场景下 Meta 租户在一定的时间段内写入较多数据可能导致内存占用过高的问题。

### V4.2.5_CE_BP7

[**点击查看 V4.2.5_CE_BP7 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 12 月 05 日
- 版本号：V4.2.5_CE_BP7
- RPM 版本号：oceanbase-ce-4.2.5.7-107000022025120120

**版本概览：**

- **优化选主策略**

  针对 4F1A 场景，primary_zone 设置为 "z1,z2;z3,z4"，当 z1、z2 所在 region 不可用时，在 V4.2.5 BP7 之前的版本，会选举 IP 最小的 Zone 作为新主，即 Leader 会全部切到 z3 而非均衡到 z3 和 z4。在 V4.2.5 BP7 支持了优化选主策略后，当高优先级的所有 Zone 都不可用时，Leader 会均匀打散到低一个优先级的各 Zone，即 Leader 会打散分布在 z3 和 z4 上，由此提高系统的高可用性。

- **SQLSTAT 能力增强**

  支持 `multi_query` 用以判断路由错误和同步提交；支持 `muti_query_batch_execute` 可以用来判断语句是否走 Batch 优化；支持 `full_table_scan` 用以判断 SQL 出现全表扫的次数；支持 `error_count` 用以统计 SQL 报错情况。更多详细内容，请通过 [GV\$OB_SQLSTAT](../ref-system-views/3200-gv-ob_sqlstat-of-mysql-mode.md) 或 [DBA_WR_SQLSTAT](../ref-system-views/15900-o-dba_wr_sqlstat-of-mysql-mode.md) 等视图获取。

- **ASH REPORT 生成加速**

  由于 ASH REPORT 的生成涉及 JOIN ASH 数据和 WR 数据，耗时较长，本特性在不改变 ASH REPORT 的行为的情况下，加速了 ASH REPORT 的生成。

- **备份归档适配 OSS WORM**

  阿里云 OSS 提供了 [WORM（Write Once Read Many）](../manage/200-preparation-before-log-archive.md) 特性，用户通过命令为 Bucket 配置保留策略后，在保留策略指定的 Object 保留时间到期之前，仅支持在 Bucket 中上传和读取 Object。Object 保留时间到期后，才可以修改或删除 Object。新版本 OceanBase 数据库备份归档适配了阿里云 OSS 的 WORM 特性，支持使用已配置合规保留策略的 OSS Bucket 作为备份归档目的端，帮助用户满足数据安全存储及政策合规要求。

### V4.2.5_CE_BP6

[**点击查看 V4.2.5_CE_BP6 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 09 月 01 日
- 版本号：V4.2.5_CE_BP6
- RPM 版本号：oceanbase-ce-4.2.5.6-106000022025082510

**版本概览：**

V4.2.5 BP6 版本进行了多项优化与增强：

- 在分布式执行的全局索引回表场景下，性能提升了 3%–5%；

- 优化备库读功能并增强其稳定性；

- 扩展支持通过 Azure Blob 协议访问 Azure Blob 对象存储；

- 新增 UDF 结果缓存功能，并针对无法缓存的场景优化了执行路径；

- 新增 TO_PINYIN 表达式，并增加可选参数，支持控制输出的大小写、全拼或首字母格式。

### V4.2.5_CE_BP5

[**点击查看 V4.2.5_CE_BP5 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 07 月 16 日
- 版本号：V4.2.5_CE_BP5
- RPM 版本号：oceanbase-ce-4.2.5.5-105000022025070909

**版本概览：**

V4.2.5_CE_BP5 版本支持了异构 Zone 功能，同一租户支持至多拥有两种不同的 Unit Num，为 OBServer 的运维能力和扩缩容能力带来了提升。此前 OBServer 受限于同一租户各 Zone 的 Unit Num 必须相同，当遇到故障且没有机器替换时，需要将所有 Zone 都降低 Unit Num，扩大了运维范围；此外，扩缩容场景可以利用该能力在 Follower 副本先行操作，然后切换 Leader 至扩缩容完成的 Zone，实现更平滑的扩缩容；另外还在 MySQL 模式下支持快速删列，标记删除无需数据重整。

### V4.2.5_CE_BP4

[**点击查看 V4.2.5_CE_BP4 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 06 月 06 日
- 版本号：V4.2.5_CE_BP4
- RPM 版本号：oceanbase-ce-4.2.5.4-104000062025053011

**版本概览：**

V4.2.5_CE_BP4 版本实现了多项性能优化与功能增强：在性能方面，重构了 `INFORMATION_SCHEMA.COLUMNS` 视图以支持索引点查；优化空表索引创建速度；支持特定场景下预计算子查询降低计算量；将 DDL 操作后的 Schema 刷新机制由 Session 级升级至 Server 级；通过日志流再均衡减少热点风险。在功能方面，新增旁路导入 OceanBase 数据库 2.x 备份数据；MySQL 模式支持二级分区添加；备库日志裁剪提升 Failover 能力；旁路导入异步 Commit 规避单任务超时回滚。此外，该版本还强化了备库读稳定性。

### V4.2.5_CE_BP3

[**点击查看 V4.2.5_CE_BP3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 04 月 03 日
- 版本号：V4.2.5_CE_BP3
- RPM 版本号：oceanbase-ce-4.2.5.3-103000022025033117

**版本概览：**

V4.2.5_CE_BP3 版本增强了一系列诊断能力，包括优化了 Ash Report 的展现形式；新增了对 I/O、事务相关信息的统计项；SQL 计划查询能力增强；稳定性增强与采集性能优化。性能方面优化表事务回收策略，高 TPS 场景下显著降低 I/O 负载；支持并行补偿日志加快备份速度；存在关联 Update 的 DML 语句支持 PDML 并行执行。此外，在 MySQL 模式下新增支持外键引用存在非唯一索引的列的特性。

### V4.2.5_CE_BP2_HF1

[**点击查看 V4.2.5_CE_BP2_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 02 月 28 日
- 版本号：4.2.5_CE_BP2_HF1
- RPM 版本号：oceanbase-ce-4.2.5.2-102010012025022610

**版本概览：**

- 修复在 Table API 场景下，当 OBKV 表结构包含时间类型列作为分区键时出现的路由问题。
- 修复在 OBKV 表结构包含时间列时，报错 4016 的问题。

### V4.2.5_CE_BP2

[**点击查看 V4.2.5_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2025 年 01 月 24 日
- 版本号：V4.2.5_CE_BP2
- RPM 版本号：oceanbase-ce-4.2.5.2-102000062025012010

**版本概览：**

V4.2.5_CE_BP2 版本推出多项核心优化与功能升级，重点包括：分区权重均衡机制通过动态调整分区权重解决业务流量不均问题，提升集群负载能力；支持手动创建及管理日志流、暂停/恢复均衡任务以增强运维灵活性；新增 PS 参数化开关和实时 SQL 内存监控，优化性能诊断与执行计划控制；完善备份/归档路径配置，减少跨地域带宽占用；在兼容性方面，扩展 MySQL 模式 Event 功能、提升 OBKV 组件的生态适配与性能；同时优化小规格 OLTP 性能及统计信息收集效率，并扩展 `ob_admin` 工具支持云原生备份场景参数解析。此次更新全面覆盖负载均衡、运维效率及多生态兼容，助力复杂业务场景高效稳定运行。

### V4.2.5_CE_BP1

[**点击查看 V4.2.5_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2024 年 12 月 13 日
- 版本号：V4.2.5_CE_BP1
- RPM 版本号：oceanbase-ce-4.2.5.1-101000092024120918

**版本概览：**

V4.2.5_CE_BP1 版本在备份恢复功能中新增了对 NFSv3 协议的支持。同时，支持了并行 Drop Table，提高了频繁执行 Drop Table 操作时的吞吐能力。此外，通过在存储层实现真正的批量接口，显著提升了诸如 Batch Insert、Delete 大量数据、Insert On Duplicate Key Update 等批量 DML 场景下的性能。V4.2.5_CE_BP1 版本还进一步适配了 `MySQL_EVENT` 功能。

### V4.2.5_CE

[**点击查看 V4.2.5_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.5)

**版本信息：**

- 发布时间：2024 年 10 月 21 日
- 版本号：V4.2.5_CE
- RPM 版本号：oceanbase-ce-4.2.5.0-100000052024102022

**版本概述：**

OceanBase 数据库 V4.2.5_CE 版本是面向 TP 的全新的 LTS 版本。在 V4.2.4_CE 版本基础上，新版本继续完善产品能力，支持了基线优先的 SPM 演进，基于分区表的晚期物化等功能，并进行了优化器估行系统改进以及 CTE 抽取/ INLINE 代价验证改进，有力增强了优化器能力。新版本支持了消费日志支持强关归档、Transfer 搬迁活跃事务以及基于 IO 负载的自适应仲裁升降级，进一步提高了系统的稳定性和可靠性。同时，也支持了备份配置项及租户资源配置和副本分布信息，有效的保证物理恢复的成功率以及后续生产业务的稳定性。

在兼容性方面，OceanBase 数据库兼容了锁函数、非法日期、XA 事务等功能。新版本进行了表级恢复性能优化、升级性能优化，大大减小表级恢复和升级的耗时。同时通过将统计信息及 clog 日志提交接入资源隔离以及实现 DDL 资源隔离，进一步强化了 OceanBase 数据库的资源隔离机制。新版本支持 SQL 级内存使用限制，并优化了存储过程内存使用，提升了多场景下的稳定性。

在易用性方面，新版本也做了诸多工作。ASH 诊断新增行锁等待和重试等待事件、响应时间直方图、日志传输链路视图等举措提升了系统的可观测性。日志副本并行迁移优化、动态修改 OBServer 内存资源规格实时生效、新增 `./alert/alert.log` 日志文件用于记录 DBA 关注的日志信息，让 OceanBase 数据库更加好用。新版本新增了 OBKV-Redis 模型的支持，丰富了 OceanBase 的多模生态。同时优化了 OBKV-HBase 过期删除能力，解决“热 Key”场景下的数据版本过多问题。新增 ColumnPaginationFilter 及 Reverse Scan 接口，进一步增强 HBase 的兼容性。

## V4.2.4

### V4.2.4_CE_HF1

[**点击查看 V4.2.4_CE_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.4)

**版本信息：**

- 发布时间：2024 年 9 月 11 日
- 版本号：V4.2.4_CE_HF1
- RPM 版本号：oceanbase-ce-4.2.4.0-100010022024091012

**版本概述：**

- 修复多表 `JOIN...JOIN...ON...ON` 查询语法与 MySQL 的兼容问题。
- 修复系统表 `information_schema.TABLES` 有多条重复记录的问题。
- 修复部分 PL 场景下 Plan Cache 无法命中的问题。
- 修复 ARM 架构环境下使用存储过程可能报错 4013 的问题。

### V4.2.4_CE

[**点击查看 V4.2.4_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.4)

**版本信息：**

- 发布时间：2024 年 7 月 12 日
- 版本号：V4.2.4_CE
- RPM 版本号：oceanbase-ce-4.2.4.0-100000082024070810

**版本概述：**

OceanBase 数据库 V4.2.4_CE 版本是面向 TP 和 HTAP 业务的高度兼容、高性能、安全且易于管理的新版本。在 V4.2.3_CE 版本基础上，新版本继续完善产品兼容性，新增多项 MySQL 特性支持，包括 Event Scheduler、ASCII/TIS620 字符集、列默认值定义为表达式等，提升 MySQL 迁移的便利性。增强优化器能力，支持统计信息过期后的自适应修正，优化直方图采样策略，提升估行准确性以防统计信息走偏。新版本也实现了主备库之间的自动路由功能，确保服务高可用性，即使在主库故障情况下也能无缝切换至备库继续提供服务。提升 PDML 高并发性能，优化 DAS 执行 GTS 开销，支持物理备库的并行同步，整体提升了小规格 OLTP 性能。另外支持 REFERENCES、CREATE/DROP ROLE、TRIGGER 权限管理，强化数据库企业级安全特性。运维易用性方面，扩展分区均衡的运维能力，优化死锁检测诊断机制，重构 ASH 报告内容展示，提升实时诊断准确性，提升了用户操作的便捷性和效率。同时重构了 OBKV 请求的 `SQL_ID` 生成方式，提升 OBKV 可观测性。

## V4.2.3

### V4.2.3_CE_BP1

[**点击查看 V4.2.3_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.3)

**版本信息：**

- 发布日期：2024 年 6 月 19 日
- 版本号：V4.2.3_CE_BP1
- RPM 版本号：oceanbase-ce-4.2.3.1-101000032024061316

**版本概述：**

- 修复插入或查询时间相关生成列或函数索引时，使用的 Timezone 和创建表时使用的地区定义的 Timezone 不一致，引起的内存泄漏问题。
- 修复备份恢复访问 S3 协议的对象存储时，必须指定 `s3_region` 的问题。
- 优化 PL 并发编译慢的问题，增加 `PLSQL_OPTIMIZE_LEVEL` 系统变量支持调整编译优化级别和并发数。
- 优化部分 OLTP 场景下的性能。

### V4.2.3_CE_BETA

[**点击查看 V4.2.3_CE_BETA Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.3)

**版本信息：**

- 发布时间：2024 年 4 月 29 日
- 版本号：V4.2.3_CE_BETA
- RPM 版本号：oceanbase-ce-4.2.3.0-100000112024042411

**版本概述：**

V4.2.3_CE_BETA 为 V4.2.x_CE 系列最新版本，支持了一系列 MySQL 兼容特性，如角色、列级权限、Union Distinct RCTE 及大量小功能兼容。在多个场景优化了系统性能，如优化多模类型读写计算和 OBKV 处理效率，扩展 Batch DML 的并行执行能力，提升备份/网络备库性能，解决自增列/Sequence 在 Order 模式下的性能问题等。同时，备份恢复扩展支持了 S3 及兼容 S3 协议的对象存储（如：OBS，GCS）作为备份目的端。在资源优化方面，进行了一系列优化包括 DDL 临时结果空间优化、旁路导入能力提升和全局前后台 CPU 资源隔离等。新版本也实现了多个业务期待的易用性功能，如用于日志分析和误操作识别的 ObLogMiner 功能，应对 Buffer 表性能问题的合并策略选择，提供模糊绑定计划和限流方式的 Format Outline，用于识别无用索引的索引使用监控特性，提供更高可读性的面向数据库管理员的 `alert.log` 系统日志，增加日志流副本管理的用户命令，提供物理恢复进度展示能力。更详细的 PX 诊断数据以及 ASH Report 的节点级分析等，有效提高系统易用性。

推荐用于测试，暂不建议用于生产。

## V4.2.2

### V4.2.2_CE_BP1

[**点击查看 V4.2.2_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.2)

**版本信息：**

- 发布时间：2024 年 3 月 13 日
- 版本号：V4.2.2_CE_BP1
- RPM 版本号：oceanbase-ce-4.2.2.1-101000012024030709

**版本概述：**

修复若干内部代码兼容性问题，已经部署 V4.2.2_CE 或 V4.2.2_CE_HF1 版本的集群，升级更高版本时，需经停 V4.2.2_CE_BP1 版本。

### V4.2.2_CE_HF1

[**点击查看 V4.2.2_CE_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.2)

**版本信息：**

- 发布时间：2024 年 2 月 28 日
- 版本号：V4.2.2_CE_HF1
- RPM 版本号：oceanbase-ce-4.2.2.0-100010012024022719

**版本概述：**

修复部署或在升级过程中经停过 V4.1.0_CE_BETA 或 V4.1.0_CE 版本的集群，在升级到 V4.2.2_CE 版本后，由于系统视图变更引发 Schema 刷新失败，导致 DDL 执行卡住的问题。

### V4.2.2_CE

[**点击查看 V4.2.2_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.2)

**版本信息：**

- 发布时间：2024 年 1 月 17 日
- 版本号：V4.2.2_CE
- RPM 版本号：oceanbase-ce-4.2.2.0-100000192024011915

**版本概述：**

作为 OceanBase 数据库 V4.2.1_CE 后继版本，V4.2.2_CE 版本已正式发布。内核层面进一步加强，重构估行系统和统计信息收集机制，持续完善 MySQL 兼容性，新增 Lateral Derived Tables、分页查询保序；同时也补充完善了 GIS/XML/JSON 等多模类型实现；新增 SQLSTAT、TIME MODEL、手动 Transfer 分区等多项易用性功能改进；通过降低索引临时空间占用、支持 OBKV RPC 压缩等一系列特性，优化系统资源使用。优化小规格基础测试性能，提高系统稳定性。

## V4.2.1

### V4.2.1_CE_BP10

[**点击查看 V4.2.1_CE_BP10 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 11 月 22 日
- 版本号：V4.2.1_CE_BP10
- RPM 版本号：oceanbase-ce-4.2.1.10-110000072024112010

**版本概述：**

- **备份配置项**

  用户在进行数据备份的时候，也期望能将源端集群级、租户级配置项一起备份，用于后续快速恢复集群和租户状态。新版本支持通过 `ALTER SYSTEM BACKUP CLUSTER PARAMETERS TO 'xxxx'` 命令对集群级配置项单独指定路径发起备份，并支持在备份数据集中增加租户配置项的备份。同时 ob_admin 工具提供了 `dump_backup` 命令用于查看备份的配置项信息。

- **备份租户资源配置信息**

  为了避免业务抖动，物理恢复的目标租户的资源配置建议与源租户相同。新版本支持将租户资源相关的配置一起备份到备份数据集中，包括 `primary_zone`/`unit_num`/`locality/unit config` 资源规格等，便于进行同等规格的租户恢复。

  关于配置项备份的详细介绍，参见 [配置项备份](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001667656)。

- **ASH 诊断热点分区**

  在不存在异常慢 SQL，但某个节点 CPU 负载很高时，可以怀疑可能存在热点分区问题。新版本在 ASH 中增加 `tablet_id` 信息的收集，便于监控热点分区，从而进行下一步的运维处理。

- **批量导入现有执行计划到 SPM 基线**

  OceanBase 已经支持指定 `sql_id` 导入 cache 中的执行计划到 SPM 基线的能力。但需要导入的计划较多时，一条条导入会比较麻烦，新版本新增 `DBMS_SPM.BATCH_LOAD_PLANS_FROM_CURSOR_CACHE` 子程序用于支持批量导入。

### V4.2.1_CE_BP9_HF1

[**点击查看 V4.2.1_CE_BP9_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 10 月 18 日
- 版本号：V4.2.1_CE_BP9_HF1
- RPM 版本号：oceanbase-ce-4.2.1.9-109010012024101414

**版本概览：**

修复使用 `ob_admin` 进行备份恢复操作异常的问题。

### V4.2.1_CE_BP9

[**点击查看 V4.2.1_CE_BP9 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 09 月 26 日
- 版本号：V4.2.1_CE_BP9
- RPM 版本号：oceanbase-ce-4.2.1.9-109000032024092015

**版本概述：**

- **磁盘空间统计的准确性和性能提升**

  OCP 的磁盘空间统计功能依赖内核提供统计数据，内核新版本优化了内部表的统计数据，提升了磁盘空间统计的准确性和性能。

- **主备库自动路由**

  在 V2.x、V3.x 系列中，OceanBase 支持集群级主备库，使用 `CLUSTER_NAME` 作为唯一表示一组主备集群的标识，用户通过 ODP 连接时，指定集群名即可自动路由到主集群。V4.x 变更为租户级主备库，主租户不记录备租户信息，备租户也不记录主租户信息，主备关系通过外部工具如 OCP 来维护，没办法通过 ODP 连接自动路由到主租户。新版本引入 `SERVICE_NAME` 概念，用于管理一组主备租户，通过 ODP 指定 `SERVICE_NAME` 登录，如 `obclient -h $ip -P $port -u$user_name@SERVICE:$service_name` ，ODP 可根据 `SERVICE_NAME` 将连接路由至主租户，以满足 V4.x 主备库自动路由的需求。同时，系统租户下也提供了一套 `SERVICE_NAME` 管理命令，用于为租户创建、删除、启动、停止 `SERVICE_NAME`。

  该功能需要配套 ODP V4.3.1 和 OCP V4.3.1 及之后版本使用。

- **定时/手动分区均衡**

  OceanBase V4.2 开始支持基于 Transfer 的分区均衡功能，通过租户级配置项 `partition_balance_schedule_interval` 控制均衡任务的调度周期，默认从 OBServer 启动时间算起，每 2 小时进行一次分区均衡。该配置项易用性较差，无法明确控制分区均衡任务的执行时间。由于 Transfer 动作可能会阻塞对应分区的读写，业务高峰期进行分区均衡会影响 RT；如果需要均衡的分区较多，也可能会暂时加大集群负载，影响集群性能。为了优化这一场景，新增 `DBMS_BALANCE` 系统包，为用户提供手动触发分区均衡的方法 `DBMS_BALANCE.TRIGGER_PARTITION_BALANCE(balance_timeout)`，同时在用户租户创建时内置了定时分区均衡任务 SCHEDULED_TRIGGER_PARTITION_BALANCE，默认每日 00:00 触发一次分区均衡，用户也可根据业务特点通过 DBMS_SCHEDULER 子程序修改定时调度的时间、频率等信息，以便更加灵活、可靠地管理分区均衡任务。

- **支持对函数索引收集统计信息**

  老版本未对函数索引收集统计信息，导致部分场景下，SQL 选不到包含函数索引的执行计划，进而无法获得最优性能。新版本调整收集策略，放开函数索引的统计信息收集。

- **Insertup、Replace 语句 multi query 性能优化**

  对 `INSERT ... VALUES ... ON DUPLICATE KEY UPDATE ...` 和 `REPLACE ... VALUES ...` 两类语句，支持 multi query 场景下的 batch 处理，提升 DML 执行性能。

- **S3 对象存储访问新增可选参数 addressing_model**

  支持 S3 路径配置可选参数 `addressing_model`，可选参数值：`virtual_hosted_style`/`path_style`。S3 路径配置`addressing_model=path_style` 后，支持以 path style addressing model 访问对象存储；配置 `addressing_model=virtual_hosted_style` 或不配置可选参数 `addressing_model` 默认以 virtual hosted style 访问对象存储。

### V4.2.1_CE_BP8

[**点击查看 V4.2.1_CE_BP8 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 7 月 31 日
- 版本号：V4.2.1_CE_BP8
- RPM 版本号：oceanbase-ce-4.2.1.8-108000022024072217

**版本概述：**

- **日志流副本管理**

  V4.0 之前的版本，OceanBase 数据库提供了分区副本管理的一系列运维命令，比如为分区添加一个副本、为分区删除一个副本、对分区的一个副本进行类型转换等。V4.x 系列在设计上使用日志流代替了分区的概念，对标低版本的分区运维命令。新版本重新设计实现了日志流副本级别任务的运维方式，提供了一系列语法，用于支持日志流副本的添加、删除、副本类型转换、迁移、修改日志流 Paxos 成员数量和取消容灾任务等能力，满足客户手动运维日志流副本的需求。

- **DBLink 支持指定域名访问**

  OceanBase 数据库支持通过 DBLink 访问远端数据库。老版本需要在创建 DBLink 时指定远端数据库的 IP 地址，新版本增加支持配置域名地址。

- **主备租户角色切换验证**

  OceanBase 数据库支持租户级主备角色切换，如在数据无损情况下可以将备租户 SWITCHOVER 成主租户，将主租户 SWITCHOVER 成备租户，或在数据损失情况下将备租户 FAILOVER 成主租户。主备租户角色切换操作有失败的可能，为了降低实际执行角色切换动作的风险，新版本新增支持主备租户角色切换验证功能（SWITCHOVER/FAILOVER VERIFY），在切换命令后添加 VERIFY 关键字，可以提前验证对应操作是否可以成功执行，如对应操作不可执行，将给出报错信息。

- **主备租户事件展示**

  OceanBase 数据库 V4.2.1 BP8 之前，主备租户 SWITCHOVER、FAILOVER 等事件记录在 RS 事件中，RS 事件会随时间清理，且租户级记录混在集群操作记录中不易查找。新版本将主备租户操作记录拆分到每个租户下，通过 `CDB/DBA_OB_TENANT_EVENT_HISTORY` 视图透出。

- **事务提交后 Cursor 访问**

  V4.0 开始，事务提交后不允许 Cursor 继续 Fetch 数据。V4.2.1 BP8 开始允许 Cursor 在没读取当前事务修改的表的情况下，在事务结束后依然可以 Fetch 数据，但需要通过 `_enable_enhanced_cursor_validation` 配置项开启。

- **增加 SM3 加密函数**

  MySQL 模式下新增 SM3 加密函数。

- **OBKV 响应时间统计直方图**

  在 V4.2.1 BP7 响应时间直方图功能基础上，新版本在 `[G]V$OB_QUERY_RESPONSE_TIME_HISTOGRAM` 系统视图中增加了 OBKV 相关的统计类别，包括 `TABLEAPI SELECT`、`TABLEAPI INSERT`、`TABLEAPI DELETE`、`TABLEAPI UPDATE`、`TABLEAPI REPLACE`、`TABLEAPI QUERY AND MUTATE`、`TABLEAPI OTHER`、`HBASE SCAN`、`HBASE PUT`、`HBASE DELETE`、`HBASE APPEND`、`HBASE INCREMENT`、`HBASE CHECK AND PUT`、`HBASE CHECK AND DELETE`、`HBASE HYBRID BATCH` 等。

- **OBKV-HBase 列分页**

  原生 HBase 支持列分页，这在大宽表场景下提供了更好的查询性能。新版本 OBKV-HBase 也提供了类似的列分页能力，支持通过 ColumnPaginationFilter 过滤器限制返回列数。

- **OBKV-HBase 逆序扫描**

  OBKV-HBase 的数据是按照 RowKey（行键）排序存储的，在需要有序访问数据的场景，一般会以 RowKey 正序（从小到大）扫描。但实际业务中还存在需要倒序访问数据的场景，因此新版本新增 Reverse Scan 功能，允许用户以 RowKey 逆序（从大到小）扫描表中的数据，提升查询性能。

- **操作系统适配支持**

  支持使用 Python 3 运行升级、TimeZone 导入等 OceanBase 内核自带的脚本，以适配部分高版本操作系统的 Python 环境依赖。

### V4.2.1_CE_BP7

[**点击查看 V4.2.1_CE_BP7 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 6 月 6 日
- 版本号：V4.2.1_CE_BP7
- RPM 版本号：oceanbase-ce-4.2.1.7-107000162024060611

**版本概述：**

- **CPU 架构适配支持**

  新增 ppc64le 架构支持。[\#1917](https://github.com/oceanbase/oceanbase/pull/1917)

- **旁路导入中间数据支持开启压缩**

  旁路导入过程中，中间数据占用空间过大时，可能会导致磁盘空间满，进而导致导入失败。新版本增加旁路导入中间数据压缩功能，通过租户级配置项 `_ob_ddl_temp_file_compress_func` 控制是否开启及使用的压缩算法。

  默认为 `NONE`，表示不开启压缩，适用于磁盘空间足够，希望获得更高导入性能的场景。根据业务需要可修改为 `ZSTD` 或 `LZ4`，来指定对应的压缩算法开启中间数据压缩，或设置为 `AUTO` 自适应开启压缩。

- **备份恢复支持 S3/OBS/GCS**

  新增支持 S3 协议，可将 S3/OBS/GCS 作为日志归档和数据备份的目的端，同时支持使用 S3/OBS/GCS 上的备份数据进行物理恢复。

- **SET/PIECE 级物理恢复**

  实际业务中存在二次备份场景，需把数据备份集或归档日志手动搬迁到新的路径。新版本增加了 SET/PIECE 级物理恢复功能，提供 `ADD RESTORE SOURCE` 命令来加载新路径的数据备份集 SET 或日志归档 PIECE，支持按需恢复到指定时间。更多信息请参见 [执行指定路径的恢复](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000827705)。

- **迁移复制源端选择优化**

  新版本将各 Server 按照地域信息划分为同 IDC、同 Region 不同 IDC、跨 Region 三种区域关系，同时提供 `choose_migration_source_policy` 配置项，用于迁移复制场景下，指定源端的选择模式，以便优先考虑地理位置就近因素以及 Follower 副本来提升迁移效率、降低 Leader 压力。更多信息请参见 [choose_migration_source_policy](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000833394)。

- **物理恢复进度统计**

  为了用户在使用物理恢复功能时可以了解恢复任务的运行状态和进度，并预估完成时间，新版本增加了物理恢复进度统计功能。用户可通过 `CDB/DBA_OB_RESTORE_PROGRESS` 视图实时查看恢复进度，获得更好的使用体验。更多信息请参见 [查看物理恢复进度](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000218387)。

- **大规格租户事务数据表转储调度优化**

  优化大规格租户下事务数据表转储不及时的问题，加快事务数据表的转储调度，进一步优化 Buffer 表性能。

- **全局 CPU 前后台任务隔离**

  在之前版本，OceanBase 数据库已实现通过租户 Unit 规格来配置租户间的 CPU 资源隔离，提供 `DBMS_RESOURCE_MANAGER` 系统包来配置租户内的 CPU 资源隔离。新版本支持全局 CPU 前后台任务隔离，可以在整体层面上限制后台任务的可用资源，相对租户内使用 `DBMS_RESOURCE_MANAGER` 单独配置更加方便易用。更多信息请参见 [使用全局 CPU 资源的前后台隔离](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000859614)。

- **新增响应时间统计直方图**

  在之前版本，OceanBase 数据库已支持基于不同 SQL 类别的平均响应时间/最大响应时间指标，但缺乏更细粒度的反映某个分位 SQL 执行性能的指标展示。新版本增加响应时间直方图功能，可基于 `[G]V$OB_QUERY_RESPONSE_TIME_HISTOGRAM` 系统视图计算和监控不同类型 SQL 的 P90/P95 之类的响应时间统计。更多信息请参见 [GV\$OB_QUERY_RESPONSE_TIME_HISTOGRAM](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000833390)、[V\$OB_QUERY_RESPONSE_TIME_HISTOGRAM](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000833389)。

- **分区均衡策略优化**

  新版本优化了分区均衡策略，支持在创建分区表时连续分区打散。当用户表存在 longtext/lob 列或局部索引时，分区磁盘均衡也会计算关联表，使磁盘使用更加均衡。更多信息请参见 [租户内均衡](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000801146)。

- **OBCDC 启动加速**

  新版本优化了 OBCDC 启动性能，协助提升下游 Binlog 工具的同步性能。

- **JSON 可嵌套层数扩展**

  历史版本限制 JSON 文档的可嵌套最大深度为 100，新版本提供 `json_document_max_depth` 配置项，允许用户根据需求调整嵌套深度。对于超过 100 的 JSON 嵌套层数需求，用户可适当调大该配置。更多信息请参见 [json_document_max_depth](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000833393).

- **支持 HBase PageFilter 功能**

  OB-HBase 模型下, 支持使用 HBase 中的 PageFilter 对 Row 进行限制, 返回指定数量的 Row。

- **备份性能优化**

  OceanBase 数据库在备份过程中，通过连续性校验确保基线版本大于转储版本来保证数据完整。然而，连续性检查涉及读取备份介质上的数据并执行带锁操作，因此会影响备份性能。新版本优化了备份过程中连续性校验操作带来的性能开销，支持通过 `ha_low_thread_score` 控制备份使用的线程数，从而有效提高备份性能。更多信息请参见 [ha_low_thread_score](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000220387)。

### V4.2.1_CE_BP6

[**点击查看 V4.2.1_CE_BP6 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 5 月 15 日
- 版本号：V4.2.1_CE_BP6
- RPM 版本号：oceanbase-ce-4.2.1.6-106000012024042515

**版本概述：**

**优化 `show table status` 性能：** 老版本 `show table status from ... like ...` 场景性能较差，未利用 `table_name` 相关索引。新版本针对存在单表过滤条件的场景，显著提升查询性能。

### V4.2.1_CE_BP5

[**点击查看 V4.2.1_CE_BP5 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 4 月 24 日
- 版本号：V4.2.1_CE_BP5
- RPM 版本号：oceanbase-ce-4.2.1.5-105000032024041915

**版本概述：**

- **MySQL 兼容性**

  - 支持在同一个 `SET` 语句中同时包含 `SET NAMES` 语句和使用 `SET` 设置其他变量。
  - 支持兼容 MySQL 的 `information_schema.events` 表结构。 [\#1194](https://github.com/oceanbase/oceanbase/issues/1194)

- **其他优化**

  - 新增 `[G]V$OB_SESSION` 视图展示会话信息，优化 Processlist 统计时间。
  - `GV$OB_SQL_AUDIT` 视图新增 `NETWORK_WAIT_TIME` 字段，用于展示所有 Network 类事件的总时间。
  - 新增 `_parallel_ddl_control` 参数用于控制是否在租户级别开启各类并行 DDL 的功能。
  - 支持将 `slog` 和 `sstable` 的目录放在不同的磁盘目录下。
  - 优化 LOB 类型数据外联存储（OUTROW）性能。
  - 优化 PL Cache 缓存失效的问题。
  - 优化 Buffer 表的自适应合并。
  - 优化统计信息收集的性能。

### V4.2.1_CE_BP4

[**点击查看 V4.2.1_CE_BP4 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 3 月 5 日
- 版本号：V4.2.1_CE_BP4
- RPM 版本号：oceanbase-ce-4.2.1.4-104000052024022918

**版本概述：**

- OBKV Batch Put 现支持覆盖写功能，使用该功能前需要升级到最新版本的客户端。
- 手动迁移分区功能支持 Cancel。
- 优化查询语句中包含多个 `MIN` 或 `MAX` 函数时的查询性能。
- 支持通过 `information_schema.STATISTICS` 的 `COMMENT` 字段来判断索引状态。

### V4.2.1_CE_BP3_HF2

[**点击查看 V4.2.1_CE_BP3_HF2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 2 月 5 日
- 版本号：V4.2.1_CE_BP3_HF2
- RPM 版本号：oceanbase-ce-4.2.1.3-103020042024020317

**版本概述：**

- 支持 Java 客户端导入超过 2M 的 LOB 数据。

- 支持通过 obshell 命令行工具对集群进行运维管理，支持通过 `systemd service` 的方式启停 OceanBase 数据库。

- 修复在并行删除列场景下，可能由于内存分配问题导致 OBServer Core 的问题。

### V4.2.1_CE_BP3_HF1

[**点击查看 V4.2.1_CE_BP3_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 1 月 25 日
- 版本号：V4.2.1_CE_BP3_HF1
- RPM 版本号：oceanbase-ce-4.2.1.3-103010052024011916

**版本概述：**

修复了一系列问题，包括：解决了 `DBMS_MONITOR` 包无法处理小数类型数据的问题、修复了含 LONGTEXT 列的 OBKV TTL 任务执行失败、修复了带主键自增列和二级索引的表不能通过 OBKV 客户端插入更新、修复了 OSS 驱动代码缺少空指针判断导致的 OBSERVER 崩溃、改善了 `order by + limit` 查询的执行计划问题、解决了备份和 medium compaction 并发导致的进程卡住、以及修复了 Transfer 期间因 SSTable 数量多导致查询性能下降问题。

### V4.2.1_CE_BP3

[**点击查看 V4.2.1_CE_BP3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2024 年 1 月 2 日
- 版本号：V4.2.1_CE_BP3
- RPM 版本号：oceanbase-ce-4.2.1.3-103000032023122818

**版本概述：**

新增了多项功能和性能优化，主要包括：支持 OBServer 与 ODP 之间的通信协议层压缩功能以减少数据传输带宽成本；OBKV 增加了对全局索引的支持；实现了 `INSERT ... ON DUPLICATE KEY UPDATE` 语法；新增了控制 MySQL 模式下最大分区数的配置项 `max_partition_num`；支持通过 `DBMS_STATS.copy_table_stats` 复制统计信息；对 `information_schema.schemata` 表实施权限过滤，用户只能查询有权限的 Schema；优化了网络直连主备库架构下的数据同步性能；改善了通过 `max_concurrent` 限制 SQL 流量场景下的系统负载，以及 `CDB_OB_BACKUP_TASKS` 视图新增了 `DATA_PROGRESS` 字段，用于显示数据备份进度。

### V4.2.1_CE_BP2_HF1

[**点击查看 V4.2.1_CE_BP2_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2023 年 12 月 18 日
- 版本号：V4.2.1_CE_BP2_HF1
- RPM 版本号：oceanbase-ce-4.2.1.2-102010022023121415

**版本概述：**

从 V4.2.1_CE_BP2_HF1 版本开始，新建集群时，Nested Loop join（NLJ）和 SUBPLAN FILTER（SPF）算子的 BATCH RESCAN 优化默认会被关闭。然而，对于从老版本升级上来的集群，它们会默认保持原来的 BATCH RESCAN 打开的状态。对于存量的环境，如果发现 NLJ/SPF BATCH RESCAN 的稳定性问题，可以通过执行 `SET GLOBAL _nlj_batching_enabled = false;` 命令来关闭该优化，这将在整个集群范围内禁用 NLJ/SPF 的 BATCH RESCAN 优化。如果在关闭优化后性能不符合预期，可以根据具体情况重新评估并选择是否重新开启。

### V4.2.1_CE_BP2

[**点击查看 V4.2.1_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2023 年 12 月 7 日
- 版本号：V4.2.1_CE_BP2
- RPM 版本号：oceanbase-ce-4.2.1.2-102000042023120514

**版本概述：**

在 MySQL 模式下增加了保序的分页查询功能，新增了 TRANSFER PARTITION 命令用于手动调整分区分布，以及 OBKV 支持 RPC 数据压缩从而减少网络带宽占用。此外，还支持设置 LOB 数据存储方式的转换阈值，用于优化大对象场景下的性能。

### V4.2.1_CE_BP1_HF1

[**点击查看 V4.2.1_CE_BP1_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2023 年 11 月 13 日
- 版本号：V4.2.1_CE_BP1_HF1
- RPM 版本号：oceanbase-ce-4.2.1.1-101010012023111012

**版本概述：**

解决客户及内部测试遇到的问题，提升版本稳定性。

### V4.2.1_CE_BP1

[**点击查看 V4.2.1_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2023 年 11 月 1 日
- 版本号：V4.2.1_CE_BP1
- RPM 版本号：oceanbase-ce-4.2.1.1-101000062023110109

**版本概述：**

针对用户自定义变量增强了与 MySQL 数据库的兼容性，引入了新的视图 `GV$OB_KV_CONNECTIONS` 和 `V$OB_KV_CONNECTIONS` 用于监控 KV 连接活跃情况，调整了系统变量 `ob_tcp_invited_nodes` 的长度限制至 64K，并将 `ls_gc_delay_time` 配置项的默认值调整为 0。此外，通过解决客户和内部测试发现的问题，进一步提高了版本的稳定性。

### V4.2.1_CE

[**点击查看 V4.2.1_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.1)

**版本信息：**

- 发布时间：2023 年 10 月 13 日
- 版本号：V4.2.1_CE
- RPM 版本号：oceanbase-ce-4.2.1.0-100000102023092807

**版本概述：**

OceanBase 数据库 V4.2.1_CE 版本是 V4.2.x_CE 版本系列的第一个长期支持版本（LTS），该版本新增了 VALUES 语句、JSON_TABLE 表达式等与 MySQL 兼容的功能，推出了 WR 数据采集框架和增强全链路诊断的产品化。同时，该版本还优化了系统资源的使用，并增加了表级恢复能力和对备份介质 COS 的支持。推荐将其用于常规业务的生产环境中。

## V4.2.0

### V4.2.0_CE_BP1

[**点击查看 V4.2.0_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.0)

**版本信息：**

- 发布时间：2023 年 9 月 14 日
- 版本号：V4.2.0_CE_BP1
- RPM 版本号：oceanbase-ce-4.2.0.0-101000032023091319

**版本概述：**

解决客户及内部测试遇到的问题，提升版本稳定性。

### V4.2.0_CE

[**点击查看 V4.2.0_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.0)

**版本信息：**

- 发布时间：2023 年 9 月 4 日
- 版本号：V4.2.0_CE
- RPM 版本号：oceanbase-ce-4.2.0.0-100010032023083021

**版本概述：**

- 解决客户及内部测试遇到的问题，提升版本稳定性。
- 社区版支持 MySQL 租户间的 DBLINK 读功能。
- MySQL 模式下禁用临时表功能。

### V4.2.0_CE_BETA_HF1

[**点击查看 V4.2.0_CE_BETA_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.0)

**版本信息：**

- 发布时间：2023 年 8 月 21 日
- 版本号：V4.2.0_CE_BETA_HF1
- RPM 版本号：oceanbase-ce-4.2.0.0-100010022023081817

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.2.0_CE_BETA

[**点击查看 V4.2.0_CE_BETA Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.2.0)

**版本信息：**

- 发布时间：2023 年 8 月 2 日

- 版本号：V4.2.0_CE_BETA

- RPM 版本号：oceanbase-ce-4.2.0.0-100000152023080109

- 版本说明：Beta 版本解决了大部分缺陷，并趋于稳定。推荐测试环境使用。

**版本概述：**

OceanBase 数据库 V4.2.0_CE 版本是在 V4.1.0_CE 版本基础上进一步健全完善核心特性，补齐了 V3.x 系列的全部主要功能，提升产品可扩展性，优化资源使用，提高性能，增强兼容性与易用性。目前发布的为 V4.2.0_CE Beta 版本，而后续的 V4.2.x 版本也会作为 **长期支持版本（LTS）** 对外提供服务。

## V4.1.0

### V4.1.0_CE_BP4_HF1

[**点击查看 V4.1.0_CE_BP4_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 10 月 8 日
- 版本号：V4.1.0_CE_BP4_HF1
- RPM 版本号：oceanbase-ce-4.1.0.2-104010012023100710

**版本概述：**

解决客户及内部测试遇到的问题，提升版本稳定性。

### V4.1.0_CE_BP4

[**点击查看 V4.1.0_CE_BP4 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 9 月 25 日
- 版本号：V4.1.0_CE_BP4

**版本概述：**

- MySQL 模式下禁用临时表功能。
- 解决客户及内部测试遇到的问题，提升版本稳定性。

### V4.1.0_CE_BP3_HF1

[**点击查看 V4.1.0_CE_BP3_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 8 月 28 日
- 版本号：V4.1.0_CE_BP3_HF1
- RPM 版本号：oceanbase-ce-4.1.0.2-103010012023082519

**版本概述：**

解决客户及内部测试遇到的问题，提升版本稳定性。

### V4.1.0_CE_BP3

[**点击查看 V4.1.0_CE_BP3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 8 月 14 日
- 版本号：V4.1.0_CE_BP3
- RPM 版本号：oceanbase-ce-4.1.0.2-103000072023081111

**版本概述：**

1.  OBKV 支持 min、max、count 等汇聚函数，同时支持自增列和插入数据时的行数据校验。
2.  新增了两个隐藏配置项 `_ha_get_tablet_info_batch_count` 和 `_ha_rpc_timeout`，用于控制迁移复制、Rebuild 和物理恢复等操作中一次 RPC 批量获取 Tablet 的数量和 RPC 超时时间。这些配置项适用于 SATA 盘 IO 较慢的场景。
3.  开放 `DBMS_RESOURCE_MANAGER` 系统包到开源版本。
4.  解决客户及内部测试遇到的问题，提升版本稳定性。

### V4.1.0_CE_BP2

[**点击查看 V4.1.0_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 6 月 15 日
- 版本号：V4.1.0_CE_BP2
- RPM 版本号：oceanbase-ce-4.1.0.1-102000042023061314

**版本概述：**

- SHOW CREATE TABLE 兼容 MySQL 以满足周边工具需求。
- 解决用户及内部测试遇到的问题，提升版本稳定性。

### V4.1.0_CE_BP1_HF1

[**点击查看 V4.1.0_CE_BP1_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 5 月 19 日
- 版本号：V4.1.0_CE_BP1_HF1
- RPM 版本号：oceanbase-ce-4.1.0.0-101010022023051821

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.1.0_CE_BP1

[**点击查看 V4.1.0_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 5 月 12 日
- 版本号：V4.1.0_CE_BP1
- RPM 版本号：oceanbase-ce-4.1.0.0-101000022023050809

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.1.0_CE

[**点击查看 V4.1.0_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 4 月 20 日
- 版本号：V4.1.0_CE
- RPM 版本号：oceanbase-ce-4.1.0.0-100000202023040520

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.1.0_CE_BETA

[**点击查看 V4.1.0_CE_BETA Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.1.0)

**版本信息：**

- 发布时间：2023 年 3 月 20 日
- 版本号：V4.1.0_CE_BETA
- RPM 版本号：oceanbase-ce-4.1.0.0-100000192023032010

**版本概述：**

OceanBase 数据库 V4.0 社区版本是对分布式数据库系统架构设计的全面升级，OceanBase 数据库 V4.1 版本面向公有云&开源用户场景需求，在对功能健全优化的同时，不断对产品进行打磨和完善，在对 MySQL 8.0 兼容、性能、易用性、成本方面进行优化增强，目标支持项目规模化复制，是真正可全面商业化推广的版本。

## V4.0.0

### V4.0.0_CE_BP3

[**点击查看 V4.0.0_CE_BP3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.0.0)

**版本信息：**

- 发布时间：2023 年 1 月 12 日
- 版本号：V4.0.0_CE_BP3
- RPM 版本号：oceanbase-ce-4.0.0.0-103000022023011215

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.0.0_CE_BP2

[**点击查看 V4.0.0_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.0.0)

**版本信息：**

- 发布时间：2022 年 12 月 7 日
- 版本号：V4.0.0_CE_BP2
- RPM 版本号：oceanbase-ce-4.0.0.0-102000032022120718

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.0.0_CE_BP1

[**点击查看 V4.0.0_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.0.0)

**版本信息：**

- 发布时间：2022 年 11 月 23 日
- 版本号：V4.0.0_CE_BP1
- RPM 版本号：oceanbase-ce-4.0.0.0-100000282022112511

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V4.0.0_CE

[**点击查看 V4.0.0_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V4.0.0)

**版本信息：**

- 发布时间：2022 年 11 月 2 日
- 版本号：V4.0.0_CE
- RPM 版本号：oceanbase-ce-4.0.0.0-100000272022110114

**版本概述：**

OceanBase 社区发布 V4.0.0 版本是对分布式数据库系统架构设计的全面升级，定位为 Beta 测试版本，社区会关注用户使用反馈，不断对产品进行打磨和完善，应用项目投产上线需要慎重审视和仔细评估。

OceanBase V4.0 版本在保证功能特性不丢失的前提下，重新审视了数据库与分布式系统两个领域最基础的设计，全新推出业内首个单机分布式一体化架构，重点构建 HTAP 和云化两个基础能力属性。与此同时，本版本也从架构上解决了 V3.2 版本的设计瓶颈，支持更多用户业务关注的多个核心能力，在内核功能、兼容性、稳定性、性能上取得突破。

## V3.1.5

### V3.1.5_CE_HF2

[**点击查看 V3.1.5_CE_HF2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.5)

**版本信息：**

- 发布时间：2023 年 9 月 12 日
- 版本号：V3.1.5_CE_HF2
- RPM 版本号：oceanbase-ce-3.1.5-100020022023091114

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.5_CE_HF1

[**点击查看 V3.1.5_CE_HF1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.5)

**版本信息：**

- 发布时间：2023 年 6 月 19 日
- 版本号：V3.1.5_CE_HF1
- RPM 版本号：oceanbase-ce-3.1.5-100010012023060910

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.5_CE

[**点击查看 V3.1.5_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.5)

**版本信息：**

- 发布时间：2023 年 4 月 19 日
- 版本号：V3.1.5_CE
- RPM 版本号：oceanbase-ce-3.1.5-100000252023041721

**版本概述：**

间隔十余月，OceanBase 数据库迎来了社区版 V3.1.5 版本的正式发布。该版本着重提高了内核的稳定性，在特性上 OBKV 支持了基于热 Key 的限流，OBCDC 通过架构优化降低了对使用者机器的资源要求。同时为满足用户对大宽表的期待，将单表列限制从 512 列优化提升至 4096 列。针对用户反馈及内部测试发现的问题，该版本也重点进行了修复。

## V3.1.4

### V3.1.4_CE_BP3

[**点击查看 V3.1.4_CE_BP3 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.4)

**版本信息：**

- 发布时间：2023 年 2 月 10 日
- 版本号：V3.1.4_CE_BP3
- RPM 版本号：oceanbase-ce-3.1.4-103000102023020719

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.4_CE_BP2

[**点击查看 V3.1.4_CE_BP2 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.4)

**版本信息：**

- 发布时间：2022 年 12 月 25 日
- 版本号：V3.1.4_CE_BP2
- RPM 版本号：oceanbase-ce-3.1.4-102000012022120715

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.4_CE_BP1

[**点击查看 V3.1.4_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.4)

**版本信息：**

- 发布时间：2022 年 10 月 27 日
- 版本号：V3.1.4_CE_BP1
- RPM 版本号：oceanbase-ce-3.1.4-100000112022102717

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.4_CE

[**点击查看 V3.1.4_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.4)

**版本信息：**

- 发布时间：2022 年 7 月 18 日
- 版本号：V3.1.4_CE
- RPM 版本号：oceanbase-ce-3.1.4-10000092022071511

**版本概述：**

在 V3.1.4 版本，OceanBase 数据库针对社区项目应用反馈，优化提升内核易用性与稳定性，服务广大社区用户。

- 内核能力提升：支持数据文件动态按需分配，支持直方图类型统计信息采集与监控。

- 稳定性提升：多模 OBKV 支持历史数据过期清理，扩展单表大事务能力上限。

- 易用性提升：支持删除单条缓存计划，优化日志与错误码展示等，ob-operator 支持部署 obproxy，开源最新测试套框架。

## V3.1.3

### V3.1.3_CE_BP1

[**点击查看 V3.1.3_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.3)

**版本信息：**

- 发布时间：2022 年 4 月 15 日
- 版本号：V3.1.3_CE_BP1
- RPM 版本号：oceanbase-ce-3.1.3-10100032022041510

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.3_CE

[**点击查看 V3.1.3_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.3)

**版本信息：**

- 发布时间：2022 年 3 月 30 日
- 版本号：V3.1.3_CE
- RPM 版本号：oceanbase-ce-3.1.3-10000292022032916

**版本概述：**

在 OceanBase 数据库 V3.1.3 版本，OceanBase 数据库进一步增强社区生态能力，更好地服务广大社区用户。

- 多模应用：新增 JSON 格式数据类型和 OBKV HBASE 客户端，支持半结构化和 NoSQL 类型业务场景应用。

- 生态能力增强：支持 MySQL 原生的 Python/Go/ODBC 类型驱动连接 OceanBase 数据库，发布 ob-operator 支持 K8s 容器编排，支持 ARM 平台编译运行。

- 更优的产品能力：支持更小的资源规格（2C8GB），提升 CDC 链路同步可靠性。

## V3.1.2

### V3.1.2_CE

[**点击查看 V3.1.2_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.2)

**版本信息：**

- 发布时间：2021 年 12 月 30 日
- 版本号：V3.1.2_CE
- RPM 版本号：oceanbase-ce-3.1.2-10000392021123010

**版本概述：**

OceanBase 数据库 V3.1.2_CE 版本为 OceanBase 数据库的用户提供了免费的图形界面开发者工具（ODC）、运维监控云平台（OCP）、数据迁移工具（OMS）、导数工具（obloader 和 obdumper）。

OceanBase 数据库支持在线跨版本轮转升级，可通过 obd 指定需要升级到的版本，自动完成最佳升级路径解析和应用升级，全过程无需人工干预且不影响业务运行。优化了热点行数据更新，性能提升了 300%。优化了分区表 SQL PLAN 淘汰机制。优化了底层通信代码等。新增了多个 SQL MODE 和系统函数。

## V3.1.1

### V3.1.1_CE_BP1

[**点击查看 V3.1.1_CE_BP1 Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.1)

**版本信息：**

- 发布时间：2021 年 10 月 21 日
- 版本号：V3.1.1_CE_BP1
- RPM 版本号：oceanbase-ce-3.1.1-4

**版本概述：**

本次发版主要是 BUG 修复，提升版本稳定性。

### V3.1.1_CE

[**点击查看 V3.1.1_CE Release Notes 的完整内容**](https://www.oceanbase.com/product/oceanbase-database-community-rn/releaseNote#V3.1.1)

**版本信息：**

- 发布时间：2021 年 9 月 30 日
- 版本号：V3.1.1_CE
- RPM 版本号：oceanbase-ce-3.1.1-1

**版本概述：**

OceanBase 数据库 V3.1.1_CE 版本全面提升内核兼容、工具生态、接口开放、备份恢复、开源 OS 支持和易用性能力，持续增强开源产品化应用能力。您可以获得以下关键特性：

- 支持 MySQL 5.7 驱动协议。
- 新增 MySQL 8.0 的通用表表达式（Common Table Expressions），丰富了 SQL 的能力，满足复杂业务查询需求实现。
- 新增校验函数 `CRC32()`，完善 MySQL 数据迁移到 OceanBase 的数据校验环节。
- 新增物理备份和恢复功能，支持近实时的数据备份和恢复到历史任意时间点功能，提升社区版的容灾能力。
- 新增 TABLE API 接口，支持 KV 接口读写数据，提升高性能存储访问能力。
- 新增 REDO 日志接口 CDC 能力，方便用户抽取 OceanBase 增量数据和跟第三方数据同步产品对接，解决了数据实时流出 OceanBase 难题。
- 支持对接 Prometheus，提升性能监控和诊断能力。
- 新增管理员工具 `ob_admin` 和 ERROR CODE 解释工具 `ob_error`，提升问题排查分析和故障应急处理能力。
- obd 新增命令参数，支持自动配置相关参数；新增租户管理命令；新增常用数据库性能测试框架，方便初次使用 OceanBase 数据库。
