---
title: "SQL*Loader"
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/part_ldr.htm
tags:
  - oracle
  - 11g
  - utilities
---

## Part II

## SQL\*Loader

The chapters in this part describe the SQL\*Loader utility:

[Chapter 7, "SQL\*Loader Concepts"](ldr_concepts.md)

This chapter introduces SQL\*Loader and describes its features. It also introduces data loading concepts (including object support). It discusses input to SQL\*Loader, database preparation, and output from SQL\*Loader.

[Chapter 8, "SQL\*Loader Command-Line Reference"](ldr_params.md)

This chapter describes the command-line syntax used by SQL\*Loader. It discusses command-line arguments, suppressing SQL\*Loader messages, sizing the bind array, and more.

[Chapter 9, "SQL\*Loader Control File Reference"](ldr_control_file.md)

This chapter describes the control file syntax you use to configure SQL\*Loader and to describe to SQL\*Loader how to map your data to Oracle format. It provides detailed syntax diagrams and information about specifying data files, tables and columns, the location of data, the type and format of data to be loaded, and more.

[Chapter 10, "SQL\*Loader Field List Reference"](ldr_field_list.md)

This chapter describes the field list section of a SQL\*Loader control file. The field list provides information about fields being loaded, such as position, datatype, conditions, and delimiters.

[Chapter 11, "Loading Objects, LOBs, and Collections"](ldr_loading.md)

This chapter describes how to load column objects in various formats. It also discusses how to load object tables, `REF` columns, LOBs, and collections.

[Chapter 12, "Conventional and Direct Path Loads"](ldr_modes.md)

This chapter describes the differences between a conventional path load and a direct path load. A direct path load is a high-performance option that significantly reduces the time required to load large quantities of data.