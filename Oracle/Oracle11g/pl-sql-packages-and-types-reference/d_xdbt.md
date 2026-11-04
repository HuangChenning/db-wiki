---
title: DBMS_XDBT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_xdbt.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 168 DBMS\_XDBT

The `DBMS_XDBT` package provides a convenient mechanism for administrators to set up a `CONTEXT` index on the Oracle XML DB hierarchy. The package contains procedures to create default preferences, create the index and set up automatic synchronization of the `CONTEXT` index

The `DBMS_XDBT` package also contains a set of package variables that describe the configuration settings for the index. These are intended to cover the basic customizations that installations may require, but is by no means a complete set.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

This chapter contains the following topics:

- Using DBMS\_XDBT
	- Overview
		- Security Model
		- Operational Notes
- Summary of DBMS\_XDBT Subprograms

---

## Using DBMS\_XDBT

---

### Overview

The `DBMS_XDBT` package can be used in the following fashion:

- Customize the package to set up the appropriate configuration.
- Use the DROPPREFERENCES Procedure to drop any existing index preferences
- Create new index preferences using the CREATEPREFERENCES Procedure procedure
- Create the `CONTEXT` index using the CREATEINDEX Procedure procedure
- Set up automatic synchronization of the index using the CONFIGUREAUTOSYNC Procedure

---

### Security Model

Owned by `XDB`, the `DBMS_XDBT` package must be created by `SYS` or `XDB`. The `EXECUTE` privilege is granted to `SYS` or `XDB`. Subprograms in this package are executed using the privileges of the current user.

---

### Operational Notes

The DBMS\_XDBT package can be customized by using a PL/SQL procedure or an anonymous block to set the relevant package variables, configuration settings, and then execute the procedures. A more general approach would be to introduce the appropriate customizations by modifying this package in place, or as a copy. The system must be configured to use job queues, and the jobs can be viewed through the `USER_JOBS` catalog views. This section describes the configuration settings, or package variables, available to customize the `DBMS_XDBT` package.

Table 168-1 General Indexing Settings for Customizing DBMS\_XDBT

| Parameter | Default Value | Description |
| --- | --- | --- |
| `IndexName` | `XDB$CI` | Name of the `CONTEXT` index. |
| `IndexTablespace` | `XDB$RESINFO` | Tablespace used by tables and indexes comprising the `CONTEXT` index. |
| `IndexMemory` | `128M` | Memory used by index creation and SYNC; less than or equal to the `MAX_INDEX_MEMORY` system parameter (see the `CTX_ADMIN` package). |
| `LogFile` | `'XdbCtxLog'` | The log file used for `ROWID` during indexing. The `LOG_DIRECTORY` system parameter must be set already. `NULL t` urn s off `ROWID` logging. |

Table 168-2 Filtering Settings for Customizing DBMS\_XDBT

| Parameter | Default Value | Description |
| --- | --- | --- |
| `SkipFilter_Types` | `image/%, audio/%, video/%, model/%` | List of mime types that should not be indexed. |
| `NullFilter_Types` | `text/plain, text/html, text/xml` | List of mime types that do not need to use the INSO filter. Use this for text-based documents. |
| `FilterPref` | `XDB$CI_FILTER` | Name of the filter preference. |

Table 168-3 Stoplist Settings for Customizing DBMS\_XDBT

| Parameter | Default Value | Description |
| --- | --- | --- |
| `StoplistPref` | `XDB$CI_STOPLIST` | Name of the stoplist. |
| `StopWords` | `0..9; 'a'..'z'; 'A'..'Z'` | List of stopwords, in excess of `CTXSYS.DEFAULT_STOPLIST`. |

Table 168-4 Sectioning and Section Group Settings for Customizing DBMS\_XDBT

| Parameter | Default Value | Description |
| --- | --- | --- |
| `SectionGroup` | `HTML_SECTION_GROUP` | Default sectioner. Use `PATH_SECTION_GROUP` or `AUTO_SECTION_GROUP` if repository contains mainly XML documents. |
| `SectiongroupPref` | `XDB$CI_SECTIONGROUP` | Name of the section group. |

Table 168-5 Other Index Preference Settings for Customizing DBMS\_XDBT

| Parameter | Default Value | Description |
| --- | --- | --- |
| `DatastorePref` | `XDB$CI_DATASTORE` | Name of the datastore preference |
| `StoragePref` | `XDB$CI_STORAGE` | Name of the storage preference. |
| `WordlistPref` | `XDB$CI_WORDLIST` | Name of the wordlist preference. |
| `DefaultLexerPref` | `XDB$CI_DEFAULT_LEXER` | Name of the default lexer preference. |

Table 168-6 SYNC (CONTEXT Synchronization) Settings for Customizing DBMS\_XDBT

| Parameter | Default Value | Description |
| --- | --- | --- |
| `AutoSyncPolicy` | `SYNC_BY_PENDING_COUNT` | Indicates when the index should be SYNCed. One of `SYNC_BY_PENDING_COUNT`, `SYNC_BY_TIME`, or `SYNC_BY_PENDING_COUNT_AND_TIME`. |
| `MaxPendingCount` | `2` | Maximum number of documents in the `CTX_USER_PENDING` queue before an index SYNC is triggered. Only if the `AutoSyncPolicy` is `SYNC_BY_PENDING_COUNT` or `SYNC_BY_PENDING_COUNT_AND_TIME`. |
| `CheckPendingCountInterval` | `10 minutes` | How often, in minutes, the pending queue should be checked. Only if the `AutoSyncPolicy` is `SYNC_BY_PENDING_COUNT` or `SYNC_BY_PENDING_COUNT_AND_TIME`. |
| `SyncInterval` | `60 minutes` | Indicates how often, in minutes, the index should be SYNCed. Only if the AutoSyncPolicy is `SYNC_BY_TIME` or `SYNC_BY_PENDING_COUNT_AND_TIME` |

---

## Summary of DBMS\_XDBT Subprograms

Table 168-7 DBMS\_XDBT Package Subprograms

| Subprogram | Description |
| --- | --- |
| CONFIGUREAUTOSYNC Procedure | Configures the `CONTEXT` index for automatic maintenance, SYNC |
| CREATEDATASTOREPREF Procedure | Creates a USER datastore preference for the `CONTEXT` index |
| CREATEFILTERPREF Procedure | Creates a filter preference for the `CONTEXT` index |
| CREATEINDEX Procedure | Creates the `CONTEXT` index on the XML DB hierarchy |
| CREATELEXERPREF Procedure | Creates a lexer preference for the `CONTEXT` index |
| CREATEPREFERENCES Procedure | Creates preferences required for the `CONTEXT` index on the XML DB hierarchy |
| CREATESECTIONGROUPPREF Procedure | Creates a storage preference for the `CONTEXT` index |
| CREATESTOPLISTPREF Procedure | Creates a section group for the `CONTEXT` index |
| CREATESTORAGEPREF Procedure | Creates a wordlist preference for the `CONTEXT` index |
| CREATEWORLDLISTPREF Procedure | Creates a stoplist for the `CONTEXT` index |
| DROPPREFERENCES Procedure | Drops any existing preferences |

---

### CONFIGUREAUTOSYNC Procedure

This procedure sets up jobs for automatic SYNCs of the `CONTEXT` index.

Syntax

```
DBMS_XDBT.CONFIGUREAUTOSYNC;
```

Usage Notes

- The system must be configured for job queues for automatic synchronization. The jobs can be viewed using the `USER_JOBS` catalog views
- The configuration parameter `AutoSyncPolicy` can be set to choose an appropriate synchronization policy.

The synchronization can be based on one of the following:

| Sync Basis | Description |
| --- | --- |
| `SYNC_BY_PENDING_COUNT` | The SYNC is triggered when the number of documents in the pending queue is greater than a threshold (See the `MaxPendingCount` configuration setting). The pending queue is polled at regular intervals (See the `CheckPendingCountInterval` configuration parameter) to determine if the number of documents exceeds the threshold. |
| `SYNC_BY_TIME` | The SYNC is triggered at regular intervals. (See the `SyncInterval` configuration parameter). |
| `SYNC_BY_PENDING_COUNT_AND_TIME` | A combination of both of the preceding options. |

---

### CREATEDATASTOREPREF Procedure

This procedure creates a user datastore preference for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATEDATASTOREPREF;
```

Usage Notes

- The name of the `d` atastore preference can be modified; see the `DatastorePref` configuration setting.
- The default `USER` datastore procedure also filters the incoming document. The `DBMS_XDBT` package provides a set of configuration settings that control the filtering process.
- The `SkipFilter_Types` array contains a list of regular expressions. Documents with a mime type that matches one of these expressions are not indexed. Some of the properties of the document metadata, such as author, remain unindexed.
	- The `NullFilter_Types` array contains a list of regular expressions. Documents with a mime type that matches one of these expressions are not filtered; however, they are still indexed. This is intended to be used for documents that are text-based, such as HTML, XML and plain-text.
		- All other documents use the INSO filter through the IFILTER API.

---

### CREATEFILTERPREF Procedure

This procedure creates a `NULL` filter preference for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATEFILTERPREF;
```

Usage Notes

- The name of the filter preference can be modified; see `FilterPref` configuration setting.
- The `USER` datastore procedure filters the incoming document; see CREATEDATASTOREPREF Procedure for more details.

---

### CREATEINDEX Procedure

This procedure creates the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATEINDEX;
```

Usage Notes

- The name of the index can be changed; see the `IndexName` configuration setting.
- Set the `LogFile` configuration parameter to enable `ROWID` logging during index creation.
- Set the `IndexMemory` configuration parameter to determine the amount of memory that index creation, and later SYNCs, will use.

---

### CREATELEXERPREF Procedure

This procedure creates a BASIC `lexer` preference for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATELEXERPREF;
```

Usage Notes

- The name of the `lexer` preference can be modified; see `LexerPref` configuration setting. No other configuration settings are provided.
- `MultiLexer` preferences are not supported.
- Base letter translation is turned on by default.

---

### CREATEPREFERENCES Procedure

This procedure creates a set of default preferences based on the configuration settings.

Syntax

```
DBMS_XDBT.CREATEPREFERENCES;
```

---

### CREATESECTIONGROUPPREF Procedure

This procedure creates a section group for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATESECTIONGROUPPREF;
```

Usage Notes

- The name of the section group can be changed; see the `SectiongroupPref` configuration setting.
- The HTML sectioner is used by default. No zone sections are created by default. If the vast majority of documents are XML, consider using the `AUTO_SECTION_GROUP` or the `PATH_SECTION_GROUP`; see the `SectionGroup` configuration setting.

---

### CREATESTOPLISTPREF Procedure

This procedure creates a stoplist for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATESTOPLISTPREF;
```

Usage Notes

- The name of the stoplist can be modified; see the `StoplistPref` configuration setting.
- Numbers are not indexed.
- The `StopWords` array is a configurable list of stopwords. These are meant to be stopwords in addition to the set of stopwords in `CTXSYS.DEFAULT_STOPLIST.`

---

### CREATESTORAGEPREF Procedure

This procedure creates a `BASIC_STORAGE` preference for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATESTORAGEPREF;
```

Usage Notes

- The name of the storage preference can be modified; see the `StoragePref` configuration setting.
- A tablespace can be specified for the tables and indexes comprising the `CONTEXT` index; see the `IndexTablespace` configuration setting.
- Prefix and Substring indexing are not turned on by default.
- The `I_INDEX_CLAUSE` uses key compression.

---

### CREATEWORLDLISTPREF Procedure

This procedure creates a word list preference for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.CREATEWORDLISTPREF;
```

Usage Notes

- The name of the word list preference can be modified; see the `WordlistPref` configuration setting. No other configuration settings are provided.
- `FUZZY_MATCH` and `STEMMER` attributes are set to `AUTO` (auto-language detection)

---

### DROPPREFERENCES Procedure

This procedure drops any previously created preferences for the `CONTEXT` index on the XML DB hierarchy.

Syntax

```
DBMS_XDBT.DROPPREFERENCES;
```