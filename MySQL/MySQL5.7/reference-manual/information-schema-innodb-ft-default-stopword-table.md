---
title: "24.4.10 The INFORMATION_SCHEMA INNODB_FT_DEFAULT_STOPWORD Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-ft-default-stopword-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.10 The INFORMATION\_SCHEMA INNODB\_FT\_DEFAULT\_STOPWORD Table

The `INNODB_FT_DEFAULT_STOPWORD` table holds a list of [stopwords](glossary.md) that are used by default when creating a `FULLTEXT` index on `InnoDB` tables. For information about the default `InnoDB` stopword list and how to define your own stopword lists, see [Section 12.9.4, “Full-Text Stopwords”](fulltext-stopwords.md).

For related usage information and examples, see [Section 14.16.4, “InnoDB INFORMATION\_SCHEMA FULLTEXT Index Tables”](innodb-information-schema-fulltext_index-tables.md).

The `INNODB_FT_DEFAULT_STOPWORD` table has these columns:

- `value`
	A word that is used by default as a stopword for `FULLTEXT` indexes on `InnoDB` tables. This is not used if you override the default stopword processing with either the [`innodb_ft_server_stopword_table`](innodb-parameters.md) or the [`innodb_ft_user_stopword_table`](innodb-parameters.md) system variable.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_FT_DEFAULT_STOPWORD;
+-------+
| value |
+-------+
| a     |
| about |
| an    |
| are   |
| as    |
| at    |
| be    |
| by    |
| com   |
| de    |
| en    |
| for   |
| from  |
| how   |
| i     |
| in    |
| is    |
| it    |
| la    |
| of    |
| on    |
| or    |
| that  |
| the   |
| this  |
| to    |
| was   |
| what  |
| when  |
| where |
| who   |
| will  |
| with  |
| und   |
| the   |
| www   |
+-------+
36 rows in set (0.00 sec)
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.
- For more information about `InnoDB` `FULLTEXT` search, see [Section 14.6.2.4, “InnoDB Full-Text Indexes”](innodb-fulltext-index.md), and [Section 12.9, “Full-Text Search Functions”](fulltext-search.md).