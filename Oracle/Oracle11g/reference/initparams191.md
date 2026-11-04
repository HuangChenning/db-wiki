---
title: PARALLEL_THREADS_PER_CPU
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams191.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Operating system-dependent, usually 2 |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Any nonzero number |

Note:

This parameter applies to parallel execution in exclusive mode as well as in a Real Application Clusters environment.

`PARALLEL_THREADS_PER_CPU` specifies the default degree of parallelism for the instance and determines the parallel adaptive and load balancing algorithms. The parameter describes the number of parallel execution processes or threads that a CPU can handle during parallel execution.

The default is platform-dependent and is adequate in most cases. You should decrease the value of this parameter if the machine appears to be overloaded when a representative parallel query is executed. You should increase the value if the system is I/O bound.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on tuning parallel execution