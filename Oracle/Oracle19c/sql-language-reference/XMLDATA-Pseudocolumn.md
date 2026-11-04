---
title: XMLDATA Pseudocolumn
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/XMLDATA-Pseudocolumn.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

Oracle stores `XMLType` data either in LOB or object-relational columns, based on XMLSchema information and how you specify the storage clause. The `XMLDATA` pseudocolumn lets you access the underlying LOB or object relational column to specify additional storage clause parameters, constraints, indexes, and so forth.

## Example

The following statements illustrate the use of this pseudocolumn. Suppose you create a simple table of `XMLType` with one `CLOB` column:

```md
CREATE TABLE xml_lob_tab of XMLTYPE
  XMLTYPE STORE AS CLOB;
```

To change the storage characteristics of the underlying LOB column, you can use the following statement:

```md
ALTER TABLE xml_lob_tab
  MODIFY LOB (XMLDATA) (STORAGE (MAXSIZE 2G) CACHE);
```

Now suppose you have created an XMLSchema-based table like the `xwarehouses` table created in [Using XML in SQL Statements](Using-XML-in-SQL-Statements.md). You could then use the `XMLDATA` column to set the properties of the underlying columns, as shown in the following statement:

```md
ALTER TABLE xwarehouses
  ADD (UNIQUE(XMLDATA."WarehouseId"));
```