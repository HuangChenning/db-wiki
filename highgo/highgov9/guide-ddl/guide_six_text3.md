---
title: "修改 ALTER"
book: "数据定义DDL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_six_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-ddl
---

## 修改 ALTER

我们可以对已经创建的表进行定义或者结构上的改变，比如对表添加新的属性、修改表中某一属性的数据类型等，修改操作都通过关键字 `ALTER` 进行。

### 增加列

要增加一个列，可以使用这样的命令：

```
ALTER TABLE table_name ADD COLUMN colname datatype;
```

### 移除列

要移除一个列，可以使用这样的命令：

```
ALTER TABLE table_name DROP COLUMN colname;
```

移除列，列中的数据将会消失，涉及到该列的表约束也会被移除。

### 修改列的数据类型

要将一个列转换为一种不同的数据类型，使用如下命令：

```
ALTER TABLE table_name ALTER COLUMN colname TYPE datatype;
```

只有当列中的每一个项都能通过一个隐式造型转换为新的类型时该操作才能成功。

HGDB 将尝试把列的默认值转换为新类型，其他涉及到该列的任何约束也是一样。但是这些转换可能失败或者产生奇特的结果，因此最好在修改类型之前先删除该列上所有的约束，修改完类型后再重新加上相应修改过的约束。

### 重命名表

要修改表的名称，可以使用这样的命令：

```
ALTER TABLE table_name1 RENAME TO table_name2;
```

### 重命名列

要修改表中某列的名称，可以使用这样的命令：

```
ALTER TABLE table_name RENAME COLUMN colname1 TO colname2;
```

### 增加约束

要增加一个约束，可以使用表约束的语法。有关约束的介绍请看下一小节内容。

例如表 products 存在 product\_no、name、price 三个属性，为该表添加以下约束：

```
ALTER TABLE products ADD CHECK (name <> ''); 
ALTER TABLE products ADD CONSTRAINT UNIQUE (product_no); 
ALTER TABLE products ADD CONSTRAINT con_name UNIQUE (name);--定义约束时为约束命名
ALTER TABLE products ADD FOREIGN KEY (product_no) REFERENCES product_;
--为 products 表的 product_no 列添加外键约束，引用表product_的主键
ALTER TABLE products ADD PRIMARY KEY(product_no);
```

非空约束的添加方式与上面不同，非空约束是没有名称的，所以不能用上面的方式。

- 添加非空约束语法：
```
ALTER TABLE products ALTER COLUMN price SET NOT NULL;
```

约束增加后会立即进行检查，所以表中的数据必须在约束被增加之前就已经符合约束，否则约束将无法添加。

### 移除约束

为了移除一个约束首先需要知道它的名称，如果在创建时已经给它指定了名称，那么事情就变得很容易，否则约束的名称是由系统生成的，必须先找出这个名称。可以通过 `\d table_name` 等方法来进行查看。



- 移除约束语法：
```
ALTER TABLE table_name DROP CONSTRAINT name;
```

移除非空约束的语句与上面不同：

- 移除非空约束语法：
```
ALTER TABLE table_name ALTER COLUMN colname DROP NOT NULL;
```

例如删除 products 表中 con\_name 约束，取消 price 的非空约束：

