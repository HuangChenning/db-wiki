---
title: "9、禁用表的触发器以及外键约束"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/trigger_disabled.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 禁用表的触发器以及外键约束

ALTER TABLE name DISABLE/ENABLE TRIGGER \[ trigger\_name | ALL | USER \]

trigger\_name  
要禁用或启用的单个触发器的名称。

ALL  
禁用或启用属于该表的所有触发器。（如果有任何触发器是内部生成的约束触发器，例如用于实现外键约束或可延迟的唯一性和排他约束的触发器则需要超级用户特权。）

USER  
禁用或启用属于该表的所有触发器，但内部生成的约束触发器（例如用于实现外键约束或可延迟的唯一性和排他约束的触发器）除外。

例子：

```
highgo=# CREATE TABLE tbl_Students
(
StudID INTEGER PRIMARY KEY,
StudName CHARACTER VARYING,
StudClass CHAR(1)
);
CREATE TABLE

highgo=# INSERT INTO tbl_Students VALUES (1,'Anvesh','A'),(2,'Neevan','B'),(3,'Jenny','C'),(4,'Roy','C'),(5,'Martin','C');
INSERT 0 5

highgo=# CREATE TABLE tbl_StudentMarks
(
StudentMarkID INTEGER PRIMARY KEY,
StudID INTEGER,
Sub1Mark SMALLINT,
Sub2Mark SMALLINT,
Sub3Mark SMALLINT,
CONSTRAINT fk_tbl_StudentMarks_StudID FOREIGN KEY (StudID) REFERENCES tbl_Students (StudID)
);
CREATE TABLE

highgo=# INSERT INTO tbl_StudentMarks VALUES (1,6,50,60,90);
ERROR:  23503: insert or update on table "tbl_studentmarks" violates foreign key constraint "fk_tbl_studentmarks_studid"
DETAIL:  Key (studid)=(6) is not present in table "tbl_students".

highgo=# ALTER TABLE tbl_StudentMarks DISABLE TRIGGER ALL;
ALTER TABLE
highgo=# INSERT INTO tbl_StudentMarks VALUES (1,6,50,60,90);
INSERT 0 1
highgo=# ALTER TABLE tbl_StudentMarks ENABLE TRIGGER ALL;
ALTER TABLE

highgo=# \c  highgo test_role
PSQL: Release 5.6.4
Connected to:
HighGo Database V5.6 Enterprise Edition Release 5.6.4 - 64-bit Production
You are now connected to database "highgo" as user "test_role".
highgo=> ALTER TABLE tbl_StudentMarks DISABLE TRIGGER ALL;
ERROR:  42501: must be owner of relation tbl_studentmarks
highgo=>
```