---
title: "数组兼容"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo6.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

在 Oracle PL/SQL 中，自定义数组（VARRAY、Nested Table） 是常用的数据结构。然而，瀚高没有完全等价的 PL/SQL 数组类型，但可通过 PL/pgSQL 的数组（Array）和复合类型（Composite Type） 实现类似功能。

## 一、Oracle PL/SQL 数组类型 vs 瀚高 对应方案

| Oracle 类型 | 特点 | PostgreSQL 等效方案 |
| --- | --- | --- |
| VARRAY （变长数组，有最大长度） | 有序、连续、固定上限 | PG 数组（type\[\]） + 检查约束 |
| Nested Table （嵌套表，无上限，可存储于表中） | 可作为列存入表，支持 SQL 操作 | PG 数组 或 UNNEST + 临时表 |

## 二、详细案例对比

案例 1：VARRAY（固定上限数组） → PG 数组  
Oracle (PL/SQL)

```sql
DECLARE
  TYPE num_array IS VARRAY(5) OF NUMBER;
  nums num_array := num_array(10, 20, 30);
BEGIN
  FOR i IN 1..nums.COUNT LOOP
    DBMS_OUTPUT.PUT_LINE('Value: ' || nums(i));
  END LOOP;
END;
```

#### PostgreSQL (PL/pgSQL) —— 推荐方式

```sql
DO $$
DECLARE
  nums INTEGER[] := ARRAY[10, 20, 30];  -- 自动推断为 integer[]
  i INT;
BEGIN
  FOR i IN 1..array_length(nums, 1) LOOP
    RAISE NOTICE 'Value: %', nums[i];
  END LOOP;
END $$;
```

说明：  
● PG 数组从 1 开始索引（与 Oracle 一致）  
● ARRAY\[…\] 构造数组  
● array\_length(arr, dim) 获取长度（dim=1 表示第一维）

#### 模拟 VARRAY 上限（可选）

```sql
-- 创建带检查约束的域（Domain）限制数组长度
CREATE DOMAIN limited_int_array AS INTEGER[]
CHECK (array_length(VALUE, 1) <= 5);

DO $$
DECLARE
  nums limited_int_array := ARRAY[10, 20, 30];
BEGIN
  RAISE NOTICE 'Array: %', nums;
END $$;
```

### 案例 2：Nested Table（嵌套表） → PG 数组 或 UNNEST

oracle

```sql
DECLARE
  TYPE emp_list IS TABLE OF VARCHAR2(100);
  employees emp_list := emp_list('Alice', 'Bob', 'Charlie');
BEGIN
  FOR i IN employees.FIRST..employees.LAST LOOP
    DBMS_OUTPUT.PUT_LINE(employees(i));
  END LOOP;
END;
```

#### PostgreSQL 方式 1：直接用数组

```sql
DO $$
DECLARE
  employees TEXT[] := ARRAY['Alice', 'Bob', 'Charlie'];
  i INT;
BEGIN
  FOR i IN 1..array_length(employees, 1) LOOP ...
    RAISE NOTICE '%', employees[i];
  END LOOP;
END $$;
```

#### PostgreSQL 方式 2：将数组展开为行（类似 TABLE() 函数）

```sql
-- 模拟 Oracle: SELECT * FROM TABLE(employees)
SELECT unnest(ARRAY['Alice', 'Bob', 'Charlie']) AS name;
```

输出：

```sql
name
--------
 Alice
 Bob
 Charlie
```

**优势** ： UNNEST() 可直接在 SQL 中使用，无需 PL/pgSQL

## 三、高级场景：数组作为表列存储

### Oracle（Nested Table 列）

```sql
CREATE TYPE tag_list AS TABLE OF VARCHAR2(50);
CREATE TABLE articles (
  id NUMBER,
  title VARCHAR2(100),
  tags tag_list
) NESTED TABLE tags STORE AS tags_table;
```

### PostgreSQL 等效

```sql
-- 直接使用数组类型
CREATE TABLE articles (
  id SERIAL,
  title TEXT,
  tags TEXT[]  -- 数组列
);

-- 插入数据
INSERT INTO articles (title, tags)
VALUES ('PG Guide', ARRAY['database', 'sql', 'tutorial']);

-- 查询包含某标签的文章
SELECT * FROM articles WHERE 'sql' = ANY(tags);

-- 展开标签（一行变多行）
SELECT id, title, unnest(tags) AS tag FROM articles;
```

## 四、关键差异总结

| 特性 | **Oracle PL/SQL** | PostgreSQL |
| --- | --- | --- |
| **数组索引起点** | 1（VARRAY/Nested Table） | 1（默认） |
| **数组作为列** | Nested Table / VARRAY | type\[\] （原生支持） |
| **动态扩容** | Nested Table 可 EXTEND | PG 数组自动扩容 |
| **遍历方式** | FOR i IN 1..arr.COUNT | FOR i IN 1..array\_length(arr,1)或FOREACH |
| **SQL 中展开** | TABLE(arr) | UNNEST(arr) |

## 五、迁移建议

1. VARRAY / Nested Table → 直接替换为 PG 数组（type\[\]）
2. 避免模拟“稀疏整数索引”：如果业务需要，用 (index, value) 临时表更清晰
3. 利用 UNNEST()：替代 Oracle 的 TABLE() 函数，实现数组转行