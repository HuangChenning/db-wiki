---
title: Physical Database Limits
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/limits002.htm
tags:
  - oracle
  - 11g
  - reference
---

| Item | Type of Limit | Limit Value |
| --- | --- | --- |
| Database Block Size | Minimum | `2048` bytes; must be a multiple of operating system physical block size |
| Database Block Size | Maximum | Operating system dependent; never more than `32` KB |
| Database Blocks | Minimum in initial extent of a segment | 2 blocks |
| Database Blocks | Maximum per datafile | Platform dependent; typically 2 <sup>22</sup> - 1 blocks |
| Controlfiles | Number of control files | `1` minimum; `2` or more (on separate devices) strongly recommended |
| Controlfiles | Size of a control file | Maximum of 201031680 logical blocks |
| Database files | Maximum per tablespace | Operating system dependent; usually `1022` |
| Database files | Maximum per database | 65533  May be less on some operating systems  Limited also by size of database blocks and by the `DB_FILES` initialization parameter for a particular instance |
| Database extents | Maximum per dictionary managed tablespace | `4` GB \* physical block size (with K/M modifier); `4` GB (without K/M modifier) |
| Database extents | Maximum per locally managed (uniform) tablespace | `2` GB \* physical block size (with K/M modifier); `2` GB (without K/M modifier) |
| Database file size | Maximum | Operating system dependent. Limited by maximum operating system file size. See the Bigfile Tablespaces and Smallfile (traditional) Tablespaces rows for more information about the maximum database file size in these types of tablespaces. |
| `MAXEXTENTS` | Default value | Derived from tablespace default storage or `DB_BLOCK_SIZE` initialization parameter |
| `MAXEXTENTS` | Maximum | Unlimited |
| Redo Log Files | Maximum number of logfiles | Limited by value of `MAXLOGFILES` parameter in the `CREATE DATABASE` statement  Control file can be resized to allow more entries; ultimately an operating system limit |
| Redo Log Files | Maximum number of logfiles per group | Unlimited |
| Redo Log File Size | Minimum size | `4 MB` |
| Redo Log File Size | Maximum Size | Operating system limit; typically `2` GB |
| Tablespaces | Maximum number per database | `64 K`  Number of tablespaces cannot exceed the number of database files because each tablespace must include at least one file |
| Bigfile Tablespaces | Number of blocks | A bigfile tablespace contains only one datafile or tempfile, which can contain up to approximately 4 billion ( 2 <sup>32</sup> ) blocks. The maximum size of the single datafile or tempfile is 128 terabytes (TB) for a tablespace with 32 K blocks and 32 TB for a tablespace with 8 K blocks. |
| Smallfile (traditional) Tablespaces | Number of blocks | A smallfile tablespace is a traditional Oracle tablespace, which can contain 1022 datafiles or tempfiles, each of which can contain up to approximately 4 million (2 <sup>22</sup>) blocks. |
| External Tables file | Maximum size | Dependent on the operating system.  An external table can be composed of multiple files. |