---
title: "MySQL :: MySQL 26.7 Reference Manual :: 10.15.2 System Variables Controlling Tracing"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/system-variables-controlling-tracing.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 10.15.2 System Variables Controlling Tracing

The following system variables affect optimizer tracing:

- [`optimizer_trace`](server-system-variables.md): Enables or disables optimizer tracing. See [Section 10.15.8, “The optimizer\_trace System Variable”](optimizer-trace-system-variable.md).
- [`optimizer_trace_features`](server-system-variables.md): Enables or disables selected features of the MySQL Optimizer, using the syntax shown here:
	```sql
	SET optimizer_trace_features=option=value[,option=value][,...]
	option: 
	  {greedy_search | range_optimizer | dynamic_range | repeated_subselect}
	value:
	  {on | off | default}
	```
	See [Section 10.15.10, “Selecting Optimizer Features to Trace”](optimizer-features-to-trace.md), for more information on the effects of these.
- [`optimizer_trace_max_mem_size`](server-system-variables.md): Maximum amount of memory that can be used for storing all traces.
- [`optimizer_trace_limit`](server-system-variables.md): The maximum number of optimizer traces to be shown. See [Section 10.15.4, “Tuning Trace Purging”](tuning-trace-purging.md), for more information.
- [`optimizer_trace_offset`](server-system-variables.md): Offset of the first trace shown. See [Section 10.15.4, “Tuning Trace Purging”](tuning-trace-purging.md).
- [`end_markers_in_json`](server-system-variables.md): If set to `1`, causes the trace to repeat the key (if present) near the closing bracket. This also affects the output of [`EXPLAIN           FORMAT=JSON`](explain.md) in those versions of MySQL which support this statement. See [Section 10.15.9, “The end\_markers\_in\_json System Variable”](end-markers-in-json-system-variable.md).