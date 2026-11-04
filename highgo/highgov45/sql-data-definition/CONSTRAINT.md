---
title: "约束 CONSTRAINT"
book: "数据定义"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/CONSTRAINT.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-definition
---

## 约束 CONSTRAINT

数据类型是一种限制能够存储在表中数据类别的方法，但是对于很多应用来说，它们提供的约束太粗糙。SQL 允许我们在列和表上定义约束，这使得我们能够根据自己的愿望来控制表中的数据。如果一个用户试图在一个列中保存违反一个约束的数据，一个错误会被抛出，即便是这个值来自于默认值定义，这个规则也同样适用。

一个列可以有多于一个的约束，约束的顺序没有关系，因为并不需要决定约束被检查的顺序。约束定义可以在创建表时跟在属性数据类型之后，也可以对已创建的表通过 `ALTER` 进行定义，通过 `ALTER` 定义的方法前面已经介绍，这里对创建表时定义约束进行介绍。

### 检查约束 CHECK

检查约束是最普通的约束类型，它允许我们指定一个特定列中的值必须要满足一个布尔表达式。

约束定义跟在数据类型之后的约束称为“列约束”，作为一个独立的项出现在逗号分隔的列表中的约束称为“表约束”，表约束也可以引用多个列。列约束定义和表约束定义可以以混合的顺序出现在列表中。

一个检查约束由关键字 `CHECK` 以及其后包围在圆括号中的表达式组成。

例如在创建一张 products 商品表时定义以下约束：

存储一个普通价格和一个打折后的价格，要求商品价格为正值，且打折后的价格需要低于普通价格：

```sql
CREATE TABLE products ( 
    product_no integer, 
    name text, 
    price numeric CHECK (price > 0), 
    discounted_price numeric CHECK (discounted_price > 0), 
    CHECK (price > discounted_price) 
);
```

需要注意的是，一个检查约束在其检查表达式值为真或空值时被满足，因为当任何操作数为空时大部分表达式将计算为空值，所以它们不会阻止被约束列中的空值。

### 非空约束 NOT NULL

一个非空约束总是被写成一个列约束，仅仅指定一个列中不会有空值。

例如在 products 表中定义 product\_no 和 name 字段非空：

```sql
CREATE TABLE products ( 
    product_no integer NOT NULL, 
    name text NOT NULL, 
    price numeric 
);
```

### 唯一约束 UNIQUE

唯一约束保证在一列中或者一组列中保存的数据在表中所有行间是唯一的。空值被认为是不同的。

列约束的表示方式与其他列约束表示方法相同，在数据类型后面加上唯一约束的关键字即可；也可以为一组列定义一个表级唯一约束，列名用逗号分隔。定义一组列的唯一约束指定这些列的组合值在整个表的范围内是唯一的，但其中任意一列的值不需要唯一。

为表 products 创建唯一约束的两种方式如下所示：

（1）列约束：

```sql
CREATE TABLE products ( 
    product_no integer UNIQUE, 
    name text, 
    price numeric 
);
```

（2）表约束：

```sql
CREATE TABLE products ( 
    product_no integer, 
    name text, 
    price numeric,
    UNIQUE (product_no) 
);
```

用表约束为一组列添加唯一约束：

```sql
CREATE TABLE example ( 
    a integer, 
    b integer, 
    c integer, 
    UNIQUE (a, c) 
);
```

### 主键约束 PRIMARY KEY

主键能唯一地标识表中的每一行，可以用作表的唯一标识符。主键约束规定该列或一组列的数据需要是非空且唯一的，可以理解为同时加上了非空约束和唯一约束。一个表最多只能有一个主键（可以有任意数量的唯一和非空约束，它们可以达到和主键几乎一样的功能，但只能有一个被标识为主键）。关系数据库理论要求每一个表都要有一个主键，HGDB 中并未强制要求这一点，但是最好能够遵循它。

主键可以作用在一个或者一组列。

例如将产品表的 product\_no 作为主键，为其添加主键约束：

```sql
CREATE TABLE products ( 
    product_no integer PRIMARY KEY, 
    name text,
    price numeric 
);
```

例如将 example 表的 a、c 列作为主键，为其添加主键约束：

```sql
CREATE TABLE example ( 
    a integer, 
    b integer, 
    c integer, 
    PRIMARY KEY (a, c) 
);
```

### 外键 REFERENCES

一个外键约束指定一列中的值必须匹配出现在另一个表中某些行的值。通常一个表中的 FOREIGN KEY 指向另一个表中的 UNIQUE KEY(唯一约束的键)，即维护了两个相关表之间的引用完整性。

外键约束的定义由 `REFERENES` 关键字、引用表、引用列组成，也可以不加引用列，直接引用表，此时被引用表的主键将被用作被引用列。一个表可以有超过一个的外键约束。

如下所示，创建一张 order 订单表，我们希望保证订单表中只包含真正存在的产品的订单，因此在订单表中定义一个引用前面创建的 products 产品表的外键约束：

```sql
CREATE TABLE orders ( 
    order_id integer PRIMARY KEY, 
    product_no integer REFERENCES products (product_no), 
    quantity integer 
);

--或
CREATE TABLE orders ( 
    order_id integer PRIMARY KEY, 
    product_no integer REFERENCES products, --引用products表
    quantity integer 
);
```

外键也可以约束和引用一组列，它需要被写成表约束的形式。例如创建一张 t1 表，为 b、c 列添加外键约束，引用 other\_table 表的 c1、c2 列。

```sql
CREATE TABLE t1 ( 
    a integer PRIMARY KEY, 
    b integer, 
    c integer, 
    FOREIGN KEY (b, c) REFERENCES other_table (c1, c2) 
);
```

### 排他约束 EXCLUSION

如果使用指定的运算符在指定列或表达式上比较任意两行， `EXCLUSION` 约束可以确保至少其中一个运算符比较将返回 false 或 null。

```sql
CREATE TABLE COMPANY7(
   ID integer PRIMARY KEY   NOT NULL,
   NAME           text,
   AGE            int,
   ADDRESS        char(50),
   SALARY         real,
   EXCLUDE USING gist
   (NAME WITH =,    AGE WITH <>)  
    -- 如果满足 NAME 相同、AGE 不相同则不允许插入，否则允许插入
    -- 其比较的结果是，如果整个表达式返回 true，则不允许插入，否则允许
);
```

> 这里，USING gist 是用于构建和执行的索引一种类型。

### 约束命名

我们可以在创建约束的时候通过 `CONSTRAINT` 给约束一个独立的名称，这会使得错误消息更为清晰，同时也允许我们在需要更改约束时能引用它，比如在移除一个约束时可以引用约束名。

例如在定义 `CHECK ` 约束时将它命名为 positive\_price：

```sql
CREATE TABLE products (
    product_no integer,
    name text,
    price numeric CONSTRAINT positive_price CHECK (price > 0)
);
```

### 约束开关

数据库支持约束开关功能，用户可以通过 `ENABLE` 和 `DISABLE` 来控制约束的开关，实现对约束的开启和禁用。

约束开启和关闭的语句如下所示：

```sql
ALTER TABLE table_name ENABLE CONTRAINT constraint_name;
ALTER TABLE table_name DISABLE CONTRAINT constraint_name;
```

### 移除约束

约束移除通过关键字 `ALTER` 来完成，前面已经介绍过这一部分内容。

移除约束（不包括非空约束）：

```sql
ALTER TABLE table_name DROP CONSTRAINT name;
```

移除非空约束：

```sql
ALTER TABLE table_name ALTER COLUMN colname DROP NOT NULL;
```

`ALTER` 关键字也可以用来定义约束（不包括非空约束）：

```sql
ALTER TABLE products ADD CHECK (name <> ''); 
ALTER TABLE products ADD CONSTRAINT UNIQUE (product_no); 
ALTER TABLE products ADD CONSTRAINT con_name UNIQUE (name);--定义约束时为约束命名
ALTER TABLE products ADD FOREIGN KEY (product_no) REFERENCES product_;
ALTER TABLE products ADD PRIMARY KEY(product_no);
```

用 `ALTER` 来定义非空约束：

```sql
ALTER TABLE products ALTER COLUMN price SET NOT NULL;
```