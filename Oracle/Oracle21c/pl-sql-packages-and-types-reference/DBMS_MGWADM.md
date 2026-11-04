---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_MGWADM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 115 DBMS\_MGWADM

`DBMS_MGWADM` defines the Messaging Gateway administrative interface. The package and object types are owned by `SYS`.

Note:

You must run the `catmgw.sql` script to load the Messaging Gateway packages and types into the database.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE3205) contains information on loading database objects and using `DBMS_MGWADM`

This chapter contains the following topics:

### 115.1 DBMS\_MGWADM Security Model

A user with administrative privilege can run all procedures in `DBMS_MGWADM`.

### 115.2 DBMS\_MGWADM Deprecated Subprograms

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

The following subprograms are deprecated with Oracle Database 11g Release 1 having been superseded by improved technology:

- ADD\_SUBSCRIBER Procedure - use instead CREATE\_JOB Procedure
- ALTER\_PROPAGATION\_SCHEDULE Procedure - use instead ALTER\_JOB Procedure
- ALTER\_SUBSCRIBER Procedure - use instead ALTER\_JOB Procedure
- DB\_CONNECT\_INFO Procedure - use instead ALTER\_AGENT Procedures
- DISABLE\_PROPAGATION\_SCHEDULE Procedure - use instead DISABLE\_JOB Procedure
- ENABLE\_PROPAGATION\_SCHEDULE Procedure - use instead ENABLE\_JOB Procedure
- REMOVE\_SUBSCRIBER Procedure - use instead REMOVE\_JOB Procedure
- RESET\_SUBSCRIBER Procedure - use instead RESET\_JOB Procedure
- SCHEDULE\_PROPAGATION Procedure - use instead CREATE\_JOB Procedure
- UNSCHEDULE\_PROPAGATION Procedure - use instead REMOVE\_JOB Procedure

### 115.3 DBMS\_MGWADM Constants

The `DBMS_MGWADM` package defines various constants for specifying parameter values.

Table 115-1 DBMS\_MGWADM Constants—Cleanup Actions

| Name | Type | Description |
| --- | --- | --- |
| `CLEAN_STARTUP_STATE` | `CONSTANT BINARY_INTEGER` | Sets the Messaging Gateway agent to a known state so that it can be started |
| `CLEAN_LOG_QUEUES` | `CONSTANT BINARY_INTEGER` | Messaging Gateway agent will clean log queues for all configured messaging system links |
| `RESET_SUB_MISSING_LOG_REC` | `CONSTANT BINARY_INTEGER` | Messaging Gateway agent recovers a Messaging Gateway subscriber that has failed due to a missing log record |
| `RESET_SUB_MISSING_MESSAGE` | `CONSTANT BINARY_INTEGER` | Messaging Gateway agent recovers a Messaging Gateway subscriber that has failed due to a missing persistent source message |

Table 115-2 DBMS\_MGWADM Constants—Force Values

| Name | Type | Description |
| --- | --- | --- |
| `FORCE` | `CONSTANT BINARY_INTEGER` | Represents a forced action |
| `NO_FORCE` | `CONSTANT BINARY_INTEGER` | Represents a normal, nonforced action |

Table 115-3 DBMS\_MGWADM Constants—Logging Levels

| Name | Type | Description |
| --- | --- | --- |
| `BASIC_LOGGING` | `CONSTANT BINARY_INTEGER` | The standard (the least) information written to the log file |
| `TRACE_DEBUG_LOGGING` | `CONSTANT BINARY_INTEGER` | The greatest information written to the log file |
| `TRACE_HIGH_LOGGING` | `CONSTANT BINARY_INTEGER` | The third level of detail of logging information written to the log file |
| `TRACE_LITE_LOGGING` | `CONSTANT BINARY_INTEGER` | The second level detail of logging information written to the log file |

Table 115-4 DBMS\_MGWADM Constants—Named Property Constants

| Name | Type | Description |
| --- | --- | --- |
| `MGWPROP_PREFIX` | `CONSTANT VARCHAR2` | A constant (`MGWPROP$_`) for the reserved property name prefix |
| `MGWPROP_REMOVE` | `CONSTANT VARCHAR2` | A constant (`MGWPROP$_REMOVE`) for the reserved property name used to remove an existing property |
| `MGWPROP_REMOVE_ALL` | `CONSTANT VARCHAR2` | A constant (`MGWPROP$_REMOVE_ALL`) for the reserved property name used to remove all properties |

Table 115-5 DBMS\_MGWADM Constants—Other Constants

| Name | Type | Description |
| --- | --- | --- |
| `JMS_CONNECTION` | `CONSTANT BINARY_INTEGER` | Used to indicate that JMS connections will be used to access JMS destinations in a domain-independent manner that supports a unified messaging model |
| `JMS_QUEUE_CONNECTION` | `CONSTANT BINARY_INTEGER` | Used to indicate that JMS queue connections will be used to access JMS destinations |
| `JMS_TOPIC_CONNECTION` | `CONSTANT BINARY_INTEGER` | Used to indicate that JMS topic connections will be used to access JMS destinations |
| `NO_CHANGE` | `CONSTANT VARCHAR2` | Indicates that an existing value should be preserved (not changed). This is used for certain APIs where the desire is to change one or more parameters but leave others unchanged. |
| `DEFAULT_AGENT` | `CONSTANT VARCHAR2` | Name of the Messaging Gateway default agent |

Table 115-6 DBMS\_MGWADM Constants—Propagation Types

| Name | Type | Description |
| --- | --- | --- |
| `INBOUND_PROPAGATION` | `CONSTANT BINARY_INTEGER` | Represents the propagation type for non-Oracle to Oracle Database Advanced Queuing propagation. The propagation source is a queue in a foreign (non-Oracle) messaging system and the destination is a local Oracle Database Advanced Queuing queue. |
| `OUTBOUND_PROPAGATION` | `CONSTANT BINARY_INTEGER` | Represents the propagation type for Oracle Database Advanced Queuing to non-Oracle propagation. The propagation source is a local Oracle Database Advanced Queuing queue and the destination is a queue in a foreign (non-Oracle) messaging system. |

Table 115-7 DBMS\_MGWADM Constants—Queue Domain Types

| Name | Type | Description |
| --- | --- | --- |
| `DOMAIN_QUEUE` | `CONSTANT BINARY_INTEGER` | Represents a queue destination. A JMS queue (point-to-point model) is classified as a queue. |
| `DOMAIN_TOPIC` | `CONSTANT BINARY_INTEGER` | Represents a topic destination. A JMS topic (publish-subscribe model) is classified as a topic. |

Table 115-8 DBMS\_MGWADM Constants—Shutdown Modes

| Name | Type | Description |
| --- | --- | --- |
| `SHUTDOWN_IMMEDIATE` | `CONSTANT BINARY_INTEGER` | Represents the immediate shutdown mode |
| `SHUTDOWN_NORMAL` | `CONSTANT BINARY_INTEGER` | Represents the normal shutdown mode |

Table 115-9 DBMS\_MGWADM Constants—WebSphere MQ Interface Types

| Name | Type | Description |
| --- | --- | --- |
| `MQSERIES_BASE_JAVA_INTERFACE` | `CONSTANT BINARY_INTEGER` | Represents the Base Java interface for the WebSphere MQ messaging system |

Table 115-10 DBMS\_MGWADM Constants—target\_type Argument of SET\_OPTION and REMOVE\_OPTION Procedures

| Name | Type | Description |
| --- | --- | --- |
| `AGENT_JAVA_PROP` | `CONSTANT PLS_INTEGER` | Used for an agent option used to set a Java System property |
| `MSGLINK_OPTION` | `CONSTANT PLS_INTEGER` | Used for a messaging system link option |
| `JOB_OPTION` | `CONSTANT PLS_INTEGER` | Used for a propagation job option |

Table 115-11 DBMS\_MGWADM Constants—conntype Argument of CREATE\_AGENT and ALTER\_AGENT Procedures

| Name | Type | Description |
| --- | --- | --- |
| `JDBC_OCI` | `CONSTANT VARCHAR2` | Used to specify the JDBC OCI driver |
| `JDBC_THIN` | `CONSTANT VARCHAR2` | Used to specify the JDBC Thin driver |

### 115.4 DBMS\_MGWADM Data Structures

#### 115.4.1 DBMS\_MGWADM SYS.MGW\_MQSERIES\_PROPERTIES Object Type

This type specifies basic properties for a WebSphere MQ messaging system link.

Syntax

```
TYPE SYS.MGW_MQSERIES_PROPERTIES IS OBJECT (
   queue_manager       VARCHAR2(64),
   hostname            VARCHAR2(64),
   port                INTEGER,
   channel             VARCHAR2(64),
   interface_type      INTEGER,
   username            VARCHAR2(64),
   password            VARCHAR2(64),
   inbound_log_queue   VARCHAR2(64),
   outbound_log_queue  VARCHAR2(64),

-- Methods 
STATIC FUNCTION construct 
RETURN SYS.MGW_MQSERIES_PROPERTIES,

STATIC FUNCTION alter_construct 
RETURN SYS.MGW_MQSERIES_PROPERTIES );
```

Attributes

Table 115-12 SYS.MGW\_MQSERIES\_PROPERTIES Attributes

| Attribute | Description |
| --- | --- |
| `queue_manager` | The name of the WebSphere MQ queue manager |
| `hostname` | The host on which the WebSphere MQ messaging system resides. If hostname is `NULL,` then a WebSphere MQ bindings connection is used. If not `NULL`, then a client connection is used and requires that a port and channel be specified. |
| `port` | The port number. This is used only for client connections; that is, when `hostname` is not `NULL`. |
| `channel` | The channel used when establishing a connection to the queue manager. This is used only for client connections; that is, when `hostname` is not `NULL`. |
| `interface_type` | The type of messaging interface to use. Values:  - `DBMS_MGWADM.MQSERIES_BASE_JAVA_INTERFACE` if the WebSphere MQ Base Java interface should be used. - `DBMS_MGWADM.JMS_CONNECTION` if the link is to be used to access JMS destinations in a unified, domain-independent manner. - `DBMS_MGWADM.JMS_QUEUE_CONNECTION` if the link is to be used for accessing JMS queues - `DBMS_MGWADM.JMS_TOPIC_CONNECTION` if the link is to be used for accessing JMS topics. |
| `username` | The username used for authentication to the WebSphere MQ messaging system |
| `password` | The password used for authentication to the WebSphere MQ messaging system |
| `inbound_log_queue` | The name of the WebSphere MQ queue used for propagation recovery purposes when this messaging link is used for inbound propagation; that is, when queues associated with this link serve as a propagation source:  - For `MQSERIES_BASE_JAVA_INTERFACE`, this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. - For the `JMS_CONNECTION` interface and the `JMS_QUEUE_CONNECTION` interface, this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. - For `JMS_TOPIC_CONNECTION` interface, this specifies the name of a WebSphere MQ JMS topic. The physical WebSphere MQ queue used by subscribers of that topic must be created using WebSphere MQ administration tools. By default, the physical queue used is `SYSTEM.JMS.D.SUBSCRIBER.QUEUE`. |
| `outbound_log_queue` | The name of the WebSphere MQ queue used for propagation recovery purposes when this messaging link is used for outbound propagation; that is, when queues associated with this link serve as a propagation destination:  - For `MQSERIES_BASE_JAVA_INTERFACE`, this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. - For the `JMS_CONNECTION` interface and the `JMS_QUEUE_CONNECTION` interface, this is the name of a physical WebSphere MQ queue created using WebSphere MQ administration tools. - For `JMS_TOPIC_CONNECTION` interface, this specifies the name of a WebSphere MQ JMS topic. The physical WebSphere MQ queue used by subscribers of that topic must be created using WebSphere MQ administration tools. By default, the physical queue used is `SYSTEM.JMS.D.SUBSCRIBER.QUEUE`. |

Methods

Table 115-13 SYS.MGW\_MQSERIES\_PROPERTIES Methods

| Method | Description |
| --- | --- |
| `construct` | Constructs a new `SYS.MGW_MQSERIES_PROPERTIES` instance. All attributes are assigned a value of `NULL` |
| `alter_construct` | Constructs a new `SYS`.`MGW_MQSERIES_PROPERTIES` instance for altering the properties of an existing messaging link. All attributes having a `VARCHAR2` datatype are assigned a value of `DBMS_MGWADM`.`NO_CHANGE`. Attributes of other datatypes are assigned a value of `NULL`. |

#### 115.4.2 DBMS\_MGWADM SYS.MGW\_PROPERTIES Object Type

This type specifies an array of properties.

Syntax

```
TYPE SYS.MGW_PROPERTIES AS VARRAY (2000) OF SYS.MGW_PROPERTY;
```

Attributes

Table 115-14 SYS.MGW\_PROPERTIES Attributes

| Attribute | Description |
| --- | --- |
| `name` | Property name |
| `value` | Property value |

Usage Notes

Unless noted otherwise, Messaging Gateway uses named properties as follows:

- Names with the `MGWPROP$_` prefix are reserved. They are used for special purposes and are invalid when used as a normal property name.
- A property name can exist only once in a property list; that is, a list can contain only one value for a given name. The name is case-insensitive.
- In general, a property list is order-independent, and the property names may appear in any order. An alter property list is an exception.
- You can use a new property list to alter an existing property list. Each new property modifies the original list in one of the following ways: adds a new property, modifies a property, removes a property, or removes all properties.

The alter list is processed in order, from the first element to the last element. Thus the order in which the elements appear in the alter list is meaningful, especially when the alter list is used to remove properties from an existing list.

The property name and value are used to determine how that element affects the original list. The following rules apply:

- Add or modify property
	```
	MGW_PROPERTY.NAME = property_name
	MGW_PROPERTY.VALUE = property_value
	```
	If a property of the given name already exists, then the current value is replaced with the new value; otherwise the new property is added to the end of the list.
- Remove property
	```
	MGW_PROPERTY.NAME = 'MGWPROP$_REMOVE'
	MGW_PROPERTY.VALUE = name_of_property_to_remove
	```
	No action is taken if the property name does not exist in the original list.
- Remove all properties
	```
	MGW_PROPERTY.NAME = 'MGWPROP$_REMOVE_ALL'
	MGW_PROPERTY.VALUE = not used
	```

See Also:

"The `DBMS_MGWADM` package defines constants to represent the reserved property names on Table 115-4

#### 115.4.3 DBMS\_MGWADM SYS.MGW\_PROPERTY Object Type

This type specifies a named property which is used to specify optional properties for messaging links, foreign queues, and subscribers.

Syntax

```
TYPE SYS.MGW_PROPERTY IS OBJECT(
   name  VARCHAR2(500),
   value VARCHAR2(4000),

-- Methods  
STATIC FUNCTION construct    --- (1)
RETURN SYS.MGW_PROPERTY,

STATIC FUNCTION construct(   --- (2)
   p_name   IN VARCHAR2,
   p_value  IN VARCHAR2)
RETURN SYS.MGW_PROPERTY );
```

Attributes

Table 115-15 SYS.MGW\_PROPERTY Attributes

| Attribute | Description |
| --- | --- |
| `name` | Property name |
| `value` | Property value |

Methods

Table 115-16 SYS.MGW\_PROPERTY Methods

| Method | Description |
| --- | --- |
| `construct --- (1)` | Constructs a new `MGW_PROPERTY` instance. All attributes are assigned a value of `NULL` |
| `construct --- (2)` | Constructs a new `MGW_PROPERTY` instance initialized using the given parameters |

See Also:

"The `DBMS_MGWADM` package defines constants to represent the reserved property names on Table 115-4

#### 115.4.4 SYS.MGW\_TIBRV\_PROPERTIES Object Type

A type that specifies basic properties for a TIB/Rendezvous messaging system link. The Messaging Gateway agent creates a TIB/Rendezvous transport of type `TibrvRvdTransport` for each Messaging Gateway link.

Syntax

```
TYPE SYS.MGW_TIBRV_PROPERTIES IS OBJECT(
   service   VARCHAR2(128),
   daemon    VARCHAR2(128),
   network   VARCHAR2(256),
   cm_name   VARCHAR2(256),
   cm_ledger VARCHAR2(256),

-- Methods
STATIC FUNCTION construct 
RETURN SYS.MGW_TIBRV_PROPERTIES,

STATIC FUNCTION alter_construct 
RETURN SYS.MGW_TIBRV_PROPERTIES );
```

Attributes

Table 115-17 SYS.MGW\_TIBRV\_PROPERTIES Attributes

| Attribute | Description |
| --- | --- |
| `service` | The service parameter for the rvd transport |
| `daemon` | The daemon parameter for the rvd transport |
| `network` | The network parameter for the rvd transport |
| `cm_name` | The CM correspondent name. Reserved for future use. |
| `cm_ledger` | The CM ledger file name. Reserved for future use. |

Methods

Table 115-18 SYS.MGW\_TIBRV\_PROPERTIES Methods

| Method | Description |
| --- | --- |
| `construct` | Constructs a new `SYS`.`MGW_TIBRV_PROPERTIES` instance. All attributes will be assigned a value of `NULL.` |
| `alter_construct` | Constructs a new `SYS`.`MGW_TIBRV_PROPERTIES` instance. This function is useful for altering the properties of an existing messaging link. All attributes having a `VARCHAR2` datatype will be assigned a value of `DBMS_MGWADM`.`NO_CHANGE`. Attributes of other datatypes will be assigned a value of `NULL`. |

### 115.5 Summary of DBMS\_MGWADM Subprograms

This table lists the `DBMS_MGWADM` subprograms and briefly describes them.

Table 115-19 DBMS\_MGWADM Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_SUBSCRIBER Procedure | Adds a subscriber used to consume messages from a source queue for propagation to a destination |
| ALTER\_AGENT Procedures | Alters Messaging Gateway agent parameters |
| ALTER\_JOB Procedure | Alters the properties of a propagation job |
| ALTER\_MSGSYSTEM\_LINK Procedure for TIB/Rendezvous | Alters the properties of a TIB/Rendezvous messaging system link |
| ALTER\_MSGSYSTEM\_LINK Procedure for WebSphere MQ | Alters the properties of a WebSphere MQ messaging system link |
| ALTER\_PROPAGATION\_SCHEDULE Procedure | Alters a propagation schedule |
| ALTER\_SUBSCRIBER Procedure | Alters the parameters of a subscriber used to consume messages from a source queue for propagation to a destination |
| CLEANUP\_GATEWAY Procedures | Cleans up Messaging Gateway |
| CREATE\_AGENT Procedure | Creates a Messaging Gateway agent that will be used to process propagation jobs |
| CREATE\_JOB Procedure | Creates a job used to propagate message from a source to a destination |
| CREATE\_MSGSYSTEM\_LINK Procedures for TIB/Rendezvous | Creates a messaging system link to a TIB/Rendezvous messaging system |
| CREATE\_MSGSYSTEM\_LINK Procedures for WebSphere MQ | Creates a messaging system link to a WebSphere MQ messaging system |
| DB\_CONNECT\_INFO Procedure | Configures connection information used by the Messaging Gateway agent for connections to Oracle Database |
| DISABLE\_JOB Procedure | Disables a propagation job |
| DISABLE\_PROPAGATION\_SCHEDULE Procedure | Disables a propagation schedule |
| ENABLE\_JOB Procedure | Enables a propagation job |
| ENABLE\_PROPAGATION\_SCHEDULE Procedure | Enables a propagation schedule |
| REGISTER\_FOREIGN\_QUEUE Procedure | Registers a non-Oracle queue entity in Messaging Gateway |
| REMOVE\_AGENT Procedure | Removes a Messaging Gateway agent |
| REMOVE\_JOB Procedure | Removes a propagation job |
| REMOVE\_MSGSYSTEM\_LINK Procedure | Removes a messaging system link for a non-Oracle messaging system |
| REMOVE\_OPTION Procedure | Removes a Messaging Gateway configuration option |
| REMOVE\_SUBSCRIBER Procedure | Removes a subscriber used to consume messages from a source queue for propagation to a destination |
| RESET\_JOB Procedure | Resets the propagation error state for a propagation job |
| RESET\_SUBSCRIBER Procedure | Resets the propagation error state for a subscriber |
| SCHEDULE\_PROPAGATION Procedure | Schedules message propagation from a source to a destination |
| SET\_LOG\_LEVEL Procedures | Dynamically alters the Messaging Gateway agent logging level |
| SET\_OPTION Procedure | Sets a Messaging Gateway configuration option |
| SHUTDOWN Procedures | Shuts down the Messaging Gateway agent |
| STARTUP Procedures | Starts the Messaging Gateway agent |
| UNREGISTER\_FOREIGN\_QUEUE Procedure | Removes a non-Oracle queue entity in Messaging Gateway |
| UNSCHEDULE\_PROPAGATION Procedure | Removes a propagation schedule |

#### 115.5.1 ADD\_SUBSCRIBER Procedure

This procedure adds a subscriber used to consume messages from a source queue for propagation to a destination.

Note:

This subprogram has been deprecated as a result of improved technology (see CREATE\_JOB Procedure), and is retained only for reasons of backward compatibility.

Syntax

```
DBMS_MGWADM.ADD_SUBSCRIBER(
   subscriber_id     IN VARCHAR2,
   propagation_type  IN BINARY_INTEGER,
   queue_name        IN VARCHAR2,
   destination       IN VARCHAR2,
   rule              IN VARCHAR2 DEFAULT NULL,
   transformation    IN VARCHAR2 DEFAULT NULL,
   exception_queue   IN VARCHAR2 DEFAULT NULL
   options           IN SYS.MGW_PROPERTIES DEFAULT NULL);
```

Parameters

Table 115-20 ADD\_SUBSCRIBER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `subscriber_id` | Specifies a user-defined name that identifies this subscriber |
| `propagation_type` | Specifies the type of message propagation. `DBMS_MGWADM.OUTBOUND_PROPAGATION` is for Oracle Database Advanced Queuing to non-Oracle propagation. `DBMS_MGWADM.INBOUND_PROPAGATION` is for non-Oracle to Oracle Database Advanced Queuing propagation |
| `queue_name` | Specifies the source queue to which this subscriber is being added. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `destination` | Specifies the destination queue to which messages consumed by this subscriber are propagated. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `rule` | Specifies an optional subscription rule used by the subscriber to dequeue messages from the source queue. This is `NULL` if no rule is needed. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `transformation` | Specifies the transformation needed to convert between the Oracle Database Advanced Queuing payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the value specified for `propagation_type`.  If `NULL`, then the Oracle Database Advanced Queuing payload type must be supported by Messaging Gateway. |
| `exception_queue` | Specifies a queue used for exception message logging purposes. This queue must be on the same messaging system as the propagation source. If `NULL,` then an exception queue is not used and propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the value specified for `propagation_type.`  The source queue and exception queue cannot be the same queue. |
| `options` | Optional subscriber properties. `NULL` if there are none. Typically these are lesser used configuration properties supported by the messaging system. |

Usage Notes

See Also:

"Handling Arbitrary Payload Types Using Message Transformations", in [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE2001) for more information regarding message conversion and transformation

If the non-Oracle messaging link being accessed for the subscriber uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Database Advanced Queuing queues. Otherwise the native Oracle Database Advanced Queuing interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections.

Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be `NULL`.

See Also:

For additional information regarding subscriber options

- ["WebSphere MQ System Properties" in Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE1901)
- ["TIB/Rendezvous System Properties" in Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE1902)

OUTBOUND\_PROPAGATION Subscribers

The parameters for a subscriber used for outbound propagation are interpreted as follows:

- `queue_name` specifies the local Oracle Database Advanced Queuing queue that is the propagation source. This must have a syntax of `schema.queue`.
- `destination` specifies the foreign queue to which messages are propagated. This must have a syntax of `registered_queue@message_link`.
- `rule` specifies an optional Oracle Database Advanced Queuing subscriber rule if the native Oracle Database Advanced Queuing interface is used, or a JMS selector if the Oracle JMS interface is used. If `NULL`, then no rule or selector is used.
- `transformation` specifies the transformation used to convert the Oracle Database Advanced Queuing payload to an ADT defined by Messaging Gateway.
	Messaging Gateway propagation dequeues messages from the Oracle Database Advanced Queuing queue using the transformation to convert the Oracle Database Advanced Queuing payload to a known ADT defined by Messaging Gateway. The message is then enqueued in the foreign messaging system based on the Messaging Gateway ADT.
- `exception_queue` specifies the name of a local Oracle Database Advanced Queuing queue to which messages are moved if an exception occurs. This must have a syntax of `schema.queue`.

If the native Oracle Database Advanced Queuing interface is used, then a subscriber will be added to the Oracle Database Advanced Queuing queue when this procedure is called, whether or not Messaging Gateway is running. The local subscriber will be of the form `sys.aq$_agent('MGW_` `subscriber_id` `'`, `NULL,` `NULL)`.

If the Oracle JMS interface is used, then the Messaging Gateway agent will create a JMS durable subscriber with the name of `MGW_` `subscriber_id`. If the agent is not running when this procedure is called, then the durable subscriber will be created the next time the agent starts.

The exception queue has the following caveats:

- The user is responsible for creating the Oracle Database Advanced Queuing queue to be used as the exception queue.
- The payload type of the source and exception queue must match.
- The exception queue must be created as a queue type of `DBMS_AQADM.NORMAL_QUEUE` rather than `DBMS_AQADM.EXCEPTION_QUEUE`. Enqueue restrictions prevent Messaging Gateway propagation from using an Oracle Database Advanced Queuing queue of type `EXCEPTION_QUEUE` as a Messaging Gateway exception queue.

INBOUND\_PROPAGATION Subscribers

The parameters for a subscriber used for inbound propagation are interpreted as follows:

- `queue_name` specifies the foreign queue that is the propagation source. This must have a syntax of `registered_queue@message_link`.
- `destination` specifies the local Oracle Database Advanced Queuing queue to which messages are propagated. This must have a syntax of `schema.queue`.
- `rule` specifies an optional subscriber rule that is valid for the foreign messaging system. This is `NULL` if no rule is needed.
- `transformation` specifies the transformation used to convert an ADT defined by Messaging Gateway to the Oracle Database Advanced Queuing payload type.
	Messaging Gateway propagation dequeues messages from the foreign messaging system and converts the message body to a known ADT defined by Messaging Gateway. The transformation is used to convert the Messaging Gateway ADT to an Oracle Database Advanced Queuing payload type when the message is enqueued to the Oracle Database Advanced Queuing queue.
- `exception_queue` specifies the name of a foreign queue to which messages are moved if an exception occurs. This must have a syntax of `registered_queue@message_link`.

Whether or not a subscriber is needed depends on the requirements of the non-Oracle messaging system. If a durable subscriber is necessary, then it will be created by the Messaging Gateway agent. If the agent is not running at the time this procedure is called, then the creation of the subscriber on the non-Oracle messaging system will occur when the agent next starts.

The exception queue has the following caveats:

- The exception queue must be a registered non-Oracle queue.
- The source and exception queues must use the same messaging system link.

#### 115.5.2 ALTER\_AGENT Procedures

This procedure configures Messaging Gateway agent parameters.

Syntax

```
DBMS_MGWADM.ALTER_AGENT (
   max_memory       IN  BINARY_INTEGER DEFAULT NULL,
   max_threads      IN  BINARY_INTEGER DEFAULT NULL,
   service          IN  VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE );
```
```
DBMS_MGWADM.ALTER_AGENT (
   agent_name      IN   VARCHAR2,
   username        IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   password        IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   database        IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   conntype        IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   max_memory      IN   PLS_INTEGER DEFAULT NULL,
   max_threads     IN   PLS_INTEGER DEFAULT NULL,
   service         IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   initfile        IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   comment         IN   VARCHAR2  DEFAULT DBMS_MGWADM.NO_CHANGE );
```

Parameters

Table 115-21 ALTER\_AGENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `max_memory` | The maximum heap size, in MB, used by the Messaging Gateway agent. If it is `NULL,` then the current value is unchanged. |
| `max_threads` | The number of messaging threads that the Messaging Gateway agent creates. If it is `NULL`, then the current value is unchanged. The maximum value of `max_threads` is limited to 128. |
| `service` | Specifies the database service that the Oracle Scheduler job class used by this agent will have affinity to. In an Oracle RAC environment, this means that the Messaging Gateway agent will run on only those database instances that are assigned to the service. If `NULL`, the job class used by this agent will be altered to belong to the default service which is mapped to every instance. If `DBMS_MGWADM`.`NO_CHANGE`, the current value is unchanged. |
| `agent_name` | Identifies the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |
| `username` | Specifies the username used for connections to the Oracle Database. `NULL` is not allowed. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged. If a username is specified then a password must also be specified. |
| `password` | Specifies the password used for connections to the Oracle Database. `NULL` is not allowed. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged. A password must be specified if a username is specified. |
| `database` | Specifies the database connect string used for connections to the Oracle Database. `NULL` indicates that a local connection should be used. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged.Oracle strongly recommends that a connect string, rather than `NULL`, be specified. Usually it will be a net service name from `tnsnames`.`ora`. |
| `conntype` | Specifies the type of connection to the Oracle Database, `DBMS_MGWADM`.`JDBC_OCI` or `DBMS_MGWADM`.`JDBC_THIN`. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged |
| `initfile` | Specifies a Messaging Gateway initialization file used by this agent. `NULL` indicates that the default initialization file is used. If a value is specified, it should be the full path name of the file. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged. |