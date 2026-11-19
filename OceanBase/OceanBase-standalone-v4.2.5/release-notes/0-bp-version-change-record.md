---
title: "V4.2.5 文档更新记录"
book: "版本发布记录"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003138710.html"
tags:
  - oceanbase
  - standalone
  - release-notes
---

# V4.2.5 文档更新记录

## V4.2.5 BP7（2025-11-03）

[TABLE]

## V4.2.5 BP6（2025-08-25）

| 功能 | 描述 |
|----|----|
| 新增 enable_ls_leader_balance 配置项 | 用于控制是否开启日志流 Leader 的自动均衡。更多信息请参见 [enable_ls_leader_balance](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003809980)。 |
| 函数 TO_PINYIN 新增参数 | 新增可选参数 `option`，以控制输出的大小写、全拼或首字母输出。更多信息请参见 [TO_PINYIN（MySQL）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002062766) 和 [TO_PINYIN（Oracle）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002062767)。 |
| **物理备份与恢复概述**章节新增 Azure Blob 描述 | OceanBase 数据库当前版本支持阿里云 OSS、NFS、Azure Blob（在 V4.2.5 版本中，从 V4.2.5 BP6 版本开始支持）、AWS S3 以及兼容 S3 协议的对象存储（例如：华为 OBS、Google GCS、腾讯云 COS），部分备份介质需要满足一些基本要求才能使用。更多信息请参见 [物理备份与恢复概述](../manage/100-overview-of-physical-backup-and-recovery.md)。 |
| 新增 Azure Blob 配置示例 | 与 OSS 一样，Azure Blob 也支持 `delete_mode` 参数和 `checksum_type` 参数。更多信息请参见 [日志归档前准备](../manage/200-preparation-before-log-archive.md)和[备份前准备](../manage/100-preparation-before-data-backup.md)。 |
| SET LOG_ARCHIVE_DEST 语法新增 Azure Blob 的参数说明 | 在 SET LOG_ARCHIVE_DEST 中包含 Azure Blob 的语法格式为 `ALTER SYSTEM SET LOG_ARCHIVE_DEST='LOCATION=azblob:////your-bucket-name/your-archive-path?host=your-service.com&access_id=your-access-id&access_key=your-access-key[&delete_mode={delete | tagging}][&checksum_type=md5]';`更多信息请参见 [SET LOG_ARCHIVE_DEST](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503152)。 |
| SET DATA_BACKUP_DEST 语法新增 Azure Blob 的参数说明 | 在 SET DATA_BACKUP_DEST 中包含 Azure Blob 的语法格式为 `ALTER SYSTEM SET DATA_BACKUP_DEST = 'oss://your-bucket-name/your-archive-path?host=oss-your-region.aliyuncs.com&access_id=your-access-id&access_key=your-access-key[&delete_mode={delete | tagging}][&checksum_type={md5 | no_checksum}][&enable_worm={true | false}]';`更多信息请参见 [SET DATA_BACKUP_DEST](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503153)。 |
| 新增 ob_deterministic_udf_cache_max_size 配置项 | 用于标记语句执行期，所有 `deterministic` 的 UDF 的缓存池总共可以使用的最大内存量。更多信息请参见 [ob_deterministic_udf_cache_max_size](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003799219)。 |
| 新增 DBA_OB_PL_OBJ_CACHE_STATUS 视图 | 用于展示 PL 缓存对象的状态信息。更多信息请参见 [DBA_OB_PL_OBJ_CACHE_STATUS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003815081)。 |

## V4.2.5 BP5（2025-07-18）

| 功能 | 描述 |
|----|----|
| MySQL 模式支持快速删列 | MySQL 模式下，老版本删列是 Offline DDL，需同步等待数据重整完成，随着数据量增加 DDL 耗时也会增加。新版本实现了快速删列功能，删除列过程中不重整表数据，只在 TableSchema 中标记列被删除(即 UNUSED 列)。由于没有重整数据操作，磁盘水位线并不会因为删列完成而下降。如果想要彻底移除标记删除列，需要执行 `ALTER TABLE TABLE_NAME FORCE` 命令等待数据重整。更多信息请参见 [快速删列](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503357)。 |
| 视图 CDB_OB_LS 新增列 | 新增 UNIT_LIST 列，描述日志流的 Unit 分布列表。更多信息请参见 [CDB_OB_LS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501318)。 |
| 视图 DBA_OB_LS 新增列 | 新增 UNIT_LIST 列，描述日志流的 Unit 分布列表。更多信息请参见 [DBA_OB_LS(MySQL)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501788) 和 [DBA_OB_LS(Oracle)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001500803)。 |
| 视图 DBA_OB_TENANTS 新增列 | 新增 ZONE_UNIT_NUM_LIST 列，租户各 Zone 的 Unit。更多信息请参见 [DBA_OB_TENANTS(MySQL)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501698) 和 [DBA_OB_TENANTS(Oracle)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001500982)。 |
| 视图 CDB_OB_BALANCE_JOBS 新增列 | 新增 ZONE_UNIT_NUM_LIST 列，记录租户各个 Zone 的 Unit 数量；新增 PARAMETER_LIST 列，展示均衡相关的配置项参数。更多信息请参见 [CDB_OB_BALANCE_JOBS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501307)。 |
| 视图 DBA_OB_BALANCE_JOBS 新增列 | 更多信息请参见 [DBA_OB_BALANCE_JOBS(MySQL)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501785) 和 [DBA_OB_BALANCE_JOBS(Oracle)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001500963)。 |
| 视图 DBA_OB_BALANCE_JOB_HISTORY 新增列 | 更多信息请参见 [DBA_OB_BALANCE_JOB_HISTORY(MySQL)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501819) 和 [DBA_OB_BALANCE_JOB_HISTORY(Oracle)](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501004)。 |

## V4.2.5 BP4（2025-05-30）

[TABLE]
