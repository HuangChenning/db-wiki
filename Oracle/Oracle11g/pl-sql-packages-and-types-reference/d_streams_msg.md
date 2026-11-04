---
title: DBMS_STREAMS_MESSAGING
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_streams_msg.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 149 DBMS\_STREAMS\_MESSAGING

The `DBMS_STREAMS_MESSAGING` package, one of a set of Oracle Streams packages, provides interfaces to enqueue messages into and dequeue messages from a `ANYDATA` queue.

This chapter contains the following topics:

- Using DBMS\_STREAMS\_MESSAGING
- Summary of DBMS\_STREAMS\_MESSAGING Subprograms

---

## Using DBMS\_STREAMS\_MESSAGING

This section contains topics which relate to using the `DBMS_CAPTURE_ADM` package.

---

### Overview

This package provides interfaces to enqueue messages into and dequeue messages from a `ANYDATA` queue.

Note:

Currently, messaging clients cannot dequeue buffered messages. In addition, the `DBMS_STREAMS_MESSAGING` package cannot be used to enqueue messages into or dequeue messages from a buffered queue. However, you can use the `DBMS_AQ` package to enqueue and dequeue buffered messages.

See Also:

- [Oracle Database 2 Day + Data Replication and Integration Guide](https://docs.oracle.com/cd/E11882_01/server.112/e17516/tdpii_messaging.htm#TDPII043) for more information about Oracle Streams and for an example that uses the procedures in this package
- [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for more information about queues, messaging, and the `DBMS_AQ` package

---

### Security Model

Security on this package can be controlled in either of the following ways:

- Granting `EXECUTE` on this package to selected users or roles.
- Granting `EXECUTE_CATALOG_ROLE` to selected users or roles.

If subprograms in the package are run from within a stored procedure, then the user who runs the subprograms must be granted `EXECUTE` privilege on the package directly. It cannot be granted through a role.

To ensure that the user who runs the subprograms in this package has the necessary privileges, configure an Oracle Streams administrator and connect as the Oracle Streams administrator when using this package.

See Also:

[Oracle Streams Replication Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10705/prep_rep.htm#STREP200) for information about configuring an Oracle Streams administrator

---

## Summary of DBMS\_STREAMS\_MESSAGING Subprograms

Table 149-1 DBMS\_STREAMS\_MESSAGING Package Subprograms

| Subprogram | Description |
| --- | --- |
| DEQUEUE Procedure | Uses the specified Oracle Streams messaging client to dequeue a message from the specified queue |
| ENQUEUE Procedure | The current user enqueues a message into the specified queue |

Note:

The subprograms in this package do not commit.

---

### DEQUEUE Procedure

This procedure uses the specified Oracle Streams messaging client to dequeue a message from the specified queue.

This procedure is overloaded. One version of this procedure contains the `msgid` `OUT` parameter, and the other does not.

Syntax

```
DBMS_STREAMS_MESSAGING.DEQUEUE(
   queue_name    IN   VARCHAR2,    
   streams_name  IN   VARCHAR2,    
   payload       OUT  ANYDATA,   
   dequeue_mode  IN   VARCHAR2        DEFAULT 'REMOVE',
   navigation    IN   VARCHAR2        DEFAULT 'NEXT MESSAGE',
   wait          IN   BINARY_INTEGER  DEFAULT FOREVER,
   msgid         OUT  RAW);

DBMS_STREAMS_MESSAGING.DEQUEUE(
   queue_name    IN   VARCHAR2,    
   streams_name  IN   VARCHAR2,    
   payload       OUT  ANYDATA,   
   dequeue_mode  IN   VARCHAR2        DEFAULT 'REMOVE',
   navigation    IN   VARCHAR2        DEFAULT 'NEXT MESSAGE',
   wait          IN   BINARY_INTEGER  DEFAULT FOREVER);
```

Parameters

Table 149-2 DEQUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | The name of the local queue from which messages will be dequeued, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be a secure queue of `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default. |
| `streams_name` | The name of the Oracle Streams messaging client. For example, if the user `strmadmin` is the messaging client, then specify `strmadmin`.  If `NULL` and a relevant messaging client for the queue exists, then the procedure uses the relevant messaging client. If `NULL` and multiple relevant messaging clients for the queue exist, then the procedure raises an error. |
| `payload` | The payload that is dequeued |
| `dequeue_mode` | Specify one of the following settings:  `REMOVE`: Read the message and delete it. This setting is the default. The message can be retained in the queue table based on the retention properties.  `LOCKED`: Read and obtain a write lock on the message. The lock lasts for the duration of the transaction. This setting is equivalent to a select for update statement.  `BROWSE`: Read the message without acquiring any lock on the message. This specification is equivalent to a select statement. |
| `navigation` | The position of the message that will be retrieved. First, the position is determined. Second, the search criterion is applied. Finally, the message is retrieved.  Specify one of the following settings:  `NEXT MESSAGE`: Retrieve the next message that is available and matches the search criteria. If the previous message belongs to a message group, then retrieve the next available message that matches the search criteria and belongs to the message group. This setting is the default.  `NEXT TRANSACTION`: Skip the remainder of the current message group (if any) and retrieve the first message of the next message group. This setting can only be used if message grouping is enabled for the current queue.  `FIRST MESSAGE`: Retrieves the first message which is available and matches the search criteria. This setting resets the position to the beginning of the queue.  Note: Each message group contains the messages in a single transaction.  See Also: [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/toc.htm) for more information about dequeue options |
| `wait` | Either `FOREVER` or `NO_WAIT`  If `FOREVER`, then the dequeue call is blocked without a time out until a message is available in the queue.  If `NO_WAIT`, then a wait time of zero seconds is used. In this case, the dequeue will return immediately even if there are no messages in the queue. |
| `msgid` | The message identifier of the message that is dequeued |

Exceptions

Table 149-3 DEQUEUE Procedure Exceptions

| Exception | Description |
| --- | --- |
| `ENDOFCURTRANS` | Dequeue has reached the end of the messages in the current transaction. Specify this exception in the following way:  ``` SYS.DBMS_STREAMS_MESSAGING.ENDOFCURTRANS ```  Every dequeue procedure should include an exception handler that handles this exception. |
| `NOMOREMSGS` | There are no more messages in the queue for the dequeue operation. Specify this exception in the following way:  ``` SYS.DBMS_STREAMS_MESSAGING.NOMOREMSGS ```  A dequeue procedure that specifies `NO_WAIT` for the `wait` parameter should include an exception handler that handles this exception. |

---

### ENQUEUE Procedure

This procedure enables the current user to enqueue a message into the specified queue.

This procedure is overloaded. One version of this procedure contains the `msgid` `OUT` parameter, and the other does not.

Syntax

```
DBMS_STREAMS_MESSAGING.ENQUEUE(
   queue_name  IN   VARCHAR2,  
   payload     IN   ANYDATA,  
   msgid       OUT  RAW);

DBMS_STREAMS_MESSAGING.ENQUEUE(
   queue_name  IN   VARCHAR2,  
   payload     IN   ANYDATA);
```

Parameters

Table 149-4 ENQUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | The name of the local queue into which messages will be enqueued, specified as `[``schema_name``.]` `queue_name`. The current database must contain the queue, and the queue must be a secure queue of `ANYDATA` type.  For example, to specify a queue named `streams_queue` in the `strmadmin` schema, enter `strmadmin.streams_queue` for this parameter. If the schema is not specified, then the current user is the default. |
| `payload` | The payload that is enqueued |
| `msgid` | The message identifier of the message that is enqueued |

Usage Notes

To successfully enqueue messages into a queue, the current user must be mapped to a unique Advanced Queuing agent with the same name as the current user. You can run the `DBMS_STREAMS_ADM.SET_UP_QUEUE` procedure and specify a user as the queue user to grant the necessary privileges to the user to perform enqueues. The Advanced Queuing agent is created automatically when you run `SET_UP_QUEUE` and specify a queue user.

See Also:

[SET\_UP\_QUEUE Procedure](d_streams_adm.md)