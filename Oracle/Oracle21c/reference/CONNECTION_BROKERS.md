---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CONNECTION_BROKERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.51 CONNECTION\_BROKERS

`CONNECTION_BROKERS` is used to specify connection broker types, the number of connection brokers of each type, and the maximum number of connections per broker.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CONNECTION_BROKERS = broker_description[,...]` |
| Syntax | broker\_description::=  `((type_clause)(brokers_clause)[(broker_options)])` |
| Syntax | type\_clause::=  `TYPE={ DEDICATED \| EMON \| POOLED }`  Indicates the broker type. This is a mandatory parameter. |
| Syntax | brokers\_clause::=  `BROKERS=` `integer`  Indicates the number of brokers of the specified type. This is a mandatory parameter. The specified integer value must be greater than or equal to 0. If set to 0, brokers will not accept new connections, but existing connections will continue as normal. |
| Syntax | broker\_options::=  `CONNECTIONS=` `integer`  The maximum number of connections per broker. This is an optional parameter. If the specified integer value is greater than the maximum allowed for the platform, the maximum allowed for the platform is used. |
| Default value | The default value for the initialization parameter will contain the `DEDICATED` and `EMON` broker types. Certain types of brokers are only started when certain features are enabled, so their configuration will only apply if the broker is needed. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value should be set on all instances |

The connection brokers are used in these cases:

- DEDICATED brokers are used by the multiprocess and multithreaded Oracle features. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1245) for more information about these features.
	`DEDICATED` brokers are also used when the `USE_DEDICATED_BROKER` initialization parameter is set to `true`. See " [USE\_DEDICATED\_BROKER](USE_DEDICATED_BROKER.md) " for more information about the `USE_DEDICATED_BROKER` initialization parameter.
- EMON brokers are used when there is a client registered for notification over 12c AQ queues. It is not on by default. See [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADQUE0100) for more information about AQ queues.
- POOLED brokers are used whenever a Database Resident Connection Pooling (DRCP) pool is active. See [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT1896) for more information about DRCP pooling.
	The POOLED broker does not appear in the parameter by default. In this case, the DRCP fields are used. If you specify the `POOLED` broker in the parameter, then that specification will override the DRCP fields, and further attempts to set the DRCP fields will then throw an error. Oracle recommends that the parameter be used instead of the DRCP fields.

To make it easier to modify the list, individual entries are indexed using the `TYPE` so it is not necessary to re-specify the entire list. For example, to adjust the number of `DEDICATED` brokers:

`alter system set connection_brokers = '((TYPE=DEDICATED)(BROKERS=2))'`