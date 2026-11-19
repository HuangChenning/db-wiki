---
title: "PL/SQL 对象批量编译最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003969213.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# PL/SQL 对象批量编译最佳实践

在数据库运维和开发过程中，PL/SQL 对象的批量编译是一个常见的任务。无论是数据库版本升级、大规模 DDL 变更，还是生产环境中的对象修复，都需要批量编译解决方案。OceanBase 数据库提供的 UTL_RECOMP 包为 PL/SQL 对象（如存储过程、函数、包、触发器和用户定义类型）的批量编译提供了企业级的解决方案，支持并行编译、智能依赖管理、错误处理等高级功能。

本文档将详细介绍 UTL_RECOMP 包的使用方法、编译策略制定、性能优化技巧以及最佳实践，帮助数据库管理员和开发人员高效完成 PL/SQL 对象的批量编译任务。

## 适用场景

- **数据库版本升级**：数据库版本升级后，大量 PL/SQL 对象失效需要重新编译。涉及编译依赖管理、并行编译调度、失败对象处理等技术挑战。

- **数据迁移**：从其他数据库迁移到 OceanBase 时，需要重新编译所有 PL/SQL 对象。需要处理语法兼容性、依赖关系重建、批量验证等问题。

- **大规模 DDL 变更后验证**：执行涉及大量表结构变更（如添加/删除列、修改数据类型）的迁移脚本，或者重建大量表后，依赖这些表的视图、存储过程、函数等对象失效。需要处理依赖关系分析、批量验证、增量编译等 问题。

- **处理级联失效**：修改被广泛引用的基础包或视图后，基础对象本身编译成功。需要运行 UTL_RECOMP 来重新编译所有因此次修改而失效的依赖对象。

- **定期维护或健康检查**：作为数据库定期维护计划的一部分，或者在执行健康检查时发现存在无效对象。需要在维护窗口内运行 UTL_RECOMP 来清理数据库或特定模式中的无效对象。

- **生产环境对象修复**：生产环境中出现 PL/SQL 对象失效，需要快速批量修复。要求最小影响编译、错误恢复、业务连续性保障。

## UTL_RECOMP 包接口

UTL_RECOMP 包对外暴露 5 个 procedure，两个 flag：

``` sql
USE_EXIST_TABLE   CONSTANT PLS_INTEGER := 512;
DROP_EXIST_TABLE  CONSTANT PLS_INTEGER := 1024;

PROCEDURE recomp_parallel(threads PLS_INTEGER := NULL,
                            schema  VARCHAR2    := NULL,
                            flags   PLS_INTEGER := 0);
PROCEDURE recomp_serial(schema VARCHAR2 := NULL,
                          flags PLS_INTEGER := 0);
PROCEDURE parallel_slave(flags PLS_INTEGER);
PROCEDURE truncate_utl_recomp_skip_list(flags PLS_INTEGER := 0);
PROCEDURE populate_utl_recomp_skip_list(flags PLS_INTEGER := 0);
```

### 参数说明

- **threads**：指定并行工作线程数。NULL 表示使用默认值（通常与 CPU 核心数相关）
- **schema**：指定要编译的模式名。NULL 表示编译当前租户下的所有 PL/SQL 对象
- **flags**：控制表处理方式
  - `USE_EXIST_TABLE`：如果 SYS 下已经存在同名的表，则直接使用该表
  - `DROP_EXIST_TABLE`：如果已经存在同名表，则 drop 掉，自动重新创建

## 使用指南

### 编译顺序与依赖处理

UTL_RECOMP 会尝试按依赖关系编译对象，但由于依赖可能很复杂，有时需要运行多次才能成功编译所有对象（第一次编译后，依赖它的对象可能变成有效并可编译）。每次运行后检查 DBA_ERRORS 查看编译错误。

### 并行度设置

**推荐设置**：

- 对于大型数据库：设置并行度为 CPU 核心数的 1-2 倍
- 对于资源受限环境：使用串行编译（RECOMP_SERIAL）
- 避免设置过高的并行度，可能导致资源争用

``` sql
-- 根据 CPU 核心数设置合适的并行度
EXEC UTL_RECOMP.RECOMP_PARALLEL(4);  -- 4 核 CPU 推荐设置
```

### 错误处理

编译失败的对象会保持 INVALID 状态。您必须检查 DBA_ERRORS 视图来定位和修复具体的编译错误（通常是代码语法错误或引用缺失的对象）。

``` sql
-- 查看编译错误
SELECT * FROM DBA_ERRORS WHERE NAME = 'OBJECT_NAME';
```

### 表管理

UTL_RECOMP 使用 SYS 用户下的 4 个表，需要确保 SYS 用户下没有用户创建的这 4 个同名表：

- SYS.UTL_RECOMP_SORTED
- SYS.UTL_RECOMP_COMPILED
- SYS.UTL_RECOMP_ERRORS
- SYS.UTL_RECOMP_SKIP_LIST

### 执行时机

调用 recomp_parallel 和 recomp_serial 时，建议您确保系统中没有正在执行的 DDL，否则可能会有非预期情况发生。调用 recomp_parallel 和 recomp_serial 时请确保：

- **维护窗口执行**：建议在维护窗口内执行，避免影响业务正常运行
- **避免 DDL 冲突**：确保系统中没有正在执行的 DDL 操作，避免产生非预期结果
- **单 session 执行**：不要多 session 并行执行，因为多个 session 会使用相同的系统表汇总结果，可能互相覆盖数据

## 使用案例

某企业在数据库版本升级后，发现大量 PL/SQL 对象失效，需要进行批量编译。数据库环境：OceanBase V4.4.0，包含 3 个业务模式（APP_USER、BIZ_USER、REPORT_USER），总计约 500 个 PL/SQL 对象需要重新编译。

### 操作步骤

1.  编译前检查

    ``` sql
    -- 检查当前无效对象数量
    SELECT owner, object_type, COUNT(*) as invalid_count
    FROM all_objects 
    WHERE status = 'INVALID'
    AND owner NOT IN ('SYS', 'SYSTEM')
    GROUP BY owner, object_type
    ORDER BY owner, object_type;

    -- 检查系统表冲突
    SELECT table_name 
    FROM all_tables 
    WHERE owner = 'SYS' 
    AND table_name IN (
        'UTL_RECOMP_SORTED',
        'UTL_RECOMP_COMPILED', 
        'UTL_RECOMP_ERRORS',
        'UTL_RECOMP_SKIP_LIST'
    );
    ```

2.  系统资源评估

    ``` sql
    -- 检查系统资源
    -- 使用 sys 用户执行
    -- 选择 oceanbase 数据库
    SELECT 
        name,
        value,
        CASE name
            WHEN 'cpu_count' THEN 
                CASE WHEN CAST(value AS SIGNED) >= 8 THEN '✅ 充足' ELSE '⚠️ 不足' END
            WHEN 'memory_limit' THEN 
                CASE 
                    WHEN UPPER(value) LIKE '%G' AND CAST(REPLACE(UPPER(value), 'G', '') AS DECIMAL) >= 8 THEN '✅ 充足'
                    ELSE '⚠️ 不足'
                END
            ELSE '🔍 检查中'
        END AS status
    FROM __ALL_VIRTUAL_SYS_PARAMETER_STAT
    WHERE name IN ('cpu_count', 'memory_limit')
    AND svr_ip = (SELECT svr_ip FROM __all_server LIMIT 1);
    ```

3.  分批编译策略

    根据对象数量和系统资源，采用分批编译策略：

    ``` sql
    -- 第一批：编译 APP_USER 模式（核心业务）
    EXEC UTL_RECOMP.RECOMP_PARALLEL(4, 'APP_USER');

    -- 检查第一批编译结果
    SELECT COUNT(*) as remaining_invalid 
    FROM all_objects 
    WHERE status = 'INVALID' AND owner = 'APP_USER';

    -- 第二批：编译 BIZ_USER 模式（业务逻辑）
    EXEC UTL_RECOMP.RECOMP_PARALLEL(4, 'BIZ_USER', 512);

    -- 第三批：编译 REPORT_USER 模式（报表相关）
    EXEC UTL_RECOMP.RECOMP_PARALLEL(4, 'REPORT_USER', 512);
    ```

4.  循环依赖处理

    ``` sql
    -- 处理循环依赖问题
    EXEC UTL_RECOMP.POPULATE_UTL_RECOMP_SKIP_LIST(512);

    -- 再次尝试编译剩余对象
    EXEC UTL_RECOMP.RECOMP_SERIAL(NULL, 512);

    -- 清理跳过列表
    EXEC UTL_RECOMP.TRUNCATE_UTL_RECOMP_SKIP_LIST(512);
    ```

5.  编译结果验证

    ``` sql
    -- 创建编译进度监控视图
    CREATE OR REPLACE VIEW compilation_progress AS
    SELECT 
        owner,
        object_type,
        COUNT(*) as total_objects,
        SUM(CASE WHEN status = 'VALID' THEN 1 ELSE 0 END) as valid_objects,
        SUM(CASE WHEN status = 'INVALID' THEN 1 ELSE 0 END) as invalid_objects,
        ROUND(100.0 * SUM(CASE WHEN status = 'VALID' THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate,
        CASE 
            WHEN ROUND(100.0 * SUM(CASE WHEN status = 'VALID' THEN 1 ELSE 0 END) / COUNT(*), 2) = 100 THEN '✅ 完成'
            WHEN ROUND(100.0 * SUM(CASE WHEN status = 'VALID' THEN 1 ELSE 0 END) / COUNT(*), 2) > 80 THEN '🔄 进行中'
            ELSE '⚠️ 需要关注'
        END as status
    FROM all_objects 
    WHERE object_type IN ('PROCEDURE', 'FUNCTION', 'PACKAGE', 'PACKAGE BODY', 'TRIGGER', 'TYPE')
    AND owner IN ('APP_USER', 'BIZ_USER', 'REPORT_USER')
    GROUP BY owner, object_type
    ORDER BY owner, object_type;

    -- 查看编译结果
    SELECT * FROM compilation_progress;
    ```

6.  错误分析和处理

    ``` sql
    -- 分析编译错误
    SELECT 
        obj#,
        error_at,
        CASE 
            WHEN UPPER(compile_err) LIKE '%TABLE%NOT%EXIST%' THEN '表不存在 - 检查表名和 schema'
            WHEN UPPER(compile_err) LIKE '%COLUMN%NOT%EXIST%' THEN '列不存在 - 检查表结构变更'
            WHEN UPPER(compile_err) LIKE '%PRIVILEGE%' THEN '权限不足 - 授予必要权限'
            WHEN UPPER(compile_err) LIKE '%COMPILATION%ERROR%' THEN '语法错误 - 检查 PL/SQL 代码'
            WHEN UPPER(compile_err) LIKE '%INVALID%' THEN '对象无效 - 检查依赖关系'
            ELSE '其他错误 - 需要详细分析'
        END as error_category,
        SUBSTR(compile_err, 1, 100) as error_text
    FROM sys.utl_recomp_errors 
    ORDER BY error_at DESC, obj#;
    ```

## 参考文档

- [UTL_RECOMP 概述](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002016390)
- [OceanBase Oracle 存储过程 DDL 执行编译结果落盘和缓存](https://www.oceanbase.com/knowledge-base/oceanbase-database-1000000001999977?back=kb)
- [UOracle 数据库离线迁移至 OceanBase 数据库 Oracle 模式的参考手册](https://www.oceanbase.com/knowledge-base/oceanbase-database-1000000002012507?back=kb)
