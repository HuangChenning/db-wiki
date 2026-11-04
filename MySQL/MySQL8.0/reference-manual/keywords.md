---
title: "11.3 Keywords and Reserved Words"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/keywords.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

Keywords are words that have significance in SQL. Certain keywords, such as [`SELECT`](select.md), [`DELETE`](delete.md), or [`BIGINT`](integer-types.md), are reserved and require special treatment for use as identifiers such as table and column names. This may also be true for the names of built-in functions.

Most nonreserved keywords are permitted as identifiers without quoting. Some keywords which are otherwise considered nonreserved are restricted from use as unquoted identifiers for roles, stored program labels, or, in some cases, both. See MySQL 8.0 Restricted Keywords, for listings of these keywords.

Reserved words are permitted as identifiers if you quote them as described in [Section 11.2, “Schema Object Names”](identifiers.md):

```
mysql> CREATE TABLE interval (begin INT, end INT);
ERROR 1064 (42000): You have an error in your SQL syntax ...
near 'interval (begin INT, end INT)'
```

`BEGIN` and `END` are keywords but not reserved, so their use as identifiers does not require quoting. `INTERVAL` is a reserved keyword and must be quoted to be used as an identifier:

```
mysql> CREATE TABLE \`interval\` (begin INT, end INT);
Query OK, 0 rows affected (0.01 sec)
```

Exception: A word that follows a period in a qualified name must be an identifier, so it need not be quoted even if it is reserved:

```
mysql> CREATE TABLE mydb.interval (begin INT, end INT);
Query OK, 0 rows affected (0.01 sec)
```

Names of built-in functions are permitted as identifiers but may require care to be used as such. For example, `COUNT` is acceptable as a column name. However, by default, no whitespace is permitted in function invocations between the function name and the following `(` character. This requirement enables the parser to distinguish whether the name is used in a function call or in nonfunction context. For further details on recognition of function names, see [Section 11.2.5, “Function Name Parsing and Resolution”](function-resolution.md).

The `INFORMATION_SCHEMA.KEYWORDS` table lists the words considered keywords by MySQL and indicates whether they are reserved. See [Section 28.3.17, “The INFORMATION\_SCHEMA KEYWORDS Table”](information-schema-keywords-table.md).

### MySQL 8.0 Keywords and Reserved Words

The following list shows the keywords and reserved words in MySQL 8.0, along with changes to individual words from version to version. Reserved keywords are marked with (R). In addition, `_FILENAME` is reserved.

At some point, you might upgrade to a higher version, so it is a good idea to have a look at future reserved words, too. You can find these in the manuals that cover higher versions of MySQL. Most of the reserved words in the list are forbidden by standard SQL as column or table names (for example, `GROUP`). A few are reserved because MySQL needs them and uses a **yacc** parser.

A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z

A

- `ACCESSIBLE` (R)
- `ACCOUNT`
- `ACTION`
- `ACTIVE`; added in 8.0.14 (nonreserved)
- `ADD` (R)
- `ADMIN`; became nonreserved in 8.0.12
- `AFTER`
- `AGAINST`
- `AGGREGATE`
- `ALGORITHM`
- `ALL` (R)
- `ALTER` (R)
- `ALWAYS`
- `ANALYSE`; removed in 8.0.1
- `ANALYZE` (R)
- `AND` (R)
- `ANY`
- `ARRAY`; added in 8.0.17 (reserved); became nonreserved in 8.0.19
- `AS` (R)
- `ASC` (R)
- `ASCII`
- `ASENSITIVE` (R)
- `AT`
- `ATTRIBUTE`; added in 8.0.21 (nonreserved)
- `AUTHENTICATION`; added in 8.0.27 (nonreserved)
- `AUTOEXTEND_SIZE`
- `AUTO_INCREMENT`
- `AVG`
- `AVG_ROW_LENGTH`

B

- `BACKUP`
- `BEFORE` (R)
- `BEGIN`
- `BETWEEN` (R)
- `BIGINT` (R)
- `BINARY` (R)
- `BINLOG`
- `BIT`
- `BLOB` (R)
- `BLOCK`
- `BOOL`
- `BOOLEAN`
- `BOTH` (R)
- `BTREE`
- `BUCKETS`; added in 8.0.2 (nonreserved)
- `BULK`; added in 8.0.32 (nonreserved)
- `BY` (R)
- `BYTE`

C

- `CACHE`
- `CALL` (R)
- `CASCADE` (R)
- `CASCADED`
- `CASE` (R)
- `CATALOG_NAME`
- `CHAIN`
- `CHALLENGE_RESPONSE`; added in 8.0.27 (nonreserved)
- `CHANGE` (R)
- `CHANGED`
- `CHANNEL`
- `CHAR` (R)
- `CHARACTER` (R)
- `CHARSET`
- `CHECK` (R)
- `CHECKSUM`
- `CIPHER`
- `CLASS_ORIGIN`
- `CLIENT`
- `CLONE`; added in 8.0.3 (nonreserved)
- `CLOSE`
- `COALESCE`
- `CODE`
- `COLLATE` (R)
- `COLLATION`
- `COLUMN` (R)
- `COLUMNS`
- `COLUMN_FORMAT`
- `COLUMN_NAME`