---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_avtune.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 37 DBMS\_AVTUNE

The `DBMS_AVTUNE` package analyzes query access levels and aggregation workloads for each auto-cache enabled analytic view (AV) and creates or drops AV auto-caches to improve the overall performance of the SQL queries on that AV.

### 37.1 DBMS\_AVTUNE Overview

This package allows you to create a cache on an existing AV. It also enables the AV for auto caching. You can also create, refresh, and remove a star cache.

Usage Notes

- It is intended that the owner of the AV is also the user calling this package. Calling this package on an AV in another schema is not supported.
- Before you use any other procedure in this package, you need to call the `AUTO_CACHE_ENABLE` procedure. After the AV is enabled, auto-tuning will continue till the AV is disabled. You can call any other procedures on an enabled AV to manually tune the AV for more fine-grained control of the performance.

### 37.2 DBMS\_AVTUNE Security Model

The `DBMS_AVTUNE` package runs under `AUTHID CURRENT_USER`. The SQL generated through use of the package is executed as the current user, and `EXECUTE` privilege on the package is granted to `PUBLIC`.

### 37.3 Summary of DBMS\_AVTUNE Subprograms

This table lists the `DBMS_AVTUNE` package subprograms and briefly describes them.

Table 37-1 DBMS\_AVTUNE Package Subprograms

| Procedure | Description |
| --- | --- |
| AUTO\_CACHE\_CREATE Procedure | This procedure creates a cache on an existing analytic view. |
| AUTO\_CACHE\_DISABLE Procedure | This procedure disables an analytic view for auto caching and removes all auto-caches. |
| AUTO\_CACHE\_ENABLE Procedure | This procedure enables analytic views for auto caching and sets auto-cache settings for analytic views. This procedure throws an error if the AV is already enabled. |
| AUTO\_CACHE\_MODIFY Procedure | This procedure modifies tuning parameters originally supplied in the enable call. |
| AUTO\_CACHE\_REFRESH Procedure | This procedure forces a refresh immediately of all auto-caches for the analytic view. |
| AUTO\_CACHE\_REMOVE Procedure | This procedure manually removes the auto-cache defined for the specified levels. |
| AUTO\_CACHE\_TUNE Procedure | This procedure forces the tuning process to run immediately for the analytic view and implement changes. |
| AUTO\_CACHE\_STAR\_DISABLE Procedure | This procedure removes the star cache on the attribute dimension `dim_name`. |
| AUTO\_CACHE\_STAR\_ENABLE Procedure | This procedure creates a star cache on the atttribute dimension `dim_name`. |
| AUTO\_CACHE\_STAR\_MODIFY Procedure | This procedure modifies the parameters specified in the enable call. |
| AUTO\_CACHE\_STAR\_REFRESH Procedure | This procedure refreshes the star cache for the attribute dimension dim\_name. |

#### 37.3.1 AUTO\_CACHE\_CREATE Procedure

This procedure creates a cache on an existing analytic view.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_CREATE (
    av_name        IN  VARCHAR2,
    level_group    IN  LEVEL_LIST,
    av_owner       IN  VARCHAR2);
```

Parameters

Table 37-2 AUTO\_CACHE\_CREATE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view. |
| `level_group` | Represents the levels to cache. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

Example

```
execute dbms_avtune.auto_cache_create('UNITS_HCUBE_AVTUNE', 
  dbms_avtune.level_list(dbms_avtune.level('PRODUCT', 'ROLLUP', 'CLASS'),
  dbms_avtune.level('TIME', 'CALENDAR', 'YEAR')));
```

#### 37.3.2 AUTO\_CACHE\_DISABLE Procedure

This procedure disables an analytic view for auto caching and removes all auto-caches.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_DISABLE (
    av_name        IN  VARCHAR2,
    av_owner       IN  VARCHAR2);
```

Parameters

Table 37-3 AUTO\_CACHE\_DISABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view to disable caching on. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.3 AUTO\_CACHE\_ENABLE Procedure

This procedure enables analytic views for auto caching and sets auto-cache settings for analytic views. This procedure throws an error if the AV is already enabled. It is not possible to update an already enabled AV using this procedure.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_ENABLE (
    av_name           IN   VARCHAR2,
    refresh_intvl     IN   NUMBER,
    num_queries       IN   NUMBER,
    avg_query_time    IN   NUMBER,
    total_cache_pct   IN   NUMBER,
    init_max_pct      IN   NUMBER,
    init_numhier      IN   NUMBER,
    init_fixed_lvls   IN   LEVEL_LIST,
    run_mode          IN   VARCHAR2,
    av_owner          IN   VARCHAR2);
```

Parameters

Table 37-4 AUTO\_CACHE\_ENABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view to enable caching on. |
| `refresh_intvl` | The number of minutes to wait between each cache refresh. The default value is 10 minutes. |
| `num_queries` | The minimum number of queries to consider for caches. The default value is 1. |
| `avg_query_time` | The average number of seconds each query should take before being considered for caches. The default value is 3. |
| `total_cache_pct` | The maximum percentage of the fact table you wish to cache. The default value is 50. |
| `init_max_pct` | The maximum percentage of the fact table for the initial cache. The default value is 1%. |
| `init_numhier` | The maximum number of hierarchies to use for each dimension in the initial cache. |
| `init_fixed_lvls` | The levels you definitely want in the initial cache. |
| `run_mode` | This parameter is not used. Always use the default value. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.4 AUTO\_CACHE\_MODIFY Procedure

This procedure modifies the tuning parameters originally supplied in the enable call. The parameters remain unchanged if `NULL` is specified.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_MODIFY (
    av_name           IN   VARCHAR2,
    refresh_intvl     IN   NUMBER,
    num_queries       IN   NUMBER,
    avg_query_time    IN   NUMBER,
    total_cache_pct   IN   NUMBER,
    av_owner          IN   VARCHAR2);
```

Parameters

Table 37-5 AUTO\_CACHE\_MODIFY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view to enable caching on. |
| `refresh_intvl` | The number of minutes to wait between each cache refresh. The default value is `10` minutes. |
| `num_queries` | The minimum number of queries to consider for caches. The default value is `1`. |
| `avg_query_time` | The average number of seconds each query should take before being considered for caches. The default value is `3`. |
| `total_cache_pct` | The maximum percentage of the fact table you wish to cache. The default value is `50`. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.5 AUTO\_CACHE\_REFRESH Procedure

This procedure forces a refresh immediately of all auto-caches for the analytic view.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_REFRESH (
    av_name           IN   VARCHAR2,
    av_owner          IN   VARCHAR2);
```

Parameters

Table 37-6 AUTO\_CACHE\_REFRESH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.6 AUTO\_CACHE\_REMOVE Procedure

This procedure manually removes the auto-cache defined for the specified levels.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_REMOVE (
    av_name        IN  VARCHAR2,
    level_group    IN  LEVEL_LIST,         
    av_owner       IN  VARCHAR2);
```

Parameters

Table 37-7 AUTO\_CACHE\_REMOVE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view. |
| `level_group` | Represents the levels to cache. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.7 AUTO\_CACHE\_TUNE Procedure

This procedure forces the tuning process to run immediately for the analytic view and implement changes.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_TUNE (
    av_name           IN   VARCHAR2,
    num_queries       IN   NUMBER,
    avg_query_time    IN   NUMBER,
    run_mode          IN   VARCHAR2,
    av_owner          IN   VARCHAR2);
```

Parameters

Table 37-8 AUTO\_CACHE\_TUNE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `av_name` | The name of the analytic view. |
| `num_queries` | The minimum number of queries to consider for caches. The default value is `1`. |
| `avg_query_time` | The average number of seconds each query should take before being considered for caches. The default value is `3`. |
| `run_mode` | The `run_mode` parameter is not used. Always use the default value. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.8 AUTO\_CACHE\_STAR\_DISABLE Procedure

This procedure removes the star cache on the attribute dimension `dim_name`.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_STAR_DISABLE (
    dim_name       IN   VARCHAR2,
    dim_owner      IN   VARCHAR2);
```

Parameters

Table 37-9 AUTO\_CACHE\_STAR\_DISABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dim_name` | The name of the attribute dimension. |
| `dim_owner` | The owner of the attribute dimension. |

#### 37.3.9 AUTO\_CACHE\_STAR\_ENABLE Procedure

This procedure creates a star cache on the atttribute dimension `dim_name`. The `av_name` can optionally be passed to qualify the attribute dimension.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_STAR_ENABLE (
    dim_name          IN   VARCHAR2,
    av_name           IN   VARCHAR2,
    refresh_intvl     IN   NUMBER,
    run_mode          IN   VARCHAR2,
    dim_owner         IN   VARCHAR2,
    av_owner          IN   VARCHAR2);
```

Parameters

Table 37-10 AUTO\_CACHE\_STAR\_ENABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dim_name` | The name of the attribute dimension. |
| `av_name` | The name of the AV to associate the star cache with, if any.  The `av_name` can optionally be specified to associate the star cache with the given AV. When this is done then the star cache will be refreshed and maintained with the AV instead of independently. |
| `refresh_intvl` | The number of minutes to wait between each cache refresh. The default value is `10` minutes. |
| `run_mode` | This parameter is not used. Always use the default value. |
| `dim_owner` | The owner of the attribute dimension. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.10 AUTO\_CACHE\_STAR\_MODIFY Procedure

This procedure modifies the parameters specified in the enable call. The parameters remain unchanged if `NULL` is specified.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_STAR_MODIFY (
    dim_name          IN   VARCHAR2,
    av_name           IN   VARCHAR2,
    refresh_intvl     IN   NUMBER,
    dim_owner         IN   VARCHAR2,
    av_owner          IN   VARCHAR2);
```

Parameters

Table 37-11 AUTO\_CACHE\_STAR\_MODIFY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dim_name` | The name of the attribute dimension. |
| `av_name` | The name of the associated analytic view. |
| `refresh_intvl` | The number of minutes to wait for each cache refresh. The default value is `10` minutes. |
| `dim_owner` | The owner of the attribute dimension. |
| `av_owner` | The owner of the AV, defaulting to the current schema. |

#### 37.3.11 AUTO\_CACHE\_STAR\_REFRESH Procedure

This procedure refreshes the star cache for the attribute dimension `dim_name`.

Syntax

```
DBMS_AVTUNE.AUTO_CACHE_STAR_REFRESH (
    dim_name       IN   VARCHAR2,
    dim_owner      IN   VARCHAR2);
```

Parameters

Table 37-12 AUTO\_CACHE\_STAR\_REFRESH Procedure Parameters

| Parameter | Description |
| --- | --- |
| `dim_name` | The name of the attribute dimension. |
| `dim_owner` | The owner of the attribute dimension. |