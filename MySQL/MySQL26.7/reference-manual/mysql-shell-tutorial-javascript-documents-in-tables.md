---
title: "MySQL :: MySQL 26.7 Reference Manual :: 22.3.5 Documents in Tables"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/mysql-shell-tutorial-javascript-documents-in-tables.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 22.3.5 Documents in Tables

In MySQL, a table may contain traditional relational data, JSON values, or both. You can combine traditional data with JSON documents by storing the documents in columns having a native [`JSON`](json.md) data type.

Examples in this section use the city table in the `world_x` schema.

#### city Table Description

The city table has five columns (or fields).

```svg
+---------------+------------+-------+-------+---------+------------------+
| Field         | Type       | Null  | Key   | Default | Extra            |
+---------------+------------+-------+-------+---------+------------------+
| ID            | int(11)    | NO    | PRI   | null    | auto_increment   |
| Name          | char(35)   | NO    |       |         |                  |
| CountryCode   | char(3)    | NO    |       |         |                  |
| District      | char(20)   | NO    |       |         |                  |
| Info          | json       | YES   |       | null    |                  |
+---------------+------------+-------+-------+---------+------------------+
```

#### Insert a Record

To insert a document into the column of a table, pass to the `values()` method a well-formed JSON document in the correct order. In the following example, a document is passed as the final value to be inserted into the Info column.

```svg
mysql-js> db.city.insert().values(
None, "San Francisco", "USA", "California", '{"Population":830000}')
```

#### Select a Record

You can issue a query with a search condition that evaluates document values in the expression.

```svg
mysql-js> db.city.select(["ID", "Name", "CountryCode", "District", "Info"]).where(
"CountryCode = :country and Info->'$.Population' > 1000000").bind(
'country', 'USA')
+------+----------------+-------------+----------------+-----------------------------+
| ID   | Name           | CountryCode | District       | Info                        |
+------+----------------+-------------+----------------+-----------------------------+
| 3793 | New York       | USA         | New York       | {"Population": 8008278}     |
| 3794 | Los Angeles    | USA         | California     | {"Population": 3694820}     |
| 3795 | Chicago        | USA         | Illinois       | {"Population": 2896016}     |
| 3796 | Houston        | USA         | Texas          | {"Population": 1953631}     |
| 3797 | Philadelphia   | USA         | Pennsylvania   | {"Population": 1517550}     |
| 3798 | Phoenix        | USA         | Arizona        | {"Population": 1321045}     |
| 3799 | San Diego      | USA         | California     | {"Population": 1223400}     |
| 3800 | Dallas         | USA         | Texas          | {"Population": 1188580}     |
| 3801 | San Antonio    | USA         | Texas          | {"Population": 1144646}     |
+------+----------------+-------------+----------------+-----------------------------+
9 rows in set (0.01 sec)
```