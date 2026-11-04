---
title: Data Dictionary
book: "Database Gateway for Adabas User's Guide"
doc_id: E12074-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/gateways.112/e12074/adabas_data_dictionary.htm
tags:
  - oracle
  - 11g
  - database-gateway-for-adabas-users-guide
---

## C Data Dictionary

The Oracle Database Gateway for Adabas translates a query that refers to an Oracle Database data dictionary table into a query that retrieves the data from an Adabas data dictionary. You perform queries on data dictionary tables over the database link in the same way you query data dictionary tables in the Oracle Database. The gateway data dictionary is similar to the Oracle Database data dictionary in appearance and use.

This appendix contains the following sections:

- Data Dictionary Support
- Adabas Data Dictionary Descriptions

## Data Dictionary Support

Data dictionary information is stored in either the gateway's advanced data dictionary (ADD) or the PREDICT table in the Adabas database. The views and tables that the gateway supports provide information on the following:

- The tables existing in the data source
- The columns for each table
- The primary key for each table
- The foreign keys for each table
- Which primary key each foreign key references
- The existing users and indexes

The following topics describe the data dictionary support for the Oracle Database Gateway.

### Accessing the Gateway Data Dictionary

Accessing a definition of the ADD or the PREDICT table in the Adabas database is identical to accessing a data dictionary table or view definition in an Oracle database. You issue a SQL `SELECT` statement specifying a database link. The Oracle Database data dictionary view and column names are used to access the gateway data dictionary. Synonyms of supported views are also acceptable. For example, the following statement queries the data dictionary table `ALL_TABLES`:

```
SQL> SELECT * FROM ALL_TABLES@Adabas;
```

When a data dictionary access query is issued, the gateway:

1. Maps the requested table, view, or synonym to one or more ADD names.
2. Processes the query within the gateway.
3. May convert the retrieved data to give it the appearance of the Oracle Database data dictionary table.
4. Passes the data dictionary information to the Oracle Database.

### Supported Views and Tables

The gateway supports the following views and tables:

- Supported Views and Tables
- `ALL_CATALOG`
- `ALL_CONS_COLUMNS`
- `ALL_IND_COLUMNS`
- `ALL_OBJECTS`
- `ALL_TAB_COMMENTS`
- `ALL_USERS`
- `DBA_CATALOG`
- `DBA_OBJECTS`
- `DICTIONARY`
- `USER_CATALOG`
- `USER_CONS_COLUMNS`
- `USER_IND_COLUMNS`
- `USER_OBJECTS`
- `USER_TAB_COMMENTS`
- `USER_USERS`
- `ALL_COL_COMMENTS`
- `ALL_CONSTRAINTS`
- `ALL_INDEXES`
- `ALL_TAB_COLUMNS`
- `ALL_TABLES`
- `ALL_VIEWS`
- `DBA_TAB_COLUMNS`
- `DICT_COLUMNS`
- `DUAL`
- `USER_COL_COMMENTS`
- `USER_CONSTRAINTS`
- `USER_INDEXES`
- `USER_TAB_COLUMNS`
- `USER_TABLES`
- `USER_VIEWS`

No other Oracle Database data dictionary tables or views are supported. If you use a view not on the list, you receive the Oracle Database error code for no more rows available.

If you want to select data dictionary views using `SELECT` `FROM` `DBA_` \*, first connect as Oracle user `SYSTEM` or `SYS`. Otherwise, you receive the following error message:

```
ORA-28506: Parse error in data dictionary translation for %s stored in %s
```

Queries through the gateway of any data dictionary table or view beginning with ALL\_ can returns rows from Adabas even when access privileges for those Adabas objects have not been granted. When querying an Oracle database with the Oracle data dictionary, rows are returned only for those objects you are permitted to access.

See Also:

[Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for more information on error messages.

### Default Column Values

There is a minor difference between the gateway data dictionary and a typical Oracle Database data dictionary. The Oracle Database columns that are missing in an Adabas data dictionary table are filled with zeros, spaces, null values, or default values, depending on the column type.

## Adabas Data Dictionary Descriptions

The gateway data dictionary tables and views provide the following information:

- Name, datatype, and width of each column
- The contents of columns with fixed values

In the descriptions that follow, the values in the Null? column may differ from the Oracle Database data dictionary tables and views. Any default value is shown to the right of an item.

Note:

In all data dictionary tables, the OWNER column has the value `ADABAS`.

Table C-1 describes the ALL\_CATALOG table.

Table C-1 ALL\_CATALOG

| Name | Null? | Type | Value |
| --- | --- | --- | --- |
| `OWNER` | `NOT` `NULL` | `VARCHAR2` `(30)` | `ADABAS` |
| `TABLE_NAME` | `NOT` `NULL` | `VARCHAR2` `(30)` | \- |
| `TABLE_TYPE` | \- | `VARCHAR2` `(11)` | " `TABLE` " |

Table C-2 describes the ALL\_COL\_COMMENTS table.

Table C-2 ALL\_COL\_COMMENTS

| Name | Null? | Type | Value |
| --- | --- | --- | --- |
| `OWNER` | `NOT` `NULL` | `VARCHAR2` `(30)` | `ADABAS` |
| `TABLE_NAME` | `NOT` `NULL` | `VARCHAR2` `(30)` | \- |
| `COLUMN_NAME` | `NOT` `NULL` | `VARCHAR2(30)` | \- |