---
title: DBMS_XDBRESOURCE
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xdbresource.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 167 DBMS\_XDBRESOURCE

The `DBMS_XDBRESOURCE` package provides the interface to operate on the resource's metadata and contents.

See Also:

Oracle XML DB Developer's Guide for examples of ["Using `DBMS_XDBRESOURCE` "](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb_repos_events.htm#ADXDB2580)

This chapter contains the following topics:

- Using DBMS\_XDBRESOURCE
- Summary of DBMS\_XDBRESOURCE Subprograms

---

## Using DBMS\_XDBRESOURCE

- Overview
- Security Model

---

### Overview

The `DBMS_XDBRESOURCE` package provides routines to get and set the resource's metadata and contents. To take advantage of the DOM traversal facility, provided in `DBMS_XMLDOM` package, an `XDBResource` instance could be converted to a `DOMDocument` type by using `DBMS_XDBRESOURCE`.`MAKEDOCUMENT` routine.

---

### Security Model

Owned by `XDB`, the `DBMS_XDBRESOURCE` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `PUBLIC`. Subprograms in this package are executed using the privileges of the current user.

---

## Summary of DBMS\_XDBRESOURCE Subprograms

Table 167-1 DBMS\_XDBRESOURCE Package Subprograms

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

---

### FREERESOURCE Procedure

This procedure frees any memory associated with an XDBResource.

Syntax

```
DBMS_XDBRESEROUCE.FREERESOURCE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-2 FREERESOURCE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource to free |

---

### GETACL Function

Given an XDBResource, this function returns its ACL as string.

Syntax

```
DBMS_XDBRESEROUCE.GETACL (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-3 GETACL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETACLDOCFROMRES Function

This function returns the ACL Document for the given resource as `XMLType`.

Syntax

```
DBMS_XDBRESEROUCE.GETACLDOCFROMRES (
   res   IN    XDBResource) 
 RETURN SYS.XMLTYPE;
```

Parameters

Table 167-4 GETACL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETAUTHOR Function

Given an XDBResource, this function returns its author.

Syntax

```
DBMS_XDBRESEROUCE.GETAUTHOR (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-5 GETAUTHOR Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCHARACTERSET Function

Given an XDBResource, this function returns its characterset.

Syntax

```
DBMS_XDBRESEROUCE.GETCHARACTERSET (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-6 GETCHARACTERSET Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCOMMENT Function

Given an XDBResource, this function returns its comment.

Syntax

```
DBMS_XDBRESEROUCE.GETCOMMENT (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-7 GETCOMMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCONTENTBLOB Function

This function returns the contents of the resource as a `BLOB`.

Syntax

```
DBMS_XDBRESEROUCE.GETCONTENTBLOB (
   res    IN     XDBResource,
   csid   OUT    PLS_INTEGER) 
 RETURN BLOB;
```

Parameters

Table 167-8 GETCONTENTBLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `csid` | Character set ID of the `BLOB` returned |

---

### GETCONTENTCLOB Function

This function returns the contents of the resource as a `CLOB`.

Syntax

```
DBMS_XDBRESEROUCE.GETCONTENTCLOB (
   res   IN    XDBResource) 
 RETURN CLOB;
```

Parameters

Table 167-9 GETCONTENTCLOB Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCONTENTREF Function

This function returns the contents of the resource as an `XMLTypeRef`.

Syntax

```
DBMS_XDBRESEROUCE.GETCONTENTREF (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-10 GETCONTENTREF Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCONTENTTYPE Function

Given an XDBResource, this function returns its content-type.

Syntax

```
DBMS_XDBRESEROUCE.GETCONTENTTYPE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-11 GETCONTENTTYPE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCONTENTXML Function

This function returns the contents of the resource as an `XMLTypeRef`.

Syntax

```
DBMS_XDBRESEROUCE.GETCONTENTXML (
   res   IN    XDBResource) 
 RETURN XMLType;
```

Parameters

Table 167-12 GETCONTENTXML Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCONTENTVARCHAR2 Function

This function returns the contents of the resource as a string.

Syntax

```
DBMS_XDBRESEROUCE.GETCONTENTVARCHAR2 (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-13 GETCONTENTVARCHAR2 Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCREATIONDATE Function

Given an XDBResource, this function returns its creation date.

Syntax

```
DBMS_XDBRESEROUCE.GETCREATIONDATE (
   res   IN    XDBResource) 
 RETURN TIMESTAMP;
```

Parameters

Table 167-14 GETCREATIONDATE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCREATOR Function

Given an XDBResource, this function returns its creator.

Syntax

```
DBMS_XDBRESEROUCE.GETCREATOR (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-15 GETCREATOR Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETCUSTOMMETADATA Function

This function returns the requested custom metadata given the xpath and namespace to the metadata.

Syntax

```
DBMS_XDBRESEROUCE.GETCUSTOMMETADATA (
   res        IN    XDBResource, 
   xpath      IN    VARCHAR2,    namespace  IN    VARCHAR2)
 RETURN XMLType;
```

Parameters

Table 167-16 GETCUSTOMMETADATA Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath for custom metadata |
| `namespace` | Namespace |

Usage Notes

The first component of the XPath expression must be "Resource".

---

### GETDISPLAYNAME Function

Given an XDBResource, this function returns its display name.

Syntax

```
DBMS_XDBRESEROUCE.GETDISPLAYNAME (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-17 GETDISPLAYNAME Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETLANGUAGE Function

Given an XDBResource, this function returns its language.

Syntax

```
DBMS_XDBRESEROUCE.GETLANGUAGE (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-18 GETLANGUAGE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETLASTMODIFIER Function

Given an XDBResource, this function returns its last modifier.

Syntax

```
DBMS_XDBRESEROUCE.GETLASTMODIFIER (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-19 GETLASTMODIFIER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETMODIFICATIONDATE Function

Given an XDBResource, this function returns its modification date.

Syntax

```
DBMS_XDBRESEROUCE.GETMODIFICATIONDATE (
   res   IN    XDBResource) 
 RETURN TIMESTAMP;
```

Parameters

Table 167-20 GETMODIFICATIONDATE Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETOWNER Function

Given an XDBResource, this function returns its owner.

Syntax

```
DBMS_XDBRESEROUCE.GETOWNER (
   res   IN    XDBResource) 
 RETURN VARCHAR2;
```

Parameters

Table 167-21 GETOWNER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETREFCOUNT Function

Given an XDBResource, this function returns its reference count.

Syntax

```
DBMS_XDBRESEROUCE.GETREFCOUNT (
   res   IN    XDBResource) 
 RETURN PLS_INTEGER;
```

Parameters

Table 167-22 GETREFCOUNT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### GETVERSIONID Function

Given an XDBResource, this function returns its version ID.

Syntax

```
DBMS_XDBRESEROUCE.GETVERSIONID (
   res   IN    XDBResource) 
 RETURN PLS_INTEGER;
```

Parameters

Table 167-23 GETVERSIONID Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASACLCHANGED Function

This function returns `TRUE` if the ACL of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASACLCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-24 GETACL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASAUTHORCHANGED Function

This function returns `TRUE` if the author of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASAUTHORCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-25 HASAUTHORCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCHANGED Function

Given an XPath, this function determines whether the element or attribute represented by the XPath has changed.

Syntax

```
DBMS_XDBRESEROUCE.HASCHANGED (
   res         IN    XDBResource, 
   xpath       IN    VARCHAR2,
   namespace   IN    VARCHAR2) 
 RETURN BOOLEAN;
```

Parameters

Table 167-26 HASCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `xpath` | XPath to check |
| `bnamespace` | Namespace to use |

---

### HASCHARACTERSETCHANGED Function

This function returns `TRUE` if the character set of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASCHARACTERSETCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-27 HASCHARACTERSETCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCOMMENTCHANGED Function

This function returns `TRUE` if the comment of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASCOMMENTCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-28 HASCOMMENTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCONTENTCHANGED Function

This function returns `TRUE` if the contents of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASCONTENTCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-29 HASCONTENTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCONTENTTYPECHANGED Function

This function returns `TRUE` if the content-type of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASCONTENTTYPECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-30 HASCONTENTTYPECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCREATIONDATECHANGED Function

This function returns `TRUE` if the creation date of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASCREATIONDATECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-31 HASCREATIONDATECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCREATORCHANGED Function

This function returns `TRUE` if the creator of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASCREATORCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-32 HASCREATORCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASCUSTOMMETADATACHANGED Function

This function checks whether the custom-metadata for a given resource has changed.

Syntax

```
DBMS_XDBRESEROUCE.HASCUSTOMMETADATACHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-33 HASCUSTOMMETADATACHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASDISPLAYNAMECHANGED Function

This function returns `TRUE` if the display name of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASDISPLAYNAMECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-34 HASDISPLAYNAMECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASLANGUAGECHANGED Function

This function returns `TRUE` if the language of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASLANGUAGECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-35 HASLANGUAGECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASLASTMODIFIERCHANGED Function

This function returns `TRUE` if the last modifier of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASLASTMODIFIERCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-36 HASLASTMODIFIERCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASMODIFICATIONDATECHANGED Function

This function returns `TRUE` if the modification date of the given resource has changed, `FALSE` otherwise

Syntax

```
DBMS_XDBRESEROUCE.HASMODIFICATIONDATECHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-37 HASMODIFICATIONDATECHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASOWNERCHANGED Function

This function returns `TRUE` if the owner of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASOWNERCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-38 HASOWNERCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASREFCOUNTCHANGED Function

This function returns `TRUE` if the reference count of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASREFCOUNTCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-39 HASREFCOUNTCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### HASVERSIONIDCHANGED Function

This function returns `TRUE` if the version ID of the given resource has changed, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.HASVERSIONIDCHANGED (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-40 HASVERSIONIDCHANGED Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### ISFOLDER Function

This function returns `TRUE` if the given resource is a folder, `FALSE` otherwise.

Syntax

```
DBMS_XDBRESEROUCE.ISFOLDER (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-41 ISFOLDER Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### ISNULL Function

This function returns `TRUE` if input resource is `NULL`.

Syntax

```
DBMS_XDBRESEROUCE.ISNULL (
   res   IN    XDBResource) 
 RETURN BOOLEAN;
```

Parameters

Table 167-42 ISNULL Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | Input resource |

---

### MAKEDOCUMENT Function

This function converts the XDBResource to a DOMDocument which can be operated on using the XMLDOM interface.

See Also:

The [DBMS\_XMLDOM](d_xmldom.md) package

Syntax

```
DBMS_XDBRESEROUCE.MAKEDOCUMENT (
   res   IN    XDBResource) 
 RETURN DBMS_XMLDOM.DOMDocument;
```

Parameters

Table 167-43 MAKEDOCUMENT Function Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### SAVE Procedure

This procedures updates the resource with any modifications.

Syntax

```
DBMS_XDBRESEROUCE.SAVE (
   res   IN    XDBResource);
```

Parameters

Table 167-44 SAVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |

---

### SETACL Procedure

This procedure sets the ACL of the given XDBResource to the path specified.

Syntax

```
DBMS_XDBRESEROUCE.SETACL (
   res      IN OUT  XDBResource, 
   ACLPath  IN      VARCHAR2);
```

Parameters

Table 167-45 SETACL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `ACLPath` | Absolute path of the new ACL |

---

### SETAUTHOR Procedure

This procedure sets the author of the given XDBResource to the specified string.

Syntax

```
DBMS_XDBRESEROUCE.SETAUTHOR (
   res     IN OUT  XDBResource, 
   author  IN      VARCHAR2);
```

Parameters

Table 167-46 SETAUTHOR Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `author` | Author |

---

### SETCHARACTERSET Procedure

This procedure sets the character set of the given XDBResource to a specified character set.

Syntax

```
DBMS_XDBRESEROUCE.SETCHARACTERSET (
   res      IN OUT  XDBResource, 
   charSet  IN      VARCHAR2);
```

Parameters

Table 167-47 SETCHARACTERSET Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |
| `charset` | New character set |

---

### SETCOMMENT Procedure

This procedure sets a comment associated with the given XDBResource.

Syntax

```
DBMS_XDBRESEROUCE.SETCOMMENT (
   res      IN OUT  XDBResource, 
   comment  IN      VARCHAR2);
```

Parameters

Table 167-48 SETCOMMENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `res` | XDBResource |