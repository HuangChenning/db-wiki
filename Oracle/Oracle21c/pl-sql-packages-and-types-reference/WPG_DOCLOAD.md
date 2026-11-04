---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/WPG_DOCLOAD.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 283 WPG\_DOCLOAD

The `WPG_DOCLOAD` package provides an interface to download files, `BLOB` s and `BFILE` s.

See Also:

For more information about implementation of this package:

- [Oracle Fusion Middleware Administrator's Guide for Oracle HTTP Server](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=HSADM)
- [Oracle Fusion Middleware User's Guide for mod\_plsql](https://docs.oracle.com/cd/E23943_01/portal.1111/e12041/toc.htm)

The chapter contains the following topics:

- Constants
- Summary of WPG\_DOCLOAD Subprograms

### 283.1 WPG\_DOCLOAD Constants

`WPG_DOCLOAD` defines several constants to use when specifying parameter values.

The `WPG_DOCLOAD` constants are listed below:

- NAME\_COL\_LEN
- MIMET\_COL\_LEN
- MAX\_DOCTABLE\_NAME\_LEN

NAME\_COL\_LEN

The `NAME` column in your document table must be the same as the value of `name_col_len`.

```
name_col_len CONSTANT pls_integer := 64;
```

MIMET\_COL\_LEN

The `MIME_TYPE` column in your document table must be the same as the value of `mimet_col_len`.

```
mimet_col_len CONSTANT pls_integer := 48;
```

MAX\_DOCTABLE\_NAME\_LEN

The name length of your document table must be less than `max_doctable_name_len`.

```
max_doctable_name_len CONSTANT pls_integer := 256;
```

### 283.2 Summary of WPG\_DOCLOAD Subprograms

The WPG\_DOCLOAD package uses one subprogram, the `DOWNLOAD_FILE` procedure.

Table 283-1 WPG\_DOCLOAD Package Subprograms

| Subprogram | Description |
| --- | --- |
| DOWNLOAD\_FILE Procedures | Downloads files, `BLOBS` and `BFILES` |

#### 283.2.1 DOWNLOAD\_FILE Procedures

There are three versions of this download file procedure.

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

Table 283-2 DOWNLOAD\_FILE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p_filename` | The file to download from the document table. |
| `p_blob` | The `BLOB` to download. |
| `p_bfile` | The `BFILE` to download (see Usage Notes). |
| `p_bcaching` | Whether browser caching is enabled (see Usage Notes). |

Usage Notes

- Normally, a document will be downloaded to the browser unless the browser sends an 'If-Modified-Since' header to the gateway indicating that it has the requested document in its cache. In that case, the gateway will determine if the browser's cached copy is up to date, and if it is, it will send an HTTP 304 status message to the browser indicating that the browser should display the cached copy. However, because a document URL and a document do not necessarily have a one-to-one relationship in the PL/SQL Web Gateway, in some cases it may be undesirable to have the cached copy of a document displayed. In those cases, the `p_bcaching` parameter should be set to FALSE to indicate to the gateway to ignore the 'If-Modified-Since' header, and download the document.
- `p_bfile` and `p_blob` are declared as `IN` `OUT` because the locator is initially opened to check for file accessibility and existence. The open operation can only be performed if the locator is writable and readable.