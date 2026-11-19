---
title: "PL/SQL 代码覆盖率测试最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000004293483.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# PL/SQL 代码覆盖率测试最佳实践

OceanBase 数据库提供了一个 PL 代码覆盖率系统包 `DBMS_PLSQL_CODE_COVERAGE`，您可以使用该系统包获取 PL 代码基本块级别的覆盖率信息，进一步通过增加测试用例提升覆盖率，确保 PL 代码的质量、可预测性和一致性。

## 适用场景

代码覆盖率在 PL/SQL 开发中是评估测试质量的关键指标，适用于以下场景：

- **复杂逻辑验证**：适用于包含复杂业务逻辑分支的 PL/SQL 代码。
- **异常路径测试**：需要验证异常处理分支的覆盖情况。
- **数据驱动测试**：不同数据输入可能触发不同代码路径。
- **质量保障**：通过覆盖率数据量化测试充分性，降低生产风险。

## 核心数据表结构

最终的行覆盖率信息保存在三张核心表中：

| 表名 | 用途 | 说明 |
|----|----|----|
| `DBMSPCC_RUNS` | 覆盖率运行记录 | 此表用来记录覆盖率统计每次启动的 `Run_ID` 和时间、注释等信息。 |
| `DBMSPCC_UNITS` | 测试单元信息 | 此表用来记录每次执行中每个 PL 单元的信息，`Run_ID` 和 `Object_ID` 是本次执行中 PL 单元的唯一标识符。 |
| `DBMSPCC_BLOCKS` | 代码块覆盖率详情 | 记录每个代码块的覆盖状态，包括有效行号、列号、是否被覆盖等。 |

## DBMS_PLSQL_CODE_COVERAGE 包接口

DBMS_PLSQL_CODE_COVERAGE 系统包提供以下与 Oracle 兼容的接口：

| 接口 | 功能 |
|----|----|
| start_coverage | 启动覆盖率统计，启动后会记录当前会话上 PL 的覆盖率情况 |
| stop_coverage | 关闭覆盖率统计，关闭后将结果汇总到数据统计表 |
| create_coverage_tables | 创建 DBMSPCC_RUNS、DBMSPCC_UNITS 和 DBMSPCC_BLOCKS 三张覆盖率信息统计表 |

## 操作步骤

使用 DBMS_PLSQL_CODE_COVERAGE 包进行 PL/SQL 代码覆盖率测试的基本流程如下：

1.  **环境准备**：使用 `create_coverage_tables` 接口创建覆盖率数据表，初始化测试环境。

2.  **制定标准**：根据项目需求，定义各类对象的覆盖率标准，以明确测试目标。

3.  **执行测试**：启动覆盖率统计，运行测试用例，收集覆盖率数据。

4.  **分析结果**：停止覆盖率统计，分析生成的覆盖率报告，识别未覆盖的代码路径。

5.  **优化测试**：根据分析结果，补充测试用例，提高代码覆盖率，确保代码质量。

首先，调用 `DBMS_PLSQL_CODE_COVERAGE.create_coverage_tables` 创建覆盖率统计表。然后，执行 `DBMS_PLSQL_CODE_COVERAGE.start_coverage` 启动覆盖率统计，此后在该会话中执行的所有 PL 的有效行信息和覆盖情况将被记录。测试用例执行完毕后，调用 `DBMS_PLSQL_CODE_COVERAGE.stop_coverage` 关闭覆盖率统计，所有记录的数据将汇总到统计表中。通过查询统计表分析覆盖率数据，完成 PL/SQL 代码覆盖率测试，从而提升代码的可靠性和可维护性。

## 案例：简单计算器代码覆盖率测试

假设我们有一个简单的计算器函数，需要测试其代码覆盖率。这个函数包含基本的数学运算和错误处理逻辑。

### 环境准备与测试对象创建

``` sql
-- 创建覆盖率数据表
BEGIN
    DBMS_PLSQL_CODE_COVERAGE.create_coverage_tables(FORCE_IT => TRUE);
END;
/

-- 验证表创建
SELECT table_name FROM user_tables 
WHERE table_name LIKE 'DBMSPCC%'
ORDER BY table_name;
```

``` sql
-- 创建简单计算器函数
CREATE OR REPLACE FUNCTION calculator(
    p_num1 IN NUMBER,
    p_num2 IN NUMBER,
    p_operation IN VARCHAR2
) RETURN NUMBER AS
    v_result NUMBER;
BEGIN
    -- 参数验证
    IF p_num1 IS NULL OR p_num2 IS NULL OR p_operation IS NULL THEN
        RETURN NULL;
    END IF;
    
    -- 根据操作类型计算结果
    CASE p_operation
        WHEN '+' THEN
            v_result := p_num1 + p_num2;
        WHEN '-' THEN
            v_result := p_num1 - p_num2;
        WHEN '*' THEN
            v_result := p_num1 * p_num2;
        WHEN '/' THEN
            IF p_num2 = 0 THEN
                RETURN NULL;  -- 除零错误
            ELSE
                v_result := p_num1 / p_num2;
            END IF;
        ELSE
            RETURN NULL;  -- 不支持的操作
    END CASE;
    
    RETURN v_result;
    
EXCEPTION
    WHEN OTHERS THEN
        RETURN NULL;  -- 异常处理
END;
/
```

### 测试用例执行与覆盖率收集

``` sql
-- 启动覆盖率统计
DECLARE
    l_run_id PLS_INTEGER;
    v_result NUMBER;
BEGIN
    l_run_id := DBMS_PLSQL_CODE_COVERAGE.start_coverage('计算器完整测试_' || TO_CHAR(SYSDATE, 'YYYYMMDD_HH24MI'));
    DBMS_OUTPUT.PUT_LINE('Coverage started with RUN_ID: ' || l_run_id);
    
    -- 测试用例1：加法运算
    DBMS_OUTPUT.PUT_LINE('测试用例1：加法运算');
    v_result := calculator(10, 5, '+');
    DBMS_OUTPUT.PUT_LINE('10 + 5 = ' || v_result);
    
    -- 测试用例2：减法运算
    DBMS_OUTPUT.PUT_LINE('测试用例2：减法运算');
    v_result := calculator(10, 3, '-');
    DBMS_OUTPUT.PUT_LINE('10 - 3 = ' || v_result);
    
    -- 测试用例3：乘法运算
    DBMS_OUTPUT.PUT_LINE('测试用例3：乘法运算');
    v_result := calculator(4, 6, '*');
    DBMS_OUTPUT.PUT_LINE('4 * 6 = ' || v_result);
    
    -- 测试用例4：除法运算（正常情况）
    DBMS_OUTPUT.PUT_LINE('测试用例4：除法运算（正常情况）');
    v_result := calculator(15, 3, '/');
    DBMS_OUTPUT.PUT_LINE('15 / 3 = ' || v_result);
    
    -- 测试用例5：除零错误
    DBMS_OUTPUT.PUT_LINE('测试用例5：除零错误');
    v_result := calculator(10, 0, '/');
    DBMS_OUTPUT.PUT_LINE('10 / 0 = ' || v_result);
    
    -- 测试用例6：不支持的操作
    DBMS_OUTPUT.PUT_LINE('测试用例6：不支持的操作');
    v_result := calculator(10, 5, '%');
    DBMS_OUTPUT.PUT_LINE('10 % 5 = ' || v_result);
    
    -- 测试用例7：NULL参数 - 第一个参数为NULL
    DBMS_OUTPUT.PUT_LINE('测试用例7：第一个参数为NULL');
    v_result := calculator(NULL, 5, '+');
    DBMS_OUTPUT.PUT_LINE('NULL + 5 = ' || v_result);
    
    -- 测试用例8：NULL参数 - 第二个参数为NULL
    DBMS_OUTPUT.PUT_LINE('测试用例8：第二个参数为NULL');
    v_result := calculator(10, NULL, '+');
    DBMS_OUTPUT.PUT_LINE('10 + NULL = ' || v_result);
    
    -- 测试用例9：NULL参数 - 操作符为NULL
    DBMS_OUTPUT.PUT_LINE('测试用例9：操作符为NULL');
    v_result := calculator(10, 5, NULL);
    DBMS_OUTPUT.PUT_LINE('10 NULL 5 = ' || v_result);
    
    -- 测试用例10：异常处理测试（通过无效操作触发）
    DBMS_OUTPUT.PUT_LINE('测试用例10：异常处理测试');
    v_result := calculator(999999999999999, 999999999999999, '*');
    DBMS_OUTPUT.PUT_LINE('大数乘法 = ' || v_result);
    
    -- 停止覆盖率统计
    DBMS_PLSQL_CODE_COVERAGE.stop_coverage();
    DBMS_OUTPUT.PUT_LINE('Coverage stopped');
    
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Test execution error: ' || SQLERRM);
        DBMS_PLSQL_CODE_COVERAGE.stop_coverage();
        RAISE;
END;
/
```

### 覆盖率数据分析

``` sql
-- 创建覆盖率分析视图
CREATE OR REPLACE VIEW coverage_analysis AS
SELECT 
    r.run_id,
    r.run_comment,
    r.run_timestamp,
    u.owner,
    u.name as object_name,
    u.type as object_type,
    COUNT(*) as total_lines,
    SUM(CASE WHEN d.covered = 1 THEN 1 ELSE 0 END) as covered_lines,
    ROUND(100.0 * SUM(CASE WHEN d.covered = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) as coverage_percentage
FROM DBMSPCC_RUNS r
JOIN DBMSPCC_UNITS u ON r.run_id = u.run_id
JOIN DBMSPCC_BLOCKS d ON u.run_id = d.run_id AND u.object_id = d.object_id
GROUP BY r.run_id, r.run_comment, r.run_timestamp, u.owner, u.name, u.type
ORDER BY r.run_timestamp DESC, coverage_percentage ASC;

-- 查看计算器函数的覆盖率统计
SELECT 
    object_name,
    object_type,
    total_lines,
    covered_lines,
    coverage_percentage,
    CASE 
        WHEN coverage_percentage >= 90 THEN '🟢 优秀'
        WHEN coverage_percentage >= 80 THEN '🟡 良好'
        WHEN coverage_percentage >= 70 THEN '🟠 一般'
        ELSE '🔴 需要改进'
    END as coverage_status
FROM coverage_analysis 
WHERE run_id = (SELECT MAX(run_id) FROM DBMSPCC_RUNS)
ORDER BY coverage_percentage ASC;
```

返回结果：

``` sql
+-------------+-------------+-------------+---------------+---------------------+-----------------+
| OBJECT_NAME | OBJECT_TYPE | TOTAL_LINES | COVERED_LINES | COVERAGE_PERCENTAGE | COVERAGE_STATUS |
+-------------+-------------+-------------+---------------+---------------------+-----------------+
| CALCULATOR  | FUNCTION    |          14 |            13 |               92.86 | 🟢 优秀           |
+-------------+-------------+-------------+---------------+---------------------+-----------------+
```

``` sql
-- 未覆盖代码分析
CREATE OR REPLACE VIEW uncovered_lines AS
SELECT 
    u.owner,
    u.name as object_name,
    u.type as object_type,
    d.line,
    d.col,
    'Not covered' as status,
    r.run_comment
FROM DBMSPCC_RUNS r
JOIN DBMSPCC_UNITS u ON r.run_id = u.run_id  
JOIN DBMSPCC_BLOCKS d ON u.run_id = d.run_id AND u.object_id = d.object_id
WHERE d.covered = 0
  AND r.run_id = (SELECT MAX(run_id) FROM DBMSPCC_RUNS)
ORDER BY u.owner, u.name, d.line;

-- 查看计算器函数中未覆盖的代码行
SELECT 
    object_name,
    object_type,
    line,
    col,
    '需要补充测试用例' as action_required
FROM uncovered_lines
ORDER BY object_name, line;
```

返回结果：

``` sql
+-------------+-------------+------+------+--------------------------+
| OBJECT_NAME | OBJECT_TYPE | LINE | COL  | ACTION_REQUIRED          |
+-------------+-------------+------+------+--------------------------+
| CALCULATOR  | FUNCTION    |   35 |    9 | 需要补充测试用例         |
+-------------+-------------+------+------+--------------------------+
```

### 生成覆盖率报告

``` sql
-- 生成简单的覆盖率报告
CREATE OR REPLACE PROCEDURE generate_simple_report IS
    l_run_id NUMBER;
    l_total_lines NUMBER;
    l_covered_lines NUMBER;
    l_coverage_percentage NUMBER;
BEGIN
    SELECT MAX(run_id) INTO l_run_id FROM DBMSPCC_RUNS;
    
    SELECT total_lines, covered_lines, coverage_percentage
    INTO l_total_lines, l_covered_lines, l_coverage_percentage
    FROM coverage_analysis
    WHERE run_id = l_run_id;
    
    DBMS_OUTPUT.PUT_LINE('==========================================');
    DBMS_OUTPUT.PUT_LINE('        计算器函数覆盖率报告');
    DBMS_OUTPUT.PUT_LINE('==========================================');
    DBMS_OUTPUT.PUT_LINE('测试运行ID: ' || l_run_id);
    DBMS_OUTPUT.PUT_LINE('测试时间: ' || TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS'));
    DBMS_OUTPUT.PUT_LINE('------------------------------------------');
    DBMS_OUTPUT.PUT_LINE('总体统计:');
    DBMS_OUTPUT.PUT_LINE('  代码总行数: ' || l_total_lines);
    DBMS_OUTPUT.PUT_LINE('  覆盖行数: ' || l_covered_lines);
    DBMS_OUTPUT.PUT_LINE('  覆盖率: ' || l_coverage_percentage || '%');
    DBMS_OUTPUT.PUT_LINE('------------------------------------------');
    
    IF l_coverage_percentage >= 90 THEN
        DBMS_OUTPUT.PUT_LINE('🟢 代码质量优秀，测试充分');
    ELSIF l_coverage_percentage >= 80 THEN
        DBMS_OUTPUT.PUT_LINE('🟡 代码质量良好，建议补充测试');
    ELSE
        DBMS_OUTPUT.PUT_LINE('🔴 代码质量需要改进，请补充测试用例');
    END IF;
    
    DBMS_OUTPUT.PUT_LINE('==========================================');
END;
/

-- 开启服务器输出
SET SERVEROUTPUT ON;

-- 生成报告
BEGIN
    generate_simple_report();
END;
/

-- 调用报告生成过程
CALL generate_simple_report();
```

返回结果：

``` sql
==========================================
        计算器函数覆盖率报告
==========================================
测试运行ID: 3
测试时间: 2025-09-25 17:38:33
------------------------------------------
总体统计:
  代码总行数: 14
  覆盖行数: 13
  覆盖率: 92.86%
------------------------------------------
🟢 代码质量优秀，测试充分
==========================================
```

在这个简单的计算器案例中，我们展示了 `DBMS_PLSQL_CODE_COVERAGE` 的完整用法：

1.  **基本运算测试**：包括加法、减法、乘法和除法运算。
2.  **边界条件测试**：处理除零错误和不支持的操作符。
3.  **参数验证测试**：测试各种 NULL 参数组合。
4.  **异常处理测试**：通过大数运算测试异常处理路径。
5.  **全面覆盖**：通过 10 个测试用例覆盖所有代码路径。
6.  **识别测试盲点**：通过覆盖率分析，找出未测试的代码路径。
7.  **指导测试改进**：根据覆盖率数据，针对性地增加测试用例。
8.  **量化质量指标**：通过具体数据评估代码测试的充分性。

在实际项目中，建议您将代码覆盖率作为代码质量的重要指标。对于关键业务逻辑，应设置更高的覆盖率要求。

## 参考文档

- [DBMS_PLSQL_CODE_COVERAGE 包](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004132047)
