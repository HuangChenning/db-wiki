---
title: Data Pump Performance
book: Utilities
doc_id: E22490-08
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_perf.htm
tags:
  - oracle
  - 11g
  - utilities
---

## 5 Data Pump Performance

The Data Pump utilities are designed especially for very large databases. If your site has very large quantities of data versus metadata, then you should experience a dramatic increase in performance compared to the original Export and Import utilities. This chapter briefly discusses why the performance is better and also suggests specific steps you can take to enhance performance of export and import operations.

This chapter contains the following sections:

Performance of metadata extraction and database object creation in Data Pump Export and Import remains essentially equivalent to that of the original Export and Import utilities.

## Data Performance Improvements for Data Pump Export and Import

The improved performance of the Data Pump Export and Import utilities is attributable to several factors, including the following:

- Multiple worker processes can perform intertable and interpartition parallelism to load and unload tables in multiple, parallel, direct-path streams.
- For very large tables and partitions, single worker processes can choose intrapartition parallelism through multiple parallel queries and parallel DML I/O server processes when the external tables method is used to access data.
- Data Pump uses parallelism to build indexes and load package bodies.
- Dump files are read and written directly by the server and, therefore, do not require any data movement to the client.
- The dump file storage format is the internal stream format of the direct path API. This format is very similar to the format stored in Oracle database data files inside of tablespaces. Therefore, no client-side conversion to `INSERT` statement bind variables is performed.
- The supported data access methods, direct path and external tables, are faster than conventional SQL. The direct path API provides the fastest single-stream performance. The external tables feature makes efficient use of the parallel queries and parallel DML capabilities of the Oracle database.
- Metadata and data extraction can be overlapped during export.

## Tuning Performance

Data Pump technology fully uses all available resources to maximize throughput and minimize elapsed job time. For this to happen, a system must be well balanced across CPU, memory, and I/O. In addition, standard performance tuning principles apply. For example, for maximum performance you should ensure that the files that are members of a dump file set reside on separate disks, because the dump files are written and read in parallel. Also, the disks should not be the same ones on which the source or target tablespaces reside.

Any performance tuning activity involves making trade-offs between performance and resource consumption.

### Controlling Resource Consumption

The Data Pump Export and Import utilities enable you to dynamically increase and decrease resource consumption for each job. This is done using the `PARALLEL` parameter to specify a degree of parallelism for the job. (The `PARALLEL` parameter is the only tuning parameter that is specific to Data Pump.) For maximum throughput, do not set `PARALLEL` to much more than twice the number of CPUs (two workers for each CPU).

See Also:

- ["PARALLEL"](dp_export.md) for more information about the Export `PARALLEL` parameter
- ["PARALLEL"](dp_import.md) for more information about the Import `PARALLEL` parameter

As you increase the degree of parallelism, CPU usage, memory consumption, and I/O bandwidth usage also increase. You must ensure that adequate amounts of these resources are available. If necessary, you can distribute files across different disk devices or channels to get the needed I/O bandwidth.

To maximize parallelism, you must supply at least one file for each degree of parallelism. The simplest way of doing this is to use substitution variables in your file names (for example, `file%u.dmp`). However, depending upon your disk set up (for example, simple, non-striped disks), you might not want to put all dump files on one device. In this case, it is best to specify multiple file names using substitution variables, with each in a separate directory resolving to a separate disk. Even with fast CPUs and fast disks, the path between the CPU and the disk may be the constraining factor in the degree of parallelism that can be sustained.

The `PARALLEL` parameter is valid only in the Enterprise Edition of Oracle Database 11g.

### Effects of Compression and Encryption on Performance

The use of Data Pump parameters related to compression and encryption can possibly have a negative impact upon performance of export and import operations. This is because additional CPU resources are required to perform transformations on the raw data.

## Initialization Parameters That Affect Data Pump Performance

The settings for certain initialization parameters can affect the performance of Data Pump Export and Import. In particular, you can try using the following settings to improve performance, although the effect may not be the same on all platforms.

- `DISK_ASYNCH_IO=TRUE`
- `DB_BLOCK_CHECKING=FALSE`
- `DB_BLOCK_CHECKSUM=FALSE`

The following initialization parameters must have values set high enough to allow for maximum parallelism:

- `PROCESSES`
- `SESSIONS`
- `PARALLEL_MAX_SERVERS`

Additionally, the `SHARED_POOL_SIZE` and `UNDO_TABLESPACE` initialization parameters should be generously sized. The exact values depend upon the size of your database.

### Setting the Size Of the Buffer Cache In a Streams Environment

Oracle Data Pump uses Streams functionality to communicate between processes. If the `SGA_TARGET` initialization parameter is set, then the `STREAMS_POOL_SIZE` initialization parameter is automatically set to a reasonable value.

If the `SGA_TARGET` initialization parameter is not set and the `STREAMS_POOL_SIZE` initialization parameter is not defined, then the size of the streams pool automatically defaults to 10% of the size of the shared pool.

When the streams pool is created, the required SGA memory is taken from memory allocated to the buffer cache, reducing the size of the cache to less than what was specified by the `DB_CACHE_SIZE` initialization parameter. This means that if the buffer cache was configured with only the minimal required SGA, then Data Pump operations may not work properly. A minimum size of 10 MB is recommended for `STREAMS_POOL_SIZE` to ensure successful Data Pump operations.