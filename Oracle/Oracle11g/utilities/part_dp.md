---
title: Oracle Data Pump
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/part_dp.htm
tags:
  - oracle
  - 11g
  - utilities
---

## Part I

## Oracle Data Pump

This part contains the following chapters:

- [Chapter 1, "Overview of Oracle Data Pump"](dp_overview.md)
	This chapter provides an overview of Oracle Data Pump technology, which enables very high-speed movement of data and metadata from one database to another.
- [Chapter 2, "Data Pump Export"](dp_export.md)
	This chapter describes the Oracle Data Pump Export utility, which is used to unload data and metadata into a set of operating system files called a dump file set.
- [Chapter 3, "Data Pump Import"](dp_import.md)
	This chapter describes the Oracle Data Pump Import utility, which is used to load an export dump file set into a target system. It also describes how to perform a network import to load a target database directly from a source database with no intervening files.
- [Chapter 4, "Data Pump Legacy Mode"](dp_legacy.md)
	This chapter describes Data Pump legacy mode, which lets you use original Export and Import parameters on the Data Pump Export and Data Pump Import command lines.
- [Chapter 5, "Data Pump Performance"](dp_perf.md)
	This chapter discusses why the performance of Data Pump Export and Import is better than that of original Export and Import. It also suggests specific steps you can take to enhance performance of export and import operations.
- [Chapter 6, "The Data Pump API"](dp_api.md)
	This chapter describes how the Data Pump API, `DBMS_DATAPUMP`, works.