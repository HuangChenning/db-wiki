---
title: Reading the Parameter Descriptions
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams005.htm
tags:
  - oracle
  - 11g
  - reference
---

The parameter descriptions in this chapter adhere to the following format.

PARAMETER\_NAME

| Property | Description |
| --- | --- |
| Parameter type | Specifies the type of the parameter: - A Boolean parameter accepts either `true` or `false` as its value. - A string parameter accepts any sequence of characters as its value, subject to the syntax for the parameter. - An integer parameter accepts a 4-byte value that can range from 0 to 2 <sup>32</sup> - 1. - A parameter file parameter accepts an initialization parameter file specification as its value. - A big integer parameter accepts an 8-byte value that can range from 0 to 2 <sup>64</sup> - 1. You specify a value for a big integer as an integer together with an optional modifier such as K, M, or G, which respectively denotes kilobytes, megabytes, or gigabytes. 	For example, 1000, 100 KB, 50 MB and 2 GB are valid specifications for big integers. |
| Syntax | For string and big integer parameters, specifies the valid syntax for specifying the parameter. |
| Default value | Specifies the value this parameter assumes if not explicitly specified. |
| Modifiable | Specifies whether the parameter can be changed for the current session (by an `ALTER SESSION` statement) or for all sessions in the current instance (by an `ALTER SYSTEM` statement): - `ALTER SESSION` overrides the instance-wide setting of the parameter for the current session only. You can restore the instance-wide setting for that session only by issuing another `ALTER SESSION` statement. - `ALTER SYSTEM` can be used to change the value in the server parameter file (SPFILE) of any initialization parameter. Such a change takes effect only in subsequent instances. The parameter descriptions indicate only those parameters that can be modified for the current instance. |
| Range of values | Specifies the valid range of values that this parameter can assume, shown as a minimum and maximum value. Not applicable to all parameters. |
| Oracle RAC | Specifies how the values for this parameter must be specified for multiple instances in an Oracle Real Application Clusters environment. Not applicable to all parameters. |

For each parameter, paragraphs following these details further describe the parameter and the effects of different settings.