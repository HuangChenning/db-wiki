---
title: "数据操纵"
book: "SQL语言参考手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceFour6.html"
tags:
  - highgo
  - highgo-v9
  - sql-language-reference
---

## 数据操纵

前面的章节讨论了如何创建表和其他结构来保存你的数据。现在是时候给表填充数据了。本章涉及如何插入、更新和删除表数据。在接下来的一章将最终解释如何把你丢失已久的数据从数据库中抽取出来。

## 插入数据

当一个表被创建后，它不包含数据。在数据库可以有点用之前要做的第一件事就是向里面插入数据。数据在概念上是以每次一行地方式被插入的。你当然可以每次插入多行，但是却没有办法一次插入少于一行的数据。即使你只知道几个列的值，那么你也必须创建一个完整的行。

要创建一个新行，使用INSERT命令。这条命令要求提供表的名字和其中列的值。例如，考虑第 4 章中的产品表：

CREATE TABLE products (

product\_no integer,

name text,

price numeric

);

一个插入一行的命令将是：

INSERT INTO products VALUES (1, 'Cheese', 9.99);

数据的值是按照这些列在表中出现的顺序列出的，并且用逗号分隔。通常，数据的值是文字（常量），但也允许使用标量表达式。

上面的语法的缺点是你必须知道表中列的顺序。要避免这个问题，你也可以显式地列出列。

例如，下面的两条命令都有和上文那条命令一样的效果：

INSERT INTO products (product\_no, name, price) VALUES (1, 'Cheese', 9.99);

INSERT INTO products (name, price, product\_no) VALUES ('Cheese', 9.99, 1);

许多用户认为明确列出列的名字是个好习惯。

如果你没有获得所有列的值，那么你可以省略其中的一些。在这种情况下，这些列将被填充为它们的缺省值。例如：

INSERT INTO products (product\_no, name) VALUES (1, 'Cheese');

INSERT INTO products VALUES (1, 'Cheese');

第二种形式是瀚高数据库的一个扩展。它从使用给出的值从左开始填充列，有多少个给出的列值就填充多少个列，其他列的将使用缺省值。

为了保持清晰，你也可以显式地要求缺省值，用于单个的列或者用于整个行：

INSERT INTO products (product\_no, name, price) VALUES (1, 'Cheese', DEFAULT);

INSERT INTO products DEFAULT VALUES;

你可以在一个命令中插入多行：

INSERT INTO products (product\_no, name, price) VALUES

(1, 'Cheese', 9.99),

(2, 'Bread', 1.99),

(3, 'Milk', 2.99);

也可以插入查询的结果（可能没有行、一行或多行）：

INSERT INTO products (product\_no, name, price)

SELECT product\_no, name, price FROM new\_products

WHERE release\_date = 'today';

这提供了用于计算要插入的行的SQL查询机制（第 5 章）的全部功能。

| 提示： |
| --- |
| 在一次性插入大量数据时，考虑使用COPY命令。它不如INSERT命令那么灵活,但是更高效。 参考第 14.4 节获取更多有关批量装载性能的信息。 |

## 更新数据

修改已经存储在数据库中的数据的行为叫做更新。你可以更新单个行，也可以更新表中所有的行，还可以更新其中的一部分行。 我们可以独立地更新每个列，而其他的列则不受影响。

要更新现有的行，使用UPDATE命令。这需要提供三部分信息：

1\. 表的名字和要更新的列名

2\. 列的新值

3\. 要更新的是哪（些）行

我们在第 5 章里说过，SQL 通常并不为行提供唯一标识符。因此我们无法总是直接指定需要更新哪一行。但是，我们可以通过指定一个被更新的行必须满足的条件。只有在表里面存在主键的时候（不管你声明它还是不声明它），我们才能可靠地通过选择一个匹配主键的条件来指定一个独立的行。图形化的数据库访问工具就靠这允许我们独立地更新某些行。

例如，这条命令把所有价格为5的产品的价格更新为10：

UPDATE products SET price = 10 WHERE price = 5;

这样做可能导致零行、一行或者更多行被更新。如果我们试图做一个不匹配任何行的更新，那也不算错误。

让我们仔细看看这个命令。首先是关键字UPDATE， 然后跟着表名字。和平常一样，表名字也可以是用模式限定的，否则会从路径中查找它。然后是关键字SET， 后面跟着列名、一个等号以及新的列值。新的列值可以是任意标量表达式，而不仅仅是常量。例如，如果你想把所有产品的价格提高 10%，你可以用：

UPDATE products SET price = price \* 1.10;

如你所见，用于新值的表达式也可以引用行中现有的值。我们还忽略了WHERE子句。如果我们忽略了这个子句， 那么就意味着表中的所有行都要被更新。如果出现了WHERE子句， 那么只有匹配它后面的条件的行被更新。请注意在SET子句中的等号是一个赋值， 而在WHERE子句中的等号是比较，不过这样并不会导致任何歧义。当然WHERE条件不一定非得是等值测试。许多其他操作符也都可以使用（参阅第 8 章）。但是表达式必须得出一个布尔结果。

你还可以在一个UPDATE命令中更新更多的列， 方法是在SET子句中列出更多赋值。例如：

UPDATE mytable SET a = 5, b = 3, c = 1 WHERE a > 0;

## 删除数据

到目前为止我们已经解释了如何向表中增加数据以及如何改变数据。剩下的是讨论如何删除不再需要的数据。和前面增加数据一样，你也只能从表中整行整行地删除数据。在前面的一节里我们解释了 SQL 不提供直接访问单个行的方法。因此，删除行只能是通过指定被删除行必须匹配的条件进行。如果你在表上有一个主键，那么你可以指定准确的行。但是你也可以删除匹配条件的一组行，或者你可以一次从表中删除所有的行。

可以使用DELETE命令删除行，它的语法和UPDATE命令非常类似。例如，要从产品表中删除所有价格为 10 的产品，使用：

DELETE FROM products WHERE price = 10;

如果你只是写：

DELETE FROM products;

那么表中所有行都会被删除！程序员一定要注意。

## 从修改的行中返回数据

有时在修改行的操作过程中获取数据很有用。INSERT、 UPDATE和DELETE命令都有一个支持这个的可选的 RETURNING子句。使用RETURNING 可以避免执行额外的数据库查询来收集数据，并且在否则难以可靠地识别修改的行时尤其有用。

所允许的RETURNING子句的内容与SELECT命令的输出列表相同 （请参阅第 5.3 节）。它可以包含命令的目标表的列名， 或者包含使用这些列的值表达式。一个常见的简写是RETURNING \*， 它按顺序选择目标表的所有列。

在INSERT中，可用于RETURNING的数据是插入的行。这在琐碎的插入中并不是很有用，因为它只会重复客户端提供的数据。 但依赖于计算出的默认值时可以非常方便。例如，当使用 serial列来提供唯一标识符时， RETURNING可以返回分配给新行的ID：

CREATE TABLE users (firstname text, lastname text, id serial primary key);

INSERT INTO users (firstname, lastname) VALUES ('Joe', 'Cool') RETURNING id;

RETURNING子句对于INSERT... SELECT也非常有用。

在UPDATE中，可用于RETURNING的数据是被修改行的新内容。 例如：

UPDATE products SET price = price \* 1.10

WHERE price <= 99.99

RETURNING name, price AS new\_price;

在DELETE中，可用于RETURNING的数据是删除行的内容。例如：

DELETE FROM products

WHERE obsoletion\_date = 'today'

RETURNING \*;

如果目标表上有触发器，可用于RETURNING 的数据是被触发器修改的行。因此，检查由触发器计算的列是RETURNING的另一个常见用例。