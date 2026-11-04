---
title: "DATE_SUB报错问题"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo16.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

```markdown
# 瀚高数据库 V9 MySQL 兼容模式下的日期函数适配方案

## 一、问题背景

\`date_sub\`

### 问题示例

执行以下 MySQL 原生 SQL 时：
\`\`\`sql
SELECT NOW(INTERVAL 90 DAY);
```

报错信息：

```
SQL 错 [24708] [HY000]: syntax error at or near "90"
```

### 根本原因

瀚高数据库 V9 的 MySQL 兼容模式未能完全识别 MySQL 的 `date_sub` 函数及其简写语法 `NOW(INTERVAL ...)` ，导致解析器在遇到 `INTERVAL` 关键字后的数字时出现语法错误。

---

## 二、解决方案

通过创建自定义函数 `ivymy.date_sub` 来模拟 MySQL 的 `date_sub` 行为，提供日期时间减去时间间隔的功能。

### 2.1 函数设计思路

- **函数名称** ： `ivymy.date_sub` （保持与 MySQL 命名习惯一致）
- **功能** ：从指定的日期或日期时间值中减去一个时间间隔
- **重载策略** ：根据第一个参数的类型提供不同的函数实现（支持 `datetime` 和 `date` 类型）
- **性能优化** ：标记为 `parallel safe` 和 `immutable` ，便于查询优化器进行优化

### 2.2 函数实现代码

#### 实现一：处理 datetime 类型

```sql
-- 删除已存在的同名函数（避免冲突）
drop function if exists date_sub(datetime, interval);

-- 创建 datetime 版本的 date_sub 函数
create or replace function ivymy.date_sub(datetime, interval) 
returns datetime 
language sql 
parallel safe 
immutable as 
$$ 
    select ($1::pg_catalog.timestamp - $2); 
$$;
```

**说明** ：

- 将第一个参数显式转换为 `pg_catalog.timestamp` 类型
- 直接使用 PostgreSQL 原生的时间戳减法运算（返回 `interval` 类型，但 PostgreSQL 会自动处理为 `datetime` ）

#### 实现二：处理 date 类型

```sql
-- 删除已存在的同名函数（避免冲突）
drop function if exists date_sub(date, interval);

-- 创建 date 版本的 date_sub 函数
create or replace function ivymy.date_sub(date, interval) 
returns date 
language sql 
parallel safe 
immutable as 
$$ 
    select ($1::pg_catalog.date - $2); 
$$;
```

**说明** ：

- 将第一个参数显式转换为 `pg_catalog.date` 类型
- 日期减去时间间隔后返回 `date` 类型

---

## 三、使用指南

### 3.1 基本用法示例

```sql
-- 从当前日期时间减去 90 天
SELECT ivymy.date_sub(NOW(), INTERVAL '90 DAY');

-- 从指定日期减去 1 个月
SELECT ivymy.date_sub('2024-01-01', INTERVAL '1 MONTH');

-- 从当前日期减去 7 天
SELECT ivymy.date_sub(CURRENT_DATE, INTERVAL '7 DAY');

-- 复杂的时间间隔运算（小时、分钟）
SELECT ivymy.date_sub(NOW(), INTERVAL '2 HOURS 30 MINUTES');
```

### 3.2 与其他函数配合使用

```sql
-- 查询 90 天前的记录
SELECT * 
FROM orders 
WHERE order_date > ivymy.date_sub(NOW(), INTERVAL '90 DAY');

-- 计算上个月的同期日期
SELECT ivymy.date_sub(CURRENT_DATE, INTERVAL '1 MONTH');
```

---

## 四、注意事项

### 4.1 模式要求

- 函数创建在 `ivymy` 模式下，执行前需确认该模式已存在
- 如模式不存在，可通过以下 SQL 创建：
	```sql
	CREATE SCHEMA IF NOT EXISTS ivymy;
	```

### 4.2 权限要求

- 需要具有 `ivymy` 模式的 `CREATE` 权限
- 需要具有函数的 `EXECUTE` 权限（通常模式所有者或超级用户拥有）

### 4.3 兼容性说明

- 该实现适用于 **瀚高数据库 V9 MySQL 兼容模式**
- 函数名与 MySQL 原生 `date_sub` 保持一致，但需要显式指定模式 `ivymy.`
- 如需全局使用，可考虑设置 `search_path` 包含 `ivymy` 模式

### 4.4 性能特性

- `parallel safe` ：表示函数可在并行查询中安全使用
- `immutable` ：表示函数结果仅依赖参数，不会因数据库状态变化而改变，便于优化器缓存结果

---

## 五、替代方案对比

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| **自定义函数 `ivymy.date_sub`** | 语法接近 MySQL，易于迁移；支持多种时间间隔单位 | 需要显式指定模式或调整 search\_path |
| **直接使用 PostgreSQL 原生语法** | 无需额外创建函数，性能最优 | 语法与 MySQL 差异大，增加迁移成本 |
| **应用层处理** | 数据库层无需改动 | 增加应用层复杂度，无法利用数据库索引优化 |

### 原生 PostgreSQL 等价写法参考

```sql
-- MySQL 风格
SELECT ivymy.date_sub(NOW(), INTERVAL '90 DAY');

-- PostgreSQL 原生风格
SELECT NOW() - INTERVAL '90 DAY';
SELECT CURRENT_TIMESTAMP - INTERVAL '90 DAY';
```

---

## 六、验证测试

执行以下 SQL 验证函数是否正确工作：

```sql
-- 测试 datetime 版本
SELECT ivymy.date_sub(NOW(), INTERVAL '90 DAY') AS result_datetime;

-- 测试 date 版本
SELECT ivymy.date_sub(CURRENT_DATE, INTERVAL '90 DAY') AS result_date;

-- 验证结果是否合理（应为 90 天前）
SELECT 
    NOW() AS current_time,
    ivymy.date_sub(NOW(), INTERVAL '90 DAY') AS ninety_days_ago;
```

预期结果：函数返回当前时间减去 90 天后的正确日期时间值。

---

## 七、总结

通过创建 `ivymy.date_sub` 自定义函数，成功解决了瀚高数据库 V9 MySQL 兼容模式下 `date_sub` 函数及 `INTERVAL` 语法不被支持的兼容性问题。该方案：

保持了与 MySQL 相近的语法风格  
支持 datetime 和 date 两种常用类型  
具备良好的性能特性（parallel safe + immutable）  
便于存量 MySQL 应用的平滑迁移

建议在数据库迁移或应用适配过程中，统一使用该函数处理日期时间减法运算，确保兼容性和代码可维护性。  
\`\`\`