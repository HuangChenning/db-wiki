---
title: "层次查询列"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle18.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 层次查询

## 说明

层次查询是一种强大的查询功能，它允许用户按照数据之间的层级关系来检索和展示信息。在现实世界中，很多数据都存在层次结构，比如组织架构（部门和员工）、产品分类（类别和子类别）、多级菜单等。通过层次查询，可以方便地从数据库中提取出这种层次化的数据，并以树形结构或其他合适的格式呈现出来，从而更直观地展现数据之间的层级关系，帮助用户更好地理解和分析数据。例如，可以查询出一个公司从最高层领导到各级下属员工的完整组织架构，或者从顶级产品类别到具体的子产品类别等。

层次查询支持兼容Oracle层次查询中的CONNECT BY与START WITH语句。其中：

- START WITH指定根行，即查询的起始点。
- CONNECT BY后指定父子关系，即迭代条件，用于定义层次结构。

1、循环处理

- NOCYCLE关键字用于表明忽略循环。
- 如果递归过程中发现存在循环，即存在节点既是祖先节点又是子节点的情况：
	- 如果不指定NOCYCLE关键字，则递归到循环时会报错。
		- 如果指定NOCYCLE，则不会继续往下递归。

2、同层节点排序

层次查询支持在ORDER BY后面加SIBLINGS指定层次查询同层节点的顺序。目前仅实现可以在 ORDER BY 之间加SIBLINGS关键字。

3、层次查询的伪列

层次查询的伪列仅能在层次查询中使用，包括以下三个：

- CONNECT\_BY\_ISCYCLE 伪列：如果当前行有一个子项，而这个子项也是当前行的祖先，则 CONNECT\_BY\_ISCYCLE 返回1，表示存在循环；否则返回 0。
- CONNECT\_BY\_ISLEAF伪列：如果当前的行是整个树的叶子节点，返回 1，否则返回 0。这个信息可以指示当前行是否还可以继续扩展。
- LEVEL伪列：LEVEL表示当前行的层级，从1开始。根行的LEVEL为1，其子节点为2，子子节点为3，以此类推。

4、操作符支持

- PRIOR操作符：PRIOR是一元运算符，它引用当前行的父行来计算紧随其后的表达式，经常出现在等式运算符比较列中。它可以位于运算符的任意一侧。
- CONNECT\_BY\_ROOT 操作符：该操作符仅能在层次查询中使用。当你使用该操作符作用于一个列时，返回的是根行的数据。

5、SYS\_CONNECT\_BY\_PATH函数

层次查询还支持SYS\_CONNECT\_BY\_PATH函数，该函数只能在层次查询中使用。它返回从根行到本行指定列的路径，路径分隔符使用char来指定，返回值是 varchar2类型。

## 示例

CREATE TABLE employees (

employee\_id NUMBER(6),

last\_name VARCHAR2(25),

manager\_id NUMBER(6)

);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (100, ‘King’, NULL);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (101, ‘Kochhar’, 100);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (102, ‘De Haan’, 100);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (103, ‘Hunold’, 102);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (104, ‘Ernst’, 103);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (105, ‘Austin’, 103);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (106, ‘Pataballa’, 103);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (107, ‘Lorentz’, 103);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (108, ‘Greenberg’, 101);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (109, ‘Faviet’, 108);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (110, ‘Chen’, 108);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (111, ‘Sciarra’, 108);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (112, ‘Urman’, 108);

INSERT INTO employees (employee\_id, last\_name, manager\_id) VALUES (113, ‘Popp’, 108);

示例查询

1、 使用 LEVEL 伪列

查询每个员工及其层级深度：

SELECT employee\_id, last\_name, manager\_id, LEVEL, SYS\_CONNECT\_BY\_PATH(last\_name, ‘/‘) “Path”

FROM employees

START WITH manager\_id IS NULL

CONNECT BY PRIOR employee\_id = manager\_id;

2、 使用 CONNECT\_BY\_ISLEAF 伪列

查询每个员工是否是叶子节点：

SELECT employee\_id, last\_name, manager\_id, LEVEL, CONNECT\_BY\_ISLEAF AS “IsLeaf”

FROM employees

START WITH manager\_id IS NULL

CONNECT BY PRIOR employee\_id = manager\_id;