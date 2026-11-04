---
title: "创建 CREATE"
book: "数据定义"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/CREATE.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-definition
---

## 创建 CREATE

数据库、用户、表、视图、模式、索引等对象的创建均通过 `CREATE` 关键字来实现。

### 创建数据库

数据库用命令 `CREATE DATABASE` 创建：

```sql
CREATE DATABASE name;
```

当前角色自动成为该新数据库的拥有者。

### 创建用户

要创建一个角色，可以使用 `CREATE ROLE` 命令：

`CREATE USER` 和 `CREATE ROLE` 等效，除了 `CREATE USER` 默认有 LOGIN，而 `CREATE ROLE ` 没有。具有 LOGIN 属性的角色才能连接到数据库。用户密码要求长度至少为8位，必须含有大小写字母、数字以及 `!@#$%^&*()` 特殊字符，不能含有当前用户名字符串，不能含有瀚高数据库保留字和关键字，不能使用最近五个使用过的密码。

```sql
CREATE ROLE name LOGIN password 'mima';
CREATE USER name password 'mima';
```

### 创建表

要创建一张表，可以使用 `CREATE TABLE` 命令：

```sql
CREATE TABLE table_name(
    colname1 datatype,
    colname2 datatype,
    ......
    colnameN datatype);
```

colname 为列名。

例如创建一个 person 表：

```sql
CREATE TABLE person(
    id int,
    name text,
    age int,
    address varchar
);
```

创建完成后，可以使用 `\d tablename` 来查看表格创建情况：

```sql
\d person
                 数据表 "public.person"
  栏位   |       类型        | 校对规则 | 可空的 | 预设 
---------+-------------------+----------+--------+------
 id      | integer           |          |        | 
 name    | text              |          |        | 
 age     | integer           |          |        | 
 address | character varying |          |        |
```

### 创建视图

视图是一张虚拟的表，只有定义，不存在数据，行和列的数据来自查询所引用的表，并且在引用视图时动态生成。可以为组合列表创建一个视图，在使用时像使用一个普通表一样来使用。要创建视图，可以使用 `CREATE VIEW` 命令。

例如为 products 产品表和 orders 订单表创建以下视图：

```sql
CREATE VIEW p_o_view AS
SELECT products.product_no, name, price, order_id, quantity
FROM products, orders
WHERE products.product_no = orders.product_no;

SELECT* FROM p_o_view;
```

查询结果如下：

```sql
product_no | name | price | order_id | quantity 
------------+------+-------+----------+----------
          1 | a    |     1 |        1 |        1
(1 行记录)
```

在 `SELECT` 部分，由于 products 表和 orders 表都出现了 product\_no 属性，即便这两个属性表示的意义相同，在查询时这个属性是不明确的，需要加上表名来显式说明， `WHERE` 里面的连接条件表达的就是这个意思。

### 创建模式

HGDB 中模式可以看作是表的集合，一个模式可以包含视图、索引、数据类型、函数和操作符等。相同的对象名称可以被用于不同的模式中而不会出现冲突，例如 schema1 和 myschema 都可以包含名为 mytable 的表。模式不能嵌套。要创建一个模式，可以使用 `CREATE SCHEMA` 命令：

创建名为 myschema 的模式：

```sql
CREATE SCHEMA myschema;
```

如果我们希望创建一个限定用户的模式，可以通过 `AUTHORIZATION` 来进行设置：

```sql
CREATE SCHEMA myschema AUTHORIZATION user_name;
```

在一个模式中创建或访问对象，需要使用由模式名和表名构成的限定名，模式名和表名之间以点号分隔，例如上面提到的 mytable 表，需要写成 schema1.mytable 或者 myschema.mytable。

在日常使用中，不指定模式的情况下，我们创建的表都会放在一个叫 public 的公共模式下。对于公共模式 public，默认所有用户都拥有在 public 模式上 `CREATE` 和 `USAGE` 权限。

### 创建索引

索引是提高数据库性能的常用方法，如果我们经常查询一张大表中的一小部分行，可以使用 `CREATE INDEX` 在表的某一列或者几列上创建一个索引，例如查询全国所有城市中的省会城市。

HGDB 会自动为定义了一个唯一约束或主键的表创建一个唯一索引，唯一索引中不允许多个表行具有相同的索引值。在唯一索引中，空值被视为不相同。

创建索引的语句如下：

单列索引：

```sql
CREATE INDEX index_name ON table_name (colname);
```

多列索引：

```sql
CREATE INDEX index_name ON table_name (colname1, colname2);
```

唯一索引：

```sql
CREATE UNIQUE INDEX index_name ON table_name (colname);
```

用上面的语句为 cities 表创建索引：

创建单列索引查询省会城市：

```sql
CREATE INDEX city_index_capital ON cities（capital);
```

创建多列索引查询省会城市及所在省：

```sql
CREATE INDEX city_index_capital_province ON cities(capital,province)
```

单列索引和多列索引的组合可以提供更多的组合，假设一个查询有时只涉及列 x，有时只涉及列 y，有时还会同时涉及到两列，可以选择在 x 和 y 上创建两个独立索引然后依赖索引组合来处理同时涉及到两列的查询。创建一个多列索引和一个 y 上的独立索引的组合将会工作得更好，多列索引可以用于那些只涉及到 x 的查询。多列索引应该较少地使用，在绝大多数情况下，单列索引就足够且能节约时间和空间。

索引列也可以是一个函数或者标量表达式，这种索引称为表达式索引。例如可以对大小写不敏感的内容创建一个 lower 函数结果的索引。

```sql
CREATE INDEX cities_lower_index ON cities(LOWER(province));
```