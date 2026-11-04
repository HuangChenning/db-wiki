---
title: Index
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/index.htm
tags:
  - oracle
  - 11g
  - utilities
---

A B C D E F G H I J K L M N O P Q R S T U V W X

---

## A

access privileges

ADD\_FILE parameter

ADR

ADR base

ADR home

ADRCI

ADRCI utility, [16](adrci.md)

Advanced Queuing

exporting advanced queue tables, [21.14.10](original_export.md)

importing advanced queue tables, [22.16.10](original_import.md)

aliases

directory

exporting, [21.14.5](original_export.md)

importing, [22.16.5](original_import.md)

analyzer statistics, [22.24](original_import.md)

analyzing redo log files, [19](logminer.md)

ANYDATA type

effect on table-mode Import, [22.6](original_import.md)

using SQL strings to load, [10.12.6](ldr_field_list.md)

APPEND parameter

SQL\*Loader utility, [9.14.2](ldr_control_file.md)

append to table

SQL\*Loader, [9.13.2.2.1](ldr_control_file.md)

archived LOBs

restrictions on export, [2.4.44](dp_export.md)

archiving

disabling

effect on direct path loads, [12.5.4.1](ldr_modes.md)

arrays

committing after insert, [22.7.2](original_import.md)

atomic null, [11.1.5.2](ldr_loading.md)

ATTACH parameter

Data Pump Export utility, [2.4.3](dp_export.md)

Data Pump Import utility, [3.4.3](dp_import.md)

attaching to an existing job

Data Pump Export utility, [2.4.3](dp_export.md)

attributes

null, [11.1.5.1](ldr_loading.md)

attribute-value constructors

overriding, [11.1.6](ldr_loading.md)

automatic diagnostic repository, [16.2](adrci.md)

---

## B

backslash escape character, [9.3.3.2](ldr_control_file.md)

backups

restoring dropped snapshots

Import, [22.18.2.1](original_import.md)

bad files

specifying for SQL\*Loader, [9.8](ldr_control_file.md)

BAD parameter

SQL\*Loader command line, [8.2.1](ldr_params.md)

BADFILE parameter

SQL\*Loader utility, [9.8](ldr_control_file.md)

BEGINDATA parameter

SQL\*Loader control file, [9.6](ldr_control_file.md)

BFILEs

in original Export, [21.14.6](original_export.md)

in original Import, [22.16.5](original_import.md)

loading with SQL\*Loader, [11.4](ldr_loading.md), [11.5](ldr_loading.md)

big-endian data

external tables, [14.2.8](et_params.md)

bind arrays

determining size of for SQL\*Loader, [9.16.4](ldr_control_file.md)

minimizing SQL\*Loader memory requirements, [9.16.5](ldr_control_file.md)

minimum requirements, [9.16.1](ldr_control_file.md)

size with multiple SQL\*Loader INTO TABLE statements, [9.16.6](ldr_control_file.md)

specifying maximum size, [8.2.2](ldr_params.md)

specifying number of rows, [8.2.23](ldr_params.md)

SQL\*Loader performance implications, [9.16.2](ldr_control_file.md)

BINDSIZE parameter

SQL\*Loader command line, [8.2.2](ldr_params.md), [9.16.3](ldr_control_file.md)

blanks

loading fields consisting of blanks, [10.9](ldr_field_list.md)

SQL\*Loader BLANKS parameter for field comparison, [10.5.1](ldr_field_list.md)

trailing, [10.4.5.4](ldr_field_list.md)

trimming, [10.10](ldr_field_list.md)

external tables, [14.3.2](et_params.md)

whitespace, [10.10](ldr_field_list.md)

BLANKS parameter

SQL\*Loader utility, [10.5.1](ldr_field_list.md)

BLOBs

loading with SQL\*Loader, [11.4](ldr_loading.md)

bound fillers, [10.3.1](ldr_field_list.md)

buffer cache size

and Data Pump operations involving Streams, [5.3.1](dp_perf.md)

BUFFER parameter

Export utility, [21.5.1](original_export.md)

Import utility, [22.7.1](original_import.md)

buffers

calculating for export, [21.5.1](original_export.md)

specifying with SQL\*Loader BINDSIZE parameter, [9.16.4](ldr_control_file.md)

byte order, [10.8](ldr_field_list.md)

big-endian, [10.8](ldr_field_list.md)

little-endian, [10.8](ldr_field_list.md)

specifying in SQL\*Loader control file, [10.8.1](ldr_field_list.md)

byte order marks, [10.8.2](ldr_field_list.md)

precedence

for first primary datafile, [10.8.2](ldr_field_list.md)

for LOBFILEs and SDFs, [10.8.2](ldr_field_list.md)

suppressing checks for, [10.8.2.1](ldr_field_list.md)

BYTEORDER parameter

SQL\*Loader utility, [10.8.1](ldr_field_list.md)

BYTEORDERMARK parameter

SQL\*Loader utility, [10.8.2.1](ldr_field_list.md)

---

## C

cached sequence numbers

Export, [21.14.1](original_export.md)

catalog.sql script

preparing database for Export and Import, [21.2.1](original_export.md), [22.2.1](original_import.md)

catexp.sql script

preparing database for Export and Import, [21.2.1](original_export.md), [22.2.1](original_import.md)

catldr.sql script

preparing for direct path loads, [12.4.1](ldr_modes.md)

changing a database ID, [18.3.1](dbnewid.md)

changing a database name, [18.3.3](dbnewid.md)

CHAR datatype

delimited form and SQL\*Loader, [10.4.5](ldr_field_list.md)

character fields

delimiters and SQL\*Loader, [10.4.2](ldr_field_list.md), [10.4.5](ldr_field_list.md)

determining length for SQL\*Loader, [10.4.7](ldr_field_list.md)

SQL\*Loader datatypes, [10.4.2](ldr_field_list.md)

character sets

conversion

during Export and Import, [21.12.1](original_export.md), [22.14.1](original_import.md)

eight-bit to seven-bit conversions

Export/Import, [21.12.3](original_export.md), [22.14.3](original_import.md)

identifying for external tables, [14.2.4](et_params.md)

multibyte

Export/Import, [21.12.4](original_export.md)

SQL\*Loader, [9.10.1](ldr_control_file.md)

single-byte

Export/Import, [21.12.3](original_export.md), [22.14.3](original_import.md)

SQL\*Loader control file, [9.10.5.3](ldr_control_file.md)

SQL\*Loader conversion between, [9.10](ldr_control_file.md)

Unicode, [9.10.2](ldr_control_file.md)

character strings

external tables

specifying bytes or characters, [14.2.10](et_params.md)

SQL\*Loader, [10.5.2](ldr_field_list.md)

character-length semantics, [9.10.5.4](ldr_control_file.md)

CHARACTERSET parameter

SQL\*Loader utility, [9.10.5.2](ldr_control_file.md)

check constraints

overriding disabling of, [12.8.1.2](ldr_modes.md)

CLOBs

loading with SQL\*Loader, [11.4](ldr_loading.md)

CLUSTER parameter

Data Pump Export utility, [2.4.4](dp_export.md)

Data Pump Import utility, [3.4.4](dp_import.md)

collection types supported by SQL\*Loader, [7.10.2](ldr_concepts.md)

collections, [7.10](ldr_concepts.md)

loading, [11.6](ldr_loading.md)

column array rows

specifying number of, [12.5.5](ldr_modes.md)

column objects

loading, [11.1](ldr_loading.md)

with user-defined constructors, [11.1.6](ldr_loading.md)

COLUMNARRAYROWS parameter

SQL\*Loader command line, [8.2.3](ldr_params.md)

columns

exporting LONG datatypes, [21.14.2](original_export.md)

loading REF columns, [11.3](ldr_loading.md)

naming

SQL\*Loader, [10.3](ldr_field_list.md)

objects

loading nested column objects, [11.1.3](ldr_loading.md)

stream record format, [11.1.1](ldr_loading.md)

variable record format, [11.1.2](ldr_loading.md), [11.1.2](ldr_loading.md)

reordering before Import, [22.3.1](original_import.md)

setting to a constant value with SQL\*Loader, [10.13.2](ldr_field_list.md)

setting to a unique sequence number with SQL\*Loader, [10.13.6](ldr_field_list.md)

setting to an expression value with SQL\*Loader, [10.13.3](ldr_field_list.md)

setting to null with SQL\*Loader, [10.13.2.1](ldr_field_list.md)

setting to the current date with SQL\*Loader, [10.13.5](ldr_field_list.md)

setting to the datafile record number with SQL\*Loader, [10.13.4](ldr_field_list.md)

specifying

SQL\*Loader, [10.3](ldr_field_list.md)

specifying as PIECED

SQL\*Loader, [12.4.7.1](ldr_modes.md)

using SQL\*Loader, [10.13.3](ldr_field_list.md)

comments

in Export and Import parameter files, [21.3.3](original_export.md), [22.5.2](original_import.md)

with external tables, [14.1](et_params.md), [15.1.1](et_dp_driver.md)

COMMIT parameter

Import utility, [22.7.2](original_import.md)

COMPILE parameter

Import utility, [22.7.3](original_import.md)

completion messages

Export, [21.7.4](original_export.md)

Import, [21.7.4](original_export.md)

COMPRESS parameter

Export utility, [21.5.2](original_export.md)

COMPRESSION parameter

Data Pump Export utility, [2.4.5](dp_export.md)

CONCATENATE parameter

SQL\*Loader utility, [9.12](ldr_control_file.md)

concurrent conventional path loads, [12.8.4](ldr_modes.md)

configuration

of LogMiner utility, [19.2.1](logminer.md)

CONSISTENT parameter

Export utility, [21.5.3](original_export.md)

nested tables and, [21.5.3](original_export.md)

partitioned table and, [21.5.3](original_export.md)

consolidating

extents, [21.5.2](original_export.md)

CONSTANT parameter

SQL\*Loader, [10.13.2](ldr_field_list.md)

constraints

automatic integrity and SQL\*Loader, [12.8.2.2](ldr_modes.md)

direct path load, [12.8](ldr_modes.md)

disabling referential constraints, [22.3.2](original_import.md)

enabling

after a parallel direct path load, [12.9.7](ldr_modes.md)

enforced on a direct load, [12.8.1.1](ldr_modes.md)

failed

Import, [22.10.1.1](original_import.md)

load method, [12.3.8](ldr_modes.md)

CONSTRAINTS parameter

Export utility, [21.5.4](original_export.md)

Import utility, [22.7.4](original_import.md)

constructors

attribute-value, [11.1.6](ldr_loading.md)

overriding, [11.1.6](ldr_loading.md)

user-defined, [11.1.6](ldr_loading.md)

loading column objects with, [11.1.6](ldr_loading.md)

CONTENT parameter

Data Pump Export utility, [2.4.6](dp_export.md)

Data Pump Import utility, [3.4.3](dp_import.md)

CONTINUE\_CLIENT parameter

Data Pump Export utility

interactive-command mode, [2.5.2](dp_export.md)

Data Pump Import utility

interactive-command mode, [3.5.1](dp_import.md)

CONTINUEIF parameter

SQL\*Loader utility, [9.12](ldr_control_file.md)

control files

character sets, [9.10.5.3](ldr_control_file.md)

data definition language syntax, [9.1](ldr_control_file.md)

specifying data, [9.6](ldr_control_file.md)

specifying SQL\*Loader discard file, [9.9](ldr_control_file.md)

CONTROL parameter

SQL\*Loader command line, [8.2.4](ldr_params.md)

conventional path Export

compared to direct path, [21.9](original_export.md)

conventional path loads

behavior when discontinued, [9.11.1](ldr_control_file.md)

compared to direct path loads, [12.3.7](ldr_modes.md)

concurrent, [12.9.1](ldr_modes.md)

of a single partition, [12.2](ldr_modes.md)

SQL\*Loader bind array, [9.16.2](ldr_control_file.md)

when to use, [12.2.2](ldr_modes.md)

conversion of character sets

during Export/Import, [21.12.1](original_export.md), [22.14.1](original_import.md)

effect of character set sorting on, [21.12.1.1](original_export.md), [22.14.1.1](original_import.md)

conversion of data

during direct path loads, [12.3.1](ldr_modes.md)

conversion of input characters, [9.10.5](ldr_control_file.md)

CREATE REPORT command, ADRCI utility, [16.9.1](adrci.md)

CREATE SESSION privilege

Export, [21.2.3](original_export.md), [22.2.2](original_import.md)

Import, [21.2.3](original_export.md), [22.2.2](original_import.md)

creating

incident package, [16.8.2](adrci.md)

tables

manually, before import, [22.3.1](original_import.md)

---

## D

data

conversion

direct path load, [12.3.1](ldr_modes.md)

delimiter marks in data and SQL\*Loader, [10.4.5.2](ldr_field_list.md)

distinguishing different input formats for SQL\*Loader, [9.15](ldr_control_file.md)

distinguishing different input row object subtypes, [9.15](ldr_control_file.md), [9.15.3](ldr_control_file.md)

exporting, [21.5.24](original_export.md)

generating unique values with SQL\*Loader, [10.13.6](ldr_field_list.md)

including in control files, [9.6](ldr_control_file.md)

loading data contained in the SQL\*Loader control file, [10.13.1](ldr_field_list.md)

loading in sections

SQL\*Loader, [12.4.7.1](ldr_modes.md)

loading into more than one table

SQL\*Loader, [9.15](ldr_control_file.md)

maximum length of delimited data for SQL\*Loader, [10.4.5.3](ldr_field_list.md)

moving between operating systems using SQL\*Loader, [10.7](ldr_field_list.md)

recovery

SQL\*Loader direct path load, [12.4.6](ldr_modes.md)

saving in a direct path load, [12.4.5](ldr_modes.md)

saving rows

SQL\*Loader, [12.5.3](ldr_modes.md)

unsorted

SQL\*Loader, [12.5.2.2](ldr_modes.md)

values optimized for SQL\*Loader performance, [10.13.1](ldr_field_list.md)

data fields

specifying the SQL\*Loader datatype, [10.3.2](ldr_field_list.md)

data files

specifying buffering for SQL\*Loader, [9.7](ldr_control_file.md)

specifying for SQL\*Loader, [9.5](ldr_control_file.md)

DATA parameter

SQL\*Loader command line, [8.2.5](ldr_params.md)

Data Pump Export utility

ATTACH parameter, [2.4.3](dp_export.md)

CLUSTER parameter, [2.4.4](dp_export.md)

command-line mode, [2.4](dp_export.md), [3.4](dp_import.md)

COMPRESSION parameter, [2.4.5](dp_export.md)

CONTENT parameter, [2.4.6](dp_export.md), [2.4.6](dp_export.md)

controlling resource consumption, [5.2.1](dp_perf.md)

DATA\_OPTIONS parameter, [2.4.7](dp_export.md)

dump file set, [2.1](dp_export.md)

DUMPFILE parameter, [2.4.9](dp_export.md)

encryption of SecureFiles, [2.4.10](dp_export.md)

ENCRYPTION parameter, [2.4.10](dp_export.md)

ENCRYPTION\_ALGORITHM parameter, [2.4.11](dp_export.md)

ENCRYPTION\_MODE parameter, [2.4.12](dp_export.md)

ENCRYPTION\_PASSWORD parameter, [2.4.13](dp_export.md)

ESTIMATE parameter, [2.4.14](dp_export.md)

ESTIMATE\_ONLY parameter, [2.4.15](dp_export.md)

EXCLUDE parameter, [2.4.16](dp_export.md)

excluding objects, [2.4.16](dp_export.md)

export modes, [2.2.2](dp_export.md)

FILESIZE command

interactive-command mode, [2.5.4](dp_export.md)

FILESIZE parameter, [2.4.17](dp_export.md)

filtering data that is exported

using EXCLUDE parameter, [2.4.16](dp_export.md)

using INCLUDE parameter, [2.4.22](dp_export.md)

FLASHBACK\_SCN parameter, [2.4.18](dp_export.md)

FLASHBACK\_TIME parameter, [2.4.19](dp_export.md)

FULL parameter, [2.4.20](dp_export.md)

HELP parameter

interactive-command mode, [2.5.5](dp_export.md)

INCLUDE parameter, [2.4.22](dp_export.md)

interactive-command mode, [2.5](dp_export.md)

ADD\_FILE parameter, [2.5.1](dp_export.md)

CONTINUE\_CLIENT parameter, [2.5.2](dp_export.md)

EXIT\_CLIENT parameter, [2.5.3](dp_export.md)

FILESIZE, [2.5.4](dp_export.md)

HELP parameter, [2.5.5](dp_export.md)

KILL\_JOB parameter, [2.5.6](dp_export.md)

PARALLEL parameter, [2.5.7](dp_export.md)

START\_JOB parameter, [2.5.8](dp_export.md)

STATUS parameter, [2.5.9](dp_export.md), [3.5.7](dp_import.md)

STOP\_JOB parameter, [2.5.10](dp_export.md), [3.5.8](dp_import.md)

interfaces, [2.2.1](dp_export.md)

invoking

as SYSDBA, [2.2](dp_export.md), [3.2](dp_import.md)

job names

specifying, [2.4.23](dp_export.md)

JOB\_NAME parameter, [2.4.23](dp_export.md)

LOGFILE parameter, [2.4.25](dp_export.md)

NETWORK\_LINK parameter, [2.4.27](dp_export.md)

NOLOGFILE parameter, [2.4.28](dp_export.md)

PARALLEL parameter

command-line mode, [2.4.29](dp_export.md)

interactive-command mode, [2.5.7](dp_export.md)

PARFILE parameter, [2.4.30](dp_export.md)

QUERY parameter, [2.4.31](dp_export.md)

REMAP\_DATA parameter, [2.4.32](dp_export.md)

REUSE\_DUMPFILES parameter, [2.4.33](dp_export.md)

SAMPLE parameter, [2.4.34](dp_export.md)

SCHEMAS parameter, [2.4.35](dp_export.md)

SecureFiles LOB considerations, [1.8](dp_overview.md)

SERVICE\_NAME parameter, [2.4.36](dp_export.md)

SOURCE\_EDITION parameter, [2.4.37](dp_export.md)

specifying a job name, [2.4.23](dp_export.md)

syntax diagrams, [2.7](dp_export.md)

TABLES parameter, [2.4.39](dp_export.md)

TABLESPACES parameter, [2.4.40](dp_export.md)

transparent data encryption, [2.4.13](dp_export.md)

TRANSPORT\_FULL\_CHECK parameter, [2.4.41](dp_export.md)

TRANSPORT\_TABLESPACES parameter, [2.4.42](dp_export.md)

TRANSPORTABLE parameter, [2.4.43](dp_export.md)

transportable tablespace mode

and time zone file versions, [2.2.2.5](dp_export.md)

VERSION parameter, [2.4.44](dp_export.md)

versioning, [1.7](dp_overview.md)

Data Pump Import utility

ATTACH parameter, [3.4.3](dp_import.md)

attaching to an existing job, [3.4.3](dp_import.md)

changing name of source datafile, [3.4.29](dp_import.md)

CLUSTER parameter, [3.4.4](dp_import.md)

command-line mode

NOLOGFILE parameter, [3.4.23](dp_import.md)

STATUS parameter, [3.4.39](dp_import.md)

CONTENT parameter, [3.4.5](dp_import.md)

controlling resource consumption, [5.2.1](dp_perf.md)

DATA\_OPTIONS parameter, [3.4.6](dp_import.md)

DIRECTORY parameter, [3.4.7](dp_import.md)

DUMPFILE parameter, [3.4.8](dp_import.md)

ENCRYPTION\_PASSWORD parameter, [3.4.9](dp_import.md)

ESTIMATE parameter, [3.4.10](dp_import.md)

estimating size of job, [3.4.10](dp_import.md)

EXCLUDE parameter, [3.4.11](dp_import.md)

filtering data that is imported

using EXCLUDE parameter, [3.4.11](dp_import.md)

using INCLUDE parameter, [3.4.16](dp_import.md)

FLASHBACK\_SCN parameter, [3.4.12](dp_import.md)

FLASHBACK\_TIME parameter, [3.4.13](dp_import.md)

full import mode, [3.2.2.1](dp_import.md)

FULL parameter, [3.4.14](dp_import.md)

HELP parameter

command-line mode, [3.4.15](dp_import.md)

interactive-command mode, [3.5.3](dp_import.md)

INCLUDE parameter, [3.4.16](dp_import.md)

interactive-command mode, [3.5](dp_import.md)

CONTINUE\_CLIENT parameter, [3.5.1](dp_import.md)

EXIT\_CLIENT parameter, [3.5.2](dp_import.md)

HELP parameter, [3.5.3](dp_import.md)

KILL\_JOB parameter, [3.5.4](dp_import.md)

START\_JOB parameter, [3.5.6](dp_import.md)

STOP\_JOB parameter, [3.5.8](dp_import.md)

interfaces, [3.2.1](dp_import.md)

JOB\_NAME parameter, [3.4.17](dp_import.md)

LOGFILE parameter, [3.4.19](dp_import.md)

PARALLEL parameter

command-line mode, [3.4.24](dp_import.md)

interactive-command mode, [3.5.5](dp_import.md)

PARFILE parameter, [3.4.25](dp_import.md)

PARTITION\_OPTIONS parameter, [3.4.26](dp_import.md)

QUERY parameter, [3.4.27](dp_import.md)

REMAP\_DATA parameter, [3.4.28](dp_import.md)

REMAP\_DATAFILE parameter, [3.4.29](dp_import.md)

REMAP\_SCHEMA parameter, [3.4.30](dp_import.md)

REMAP\_TABLE parameter, [3.4.31](dp_import.md)

REMAP\_TABLESPACE parameter, [3.4.32](dp_import.md)

REUSE\_DATAFILES parameter, [3.4.33](dp_import.md)

schema mode, [3.2.2.2](dp_import.md)

SCHEMAS parameter, [3.4.34](dp_import.md)

SERVICE\_NAME parameter, [3.4.35](dp_import.md)

SKIP\_UNUSABLE\_INDEXES parameter, [3.4.36](dp_import.md)

SOURCE\_EDITION parameter, [3.4.37](dp_import.md)

specifying a job name, [3.4.17](dp_import.md)

specifying dump file set to import, [3.4.8](dp_import.md)

SQLFILE parameter, [3.4.38](dp_import.md)

STREAMS\_CONFIGURATION parameter, [3.4.40](dp_import.md)

syntax diagrams, [3.7](dp_import.md)

table mode, [3.2.2.3](dp_import.md)

TABLE\_EXISTS\_ACTION parameter, [3.4.41](dp_import.md)

TABLES parameter, [3.4.42](dp_import.md)

tablespace mode, [3.2.2.4](dp_import.md)

TABLESPACES parameter, [3.4.43](dp_import.md)

TARGET\_EDITION parameter, [3.4.44](dp_import.md)

TRANSFORM parameter, [3.4.45](dp_import.md)

transparent data encryption, [3.4.9](dp_import.md)

TRANSPORT\_DATAFILES parameter, [3.4.46](dp_import.md)

TRANSPORT\_FULL\_CHECK parameter, [3.4.47](dp_import.md)

TRANSPORT\_TABLESPACES parameter, [3.4.48](dp_import.md)

TRANSPORTABLE parameter, [3.4.49](dp_import.md)

transportable tablespace mode, [3.2.2.5](dp_import.md)

and time zone file versions, [3.2.2.5](dp_import.md)

VERSION parameter, [3.4.50](dp_import.md)

versioning, [1.7](dp_overview.md)

Data Pump legacy mode, [4](dp_legacy.md)

DATA\_OPTIONS parameter

Data Pump Export utility, [2.4.7](dp_export.md)

Data Pump Import utility, [3.4.6](dp_import.md)

database ID (DBID)

changing, [18.3.1](dbnewid.md)

database identifier

changing, [18.3.1](dbnewid.md)

database migration

partitioning of, [21.17](original_export.md), [22.25](original_import.md)

database name (DBNAME)

changing, [18.3.3](dbnewid.md)

database objects

exporting LONG columns, [21.14.2](original_export.md)

databases

changing the database ID, [18.3.1](dbnewid.md)

changing the name, [18.3.3](dbnewid.md)

exporting entire, [21.5.11](original_export.md)

full import, [22.7.12](original_import.md)

privileges for exporting and importing, [21.2.3](original_export.md), [22.2.2](original_import.md)

reusing existing datafiles

Import, [22.7.7](original_import.md)

datafiles

preventing overwrite during import, [22.7.7](original_import.md)

reusing during import, [22.7.7](original_import.md)

specifying, [8.2.5](ldr_params.md)

specifying format for SQL\*Loader, [9.7](ldr_control_file.md)

DATAFILES parameter

Import utility, [22.7.6](original_import.md)

DATAPUMP\_EXP\_FULL\_DATABASE role, [1.3](dp_overview.md)

DATAPUMP\_IMP\_FULL\_DATABASE role, [1.3](dp_overview.md)

datatypes

BFILEs

in original Export, [21.14.6](original_export.md)

in original Import, [22.16.5](original_import.md)

loading with SQL\*Loader, [11.4](ldr_loading.md)

BLOBs

loading with SQL\*Loader, [11.4](ldr_loading.md)

CLOBs

loading with SQL\*Loader, [11.4](ldr_loading.md)

converting SQL\*Loader, [10.4.3](ldr_field_list.md)

describing for external table fields, [14.3.6](et_params.md)

determining character field lengths for SQL\*Loader, [10.4.7](ldr_field_list.md)

determining DATE length, [10.4.7.3](ldr_field_list.md)

identifying for external tables, [14.3.4](et_params.md)

native

conflicting length specifications in SQL\*Loader, [10.4.2.9](ldr_field_list.md)

NCLOBs

loading with SQL\*Loader, [11.4](ldr_loading.md)

nonscalar, [11.1.5](ldr_loading.md)

specifying in SQL\*Loader, [10.3.2](ldr_field_list.md)

supported by the LogMiner utility, [19.13.1](logminer.md)

types used by SQL\*Loader, [10.4](ldr_field_list.md)

unsupported by LogMiner utility, [19.13.2](logminer.md)

date cache feature

DATE\_CACHE parameter, [8.2.6](ldr_params.md)

external tables, [14.7](et_params.md)

SQL\*Loader, [12.5.6](ldr_modes.md)

DATE datatype

delimited form and SQL\*Loader, [10.4.5](ldr_field_list.md)

determining length, [10.4.7.3](ldr_field_list.md)

mask

SQL\*Loader, [10.4.7.3](ldr_field_list.md)

DATE\_CACHE parameter

SQL\*Loader utility, [8.2.6](ldr_params.md)

DBID (database identifier)

changing, [18.3.1](dbnewid.md)

DBMS\_DATAPUMP PL/SQL package, [6](dp_api.md)

DBMS\_LOGMNR PL/SQL procedure

LogMiner utility and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D PL/SQL procedure

LogMiner utility and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D.ADD\_LOGFILES PL/SQL procedure

LogMiner utility and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D.BUILD PL/SQL procedure

LogMiner utility and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D.END\_LOGMNR PL/SQL procedure

LogMiner utility and, [19.2.2](logminer.md)

DBMS\_LOGMNR.ADD\_LOGFILE PL/SQL procedure

ADDFILE option, [19.3.2](logminer.md)

NEW option, [19.3.2](logminer.md)

DBMS\_LOGMNR.COLUMN\_PRESENT function, [19.5.2](logminer.md)

DBMS\_LOGMNR.MINE\_VALUE function, [19.5.2](logminer.md)

null values and, [19.5.2.1](logminer.md)

DBMS\_LOGMNR.START\_LOGMNR PL/SQL procedure, [19.4](logminer.md)

calling multiple times, [19.8](logminer.md)

COMMITTED\_DATA\_ONLY option, [19.6.1](logminer.md)

CONTINUOUS\_MINE option, [19.3.2](logminer.md)

ENDTIME parameter, [19.6.3](logminer.md), [19.6.4](logminer.md)

LogMiner utility and, [19.2.2](logminer.md)

options for, [19.4](logminer.md)

PRINT\_PRETTY\_SQL option, [19.6.6](logminer.md)

SKIP\_CORRUPTION option, [19.6.2](logminer.md)

STARTTIME parameter, [19.6.3](logminer.md), [19.6.4](logminer.md)

DBMS\_METADATA PL/SQL package, [20.3.1](metadata_api.md)

DBNAME

changing, [18.3.3](dbnewid.md)

DBNEWID utility, [18](dbnewid.md)

changing a database ID, [18.3.1](dbnewid.md)

changing a database name, [18.3.3](dbnewid.md)

effect on global database names, [18.2.1](dbnewid.md)

restrictions, [18.4.2](dbnewid.md)

syntax, [18.4](dbnewid.md)

troubleshooting a database ID change, [18.3.4](dbnewid.md)

DBVERIFY utility

output, [17.1.3](dbverify.md)

restrictions, [17](dbverify.md)

syntax, [17.1.1](dbverify.md)

validating a segment, [17.2](dbverify.md)

validating disk blocks, [17.1](dbverify.md)

default schema

as determined by SQL\*Loader, [9.13.1.1](ldr_control_file.md)

DEFAULTIF parameter

SQL\*Loader, [10.5](ldr_field_list.md)

DELETE ANY TABLE privilege

SQL\*Loader, [9.13.2.2.4](ldr_control_file.md)

DELETE CASCADE

effect on loading nonempty tables, [9.13.2.2.2](ldr_control_file.md)

SQL\*Loader, [9.13.2.2.4](ldr_control_file.md)

DELETE privilege

SQL\*Loader, [9.13.2.2.2](ldr_control_file.md)

delimited data

maximum length for SQL\*Loader, [10.4.5.3](ldr_field_list.md)

delimited fields

field length, [10.4.7.2](ldr_field_list.md)

delimited LOBs, [11.4.2.2.3](ldr_loading.md)

delimiters

in external tables, [14.2.3](et_params.md)

loading trailing blanks, [10.4.5.4](ldr_field_list.md)

marks in data and SQL\*Loader, [10.4.5.2](ldr_field_list.md)

specifying for external tables, [14.3.1](et_params.md)

specifying for SQL\*Loader, [9.13.5](ldr_control_file.md), [10.4.5](ldr_field_list.md)

SQL\*Loader enclosure, [10.10.2.2](ldr_field_list.md)

SQL\*Loader field specifications, [10.10.2.2](ldr_field_list.md)

termination, [10.10.2.2](ldr_field_list.md)

DESTROY parameter

Import utility, [22.7.7](original_import.md)

dictionary

requirements for LogMiner utility, [19.2.1.2](logminer.md)

dictionary version mismatch, [19.9.4](logminer.md)

DIRECT parameter

Export utility, [21.5.5](original_export.md)

direct path Export, [21.9](original_export.md), [21.10](original_export.md)

compared to conventional path, [21.9](original_export.md)

effect of EXEMPT ACCESS POLICY privilege, [21.10.1](original_export.md)

performance issues, [21.10.2](original_export.md)

restrictions, [21.10.3](original_export.md)

security considerations, [21.10.1](original_export.md)

direct path load

advantages, [12.3.4](ldr_modes.md)

behavior when discontinued, [9.11.2](ldr_control_file.md)

choosing sort order

SQL\*Loader, [12.5.2.4](ldr_modes.md)

compared to conventional path load, [12.3.7](ldr_modes.md)

concurrent, [12.9.3](ldr_modes.md), [12.9.3](ldr_modes.md)

conditions for use, [12.3.5](ldr_modes.md)

data saves, [12.4.5](ldr_modes.md), [12.5.3](ldr_modes.md)

DIRECT command-line parameter

SQL\*Loader, [12.4.2](ldr_modes.md)

dropping indexes, [12.7](ldr_modes.md)

effect of disabling archiving, [12.5.4](ldr_modes.md)

effect of PRIMARY KEY constraints, [12.9.8](ldr_modes.md)

effect of UNIQUE KEY constraints, [12.9.8](ldr_modes.md)

field defaults, [12.3.9](ldr_modes.md)

improper sorting

SQL\*Loader, [12.5.2.2](ldr_modes.md)

indexes, [12.4.3](ldr_modes.md)

instance recovery, [12.4.6](ldr_modes.md)

intersegment concurrency, [12.9.3](ldr_modes.md)

intrasegment concurrency, [12.9.3](ldr_modes.md)

location of data conversion, [12.3.1](ldr_modes.md)

media recovery, [12.4.6.1](ldr_modes.md), [12.4.6.1](ldr_modes.md)

optimizing on multiple-CPU systems, [12.6](ldr_modes.md)

partitioned load

SQL\*Loader, [12.8.4](ldr_modes.md)

performance, [12.4.3](ldr_modes.md), [12.5](ldr_modes.md)

preallocating storage, [12.5.1](ldr_modes.md)

presorting data, [12.5.2](ldr_modes.md)

recovery, [12.4.6](ldr_modes.md)

ROWS command-line parameter, [12.4.5.1](ldr_modes.md)

setting up, [12.4.1](ldr_modes.md)

specifying, [12.4.2](ldr_modes.md)

specifying number of rows to be read, [8.2.23](ldr_params.md)

SQL\*Loader data loading method, [7.9.2](ldr_concepts.md)

table insert triggers, [12.8.2](ldr_modes.md)

temporary segment storage requirements, [12.4.3.2](ldr_modes.md)

triggers, [12.8](ldr_modes.md)

using, [12.3.7](ldr_modes.md), [12.4](ldr_modes.md)

version requirements, [12.3.5](ldr_modes.md)

directory aliases

exporting, [21.14.5](original_export.md)

importing, [22.16.5](original_import.md)

directory objects

using with Data Pump

effect of Oracle ASM, [1.6.2.2](dp_overview.md)

DIRECTORY parameter

Data Pump Export utility, [2.4.8](dp_export.md)

Data Pump Import utility, [3.4.7](dp_import.md)

disabled unique indexes

loading tables with, [1.2](dp_overview.md)

discard files

SQL\*Loader, [9.9](ldr_control_file.md)

specifying a maximum, [9.9.2](ldr_control_file.md)

DISCARD parameter

SQL\*Loader command-line, [8.2.8](ldr_params.md)

discarded SQL\*Loader records, [7.7](ldr_concepts.md)

causes, [9.9.4](ldr_control_file.md)

discard file, [9.9](ldr_control_file.md)

limiting, [9.9.6](ldr_control_file.md)

DISCARDMAX parameter

SQL\*Loader command-line, [8.2.9](ldr_params.md)

discontinued loads, [9.11](ldr_control_file.md)

continuing, [9.11.5](ldr_control_file.md)

conventional path behavior, [9.11.1](ldr_control_file.md)

direct path behavior, [9.11.2](ldr_control_file.md)

dropped snapshots

Import, [22.18.2.1](original_import.md)

dump files

maximum size, [21.5.8](original_export.md)

DUMPFILE parameter

Data Pump Export utility, [2.4.9](dp_export.md)

Data Pump Import utility, [3.4.8](dp_import.md)

---

## E

EBCDIC character set

Import, [21.12.3](original_export.md), [22.14.3](original_import.md)

ECHO command, ADRCI utility, [16.9.2](adrci.md)

eight-bit character set support, [21.12.3](original_export.md), [22.14.3](original_import.md)

enclosed fields

whitespace, [10.10.6](ldr_field_list.md)

enclosure delimiters, [10.4.5](ldr_field_list.md)

SQL\*Loader, [10.10.2.2](ldr_field_list.md)

encrypted columns

in external tables, [15.1.6](et_dp_driver.md)

ENCRYPTION parameter

Data Pump Export utility, [2.4.10](dp_export.md)

ENCRYPTION\_ALGORITHM parameter

Data Pump Export utility, [2.4.11](dp_export.md)

ENCRYPTION\_MODE parameter

Data Pump Export utility, [2.4.12](dp_export.md)

ENCRYPTION\_PASSWORD parameter

Data Pump Export utility, [2.4.13](dp_export.md)

Data Pump Import utility, [3.4.9](dp_import.md)

errors

caused by tab characters in SQL\*Loader data, [10.2.1](ldr_field_list.md)

LONG data, [22.10.1.2](original_import.md)

object creation, [22.10.2.1](original_import.md)

Import parameter IGNORE, [22.7.15](original_import.md)

resource errors on import, [22.10.2.3](original_import.md)

writing to export log file, [21.5.15](original_export.md)

ERRORS parameter

SQL\*Loader command line, [8.2.10](ldr_params.md)

escape character

quoted strings and, [9.3.3.2](ldr_control_file.md)

usage in Data Pump Export, [2.4](dp_export.md)

usage in Data Pump Import, [3.4](dp_import.md)

usage in Export, [21.5.26.1](original_export.md)

usage in Import, [22.7.30](original_import.md)

ESTIMATE parameter

Data Pump Export utility, [2.4.14](dp_export.md)

Data Pump Import utility, [3.4.10](dp_import.md)

ESTIMATE\_ONLY parameter

Data Pump Export utility, [2.4.15](dp_export.md)

estimating size of job

Data Pump Export utility, [2.4.14](dp_export.md)

EVALUATE CHECK\_CONSTRAINTS clause, [12.8.1.2](ldr_modes.md)

EXCLUDE parameter

Data Pump Export utility, [2.4.16](dp_export.md)

Data Pump Import utility, [3.4.11](dp_import.md)

exit codes

Export and Import, [21.8](original_export.md), [22.9](original_import.md)

SQL\*Loader, [1.9](dp_overview.md), [8.3](ldr_params.md)

EXIT command, ADRCI utility, [16.9.3](adrci.md)

EXIT\_CLIENT parameter

Data Pump Export utility

interactive-command mode, [2.5.3](dp_export.md)

Data Pump Import utility

interactive-command mode, [3.5.2](dp_import.md)

EXP\_FULL\_DATABASE role

assigning in Export, [21.2.1](original_export.md), [22.2.1](original_import.md)

expdat.dmp

Export output file, [21.5.7](original_export.md)

Export

BUFFER parameter, [21.5.1](original_export.md)

character set conversion, [21.12.1](original_export.md), [22.14.1](original_import.md)

COMPRESS parameter, [21.5.2](original_export.md)

CONSISTENT parameter, [21.5.3](original_export.md)

CONSTRAINTS parameter, [21.5.4](original_export.md)

conventional path, [21.9](original_export.md)

creating

necessary privileges, [21.2.1](original_export.md), [22.2.1](original_import.md)

necessary views, [21.2.1](original_export.md), [22.2.1](original_import.md)

database optimizer statistics, [21.5.25](original_export.md)

DIRECT parameter, [21.5.5](original_export.md)

direct path, [21.9](original_export.md)

displaying online help, [21.5.13](original_export.md)

example sessions, [21.6](original_export.md)

full database mode, [21.6.1](original_export.md)

partition-level, [21.6.4](original_export.md)

table mode, [21.6.3](original_export.md)

user mode, [21.5.17](original_export.md), [21.6.2](original_export.md)

exit codes, [21.8](original_export.md), [22.9](original_import.md)

exporting an entire database, [21.5.11](original_export.md)

exporting indexes, [21.5.14](original_export.md)

exporting sequence numbers, [21.14.1](original_export.md)

exporting synonyms, [21.14.11](original_export.md)

exporting to another operating system, [21.5.20](original_export.md), [22.7.20](original_import.md)

FEEDBACK parameter, [21.5.6](original_export.md)

FILE parameter, [21.5.7](original_export.md)

FILESIZE parameter, [21.5.8](original_export.md)

FLASHBACK\_SCN parameter, [21.5.9](original_export.md)

FLASHBACK\_TIME parameter, [21.5.10](original_export.md)

full database mode

example, [21.6.1](original_export.md)

FULL parameter, [21.5.11](original_export.md)

GRANTS parameter, [21.5.12](original_export.md)

HELP parameter, [21.5.13](original_export.md)

INDEXES parameter, [21.5.14](original_export.md)

invoking, [21.3](original_export.md), [22.5](original_import.md)

log files

specifying, [21.5.15](original_export.md)

LOG parameter, [21.5.15](original_export.md)

logging error messages, [21.5.15](original_export.md)

LONG columns, [21.14.2](original_export.md)

OBJECT\_CONSISTENT parameter, [21.5.16](original_export.md)

online help, [21.3.5](original_export.md)

OWNER parameter, [21.5.17](original_export.md)

parameter file, [21.5.18](original_export.md)

maximum size, [21.3.3](original_export.md), [22.5.2](original_import.md)

parameter syntax, [21.5](original_export.md)

PARFILE parameter, [21.5.18](original_export.md)

partitioning a database migration, [21.17](original_export.md), [22.25](original_import.md)

QUERY parameter, [21.5.19](original_export.md)

RECORDLENGTH parameter, [21.5.20](original_export.md)

redirecting output to a log file, [21.7.1](original_export.md)

remote operation, [21.11.2](original_export.md), [22.13](original_import.md)

restrictions based on privileges, [21.2.3](original_export.md)

RESUMABLE parameter, [21.5.21](original_export.md)

RESUMABLE\_NAME parameter, [21.5.22](original_export.md)

RESUMABLE\_TIMEOUT parameter, [21.5.23](original_export.md)

ROWS parameter, [21.5.24](original_export.md)

sequence numbers, [21.14.1](original_export.md)

STATISTICS parameter, [21.5.25](original_export.md)

storage requirements, [21.2.2](original_export.md)

table mode

example session, [21.6.3](original_export.md)

table name restrictions, [21.5.26.1](original_export.md)

TABLES parameter, [21.5.26](original_export.md)

TABLESPACES parameter, [21.5.27](original_export.md)

TRANSPORT\_TABLESPACE parameter, [21.5.28](original_export.md)

TRIGGERS parameter, [21.5.29](original_export.md)

TTS\_FULL\_CHECK parameter, [21.5.30](original_export.md)

user access privileges, [21.2.3](original_export.md), [22.2.2](original_import.md)

user mode

example session, [21.5.17](original_export.md), [21.6.2](original_export.md)

specifying, [21.5.17](original_export.md)

USERID parameter, [21.5.31](original_export.md)

VOLSIZE parameter, [21.5.32](original_export.md)

export dump file

importing the entire file, [22.7.12](original_import.md)

export file

listing contents before importing, [22.7.25](original_import.md)

specifying, [21.5.7](original_export.md)

exporting

archived LOBs, [2.4.44](dp_export.md)

EXPRESSION parameter

SQL\*Loader, [10.13.3](ldr_field_list.md), [10.13.3.1](ldr_field_list.md)

extents

consolidating, [21.5.2](original_export.md)

EXTERNAL parameter

SQL\*Loader, [10.4.2.5](ldr_field_list.md)

EXTERNAL SQL\*Loader datatypes

numeric

determining len, [10.4.7](ldr_field_list.md)

external tables

access parameters, [13.1.2](et_concepts.md), [14.1](et_params.md), [15.1](et_dp_driver.md)

and encrypted columns, [15.1.6](et_dp_driver.md)

big-endian data, [14.2.8](et_params.md)

cacheing data during reads, [14.2.23](et_params.md)

column\_transforms clause, [14.1](et_params.md)

datatypes, [14.3.6](et_params.md)

date cache feature, [14.7](et_params.md)

delimiters, [14.2.3](et_params.md)

describing datatype of a field, [14.3.6](et_params.md)

field\_definitions clause, [14.1](et_params.md), [14.3](et_params.md)

fixed-length records, [14.2.1](et_params.md)

identifying character sets, [14.2.4](et_params.md)

identifying datatypes, [14.3.4](et_params.md)

improving performance when using

date cache feature, [14.7](et_params.md)

IO\_OPTIONS clause, [14.2.23](et_params.md)

little-endian data, [14.2.8](et_params.md)

opaque\_format\_spec, [13.1.2](et_concepts.md), [14.1](et_params.md), [15.1](et_dp_driver.md)

preprocessing data, [14.2.5](et_params.md)

record\_format\_info clause, [14.1](et_params.md), [14.2](et_params.md)

reserved words, [13.3](et_concepts.md), [14.8](et_params.md), [15.6](et_dp_driver.md)

restrictions, [13.3](et_concepts.md), [14.8](et_params.md)

setting a field to a default value, [14.3.7](et_params.md)

setting a field to null, [14.3.7](et_params.md)

skipping records when loading data, [14.2.15](et_params.md)

specifying delimiters, [14.3.1](et_params.md)

specifying load conditions, [14.2.11](et_params.md)

trimming blanks, [14.3.2](et_params.md)

use of SQL strings, [13.3](et_concepts.md), [14.8](et_params.md)

using comments, [14.1](et_params.md), [15.1.1](et_dp_driver.md)

variable-length records, [14.2.2](et_params.md)

EXTERNAL\_TABLE parameter

SQL\*Loader, [8.2.11](ldr_params.md)

---

## F

fatal errors

*See* nonrecoverable error messages

FEEDBACK parameter

Export utility, [21.5.6](original_export.md)

Import utility, [22.7.8](original_import.md)

field conditions

specifying for SQL\*Loader, [10.5](ldr_field_list.md)

field length

SQL\*Loader specifications, [10.10.2](ldr_field_list.md)

field location

SQL\*Loader, [10.2](ldr_field_list.md)

fields

character data length and SQL\*Loader, [10.4.7](ldr_field_list.md)

comparing to literals with SQL\*Loader, [10.5.2](ldr_field_list.md)

delimited

determining length, [10.4.7.2](ldr_field_list.md)

SQL\*Loader, [10.4.5](ldr_field_list.md)

loading all blanks, [10.9](ldr_field_list.md)

predetermined size

length, [10.4.7.1](ldr_field_list.md)

SQL\*Loader, [10.10.2.1](ldr_field_list.md)

relative positioning and SQL\*Loader, [10.10.3](ldr_field_list.md)

specifying default delimiters for SQL\*Loader, [9.13.5](ldr_control_file.md)

specifying for SQL\*Loader, [10.3](ldr_field_list.md)

SQL\*Loader delimited

specifications, [10.10.2.2](ldr_field_list.md)

FIELDS clause

SQL\*Loader, [9.13.5](ldr_control_file.md)

terminated by whitespace, [10.10.4.1](ldr_field_list.md)

file names

quotation marks and, [9.3.3.1](ldr_control_file.md)

specifying multiple SQL\*Loader, [9.5.2](ldr_control_file.md)

SQL\*Loader, [9.3](ldr_control_file.md)

SQL\*Loader bad file, [9.8](ldr_control_file.md)

FILE parameter

Export utility, [21.5.7](original_export.md)

Import utility, [22.7.9](original_import.md)

SQL\*Loader utility, [12.9.6.1](ldr_modes.md)

FILESIZE parameter

Data Pump Export utility, [2.4.17](dp_export.md)

Export utility, [21.5.8](original_export.md)

Import utility, [22.7.10](original_import.md)

FILLER field

using as argument to init\_spec, [10.3.1](ldr_field_list.md)

filtering data

using Data Pump Export utility, [2.1](dp_export.md)

using Data Pump Import utility, [3.1](dp_import.md)

filtering metadata that is imported

Data Pump Import utility, [3.4.11](dp_import.md)

finalizing

fine-grained access support

Export and Import, [22.17](original_import.md)

fixed-format records, [7.4.1](ldr_concepts.md)

fixed-length records

external tables, [14.2.1](et_params.md)

FLASHBACK\_SCN parameter

Data Pump Export utility, [2.4.18](dp_export.md)

Data Pump Import utility, [3.4.12](dp_import.md)

Export utility, [21.5.9](original_export.md)

FLASHBACK\_TIME parameter

Data Pump Export utility, [2.4.19](dp_export.md)

Data Pump Import utility, [3.4.13](dp_import.md)

Export utility, [21.5.10](original_export.md)

FLOAT EXTERNAL data values

SQL\*Loader, [10.4.2.5](ldr_field_list.md)

foreign function libraries

exporting, [21.14.3](original_export.md)

importing, [22.16.6](original_import.md), [22.16.9](original_import.md)

formats

SQL\*Loader input records and, [9.15.2](ldr_control_file.md)

formatting errors

SQL\*Loader, [9.8](ldr_control_file.md)

FROMUSER parameter

Import utility, [22.7.11](original_import.md)

full database mode

Import, [22.7.12](original_import.md)

specifying with FULL, [21.5.11](original_export.md)

full export mode

Data Pump Export utility, [2.2.2.1](dp_export.md)

FULL parameter

Data Pump Export utility, [2.4.20](dp_export.md)

Data Pump Import utility, [3.4.14](dp_import.md)

Export utility, [21.5.11](original_export.md)

Import utility, [22.7.12](original_import.md)

---

## G

globalization

SQL\*Loader, [9.10](ldr_control_file.md)

grants

exporting, [21.5.12](original_export.md)

importing, [22.7.13](original_import.md)

GRANTS parameter

Export utility, [21.5.12](original_export.md)

Import utility, [22.7.13](original_import.md)

---

## H

HELP parameter

Data Pump Export utility

command-line mode, [2.4.21](dp_export.md)

interactive-command mode, [2.5.5](dp_export.md)

Data Pump Import utility

command-line mode, [3.4.15](dp_import.md)

interactive-command mode, [3.5.3](dp_import.md)

Export utility, [21.5.13](original_export.md)

Import utility, [22.7.14](original_import.md)

hexadecimal strings

SQL\*Loader, [10.5.2](ldr_field_list.md)

homepath

HOST command, ADRCI utility, [16.9.4](adrci.md)

---

## I

IGNORE parameter

Import utility, [22.7.15](original_import.md)

IMP\_FULL\_DATABASE role

assigning in Import, [21.2.1](original_export.md), [22.2.1](original_import.md)

Import

BUFFER parameter, [22.7.1](original_import.md)

character set conversion, [21.12.1](original_export.md), [21.12.3](original_export.md), [22.14.1](original_import.md), [22.14.3](original_import.md)

COMMIT parameter, [22.7.2](original_import.md)

committing after array insert, [22.7.2](original_import.md)

COMPILE parameter, [22.7.3](original_import.md)

CONSTRAINTS parameter, [22.7.4](original_import.md)

creating

necessary privileges, [21.2.1](original_export.md), [22.2.1](original_import.md)

necessary views, [21.2.1](original_export.md), [22.2.1](original_import.md)

creating an index-creation SQL script, [22.7.17](original_import.md)

database optimizer statistics, [22.7.27](original_import.md)

DATAFILES parameter, [22.7.6](original_import.md)

DESTROY parameter, [22.7.7](original_import.md)

disabling referential constraints, [22.3.2](original_import.md), [22.3.2](original_import.md)

displaying online help, [22.7.14](original_import.md)

dropping a tablespace, [22.22](original_import.md)

errors importing database objects, [22.10.2](original_import.md)

example sessions, [22.8](original_import.md)

all tables from one user to another, [22.8.3](original_import.md)

selected tables for specific user, [22.8.1](original_import.md)

tables exported by another user, [22.8.2](original_import.md)

using partition-level Import, [22.8.4](original_import.md)

exit codes, [21.8](original_export.md), [22.9](original_import.md)

export file

importing the entire file, [22.7.12](original_import.md)

listing contents before import, [22.7.25](original_import.md)

FEEDBACK parameter, [22.7.8](original_import.md)

FILE parameter, [22.7.9](original_import.md)

FILESIZE parameter, [22.7.10](original_import.md)

FROMUSER parameter, [22.7.11](original_import.md)

FULL parameter, [22.7.12](original_import.md)

grants

specifying for import, [22.7.13](original_import.md)

GRANTS parameter, [22.7.13](original_import.md)

HELP parameter, [22.7.14](original_import.md)

IGNORE parameter, [22.7.15](original_import.md)

importing grants, [22.7.13](original_import.md)

importing objects into other schemas, [22.2.2.3](original_import.md)

importing rows, [22.7.24](original_import.md)

importing tables, [22.7.30](original_import.md)

INDEXES parameter, [22.7.16](original_import.md)

INDEXFILE parameter, [22.7.17](original_import.md)

INSERT errors, [22.10.1.2](original_import.md)

invalid data, [22.10.1.2](original_import.md)

invoking, [21.3](original_export.md), [22.5](original_import.md)

LOG parameter, [22.7.18](original_import.md)

LONG columns, [22.16.11](original_import.md), [22.16.11](original_import.md)

manually creating tables before import, [22.3.1](original_import.md)

manually ordering tables, [22.3.3](original_import.md)

NLS\_LANG environment variable, [21.12.3](original_export.md), [22.14.3](original_import.md)

object creation errors, [22.7.15](original_import.md)

online help, [21.3.5](original_export.md)

parameter file, [22.7.19](original_import.md)

maximum size, [21.3.3](original_export.md), [22.5.2](original_import.md)

parameter syntax, [22.7](original_import.md)

PARFILE parameter, [22.7.19](original_import.md)

partition-level, [22.11](original_import.md)

pattern matching of table names, [22.7.30](original_import.md)

read-only tablespaces, [22.21](original_import.md)

RECORDLENGTH parameter, [22.7.20](original_import.md)

records

specifying length, [22.7.20](original_import.md)

redirecting output to a log file, [21.7.1](original_export.md)

refresh error, [22.18.1](original_import.md)

remote operation, [21.11.2](original_export.md), [22.13](original_import.md)

reorganizing tablespace during, [22.23](original_import.md)

resource errors, [22.10.2.3](original_import.md)

restrictions

importing into own schema, [22.2.2.1](original_import.md)

RESUMABLE parameter, [22.7.21](original_import.md)

RESUMABLE\_NAME parameter, [22.7.22](original_import.md)

RESUMABLE\_TIMEOUT parameter, [22.7.23](original_import.md)

reusing existing datafiles, [22.7.7](original_import.md)

rows

specifying for import, [22.7.24](original_import.md)

ROWS parameter, [22.7.24](original_import.md)

schema objects, [22.2.2.3](original_import.md)

sequences, [22.10.2.2](original_import.md)

SHOW parameter, [22.7.25](original_import.md)

single-byte character sets, [21.12.3](original_export.md), [22.14.3](original_import.md)

SKIP\_UNUSABLE\_INDEXES parameter, [22.7.26](original_import.md)

snapshot master table, [22.18.1](original_import.md)

snapshots, [22.18](original_import.md)

restoring dropped, [22.18.2.1](original_import.md)

specifying by user, [22.7.11](original_import.md)

specifying index creation commands, [22.7.17](original_import.md)

specifying the export file, [22.7.9](original_import.md)

STATISTICS parameter, [22.7.27](original_import.md)

storage parameters

overriding, [22.20.3](original_import.md)

stored functions, [22.16.7](original_import.md)

stored procedures, [22.16.7](original_import.md)

STREAMS\_CONFIGURATION parameter, [22.7.28](original_import.md)

STREAMS\_INSTANTIATION parameter, [22.7.29](original_import.md)

system objects, [22.2.2.4](original_import.md)

table name restrictions, [2.4.39](dp_export.md), [3.4.42](dp_import.md), [22.7.30.1](original_import.md)

table objects

import order, [22.1.1](original_import.md)

table-level, [22.11](original_import.md)

TABLES parameter, [22.7.30](original_import.md)

TABLESPACES parameter, [22.7.31](original_import.md)

TOID\_NOVALIDATE parameter, [22.7.32](original_import.md)

TOUSER parameter, [22.7.33](original_import.md)

TRANSPORT\_TABLESPACE parameter, [22.7.34](original_import.md)

TTS\_OWNER parameter, [22.7.35](original_import.md)

tuning considerations, [22.26](original_import.md)

user access privileges, [21.2.3](original_export.md), [22.2.2](original_import.md)

USERID parameter, [22.7.36](original_import.md)

VOLSIZE parameter, [22.7.37](original_import.md)

incident

fault diagnosability infrastructure, [16.2](adrci.md)

packaging, [16.8](adrci.md)

incident package

fault diagnosability infrastructure, [16.2](adrci.md)

INCLUDE parameter

Data Pump Export utility, [2.4.22](dp_export.md)

Data Pump Import utility, [3.4.16](dp_import.md)

index options

SORTED INDEXES with SQL\*Loader, [9.14.1](ldr_control_file.md)

SQL\*Loader SINGLEROW parameter, [9.14.2](ldr_control_file.md)

Index Unusable state

indexes left in Index Unusable state, [9.11.3](ldr_control_file.md), [12.4.4](ldr_modes.md)

indexes

creating manually, [22.7.17](original_import.md)

direct path load

left in direct load state, [12.4.4](ldr_modes.md)

dropping

SQL\*Loader, [12.7](ldr_modes.md)

estimating storage requirements, [12.4.3.1](ldr_modes.md)

exporting, [21.5.14](original_export.md)

importing, [22.7.16](original_import.md)

index-creation commands

Import, [22.7.17](original_import.md)

left in unusable state, [9.11.3](ldr_control_file.md), [12.5.2.2](ldr_modes.md)

multiple-column

SQL\*Loader, [12.5.2.3](ldr_modes.md)

presorting data

SQL\*Loader, [12.5.2](ldr_modes.md)

skipping maintenance, [8.2.26](ldr_params.md), [12.7](ldr_modes.md)

skipping unusable, [8.2.27](ldr_params.md), [12.7](ldr_modes.md)

SQL\*Loader, [9.14](ldr_control_file.md)

state after discontinued load, [9.11.3](ldr_control_file.md)

unique, [22.7.16](original_import.md)

INDEXES parameter

Export utility, [21.5.14](original_export.md)

Import utility, [22.7.16](original_import.md)

INDEXFILE parameter

Import utility, [22.7.17](original_import.md)

INFILE parameter

SQL\*Loader utility, [9.5](ldr_control_file.md)

insert errors

Import, [22.10.1.2](original_import.md)

specifying, [8.2.10](ldr_params.md)

INSERT into table

SQL\*Loader, [9.13.2.1.1](ldr_control_file.md)

instance affinity

Export and Import, [21.13](original_export.md)

instance recovery, [12.4.6.2](ldr_modes.md)

integrity constraints

disabled during direct path load, [12.8.1.2](ldr_modes.md)

enabled during direct path load, [12.8.1.1](ldr_modes.md)

failed on Import, [22.10.1.1](original_import.md)

load method, [12.3.8](ldr_modes.md)

interactive method

Data Pump Export utility, [2.2.1](dp_export.md)

internal LOBs

loading, [11.4.1](ldr_loading.md)

interrupted loads, [9.11](ldr_control_file.md)

INTO TABLE statement

effect on bind array size, [9.16.6](ldr_control_file.md)

multiple statements with SQL\*Loader, [9.15](ldr_control_file.md)

SQL\*Loader, [9.13](ldr_control_file.md)

column names, [10.3](ldr_field_list.md)

discards, [9.9.4](ldr_control_file.md)

invalid data

Import, [22.10.1.2](original_import.md)

invoking

Export, [21.3](original_export.md), [22.5](original_import.md)

at the command line, [21.3.2](original_export.md), [22.5.1](original_import.md)

direct path, [21.10](original_export.md)

interactively, [21.3.4](original_export.md), [22.5.3](original_import.md)

with a parameter file, [21.3.3](original_export.md), [22.5.2](original_import.md)

Import, [21.3](original_export.md), [22.5](original_import.md)

as SYSDBA, [21.3.1](original_export.md), [22.5.4](original_import.md)

at the command line, [21.3.2](original_export.md), [22.5.1](original_import.md)

interactively, [21.3.4](original_export.md), [22.5.3](original_import.md)

with a parameter file, [21.3.3](original_export.md), [22.5.2](original_import.md)

IPS command, ADRCI utility, [16.9.5](adrci.md)

---

## J

JOB\_NAME parameter

Data Pump Export utility, [2.4.23](dp_export.md)

Data Pump Import utility, [3.4.17](dp_import.md)

---

## K

key values

generating with SQL\*Loader, [10.13.6](ldr_field_list.md)

KILL\_JOB parameter

Data Pump Export utility

interactive-command mode, [2.5.6](dp_export.md)

Data Pump Import utility, [3.5.4](dp_import.md)

---

## L

leading whitespace

definition, [10.10.1](ldr_field_list.md)

trimming and SQL\*Loader, [10.10.4](ldr_field_list.md)

legacy mode in Data Pump, [4](dp_legacy.md)

length indicator

determining size, [9.16.4.1](ldr_control_file.md)

length-value pair specified LOBs, [11.4.2.2.4](ldr_loading.md)

libraries

foreign function

exporting, [21.14.3](original_export.md)

importing, [22.16.6](original_import.md), [22.16.9](original_import.md)

little-endian data

external tables, [14.2.8](et_params.md)

LOAD parameter

SQL\*Loader command line, [8.2.13](ldr_params.md)

loading

collections, [11.6](ldr_loading.md)

column objects, [11.1](ldr_loading.md)

in variable record format, [11.1.2](ldr_loading.md)

with a derived subtype, [11.1.4](ldr_loading.md)

with user-defined constructors, [11.1.6](ldr_loading.md)

datafiles containing tabs

SQL\*Loader, [10.2.1](ldr_field_list.md)

external table data

skipping records, [14.2.15](et_params.md)

specifying conditions, [14.2.8](et_params.md), [14.2.20](et_params.md)

LOBs, [11.4](ldr_loading.md)

nested column objects, [11.1.3](ldr_loading.md)

object tables, [11.2](ldr_loading.md)

object tables with a subtype, [11.2.1](ldr_loading.md)

REF columns, [11.3](ldr_loading.md)

subpartitioned tables, [12.3.2](ldr_modes.md)

tables, [12.3.2](ldr_modes.md)

LOB data

in delimited fields, [11.4.1.2](ldr_loading.md)

in length-value pair fields, [11.4.1.3](ldr_loading.md)

in predetermined size fields, [11.4.1.1](ldr_loading.md)

loading with SQL\*Loader, [11.4](ldr_loading.md)

no compression during export, [21.5.2](original_export.md)

size of read buffer, [8.2.19](ldr_params.md)

types supported by SQL\*Loader, [7.10.3](ldr_concepts.md), [11.4](ldr_loading.md)

LOB data types, [7.5](ldr_concepts.md)

LOBFILEs, [7.5](ldr_concepts.md), [11.4](ldr_loading.md), [11.4.2](ldr_loading.md)

log files

after a discontinued load, [9.11.4](ldr_control_file.md)

Export, [21.5.15](original_export.md), [21.7.1](original_export.md)

Import, [21.7.1](original_export.md), [22.7.18](original_import.md)

specifying for SQL\*Loader, [8.2.14](ldr_params.md)

SQL\*Loader, [7.8](ldr_concepts.md)

LOG parameter

Export utility, [21.5.15](original_export.md)

Import utility, [22.7.18](original_import.md)

SQL\*Loader command line, [8.2.14](ldr_params.md)

LOGFILE parameter

Data Pump Export utility, [2.4.25](dp_export.md)

Data Pump Import utility, [3.4.19](dp_import.md)

logical records

consolidating multiple physical records using SQL\*Loader, [9.12](ldr_control_file.md)

LogMiner utility

accessing redo data of interest, [19.5](logminer.md)

adjusting redo log file list, [19.8](logminer.md)

analyzing output, [19.5.1](logminer.md)

configuration, [19.2.1](logminer.md)

considerations for reapplying DDL statements, [19.7](logminer.md)

current log file list

stored information about, [19.10.1](logminer.md)

DBMS\_LOGMNR PL/SQL procedure and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D PL/SQL procedure and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D.ADD\_LOGFILES PL/SQL procedure and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D.BUILD PL/SQL procedure and, [19.2.2](logminer.md)

DBMS\_LOGMNR\_D.END\_LOGMNR PL/SQL procedure and, [19.2.2](logminer.md)

DBMS\_LOGMNR.START\_LOGMNR PL/SQL procedure and, [19.2.2](logminer.md)

DDL tracking

time or SCN ranges, [19.9.6](logminer.md)

determining redo log files being analyzed, [19.3.2](logminer.md)

dictionary

purpose of, [19.2.1](logminer.md)

dictionary extracted to flat file

stored information about, [19.10](logminer.md)

dictionary options, [19.3.1](logminer.md)

flat file and, [19.3.1](logminer.md)

online catalog and, [19.3.1](logminer.md)

redo log files and, [19.3.1](logminer.md)

ending a session, [19.11.6](logminer.md)

executing reconstructed SQL, [19.6.5](logminer.md)

extracting data values from redo logs, [19.5.2](logminer.md)

filtering data by SCN, [19.6.4](logminer.md)

filtering data by time, [19.6.3](logminer.md)

formatting returned data, [19.6.6](logminer.md)

graphical user interface, [19](logminer.md)

levels of supplemental logging, [19.9](logminer.md)

LogMiner dictionary defined, [19.2.1](logminer.md)

mining a subset of data in redo log files, [19.8](logminer.md)

mining database definition for, [19.2.1](logminer.md)

operations overview, [19.2.2](logminer.md)

parameters

stored information about, [19.10](logminer.md)

redo log files

on a remote database, [19.8](logminer.md)

stored information about, [19.10](logminer.md)

requirements for dictionary, [19.2.1.2](logminer.md)

requirements for redo log files, [19.2.1.2](logminer.md)

requirements for source and mining databases, [19.2.1.2](logminer.md)

restrictions with XMLType data, [19.5.3.1](logminer.md)

sample configuration, [19.2.1.1](logminer.md)

showing committed transactions only, [19.6.1](logminer.md)

skipping corruptions, [19.6.2](logminer.md)

source database definition for, [19.2.1](logminer.md)

specifying redo log files to mine, [19.3.2](logminer.md)

automatically, [19.3.2](logminer.md)

manually, [19.3.2](logminer.md)

specifying redo logs for analysis, [19.11.3](logminer.md)

starting, [19.4](logminer.md), [19.11.4](logminer.md)

starting multiple times within a session, [19.8](logminer.md)

steps for extracting dictionary to a flat file, [19.3.1.3](logminer.md)

steps for extracting dictionary to redo log files, [19.3.1.2](logminer.md)

steps for using dictionary in online catalog, [19.3.1.1](logminer.md)

steps in a typical session, [19.11](logminer.md)

supplemental log groups, [19.9](logminer.md)

conditional, [19.9](logminer.md)

unconditional, [19.9](logminer.md)

supplemental logging, [19.9](logminer.md)

database level, [19.9.1](logminer.md)

database-level identification keys, [19.9.1.2](logminer.md)

disabling database-level, [19.9.2](logminer.md)

interactions with DDL tracking, [19.9.5](logminer.md)

log groups, [19.9](logminer.md)

minimal, [19.9.1.1](logminer.md)

stored information about, [19.10](logminer.md)

table-level identification keys, [19.9.3.1](logminer.md)

table-level log groups, [19.9.3.2](logminer.md)

user-defined log groups, [19.9.3.3](logminer.md)

support for transparent data encryption, [19.5](logminer.md)

supported database versions, [19.13.3](logminer.md)

supported datatypes, [19.13.1](logminer.md)

supported redo log file versions, [19.13.3](logminer.md)

suppressing delimiters in SQL\_REDO and SQL\_UNDO, [19.6.5](logminer.md)

table-level supplemental logging, [19.9.3](logminer.md)

tracking DDL statements, [19.9.4](logminer.md)

requirements, [19.9.4](logminer.md)

unsupported datatypes, [19.13.2](logminer.md)

using the online catalog, [19.3.1.1](logminer.md)

using to analyze redo log files, [19](logminer.md)

V$DATABASE view, [19.10](logminer.md)

V$LOGMNR\_CONTENTS view, [19.2.2](logminer.md), [19.5.1](logminer.md), [19.6](logminer.md)

V$LOGMNR\_DICTIONARY view, [19.10](logminer.md)

V$LOGMNR\_LOGS view, [19.10](logminer.md)

querying, [19.10.1](logminer.md)

V$LOGMNR\_PARAMETERS view, [19.9.6](logminer.md), [19.10](logminer.md)

views, [19.10](logminer.md)

LogMiner Viewer, [19](logminer.md)

LONG data

exporting, [21.14.2](original_export.md)

importing, [22.16.11](original_import.md)

---

## M

master tables

Oracle Data Pump API, [1.4.2](dp_overview.md)

snapshots

original Import, [22.18.1](original_import.md)

materialized views, [22.18](original_import.md)

media recovery

direct path load, [12.4.6.1](ldr_modes.md)

Metadata API

enhancing performance, [20.7](metadata_api.md)

retrieving collections, [20.5](metadata_api.md)

using to retrieve object metadata, [20.3](metadata_api.md)

missing data columns

SQL\*Loader, [9.13.6](ldr_control_file.md)

multibyte character sets

blanks with SQL\*Loader, [10.5.1](ldr_field_list.md)

SQL\*Loader, [9.10.1](ldr_control_file.md)

multiple-column indexes

SQL\*Loader, [12.5.2.3](ldr_modes.md)

multiple-CPU systems

optimizing direct path loads, [12.6](ldr_modes.md)

multiple-table load

generating unique sequence numbers using SQL\*Loader, [10.13.7](ldr_field_list.md)

SQL\*Loader control file specification, [9.15](ldr_control_file.md)

multithreading

on multiple-CPU systems, [12.6](ldr_modes.md)

MULTITHREADING parameter

SQL\*Loader command line, [8.2.15](ldr_params.md)

---

## N

named pipes

external table loads, [7.9.3](ldr_concepts.md)

native datatypes

conflicting length specifications

SQL\*Loader, [10.4.2.9](ldr_field_list.md)

NCLOBs

loading with SQL\*Loader, [11.4](ldr_loading.md)

nested column objects

loading, [11.1.3](ldr_loading.md)

nested tables

exporting, [21.14.9](original_export.md)

consistency and, [21.5.3](original_export.md)

importing, [22.16.3](original_import.md)

NETWORK\_LINK parameter

Data Pump Export utility, [2.4.27](dp_export.md)

Data Pump Import utility, [3.4.22](dp_import.md)

networks

Export and Import, [21.11](original_export.md), [22.13](original_import.md)

NLS\_LANG environment variable, [21.12.2](original_export.md), [22.14.2](original_import.md)

with Export and Import, [21.12.3](original_export.md), [22.14.3](original_import.md)

NO\_INDEX\_ERRORS parameter

SQL\*Loader command line, [8.2.16](ldr_params.md)

NOLOGFILE parameter

Data Pump Export utility, [2.4.28](dp_export.md)

Data Pump Import utility, [3.4.23](dp_import.md)

nonrecoverable error messages

Export, [21.7.3](original_export.md)

Import, [21.7.3](original_export.md)

nonscalar datatypes, [11.1.5](ldr_loading.md)

NOT NULL constraint

load method, [12.3.8](ldr_modes.md)

null data

missing columns at end of record during load, [9.13.6](ldr_control_file.md)

unspecified columns and SQL\*Loader, [10.3](ldr_field_list.md)

NULL values

objects, [11.1.5](ldr_loading.md)

NULLIF clause

SQL\*Loader, [10.5](ldr_field_list.md), [10.9](ldr_field_list.md)

NULLIF...BLANKS clause

SQL\*Loader, [10.5.1](ldr_field_list.md)

nulls

atomic, [11.1.5.2](ldr_loading.md)

attribute, [11.1.5.1](ldr_loading.md)

NUMBER datatype

SQL\*Loader, [10.4.3](ldr_field_list.md), [10.4.4](ldr_field_list.md)

numeric EXTERNAL datatypes

delimited form and SQL\*Loader, [10.4.5](ldr_field_list.md)

determining length, [10.4.7](ldr_field_list.md)

---

## O

object identifiers, [11.2](ldr_loading.md)

importing, [22.16.1](original_import.md)

object names

SQL\*Loader, [9.3](ldr_control_file.md)

object tables

loading, [11.2](ldr_loading.md), [11.2](ldr_loading.md)

with a subtype

loading, [11.2.1](ldr_loading.md)

object type definitions

exporting, [21.14.8](original_export.md)

object types supported by SQL\*Loader, [7.10.1](ldr_concepts.md)

OBJECT\_CONSISTENT parameter

Export utility, [21.5.16](original_export.md)

objects, [7.10](ldr_concepts.md)

creation errors, [22.10.2.1](original_import.md)

ignoring existing objects during import, [22.7.15](original_import.md)

import creation errors, [22.7.15](original_import.md)

loading nested column objects, [11.1.3](ldr_loading.md)

NULL values, [11.1.5](ldr_loading.md)

stream record format, [11.1.1](ldr_loading.md)

variable record format, [11.1.2](ldr_loading.md)

offline locally managed tablespaces

exporting, [21.14.4](original_export.md)

OID

*See* object identifiers

online help

Export and Import, [21.3.5](original_export.md)

opaque\_format\_spec, [13.1.2](et_concepts.md), [14.1](et_params.md), [15.1](et_dp_driver.md)

operating systems

moving data to different systems using SQL\*Loader, [10.7](ldr_field_list.md)

OPTIMAL storage parameter

used with Export/Import, [22.20.1](original_import.md)

optimizer statistics, [22.24](original_import.md)

optimizing

direct path loads, [12.5](ldr_modes.md)

SQL\*Loader input file processing, [9.7](ldr_control_file.md)

OPTIONALLY ENCLOSED BY clause

SQL\*Loader, [10.10.2.2](ldr_field_list.md)

OPTIONS parameter

for parallel loads, [9.13.3](ldr_control_file.md)

SQL\*Loader utility, [9.2.1](ldr_control_file.md)

Oracle Advanced Queuing

*See* Advanced Queuing

Oracle Automatic Storage Management (ASM)

Data Pump and, [1.6.2.2](dp_overview.md)

Oracle Data Pump

direct path loads

restrictions, [1.2.2](dp_overview.md)

master table, [1.4.2](dp_overview.md)

tuning performance, [5.2](dp_perf.md)

Oracle Data Pump API, [6](dp_api.md)

client interface, [6.1](dp_api.md)

job states, [6.1.1](dp_api.md)

monitoring job progress, [1.5.1](dp_overview.md)

ORACLE\_DATAPUMP access driver

effect of SQL ENCRYPT clause on, [15.1.6](et_dp_driver.md)

reserved words, [15](et_dp_driver.md), [15.7](et_dp_driver.md)

ORACLE\_LOADER access driver

reserved words, [14](et_params.md), [14.9](et_params.md)

OWNER parameter

Export utility, [21.5.17](original_export.md)

---

## P

packages

creating, [16.8.2](adrci.md)

padding of literal strings

SQL\*Loader, [10.5.2](ldr_field_list.md)

parallel loads, [12.9](ldr_modes.md)

restrictions on direct path, [12.9.4](ldr_modes.md)

when using PREPROCESSOR clause, [14.2.5.1](et_params.md)

PARALLEL parameter

Data Pump Export utility

command-line interface, [2.4.29](dp_export.md)

interactive-command mode, [2.5.7](dp_export.md)

Data Pump Import utility

command-line mode, [3.4.24](dp_import.md)

interactive-command mode, [3.5.5](dp_import.md)

SQL\*Loader command line, [8.2.17](ldr_params.md)

parameter files

Export, [21.5.18](original_export.md)

Export and Import

comments in, [21.3.3](original_export.md), [22.5.2](original_import.md)

maximum size, [21.3.3](original_export.md), [22.5.2](original_import.md)

Import, [22.7.19](original_import.md)

SQL\*Loader, [8.2.18](ldr_params.md)

PARFILE parameter

Data Pump Export utility, [2.4.30](dp_export.md)

Data Pump Import utility, [3.4.25](dp_import.md)

Export command line, [21.5.18](original_export.md)

Import command line, [22.7.19](original_import.md)

SQL\*Loader command line, [8.2.18](ldr_params.md)

PARTITION\_OPTIONS parameter

Data Pump Import utility, [3.4.26](dp_import.md)

partitioned loads

concurrent conventional path loads, [12.8.4](ldr_modes.md)

SQL\*Loader, [12.8.4](ldr_modes.md)

partitioned object support in SQL\*Loader, [7.11](ldr_concepts.md)

partitioned tables

export consistency and, [21.5.3](original_export.md)

exporting, [21.4.1](original_export.md)

importing, [22.8.1](original_import.md), [22.11.1](original_import.md)

loading, [12.3.2](ldr_modes.md)

partitioning a database migration, [21.17](original_export.md), [22.25](original_import.md)

advantages of, [21.17](original_export.md), [22.25](original_import.md)

disadvantages of, [21.17](original_export.md), [22.25](original_import.md)

procedure during export, [21.17.3](original_export.md), [22.25.3](original_import.md)

partition-level Export, [21.4.1](original_export.md)

example session, [21.6.4](original_export.md)

partition-level Import, [22.11](original_import.md)

specifying, [21.5.26](original_export.md)

pattern matching

table names during import, [22.7.30](original_import.md)

performance

improving when using integrity constraints, [12.8.4](ldr_modes.md)

optimizing for direct path loads, [12.5](ldr_modes.md)

optimizing reading of SQL\*Loader data files, [9.7](ldr_control_file.md)

tuning original Import, [22.26](original_import.md)

performance tuning

Oracle Data Pump, [5.2](dp_perf.md)

PIECED parameter

SQL\*Loader, [12.4.7.1](ldr_modes.md)

POSITION parameter

using with data containing tabs, [10.2.1](ldr_field_list.md)

with multiple SQL\*Loader INTO TABLE clauses, [9.15.2.1](ldr_control_file.md), [10.2](ldr_field_list.md), [10.2.2](ldr_field_list.md)

predetermined size fields

SQL\*Loader, [10.10.2.1](ldr_field_list.md)

predetermined size LOBs, [11.4.2.2.2](ldr_loading.md)

preprocessing data for external tables, [14.2.5](et_params.md)

effects of parallel processing, [14.2.5.1](et_params.md)

prerequisites

SQL\*Loader, [12.1](ldr_modes.md)

PRESERVE parameter, [9.12.2](ldr_control_file.md)

preserving

whitespace, [10.11](ldr_field_list.md)

PRIMARY KEY constraints

effect on direct path load, [12.9.8](ldr_modes.md)

primary key OIDs

example, [11.2](ldr_loading.md)

primary key REF columns, [11.3.3](ldr_loading.md), [11.3.3](ldr_loading.md)

privileges

EXEMPT ACCESS POLICY

effect on direct path export, [21.10.1](original_export.md)

required for Export and Import, [21.2.1](original_export.md), [22.2.1](original_import.md)

required for SQL\*Loader, [12.1](ldr_modes.md)

problem

fault diagnosability infrastructure, [16.2](adrci.md)

problem key

fault diagnosability infrastructure, [16.2](adrci.md)

PURGE command, ADRCI utility, [16.9.6](adrci.md)

---

## Q

QUERY parameter

Data Pump Export utility, [2.4.31](dp_export.md)

Data Pump Import utility, [3.4.27](dp_import.md)

Export utility, [21.5.19](original_export.md)

restrictions, [21.5.19.1](original_export.md)

QUIT command, ADRCI utility, [16.9.7](adrci.md)

quotation marks

escape characters and, [9.3.3.2](ldr_control_file.md)

file names and, [9.3.3.1](ldr_control_file.md)

SQL strings and, [9.3.2](ldr_control_file.md)

table names and, [2.4.39](dp_export.md), [3.4.42](dp_import.md), [21.5.26.1](original_export.md), [22.7.30.1](original_import.md)

usage in Data Pump Export, [2.4](dp_export.md)

usage in Data Pump Import, [3.4](dp_import.md)

use with database object names, [9.3.1](ldr_control_file.md)

---

## R

read-consistent export, [21.5.3](original_export.md)

read-only tablespaces

Import, [22.21](original_import.md)

READSIZE parameter

SQL\*Loader command line, [8.2.19](ldr_params.md)

effect on LOBs, [8.2.19](ldr_params.md)

maximum size, [8.2.19](ldr_params.md)

RECNUM parameter

use with SQL\*Loader SKIP parameter, [10.13.4](ldr_field_list.md)

RECORDLENGTH parameter

Export utility, [21.5.20](original_export.md)

Import utility, [22.7.20](original_import.md)

records

consolidating into a single logical record

SQL\*Loader, [9.12](ldr_control_file.md)

discarded by SQL\*Loader, [7.7](ldr_concepts.md), [9.9](ldr_control_file.md)

DISCARDMAX command-line parameter, [8.2.9](ldr_params.md)

distinguishing different formats for SQL\*Loader, [9.15.2](ldr_control_file.md)

extracting multiple logical records using SQL\*Loader, [9.15](ldr_control_file.md)

fixed format, [7.4.1](ldr_concepts.md)

missing data columns during load, [9.13.6](ldr_control_file.md)

rejected by SQL\*Loader, [7.7](ldr_concepts.md), [7.7.1.1](ldr_concepts.md), [7.7.1.2](ldr_concepts.md), [9.8](ldr_control_file.md)

setting column to record number with SQL\*Loader, [10.13.4](ldr_field_list.md)

specifying how to load, [8.2.13](ldr_params.md)

specifying length for export, [21.5.20](original_export.md)

specifying length for import, [22.7.20](original_import.md)

stream record format, [7.4.3](ldr_concepts.md)

recovery

direct path load

SQL\*Loader, [12.4.6](ldr_modes.md)

replacing rows, [9.13.2.2](ldr_control_file.md)

redo log file

LogMiner utility

versions supported, [19.13.3](logminer.md)

redo log files

analyzing, [19](logminer.md)

requirements for LogMiner utility, [19.2.1.2](logminer.md)

specifying for the LogMiner utility, [19.3.2](logminer.md)

redo logs

direct path load, [12.4.6.1](ldr_modes.md)

instance and media recovery

SQL\*Loader, [12.4.6.1](ldr_modes.md)

minimizing use during direct path loads, [12.5.4](ldr_modes.md)

saving space

direct path load, [12.5.4.2](ldr_modes.md)

REF columns, [11.3](ldr_loading.md)

loading, [11.3](ldr_loading.md)

primary key, [11.3.3](ldr_loading.md)

system-generated, [11.3.2](ldr_loading.md)

REF data

importing, [22.16.4](original_import.md)

referential integrity constraints

disabling for import, [22.3.2](original_import.md)

SQL\*Loader, [12.8](ldr_modes.md)

refresh error

snapshots

Import, [22.18.1](original_import.md)

reject files

specifying for SQL\*Loader, [9.8](ldr_control_file.md)

rejected records

SQL\*Loader, [7.7](ldr_concepts.md), [9.8](ldr_control_file.md)

relative field positioning

where a field starts and SQL\*Loader, [10.10.3](ldr_field_list.md)

with multiple SQL\*Loader INTO TABLE clauses, [9.15.1.1](ldr_control_file.md)

REMAP\_DATA parameter

Data Pump Export utility, [2.4.32](dp_export.md)

Data Pump Import utility, [3.4.28](dp_import.md)

REMAP\_DATAFILE parameter

Data Pump Import utility, [3.4.29](dp_import.md)

REMAP\_SCHEMA parameter

Data Pump Import utility, [3.4.30](dp_import.md)

REMAP\_TABLE parameter

Data Pump Import utility, [3.4.31](dp_import.md)

REMAP\_TABLESPACE parameter

Data Pump Import utility, [3.4.32](dp_import.md)

remote operation

Export/Import, [21.11.2](original_export.md), [22.13](original_import.md)

REPLACE table

replacing a table using SQL\*Loader, [9.13.2.2.2](ldr_control_file.md)

reserved words

external tables, [13.3](et_concepts.md), [14.8](et_params.md), [15.6](et_dp_driver.md)

ORACLE\_DATAPUMP access driver, [15](et_dp_driver.md), [15.7](et_dp_driver.md)

ORACLE\_LOADER access driver, [14](et_params.md), [14.9](et_params.md)

SQL\*Loader, [7.3](ldr_concepts.md)

resource consumption

controlling in Data Pump Export utility, [5.2.1](dp_perf.md)

controlling in Data Pump Import utility, [5.2.1](dp_perf.md)

resource errors

Import, [22.10.2.3](original_import.md)

RESOURCE role, [22.2.2.1](original_import.md)

restrictions

importing into another user’s schema, [22.2.2.3](original_import.md)

table names in Export parameter file, [21.5.26.1](original_export.md)

table names in Import parameter file, [2.4.39](dp_export.md), [3.4.42](dp_import.md), [22.7.30.1](original_import.md)

RESUMABLE parameter

Export utility, [21.5.21](original_export.md)

Import utility, [22.7.21](original_import.md)

SQL\*Loader utility, [8.2.20](ldr_params.md)

resumable space allocation

enabling and disabling, [8.2.20](ldr_params.md), [21.5.21](original_export.md), [22.7.21](original_import.md)

RESUMABLE\_NAME parameter

Export utility, [21.5.22](original_export.md)

Import utility, [22.7.22](original_import.md)

SQL\*Loader utility, [8.2.21](ldr_params.md)

RESUMABLE\_TIMEOUT parameter

Export utility, [21.5.23](original_export.md)

Import utility, [22.7.23](original_import.md)

SQL\*Loader utility, [8.2.22](ldr_params.md)

retrieving object metadata

using Metadata API, [20.3](metadata_api.md)

REUSE\_DATAFILES parameter

Data Pump Import utility, [3.4.33](dp_import.md)

REUSE\_DUMPFILES parameter

Data Pump Export utility, [2.4.33](dp_export.md)

roles

DATAPUMP\_EXP\_FULL\_DATABASE, [1.3](dp_overview.md)

DATAPUMP\_IMP\_FULL\_DATABASE, [1.3](dp_overview.md)

EXP\_FULL\_DATABASE, [21.2.1](original_export.md)

IMP\_FULL\_DATABASE, [22.2.1](original_import.md)

RESOURCE, [22.2.2.1](original_import.md)

rollback segments

effects of CONSISTENT Export parameter, [21.5.3](original_export.md)

row errors

Import, [22.10.1.1](original_import.md)

ROWID columns

loading with SQL\*Loader, [12.1.1](ldr_modes.md)

rows

choosing which to load using SQL\*Loader, [9.13.4](ldr_control_file.md)

exporting, [21.5.24](original_export.md)

specifying for import, [22.7.24](original_import.md)

specifying number to insert before save

SQL\*Loader, [12.4.5.1](ldr_modes.md)

updates to existing rows with SQL\*Loader, [9.13.2.2.3](ldr_control_file.md)

ROWS parameter

Export utility, [21.5.24](original_export.md)

Import utility, [22.7.24](original_import.md)

performance issues

SQL\*Loader, [12.5.3](ldr_modes.md)

SQL\*Loader command line, [8.2.23](ldr_params.md)

using to specify when data saves occur, [12.4.5.1](ldr_modes.md)

RUN command, ADRCI utility, [16.9.8](adrci.md)

---

## S

SAMPLE parameter

Data Pump Export utility, [2.4.34](dp_export.md)

schema mode export

Data Pump Export utility, [2.2.2.2](dp_export.md)

schemas

specifying for Export, [21.5.26](original_export.md)

SCHEMAS parameter

Data Pump Export utility, [2.4.35](dp_export.md)

Data Pump Import utility, [3.4.34](dp_import.md)

scientific notation for FLOAT EXTERNAL, [10.4.2.5](ldr_field_list.md)

script files

running before Export and Import, [21.2.1](original_export.md), [22.2.1](original_import.md)

SDFs

*See* secondary datafiles

secondary datafiles, [7.5](ldr_concepts.md), [11.6.2](ldr_loading.md)

SecureFiles

encryption during Data Pump export, [2.4.10](dp_export.md)

SecureFiles LOBs

export considerations, [1.8](dp_overview.md)

security considerations

direct path export, [21.10.1](original_export.md)

segments

temporary

FILE parameter in SQL\*Loader, [12.9.6.1](ldr_modes.md)

SELECT command, ADRCI utility, [16.9.9](adrci.md)

functions, [16.9.9](adrci.md)

sequence numb, [10.13.6](ldr_field_list.md)

sequence numbers

cached, [21.14.1](original_export.md)

exporting, [21.14.1](original_export.md)

for multiple tables and SQL\*Loader, [10.13.7](ldr_field_list.md)

generated by SQL\*Loader SEQUENCE clause, [10.13.6](ldr_field_list.md)

generated, not read and SQL\*Loader, [10.3](ldr_field_list.md)

SERVICE\_NAME parameter

Data Pump Export utility, [2.4.36](dp_export.md)

Data Pump Import utility, [3.4.35](dp_import.md)

SET BASE command, ADRCI utility, [16.9.10](adrci.md)

SET BROWSER command, ADRCI utility, [16.9.11](adrci.md)

SET CONTROL command, ADRCI utility, [16.9.12](adrci.md)

SET ECHO command, ADRCI utility, [16.9.13](adrci.md)

SET EDITOR command, ADRCI utility, [16.9.14](adrci.md)

SET HOMEPATH command, ADRCI utility, [16.9.15](adrci.md)

SET TERMOUT command, ADRCI utility, [16.9.16](adrci.md)

short records with missing data

SQL\*Loader, [9.13.6](ldr_control_file.md)

SHOW ALERT command, ADRCI utility, [16.9.17](adrci.md)

SHOW BASE command, ADRCI utility, [16.9.18](adrci.md)

SHOW CONTROL command, ADRCI utility, [16.9.19](adrci.md)

SHOW HM\_RUN command, ADRCI utility, [16.9.20](adrci.md)

SHOW HOMEPATH command, ADRCI utility, [16.9.21](adrci.md)

SHOW HOMES command, ADRCI utility, [16.9.22](adrci.md)

SHOW INCDIR command, ADRCI utility, [16.9.23](adrci.md)

SHOW INCIDENT command, ADRCI utility, [16.9.24](adrci.md)

SHOW parameter

Import utility, [22.7.25](original_import.md)

SHOW PROBLEM command, ADRCI utility, [16.9.25](adrci.md)

SHOW REPORT command, ADRCI utility, [16.9.26](adrci.md)

SHOW TRACEFILE command, ADRCI utility, [16.9.27](adrci.md)

SILENT parameter

SQL\*Loader command line, [8.2.24](ldr_params.md)

single-byte character sets

Export and Import, [21.12.3](original_export.md), [22.14.3](original_import.md)

SINGLEROW parameter, [9.14.2](ldr_control_file.md), [12.7](ldr_modes.md)

single-table loads

continuing, [9.11.5](ldr_control_file.md)

SKIP parameter

effect on SQL\*Loader RECNUM specification, [10.13.4](ldr_field_list.md)

SQL\*Loader command line, [8.2.25](ldr_params.md), [8.2.25](ldr_params.md)

SKIP\_INDEX\_MAINTENANCE parameter

SQL\*Loader command line, [8.2.26](ldr_params.md), [12.7](ldr_modes.md)

SKIP\_UNUSABLE\_INDEXES parameter

Import utility, [22.7.26](original_import.md)

SQL\*Loader command line, [8.2.27](ldr_params.md), [12.7](ldr_modes.md)

SKIP\_USABLE\_INDEXES parameter

Data Pump Import utility, [3.4.36](dp_import.md)

skipping index maintenance, [8.2.26](ldr_params.md), [12.7](ldr_modes.md)

skipping unusable indexes, [8.2.27](ldr_params.md), [12.7](ldr_modes.md)

snapshot log

Import, [22.18.1](original_import.md)

snapshots, [22.18.2](original_import.md)

importing, [22.18](original_import.md)

master table

Import, [22.18.1](original_import.md)

restoring dropped

Import, [22.18.2.1](original_import.md)

SORTED INDEXES clause

direct path loads, [9.14.1](ldr_control_file.md)

SQL\*Loader, [12.5.2.1](ldr_modes.md)

sorting

multiple-column indexes

SQL\*Loader, [12.5.2.3](ldr_modes.md)

optimum sort order

SQL\*Loader, [12.5.2.4](ldr_modes.md)

presorting in direct path load, [12.5.2](ldr_modes.md)

SORTED INDEXES clause

SQL\*Loader, [12.5.2.1](ldr_modes.md)

SOURCE\_EDITION parameter

Data Pump Export utility, [2.4.37](dp_export.md)

Data Pump Import utility, [3.4.37](dp_import.md)

SPOOL command, ADRCI utility, [16.9.28](adrci.md)

SQL operators

applying to fields, [10.12](ldr_field_list.md)

SQL strings

applying SQL operators to fields, [10.12](ldr_field_list.md)

quotation marks and, [9.3.2](ldr_control_file.md)

SQL\*Loader

appending rows to tables, [9.13.2.2.1](ldr_control_file.md)

BAD command-line parameter, [8.2.1](ldr_params.md)

bad file, [8.2.1](ldr_params.md)

BADFILE parameter, [9.8](ldr_control_file.md)

bind arrays and performance, [9.16.2](ldr_control_file.md)

BINDSIZE command-line parameter, [8.2.2](ldr_params.md), [9.16.3](ldr_control_file.md)

choosing which rows to load, [9.13.4](ldr_control_file.md)

COLUMNARRAYROWS command-line parameter, [8.2.3](ldr_params.md)

command-line parameters, [8.1](ldr_params.md)

continuing single-table loads, [9.11.5](ldr_control_file.md)

CONTROL command-line parameter, [8.2.4](ldr_params.md)

conventional path loads, [7.9.1](ldr_concepts.md), [12.2](ldr_modes.md)

DATA command-line parameter, [8.2.5](ldr_params.md)

data conversion, [7.6](ldr_concepts.md)

data definition language

syntax diagrams, [A](app_ldr_syntax.md)

datatype specifications, [7.6](ldr_concepts.md)

DATE\_CACHE command-line parameter, [8.2.6](ldr_params.md)

determining default schema, [9.13.1.1](ldr_control_file.md)

DIRECT command-line parameter, [12.4.2](ldr_modes.md)

direct path method, [7.9.2](ldr_concepts.md)

using date cache feature to improve performance, [12.5.6](ldr_modes.md)

DISCARD command-line parameter, [8.2.8](ldr_params.md)

discarded records, [7.7](ldr_concepts.md)

DISCARDFILE parameter, [9.9.1](ldr_control_file.md)

DISCARDMAX command-line parameter, [8.2.9](ldr_params.md)

DISCARDMAX parameter, [9.9.6](ldr_control_file.md)

DISCARDS parameter, [9.9.6](ldr_control_file.md)

errors caused by tabs, [10.2.1](ldr_field_list.md)

ERRORS command-line parameter, [8.2.10](ldr_params.md)

exclusive access, [12.8.3](ldr_modes.md)

external table loads, [7.9.3](ldr_concepts.md)

EXTERNAL\_TABLE parameter, [8.2.11](ldr_params.md)

FILE command-line parameter, [8.2.12](ldr_params.md)

file names, [9.3](ldr_control_file.md)

globalization technology, [9.10](ldr_control_file.md)

index options, [9.14](ldr_control_file.md)

inserting rows into tables, [9.13.2.1.1](ldr_control_file.md)

INTO TABLE statement, [9.13](ldr_control_file.md)

LOAD command-line parameter, [8.2.13](ldr_params.md)

load methods, [12.1](ldr_modes.md)

loading column objects, [11.1](ldr_loading.md)

loading data across different platforms, [10.7](ldr_field_list.md)

loading data contained in the control file, [10.13.1](ldr_field_list.md)

loading object tables, [11.2](ldr_loading.md)

LOG command-line parameter, [8.2.14](ldr_params.md)

log files, [7.8](ldr_concepts.md)

methods of loading data, [7.9](ldr_concepts.md)

multiple INTO TABLE statements, [9.15](ldr_control_file.md)

MULTITHREADING command-line parameter, [8.2.15](ldr_params.md)

object names, [9.3](ldr_control_file.md)

parallel data loading, [12.9](ldr_modes.md), [12.9.3](ldr_modes.md), [12.10](ldr_modes.md)

PARFILE command-line parameter, [8.2.18](ldr_params.md)

portable datatypes, [10.4.2](ldr_field_list.md)

READSIZE command-line parameter, [8.2.19](ldr_params.md)

maximum size, [8.2.19](ldr_params.md)

rejected records, [7.7](ldr_concepts.md)

replacing rows in tables, [9.13.2.2.2](ldr_control_file.md)

required privileges, [12.1](ldr_modes.md)

RESUMABLE parameter, [8.2.20](ldr_params.md)

RESUMABLE\_NAME parameter, [8.2.21](ldr_params.md)

RESUMABLE\_TIMEOUT parameter, [8.2.22](ldr_params.md)

ROWS command-line parameter, [8.2.23](ldr_params.md)

SILENT command-line parameter, [8.2.24](ldr_params.md)

SINGLEROW parameter, [9.14.2](ldr_control_file.md)

SKIP\_INDEX\_MAINTENANCE command-line parameter, [8.2.26](ldr_params.md)

SKIP\_UNUSABLE\_INDEXES command-line parameter, [8.2.27](ldr_params.md)

SORTED INDEXES during direct path loads, [9.14.1](ldr_control_file.md)

specifying columns, [10.3](ldr_field_list.md)

specifying data files, [9.5](ldr_control_file.md)

specifying field conditions, [10.5](ldr_field_list.md)

specifying fields, [10.3](ldr_field_list.md)

specifying more than one data file, [9.5.2](ldr_control_file.md)

STREAMSIZE command-line parameter, [8.2.28](ldr_params.md)

suppressing messages, [8.2.24](ldr_params.md)

USERID command-line parameter, [8.2.29](ldr_params.md)

SQL\*Loader control files

guidelines when creating, [7.3](ldr_concepts.md)

SQL\*Loader datatypes

nonportable, [10.4.1](ldr_field_list.md)

SQLFILE parameter

Data Pump Import utility, [3.4.38](dp_import.md)

START\_JOB parameter

Data Pump Export utility

interactive-command mode, [2.5.8](dp_export.md)

Data Pump Import utility

interactive-command mode, [3.5.6](dp_import.md)

starting

LogMiner utility, [19.4](logminer.md)

statistics

analyzer, [22.24](original_import.md)

database optimizer

specifying for Export, [21.5.25](original_export.md)

optimizer, [22.24](original_import.md)

specifying for Import, [22.7.27](original_import.md)

STATISTICS parameter

Export utility, [21.5.25](original_export.md)

Import utility, [22.7.27](original_import.md)

STATUS parameter

Data Pump Export utility, [2.4.38](dp_export.md)

interactive-command mode, [2.5.9](dp_export.md)

Data Pump Import utility, [3.4.39](dp_import.md)

interactive-command mode, [3.5.7](dp_import.md)

STOP\_JOB parameter

Data Pump Export utility

interactive-command mode, [2.5.10](dp_export.md)

Data Pump Import utility

interactive-command mode, [3.5.8](dp_import.md)

STORAGE parameter, [12.9.6.1.2](ldr_modes.md)

storage parameters

estimating export requirements, [21.2.2](original_export.md)

OPTIMAL parameter, [22.20.1](original_import.md)

overriding

Import, [22.20.3](original_import.md)

preallocating

direct path load, [12.5.1](ldr_modes.md)

temporary for a direct path load, [12.4.3.2](ldr_modes.md)

using with Export/Import, [22.20](original_import.md)

stored functions

importing, [22.16.7](original_import.md)

effect of COMPILE parameter, [22.16.7](original_import.md)

stored package, [22.16.7](original_import.md)

stored packages

importing, [22.16.7](original_import.md)

stored procedures

direct path load, [12.8.2.6](ldr_modes.md)

importing, [22.16.7](original_import.md)

effect of COMPILE parameter, [22.16.7](original_import.md)

stream buffer

specifying size for direct path, [12.5.5](ldr_modes.md)

stream record format, [7.4.3](ldr_concepts.md)

loading column objects in, [11.1.1](ldr_loading.md)

Streams environment in Data Pump

setting buffer cache size, [5.3.1](dp_perf.md)

STREAMS\_CONFIGURATION parameter

Data Pump Import utility, [3.4.40](dp_import.md)

Import utility, [22.7.28](original_import.md)

STREAMS\_INSTANTIATION parameter

Import utility, [22.7.29](original_import.md)

STREAMSIZE parameter

SQL\*Loader command line, [8.2.28](ldr_params.md)

string comparisons

SQL\*Loader, [10.5.2](ldr_field_list.md)

subpartitioned tables

loading, [12.3.2](ldr_modes.md)

subtypes

loading multiple, [9.15.3](ldr_control_file.md)

supplemental logging

LogMiner utility,

database-level identification keys, [19.9.1.2](logminer.md)

log groups, [19.9](logminer.md)

table-level, [19.9.3](logminer.md)

table-level identification keys, [19.9.3.1](logminer.md)

table-level log groups, [19.9.3.2](logminer.md), [19.9.3.2](logminer.md)

synonyms

exporting, [21.14.11](original_export.md)

syntax diagrams

Data Pump Export, [2.7](dp_export.md)

Data Pump Import, [3.7](dp_import.md)

SQL\*Loader, [A](app_ldr_syntax.md)

SYSDATE parameter

SQL\*Loader, [10.13.5](ldr_field_list.md)

system objects

importing, [22.2.2.4](original_import.md)

system triggers

effect on import, [22.4](original_import.md)

testing, [22.4](original_import.md)

system-generated OID REF columns, [11.3.2](ldr_loading.md)

---

## T

table names

preserving case sensitivity, [21.5.26.1](original_export.md)

TABLE\_EXISTS\_ACTION parameter

Data Pump Import utility, [3.4.41](dp_import.md)

table-level Export, [21.4.1](original_export.md)

table-level Import, [22.11](original_import.md)

table-mode Export

Data Pump Export utility, [2.2.2.3](dp_export.md)

specifying, [21.5.26](original_export.md)

table-mode Import

examples, [22.8.1](original_import.md)

tables

Advanced Queuing

exporting, [21.14.10](original_export.md)

importing, [22.16.10](original_import.md)

appending rows with SQL\*Loader, [9.13.2.2.1](ldr_control_file.md)

defining before Import, [22.3.1](original_import.md)

definitions

creating before Import, [22.3.1](original_import.md)

exclusive access during direct path loads

SQL\*Loader, [12.8.3](ldr_modes.md)

external, [13](et_concepts.md)

importing, [22.7.30](original_import.md)

insert triggers

direct path load in SQL\*Loader, [12.8.2](ldr_modes.md)

inserting rows using SQL\*Loader, [9.13.2.1.1](ldr_control_file.md)

loading data into more than one table using SQL\*Loader, [9.15](ldr_control_file.md)

loading object tables, [11.2](ldr_loading.md)

maintaining consistency during Export, [21.5.3](original_export.md)

manually ordering for Import, [22.3.3](original_import.md)

master table

Import, [22.18.1](original_import.md)

name restrictions

Export, [21.5.26.1](original_export.md)

Import, [2.4.39](dp_export.md), [3.4.42](dp_import.md), [22.7.30](original_import.md), [22.7.30.1](original_import.md)

nested

exporting, [21.14.9](original_export.md)

importing, [22.16.3](original_import.md)

objects

order of import, [22.1.1](original_import.md)

partitioned, [21.4.1](original_export.md)

replacing rows using SQL\*Loader, [9.13.2.2.2](ldr_control_file.md)

specifying for export, [21.5.26](original_export.md)

specifying table-mode Export, [21.5.26](original_export.md)

SQL\*Loader method for individual tables, [9.13.2](ldr_control_file.md)

truncating

SQL\*Loader, [9.13.2.2.4](ldr_control_file.md)

updating existing rows using SQL\*Loader, [9.13.2.2.3](ldr_control_file.md)

*See also* external tables

TABLES parameter

Data Pump Export utility, [2.4.39](dp_export.md)

Data Pump Import utility, [3.4.42](dp_import.md)

Export utility, [21.5.26](original_export.md)

Import utility, [22.7.30](original_import.md)

tablespace mode Export

Data Pump Export utility, [2.2.2.4](dp_export.md)

tablespaces

dropping during import, [22.22](original_import.md)

exporting a set of, [21.15](original_export.md), [22.19](original_import.md)

metadata

transporting, [22.7.34](original_import.md)

read-only

Import, [22.21](original_import.md)

reorganizing

Import, [22.23](original_import.md)

TABLESPACES parameter

Data Pump Export utility, [2.4.40](dp_export.md)

Data Pump Import utility, [3.4.43](dp_import.md)

Export utility, [21.5.27](original_export.md)

Import utility, [22.7.31](original_import.md)

tabs

loading datafiles containing tabs, [10.2.1](ldr_field_list.md)

trimming, [10.10](ldr_field_list.md)

whitespace, [10.10](ldr_field_list.md)

TARGET\_EDITION parameter

Data Pump Import utility, [3.4.44](dp_import.md)

temporary segments, [12.9.6.1](ldr_modes.md)

FILE parameter

SQL\*Loader, [12.9.6.1](ldr_modes.md)

temporary storage in a direct path load, [12.4.3.2](ldr_modes.md)

TERMINATED BY clause

with OPTIONALLY ENCLOSED BY, [10.10.2.2](ldr_field_list.md)

terminated fields

specified with a delimiter, [10.10.2.2](ldr_field_list.md)

time zone file versions

Data Pump Export, [2.2.2.5](dp_export.md)

Data Pump Import, [3.2.2.5](dp_import.md)

TOID\_NOVALIDATE parameter

Import utility, [22.7.32](original_import.md)

TOUSER parameter

Import utility, [22.7.33](original_import.md)

trace files

viewing with ADRCI, [16.6](adrci.md)

trailing blanks

loading with delimiters, [10.4.5.4](ldr_field_list.md)

TRAILING NULLCOLS parameter

SQL\*Loader utility, [9.1](ldr_control_file.md), [9.13.6.1](ldr_control_file.md)

trailing whitespace

trimming, [10.10.5](ldr_field_list.md)

TRANSFORM parameter

Data Pump Import utility, [3.4.45](dp_import.md)

transparent data encryption

as handled by Data Pump Export, [2.4.13](dp_export.md)

as handled by Data Pump Import, [3.4.9](dp_import.md)

LogMiner support, [19.5](logminer.md)

TRANSPORT\_DATAFILES parameter

Data Pump Import utility, [3.4.46](dp_import.md)

TRANSPORT\_FULL\_CHECK parameter

Data Pump Export utility, [2.4.41](dp_export.md)

Data Pump Import utility, [3.4.47](dp_import.md)

TRANSPORT\_TABLESPACE parameter

Export utility, [21.5.28](original_export.md)

Import utility, [22.7.34](original_import.md)

TRANSPORT\_TABLESPACES parameter

Data Pump Export utility, [2.4.42](dp_export.md)

Data Pump Import utility, [3.4.48](dp_import.md)

transportable option

used during table-mode export, [2.4.39](dp_export.md)

TRANSPORTABLE parameter

Data Pump Export utility, [2.4.43](dp_export.md)

Data Pump Import utility, [3.4.49](dp_import.md)

transportable tablespaces, [21.15](original_export.md), [22.19](original_import.md)

transportable-tablespace mode Export

Data Pump Export utility, [2.2.2.5](dp_export.md)

triggers

database insert, [12.8.2](ldr_modes.md)

logon

effect in SQL\*Loader, [9.13.1.1](ldr_control_file.md)

permanently disabled, [12.8.3](ldr_modes.md)

replacing with integrity constraints, [12.8.2.1](ldr_modes.md)

system

testing, [22.4](original_import.md)

update

SQL\*Loader, [12.8.2.4](ldr_modes.md)

TRIGGERS parameter

Export utility, [21.5.29](original_export.md)

trimming

summary, [10.10](ldr_field_list.md)

trailing whitespace

SQL\*Loader, [10.10.5](ldr_field_list.md)

TTS\_FULL\_CHECK parameter

Export utility, [21.5.30](original_export.md)

TTS\_OWNERS parameter

Import utility, [22.7.35](original_import.md)

---

## U

UNIQUE KEY constraints

effect on direct path load, [12.9.8](ldr_modes.md)

unique values

generating with SQL\*Loader, [10.13.6](ldr_field_list.md)

unloading entire database

Data Pump Export utility, [2.2.2.1](dp_export.md)

UNRECOVERABLE clause

SQL\*Loader, [12.5.4.2](ldr_modes.md)

unsorted data

direct path load

SQL\*Loader, [12.5.2.2](ldr_modes.md)

user mode export

specifying, [21.5.17](original_export.md)

USER\_SEGMENTS view

Export and, [21.2.2](original_export.md)

user-defined constructors, [11.1.6](ldr_loading.md)

loading column objects with, [11.1.6](ldr_loading.md)

USERID parameter

Export utility, [21.5.31](original_export.md)

Import utility, [22.7.36](original_import.md)

SQL\*Loader command line, [8.2.29](ldr_params.md)

---

## V

V$DATABASE view, [19.10](logminer.md)

V$LOGMNR\_CONTENTS view, [19.5.1](logminer.md)

formatting information returned to, [19.6](logminer.md)

impact of querying, [19.5.1](logminer.md)

information within, [19.5](logminer.md)

limiting information returned to, [19.6](logminer.md)

LogMiner utility, [19.2.2](logminer.md)

requirements for querying, [19.4](logminer.md), [19.5.1](logminer.md)

V$LOGMNR\_DICTIONARY view, [19.10](logminer.md)

V$LOGMNR\_LOGS view, [19.3.2](logminer.md), [19.10](logminer.md)

querying, [19.10.1](logminer.md)

V$LOGMNR\_PARAMETERS view, [19.9.6](logminer.md), [19.10](logminer.md)

V$SESSION\_LONGOPS view

monitoring Data Pump jobs with, [1.5.1](dp_overview.md)

VARCHAR2 datatype

SQL\*Loader, [10.4.3](ldr_field_list.md)

VARCHARC datatype

SQL\*Loader, [10.4.2.7](ldr_field_list.md)

variable records, [7.4.2](ldr_concepts.md)

format, [11.1.2](ldr_loading.md)

variable-length records

external tables, [14.2.2](et_params.md)

VARRAWC datatype, [10.4.2.8](ldr_field_list.md)

VARRAY columns

memory issues when loading, [11.8.1](ldr_loading.md)

VERSION parameter

Data Pump Export utility, [2.4.44](dp_export.md)

Data Pump Import utility, [3.4.50](dp_import.md)

viewing

trace files with ADRCI, [16.6](adrci.md)

VOLSIZE parameter

---

## W

warning messages

WHEN clause

whitespace

---

## X

XML columns

XML type tables

XMLTYPE clause