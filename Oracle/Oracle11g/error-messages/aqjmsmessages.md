---
title: JMS-00101 to JMS-00243
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/aqjmsmessages.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 125 JMS-00101 to JMS-00243

JMS-00101: Invalid delivery mode {0}

Cause: The delivery mode is not supported

Action: The valid delivery mode is AQjmsConstants.PERSISTENT or AQjmsConstants.NON\_PERSISTENT

JMS-00102: Feature not supported {0}

Cause: This feature is not supported in the current release

Action: None

JMS-00105: Agent must be specified

Cause: AQjmsAgent object was null

Action: Specify a valid AQjmsAgent representing the remote subscriber must

JMS-00106: Cannot have more than one open Session on a JMSConnection

Cause: There is already one open jms session on the connection Cannot have more than one open session on a connection

Action: Close the open session and then open a new one

JMS-00107: Operation not allowed on {0}

Cause: The specified operation is not allowed on this object

Action: None

JMS-00108: Messages of type {0} not allowed with Destinations containing payload of type {1}

Cause: There was a mismatch between the message type being used and the payload type specified for the destination

Action: Use the message type that maps to the payload specified for the queue table that contains this destination

JMS-00109: Class not found: {0}

Cause: The specified class was not found

Action: Make sure your CLASSPATH contains the class

JMS-00110: Property {0} not writeable

Action: None

JMS-00111: Connection must be specified

Cause: The connection object was null

Action: Specify a non-null jdbc connection

JMS-00112: Connection is invalid

Cause: The jdbc connection is invalid

Action: Specify a non-null oracle jdbc connection

JMS-00113: Connection is in stopped state

Cause: An attempt was made to receive messages on a connection that is in stopped state

Action: Start the connection

JMS-00114: Connection is closed

Cause: An attempt was made to use a Connection that has been closed

Action: Create a new connection

JMS-00115: Consumer is closed

Cause: An attempt was mode to use a Consumer that has been closed

Action: Create a new Message Consumer

JMS-00116: Subscriber name must be specified

Cause: Subscriber name was null

Action: Specify a non-null subscription name

JMS-00117: Conversion failed - invalid property type

Cause: An error occured while converting the property to the requested type

Action: Use the method corresponding to the property data type to retrieve it

JMS-00119: Invalid Property value

Cause: The property value specified is invalid

Action: Use the appropriate type of value for the property being set

JMS-00120: Dequeue failed

Cause: An error occurred while receiving the message

Action: See message inside the JMSException and linked SQLException for more information

JMS-00121: DestinationProperty must be specified

Cause: A null AQjmsDestinationProperty was specified while creating a queue/topic

Action: Specify a non-null AQjmsDestinationProperty for the destination

JMS-00123: Interval must be atleast {0} seconds

Cause: An invalid interval was specified

Action: The interval must be greater than 30 seconds

JMS-00124: Invalid Dequeue mode

Cause: Invalid dequeue mode was specified

Action: Valid Dequeue modes are AQConstants.DEQUEUE\_BROWSE, AQConstants.DEQUEUE\_REMOVE, AQConstants.DEQUEUE\_LOCKED, AQConstants.DEQUEUE\_REMOVE\_NODATA

JMS-00125: Invalid Queue specified

Cause: An invalid Queue object was specified

Action: Specify a valid Queue handle

JMS-00126: Invalid Topic specified

Cause: An invalid Topic object was specified

Action: Specify a valid Topic handle

JMS-00127: Invalid Destination

Cause: An invalid destination object was specified

Action: Specify a valid destination (Queue/Topic) object

JMS-00128: Invalid Navigation mode

JMS-00129: Invalid Payload type

Cause: There was a mismatch between the message type being used and the payload type specified for the destination

Action: Use the message type that maps to the payload specified for the queue table that contains this destination. For ADT messages, use the aprropriate CustomDatum/ORAData factory to create the message consumer

JMS-00130: JMS queue cannot be multi-conumer enabled

Cause: An attempt was made to get a AQ multi-consumer queue as a JMS queue

Action: JMS queues cannot be multiconsumer enabled

JMS-00131: Session is closed

Cause: An attempt was made to use a session that has been closed

Action: Open a new session

JMS-00132: Maximum number of properties {0} exceeded

Cause: Maximum number of user defined properties for the message has been exceeded

Action: None

JMS-00133: Message must be specified

Cause: Message specified was null

Action: Specify a non-null message

JMS-00134: Name must be specified

Cause: Queue or Queue table Name specified was null

Action: Specify a non-null name

JMS-00135: Driver {0} not supported

Cause: The specified driver is not supported

Action: Valid drivers are oci8 and thin. To use the kprb driver get the kprb connection using getDefaultConnection() and use the static createTopicConnection and createQueueConnection methods

JMS-00136: Payload factory can only be specified for destinations with ADT payloads

Cause: A CustomDatumFactory/ORADataFactory was specifed for consumers on destinations not containing ADT payloads

Action: This field must be set to null for destinations containing payloads of type SYS.AQ$\_JMS\_TEXT\_MESSAGE, SYS.AQ$\_JMS\_BYTES\_MESSAGE, SYS.AQ$\_JMS\_MAP\_MESSAGE, SYS.AQ$\_JMS\_OBJECT\_MESSAGE, SYS.AQ$\_JMS\_STREAM\_MESSAGE

JMS-00137: Payload factory must be specified for destinations with ADT payloads

Cause: CustomDatumFactory/ORADataFactory was not specified for destinations containing ADT payloads

Action: For destinations containing ADT messages, a CustomDatumFactory/ORADataFactory for a java class that maps to the SQL ADT type of the destination must be specified

JMS-00138: Producer is closed

Cause: An attempt was made to use a producer that has been closed

Action: Create a new Message Producer

JMS-00139: Property name must be specified

Cause: Property name was null

Action: Specify a non-null property name

JMS-00140: Invalid System property

Cause: Invalid system property name specified.

Action: Specify one of the valid JMS system properties

JMS-00142: JMS topic must be created in multi-consumer enabled queue tables

Cause: An attempt was made to create a JMS topic in a single-consumer queue table

Action: JMS topics can only be created in queue tables that are multiconsumer enabled

JMS-00143: Queue must be specified

Cause: Null queue was specified

Action: Specify a non-null queue

JMS-00144: JMS queue cannot be created in multi-consumer enabled queue tables

Cause: An attempt was made to create a JMS queue in a multi-consumer queue table

Action: JMS queues can only be created in queue tables that are not multiconsumer enabled

JMS-00145: Invalid recipient list

Cause: The recipient list specified was empty

Action: Specify a recipient list with atleast one recipient

JMS-00146: Registration failed

Cause: An error occured while registering the type in the type map

Action: None

JMS-00147: Invalid ReplyTo destination type,

Cause: The ReplyTo destination object is invalid

Action: The ReplyTo destination must be of type AQjmsAgent, or AQjmsDestination. If AQjmsAgent is used, its "name" must not be "JMSReplyTo" (which is considered a reserved name to be used for AQjmsDestination objects). If AQjmsDestination is used, it must be serializable into a string (and vice-versa).

JMS-00148: Property name size exceeded

Cause: The property name is greater than the maximum size

Action: Specify a property name that is less than 100 characters

JMS-00149: Subscriber must be specified

Cause: Subscriber specified was null

Action: Specify a non-null subscriber

JMS-00150: Property not supported

Cause: An attempt was made to use a property that is not supported

Action: None

JMS-00151: Topics cannot be of type EXCEPTION

Cause: Topics cannot be of type AQjmsConstants.EXCEPTION

Action: Specify topics to be of type AQjmsConstants.NORMAL

JMS-00153: Invalid System property type

Cause: The type of the value specified does not match the type defined for the system property being set

Action: Use the correct type for the setting the system property

JMS-00154: Invalid value for sequence deviation

Cause: The sequence deviation is invalid

Action: Valid values are AQEnqueueOption.DEVIATION\_BEFORE, AQEnqueueOption.DEVIATION\_TOP

JMS-00155: AQ Exception {0}

Cause: An error occured in the AQ java layer

Action: See the message inside the JMSException and the linked exception for more information

JMS-00156: Invalid Class {0}

Cause: Class specified is invalid

Action: make sure your CLASSPATH has the specified class

JMS-00157: IO Exception {0}

Cause: IO exception

Action: See message is JMSException for details

JMS-00158: SQL Exception {0}

Cause: SQL Exception

Action: See message inside linked SQLException for details

JMS-00159: Invalid selector {0}

Cause: The selector specified is either invalid or too long

Action: Check the syntax of the selector

JMS-00160: EOF Exception {0}

Cause: EOF exception occurred while reading the byte stream

Action: None

JMS-00161: MessageFormat Exception: {0}

Cause: An error occured while converting the stream data to specified type

Action: check the type of data expected on the stream and use the appropriate read method

JMS-00162: Message not Readable

Cause: Message is in write-only mode

Action: Call the reset method to make the message readable

JMS-00163: Message not Writeable

Cause: Message is in read-only mode

Action: Use the clearBody method to make the message writeable

JMS-00164: No such element

Cause: Element with specified name was not found in the map message

Action: None

JMS-00165: Maximum size of property value exceeded

Cause: The property value exceeded the maximum length allowed

Action: Values for JMS defined properties can be a maximum of length of 100, Values for User defined properties can have a maximum length of 2000

JMS-00166: Topic must be specified

Cause: Topic speecified was null

Action: Specify a non-null topic

JMS-00167: Payload factory or Sql\_data\_class must be specified

Cause: Payload factory or Sql\_data\_class not specified for queues containing object payloads

Action: Specify a CustomDatumFactory/ORADataFactory or the SQLData class of the java object that maps to the ADT type defined for the queue.

JMS-00168: Cannot specify both payload factory and sql\_data\_class

Cause: Both CustomDatumFactory/ORADataFactory and SQLData class were specified during dequeue

Action: Specify either the CustomDatumFactory/ORADataFactory or the SQLData class of the java object that maps to the ADT type defined for the queue.

JMS-00169: Sql\_data\_class cannot be null

Cause: SQLData class specified is null

Action: Specify the SQLData class that maps to the ADT type defined for the queue

JMS-00171: Message is not defined to contain {0}

Cause: Invalid payload type in message

Action: Check if the queue is defined to contain RAW or OBJECT payloads and use the approprate payload type in the message

JMS-00172: More than one queue table matches query {0}

Cause: More than one queue table matches the query

Action: Specify both owner and queue table name

JMS-00173: Queue Table {0} not found

Cause: The specified queue table was not found

Action: Specify a valid queue table

JMS-00174: Class must be specified for queues with object payloads Use dequeue(deq\_option, payload\_fact) or dequeue(deq\_option, sql\_data\_cl)

Cause: This dequeue method cannot be used to dequeue from queues with OBJECT payloads

Action: use the either dequeue(deq\_option, payload\_fact) or dequeue(deq\_option, sql\_data\_cl)

JMS-00175: DequeueOption must be specified

Cause: DequeueOption specified is null

Action: Specify a non-null dequeue option

JMS-00176: EnqueueOption must be specified

Cause: EnqueueOption specified is null

Action: Specify a non-null enqueue option

JMS-00177: Invalid payload type: Use dequeue(deq\_option) for raw payload queues

Cause: This method cannot be used to dequeue from queues with RAW payload

Action: use the dequeue(deq\_option) method

JMS-00178: Invalid Queue name - {0}

Cause: The queue name specified is null or invalid

Action: Specify a queue name that is not null. The queue name must not be qualified with the schema name. The schema name must be specified as the value of the owner parameter

JMS-00179: Invalid Queue Table name - {0}

Cause: The queue table name specified is null or invalid

Action: Specify a queue table name that is not null. The queue table name must not be qualified with the schema name. The schema name must be specified as the value of the owner parameter

JMS-00180: Invalid Queue Type

Cause: Queue type is invalid

Action: Valid types are AQConstants.NORMAL or AQConstants.EXCEPTION

JMS-00181: Invalid value for wait\_time

Cause: Invalid value for wait type

Action: Wait time can be AQDequeueOption.WAIT\_FOREVER, AQDequeueOption.WAIT\_NONE or any value greater than 0

JMS-00182: More than one queue matches query

Cause: More than one queue matches query

Action: Specify both the owner and name of the queue

JMS-00183: No AQ driver registered

Cause: No AQDriver registered

Action: Make sure that the AQ java driver is registered. Use Class.forName("oracle.AQ.AQOracleDriver")

JMS-00184: Queue object is invalid

Cause: The queue object is invalid

Action: The underlying JDBC connection may have been closed. Get the queue handle again

JMS-00185: QueueProperty must be specified

Cause: AQQueueProperty specified is null

Action: Specify a non-null AQQueueProperty

JMS-00186: QueueTableProperty must be specified

Cause: QueueTableProperty specified is null

Action: Specify a non-null AQQueueTableProperty

JMS-00187: Queue Table must be specified

Cause: Queue Table specified is null

Action: Specify a non-null queue table

JMS-00188: QueueTable object is invalid

Cause: The queue table object is invalid

Action: The underlying JDBC connection may have been closed. Get the queue table handle again

JMS-00189: Byte array too small

Cause: The byte array given is too small to hold the data requested

Action: Specify a byte array that is large enough to hold the data requested or reduce the length requested

JMS-00190: Queue {0} not found

Cause: The specified queue was not found

Action: Specify a valid queue

JMS-00191: sql\_data\_cl must be a class that implements SQLData interface

Cause: The class specified does not support the java.sql.SQLData interface

Action: None

JMS-00192: Invalid Visibility value

Cause: Visibility value specified is invalid

Action: Valid values areAQConstants.VISIBILITY\_ONCOMMIT, AQConstants.VISIBILITY\_IMMEDIATE

JMS-00193: JMS queues cannot contain payload of type RAW

Cause: An attempt was made to create a JMS queue with RAW payload

Action: JMS queues/topics cannot contain RAW payload

JMS-00194: Session object is invalid

Cause: Session object is invalid

Action: The underlying JDBC connection may have been closed. Create a new session

JMS-00195: Invalid object type: object must implement CustomDatum/ORAData or SQLData interface

Cause: Invalid object type specified

Action: object must implement CustomDatum/ORAData or SQLData interface

JMS-00196: Cannot have more than one open QueueBrowser for the same destination on a JMS Session

Cause: There is already an open QueueBrowser for this queue on this session

Action: There cannot be more than one queue browser for the same queue in a particular session. Close the existing QueueBrowser and then open a new one

JMS-00197: Agent address must be specified for remote subscriber

Cause: Address field is null for remote subscriber

Action: The address field must contain the fully qualified name of the remote topic

JMS-00199: Registration for asynchronous receipt of messages failed

Cause: Registration with the database for asynchronous receipt of messages for the consumer failed

Action: See error message in linked Exception for details

JMS-00200: Destination must be specified

Cause: Destination is null

Action: Specify a non-null destination

JMS-00201: All Recipients in recipient\_list must be specified

Cause: One or more elements in the recipient list are null

Action: All AQjmsAgents in the recipient list must be specified

JMS-00202: Unregister for asynchronous receipt of messages failed

Cause: An error occured while removing the registration of the consumer with the database for asynchronous receipt

Action: None

JMS-00203: Payload Factory must be specified

Cause: Null Payload Factory was specified

Action: None

JMS-00204: An error occurred in the AQ JNI layer

Cause: JNI Error

Action: Check error message in linked exception for details

JMS-00205: Naming Exception

Cause: Naming exception

Action: None

JMS-00206: XA Exception XAError-{0}:: OracleError-{1}

Cause: An error occured in the XA layer

Action: See the message inside the linked XAException for more information

JMS-00207: JMS Exception {0}

Cause: An error occured in the JMS layer

Action: See the message inside the linked JMSException for more information

JMS-00208: XML SQL Exception

Cause: An error occured in the XML SQL layer

Action: See the message inside the linked AQxmlException for more information

JMS-00209: XML SAX Exception

Cause: An error occured in the XML SAX layer

Action: See the message inside the linked AQxmlException for more information

JMS-00210: XML Parse Exception

Cause: An error occured in the XML Parser layer

Action: See the message inside the linked AQxmlException for more information

JMS-00220: Connection no longer available

Cause: Connection to the database no longer available.

Action: None

JMS-00221: Free physical database connection unavailable in connection pool

Cause: A free physical database connection was not available in the OCI connection pool in order to perform the specified operation.

Action: Try performing the operation later

JMS-00222: Invalid Payload factory type

Cause: Payload factory should be of CustomDatumFactory or ORADataFactory type.

Action: Use one of CustomDatumFactory/ORADataFactory types.

JMS-00223: Payload factory must be null for destinations with Sys.AnyData payload - use typemap instead

Cause: A CustomDatumFactory/ORADataFactory was specifed for consumers on destinations containing SYS.ANYDATA payloads

Action: This field must be set to null for destinations containing payloads of type SYS.AnyData. The ORADataFactory(s) must be registered in the session's typemap

JMS-00224: Typemap is invalid - must be populated with SQLType/OraDataFactory mappings to receive messages from Sys.AnyData destinations

Cause: The typemap of the session is null or empty. For destinations of tpye Sys.AnyData, the typemap must contain OraDataFactory objects for all possible types that may be stored in the queue/topic

Action: Use the AQjmsSession.getTypeMap() method get the typemap. Then use the put() method to register SQLType names and their corresponding OraDataFactory objects

JMS-00225: Invalid JDBC driver - OCI driver must be used for this operation

Cause: Operations on Sys.AnyData queues/topics are not supported using this JDBC driver

Action: Use the JDBC OCI driver to receive messages from Sys.AnyData queues/topics

JMS-00226: Header-only Message does not have a body

Cause: Header-only message does not have a body; the body cannot be cleared, changed, or queried.

Action: Do not access or modify the body of a read-only message.

JMS-00227: Illegal attempt to commit on a non transacted JMS Session

Cause: Illegal attempt to invoke the commit method on a non transacted JMS Session

Action: Remove invocation of the commit method on the current JMS Session

JMS-00228: Illegal attempt to rollback on a non transacted JMS Session

Cause: Illegal attempt to invoke the rollback method on a non transacted JMS Session

Action: Remove invocation of the rollback method on the current JMS Session

JMS-00229: {0} must be specified

Cause: The specified parameter was null

Action: Specify a non-null value for the parameter

JMS-00230: Illegal operation on durable subscription with active TopicSubscriber

Cause: Try to unsubscribe, change or create durable subscription while it has an active TopicSubscriber.

Action: Close the active TopicSubscriber and try again.

JMS-00231: Consumers on temporary destination must belong to the same

Cause: The specified parameter was null

Action: Specify a non-null value for the parameter

JMS-00232: An invalid user/password was specified for the JMS connection

Cause: Invalid user/password specified for connection

Action: Specify valid user/password for connection

JMS-00233: The required subscriber information is not available

Cause: Try to retrieve subscriber information from a subscriber which was obtained with getDurableSubscriber method and had no corresponding information in the in-memory map.

Action: Do not retrieve subscriber information from such a subscriber

JMS-00234: This operation is not allowed in the current messaging domain

Cause: Perform an operation that is not allowed in the current messaging domain

Action: Do not perform the operation in the current messaging domain

JMS-00235: Can not link the durable subscriber name with a topic in unsubscribe method.

Cause: OJMS is unable to link the supplied durable subscriber name with a topic. This causes unsubscribe method to fail.

Action: Use other unsubscribe methods which the user can provide topic name.

JMS-00236: OJMS encountered invalid OCI handles.

Cause: OJMS encountered invalid OCI handles when using JDBC OCI driver.

Action: Make sure the underlying JDBC connection is not closed while OJMS is still operating.

JMS-00237: Can not start thread for message listener.

Cause: OJMS is unable to start a new thread for message listener.

Action: Check the thread proxy code if the thread was started by a user provided thread proxy.

JMS-00238: Illegal attempt to recover on a transacted JMS Session

Cause: Illegal attempt to invoke the recover method on a transacted JMS Session

Action: Use rollback method instead of recover method on transacted JMS session.

JMS-00239: Illegal attempt to call {0} method on a XASession.

Cause: Illegal attempt to invoke the commit or rollback method on a XASession

Action: Use JTA to commit or rollback a distributed transaction

JMS-00240: Illegal attempt to call setClientID after other actions.

Cause: Illegal attempt to call Connection.setClientID method after other actions has been taken on this Connection

Action: set client ID before any other action on the Connection

JMS-00241: Illegal attempt to delete temporary destination when there are consumers using it.

Cause: Illegal attempt to delete temporary destination while there are existing consumers still using it.

Action: close the consumers before deleting the temporary destination

JMS-00242: Illegal attempt to enqueue message with both immediate visibility and three phase enqueue process.

Cause: Illegal attempt to enqueue message with both immediate visibility and three phase enqueue process.

Action: turn on the system property oracle.jms.useTemplobsForEnqueue