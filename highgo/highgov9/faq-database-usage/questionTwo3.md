---
title: "oracle兼容模式分区表语法兼容"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo3.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

```
Oracle 和 PostgreSQL 都支持表分区（Partitioning），用于管理大表、提升查询性能和简化数据维护。但在 语法、功能细节和实现机制 上存在显著差异。
```

## 语法差异详解

### 1\. Range 分区

Oracle 语法：

```
CREATE TABLE sales (
  id NUMBER,
  sale_date DATE,
  amount NUMBER
)
PARTITION BY RANGE (sale_date) (
  PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01'),
  PARTITION p2024 VALUES LESS THAN (DATE '2025-01-01'),
  PARTITION p_max VALUES LESS THAN (MAXVALUE)
);
```

PostgreSQL 语法：

```
CREATE TABLE sales (
  id INT,
  sale_date DATE,
  amount NUMERIC
) PARTITION BY RANGE (sale_date);

-- 创建分区（必须单独创建）
CREATE TABLE sales_p2023 PARTITION OF sales
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');

CREATE TABLE sales_p2024 PARTITION OF sales
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

-- PostgreSQL 不支持 MAXVALUE，但可用 open-ended range（PG 16+）
-- 或用远期日期替代
CREATE TABLE sales_p_future PARTITION OF sales
    FOR VALUES FROM ('2025-01-01') TO ('9999-12-31');
```

关键差异：

- PG必须先创建主表（partition by …）,再单独创建每个分区。
- PG使用from … to（左闭右开），Oracle用less than。
- PG无MAXVALUE，需用极大值替代。

### 2\. List 分区

Oracle：

```
CREATE TABLE orders (
  order_id NUMBER,
  region VARCHAR2(10)
)
PARTITION BY LIST (region) (
  PARTITION p_north VALUES ('BEIJING', 'TIANJIN'),
  PARTITION p_south VALUES ('GUANGZHOU', 'SHENZHEN'),
  PARTITION p_default VALUES (DEFAULT)
);
```

PostgreSQL：

```
CREATE TABLE orders (
  order_id INT,
  region TEXT
) PARTITION BY LIST (region);

CREATE TABLE orders_p_north PARTITION OF orders
    FOR VALUES IN ('BEIJING', 'TIANJIN');

CREATE TABLE orders_p_south PARTITION OF orders
    FOR VALUES IN ('GUANGZHOU', 'SHENZHEN');

-- 默认分区（PG 11+）
CREATE TABLE orders_p_default PARTITION OF orders DEFAULT;
```

几乎–对应，default分区语法一致。

### 3.hash分区

oracle:

```
CREATE TABLE users (
  id NUMBER,
  name VARCHAR2(50)
)
PARTITION BY HASH (id)
PARTITIONS 4;
```

postgresql:

```
CREATE TABLE users (
  id INT,
  name TEXT
) PARTITION BY HASH (id);

-- 必须显式定义每个分区（不能自动分）
CREATE TABLE users_p0 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE users_p1 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE users_p2 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE users_p3 PARTITION OF users
    FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

关键差异：

- Oracle可partition N自定生成。
- PG必须手动指定每个（MODULUS，REMAINDER）组合。

### 4.多级分区

Oracle：

```sql
CREATE TABLE logs (
  log_date DATE,
  level VARCHAR2(10)
)
PARTITION BY RANGE (log_date)
SUBPARTITION BY LIST (level) (
  PARTITION p2023 VALUES LESS THAN (DATE '2024-01-01')
  (SUBPARTITION p2023_info VALUES ('INFO'),
         SUBPARTITION p2023_error VALUES ('ERROR'))
);
```

postgresql（PG12+）：

```
-- 主表按 range 分区
CREATE TABLE logs (
  log_date DATE,
  level TEXT
) PARTITION BY RANGE (log_date);

-- 子分区表再按 list 分区
CREATE TABLE logs_p2023 PARTITION OF logs
    FOR VALUES FROM ('2023-01-01') TO ('2024-01-01')
    PARTITION BY LIST (level);

-- 最终叶子分区
CREATE TABLE logs_p2023_info PARTITION OF logs_p2023
    FOR VALUES IN ('INFO');
CREATE TABLE logs_p2023_error PARTITION OF logs_p2023
    FOR VALUES IN ('ERROR');
```

pg支持多级分区，但需逐层定义，结构更显式。