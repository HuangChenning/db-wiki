---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_flashback_archive_migrate.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 79 DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE

Using the `DBMS_FLASHBACK_ARCHIVE_MIGRATE` package, you can export and import the Flashback Archive base tables along with their history to another database using the Transportable Tablespaces.

Restrictions

You can use this migration package only on a non-CDB environment.

This chapter contains the following topics:

See Also:

For detailed information about `DBMS_FLASHBACK_ARCHIVE_MIGRATE`:

- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-03D1CAAE-D940-444A-8771-B1BC636D105D)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=SQLRF-GUID-049B7AE8-11E1-4110-B3E4-D117907D77AC).

### 79.1 DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE Overview

Using this package one can export and import the Flashback Archive base tables along with their history to another database using the Transportable Tablespaces.

### 79.2 DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE Security Model

The `DBMS_FLASHBACK_ARCHIVE_MIGRATE` package must be compiled on both the source and target databases as `SYS`. The source file is located at `?/rdbms/admin/crefbamig.sql`, using which the package can be created or compiled.

The export and import procedures must be executed as `SYS`. Since the package uses `DBMS_DATAPUMP`, `DBMS_LOCK`, `DBMS_SYSTEM`, `DBMS_SQL`. and `DBMS_SCHEDULER` PL/SQL packages, their Security Models are also applicable. Along with the user's FDA tables that are being exported the export function also exports the following `SYS` tables' data:
- SMON\_SCN\_TIME
- SYS\_FBA\_FA
- SYS\_FBA\_TSFA
- SYS\_FBA\_TRACKEDTABLES
- SYS\_FBA\_PARTITIONS
- SYS\_FBA\_USERS

### 79.3 DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE Operational Notes

This section describes how to use the `DBMS_FLASHBACK_ARCHIVE_MIGRATE` package.

Prerequisites

Database version >= 11.2

If database version is `11.2`, following conditions should be met:

- `shared_pool_size` >= 500M
- `streams_pool_size` >= 40M

or

- `sga_target` >= 2G

Constants

None

1. On the source database run `flashback_archive.export` to export the given Flashback Archive enabled tables, their history tables and other relevant metadata information using the transportable tablespaces.
2. Copy the transportable tablespace export dump and relevant datafiles from the source to the target database.
3. On the target database run `flashback_archive.import` to finish the import of the exported Flashback Archive enabled table and their history.

Extraneous objects

The tablespaces which host the Flashback Archive enabled tables and Flashback archive itself may have totally unrelated objects. During the export all those objects are also exported as the process uses the transportable tablespaces feature. Such extraneous objects are listed in the table `SYS_FBA_EXTRANEOUSOBJS`.

Upon successful import, the extraneous objects are left as is. DBA should drop the extraneous objects.

Self Containment of Tablespaces

Since transportable tablespaces feature is used for export and import, all the objects in those tablespaces must be self contained. Otherwise, the function aborts.

Reduction in History Granularity

After the import, it is possible to see the reduction in the granularity of the history.

For example, The multiple history generated on the source database in a small duaration of time may be coalesced into one history.

Logs

Export and import logs are available in the `OS` directory given as the input `data_pump_dir` argument.

The format of export logs is `fda_mig_expdp_YYYY_MMDD_HH24MI.log`

The format of import logs is `fda_mig_impdp_YYYY_MMDD_HH24MI.log`

Operational Notes

- After export, involved tablespaces are kept in `READONLY` mode so that the DBA can copy the involved datafiles.
- Keeping the involved tablespaces in `READONLY` mode also ensures the exported tables are in immutable state during exporting and copying of the datafiles.
- The procedures provided cannot be used for exporting and importing to change the table blocksizes. Because, internally these procedures use transportable tablespace export and import functionalities.
- After successful import, the tablespaces are again kept in `READONLY` mode. After the DBA verify the imported data, tablespaces can be made `READ-WRITE`.
- After successful import, the small tablespace that was given as input to the export operation can be dropped.

### 79.4 DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE Examples

This section illustrates exporting and importing Flashback Archive tables along with their history.

Step 1: Export the Flashback Archive enables tables along with their history

In the example, three Flashback Archive enabled tables `USR1_TAB1`, `USR1_TAB2`, and `USR1_TAB3` are exported. These tables are spread across the `FA1_TBSP`, `FA1_TBSP_1`, `USR1_TBSP`, and `USR1_TBSP_1` tablespaces.

The `TTS_TBSP` is a small tablespace that holds export related metadata.

`/some/dir/with/enough/disk/space` is the `OS` directory where data pump files and logs are created.

```
set serveroutput on;
declare
  l_fda_tabs dbms_sql.varchar2_table;
begin
  l_fda_tabs(1) := upper('usr1_tab1');
  l_fda_tabs(2) := upper('usr1_tab2');
  l_fda_tabs(3) := upper('usr1_tab3');
  flashback_archive_migrate.export
  ( schema_owner  => 'USR1'
  , fda_tables    => l_fda_tabs
  , tts           => 'TTS_TBSP'
  , data_pump_dir => '/some/dir/with/enough/disk/space'
  );
end;
/
```

On completion, the export output lists the datapump dump file and the datafiles that are to be copied to the target database to complete the import.

`Step 2`: Copy the datapump dump file and datafiles listed in the `Step 1` to the target database.

`Step 3`: Import the Flashback Archive tables along with their history

In the example, three Flashback Archive enabled tables `USR1_TAB1`, `USR1_TAB2`, and `USR1_TAB3` are imported from `FA1_TBSP`, `FA1_TBSP_1`, `USR1_TBSP`, and `USR1_TBSP_1` tablespaces spread over the data files.

For the example given, following are the data files captured in the export (`Step 1`) log file:
- `/u01/app/oracle/oradata/TGT_DB/tts_tbsp.dbf`
- `/u01/app/oracle/oradata/TGT_DB/usr1_tbsp.dbf`
- `/u01/app/oracle/oradata/TGT_DB/usr1_tbsp1.dbf`
- `/u01/app/oracle/oradata/TGT_DB/FA1_tbsp.dbf`
- `/u01/app/oracle/oradata/TGT_DB/FA1_tbsp_1.dbf`

The `TTS_TBSP` is a small tablespace that holds the export related metadata whose datafile is `/ade/nkedlaya_fda2/rdbms/dbs/tts_tbsp.dbf`.

`/some/dir/with/enough/disk/space` is the `OS` directory where data pump files are created.

```
set serveroutput on;
   declare
     l_data_files dbms_sql.varchar2_table;
   begin
     l_data_files(1) := '/u01/app/oracle/oradata/TGT_DB/tts_tbsp.dbf';
     l_data_files(2) := '/u01/app/oracle/oradata/TGT_DB/usr1_tbsp.dbf';
     l_data_files(3) := '/u01/app/oracle/oradata/TGT_DB/usr1_tbsp1.dbf';
     l_data_files(4) := '/u01/app/oracle/oradata/TGT_DB/FA1_tbsp.dbf';
     l_data_files(5) := '/u01/app/oracle/oradata/TGT_DB/FA1_tbsp_1.dbf';

     flashback_archive_migrate.import
     ( schema_owner   => 'USR1'
     , tts            => 'TTS_TBSP'
     , data_pump_dir  => '/data/pump/dir/where/export/dump/file/resides'
     , tts_data_files => l_data_files
     );
   end;
   /
```

Upon successful completion of the import, Flashback Archive is enabled on the imported tables and the prior history is available along with the new history that will be generated.

### 79.5 Summary of DBMS\_FLASHBACK Subprograms

This table lists the `DBMS_FLASHBACK_ARCHIVE_MIGRATE` subprograms and briefly describes them.

Table 79-1 DBMS\_FLASHBACK\_ARCHIVE\_MIGRATE Package Subprograms

| Subprogram | Description |
| --- | --- |
| EXPORT Procedure | This procedure exports the given Flashback Archive enabled base tables, their history, and related tablespaces. |
| EXPORT\_ANALYZE Procedure | This procedure analyzes the given Flashback Archive enabled base tables, their history, and related tablespaces for self containment using transportable tablesapce checks. |
| IMPORT Procedure | This procedure imports the Flashback Archive enabled base tables that were exported, their history, and related tablespaces. |

#### 79.5.1 EXPORT Procedure

This procedure exports the given Flashback Archive enabled base tables, their history, and related tablespaces.

Syntax

```
DBMS_FLASHBACK_ARCHIVE_MIGRATE.EXPORT (
   schema_owner        IN   VARCHAR2, 
   fda_tables          IN   DBMS_SQL.VARCHAR2, 
   tts                 IN   VARCHAR2,
   data_pump_dir       IN   VARCHAR2,
   ignore_errors       IN   BOOLEAN DEFAULT FALSE);
```

Parameters

Table 79-2 EXPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_owner` | Flashback Archive enabled tables' owner |
| `fda_tables` | Array of Flashback Archive enabled tables |
| `tts` | A small tablespace that can be used to hold the export related metadata |
| `data_pump_dir` | The directory path in the operating system where the export dump is placed |
| `ignore_errors` | Ignore any transportable tablespaces errors. The default value is `FALSE`. |

#### 79.5.2 EXPORT\_ANALYZE Procedure

This procedure analyzes the given Flashback Archive enabled base tables, their history, and related tablespaces for self containment using Transportable tablesapce checks.

Syntax

```
DBMS_FLASHBACK_ARCHIVE_MIGRATE.EXPORT_ANALYZE (
   schema_owner        IN   VARCHAR2, 
   fda_tables          IN   DBMS_SQL.VARCHAR2, 
   tts                 IN   VARCHAR2);
```

Parameters

Table 79-3 EXPORT\_ANALYZE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_owner` | Flashback Archive enabled tables' owner |
| `fda_tables` | Array of Flashback Archive enabled tables |
| `tts` | A small tablespace that can be used to hold the export related metadata |

#### 79.5.3 IMPORT Procedure

This procedure Imports the Flashback Archive enabled base tables that were exported, their history, and related tablespaces.

Syntax

```
DBMS_FLASHBACK_ARCHIVE_MIGRATE.IMPORT (
   schema_owner        IN   VARCHAR2, 
   tts                 IN   VARCHAR2,
   data_pump_dir       IN   VARCHAR2,
   tts_data_files      IN   DBMS_SQL.VARCHAR2_TABLE);
```

Parameters

Table 79-4 IMPORT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schema_owner` | Flashback Archive enabled tables' owner |
| `tts` | A small tablespace that can be used to hold the export related metadata |
| `data_pump_dir` | The directory path in the operating system where the export dump is placed |
| `tts_data_files` | The data files list of TTS exported tablespaces. |