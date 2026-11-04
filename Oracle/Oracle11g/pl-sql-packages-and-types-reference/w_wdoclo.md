---
title: WPG_DOCLOAD
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/w_wdoclo.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 240 WPG\_DOCLOAD

The `WPG_DOCLOAD` package provides an interface to download files, `BLOB` s and `BFILE` s.

See Also:

For more information about implementation of this package:
- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=YPMOD)

The chapter contains the following topics:

- Using WPG\_DOCLOAD
	- Constants
- Summary of WPG\_DOCLOAD Subprograms

---

## Using WPG\_DOCLOAD

- Constants

---

### Constants

#### NAME\_COL\_LEN

The `NAME` column in your document table must be the same as the value of `name_col_len`.

```
name_col_len CONSTANT pls_integer := 64;
```

#### MIMET\_COL\_LEN

The `MIME_TYPE` column in your document table must be the same as the value of `mimet_col_len`.

```
mimet_col_len CONSTANT pls_integer := 48;
```

#### MAX\_DOCTABLE\_NAME\_LEN

The name length of your document table must be less than `max_doctable_name_len`.

```
max_doctable_name_len CONSTANT pls_integer := 256;
```

---

## Summary of WPG\_DOCLOAD Subprograms

Table 240-1 WPG\_DOCLOAD Package Subprograms

| Subprogram | Description |
| --- | --- |
| DOWNLOAD\_FILE Procedures | Downloads files, `BLOBS` and `BFILES` |

---

### DOWNLOAD\_FILE Procedures

There are three versions of this procedure:

- The first version downloads files and is invoked from within a document download procedure to signal the PL/SQL Gateway that `p_filename` is to be downloaded from the document table to the client's browser.
- The second version can be called from within any procedure to signal the PL/SQL Gateway that `p_blob` is to be downloaded to the client's browser.
- The third version can be called from within any procedure to signal the PL/SQL Gateway that `p_bfile` is to be downloaded to the client's browser.

Syntax

```
WPG_DOCLOAD.DOWNLOAD_FILE(
   p_filename      IN             VARCHAR2, 
   p_bcaching      IN             BOOLEAN DEFAULT TRUE);
```
```
WPG_DOCLOAD.DOWNLOAD_FILE(
   p_blob          IN OUT NOCOPY  BLOB);

WPG_DOCLOAD.DOWNLOAD_FILE(
   p_bfile         IN OUT         BFILE);
```

Parameters

Table 240-2 DOWNLOAD\_FILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p_filename` | The file to download from the document table. |
| `p_blob` | The `BLOB` to download. |
| `p_bfile` | The `BFILE` to download (see Usage Notes). |
| `p_bcaching` | Whether browser caching is enabled (see Usage Notes). |

Usage Notes

- Normally, a document will be downloaded to the browser unless the browser sends an 'If-Modified-Since' header to the gateway indicating that it has the requested document in its cache. In that case, the gateway will determine if the browser's cached copy is up to date, and if it is, it will send an HTTP 304 status message to the browser indicating that the browser should display the cached copy. However, because a document URL and a document do not necessarily have a one-to-one relationship in the PL/SQL Web Gateway, in some cases it may be undesirable to have the cached copy of a document displayed. In those cases, the `p_bcaching` parameter should be set to FALSE to indicate to the gateway to ignore the 'If-Modified-Since' header, and download the document.
- `p_bfile` and `p_blob` are declared as `IN` `OUT` because the locator is initially opened to check for file accessibility and existence. The open operation can only be performed if the locator is writable and readable.