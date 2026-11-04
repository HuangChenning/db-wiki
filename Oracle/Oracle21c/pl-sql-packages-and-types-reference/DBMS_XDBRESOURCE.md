---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_XDBRESOURCE.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 207 DBMS\_XDBRESOURCE

The `DBMS_XDBRESOURCE` package provides the interface to operate on the resource's metadata and contents.

This chapter contains the following topics:

See Also:

Oracle XML DB Developer's Guide for examples of ["Using `DBMS_XDBRESOURCE` "](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADXDB2580)

### 207.1 DBMS\_XDBRESOURCE Overview

The `DBMS_XDBRESOURCE` package provides routines to get and set the resource's metadata and contents. To take advantage of the DOM traversal facility, provided in `DBMS_XMLDOM` package, an `XDBResource` instance could be converted to a `DOMDocument` type by using `DBMS_XDBRESOURCE`.`MAKEDOCUMENT` routine.

### 207.2 DBMS\_XDBRESOURCE Security Model

Owned by `XDB`, the `DBMS_XDBRESOURCE` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

### 207.3 Summary of DBMS\_XDBRESOURCE Subprograms

This table lists the `DBMS_XDBRESOURCE` subprograms and briefly describes them.

Table 207-1 DBMS\_XDBRESOURCE Package Subprograms

| Subprogram | Description |
| --- | --- |
| FREERESOURCE Procedure | Frees any memory associated with an XDBResource |
| GETACL Function | Given an XDBResource, returns its ACL as string |
| GETACLDOCFROMRES Function | Returns the ACL Document for the given resource as `XMLType` |
| GETAUTHOR Function | Given an XDBResource, returns its author |
| GETCHARACTERSET Function | Given an XDBResource, returns its character set |
| GETCOMMENT Function | Given an XDBResource, returns its comment |
| GETCONTENTBLOB Function | Returns the contents of the resource as a `BLOB` |
| GETCONTENTCLOB Function | Returns the contents of the resource as a `CLOB` |
| GETCONTENTREF Function | Returns the contents of the resource as an `XMLTypeRef` |
| GETCONTENTTYPE Function | Given an XDBResource, returns its content-type |
| GETCONTENTXML Function | Returns the contents of the resource as XML |
| GETCONTENTVARCHAR2 Function | Returns the contents of the resource as a string |
| GETCREATIONDATE Function | Given an XDBResource, returns its creation date |
| GETCREATOR Function | Given an XDBResource, returns its creator |
| GETCUSTOMMETADATA Function | Returns the requested custom metadata given the xpath and namespace to the metadata |
| GETDISPLAYNAME Function | Given an XDBResource, returns its display name |
| GETLANGUAGE Function | Given an XDBResource, returns its language |
| GETLASTMODIFIER Function | Given an XDBResource, returns its last modifier |
| GETMODIFICATIONDATE Function | Given an XDBResource, returns its modification date |
| GETOWNER Function | Given an XDBResource, returns its owner. |
| GETREFCOUNT Function | Given an XDBResource, returns its reference count |
| GETVERSIONID Function | Given an XDBResource, returns its version ID. |
| HASACLCHANGED Function | Returns `TRUE` if the ACL of the given resource has changed, `FALSE` otherwise |
| HASAUTHORCHANGED Function | Returns `TRUE` if the ACL of the given resource has changed `FALSE` otherwise |
| HASCHANGED Function | Returns `TRUE` if the element or attribute represented by the given XPath has changed, `FALSE` otherwise |
| HASCHARACTERSETCHANGED Function | Returns `TRUE` if the character set of the given resource has changed, `FALSE` otherwise |
| HASCOMMENTCHANGED Function | Returns `TRUE` if the comment of the given resource has changed, `FALSE` otherwise |
| HASCONTENTCHANGED Function | Returns `TRUE` if the contents of the given resource has changed, `FALSE` otherwise |
| HASCONTENTTYPECHANGED Function | Returns `TRUE` if the content-type of the given resource has changed, `FALSE` otherwise |
| HASCREATIONDATECHANGED Function | Returns `TRUE` if the creation date of the given resource has changed, `FALSE` otherwise |
| HASCREATORCHANGED Function | Returns `TRUE` if the creator of the given resource has changed, `FALSE` otherwise |
| HASCUSTOMMETADATACHANGED Function | Returns `TRUE` if custom-metadata for this XPath has changed, `FALSE` otherwise |
| HASDISPLAYNAMECHANGED Function | Returns `TRUE` if the display name of the given resource has changed, `FALSE` otherwise |
| HASLANGUAGECHANGED Function | Returns `TRUE` if the language of the given resource has changed, `FALSE` otherwise |
| HASLASTMODIFIERCHANGED Function | Returns `TRUE` if the last modifier of the given resource has changed, `FALSE` otherwise |
| HASMODIFICATIONDATECHANGED Function | Returns `TRUE` if the modification date of the given resource has changed, `FALSE` otherwise |
| HASOWNERCHANGED Function | Returns `TRUE` if the owner of the given resource has changed, `FALSE` otherwise |
| HASREFCOUNTCHANGED Function | Returns `TRUE` if the reference count of the given resource has changed, `FALSE` otherwise |
| HASVERSIONIDCHANGED Function | Returns `TRUE` if the version ID of the given resource has changed, `FALSE` otherwise |
| ISFOLDER Function | Returns `TRUE` if the given resource is a folder, `FALSE` otherwise |
| ISNULL Function | Returns `TRUE` if input resource is `NULL`, `FALSE` otherwise |
| MAKEDOCUMENT Function | Converts the XDBResource to a DOMDocument which can be operated on using the XMLDOM interface |
| SAVE Procedure | Updates the resource with any modifications |
| SETACL Procedure | Sets the ACL of the given XDBResource to the path specified |
| SETAUTHOR Procedure | Sets the author of the given XDBResource to the specified string |
| SETCHARACTERSET Procedure | Sets the character set of the given XDBResource to a specified character set |
| SETCOMMENT Procedure | Sets a comment associated with the given XDBResource |
| SETCONTENT Procedures | Replaces the contents of the given resource with the given `CLOB` |
| SETCONTENTTYPE Procedure | Sets the content-type of the given XDBResource |
| SETCUSTOMMETADATA Procedure | Sets the custom metadata specified by the XPath and namespace to new data |
| SETDISPLAYNAME Procedure | Sets the display name of the given XDBResource |
| SETLANGUAGE Procedure | Sets the language of the given XDBResource |
| SETOWNER Procedure | Sets the owner of the given XDBResource |

#### 207.3.1 FREERESOURCE Procedure

This procedure frees any memory associated with an XDBResource.

Syntax

```
DBMS_XDBRESOURCE.FREERESOURCE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-2 FREERESOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource to free |

#### 207.3.2 GETACL Function

Given an XDBResource, this function returns its ACL as string.

Syntax

```
DBMS_XDBRESOURCE.GETACL (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-3 GETACL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.3 GETACLDOCFROMRES Function

This function returns the ACL Document for the given resource as `XMLType`.

Syntax

```
DBMS_XDBRESOURCE.GETACLDOCFROMRES (
   res   IN    XDBResource) 
 RETURN SYS.XMLTYPE;
```

Parameters

Table 207-4 GETACLDOCFROMRES Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.4 GETAUTHOR Function

Given an XDBResource, this function returns its author.

Syntax

```
DBMS_XDBRESOURCE.GETAUTHOR (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-5 GETAUTHOR Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.5 GETCHARACTERSET Function

Given an XDBResource, this function returns its characterset.

Syntax

```
DBMS_XDBRESOURCE.GETCHARACTERSET (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-6 GETCHARACTERSET Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.6 GETCOMMENT Function

Given an XDBResource, this function returns its comment.

Syntax

```
DBMS_XDBRESOURCE.GETCOMMENT (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-7 GETCOMMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.7 GETCONTENTBLOB Function

This function returns the contents of the resource as a `BLOB`.

Syntax

```
DBMS_XDBRESOURCE.GETCONTENTBLOB (
   res    IN     XDBResource,
   csid   OUT    PLS_INTEGER) 
 RETURN BLOB;
```

Parameters

Table 207-8 GETCONTENTBLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `csid` | Character set ID of the `BLOB` returned |

#### 207.3.8 GETCONTENTCLOB Function

This function returns the contents of the resource as a `CLOB`.

Syntax

```
DBMS_XDBRESOURCE.GETCONTENTCLOB (
   res   IN    XDBResource) 
 RETURN CLOB;
```

Parameters

Table 207-9 GETCONTENTCLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.9 GETCONTENTREF Function

This function returns the contents of the resource as an `XMLTypeRef`.

Syntax

```
DBMS_XDBRESOURCE.GETCONTENTREF (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-10 GETCONTENTREF Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.10 GETCONTENTTYPE Function

Given an XDBResource, this function returns its content-type.

Syntax

```
DBMS_XDBRESOURCE.GETCONTENTTYPE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-11 GETCONTENTTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.11 GETCONTENTXML Function

This function returns the contents of the resource as an `XMLTypeRef`.

Syntax

```
DBMS_XDBRESOURCE.GETCONTENTXML (
   res   IN    XDBResource) 
 RETURN XMLType;
```

Parameters

Table 207-12 GETCONTENTXML Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.12 GETCONTENTVARCHAR2 Function

This function returns the contents of the resource as a string.

Syntax

```
DBMS_XDBRESOURCE.GETCONTENTVARCHAR2 (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-13 GETCONTENTVARCHAR2 Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.13 GETCREATIONDATE Function

Given an XDBResource, this function returns its creation date.

Syntax

```
DBMS_XDBRESOURCE.GETCREATIONDATE (
   res   IN    XDBResource) 
 RETURN TIMESTAMP;
```

Parameters

Table 207-14 GETCREATIONDATE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.14 GETCREATOR Function

Given an XDBResource, this function returns its creator.

Syntax

```
DBMS_XDBRESOURCE.GETCREATOR (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-15 GETCREATOR Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.15 GETCUSTOMMETADATA Function

This function returns the requested custom metadata given the xpath and namespace to the metadata.

Syntax

```
DBMS_XDBRESOURCE.GETCUSTOMMETADATA (
   res        IN    XDBResource, 
   xpath      IN    VARCHAR2,    namespace  IN    VARCHAR2)
 RETURN XMLType;
```

Parameters

Table 207-16 GETCUSTOMMETADATA Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath for custom metadata |
| `namespace` | Namespace |

Usage Notes

The first component of the XPath expression must be "Resource".

#### 207.3.16 GETDISPLAYNAME Function

Given an XDBResource, this function returns its display name.

Syntax

```
DBMS_XDBRESOURCE.GETDISPLAYNAME (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-17 GETDISPLAYNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.17 GETLANGUAGE Function

Given an XDBResource, this function returns its language.

Syntax

```
DBMS_XDBRESOURCE.GETLANGUAGE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-18 GETLANGUAGE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.18 GETLASTMODIFIER Function

Given an XDBResource, this function returns its last modifier.

Syntax

```
DBMS_XDBRESOURCE.GETLASTMODIFIER (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-19 GETLASTMODIFIER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.19 GETMODIFICATIONDATE Function

Given an XDBResource, this function returns its modification date.

Syntax

```
DBMS_XDBRESOURCE.GETMODIFICATIONDATE (
   res   IN    XDBResource) 
 RETURN TIMESTAMP;
```

Parameters

Table 207-20 GETMODIFICATIONDATE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.20 GETOWNER Function

Given an XDBResource, this function returns its owner.

Syntax

```
DBMS_XDBRESOURCE.GETOWNER (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 207-21 GETOWNER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.21 GETREFCOUNT Function

Given an XDBResource, this function returns its reference count.

Syntax

```
DBMS_XDBRESOURCE.GETREFCOUNT (
   res   IN    XDBResource) 
 RETURN PLS_INTEGER;
```

Parameters

Table 207-22 GETREFCOUNT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.22 GETVERSIONID Function

Given an XDBResource, this function returns its version ID.

Syntax

```
DBMS_XDBRESOURCE.GETVERSIONID (
   res   IN    XDBResource) 
 RETURN PLS_INTEGER;
```

Parameters

Table 207-23 GETVERSIONID Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.23 HASACLCHANGED Function

This function returns `TRUE` if the ACL of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASACLCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-24 HASACLCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.24 HASAUTHORCHANGED Function

This function returns `TRUE` if the author of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASAUTHORCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-25 HASAUTHORCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.25 HASCHANGED Function

Given an XPath, this function determines whether the element or attribute represented by the XPath has changed.

Syntax

```
DBMS_XDBRESOURCE.HASCHANGED (
   res         IN    XDBResource, 
   xpath       IN    VARCHAR2,
   namespace   IN    VARCHAR2) 
 RETURN BOOLEAN;
```

Parameters

Table 207-26 HASCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath to check |
| `bnamespace` | Namespace to use |

#### 207.3.26 HASCHARACTERSETCHANGED Function

This function returns `TRUE` if the character set of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASCHARACTERSETCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-27 HASCHARACTERSETCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.27 HASCOMMENTCHANGED Function

This function returns `TRUE` if the comment of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASCOMMENTCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-28 HASCOMMENTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.28 HASCONTENTCHANGED Function

This function returns `TRUE` if the contents of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASCONTENTCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-29 HASCONTENTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.29 HASCONTENTTYPECHANGED Function

This function returns `TRUE` if the content-type of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESOURCE.HASCONTENTTYPECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-30 HASCONTENTTYPECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.30 HASCREATIONDATECHANGED Function

This function returns `TRUE` if the creation date of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESOURCE.HASCREATIONDATECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-31 HASCREATIONDATECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.31 HASCREATORCHANGED Function

This function returns `TRUE` if the creator of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESOURCE.HASCREATORCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-32 HASCREATORCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.32 HASCUSTOMMETADATACHANGED Function

This function checks whether the custom-metadata for a given resource has changed.

Syntax

```
DBMS_XDBRESOURCE.HASCUSTOMMETADATACHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-33 HASCUSTOMMETADATACHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.33 HASDISPLAYNAMECHANGED Function

This function returns `TRUE` if the display name of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASDISPLAYNAMECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-34 HASDISPLAYNAMECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.34 HASLANGUAGECHANGED Function

This function returns `TRUE` if the language of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASLANGUAGECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-35 HASLANGUAGECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.35 HASLASTMODIFIERCHANGED Function

This function returns `TRUE` if the last modifier of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESOURCE.HASLASTMODIFIERCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-36 HASLASTMODIFIERCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.36 HASMODIFICATIONDATECHANGED Function

This function returns `TRUE` if the modification date of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESOURCE.HASMODIFICATIONDATECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-37 HASMODIFICATIONDATECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.37 HASOWNERCHANGED Function

This function returns `TRUE` if the owner of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASOWNERCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-38 HASOWNERCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.38 HASREFCOUNTCHANGED Function

This function returns `TRUE` if the reference count of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASREFCOUNTCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-39 HASREFCOUNTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.39 HASVERSIONIDCHANGED Function

This function returns `TRUE` if the version ID of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.HASVERSIONIDCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-40 HASVERSIONIDCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.40 ISFOLDER Function

This function returns `TRUE` if the given resource is a folder, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESOURCE.ISFOLDER (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-41 ISFOLDER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.41 ISNULL Function

This function returns `TRUE` if input resource is `NULL`.

Syntax

```
DBMS_XDBRESOURCE.ISNULL (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 207-42 ISNULL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | Input resource |

#### 207.3.42 MAKEDOCUMENT Function

This function converts the XDBResource to a DOMDocument which can be operated on using the XMLDOM interface.

See Also:

The [DBMS\_XMLDOM](DBMS_XMLDOM.md) package

Syntax

```
DBMS_XDBRESOURCE.MAKEDOCUMENT (
   res   IN    XDBResource) 
 RETURN DBMS_XMLDOM.DOMDocument;
```

Parameters

Table 207-43 MAKEDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.43 SAVE Procedure

This procedures updates the resource with any modifications.

Syntax

```
DBMS_XDBRESOURCE.SAVE (
   res   IN    XDBResource);
```

Parameters

Table 207-44 SAVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

#### 207.3.44 SETACL Procedure

This procedure sets the ACL of the given XDBResource to the path specified.

Syntax

```
DBMS_XDBRESOURCE.SETACL (
   res      IN OUT  XDBResource, 
   ACLPath  IN      VARCHAR2);
```

Parameters

Table 207-45 SETACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `ACLPath` | Absolute path of the new ACL |

#### 207.3.45 SETAUTHOR Procedure

This procedure sets the author of the given XDBResource to the specified string.

Syntax

```
DBMS_XDBRESOURCE.SETAUTHOR (
   res     IN OUT  XDBResource, 
   author  IN      VARCHAR2);
```

Parameters

Table 207-46 SETAUTHOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `author` | Author |

#### 207.3.46 SETCHARACTERSET Procedure

This procedure sets the character set of the given XDBResource to a specified character set.

Syntax

```
DBMS_XDBRESOURCE.SETCHARACTERSET (
   res      IN OUT  XDBResource, 
   charSet  IN      VARCHAR2);
```

Parameters

Table 207-47 SETCHARACTERSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `charset` | New character set |

#### 207.3.47 SETCOMMENT Procedure

This procedure sets a comment associated with the given XDBResource.

Syntax

```
DBMS_XDBRESOURCE.SETCOMMENT (
   res      IN OUT  XDBResource, 
   comment  IN      VARCHAR2);
```

Parameters

Table 207-48 SETCOMMENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |