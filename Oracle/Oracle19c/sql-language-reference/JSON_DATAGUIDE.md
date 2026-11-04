---
title: JSON_DATAGUIDE
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/JSON_DATAGUIDE.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

[Description of the illustration json\_dataguide.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/json_dataguide.html)

## Purpose

The aggregate function `JSON_DATAGUIDE` takes a table column of JSON data as input, and returns the data guide as a `CLOB`. Each row in the column is referred to as a JSON document. For each JSON document in the column, this function returns a `CLOB` value that contains a flat data guide for that JSON document.

`JSON_DATAGUIDE` can detect `GeoJSON` type.

## expr expr is a SQL expression that evaluates to a JSON object or a JSON array.

## format options

Use the format options to specify the format of the data guide that will be returned. It must be one of the following values:

- `dbms_json.format_flat` for a flat structure.
- `dbms_json.format_hierarchical` for a hierarchical structure.

## flag options

`flag` can have the following values:

- Specify `DBMS_JSON.PRETTY` to improve readability of returned data guide with appropriate indentation.
- Specify `DBMS_JSON.GEOJSON` for the data guide to auto detect the `GeoJSON` type.
- Specify `DBMS_JSON.GEOJSON+DBMS_JSON.PRETTY` for the data guide to auto detect the `GeoJSON` type and to improve readability of the returned data guide.

A view created with the data guide will have a corresponding column with `sdo_geometry` type.

**Restrictions on JSON\_DATAGUIDE**

You cannot run this function on a shard catalog server.

**See Also:** [*Oracle Database JSON Developer’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=ADJSN-GUID-219FC30E-89A7-4189-BC36-7B961A24067C) for more information on data guides

## Examples

The following example uses the `j_purchaseorder` table, which is created in “ [Creating a Table That Contains a JSON Document: Example](JSON_TABLE.md) ”. This table contains a column of JSON data called `po_document`. This examples returns a flat data guide for each JSON document in the column `po_document`.

```md
SELECT EXTRACT(YEAR FROM date_loaded) YEAR,
       JSON_DATAGUIDE(po_document) "DATA GUIDE"
  FROM j_purchaseorder
  GROUP BY extract(YEAR FROM date_loaded)
  ORDER BY extract(YEAR FROM date_loaded) DESC;

YEAR DATA GUIDE
---- ------------------------------------------
2016 [
       {
         "o:path" : "$.PO_ID",
         "type" : "number",
         "o:length" : 4
       },
       {
         "o:path" : "$.PO_Ref",
         "type" : "string",
         "o:length" : 16
       },
       {
         "o:path" : "$.PO_Items",
         "type" : "array",
         "o:length" : 64
       },
       {
         "o:path" : "$.PO_Items.Part_No",
         "type" : "number",
         "o:length" : 16
       },
       {
         "o:path" : "$.PO_Items.Item_Quantity",
         "type" : "number",
         "o:length" : 2
       }
     ]
. . .
```