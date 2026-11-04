---
title: DBMS_MGWADM
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_MGWADM.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

`DBMS_MGWADM` defines the Messaging Gateway administrative interface. The package and object types are owned by `SYS`.

**Note:** You must run the `catmgw.sql` script to load the Messaging Gateway packages and types into the database.

**See Also:** [*Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE3205) contains information on loading database objects and using `DBMS_MGWADM`

This chapter contains the following topics:

### DBMS\_MGWADM Security Model

A user with administrative privilege can run all procedures in `DBMS_MGWADM`.

### DBMS\_MGWADM Deprecated Subprograms

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

The following subprograms are deprecated with Oracle Database 11 *g* Release 1 having been superseded by improved technology:

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

### DBMS\_MGWADM Constants

The `DBMS_MGWADM` package defines various constants for specifying parameter values.

- Table 118-1
- Table 118-2
- Table 118-3
- Table 118-4
- Table 118-5
- Table 118-6
- Table 118-7
- Table 118-8
- Table 118-9
- Table 118-10
- Table 118-11

Table 1 DBMS\_MGWADM Constants-Cleanup Actions

| Name | Type | Description |
| --- | --- | --- |
| `CLEAN_STARTUP_STATE` | `CONSTANT BINARY_INTEGER` | Sets the Messaging Gateway agent to a known state so that it can be started |
| `CLEAN_LOG_QUEUES` | `CONSTANT BINARY_INTEGER` | Messaging Gateway agent will clean log queues for all configured messaging system links |
| `RESET_SUB_MISSING_LOG_REC` | `CONSTANT BINARY_INTEGER` | Messaging Gateway agent recovers a Messaging Gateway subscriber that has failed due to a missing log record |
| `RESET_SUB_MISSING_MESSAGE` | `CONSTANT BINARY_INTEGER` | Messaging Gateway agent recovers a Messaging Gateway subscriber that has failed due to a missing persistent source message |

Table 2 DBMS\_MGWADM Constants-Force Values

| Name | Type | Description |
| --- | --- | --- |
| `FORCE` | `CONSTANT BINARY_INTEGER` | Represents a forced action |
| `NO_FORCE` | `CONSTANT BINARY_INTEGER` | Represents a normal, nonforced action |

Table 3 DBMS\_MGWADM Constants-Logging Levels

| Name | Type | Description |
| --- | --- | --- |
| `BASIC_LOGGING` | `CONSTANT BINARY_INTEGER` | The standard (the least) information written to the log file |
| `TRACE_DEBUG_LOGGING` | `CONSTANT BINARY_INTEGER` | The greatest information written to the log file |
| `TRACE_HIGH_LOGGING` | `CONSTANT BINARY_INTEGER` | The third level of detail of logging information written to the log file |
| `TRACE_LITE_LOGGING` | `CONSTANT BINARY_INTEGER` | The second level detail of logging information written to the log file |

Table 4 DBMS\_MGWADM Constants-Named Property Constants

| Name | Type | Description |
| --- | --- | --- |
| `MGWPROP_PREFIX` | `CONSTANT VARCHAR2` | A constant (`MGWPROP$_`) for the reserved property name prefix |
| `MGWPROP_REMOVE` | `CONSTANT VARCHAR2` | A constant (`MGWPROP$_REMOVE`) for the reserved property name used to remove an existing property |
| `MGWPROP_REMOVE_ALL` | `CONSTANT VARCHAR2` | A constant (`MGWPROP$_REMOVE_ALL`) for the reserved property name used to remove all properties |

Table 5 DBMS\_MGWADM Constants-Other Constants

| Name | Type | Description |
| --- | --- | --- |
| `JMS_CONNECTION` | `CONSTANT BINARY_INTEGER` | Used to indicate that JMS connections will be used to access JMS destinations in a domain-independent manner that supports a unified messaging model |
| `JMS_QUEUE_CONNECTION` | `CONSTANT BINARY_INTEGER` | Used to indicate that JMS queue connections will be used to access JMS destinations |
| `JMS_TOPIC_CONNECTION` | `CONSTANT BINARY_INTEGER` | Used to indicate that JMS topic connections will be used to access JMS destinations |
| `NO_CHANGE` | `CONSTANT VARCHAR2` | Indicates that an existing value should be preserved (not changed). This is used for certain APIs where the desire is to change one or more parameters but leave others unchanged. |
| `DEFAULT_AGENT` | `CONSTANT VARCHAR2` | Name of the Messaging Gateway default agent |

Table 6 DBMS\_MGWADM Constants-Propagation Types

| Name | Type | Description |
| --- | --- | --- |
| `INBOUND_PROPAGATION` | `CONSTANT BINARY_INTEGER` | Represents the propagation type for non-Oracle to Oracle Database Advanced Queuing propagation. The propagation source is a queue in a foreign (non-Oracle) messaging system and the destination is a local Oracle Database Advanced Queuing queue. |
| `OUTBOUND_PROPAGATION` | `CONSTANT BINARY_INTEGER` | Represents the propagation type for Oracle Database Advanced Queuing to non-Oracle propagation. The propagation source is a local Oracle Database Advanced Queuing queue and the destination is a queue in a foreign (non-Oracle) messaging system. |

Table 7 DBMS\_MGWADM Constants-Queue Domain Types

| Name | Type | Description |
| --- | --- | --- |
| `DOMAIN_QUEUE` | `CONSTANT BINARY_INTEGER` | Represents a queue destination. A JMS queue (point-to-point model) is classified as a queue. |
| `DOMAIN_TOPIC` | `CONSTANT BINARY_INTEGER` | Represents a topic destination. A JMS topic (publish-subscribe model) is classified as a topic. |

Table 8 DBMS\_MGWADM Constants-Shutdown Modes

| Name | Type | Description |
| --- | --- | --- |
| `SHUTDOWN_IMMEDIATE` | `CONSTANT BINARY_INTEGER` | Represents the immediate shutdown mode |
| `SHUTDOWN_NORMAL` | `CONSTANT BINARY_INTEGER` | Represents the normal shutdown mode |

Table 9 DBMS\_MGWADM Constants-WebSphere MQ Interface Types

| Name | Type | Description |
| --- | --- | --- |
| `MQSERIES_BASE_JAVA_INTERFACE` | `CONSTANT BINARY_INTEGER` | Represents the Base Java interface for the WebSphere MQ messaging system |

Table 10 DBMS\_MGWADM Constants-target\_type Argument of SET\_OPTION and REMOVE\_OPTION Procedures

| Name | Type | Description |
| --- | --- | --- |
| `AGENT_JAVA_PROP` | `CONSTANT PLS_INTEGER` | Used for an agent option used to set a Java System property |
| `MSGLINK_OPTION` | `CONSTANT PLS_INTEGER` | Used for a messaging system link option |
| `JOB_OPTION` | `CONSTANT PLS_INTEGER` | Used for a propagation job option |

Table 11 DBMS\_MGWADM Constants-conntype Argument of CREATE\_AGENT and ALTER\_AGENT Procedures

| Name | Type | Description |
| --- | --- | --- |
| `JDBC_OCI` | `CONSTANT VARCHAR2` | Used to specify the JDBC OCI driver |
| `JDBC_THIN` | `CONSTANT VARCHAR2` | Used to specify the JDBC Thin driver |

### DBMS\_MGWADM Data Structures

The `DBMS_MGWADM` package defines several `OBJECT` types.

**DBMS\_MGWADM Object Types**

- SYS.MGW\_MQSERIES\_PROPERTIES Object Type
- SYS.MGW\_PROPERTIES Object Type
- SYS.MGW\_PROPERTY Object Type
- SYS.MGW\_TIBRV\_PROPERTIES Object Type

### DBMS\_MGWADM SYS.MGW\_MQSERIES\_PROPERTIES Object Type

This type specifies basic properties for a WebSphere MQ messaging system link.

**Syntax**

```md
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

**Attributes**

Table 12 SYS.MGW\_MQSERIES\_PROPERTIES Attributes

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

**Methods**

Table 13 SYS.MGW\_MQSERIES\_PROPERTIES Methods

| Method | Description |
| --- | --- |
| `construct` | Constructs a new `SYS.MGW_MQSERIES_PROPERTIES` instance. All attributes are assigned a value of `NULL` |
| `alter_construct` | Constructs a new `SYS`.`MGW_MQSERIES_PROPERTIES` instance for altering the properties of an existing messaging link. All attributes having a `VARCHAR2` datatype are assigned a value of `DBMS_MGWADM`.`NO_CHANGE`. Attributes of other datatypes are assigned a value of `NULL`. |

### DBMS\_MGWADM SYS.MGW\_PROPERTIES Object Type

This type specifies an array of properties.

**Syntax**

```md
TYPE SYS.MGW_PROPERTIES AS VARRAY (2000) OF SYS.MGW_PROPERTY;
```

**Attributes**

Table 14 SYS.MGW\_PROPERTIES Attributes

| Attribute | Description |
| --- | --- |
| `name` | Property name |
| `value` | Property value |

**Usage Notes**

Unless noted otherwise, Messaging Gateway uses named properties as follows:

- Names with the `MGWPROP$_` prefix are reserved. They are used for special purposes and are invalid when used as a normal property name.
- A property name can exist only once in a property list; that is, a list can contain only one value for a given name. The name is case-insensitive.
- In general, a property list is order-independent, and the property names may appear in any order. An alter property list is an exception.
- You can use a new property list to alter an existing property list. Each new property modifies the original list in one of the following ways: adds a new property, modifies a property, removes a property, or removes all properties.

The alter list is processed in order, from the first element to the last element. Thus the order in which the elements appear in the alter list is meaningful, especially when the alter list is used to remove properties from an existing list.

The property name and value are used to determine how that element affects the original list. The following rules apply:

- Add or modify property
```md
MGW_PROPERTY.NAME = property_name
MGW_PROPERTY.VALUE = property_value
```

If a property of the given name already exists, then the current value is replaced with the new value; otherwise the new property is added to the end of the list.

- Remove property
```md
MGW_PROPERTY.NAME = 'MGWPROP$_REMOVE'
MGW_PROPERTY.VALUE = name_of_property_to_remove
```

No action is taken if the property name does not exist in the original list.

- Remove all properties
	```md
	MGW_PROPERTY.NAME = 'MGWPROP$_REMOVE_ALL'
	MGW_PROPERTY.VALUE = not used
	```

**See Also:** “The `DBMS_MGWADM` package defines constants to represent the reserved property names on Table 118-4

### DBMS\_MGWADM SYS.MGW\_PROPERTY Object Type

This type specifies a named property which is used to specify optional properties for messaging links, foreign queues, and subscribers.

**Syntax**

```md
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

**Attributes**

Table 15 SYS.MGW\_PROPERTY Attributes

| Attribute | Description |
| --- | --- |
| `name` | Property name |
| `value` | Property value |

**Methods**

Table 16 SYS.MGW\_PROPERTY Methods

| Method | Description |
| --- | --- |
| `construct --- (1)` | Constructs a new `MGW_PROPERTY` instance. All attributes are assigned a value of `NULL` |
| `construct --- (2)` | Constructs a new `MGW_PROPERTY` instance initialized using the given parameters |

**See Also:** “The `DBMS_MGWADM` package defines constants to represent the reserved property names on Table 118-4

### SYS.MGW\_TIBRV\_PROPERTIES Object Type

A type that specifies basic properties for a TIB/Rendezvous messaging system link. The Messaging Gateway agent creates a TIB/Rendezvous transport of type `TibrvRvdTransport` for each Messaging Gateway link.

**Syntax**

```md
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

**Attributes**

Table 17 SYS.MGW\_TIBRV\_PROPERTIES Attributes

| Attribute | Description |
| --- | --- |
| `service` | The service parameter for the rvd transport |
| `daemon` | The daemon parameter for the rvd transport |
| `network` | The network parameter for the rvd transport |
| `cm_name` | The CM correspondent name. Reserved for future use. |
| `cm_ledger` | The CM ledger file name. Reserved for future use. |

**Methods**

Table 18 SYS.MGW\_TIBRV\_PROPERTIES Methods

| Method | Description |
| --- | --- |
| `construct` | Constructs a new `SYS`.`MGW_TIBRV_PROPERTIES` instance. All attributes will be assigned a value of `NULL.` |
| `alter_construct` | Constructs a new `SYS`.`MGW_TIBRV_PROPERTIES` instance. This function is useful for altering the properties of an existing messaging link. All attributes having a `VARCHAR2` datatype will be assigned a value of `DBMS_MGWADM`.`NO_CHANGE`. Attributes of other datatypes will be assigned a value of `NULL`. |

### Summary of DBMS\_MGWADM Subprograms

This table lists the `DBMS_MGWADM` subprograms and briefly describes them.

Table 19 DBMS\_MGWADM Package Subprograms

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

### ADD\_SUBSCRIBER Procedure

This procedure adds a subscriber used to consume messages from a source queue for propagation to a destination.

**Note:** This subprogram has been deprecated as a result of improved technology (see CREATE\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
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

**Parameters**

Table 20 ADD\_SUBSCRIBER Procedure Parameters

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

**Usage Notes**

**See Also:** “Handling Arbitrary Payload Types Using Message Transformations”, in [*Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE2001) for more information regarding message conversion and transformation

If the non-Oracle messaging link being accessed for the subscriber uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Database Advanced Queuing queues. Otherwise the native Oracle Database Advanced Queuing interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections.

Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be `NULL`.

**See Also:**

For additional information regarding subscriber options

- [“WebSphere MQ System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1901)
- [“TIB/Rendezvous System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1902)

OUTBOUND\_PROPAGATION Subscribers

The parameters for a subscriber used for outbound propagation are interpreted as follows:

- `queue_name` specifies the local Oracle Database Advanced Queuing queue that is the propagation source. This must have a syntax of `schema.queue`.
- `destination` specifies the foreign queue to which messages are propagated. This must have a syntax of `registered_queue@message_link`.
- `rule` specifies an optional Oracle Database Advanced Queuing subscriber rule if the native Oracle Database Advanced Queuing interface is used, or a JMS selector if the Oracle JMS interface is used. If `NULL`, then no rule or selector is used.
- `transformation` specifies the transformation used to convert the Oracle Database Advanced Queuing payload to an ADT defined by Messaging Gateway.
	Messaging Gateway propagation dequeues messages from the Oracle Database Advanced Queuing queue using the transformation to convert the Oracle Database Advanced Queuing payload to a known ADT defined by Messaging Gateway. The message is then enqueued in the foreign messaging system based on the Messaging Gateway ADT.
- `exception_queue` specifies the name of a local Oracle Database Advanced Queuing queue to which messages are moved if an exception occurs. This must have a syntax of `schema.queue`.

If the native Oracle Database Advanced Queuing interface is used, then a subscriber will be added to the Oracle Database Advanced Queuing queue when this procedure is called, whether or not Messaging Gateway is running. The local subscriber will be of the form `sys.aq$_agent('MGW_` *subscriber\_id* `'`, `NULL,` `NULL)`.

If the Oracle JMS interface is used, then the Messaging Gateway agent will create a JMS durable subscriber with the name of `MGW_` *subscriber\_id*. If the agent is not running when this procedure is called, then the durable subscriber will be created the next time the agent starts.

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

### ALTER\_AGENT Procedures

This procedure configures Messaging Gateway agent parameters.

**Syntax**

```md
DBMS_MGWADM.ALTER_AGENT (
   max_memory       IN  BINARY_INTEGER DEFAULT NULL,
   max_threads      IN  BINARY_INTEGER DEFAULT NULL,
   service          IN  VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE );
```
```md
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

**Parameters**

Table 21 ALTER\_AGENT Procedure Parameters

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
| `comment` | Optional comments for this agent. `NULL` if a comment is not desired. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged. |

**Usage Notes**

- Default values for these configuration parameters are set when the Messaging Gateway agent is installed.
- Changes to the `max_memory` and `max_threads` parameters take effect the next time the Messaging Gateway agent is active. If the Messaging Gateway agent is currently active, then it must be shut down and restarted for the changes to take effect.
- The `service` parameter is used to set an Oracle Scheduler job class attribute. The job class is used to create a Scheduler job that starts the Messaging Gateway agent. An Oracle administrator must create the database service. If the value is NULL, the job class will belong to an internal service that is mapped to all instances.
- The `username`, `password`, and `database` parameters specify connection information used by the Messaging Gateway agent for connections to the Oracle Database. An Oracle administrator should create the user and grant it the role `MGW_AGENT_ROLE`.

### ALTER\_JOB Procedure

This procedure alters the properties of a propagation job.

**Syntax**

```md
DBMS_MGWADM.ALTER_JOB (
   job_name          IN   VARCHAR2,
   rule              IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   transformation    IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   exception_queue   IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   poll_interval     IN   PLS_INTEGER DEFAULT 0,
   options           IN   SYS.MGW_PROPERTIES DEFAULT NULL,
   comments          IN   VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE );
```

**Parameters**

Table 22 ALTER\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `job_name` | Identifies the propagation job |
| `rule` | Specifies an optional subscription rule used to dequeue messages from the propagation source. The syntax and interpretation of this parameter depend on the propagation type. A `NULL` value indicates that no subscription rule is needed. If `DBMS_MGWADM`.`NO_CHANGE`, then the current value is unchanged. |
| `transformation` | Specifies the transformation needed to convert between the Oracle Streams AQ payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the value specified for `propagation_type`.  A `NULL` value indicates that no transformation is needed. If `DBMS_MGWADM`.`NO_CHANGE`, the current value is unchanged. |
| `exception_queue` | Specifies a queue used for exception message logging purposes. This queue must be on the same messaging system as the propagation source. In cases in which no exception queue is associated with the job, propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the propagation type.  A `NULL` value indicates that no exception queue is used. If `DBMS_MGWADM`.`NO_CHANGE`, the current value is unchanged. |
| `poll_interval` | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available.  Values: `NULL`, 0, or value > 0:  - If zero (default), the current value will not be changed. - If `NULL`, the current value will be reset and the Messaging Gateway default polling interval will be used. The default polling interval is 5 seconds and can be overridden by the Messaging Gateway initialization file. |
| `options` | Optional job properties. If `NULL`, no options will be changed. If not `NULL`, then the properties specified in this list are combined with the current optional properties to form a new set of job options. |
| `comments` | An optional comment for this agent, or `NULL` if one is not desired. If `DBMS_MGWADM`.`NO_CHANGE`, the current value will not be changed. |

**Usage Notes**

- If the non-Oracle messaging link being accessed for the propagation job uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Streams AQ queues. Otherwise the native Oracle Streams AQ interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections.
- The subscriber rule cannot be altered when propagating from a JMS source. Instead, the propagation job must be dropped and re-created with the new rule. For JMS, changing the message selector on a durable subscription is equivalent to deleting and re-creating the subscription.
- Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be `DBMS_MGWADM`.`NO_CHANGE` (the default value).
- The options parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner; add a new property, replace an existing property, remove an existing property or remove all properties.

**Note:**

- SYS.MGW\_PROPERTY Object Type for more information about the options parameter
- OUTBOUND\_PROPAGATION Jobs for outbound propagation parameter interpretation
- INBOUND\_PROPAGATION Jobs for inbound propagation parameter interpretation

### ALTER\_MSGSYSTEM\_LINK Procedure for TIB/Rendezvous

This procedure alters the properties of a TIB/Rendezvous messaging system link.

**Syntax**

```md
DBMS_MGWADM.ALTER_MSGSYSTEM_LINK (
   linkname      IN  VARCHAR2,
   properties    IN  SYS.MGW_TIBRV_PROPERTIES,
   options       IN  SYS.MGW_PROPERTIES DEFAULT NULL,
   comment       IN  VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE );
```

**Parameters**

Table 23 ALTER\_MSGSYSTEM\_LINK Procedure Parameters for TIB/Rendezvous

| Parameters | Description |
| --- | --- |
| `linkname` | The messaging system link name |
| `properties` | Basic properties for a TIB/Rendezvous messaging system link. If `NULL`, then no link properties will be changed. |
| `options` | Optional link properties. If `NULL`, then no options will be changed. If not `NULL`, then the properties specified in this list are combined with the current options properties to form a new set of link options. |
| `comment` | A user-specified description, or `NULL` if one is not desired. If `DBMS_MGWADM.NO_CHANGE`, then the current value will not be changed. |

**Usage Notes**

To retain an existing value for a messaging link property with a `VARCHAR2` datatype, specify `DBMS_MGWADM.NO_CHANGE` for that particular property. To preserve an existing value for a property of another datatype, specify `NULL` for that property.

The `options` parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner: add a new property, replace an existing property, remove an existing property, or remove all properties.

**See Also:** SYS.MGW\_PROPERTIES Object Type

Some properties cannot be modified, and this procedure will fail if an attempt is made to alter such a property. For properties and options that can be changed, a few are dynamic, and Messaging Gateway uses the new values immediately. Others require the Messaging Gateway agent to be shut down and restarted before they take effect.

**See Also:** [“TIB/Rendezvous System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1902) for more information about the messaging system properties and options

### ALTER\_MSGSYSTEM\_LINK Procedure for WebSphere MQ

This procedure alters the properties of a WebSphere MQ messaging system link.

**Syntax**

```md
DBMS_MGWADM.ALTER_MSGSYSTEM_LINK (
   linkname   IN  VARCHAR2,
   properties IN  SYS.MGW_MQSERIES_PROPERTIES,
   options    IN  SYS.MGW_PROPERTIES DEFAULT NULL,
   comment    IN  VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE);
```

**Parameters**

Table 24 ALTER\_MSGSYSTEM\_LINK Procedure Parameters for WebSphere MQ

| Parameters | Description |
| --- | --- |
| `linkname` | The messaging system link name |
| `properties` | Basic properties for a WebSphere MQ messaging system link. If it is `NULL`, then no link properties are changed. |
| `options` | Optional link properties. `NULL` if no options are changed. If not `NULL`, then the properties specified in this list are combined with the current options properties to form a new set of link options. |
| `comment` | An optional description or `NULL` if not desired. If `DBMS_MGWADM.NO_CHANGE` is specified, then the current value is not changed. |

**Usage Notes**

To retain an existing value for a messaging link property with a `VARCHAR2` datatype, specify `DBMS_MGWADM.NO_CHANGE` for that particular property. To preserve an existing value for a property of another datatype, specify `NULL` for that property.

The `options` parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner: add a new property, replace an existing property, remove an existing property, or remove all properties.

**See Also:** SYS.MGW\_PROPERTIES Object Type

Some properties cannot be modified, and this procedure will fail if an attempt is made to alter such a property. For properties and options that can be changed, a few are dynamic, and Messaging Gateway uses the new values immediately. Others require the Messaging Gateway agent to be shut down and restarted before they take effect.

**See Also:** [“WebSphere MQ System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1901) for more information about the messaging system properties and options

### ALTER\_PROPAGATION\_SCHEDULE Procedure

This procedure alters a propagation schedule.

**Note:** This subprogram has been deprecated as a result of improved technology (see ALTER\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
DBMS_MGWADM.ALTER_PROPAGATION_SCHEDULE (
   schedule_id  IN VARCHAR2,
   duration     IN NUMBER DEFAULT NULL,
   next_time    IN VARCHAR2 DEFAULT NULL,
   latency      IN NUMBER DEFAULT NULL);
```

**Parameters**

Table 25 ALTER\_PROPAGATION\_SCHEDULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_id` | Identifies the propagation schedule to be altered |
| `duration` | Reserved for future use |
| `next_time` | Reserved for future use |
| `latency` | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available in the source queue, then the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available.  Values: `NULL` or value > 0. If `latency` is `NULL`, then the Messaging Gateway agent default polling interval will be used. The default polling interval is 5 seconds, but it can be overridden by the Messaging Gateway initialization file. |

**Usage Notes**

This procedure always overwrites the existing value for each parameter. If a given parameter is not specified, then the existing values are overwritten with the default value.

### ALTER\_SUBSCRIBER Procedure

This procedure alters the parameters of a subscriber used to consume messages from a source queue for propagation to a destination.

**Note:** This subprogram has been deprecated as a result of improved technology (see ALTER\_JOB Procedure ), and is retained only for reasons of backward compatibility.

.infoboxnote}

**Syntax**

```md
DBMS_MGWADM.ALTER_SUBSCRIBER (
   subscriber_id    IN VARCHAR2,
   rule             IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   transformation   IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   exception_queue  IN VARCHAR2 DEFAULT DBMS_MGWADM.NO_CHANGE,
   options          IN SYS.MGW_PROPERTIES DEFAULT NULL );
```

**Parameters**

Table 26 ALTER\_SUBSCRIBER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `subscriber_id` | Identifies the subscriber to be altered |
| `rule` | Specifies an optional subscription rule used by the subscriber to dequeue messages from the source queue. The syntax and interpretation of this parameter depend on the subscriber propagation type.  A `NULL` value indicates that no subscription rule is needed. If `DBMS_MGWADM.NO_CHANGE,` then the current value is unchanged. |
| `transformation` | Specifies the transformation needed to convert between the Oracle Database Advanced Queuing payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the subscriber propagation type.  A `NULL` value indicates that no transformation is needed. If `DBMS_MGWADM.NO_CHANGE,` then the current value is unchanged. |
| `exception_queue` | Specifies a queue used for exception message logging. This queue must be on the same messaging system as the propagation source. If no exception queue is associated with the subscriber, then propagation stops if a problem occurs. The syntax and interpretation of this parameter depend on the subscriber propagation type.  A `NULL` value indicates that no exception queue is used. If `DBMS_MGWADM.NO_CHANGE,` then the current value is unchanged.  The source queue and exception queue cannot be the same queue. |
| `options` | Optional subscriber properties. If `NULL`, then no options will be changed. If not `NULL`, then the properties specified in this list are combined with the current optional properties to form a new set of subscriber options. |

**Usage Notes**

If the non-Oracle messaging link being accessed for the subscriber uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Database Advanced Queuing queues. Otherwise the native Oracle Database Advanced Queuing interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections.

When propagating from a JMS source, the subscriber rule cannot be altered. Instead, the subscriber must be removed and added with the new rule. For JMS, changing the message selector on a durable subscription is equivalent to deleting and re-creating the subscription.

Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be `DBMS_MGWADM.NO_CHANGE` (the default value).

The `options` parameter specifies a set of properties used to alter the current optional properties. Each property affects the current property list in a particular manner: add a new property, replace an existing property, remove an existing property, or remove all properties.

**See Also:**

- SYS.MGW\_PROPERTIES Object Type for more information on the options parameter
- [“WebSphere MQ System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1901) for more information about WebSphere MQ subscriber options
- [“TIB/Rendezvous System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1902) for more information about TIB/Rendezvous subscriber options
- “ OUTBOUND\_PROPAGATION Subscribers for outbound propagation parameter interpretation
- “ INBOUND\_PROPAGATION Subscribers for inbound propagation parameter interpretation

### CLEANUP\_GATEWAY Procedures

This procedure cleans up Messaging Gateway. The procedure performs cleanup or recovery actions that may be needed when Messaging Gateway is left in some abnormal or unexpected condition. The `MGW_GATEWAY` view lists Messaging Gateway status and configuration information that pertains to the cleanup actions.

**Syntax**

```md
DBMS_MGWADM.CLEANUP_GATEWAY(
   action       IN   BINARY_INTEGER,
   sarg         IN   VARCHAR2 DEFAULT NULL);
```
```md
DBMS_MGWADM.CLEANUP_GATEWAY(
   agent_name   IN   VARCHAR2,   action       IN   BINARY_INTEGER,   sarg         IN   VARCHAR2 DEFAULT NULL );
```

**Parameters**

Table 27 CLEANUP\_GATEWAY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `action` | The cleanup action to be performed. Values:  - `DBMS_MGWADM.CLEAN_STARTUP_STATE` for Messaging Gateway start up state recovery - `DBMS_MGWADM.CLEAN_LOG_QUEUES` for log queue cleanup - `DBMS_MGWADM.RESET_SUB_MISSING_LOG_REC` for propagation job recovery due to missing log record - `DBMS_MGWADM.RESET_SUB_MISSING_MESSAGE` for propagation job recovery due to missing message |
| `sarg` | Optional argument whose meaning depends on the value specified for `action`. This should be `NULL` if it is not used for the specified action. |
| `agent_name` | Identifies the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |

**Usage Notes**

CLEAN\_STARTUP\_STATE

`sarg` is not used and must be `NULL`.

The `CLEAN_STARTUP_STATE` action recovers Messaging Gateway to a known state when the Messaging Gateway agent has crashed or some other abnormal event occurs, and Messaging Gateway cannot be restarted. This should be done only when the Messaging Gateway agent has been started but appears to have crashed or has been nonresponsive for an extended period of time.

The `CLEAN_STARTUP_STATE` action may be needed when the `MGW_GATEWAY` view shows that the `AGENT_STATUS` value is something other than `NOT_STARTED` or `START_SCHEDULED,` and the `AGENT_PING` value is `UNREACHABLE` for an extended period of time.

If the `AGENT_STATUS` value is `BROKEN`, then the Messaging Gateway agent cannot be started until the problem has been resolved and the `CLEAN_STARTUP_STATE` action used to reset the agent status. A `BROKEN` status can indicate that the Messaging Gateway start job detected a Messaging Gateway agent already running. This condition that should never occur under normal use.

Cleanup tasks include:

- Removing the Scheduler job used to start the external Messaging Gateway agent process.
- Setting certain configuration information to a known state. For example, setting the agent status to `NOT_STARTED.`

Execution of this command fails if:

- The agent status is `NOT_STARTED` or `START_SCHEDULED.`
- No shutdown attempt has been made prior to calling this procedure, except if the agent status is `STARTING.`
- The Messaging Gateway agent is successfully contacted.
	The assumption is that the agent is active, and this procedure fails. If the agent does not respond after several attempts have been made, then the cleanup tasks are performed. This procedure takes at least several seconds and possibly up to one minute. This is expected behavior under conditions where this particular cleanup action is appropriate and necessary.

**Note:** Terminate any Messaging Gateway agent process that may still be running after a `CLEAN_STARTUP_STATE` action has been successfully performed. This should be done before calling `DBMS_MGWADM`.`STARTUP` to start Messaging Gateway. The process is usually named `extprocmgwextproc`.

CLEAN\_LOG\_QUEUES

`sarg` is not used and must be `NULL`.

The Messaging Gateway agent will clean log queues for all configured messaging system links. The agent will temporarily stop all propagation activity and then remove all obsolete and bad log records from the log queues for all links. The procedure will fail if the Messaging Gateway agent is not running.

This cleanup action is automatically performed each time the Messaging Gateway agent is started.

**Note:** The `CLEAN_LOG_QUEUES` action is performed only on agent startup. If this procedure is called when the agent is running, then the Messaging Gateway agent ignores it.

RESET\_SUB\_MISSING\_LOG\_REC

`sarg` specifies a Messaging Gateway job name (or subscriber ID) to be reset. It must not be `NULL`.

The Messaging Gateway agent recovers a Messaging Gateway propagation job that has failed due to a missing log record. The agent will reset the source and destination log records. The procedure will fail if the Messaging Gateway agent is not running.

**Note:** If the messages in the source queue had already been propagated to the destination queue, then this action may result in duplicate messages.

RESET\_SUB\_MISSING\_MESSAGE

`sarg` specifies a Messaging Gateway job name (or subscriber ID) to be reset. It must not be `NULL`.

The Messaging Gateway agent recovers a Messaging Gateway propagation job that has failed due to a missing persistent source message. The agent will treat the message as a non-persistent message and continue processing that propagation job. The procedure will fail if the Messaging Gateway agent is not running.

### CREATE\_AGENT Procedure

This procedure creates a Messaging Gateway agent that will be used to process propagation jobs.

**Syntax**

```md
DBMS_MGWADM.CREATE_AGENT (
   agent_name     IN   VARCHAR2,
   username       IN   VARCHAR2 DEFAULT NULL,
   password       IN   VARCHAR2 DEFAULT NULL,
   database       IN   VARCHAR2 DEFAULT NULL,
   conntype       IN   VARCHAR2 DEFAULT DBMS_MGWADM.JDBC_OCI,
   max_memory     IN   PLS_INTEGER DEFAULT 64,
   max_threads    IN   PLS_INTEGER DEFAULT 1,
   service        IN   VARCHAR2 DEFAULT NULL,
   initfile       IN   VARCHAR2 DEFAULT NULL,
   comment        IN   VARCHAR2  DEFAULT NULL );
```

**Parameters**

Table 28 CREATE\_AGENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `agent_name` | A name used to identify the agent |
| `username` | Specifies the username used for connections to the Oracle Database |
| `password` | Specifies the password used for connections to the Oracle Database. A password must be specified if a username is specified. |
| `database` | Specifies the database connect string used for connections to the Oracle Database. `NULL` indicates that a local connection should be used. A value can be specified only if username is specified. Oracle strong recommends that a connect string, rather than `NULL` be specified. Usually it will be a net service name from `tnsnames`.`ora`. |
| `conntype` | Specifies the type of connection to the Oracle Database.Values: `DBMS_MGWADM`.`JDBC_OCI`, `DBMS_MGWADM`.`JDBC_THIN` |
| `max_memory` | Specifies the maximum heap size, in MB, used by the Messaging Gateway agent |
| `max_threads` | Specifies the number of messaging threads that the Messaging Gateway agent creates. This determines the number of propagation jobs that the agent can concurrently process. The maximum value of `max_threads` is limited to 128. |
| `service` | Specifies the database service that the Oracle Scheduler job class used by this agent will have affinity to. In an Oracle RAC environment, this means that the Messaging Gateway agent will only run on those database instances that are assigned to the service. If NULL, then the job class will belong to the default service which is mapped to every instance. |
| `initfile` | Specifies a Messaging Gateway initialization file used by this agent. NULL indicates that the default initialization file is used. If a value is specified, it should be the full path name of the file. |
| `comment` | An optional comment for this agent. `NULL` if one is not desired. |

**Usage Notes**

- The Messaging Gateway automatically configures a default agent when Messaging Gateway is installed. The name of the default agent is `DEFAULT_AGENT`. This procedure can be used to create additional agents.
- The `username`, `password`, and `database` parameters specify connection information used by the Messaging Gateway agent for connections to the Oracle Database. An Oracle administrator should create the database user and grant it the role `MGW_AGENT_ROLE`. It is not mandatory that the connection information be specified when this procedure is called but it must be set before the agent can be started.
- The `service` parameter is used to create an Oracle Scheduler job class. The job class is used to create a Scheduler job that starts the Messaging Gateway agent. An Oracle administrator must create the database service. If the value is `NULL`, the job class will belong to an internal service that is mapped to all instances.

### CREATE\_JOB Procedure

This procedure creates a job used to propagate message from a source to a destination.

**Syntax**

```md
DBMS_MGWADM.CREATE_JOB (
   job_name           IN   VARCHAR2,
   propagation_type   IN   PLS_INTEGER,
   source             IN   VARCHAR2,
   destination        IN   VARCHAR2,
   rule               IN   VARCHAR2 DEFAULT NULL,
   transformation     IN   VARCHAR2 DEFAULT NULL,
   exception_queue    IN   VARCHAR2 DEFAULT NULL,
   poll_interval      IN   PLS_INTEGER DEFAULT NULL,
   options            IN   SYS.MGW_PROPERTIES DEFAULT NULL,
   enabled            IN   BOOLEAN DEFAULT TRUE,
   comments           IN   VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 29 CREATE\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `job_name` | A user defined name to identify the propagation job |
| `propagation_type` | Specifies the type of message propagation.  - `DBMS_MGWADM`.`OUTBOUND_PROPAGATION` for Oracle Streams AQ to non-Oracle propagation. - `DBMS_MGWADM`.`INBOUND_PROPAGATION` for non-Oracle to Oracle Streams AQ propagation. |
| `source` | Specifies the source queue whose messages are to be propagated. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `destination` | Specifies the destination queue to which messages are propagated. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `rule` | Specifies an optional subscription rule used to dequeue messages from the source queue. This should be `NULL` if no rule is needed. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `transformation` | Specifies the transformation needed to convert between the Oracle Streams AQ payload and an ADT defined by Messaging Gateway. The type of transformation needed depends on the value specified for `propagation_type`.  If no transformation is specified the Oracle Streams AQ payload type must be supported by Messaging Gateway. |
| `exception_queue` | Specifies a queue used for exception message logging purposes. This queue must be on the same messaging system as the propagation source. If `NULL`, an exception queue will not be used and propagation will stop if a problem occurs. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`.  The source queue and exception queue cannot be the same queue. |
| `poll_interval` | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available.  Values: `NULL` or value > 0. If `NULL`, then the Messaging Gateway default polling interval will be used. The default polling interval is 5 seconds and can be overridden by the Messaging Gateway initialization file. |
| `options` | Optional job properties, `NULL` if there are none. Typically these are lesser used configuration properties supported by the messaging system. |
| `enabled` | Specifies whether this propagation job is enabled after creation. Values: `TRUE`, `FALSE`.  - If `TRUE` (default), the job will be enabled after it is created. - If `FALSE`, the job will be disabled after it is created. A propagation job must be enabled and the Messaging Gateway agent running before messages can be propagated. |
| `comments` | An optional comment for this job. `NULL` if one is not desired. |

**Usage Notes**

- The job must be enabled and Messaging Gateway agent started in order for messages to be propagated.
- If the non-Oracle messaging link being accessed for the propagation job uses a JMS interface, then the Messaging Gateway agent will use the Oracle JMS interface to access the Oracle Streams AQ queues. Otherwise the native Oracle Streams AQ interface will be used. Parameters are interpreted differently when the Messaging Gateway agent uses Oracle JMS for JMS connections.
- Transformations are not currently supported if the Oracle JMS interface is used for propagation. The transformation parameter must be `NULL`.

OUTBOUND\_PROPAGATION Jobs

The parameters for an outbound propagation job are interpreted as follows:

- `source` specifies the local Oracle Streams AQ queue that is the propagation source. This must have syntax of schema.queue. This can be either a multiple consumer queue or a single consumer queue.
- `destination` specifies the non-Oracle queue to which messages are propagated. This must have syntax of `registered_queue` @ `message_link`.
- `rule` specifies an optional Oracle Streams AQ subscriber rule if the native Oracle Stream AQ interface is used, or a JMS selector if the Oracle JMS interface is used. If `NULL`, then no rule or selector is used. This parameter must be `NULL` if the native Oracle Stream AQ interface is used and the propagation source is a single consumer queue.
- `transformation` specifies the transformation used to convert the Oracle Streams AQ payload to an ADT defined by Messaging Gateway. The full transformation name (`schema`.`name`) should be used if one is specified.
	Messaging Gateway propagation dequeues messages from the Oracle Streams AQ queue using the transformation to convert the Oracle Streams AQ payload to a known ADT defined by Messaging Gateway. The message is then enqueued in the non-Oracle messaging system based on the Messaging Gateway ADT.
- `exception_queue` specifies the name of a local Oracle Streams AQ queue to which messages are moved if an exception occurs. The syntax must be `schema`.`queue`.
	If the native Oracle Streams AQ interface is used and the source is a multiple consumer queue, then a subscriber will be added to the Oracle Streams AQ queue when this procedure is called, whether or not the Messaging Gateway agent is running. The local subscriber will be of the form `sys`.`aq$_agent` (‘ `MGW_job_name` ’, `NULL`, `NULL`).
	If the Oracle JMS interface is used, then the Messaging Gateway agent will create a JMS durable subscriber with the name of `MGW_job_name`. If the agent is not running when this procedure is called, then the durable subscriber will be created the next time the agent starts.
	The exception queue has the following conditions:
	- The user is responsible for creating the Oracle Streams AQ queue to be used as the exception queue.
		- The payload type of the source queue and exception queue must match.
		- The exception queue must be created as a queue type of `DBMS_AQADM`.`NORMAL_QUEUE`. Enqueue restrictions prevent Messaging Gateway from using an Oracle Streams AQ queue of type `DBMS_AQADM`.`EXCEPTION_QUEUE` as a Messaging Gateway exception queue.

INBOUND\_PROPAGATION Jobs

The parameters for an inbound propagation job are interpreted as follows:

- `source` specifies the non-Oracle queue that is the propagation source. The syntax must be `registered_queue` @ `message_link`.
- `destination` specifies the local Oracle Streams AQ queue to which messages are propagated. The syntax must be `schema`.`queue`.
- `rule` specifies an optional subscriber rule that is valid for the non-Oracle messaging system. This should be `NULL` if no rule is needed.
- `transformation` specifies the transformation used to convert an ADT defined by Messaging Gateway to the Oracle Streams AQ payload type. The full transformation name (`schema`.`name`) should be used if one is specified
	Messaging Gateway propagation dequeues messages from the non-Oracle messaging system and converts the message body to a known ADT defined by Messaging Gateway. The transformation is used to convert the Messaging Gateway ADT to an Oracle Streams AQ payload type when the message is enqueued to the Oracle Streams AQ queue.
- `exception_queue` specifies the name of a registered non-Oracle queue to which messages are moved if an exception occurs. The syntax must be `registered_queue@message_link`.
	Whether or not a subscriber is needed for the source queue depends on the requirements of the non-Oracle messaging system. If a durable subscriber is necessary, then the Messaging Gateway agent will create it. If the agent is not running when this procedure is called, then the subscriber will be created on the non-Oracle messaging system the next time the agent starts.
	The exception queue has the following conditions:
	- The exception queue must be a registered non-Oracle queue.
		- The source queue and exception queue must use the same messaging system link.

### CREATE\_MSGSYSTEM\_LINK Procedures for TIB/Rendezvous

This procedure creates a link to a TIB/Rendezvous messaging system.

**Syntax**

```md
DBMS_MGWADM.CREATE_MSGSYSTEM_LINK (
   linkname     IN  VARCHAR2,
   properties   IN  SYS.MGW_TIBRV_PROPERTIES,
   options      IN  SYS.MGW_PROPERTIES DEFAULT NULL,
   comment      IN  VARCHAR2 DEFAULT NULL );
```
```md
DBMS_MGWADM.CREATE_MSGSYSTEM_LINK (
   linkname     IN  VARCHAR2,
   agent_name   IN  VARCHAR2,
   properties   IN  SYS.MGW_TIBRV_PROPERTIES,
   options      IN  SYS.MGW_PROPERTIES DEFAULT NULL,
   comment      IN  VARCHAR2 DEFAULT NULL );
```

**Parameters**

Table 30 CREATE\_MSGSYSTEM\_LINK Procedure Parameters for TIB/Rendezvous

| Parameter | Description |
| --- | --- |
| `linkname` | A user-defined name to identify this messaging system link |
| `properties` | Basic properties of a TIB/Rendezvous messaging system link. |
| `options` | Optional link properties. `NULL` if there are none. These are less frequently used configuration properties supported by the messaging system |
| `comment` | A user-specified description. `NULL` if one is not desired. |
| `agent_name` | Specifies the Messaging Gateway agent that will be used to process all propagation jobs associated with this link. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |

**Usage Notes**

The Messaging Gateway default agent will process the propagation jobs associated with this link if an agent name is not specified.

**See Also:** [“TIB/Rendezvous System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1902) for more information about the messaging system properties and options

### CREATE\_MSGSYSTEM\_LINK Procedures for WebSphere MQ

This procedure creates a messaging system link to a WebSphere MQ messaging system.

**Syntax**

```md
DBMS_MGWADM.CREATE_MSGSYSTEM_LINK(
   linkname    IN VARCHAR2,
   properties  IN SYS.MGW_MQSERIES_PROPERTIES,
   options     IN SYS.MGW_PROPERTIES DEFAULT NULL,
   comment     IN VARCHAR2 DEFAULT NULL);
```
```md
DBMS_MGWADM.CREATE_MSGSYSTEM_LINK(
   linkname    IN VARCHAR2,
   agent_name  IN  VARCHAR2,
   properties  IN SYS.MGW_MQSERIES_PROPERTIES,
   options     IN SYS.MGW_PROPERTIES DEFAULT NULL,
   comment     IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 31 CREATE\_MSGSYSTEM\_LINK Procedure Parameters for WebSphere MQ

| Parameter | Description |
| --- | --- |
| `linkname` | A user-defined name to identify the messaging system link |
| `properties` | Basic properties of a WebSphere MQ messaging system link |
| `options` | Optional link properties. `NULL` if there are none. These are less frequently used configuration properties supported by the messaging system. |
| `comment` | A user-specified description. `NULL` if one is not desired |
| `agent_name` | Specifies the Messaging Gateway agent that will be used to process all propagation jobs associated with this link. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |

**Usage Notes**

The Messaging Gateway default agent will process the propagation jobs associated with this link if an agent name is not specified.

**See Also:** [“WebSphere MQ System Properties” in *Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1901) for more information about the messaging system properties and options

### DB\_CONNECT\_INFO Procedure

This deprecated procedure configures connection information used by the Messaging Gateway default agent for connections to Oracle Database.

**Note:** This subprogram has been deprecated as a result of improved technology (see ALTER\_AGENT Procedures), and is retained only for reasons of backward compatibility.

.infoboxnote}

**Syntax**

```md
DBMS_MGWADM.DB_CONNECT_INFO (
   username      IN VARCHAR2,
   password      IN VARCHAR2,
   database      IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 32 DB\_CONNECT\_INFO Procedure Parameters

| Parameter | Description |
| --- | --- |
| `username` | The username used for connections to Oracle Database. `NULL` is not allowed |
| `password` | The password used for connections to Oracle Database. `NULL` is not allowed |
| `database` | The database connect string used by the Messaging Gateway agent. `NULL` indicates that a local connection should be used.  Oracle strongly recommends that a not `NULL` value be specified. Usually it will be a net service name from `tnsnames.ora`. |

**Usage Notes**

The Messaging Gateway agent connects to Oracle Database as the user configured by this procedure. An Oracle administrator should create the user, grant it the role `MGW_AGENT_ROLE,` and then call this procedure to configure Messaging Gateway. Role `MGW_AGENT_ROLE` is used to grant this user special privileges needed to access Messaging Gateway configuration information stored in the database, enqueue or dequeue messages to and from Oracle Database Advanced Queuing queues, and perform certain Oracle Database Advanced Queuing administration tasks.

### DISABLE\_JOB Procedure

This procedure disables a propagation job.

**Syntax**

```md
DBMS_MGWADM.DISABLE_JOB (
   job_name  IN VARCHAR2);
```

**Parameters**

Table 33 DISABLE\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| job\_name | Identifies the propagation job |

### DISABLE\_PROPAGATION\_SCHEDULE Procedure

This **deprecated procedure** disables a propagation schedule.

**Note:** This subprogram has been deprecated as a result of improved technology (see DISABLE\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
DBMS_MGWADM.DISABLE_PROPAGATION_SCHEDULE (
   schedule_id  IN VARCHAR2);
```

**Parameters**

Table 34 DISABLE\_PROPAGATION\_SCHEDULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_id` | Identifies the propagation schedule to be disabled |

### ENABLE\_JOB Procedure

This procedure enables a propagation job.

**Syntax**

```md
DBMS_MGWADM.ENABLE_JOB (
   job_name  IN VARCHAR2 );
```

**Parameters**

Table 35 ENABLE\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `job_name` | Identifies the propagation job |

### ENABLE\_PROPAGATION\_SCHEDULE Procedure

This deprecated procedure enables a propagation schedule.

**Note:** This subprogram has been deprecated as a result of improved technology (see ENABLE\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
DBMS_MGWADM.ENABLE_PROPAGATION_SCHEDULE (
   schedule_id  IN VARCHAR2 );
```

**Parameters**

Table 36 ENABLE\_PROPAGATION\_SCHEDULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_id` | Identifies the propagation schedule to be enabled |

### REGISTER\_FOREIGN\_QUEUE Procedure

This procedure registers a non-Oracle queue entity in Messaging Gateway.

**Syntax**

```md
DBMS_MGWADM.REGISTER_FOREIGN_QUEUE(
   name            IN VARCHAR2,
   linkname        IN VARCHAR2,
   provider_queue  IN VARCHAR2 DEFAULT NULL,
   domain          IN INTEGER DEFAULT NULL,
   options         IN SYS.MGW_PROPERTIES DEFAULT NULL,
   comment         IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 37 REGISTER\_FOREIGN\_QUEUE Procedure Parameters

| Parameters | Description |
| --- | --- |
| `name` | The registered queue name. This name identifies the foreign queue within Messaging Gateway and need not match the name of the queue in the foreign messaging system. |
| `linkname` | The link name for the messaging system on which this queue exists |
| `provider_queue` | The message provider (native) queue name. If `NULL,` then the value provided for the `name` parameter is used as the provider queue name. |
| `domain` | The domain type of the queue. `NULL` means the domain type is automatically determined based on the messaging system of the queue. `DBMS_MGWADM.DOMAIN_QUEUE` is for a queue (point-to-point model). `DBMS_MGWADM.DOMAIN_TOPIC` is for a topic (publish-subscribe model). |
| `options` | Optional queue properties |
| `comment` | A user-specified description. Can be `NULL`. |

**Usage Notes**

This procedure does not create the physical queue in the non-Oracle messaging system. The non-Oracle queue must be created using the administration tools for that messaging system.

**See Also:** For more information when registering queues for the WebSphere MQ messaging system or the TIB/Rendezvous messaging system, specifically “Optional Foreign Queue Configuration Properties” in [*Oracle Database Advanced Queuing User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADQUE1904).

### REMOVE\_AGENT Procedure

This procedure removes a Messaging Gateway agent.

**Syntax**

```md
DBMS_MGWADM.REMOVE_AGENT(
   agent_name   IN   VARCHAR2 );
```

**Parameters**

Table 38 REMOVE\_AGENT Procedure Parameters

| Parameters | Description |
| --- | --- |
| `agent_name` | Identifies the Messaging Gateway agent |

**Usage Notes**

All messaging system links associated with this Messaging Gateway agent must be removed and the agent must be stopped before it can be removed. The Messaging Gateway default agent cannot be removed.

### REMOVE\_JOB Procedure

This procedure removes a propagation job.

**Syntax**

```md
DBMS_MGWADM.REMOVE_JOB(
   job_name   IN   VARCHAR2,   force      IN   PLS_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE);
```

**Parameters**

Table 39 REMOVE\_JOB Procedure Parameters

| Parameters | Description |
| --- | --- |
| `job_name` | Identifies the propagation job |
| force | Specifies whether the procedure should succeed even if Messaging Gateway is not able to perform all cleanup actions pertaining to this propagation job.  Values: `DBMS_MGWADM`.`NO_FORCE`, `DBMS_MGWADM`.`FORCE`  - `NO_FORCE` (default) means the job is not removed if Messaging Gateway is unable to clean up successfully - `FORCE` means the job is removed even though all cleanup actions may not be done |

**Usage Notes**

- The Messaging Gateway agent uses various resources of the Oracle Database and the non-Oracle messaging system for its propagation work. These resources need to be released when the job is removed. For example, Messaging Gateway may create a durable subscriber on the source queue that should be removed when the job is removed. Therefore, this procedure should normally be called when the Messaging Gateway agent is running and able to access the non-Oracle messaging system associated with this job.
- For outbound propagation, a local subscriber is removed from the Oracle Streams AQ queue when the propagation source is a multiple consumer queue.

### REMOVE\_MSGSYSTEM\_LINK Procedure

This procedure removes a messaging system link for a non-Oracle messaging system.

**Syntax**

```md
DBMS_MGWADM.REMOVE_MSGSYSTEM_LINK(
   linkname  IN VARCHAR2);
```

**Parameters**

Table 40 REMOVE\_MSGSYSTEM\_LINK Procedure Parameters

| Parameters | Description |
| --- | --- |
| `linkname` | The messaging system link name |

**Usage Notes**

All registered queues associated with this link must be removed before the messaging system link can be removed. This procedure fails if there is a registered foreign (non-Oracle) queue that references this link.

### REMOVE\_OPTION Procedure

This procedure removes a Messaging Gateway configuration option. It can be used to remove an agent option, a messaging link option, or a propagation job option.

**Syntax**

```md
DBMS_MGWADM.REMOVE_OPTION (
   target_type   IN   PLS_INTEGER,
   target_name   IN   VARCHAR2,
   option_name   IN   VARCHAR2);
```

**Parameters**

Table 41 REMOVE\_OPTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `target_type` | Specifies the target type of the Messaging Gateway entity:  - `DBMS_MGWADM`.`AGENT_JAVA_PROP` to remove a Java System property for a Messaging Gateway agent - `DBMS_MGWADM`.`MSGLINK_OPTION` to remove a messaging link option - `DBMS_MGWADM`.`JOB_OPTION` to remove a propagation job option |
| `target_name` | Name or identifier of the target. The value for this parameter depends on the value specified for `target_type` parameter. This must not be `NULL`. |
| option\_name | Option name. This must not be `NULL`. |

**See Also:** Table 118-10 regarding options for the `option_type` parameter

**Usage Notes**

DBMS\_MGWADM.AGENT\_JAVA\_PROP Target

The procedure removes an agent option used to set a Java System property when the Messaging Gateway agent is started. The agent must be restarted for the change to take effect.

The parameters are interpreted as follows:

- `target_name` specifies the name of the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` can be used for the default agent.
- `option_name` specifies the Java System property
- `encrypted` can be either `TRUE` or `FALSE`

DBMS\_MGWADM.MSGLINK\_OPTION Target

The procedure removes a single option for a Messaging Gateway messaging system link. This is equivalent to calling `DBMS_MGWADM`.`ALTER_MSGSYSTEM_LINK` and using the options parameter to remove an option.

The parameters are interpreted as follows:

- `target_name` specifies the name of the message system link
- `option_name` specifies the option to set
- `encrypted` must be `FALSE`

DBMS\_MGWADM.JOB\_OPTION Target

The procedure removes a single option for a Messaging Gateway propagation job. This is equivalent to calling `DBMS_MGWADM`.`ALTER_JOB` and using the options parameter to remove an option.

The parameters are interpreted as follows:

- `target_name` specifies the name of the propagation job
- `option_name` specifies the option to set
- `encrypted` must be `FALSE`

### REMOVE\_SUBSCRIBER Procedure

This procedure removes a subscriber used to consume messages from a source queue for propagation to a destination.

**Note:** This subprogram has been deprecated as a result of improved technology (see REMOVE\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
DBMS_MGWADM.REMOVE_SUBSCRIBER (
   subscriber_id  IN VARCHAR2,
   force          IN BINARY_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE );
```

**Parameters**

Table 42 REMOVE\_SUBSCRIBER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `subscriber_id` | Identifies the subscriber to be removed |
| `force` | Specifies whether this procedure should succeed even if Messaging Gateway is not able to perform all cleanup actions pertaining to this subscriber.  Values: `DBMS_MGWADM`.`NO_FORCE`, `DBMS_MGWADM`.`FORCE`  - `NO_FORCE` means the subscriber is not removed if Messaging Gateway is unable to clean up successfully (default) - `FORCE` means the subscriber is removed even though all cleanup actions may not be done |

**Usage Notes**

- The Messaging Gateway agent uses various resources of Oracle Database and the non-Oracle messaging system for its propagation work. These resources are typically associated with each subscriber and need to be released when the subscriber is no longer needed. Therefore, this procedure should only be called when the Messaging Gateway agent is running and able to access the non-Oracle messaging system associated with this subscriber.
- For outbound propagation, a local subscriber is removed from the Oracle Database Advanced Queuing queue.

### RESET\_JOB Procedure

This procedure resets the propagation error state for a propagation job.

**Syntax**

```md
DBMS_MGWADM.RESET_JOB (
   job_name   IN   VARCHAR2);
```

**Parameters**

Table 43 RESET\_JOB Procedure Parameters

| Parameter | Description |
| --- | --- |
| `job_name` | Identifies the propagation job |

**Usage Notes**

This procedure can be used to reset a propagation job that has been set to a failed state and propagation activities have been stopped. The administrator should correct the problem and then call this procedure to allow the agent to retry the propagation job. The `STATUS` field of the `MGW_JOBS` view indicates the job status.

### RESET\_SUBSCRIBER Procedure

This procedure resets the propagation error state for a subscriber.

**Note:** This subprogram has been deprecated as a result of improved technology (see RESET\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
DBMS_MGWADM.RESET_SUBSCRIBER (
   subscriber_id  IN VARCHAR2 );
```

**Parameters**

Table 44 RESET\_SUBSCRIBER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `subscriber_id` | Identifies the subscriber |

### SCHEDULE\_PROPAGATION Procedure

This procedure schedules message propagation from a source to a destination.

The schedule must be enabled and Messaging Gateway started in order for messages to be propagated.

**Note:** This subprogram has been deprecated as a result of improved technology (see CREATE\_JOB Procedure), and is retained only for reasons of backward compatibility.

**Syntax**

```md
DBMS_MGWADM.SCHEDULE_PROPAGATION (
   schedule_id       IN VARCHAR2,
   propagation_type  IN BINARY_INTEGER,
   source            IN VARCHAR2,
   destination       IN VARCHAR2,
   start_time        IN DATE DEFAULT SYSDATE,
   duration          IN NUMBER DEFAULT NULL,
   next_time         IN VARCHAR2 DEFAULT NULL,
   latency           IN NUMBER DEFAULT NULL);
```

**Parameters**

Table 45 SCHEDULE\_PROPAGATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_id` | Specifies a user-defined name that identifies the schedule |
| `propagation_type` | Specifies the type of message propagation. `DBMS_MGWADM.OUTBOUND_PROPAGATION` is for Oracle Database Advanced Queuing to non-Oracle propagation. `DBMS_MGWADM.INBOUND_PROPAGATION` is for non-Oracle to Oracle Database Advanced Queuing propagation. |
| `source` | Specifies the source queue whose messages are to be propagated. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `destination` | Specifies the destination queue to which messages are propagated. The syntax and interpretation of this parameter depend on the value specified for `propagation_type`. |
| `start_time` | Reserved for future use |
| `duration` | Reserved for future use |
| `next_time` | Reserved for future use |
| `latency` | Specifies the polling interval, in seconds, used by the Messaging Gateway agent when checking for messages in the source queue. If no messages are available in the source queue, then the agent will not poll again until the polling interval has passed. Once the agent detects a message it will continue propagating messages as long as any are available.  Values: `NULL` or value > 0. If `latency` is `NULL`, then the Messaging Gateway agent default polling interval will be used. The default polling interval is 5 seconds but it can be overridden by the Messaging Gateway initialization file. |

**Usage Notes**

For outbound propagation, parameters are interpreted as follows:

- `source` specifies the local Oracle Database Advanced Queuing queue from which messages are propagated. This must have a syntax of `schema.queue`.
- `destination` specifies the foreign queue to which messages are propagated. This must have a syntax of `registered_queue@message_link`.

For inbound propagation, parameters are interpreted as follows:

- `source` specifies the foreign queue from which messages are propagated. This must have a syntax of `registered_queue@message_link`.
- `destination` specifies the local Oracle Database Advanced Queuing queue to which messages are propagated. This must have a syntax of `schema.queue`.

The schedule is set to an enabled state when it is created.

### SET\_LOG\_LEVEL Procedures

This procedure dynamically alters the Messaging Gateway agent logging level. The Messaging Gateway agent must be running.

**Syntax**

```md
DBMS_MGWADM.SET_LOG_LEVEL (
   log_level    IN   BINARY_INTEGER);
```
```md
DBMS_MGWADM.SET_LOG_LEVEL (
   agent_name   IN   VARCHAR2,
   log_level    IN   BINARY_INTEGER);
```

**Parameters**

Table 46 SET\_LOG\_LEVEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `log_level` | Level at which the Messaging Gateway agent logs information. `DBMS_MGWADM.BASIC_LOGGING` generates the least information while `DBMS_MGWADM.TRACE_DEBUG_LOGGING` generates the most information. |
| `agent_name` | Identifies the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |

**See Also:** Table 118-3 for details on the `log_level` parameter

### SET\_OPTION Procedure

This procedure sets a Messaging Gateway configuration option. It can be used to set an agent option, a messaging link option, or a propagation job option.

**Syntax**

```md
DBMS_MGWADM.SET_OPTION (
   target_type   IN   PLS_INTEGER,
   target_name   IN   VARCHAR2,
   option_name   IN   VARCHAR2,
   option_value  IN   VARCHAR2,
   encrypted     IN   BOOLEAN DEFAULT FALSE );
```

**Parameters**

Table 47 SET\_OPTION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `target_type` | Specifies the target type of the Messaging Gateway entity:  - `DBMS_MGWADM`.`AGENT_JAVA_PROP` to set a Java System property for a Messaging Gateway agent - `DBMS_MGWADM`.`MSGLINK_OPTION` to set a messaging link option - `DBMS_MGWADM`.`JOB_OPTION` to set a propagation job option |
| `target_name` | Name or identifier of the target. The value for this parameter depends on the value specified for `target_type` parameter. This must not be `NULL`. |
| option\_name | Option name. This must not be `NULL`. |
| `option_value` | Option value |
| `encrypted` | Indicates whether the value should be stored as encrypted:  - `TRUE` if the value should be stored in an encrypted form - `FALSE` if the value should be stored in a cleartext form |

**See Also:** Table 118-10 regarding options for the `option_type` parameter

**Usage Notes**

DBMS\_MGWADM.AGENT\_JAVA\_PROP Target

The procedure will store an agent option used to set a Java System property when the Messaging Gateway agent is started. The agent must be restarted for the change to take effect.

The parameters are interpreted as follows:

- `target_name` specifies the name of the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` can be used for the default agent.
- `option_name` specifies the Java System property
- `encrypted` can be either `TRUE` or `FALSE`

DBMS\_MGWADM.MSGLINK\_OPTION Target

The procedure will set or alter a single option for a Messaging Gateway messaging system link. This is equivalent to calling `DBMS_MGWADM`.`ALTER_MSGSYSTEM_LINK` and using the options parameter to set an option.

The parameters are interpreted as follows:

- `target_name` specifies the name of the message system link
- `option_name` specifies the option to set
- `encrypted` must be `FALSE`

DBMS\_MGWADM.JOB\_OPTION Target

The procedure will set or alter a single option for a Messaging Gateway propagation job. This is equivalent to calling `DBMS_MGWADM`.`ALTER_JOB` and using the options parameter to set an option.

The parameters are interpreted as follows:

- `target_name` specifies the name of the propagation job
- `option_name` specifies the option to set
- `encrypted` must be `FALSE`

### SHUTDOWN Procedures

This procedure shuts down the Messaging Gateway agent. No propagation activity occurs until Messaging Gateway is restarted.

**Syntax**

```md
DBMS_MGWADM.SHUTDOWN (
   sdmode      IN BINARY_INTEGER DEFAULT DBMS_MGWADM.SHUTDOWN_NORMAL);
```
```md
DBMS_MGWADM.SHUTDOWN (
   agent_name  IN VARCHAR2);
```

**Parameters**

Table 48 SHUTDOWN Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sdmode` | The shutdown mode. The only value currently supported is `DBMS_MGWADM.SHUTDOWN_NORMAL` for normal shutdown. The Messaging Gateway agent may attempt to complete any propagation work currently in progress. |
| `agent_name` | Identifies the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |

**Usage Notes**

The Messaging Gateway default agent is shut down if no agent name is specified.

### STARTUP Procedures

This procedure starts the Messaging Gateway agent. It must be called before any propagation activity can take place.

**Syntax**

```md
DBMS_MGWADM.STARTUP(
   instance       IN  BINARY_INTEGER DEFAULT 0,
   force          IN  BINARY_INTEGER DEFAULT DBMS_MGWADM.NO_FORCE);
```
```md
DBMS_MGWADM.STARTUP(
   agent_name     IN  VARCHAR2);
```

**Parameters**

Table 49 STARTUP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `instance` | Specifies which instance can run the job queue job used to start the Messaging Gateway agent. If this is zero, then the job can be run by any instance.  Caution: This parameter has been deprecated. |
| `force` | If this is `DBMS_MGWADM.FORCE`, then any positive integer is acceptable as the job instance. If this is `DBMS_MGWADM.NO_FORCE` (the default), then the specified instance must be running; otherwise the routine raises an exception.  Caution: This parameter has been deprecated. |
| `agent_name` | Identifies the Messaging Gateway agent. `DBMS_MGWADM`.`DEFAULT_AGENT` specifies the default agent. |

**Usage Notes**

- The Messaging Gateway default agent will be started if an agent name is not specified.
- The `force` and `instance` parameters are no longer used and will be ignored. If the `instance` affinity parameters were being used to start the default agent on a specific instance, the administrator will need to create a database service and then assign that service to the default agent using the `DBMS_MGWADM`.`ALTER_AGENT` procedure.
- The Messaging Gateway agent cannot be started until an agent user has been configured by the `DBMS_MGWADM`.`CREATE_AGENT` or `DBMS_MGWADM`.`ALTER_AGENT` subprograms.

### UNREGISTER\_FOREIGN\_QUEUE Procedure

This procedure removes a non-Oracle queue entity in Messaging Gateway.

**Syntax**

```md
DBMS_MGWADM.UNREGISTER_FOREIGN_QUEUE(
   name         IN VARCHAR2,
   linkname     IN VARCHAR2);
```

**Parameters**

Table 50 UNREGISTER\_FOREIGN\_QUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `name` | The queue name |
| `linkname` | The link name for the messaging system on which the queue exists |

**Usage Notes**

- This procedure does not remove the physical queue in the non-Oracle messaging system.
- All propagation jobs, subscribers and schedules referencing this queue must be removed before it can be unregistered. This procedure fails if a propagation job, subscriber, or propagation schedule references the non-Oracle queue.

### UNSCHEDULE\_PROPAGATION Procedure

This deprecated procedure removes a propagation schedule.

**Syntax**

```md
DBMS_MGWADM.UNSCHEDULE_PROPAGATION (
   schedule_id   IN VARCHAR2 );
```

**Parameters**

Table 51 UNSCHEDULE\_PROPAGATION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `schedule_id` | Identifies the propagation schedule to be removed |