---
title: OWA_CACHE
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/OWA_CACHE.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `OWA_CACHE` package provides an interface that enables the `PL/SQL Gateway` cache to improve the performance of PL/SQL Web applications.

**See Also:**

For more information about implementation of this package:

- [*Oracle Fusion Middleware Administrator’s Guide for Oracle HTTP Server*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=HSADM)
- [*Oracle Fusion Middleware User’s Guide for mod\_plsql*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=YPMOD)

The chapter contains the following topics:

- Constants
- Summary of OWA\_CACHE Subprograms

### OWA\_CACHE Constants

`OWA_CACHE` defines several constants to use when specifying parameter values.

- `system_level` `CONSTANT` `VARCHAR(6)` `:=` `'SYSTEM';`
- `user_level` `CONSTANT` `VARCHAR(4)` `:=` `'USER';`

### Summary of OWA\_CACHE Subprograms

This table lists the OWA\_CACHE subprograms and briefly describes them.

Table 1 OWA\_CACHE Package Subprograms

| Subprogram | Description |
| --- | --- |
| DISABLE Procedure | Disables the cache for this particular request |
| GET\_ETAG Function | Returns the tag associated with the cached content (used in the Validation technique model only) |
| GET\_LEVEL Function | Returns the caching level (used in the Validation technique model only) |
| SET\_CACHE Procedure | Sets up the cache headers for validation model cache type |
| SET\_EXPIRES Procedure | Sets up the cache headers for expires model cache type |
| SET\_NOT\_MODIFIED Procedure | Sets up the headers for a not modified cache hit (used in the Validation technique model only) |
| SET\_SURROGATE\_CONTROL Procedure | Sets up the headers for a surrogate-control header for Web cache |

### DISABLE Procedure

This procedure disables the cache for this particular request.

**Syntax**

```md
OWA_CACHE.DISABLE;
```

### GET\_ETAG Function

This function returns the tag associated with the cached content. It is used in the Validation technique only.

**Syntax**

```md
OWA_CACHE.GET_ETAG
  RETURN VARCHAR2;
```

**Return Values**

The tag for cache hit, otherwise `NULL`.

### GET\_LEVEL Function

This returns the caching level. It is used in the Validation technique model only.

**Syntax**

```md
OWA_CACHE.GET_LEVEL
  RETURN VARCHAR2;
```

**Return Values**

The caching level string (‘ `USER` ’ or ‘ `SYSTEM` ’) for cache hit, otherwise `NULL`.

### SET\_CACHE Procedure

This procedure sets up the cache headers for validation model cache type.

**Syntax**

```md
OWA_CACHE.SET_CACHE(
   p_etag        IN       VARCHAR2,
   p_level       IN       VARCHAR2);
```

**Parameters**

Table 2 *SET\_CACHE Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `p_etag` | The `etag` associated with this content |
| `p_level` | The caching level (‘ `USER'` or ‘ `SYSTEM'`). |

**Exceptions**

`VALUE_ERROR` is thrown if

- `p_etag` is greater than 55
- `p_level` is not ‘ `USER` ’ or ‘ `SYSTEM` ’

### SET\_EXPIRES Procedure

This procedure sets up the cache headers for expires model cache type.

**Syntax**

```md
OWA_CACHE.SET_EXPIRES(
   p_expires      IN       NUMBER,
   p_level        IN       VARCHAR2);
```

**Parameters**

Table 3 SET\_EXPIRES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p_expires` | The number of minutes this content is valid. |
| `p_level` | The caching level (‘ `USER'` or ‘ `SYSTEM'`). |

**Exceptions**

`VALUE_ERROR` is thrown if

- `p_expires` is negative or zero
- `p_level` is not ‘ `USER` ’ or ‘ `SYSTEM` ’
- `p_expires` is > 525600 (1 year)

### SET\_NOT\_MODIFIED Procedure

This procedure sets up the headers for a not-modified cache hit. It is used in the Validation technique only.

**Syntax**

```md
OWA_CACHE.SET_NOT_MODIFIED;
```

**Exceptions**

`VALUE_ERROR` is thrown if If the `etag` was not passed in

### SET\_SURROGATE\_CONTROL Procedure

This procedure sets the headers for a surrogate-control header for Web cache

**Syntax**

```md
OWA_CACHE.SET_SURROGATE_CONTROL(
   p_value        IN       VARCHAR2);
```

**Parameters**

Table 4 SET\_SURROGATE\_CONTROL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `p_value` | The value to be passed as the Surrogate-Control header. |

**Exceptions**

`VALUE_ERROR` is thrown if If p\_value is greater than 55 in length.