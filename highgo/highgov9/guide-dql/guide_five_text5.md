---
title: "LIMIT 和 OFFSET"
book: "数据查询DQL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_five_text5.html"
tags:
  - highgo
  - highgo-v9
  - guide-dql
---

## LIMIT 和 OFFSET

LIMIT 和 OFFSET 允许你只检索查询产生的行的一部分。如果给出了一个 LIMIT 限制计数，那么会返回数量不超过该限制的行，LIMIT ALL 的效果和省略 LIMIT 子句一样，就像是 LIMIT 带有 NULL 参数一样，返回全部查询结果。OFFSET 说明在开始返回行之前忽略多少行，OFFSET 0 的效果和省略 OFFSET 子句是一样的，即不忽略任何行。如果 OFFSET 和 LIMIT 都出现了，那么在返回 LIMIT 个行之前要先忽略 OFFSET 个行。

在使用 LIMIT 时，用一个 ORDER BY 子句把结果行约束成一个唯一的顺序是很重要的，否则你将拿到一个不确定的查询结果。

### 基本语法

```
SELECT column1, column2, ...
FROM table_name
[WHERE condition]
[ORDER BY column1, column2, ...]
LIMIT n
OFFSET m;
```

### 参数说明

- \*\* `LIMIT n` \*\*：限制返回的行数为 `n` 。
- \*\* `OFFSET m` \*\*：跳过前 `m` 行数据，从第 `m+1` 行开始返回。

下面是 LIMIT 和 OFFSET 的例子：

### 分页查询

```
-- 第 1 页：跳过 0 行，取 10 行
SELECT * FROM users LIMIT 10 OFFSET 0;

-- 第 2 页：跳过 10 行，取 10 行
SELECT * FROM users LIMIT 10 OFFSET 10;

-- 第 n 页：跳过 (n-1)*10 行，取 10 行
SELECT * FROM users LIMIT 10 OFFSET ((n-1) * 10);
```

### 结合 order by 使用

```
-- 按 ID 降序排列后分页
SELECT * FROM users
ORDER BY id DESC
LIMIT 10 OFFSET 20;

-- 返回前n条
-- 返回年龄最大的 5 个用户
SELECT * FROM users
ORDER BY age DESC
LIMIT 5;

-- 跳过前n条数据
-- 跳过前 10 条，返回剩余的所有数据
SELECT * FROM users OFFSET 10;
```