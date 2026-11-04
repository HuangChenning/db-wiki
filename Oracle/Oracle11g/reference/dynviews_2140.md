---
title: "V$RESULT_CACHE_OBJECTS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2140.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RESULT_CACHE_OBJECTS` displays all the objects (both cached results and dependencies) and their attributes.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Identifier for the cache object (also the ID of the first block) |
| `TYPE` | `VARCHAR2(10)` | Type of the cache object: |
| `STATUS` | `VARCHAR2(9)` | Status of the object: - `New` - Result is still under construction - `Published` - Result is available for use - `Bypass` - Result will be bypassed from use - `Expired` - Result has exceeded expiration time - `Invalid` - Result is no longer available for use |
| `BUCKET_NO` | `NUMBER` | Internal hash bucket for the object |
| `HASH` | `NUMBER` | Hash value for the object |
| `NAME` | `VARCHAR2(128)` | Name (for example, SQL prefix or PL/SQL function name) |
| `NAMESPACE` | `VARCHAR2(5)` | Namespace: - `SQL` - `PLSQL` |
| `CREATION_TIMESTAMP` | `DATE` | Time when the object was created |
| `CREATOR_UID` | `NUMBER` | UID that created the object |
| `DEPEND_COUNT` | `NUMBER` | Number of dependencies (`TYPE` = `Result`) or dependents (`TYPE` = `Dependency`) |
| `BLOCK_COUNT` | `NUMBER` | Total number of blocks in the cached object |
| `SCN` | `NUMBER` | Build SCN (`TYPE` = `Result`) or invalidation SCN (`TYPE` = `Dependency`) |
| `COLUMN_COUNT` | `NUMBER` | Number of columns in the cached result <sup>Foot 1</sup> |
| `PIN_COUNT` | `NUMBER` | Number of active scans on this result <sup>Footref 1</sup> |
| `SCAN_COUNT` | `NUMBER` | Total number of scans initiated on the cached result <sup>Footref 1</sup> |
| `ROW_COUNT` | `NUMBER` | Total number of rows in the cached result <sup>Footref 1</sup> |
| `ROW_SIZE_MAX` | `NUMBER` | Size of the largest row (in bytes) <sup>Footref 1</sup> |
| `ROW_SIZE_MIN` | `NUMBER` | Size of the smallest row (in bytes) <sup>Footref 1</sup> |
| `ROW_SIZE_AVG` | `NUMBER` | Average size of a row (in bytes) <sup>Footref 1</sup> |
| `BUILD_TIME` | `NUMBER` | Amount of time (in hundredths of a second) it took to build the cached result <sup>Footref 1</sup> |
| `LRU_NUMBER` | `NUMBER` | LRU list position (the smaller the value, the more recent the usage) <sup>Footref 1</sup> |
| `OBJECT_NO` | `NUMBER` | Dictionary object number of the dependency object <sup>Foot 2</sup> |
| `INVALIDATIONS` | `NUMBER` | Number of times the object has invalidated its dependents <sup>Footref 2</sup> |
| `SPACE_OVERHEAD` | `NUMBER` | Overhead (in bytes) for the result <sup>Footref 1</sup> |
| `SPACE_UNUSED` | `NUMBER` | Unused space (in bytes) for the result <sup>Footref 1</sup> |
| `CACHE_ID` | `VARCHAR2(93)` | `CacheId` for the result (object name if it's a dependency) |
| `CACHE_KEY` | `VARCHAR2(93)` | `CacheKey` for the result (object name if it's a dependency) |
| `DB_LINK` <sup>Foot 3</sup> | `VARCHAR2(3)` | Possible values: - `YES`: If the result cache object references a remote database object - `NO`: If the result cache object does not reference a remote database object |
| `CHECKSUM` <sup>Footref 3</sup> | `NUMBER` | Checksum for the result object. The checksum is computed over all the blocks in the result cache object minus the object header. |

<sup>Footnote 1</sup> These columns are only valid for `TYPE` = `Result`; otherwise, they are NULL.

<sup>Footnote 2</sup> These columns are only valid for `TYPE` = `Dependency`; otherwise, they are NULL.

<sup>Footnote 3</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)