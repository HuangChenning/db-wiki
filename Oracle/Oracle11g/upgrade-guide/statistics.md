---
title: Gathering Optimizer Statistics for Upgrading Oracle Database
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/statistics.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

## B Gathering Optimizer Statistics for Upgrading Oracle Database

Oracle provides scripts that collect optimizer statistics for dictionary objects in Oracle Database. By running these scripts before performing the actual database upgrade, you can decrease the amount of downtime incurred during the database upgrade.

This process should be tested on a test database just like any other aspect of the upgrade. Also, some schemas referenced in these scripts might not exist if some database components have not been installed.

This appendix contains the following topics:

- Collecting Statistics for System Component Schemas
- Creating a Statistics Table

## Collecting Statistics for System Component Schemas

If you are using Oracle9i Release 2 (9.2), then you should use the `DBMS_STATS.GATHER_SCHEMA_STATS` procedure to gather statistics. The following sample script uses this procedure to collect statistics for system component schemas.

To run this script, connect to the database `AS SYSDBA` using SQL\*Plus.

```
spool gdict

grant analyze any to sys;

exec dbms_stats.gather_schema_stats('WMSYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('MDSYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('CTXSYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('XDB',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('WKSYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('LBACSYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('ORDSYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('ORDPLUGINS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('SI_INFORMTN_SCHEMA',-
options=>'GATHER', estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('OUTLN',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('DBSNMP',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('SYSTEM',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

exec dbms_stats.gather_schema_stats('SYS',options=>'GATHER', -
estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE, -
method_opt => 'FOR ALL COLUMNS SIZE AUTO', cascade => TRUE);

spool off
```

Note:

The statistics collection might give errors if a particular component schema does not exist in the database. This can happen if a component is not installed or if it is invalid.

## Creating a Statistics Table

This script creates the table, `dictstattab`, and exports the statistics for the RDBMS component schemas into it. The export returns an error if a particular component schema does not exist in the database. This can happen if a component is not installed or if it is invalid.

This script is useful when you want to import the statistics back into the database. For example, the following PL/SQL subprograms import the statistics for the `SYS` schema after deleting the existing statistics:

```
EXEC DBMS_STATS.DELETE_SCHEMA_STATS('SYS');
EXEC DBMS_STATS.IMPORT_SCHEMA_STATS('SYS','dictstattab');
```

To run the following script, connect to the database `AS SYSDBA` using SQL\*Plus.

```
spool sdict

grant analyze any to sys;

exec dbms_stats.create_stat_table('SYS','dictstattab');

exec dbms_stats.export_schema_stats('WMSYS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('MDSYS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('CTXSYS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('XDB','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('WKSYS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('LBACSYS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('ORDSYS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('ORDPLUGINS','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('SI_INFORMTN_SCHEMA','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('OUTLN','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('DBSNMP','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('SYSTEM','dictstattab',statown => 'SYS');
exec dbms_stats.export_schema_stats('SYS','dictstattab',statown => 'SYS');

spool off
```