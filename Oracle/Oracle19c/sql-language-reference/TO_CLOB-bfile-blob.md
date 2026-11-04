---
title: "TO_CLOB (bfile|blob)"
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/TO_CLOB-bfile-blob.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

![to_clob_bfile_blob](img/to_clob_bfile_blob.gif)

> ```
> TO_CLOB( { bfile | blob } [, csid] [, mime_type] )
> ```
>
> [Copyright ©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr) 2026,1996, Oracle and/or its affiliates.


[Description of the illustration to\_clob\_bfile\_blob.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/to_clob_bfile_blob.html)

## Purpose

`TO_CLOB` (bfile|blob) converts `BFILE` or `BLOB` data to the database character set and returns the data as a `CLOB` value.

For *csid*, specify the character set ID of the `BFILE` or `BLOB` data. If the character set of the `BFILE` or `BLOB` data is the database character set, then you can specify a value of 0 for *csid*, or omit *csid* altogether.

For *mime\_type*, specify the MIME type to be set on the `CLOB` value returned by this function. If you omit *mime\_type*, then a MIME type will not be set on the `CLOB` value.

**See Also:** in [*Oracle Database Globalization Support Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=NLSPG-GUID-AFCE41ED-775B-4A00-AF38-C436776AE0C5) for the collation derivation rules, which define the collation assigned to the character return value of this function

## Example

The following hypothetical example returns the `CLOB` of a `BFILE` column value `docu` in table `media_tab`, which uses the character set with ID 873. It sets the MIME type to `text/xml` for the resulting `CLOB`.

```md
SELECT TO_CLOB(docu, 873, 'text/xml') FROM media_tab;
```