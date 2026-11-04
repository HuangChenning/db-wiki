---
title: DRG-10000 to DRG-52305
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/drgus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 115 DRG-10000 to DRG-52305

DRG-10001: can not access result table string

Cause: specified table does not exist or server does not have write privileges

Action: check result table

DRG-10002: can not insert into result table

Cause: text server is not privileged to insert, tablespace exhausted

Action: check privileges and tablespace

DRG-10011: invalid object name string

Cause: a table, column or procedure name specified had an invalid format. It is either too long or contains illegal characters. Probably you are passing in incorrect parameters.

Action: check parameter values

DRG-10015: id exceeds limit(2147483642) of a number

Cause: the limit of an id is 2147483642

Action: use an id with value 214748364 or under

DRG-10016: you must be the owner to modify this object

Cause: you tried to modify an object which you do not own

Action: have the owner modify the object

DRG-10017: you must be string to do this: string

Cause: you tried to modify an object which you have no privilege

Action: have the owner modify the object

DRG-10100: invalid argument found: string

Cause: invalid command argument was specified

Action: check the documentation for the legal arguments and re-execute the command

DRG-10101: no value for argument: string

Cause: this argument requires value(s)

Action: re-execute the command with the correct argument value(s)

DRG-10102: mandatory argument missing: string

Cause: this argument is mandatory

Action: re-execute the command and specify the argument

DRG-10103: illegal value for argument: string

Cause: an illegal value was passed to this argument

Action: check the documentation for the legal values for this argument

DRG-10200: invalid server personality mask: string

Cause: the specification for the server personality mask is invalid

Action: check the documentation and specify the correct mask

DRG-10202: server failed to register

Action: look at the next error on the stack

DRG-10203: server named string does not exist

Cause: update was called with the name of a server that does not exist

Action: correct the name of the server

DRG-10204: server update failed

Cause: the attempt to update the server failed

Action: look at the next error on the stack

DRG-10205: server deregister failed

Cause: the attempt to deregister the server from the data dictionary failed

Action: look at the next error on the stack

DRG-10206: failed to perform recovery for a server or client

Cause: Contact oracle support

Action: Contact oracle support

DRG-10301: timed out waiting for responses from servers

Cause: Not enough servers are running to handle the current system load, and a large backlog of commands has accumulated; perhaps no servers are running. This message could also indicate an internal error where one of the servers has crashed trying to process a given request

Action: Check that enough servers are running, and that they are processing commands of the correct type. For instance, a DDL command might timeout if all the servers are setup to exclusively process query commands. Also, check the server log files.

DRG-10302: interrupted waiting for responses from servers

Cause: User interrupted the request before it was completed

Action: Restart the request

DRG-10303: could not queue given commands to be processed

Cause: The given command or commands could not (all) be queued. This could indicate an extremely high system load, but it is more likely an internal error.

Action: Check if any servers are running to process the command.

DRG-10304: unexpected error sending command(s) to Oracle Text server

Cause: There was an unexpected error sending command(s) to server

Action: Call customer support.

DRG-10305: pipe string is full

Cause: Could not send command to pipe, because the pipe was full

Action: Check if any servers are running to process the commands on that pipe

DRG-10306: server terminated unexpectedly while processing command

Cause: The server shutdown during execution of your command. This could be caused by a shutdown abort, or by an internal error in the server.

Action: If the server terminated had an internal error, contact customer support.

DRG-10307: no servers running

Cause: Could not process command because no servers are running with the correct personality mask.

Action: Start some servers with correct personality mask.

DRG-10308: no server with the required string personality mask is running

Cause: Could not process command because no servers are running with the correct personality mask.

Action: Start some servers with correct personality mask.

DRG-10309: not enough job queue processes

Cause: Could not process command because no servers with the correct personality mask are running.

Action: increase the JOB\_QUEUE\_PROCESSES initialization parameter or reduce the parallel degree for this statement.

DRG-10310: servers were shutdown before processing request

Cause: The command could not be completed because the servers were shut down or terminated before processing the request.

Action: Start another server with the correct personality mask.

DRG-10311: remote send not supported

Cause: You tried to specify a database link in an index specification

Action: Specify only local index names

DRG-10312: logfile name must be specified

Cause: You tried to start logging without specifying a logfile name

Action: Specify a logfile name

DRG-10313: logging has already been started

Cause: You tried to start logging even though logging has already been started

Action: Stop logging first, or ignore

DRG-10314: logging has not been started

Cause: You tried to stop logging even though logging has not been started

Action: Start logging first, or ignore

DRG-10315: logging is not supported on MTS

Cause: You tried to start logging on MTS

Action: None

DRG-10500: CREATE\_INDEX failed: column spec string

Cause: failed to create text index on the specified column

Action: See the next errors on stack and take appropriate action

DRG-10501: invalid stopword: string

Cause: The stopword specified cound be lexed into multiple tokens with current lexer preference

Action: Check lexer preference and Respecifies the stopword

DRG-10502: index string does not exist

Cause: the specified index does not exist or you do not have access to it.

Action: Specify an existing index

DRG-10503: table string cannot be indexed because it has no primary key

Cause: a textkey needs to be a single column unique key whose length does not exceed 64 bytes. no such key was defined as an unique index or declared as a primary or unique key constraint

Action: create a suitable textkey for the table or specify it explicitly in this procedure call

DRG-10504: primary key is required when using the DETAIL\_DATASTORE

Cause: you tried to use the detail datastore to index a table with no primary key constraint

Action: add a primary key constraint on the table

DRG-10506: table does not exist: string

Cause: The table, view, or synonym specified does not exist. There may also be a permissions problem reading the table.

Action: Reinvoke the operation with the correct table name

DRG-10507: duplicate index name: string

Cause: the specified index already exists in the dictionary

Action: this index can be updated or deleted, however this is only allowed if there is no text index available on the text column

DRG-10509: invalid text column: string

Cause: the column specified is not valid

Action: check that the followings are valid: a) text column is of supported datatype b) valid table name, column name in the specification.

DRG-10510: stopword is missing

Cause: The stopword to be added was not specified.

Action: Specify the stopword

DRG-10511: index string does not exist or is incomplete

Cause: index creation is not complete

Action: create index before performing this operation

DRG-10513: index string metadata is corrupt

Cause: dictionary contains bad preferences for this index

Action: contact you DBA

DRG-10516: failed to perform DDL operation due to an Oracle error

Cause: the ddl operation requested has failed because of an Oracle error

Action: see the Oracle error on the stack and take the appropriate action

DRG-10517: index string is already valid

Cause: The index was in a valid state and did not need the requested operation.

Action: Check the requested operation

DRG-10518: an operation is in progress which conflicts with string request

Cause: another session is operating on this index. it could be: a) DML is requested and DDL is in progress or b) DDL is requested and DML is in progress operation on the index

Action: try again later

DRG-10520: failed to drop index: string

Cause: Failed to drop index on the specified index

Action: see the Oracle error on the stack and take the appropriate action

DRG-10525: missing REBUILD keyword

Cause: all Oracle Text alter index options require the REBUILD keyword

Action: specify alter index with the REBUILD keyword

DRG-10528: primary keys of type string are not allowed

Cause: you tried to create an index on a table with an illegal primary key datatype

Action: change the textkey to one of the followings: VARCHAR2, NUMBER, VARCHAR, DATE, CHAR, MLSLABEL

DRG-10531: parallel parameter must be > 0

Cause: you called create index with parallel = 0

Action: specify with value > 0

DRG-10532: table is not partitioned

Cause: you called parallel create index on non-partitioned table

Action: recreate the table with partitions or remove the PARALLEL clause

DRG-10533: invalid user name: string

Cause: you specified a user name that is invalid

Action: specify the correct user name

DRG-10535: failed to optimize text index string

Cause: the optimize operation requested has failed because of an Oracle error

Action: see the Oracle error on the stack and take the appropriate action

DRG-10549: length of the object name string exceeded the limit

Cause: object name has exceeded the maximun length of 30 bytes

Action: Reduce the length of the object name if you want to re-create it

DRG-10550: illegal syntax for index, preference, source or section name

Cause: name may have additional periods(.)

Action: check the syntax of the name

DRG-10553: illegal syntax for column specification string

Cause: column specification may have additional periods(.)

Action: check the syntax of column specification if you want to re-create it

DRG-10561: index string is not valid for requested operation

Cause: The index was not in a valid state due to some prior error.

Action: Drop index and create index again.

DRG-10562: missing alter index parameter

Cause: The parameter string was missing

Action: Provide correct parameter string with regard to the requested alter index operation.

DRG-10569: table or column does not exist: string

Cause: The table, view, synonym or column specified does not exist. There may also be a permissions problem reading the table.

Action: Reinvoke the operation with the correct table name or column name

DRG-10573: index string is obsolete

Cause: you specified an obsolete index

Action: perform upgrade\_index on the index

DRG-10574: failed to upgrade text index string

Cause: the upgrade operation has failed because of an Oracle error

Action: see the Oracle error on the stack and take the appropriate action

DRG-10579: must provide text query criteria

Cause: text query criteria is mandatory

Action: provide text query criteria

DRG-10580: parallel indexing is not supported: string

Cause: attempted to create index with parallel servers

Action: Drop index and set parallel to 1 in create index

DRG-10581: indirect datastores cannot be used with long or lob text columns

Cause: You tried to create an index on a long or lob column using an indirect datastore such as the file or url datastores

Action: Use direct datastore or a varchar column

DRG-10582: column string does not exist in table string

Cause: you specified an invalid column

Action: specify valid column

DRG-10583: TRUNCATE INDEX failed: string

Cause: Failed to truncate index

Action: See the next errors on stack and take appropriate action

DRG-10584: failed to string string string due to an Oracle error

Cause: a DDL operation on an index object failed due to SQL error

Action: see following error

DRG-10595: ALTER INDEX string failed

Cause: failed to alter index

Action: See the next errors on stack and take appropriate action

DRG-10597: invalid rebuild online operation

Cause: REBUILD ONLINE is not supported for requested operation.

Action: Alter index without the online option.

DRG-10598: invalid parallel operation

Cause: PARALLEL is not supported for requested operation.

Action: Alter index without the parallel option

DRG-10599: column is not indexed

Cause: The column specified is not indexed.

Action: Create index on the column before performing this operation

DRG-10601: failed to remove pending DML for this index

Cause: The system could not remove triggers setup to monitor updates to the requested table

Action: See next error on stack to determine course of action. Call Oracle support if necessary. Until this error is fixed, updates to all text columns in the given table may not be indexed.

DRG-10602: failed to queue DML change to column string for primary key string

Cause: The system could not record that a change had been made to the given column

Action: See next error on stack to determine course of action. Call Oracle support if necessary. Until this error is fixed, updates to all text columns in the given table may not be indexed.

DRG-10606: server failed to access the DML Queue

Cause: The server was had an error accessing the DML Queue

Action: See next error on stack.

DRG-10607: index meta data is not ready yet for queuing DML

Cause: the meta data for the index has not been created yet

Action: retry the DML operation

DRG-10700: preference does not exist: string

Cause: the preference name specified does not exists

Action: retry with the correct preference name

DRG-10701: preference string.string already exists

Cause: the specified preference already exists

Action: must drop the preference if you want to re-create it.

DRG-10702: cannot create or modify preference in another user's schema

Cause: you tried to create a preference for another user

Action: owner or CTXSYS or a user who has CTXADMIN role should create preference

DRG-10703: invalid framework object string

Cause: you specified an invalid object type

Action: use a valid framework object

DRG-10704: preference string does not have an attribute named string

Cause: you tried to set value for a invalid attribute (not supported by the object.

Action: specify the correct attribute name

DRG-10705: invalid value string for attribute string

Cause: you tried to set an illegal value for an attribute

Action: specify the correct attribute value for the datatype of the attribute

DRG-10706: length of string exceeds maximum size of string

Cause: Parameter is too many bytes

Action: Correct preference setting and resubmit

DRG-10707: a value is required for attribute string of preference string

Cause: A required attribute was not provided

Action: Correct preference setting and resubmit

DRG-10708: invalid class id string for preference string

Cause: the specified class id is not correct for the specified preference

Action: specify the correct class id

DRG-10709: this preference is referenced by string and cannot be dropped

Cause: the specified preference is used as part of another preference and cannot be dropped until the referring preference is modified

Action: modify the referring preference

DRG-10710: Invalid value string for string attribute

Cause: Invalid value provided for save\_copy attribute It should be one of these: (PLAINTEXT, FILTERED, NONE)

Action: Provide correct SAVE\_COPY attribute value

DRG-10750: unknown parameter string

Cause: Unrecognized parameter

Action: Specify correct parameter

DRG-10751: invalid value for parameter

Cause: Wrong data type or out of range

Action: Specify correct parameter value

DRG-10752: DEFAULT\_INDEX\_MEMORY cannot be greater than MAX\_INDEX\_MEMORY

Cause: You tried to set DEFAULT\_INDEX\_MEMORY to a value higher than the maximum set in MAX\_INDEX\_MEMORY

Action: Specify a lower value

DRG-10753: invalid memory size string string

Cause: You specified an incorrectly formatted memory string

Action: Specify a correctly formatted memory string

DRG-10754: memory size must be between string and string

Cause: You specified a memory size which is outside the allowed range

Action: Specify a memory size within the allowed range

DRG-10755: string and string have characters in common

Cause: the join character sets cannot have characters in common

Action: Correct the attribute values and resubmit

DRG-10756: neither text indexing nor theme indexing has been selected

Cause: INDEX\_TEXT and INDEX\_THEMES preferences both cannot be FALSE.

Action: Set either of INDEX\_TEXT or INDEX\_THEMES or both to TRUE.

DRG-10757: stoplist cannot have more than 4096 stopwords

Cause: a stoplist cannot have more than 4096 stopwords. This includes stopthemes.

Action: none required

DRG-10758: index owner does not have the privilege to use file or URL datastore

Cause: index owner does not have the role defined in FILE\_ACCESS\_ROLE

Action: grant index owner the appropriate role

DRG-10759: invalid role

Cause: the role does not exist in the database

Action: check the role name or create the role

DRG-10760: illegal format for procedure name

Cause: the procedure name specified is invalid. For instance, it may have a semicolon

Action: check the procedure name

DRG-10761: procedure string does not exist

Cause: the specified procedure could not be found

Action: check input. Try a fully-specified format such as OWNER.OBJECT

DRG-10762: index owner does not have access to procedure string

Cause: the index owner does not have execute privilege on the specified procedure

Action: grant index owner execute permission on the procedure

DRG-10763: value string is not a valid character set

Cause: the value specified for the filename\_charset attribute of the file datastore is not a valid character set name

Action: specify a valid Oracle character set name

DRG-10764: only SYS can modify FILE\_ACCESS\_ROLE

Cause: For security reasons, only SYS can modify the FILE\_ACCESS\_ROLE system parameter

Action: Connect as SYS before modifying the parameter

DRG-10800: query failed: string string string

Cause: Failed to process the query

Action: Check the errors on stack and take appropriate action

DRG-10801: cannot create an SQE for another user

Cause: You tried to create an SQE for another user

Action: Remove owner from SQE name specification

DRG-10816: display/highlight call failed

Cause: See the next error on the stack.

Action: See the next error on the stack.

DRG-10817: CONTAINS term consists of stopword or phrase of stopwords: string

Action: Replace the stopword or use stopwords within phrases containing non-stopwords.

DRG-10819: could not open contains cursor

Cause: An error occurred while trying to open a contains cursor

Action: See accompanying error messages in the stack

DRG-10820: invalid contains cursor id

Cause: You tried to fetch or close a contains cursor with an id which does not exist.

Action: Review fetch or close invocation

DRG-10821: contains cursor is not open

Cause: You tried to fetch from a contains cursor which was not open.

Action: Open cursor first

DRG-10822: duplicate query name

Cause: You tried to create a stored query with a name already used.

Action: Use different name

DRG-10823: invalid query name

Cause: The query name specified is not valid

Action: Check the query name

DRG-10825: stored query does not exist: string

Cause: The specified stored query does not exist.

Action: Check the query name

DRG-10826: no document with the specified textkey is found

Cause: There is no document with the specified textkey.

Action: Check the textkey

DRG-10827: open\_con must be performed before count\_last

Cause: last\_count returns hit from in-memory query,so an in-memory query must be run before you can use count\_last

Action: execute open\_con before run count\_last

DRG-10828: token string is longer than maximum length for column string

Cause: A token to be inserted in the feedback table is longer than the maximum allowed column size.

Action: Modify the query, or the column size for feedback table, or feedback procedure arguments accordingly.

DRG-10829: feedback id string is longer than the maximum length of string bytes

Cause: Feedback id is longer than the maximum allowed length for the feedback\_id column.

Action: Use a smaller feedback\_id.

DRG-10830: SHARELEVEL is not 0 or 1

Cause: You specified a sharelevel which is not 0 or 1

Action: Use sharelevel equal to 0 or 1 only.

DRG-10831: can not insert into feedback table string

Cause: Not privileged to insert.

Action: Check privileges.

DRG-10832: can not delete from feedback table string

Cause: Not privileged to delete.

Action: Check privileges.

DRG-10833: feedback failed

Cause: Failed to process feedback request

Action: Check the errors on stack and take appropriate action

DRG-10834: upper-case form of section name string too long

Cause: upper-case form of the section name is longer then supported length

Action: reduce length of section name when adding section

DRG-10835: WITHIN operator not supported for theme index

Cause: WITHIN operator used in theme index query

Action: Rewrite query without WITHIN operator

DRG-10836: field section and attribute section can not be nested

Cause: A field section or a attribute section is specified in a nested section search

Action: Rewrite query without nested field sections

DRG-10837: section string does not exist

Cause: The given section name does not exist in USER\_SECTIONS

Action: Rewrite query with valid section name

DRG-10838: invalid SPAN argument supplied to NEAR

Cause: An invalid value was supplied for SPAN argument to NEAR

Action: Provide a valid SPAN. Valid values are integers from 0 to 100.

DRG-10839: invalid ORDER argument supplied to NEAR

Cause: An invalid value was supplied for ORDER argument to NEAR

Action: Provide a valid ORDER. Valid values are T, TRUE, F, FALSE (case insensitive).

DRG-10840: CONTAINS predicate including 0 is not supported by FIRST\_ROWS hint

Cause: User attempts to issue a query with CONTAINS predicate including 0 while giving FIRST\_ROWS hint.

Action: remove FIRST\_ROWS hint.

DRG-10841: invalid SCORE argument supplied to FUZZY

Cause: An invalid value was supplied for SCORE argument to FUZZY

Action: Provide a valid SCORE. Valid values are integers from 0 to 80.

DRG-10842: invalid NUMRESULTS argument supplied to FUZZY

Cause: An invalid value was supplied for NUMRESULTS argument to FUZZY

Action: Provide a valid NUMRESULTS. Valid values are integers from 0 to 5000.

DRG-10843: invalid WEIGHT argument supplied to FUZZY

Cause: An invalid value was supplied for WEIGHT argument to FUZZY

Action: Set WEIGHT to WEIGHT or NOWEIGHT.

DRG-10844: index cannot execute this structured predicate efficiently

Cause: You specified a combination of condition and order by columns in a catsearch query which cannot be executed by the index's index set efficiently

Action: None

DRG-10845: column string is not indexed

Cause: You specified a column in a condition or order by which is not part of the ctxcat index

Action: None

DRG-10846: order by columns must be all ascending or all descending

Cause: You specified an order by clause which has some columns ascending and some descending. This is not currently supported by catsearch

Action: None

DRG-10847: catsearch requires prefix index for this type of query

Cause: For efficient execution of this Vgram query, we require presence of a prefix index.

Action: create a prefix index

DRG-10848: invalid structured clause

Cause: you have specified an invalid structured clause

Action: None

DRG-10849: catsearch does not support functional invocation

Cause: the query plan for your query is invoking a catsearch operator functionally rather than as an index rowsource. The catsearch operator does not support functional invocation

Action: add optimizer hints so that all catsearch operators are performed through index scans

DRG-10850: CTXRULE indextype does not support the operator

Cause: Used an operator not supported by CTXRULE. Currently it only supports AND, NEAR, phrase, NOT, WITHIN, OR, ABOUT, EQUIVALENCE, STEM and THESAURUS operators

Action: Rewrite query without this operator

DRG-10851: Invalid grammar string specified for query template

Cause: incorrect grammar specification

Action: Rewrite query specifying valid grammar name

DRG-10852: Invalid scoring type string specified for query template

Cause: incorrect scoring type specification

Action: Rewrite query specifying valid scoring type (integer/float)

DRG-10853: Catsearch does not support this operator

Cause: unsupported operator specified

Action: Rewrite query using valid operators

DRG-10854: Invalid scoring algorithm string specified for query template

Cause: incorrect scoring algorithm specification

Action: Rewrite query specifying valid scoring algorithm (default/count)

DRG-10855: CTXRULE indextype does not support the token type

Cause: Unsupported VGRAM token type 1.

Action: None

DRG-10856: SDATA section string does not exist

Cause: The given SDATA section name does not exist in USER\_SECTIONS

Action: Rewrite query with valid SDATA section name

DRG-10857: literal is not compatible with the data type of the SDATA section

Cause: The given literal is not compatible with the data type of the specified SDATA section.

Action: Rewrite query with a compatible literal

DRG-10858: SDATA operator is not allowed in WITHIN

Cause: A field section or a attribute section is specified in a nested section search

Action: Rewrite query without nested field sections

DRG-10859: Only one predefined scoring component can be used in DEFINESCORE

Cause: More than one predefined scoring component (i.e. RELEVANCE, OCCURRENCE, etc.) is used in the scoring expression of the DEFINESCORE operator

Action: Rewrite query using only one predefined component

DRG-10860: All expressions under the same WITHIN must use the same predefined scoring component

Cause: The query side of the same within mixes different types of scoring components(i.e. RELEVANCE, OCCURRENCE, etc.)

Action: Rewrite query using only one type of predefined component

DRG-10861: COMPLETION score must be used with WITHIN operator

Cause: The completion score is used without using the WITHIN operator

Action: Rewrite query to include a within operator

DRG-10862: string attribute cannot be used with CTXRULE indexes

Cause: Used an attribute not supported by CTXRULE. This restriction is due to lack of wildcard support for CTXRULE indexes.

Action: Rewrite query without this attribute

DRG-10863: invalid ORDER argument supplied to NDATA

Cause: An invalid value was supplied for ORDER argument to NDATA

Action: Set ORDER to ORDER or NOORDER.

DRG-10864: invalid PROXIMITY argument supplied to NDATA

Cause: An invalid value was supplied for PROXIMITY argument to NDATA

Action: Set PROXIMITY to PROXIMITY or NOPROXIMITY.

DRG-10865: invalid datatype in user scoring expression

Cause: The scoring expression specified in DEFINESCORE or NORMALIZATION\_EXPR in the query template either contains components with unsupported datatypes or does not return numerical values.

Action: Rewrite the scoring expression.

DRG-10866: The right hand operand of MINUS cannot use IGNORE score

Cause: The IGNORE score is used as the right hand operand of MINUS

Action: Rewrite the scoring expression.

DRG-10867: OCCURRENCE and COMPLETION score cannot be used with ABOUT in DEFINESCORE

Cause: The OCCURRENCE and COMPLETION score cannot be used with ABOUT queries

Action: Rewrite the scoring expression.

DRG-10868: matches does not support functional invocation

Cause: the query plan for your query is invoking a matches operator functionally rather than as an index rowsource. The matches operator does not support functional invocation

Action: add optimizer hints so that all matches operators are performed through index scans

DRG-10869: Invalid span supplied to NEAR2 operator

Cause: Near2 span must be between 0 and 100

Action: Use acceptable span

DRG-10870: Invalid weight supplied to NEAR2 operator

Cause: Near2 weights must be between 0 and 10

Action: Use acceptable weight

DRG-10871: NDATA operator not supported with string

Cause: NDATA operator is not supported in the specified operation

Action: Rewrite the query without NDATA operator

DRG-10872: Invalid setting of savescore in ctxfiltercache

Cause: savescore argument must be true or false

Action: set savescore to true or false

DRG-10873: Invalid setting of topn in ctxfiltercache

Cause: topn argument must be true or false

Action: set topn to true or false

DRG-10874: savescore must be true to use topn in ctxfiltercache

Cause: savescore must be true to use topn in ctxfiltercache

Action: set savescore to true to use topn processing

DRG-10875: invalid use of ctxfiltercache with topn

Cause: ctxfiltercache with topn must be child of AND, THRESHOLD, or WEIGHT operators

Action: invalid query

DRG-10876: ctxfiltercache operator requires non-zero query\_filter\_cache\_size

Cause: used ctxfiltercache operator with zero query\_filter\_cache\_size

Action: Set a non-zero query\_filter\_cache\_size

DRG-10877: Syntax error in XML Query

Cause: XML template is wrong. Possible causes include missing closing tag or receiving invalid attributes or characters.

Action: Check that the query is valid XML

DRG-10878: Missing closing tag in XML Query

Cause: Some tag has been opened and not closed properly.

Action: Close all tags properly

DRG-10879: topn must be used with order by score desc in ctxfiltercache

Cause: must order query results by score desc when topn argument is true

Action: Add order by score desc

DRG-10900: out of memory

Cause: can not allocate more memory

Action: Contact your system adminstrator

DRG-11000: invalid keyword string

Cause: A keyword was invalid.

Action: Respecify the parameter string with correct keyword

DRG-11001: missing keyword when expecting one of string

Cause: A keyword was missing.

Action: Respecify the parameter string with keyword

DRG-11002: missing value for string

Cause: A value for the argument was missing.

Action: Respecify the parameter string with value

DRG-11003: invalid value string for string

Cause: An invalid value was given for the argument

Action: Specify a valid value

DRG-11004: duplicate or conflicting value for string

Cause: More than one value has been specified for the argument

Action: Check parameter string and correct the problem parameter

DRG-11005: invalid create index parameter string

Cause: the supplied parameter string is not correct

Action: drop index and recreate index with correct parameters

DRG-11006: invalid alter index parameter string

Cause: The parameter string was invalid.

Action: Reissue the statement with the correct parameter string.

DRG-11007: multiple stopwords specified

Cause: Tried to add more than one stopword

Action: Specify one stopword at a time

DRG-11008: invalid create index partition parameter string

Cause: The parameter string was invalid

Action: drop index and recreate index with correct parameters

DRG-11100: unable to connect to the database

Cause: failed to connect to Oracle database

Action: check the Oracle error and connect string

DRG-11101: failed to open file string

Cause: failed to open a file

Action: check whether the file exist or access permission available

DRG-11102: assigned lexer can not operate on string language setting

Cause: Single byte lexer selected in multibyte language setting

Action: check RDBMS language setting or text columns lexer setting

DRG-11104: Oracle Text error:

Cause: See the next error on stack

Action: See the next error on stack

DRG-11106: user database session has terminated during this operation

Cause: this database session does not exist or has terminated

Action: determine why the user database session terminated while the operation was still being carried out.

DRG-11107: invalid path specification: string

Cause: the path specified is not valid

Action: check the path specification

DRG-11108: invalid filename specified: string

Cause: the filename specified is not valid

Action: check the filename for beginning or trailing spaces, invalid characters, or other such problems.

DRG-11109: assigned lexer does not support string query operator

Cause: This lexer does not support this query operator

Action: do not use the operator in your query

DRG-11111: value of string must be between string and string

Cause: You specified a value for the parameter which is out of range

Action: Specify a value which is in the allowed range

DRG-11112: length of string exceeds maximum of string

Cause: You specified a value for the parameter which is too long

Action: Specify a value which is less than or equal to the maximum length

DRG-11113: value of string must be one of string

Cause: You specified a value for the parameter which is invalid

Action: Specify a valid value for the parameter

DRG-11114: result table format is not correct for this operation

Cause: You specified a result table which has the wrong number, type, or names of columns for this operation.

Action: Check result table. Refer to the documentation for the correct format for each operation

DRG-11115: a value for string must be specified

Cause: You did not specify a value for the parameter

Action: Specify a value for the parameter

DRG-11116: value of string must be less than or equal to value of string

Cause: You specified values for the two parameters which are invalid

Action: Specify valid values for the parameters

DRG-11117: name is already used by an existing object

Cause: You tried to create an object whose name conflicts with an object of that type which already exists

Action: Specify a new name

DRG-11118: object string does not exist

Cause: You tried to modify or drop an object which does not exist

Action: Specify correct object name

DRG-11119: operation is not supported by this index type

Cause: You tried to invoke an operation on an index which is not supported by the index type

Action: None

DRG-11120: failed to write to file string

Cause: failed to write to a file

Action: check whether the file exist or access permission available

DRG-11121: failed to read from file string

Cause: failed to read from a file

Action: check whether the file exist or access permission available

DRG-11122: unsupported section group

Cause: unsupported section group is specified for functional contains

Action: change the section group to NULL\_SECTION\_GROUP

DRG-11123: theme indexing is not supported

Cause: theme indexing is on in the lexer preference for functional contains

Action: turn off theme indexing

DRG-11124: invalid value string

Cause: you specified an invalid value

Action: specify a valid value

DRG-11125: invalid format of existing log file string

Cause: the file specified by START\_LOG already exists, and is not a previously written log file

Action: specify a new file, or remove the existing file

DRG-11126: context index is empty

Cause: the training table is empty or the context index of training table is not populated

Action: populate the training table or context index

DRG-11127: inconsistent index policy with trained rule

Cause: the ctxrule index policy is inconsistent with the policy in which the rule was trained

Action: change the ctxrule index policy

DRG-11128: invalid format of rule

Cause: the rule format is not valid for this operation

Action: check the rule type and operation type

DRG-11129: the rule table is empty

Cause: the rule table is empty

Action: populate the rule table by training

DRG-11130: no data found in the collection

Cause: feature preparation program can not find any feature in the specified collection

Action: check the setting for extracting features.

DRG-11131: Error from Oracle XML parser: string

Cause: The Oracle XML parser reported an error

Action: Check the document for the error, and fix if necessary

DRG-11132: Invalid character in logfile name

Cause: The logfile parameter to CTX\_OUTPUT.START\_LOG or CTX\_OUTPUT.START\_QUERY\_LOG contains an invalid character (such as a forward slash)

Action: Remove the invalid character

DRG-11133: failed to convert a datatime value \[ora-number\]

Cause: Failed to convert the datetime value.

Action: Check the error code

DRG-11134: The file string is currenly being used for logging by another process

Cause: The file is currently being used by another process.

Action: Give a different file name.

DRG-11135: feature not generally available

Cause: You tried to use a feature not generally available.

Action: Contact customer support

DRG-11136: assigned lexer does not support entity extraction

Cause: This lexer does not support entity extraction

Action: Do not use this lexer for entity extraction

DRG-11137: tracing is not supported on MTS

Cause: you tried to use ctx\_output tracing in an MTS session

Action: connect using a dedicated session and retry the operation

DRG-11138: trace string is already enabled

Cause: you tried to enable a trace that is already enabled

Action: disable the trace first

DRG-11139: trace string is not enabled

Cause: you tried to disable a trace that is not enabled

Action: enable the trace first

DRG-11140: Section string is not MDATA

Cause: you tried to perform MDATA operation on non-mdata section

Action: provide correct mdata section name

DRG-11141: CTX\_DDL.REMOVE\_MDATA() and CTX\_DDL.ADD\_MDATA() not allowed for MDATA Section string

Cause: you tried to call CTX\_DDL.REMOVE\_MDATA() or CTX\_DDL.ADD\_MDATA() on a MDATA section which is created with ALLOW\_ADD\_REM parameter set to FALSE.

Action: do not call CTX\_DDL.REMOVE\_MDATA() or CTX\_DDL.ADD\_MDATA() on a MDATA section that is created with ALLOW\_ADD\_REM parameter set to FALSE.

DRG-11142: string cannot be string

Cause: The value for the specified parameter cannot be as specified

Action: Specify the correct value

DRG-11143: Only 64 errors can be traced

Cause: You tried to trace more than 64 errors with ctx\_output

Action: Trace fewer errors, or use DRG\_DUMP\_ALL\_ERRORS

DRG-11203: INSO filter not supported on this platform

Cause: You tried to use the INSO filter on a platform which does not support it

Action: Do not use the INSO filter

DRG-11204: user filter command is too long

Cause: The user filter command must be 32 characters or less

Action: Specify a shorted user filter command

DRG-11205: user filter command contains illegal characters

Cause: The user filter command cannot contain special characters such as slashes, parentheses, semicolons, etc.

Action: Correct command specification

DRG-11206: user filter command string could not be executed

Cause: The user filter command could not be executed.

Action: Check that the command exists in $ORACLE\_HOME/ctx/bin, and that it is executable.

DRG-11207: user filter command exited with status string

Cause: The user filter command exited with the given error status.

Action: See any DRG-11220, DRG-11221, DRG-11222, DRG-11223, DRG-11224, DRG-11225, or DRG-11227 error message on the error stack otherwise see error status.

DRG-11208: ORACLE\_HOME is not set

Cause: ORACLE\_HOME is not set

Action: make sure ORACLE\_HOME is set when running ctxsrv

DRG-11209: filename for string exceeds maximum length of string

Cause: Value of the file name is too long

Action: Specify a shorter filename

DRG-11210: format column must be a char, varchar, or varchar2 type

Cause: you specified a format column which is not a char, varchar, or varchar2 type.

Action: specify a format column of correct type

DRG-11211: charset column must be a char, varchar, or varchar2 type

Cause: you specified a charset column which is not a char, varchar, or varchar2 type.

Action: specify a charset column of correct type

DRG-11212: procedure filter procedure name contains a semicolon

Cause: the procedure name specified had a semicolon

Action: remove semicolon or rename procedure name. The correct format is PACKAGENAME.PROCEDURE\_NAME

DRG-11213: CTXSYS does not own procedure filter stored procedure: string

Cause: CTXSYS does not have execute privilege to the procedure filter stored procedure

Action: make sure the package is owned by CTXSYS and the procedure exist

DRG-11214: execution of procedure filter stored procedure has failed

Cause: an error occur while executing the proedure filter stored procedure

Action: check or debug the stored procedure

DRG-11215: index owner does not have access to filter stored procedure: string

Cause: the index owner does not have execute privilege of the procedure

Action: CTXSYS to grant execute privilege of the procedure to index owner

DRG-11216: length of datastore data exceeds limit

Cause: the length of the datastore data passed to the filter stored procedure is longer than the maximum length (32767 bytes)

Action: check primary key parameter

DRG-11217: INSO safe callout failed

Cause: The INSO safe callout cannot be executed

Action: check the Oracle errpr

DRG-11218: malformed mail line, line string

Cause: The mail message has an error at the indicated line

Action: manually edit mail message, if possible

DRG-11219: malformed mail configuration file, line string

Cause: mail filter configuration file has an error at the indicated line

Action: manually edit mail filter configuration file, if possible

DRG-11220: Third-party filter is out of memory.

Cause: Third-party filter could not filter this document because it was unable to allocate sufficient virtual memory.

Action: Increase virtual memory provided by the Operating System and reindex this document.

DRG-11221: Third-party filter indicates this document is corrupted.

Cause: Third-party filter could not filter this document because this document is corrupted.

Action: Fix the corruption and reindex this document.

DRG-11222: Third-party filter does not support this known document format.

Cause: Third-party filter was able to recognize the format of this document but could not filter it because this format is not supported.

Action: Remove this document or specify it to be ignored.

DRG-11223: Third-party filter indicates this document is password protected or encrypted.

Cause: Third-party filter encountered a password protected or encrypted document and could not filter it because this level of password protection or encryption is not supported.

Action: Remove this document or specify it to be ignored.

DRG-11224: Third-party filter is unable to create or write to temporary file.

Cause: Third-party filter could not filter this document because it was unable to create a temporary file or unable to write to a temporary file.

Action: Make sure that the Operating System specified temporary directory has enough space and that the Operating System Oracle user has the privileges to create files in this temporary directory.

DRG-11225: Third-party filter timed out.

Cause: Third-party filter could not filter this document because the filter timed out.

Action: Increase the value of the TIMEOUT attribute of INSO\_FILTER filter type and reindex this document. When TIMEOUT attribute is set to 0 and the session hangs then contact Oracle Support.

DRG-11226: Error initializing third-party filter: string

Cause: There was an error initializing the third-party filter.

Action: Check the following messages for details

DRG-11227: Third-party filter does not support this document format.

Cause: Third-party filter does not support the format of this document.

Action: Remove this document or specify it to be ignored.

DRG-11228: Charset filter does not support binary documents.

Cause: The format column specifies a binary document

Action: Do not attempt to filter binary documents using the charset filter

DRG-11229: configuration column must be a char, varchar, or varchar2 type

Cause: you specified a configuration column which is not a char, varchar, or varchar2 type.

Action: specify a configuration column of correct type

DRG-11301: error while indexing document

Cause: An error was encountered while indexing the document. The error may have occurred during lexing, parsing for sections, or other

Action: review document and update with valid data. Note that the document contents may have been partially indexed, so it may be returned by some queries.

DRG-11303: secondary indexes are not supported by this indextype

Cause: You attempted to create an index on an index-organized table, but the indextype does not support this action.

Action: None

DRG-11304: function-based indexes are not supported by this indextype

Cause: You attempted to create a function-based index but the indextype does not support this action.

Action: None

DRG-11305: create/alter index string is in progress in another session

Cause: you attempted to mark the index from INPROGRESS to FAILURE but create/alter on the same index is in progress in another session

Action: None

DRG-11306: operation cannot be performed on a policy

Cause: you attempted to perform an operation on a policy, but the operation is only valid for an index.

Action: None

DRG-11307: operation cannot be performed on an index

Cause: you attempted to perform an operation on an index, but the operation is only valid for a policy.

Action: None

DRG-11308: unsupported column expression string

Cause: You attempted to create an index with an unsupported column expression.

Action: None

DRG-11309: invalid filter by column: string

Cause: the column specified is not valid

Action: check that the followings are valid: a) column is of supported datatype b) valid table name, column name in the specification.

DRG-11310: invalid order by column: string

Cause: the column specified is not valid

Action: check that the followings are valid: a) column is of supported datatype b) valid table name, column name in the specification.

DRG-11311: string cannot be specified for this optimization mode

Cause: the specified option is not valid for this optimization mode

Action: remove the specified option

DRG-11312: source and new policy must have same owner

Cause: the new policy has a different owner than the source policy

Action: Ensure that both policies are owned by the same user

DRG-11313: populate index error on index partition string

Cause: failed to polulate the text index on the specified partition

Action: See the next errors on stack and take appropriate action

DRG-11314: changing TRANSACTIONAL property on index with rows on pending queue not allowed

Cause: the index has pending unsynced rows

Action: sync the index before changing the TRANSACTIONAL property

DRG-11316: $S table cannot be created with string

Cause: the $S table cannot be created with the specified storage option

Action: remove the specified option from the index preference and retry the index creation

DRG-11317: rowid string is not in the index

Cause: you specified an invalid rowid in ctx\_ddl.add\_mdata

Action: correct the rowid and retry

DRG-11318: error processing dr$sdata\_update

Cause: there was an error

Action: check the error stack for more details

DRG-11319: more than 1 index found on $I. OPTIMIZE REBUILD not supported

Cause: OPTIMIZE REBUILD is not supported due to the specified reason

Action: resolve the issue, and retry the operation

DRG-11320: no index found on $I. OPTIMIZE REBUILD not supported

Cause: OPTIMIZE REBUILD is not supported due to the specified reason

Action: resolve the issue, and retry the operation

DRG-11321: triggers detected on $I. OPTIMIZE REBUILD not supported

Cause: OPTIMIZE REBUILD is not supported due to the specified reason

Action: resolve the issue, and retry the operation

DRG-11322: fast optimize not supported for big\_io option

Cause: OPTIMIZE FAST is not supported with big\_io option

Action: run optimize full or rebuild instead

DRG-11323: merge optimize requires near\_realtime option

Cause: OPTIMIZE MERGE requires near\_realtime option

Action: run another optimize mode

DRG-11324: fast optimize not supported for separate\_offsets option

Cause: OPTIMIZE FAST is not supported with separate\_offsets option

Action: run optimize full or rebuild instead

DRG-11325: stageitab only supported for context index

Cause: STAGEITAB requires context index

Action: don't use stageitab on non context indexes

DRG-11326: separate offsets only supported for context index

Cause: SEPARATE\_OFFSETS requires context index

Action: don't use separate\_offsets on non context indexes

DRG-11327: big\_io only supported for context index

Cause: BIG\_IO requires context index

Action: don't use big\_io on non context indexes

DRG-11328: optimize validation failed

Cause: optimize validation failed

Action: file a bug

DRG-11332: Index already has STAGE\_ITAB set

Cause: Index already has stage\_itab set

Action: Do not add stage\_itab to this index

DRG-11333: Index does not have STAGE\_ITAB set

Cause: Index does not have stage\_itab set

Action: Do not remove stage\_itab from this index

DRG-11334: Index already has BIG\_IO set

Cause: Index already has big\_io set

Action: Do not add big\_io to this index

DRG-11335: Index does not have BIG\_IO set

Cause: Index does not have big\_io set

Action: Do not remove big\_io from this index

DRG-11336: Index already has SEPARATE\_OFFSETS set

Cause: Index already has separate\_offsets set

Action: Do not add separate\_offsets to this index

DRG-11337: Index does not have SEPARATE\_OFFSETS set

Cause: Index does not have separate\_offsets set

Action: Do not remove separate\_offsets from this index

DRG-11338: policy string does not exist

Cause: the specified policy does not exist or you do not have access to it.

Action: Specify an existing index

DRG-11339: $A table cannot be created with string

Cause: the $A table cannot be created with the specified storage option

Action: remove the specified option from the index preference and retry the index creation

DRG-11340: $F table cannot be created with string

Cause: the $F table cannot be created with the specified storage option

Action: remove the specified option from the index preference and retry the index creation

DRG-11341: Index optimization failed for one or more tokens

Cause: Index optimization generated an error for one or more tokens, possibly due to corruption of the token\_info blob.

Action: Check the index optimization log for the detailed error, or retry the optimize call with logging enabled

DRG-11342: OPTIMIZE REBUILD not supported for partitioned $I and global $X

Cause: OPTIMIZE REBUILD is not supported due to the specified reason

Action: resolve the issue, and retry the operation

DRG-11343: OPTIMIZE REBUILD not supported for current $I partitioning scheme

Cause: OPTIMIZE REBUILD is not supported due to the specified reason

Action: resolve the issue, and retry the operation

DRG-11344: SPLIT DOLLARI does not allow an empty mapping table input

Cause: SPLIT DOLLARI doesn't generate any output for empty mapping table

Action: populate the mapping table, and retry the operation

DRG-11345: Index optimization was interrupted

Cause: Index optimization was interrupted by ctx\_adm.stop\_optimize

Action: None

DRG-11346: OPTIMIZE REBUILD not supported for $I with character length semantics columns

Cause: OPTIMIZE REBUILD is not supported due to the specified reason

Action: resolve the issue, and retry the operation

DRG-11347: FILTER CACHE only supported for context index

Cause: FILTER CACHE only for context index

Action: Don't use FILTER\_CACHE on non context indexes

DRG-11348: SAVE COPY only supported for context index

Cause: SAVE COPY needs context index

Action: Don't use SAVE COPY on non context indexes

DRG-11349: FORWARD INDEX only supported for context index

Cause: FORWARD INDEX needs context index

Action: Don't use FORWARD INDEX on non context indexes

DRG-11350: FORWARD INDEX does not exist for this index

Cause: FORWARD INDEX does not exist

Action: Enable forward index for the index

DRG-11400: failed to parse document with key string

Cause: the document specified for linguistic extraction could not be parsed. This could indicate that the document is not well-formed English

Action: check the document contents

DRG-11403: primary key value too long

Cause: the primary key value parameter passed to the service request is longer than the maximum primary key length (64 bytes)

Action: check primary key parameter

DRG-11404: no primary key value specified

Cause: the primary key value parameter passed to the service request is null

Action: check primary key parameter

DRG-11410: could not insert into string result table

Cause: an ORACLE error occurred while linguistic output was being inserted into the result table

Action: take action appropriate to the ORACLE error code.

DRG-11418: insufficient document content for linguistic parser

Cause: the document specified for linguistic extraction was parsed but the document content was insufficient for linguistic extraction by the specified parser.

Action: check the document contents or try modifying linguistic settings

DRG-11422: linguistic initialization failed

Cause: linguistic services initialization failed

Action: Check to see if knowledge base files present for the language

DRG-11425: gist level string is invalid

Cause: invalid gist level

Action: Specify a valid gist level

DRG-11427: valid gist level values are string

Cause: Invalid gist level

Action: Specify a valid gist level

DRG-11428: document contains invalid characters

Cause: The document contains invalid characters

Action: Remove invalid characters

DRG-11432: file error while accessing knowledge base

Cause: An oracle error was encountered during knowledge base access

Action: Check to see if knowledge base files present for the language

DRG-11435: primary key value is invalid

Cause: the primary key value parameter passed to the service request is not valid

Action: check primary key parameter

DRG-11439: index name length exceeds maximum of string bytes

Cause: the length of the index name is longer than the maximum index name size

Action: drop the index and recreate the index with a shorter index name

DRG-11440: operation not supported for the string language

Cause: the requested operation is not supported for the current language

Action: Do not request this operation

DRG-11441: gist numParagraphs string is invalid

Cause: invalid gist numparagraphs

Action: Specify valid gist numparagraphs

DRG-11442: valid gist numParagraphs values are string

Cause: invalid gist numparagraphs

Action: Specify valid gist numparagraphs

DRG-11443: gist maxPercent string is invalid

Cause: invalid gist max percent

Action: Specify valid gist max percent

DRG-11444: valid gist maxPercent values are string

Cause: invalid gist max percent

Action: Specify valid gist max percent

DRG-11445: rowid value is invalid: string

Cause: the rowid value parameter passed to the service request is not valid

Action: check rowid parameter

DRG-11446: supplied knowledge base file string not installed

Cause: Either using Oracle Express edition or supplied Knowledge Base was required but was not installed.

Action: If using Oracle Express edition then upgrade to Oracle Enterprise or Oracle Standard edition. Otherwise see post-installation tasks section of the Database Installation Guide for instructions to install supplied Knowledge Base.

DRG-11480: ctxkbtc memory allocation error: %(1)

Cause: Unable to allocate memory

Action: Contact your system administrator

DRG-11481: linguistic feature not enabled

Cause: linguistic feature not enabled

Action: enable linguistic feature

DRG-11500: column name expected, found string on line string

Cause: possibly miss-spelt column name or keyword

Action: check spellings and punctuation around specified line

DRG-11501: identifier string found in place of column name on line string

Cause: possibly miss-spelt column name

Action: check spellings around specified line

DRG-11502: read of file failed at line string for file string

Cause: bad file name, wrong file\_type or file system error

Action: check file name, type and/or file integrity

DRG-11503: insert statement overflows maximum statement size

Cause: total length of statement exceeds database maximum

Action: reduce length of column names or number of columns

DRG-11504: invalid longsize parameter of string specified

Cause: invalid option argument

Action: specify long buffer size in kbytes above 0

DRG-11505: long data on line string not found or invalid

Cause: either bad data or bad data file

Action: check file exists and is accessible, if separate

DRG-11506: record ignored on line string because of error(s)

Cause: an error occured parsing this row's data

Action: move and amend line in error to alternate load file

DRG-11507: file error trying to read file string

Cause: file not found or could not be read

Action: check name and location of file

DRG-11508: bad or missing string token on line string

Cause: token expected was not found

Action: move and amend record affected to error load file

DRG-11509: value expected on line string

Cause: could not make sense of text where value expected

Action: move and amend record affected to error load file

DRG-11510: encountered unrecoverable error on line string

Cause: see previous messages

Action: see previous errors

DRG-11511: specified table does not contain a LONG RAW column

Cause: text must be inserted into a LONG RAW type column

Action: check table and type of data

DRG-11512: bad syntax for thesaurus load file at line string

Cause: load file must have specific format for loading thesaurus

Action: check documentation for description of correct format

DRG-11513: unable to open or write to file string

Cause: an attempt to open or to write to the given file failed

Action: check with system administrator

DRG-11514: user string does not have UPDATE or SELECT privilege on string

Cause: user has not been granted UPDATE or SELECT privilege

Action: check privilege on the user

DRG-11515: not enough text key values

Cause: number of values provided does not match the number of text keys

Action: provide same number of values as the number of text keys

DRG-11516: user must be at least in role CTXUSER to perform this operation

Cause: user does not have CTXUSER, CXAPP or CTXADMIN role

Action: grant user the proper role

DRG-11517: error when validating text objects

Cause: see accompanying Oracle error

Action: see accompanying Oracle error

DRG-11518: text table string does not have a LONG or LONG RAW column

Cause: table specified does not have a LONG or LONG RAW column

Action: check the table

DRG-11519: encounter error when exporting a LONG or LONG RAW column

Cause: see accompanying error message

Action: see accompanying error message

DRG-11520: error writing to file

Cause: file does not exist

Action: make sure file exists

DRG-11521: encounter error when updating a LONG or LONG RAW column

Cause: see accompanying error message

Action: see accompanying error message

DRG-11522: no row exists for the text key(s) specified

Cause: no row in the table has the text key(s) specified

Action: use a valid text key(s)

DRG-11523: unable to lock the specified row for update

Cause: some other process has a lock on the row

Action: release the lock or wait until the lock is released

DRG-11524: primary key value is missing

Cause: primary key value is not provided

Action: provide the primary key value(s)

DRG-11525: invalid commitafter parameter of string specified

Cause: invalid option argument

Action: specify commitafter above 0

DRG-11526: filename exceeds maximum length

Cause: value of the file name is too long

Action: Specify a shorter file name

DRG-11527: end token not found on line string

Cause: \<TEXTEND> not found at end of record

Action: processing discontinued - amend record

DRG-11528: LONG or LONG RAW column defintion found in structure data

Cause: could be misplaced

Action: remove reference to LONG or LONG RAW column from structure data

DRG-11529: token exceeds maximum length

Cause: value of the column name or value is too long

Action: processing discontinued - amend record

DRG-11530: token exceeds maximum length

Cause: value of the phrase or relation word is too long

Action: processing discontinued - amend record

DRG-11531: start token not found on line string

Cause: <TEXTSTART: not found at start of record

Action: processing discontinued - amend record

DRG-11532: error reading through end of line string for file string

Cause: characters encountered while reading through end of line

Action: remove extraneous characters

DRG-11533: improper value of column string

Cause: value of the column is too long or mismatched quote

Action: processing discontinued - amend record

DRG-11534: invalid column string

Cause: column does not exist or it's misspelled

Action: processing discontinued - amend record

DRG-11535: error writing phrase or qualifier: string on line string to memory

Cause: not enough memory

Action: allocate more memory, contact WorldWide Support if problem persists

DRG-11600: URL store: string has permanently moved

Cause: the document referred to by the URL has permanently moved

Action: find the new address, if any, of the document

DRG-11601: URL store: bad syntax on request for string

Cause: client did not make correct request

Action: contact support

DRG-11602: URL store: access to string requires authentication

Cause: user has to provide password or other authentication

Action: get required access, or check URL

DRG-11603: URL store: payment required to access string

Cause: payment is required before the URL can be accessed

Action: check URL, or pay if required if access necessary

DRG-11604: URL store: access to string is denied

Cause: access to the URL is denied

Action: check URL; if correct, do not try to access URL again

DRG-11605: URL store: document specified by string not found

Cause: the document can not be found on the host specified

Action: check URL

DRG-11606: URL store: access to string timed out waiting for client request

Cause: client did not make response within timeout period

Action: check URL

DRG-11607: URL store: access to string was denied due to garbled response

Cause: Web server identified in URL doesn't obey HTTP protocol

Action: contact the Web administrator of the remote host

DRG-11608: URL store: host portion of string specified incorrectly

Cause: host portion of the URL could not be parsed

Action: check URL

DRG-11609: URL store: unable to open local file specified by string

Cause: attempt to open local file failed

Action: check URL

DRG-11610: URL store: unable to read local file specified by string

Cause: attempt to read local file failed

Action: contact system administrator

DRG-11611: URL store: unknown protocol specified in string

Cause: the protocol parsed is neither http or file

Action: check URL

DRG-11612: URL store: unknown host specified in string

Cause: the address of the host specified could not be resolved

Action: check URL

DRG-11613: URL store: connection refused to host specified by string

Cause: attempt to connect to host was forcibly refused

Action: check URL

DRG-11614: URL store: communication with host specified in string timed out

Cause: a network operation timed out

Action: try again later; network connection may be down to Web server

DRG-11615: URL store: write failed sending to string over network

Cause: unknown error writing request to Web server

Action: check network connection

DRG-11616: URL store: too many redirections trying to access string

Cause: too long a chain of HTTP redirections given the URL

Action: contact the Web administrator of the remote host

DRG-11617: URL store: URL string is too long

Cause: The length of the URL string is longer than URLSIZE

Action: set URLSIZE attribute to a larger value

DRG-11618: URL store: document identified by string is too large

Cause: document larger than user-set maximum size

Action: do not access URL, or increase document size limit

DRG-11619: URL store: row in table is empty

Cause: row deleted or otherwise missing

Action: check table if necessary

DRG-11620: URL store: thread operation error

Cause: thread operation failed

Action: contact system administrator

DRG-11621: URL store: socket open error for string

Cause: socket open failed; probably too many open file descriptors

Action: reduce the maximum number of threads started

DRG-11622: URL store: unknown HTTP error string getting string

Cause: an unexpected HTTP error has occurred

Action: consult HTTP error codes; if valid, contact support

DRG-11623: URL store: unknown error getting string

Cause: unexpected error

Action: contact support

DRG-11624: invalid attribute string for string: proper range string to string

Cause: unexpected error

Action: change attribute value

DRG-11625: MAXURLS \* URLSIZE must be less than string

Cause: MAXURLS \* URLSIZE cannot be larger than the limit

Action: Lower either MAXURLS or URLSIZE

DRG-11626: URL store: unknown protocol specified during redirect from string

Cause: the URL redirected to a site with neither http nor file protocol

Action: check URL

DRG-11627: URL store: not implemented error getting string

Cause: The remote host returned a 501 not implemented error

Action: Check URL

DRG-11628: URL store: bad gateway error getting string

Cause: The remote host returned a 502 bad gateway error

Action: Check URL

DRG-11629: URL store: service unavailable error getting string

Cause: The remote host returned a 503 service temporarily unavailable error

Action: Check URL

DRG-11630: URL store: gateway timeout error getting string

Cause: The remote host returned a 504 gateway timeout error

Action: Check URL

DRG-11700: thesaurus string already exists

Cause: thesaurus with same name exists

Action: use another name

DRG-11701: thesaurus string does not exist

Cause: thesaurus does not exist

Action: use another thesaurus or create it

DRG-11702: string

Cause: error while parsing thesaurus operator in query term. see error message for details.

Action: see error message

DRG-11703: user string must have at least CTXAPP role to execute this function

Cause: privilege is not sufficient

Action: grant user CTXAPP role

DRG-11704: phrase 'string' does not exist

Cause: phrase does not exist

Action: use another phrase or create it

DRG-11705: multilevel jump from string to string

Cause: the thesaurus load file has a multilevel jump which could not be parsed.

Action: correct thesaurus file

DRG-11706: invalid relation string

Cause: You specified an invalid relation. The set of valid relations will be displayed. Additionally, you may be able to specify a translation, which has the syntax languagename: where languagename can be any string up to 10 bytes

Action: Specify a valid relation

DRG-11707: valid relations: string

Cause: You specified an invalid relation. The set of valid relations will be displayed. Additionally, you may be able to specify a translation, which has the syntax languagename: where languagename can be any string up to 10 bytes

Action: Specify a valid relation

DRG-11708: too many thesauri

Cause: ctxkbtc cannot compile more than 16 thesauri

Action: Specify fewer thesauri

DRG-11709: too many terms in thesaurus

DRG-11710: thesaurus term string too long

Action: Correct thesaurus

DRG-11711: too much data for term string

Cause: internal limit on size of data per term

Action: redesign thesaurus

DRG-11712: multiple Broader Terms for term string

Action: make sure each term has only one broader term

DRG-11713: multiple Preferred Terms per synonym ring

Action: make sure each synonym ring has only one preferred term

DRG-11714: synonyms have different Broader Terms

Action: make sure all synonyms have the same broader term

DRG-11715: attempt to add a BT relation between 2 KB categories string and string

Cause: BT relation cannot be between two existing knowledge base categories

Action: redesign the BT hierarchy

DRG-11716: attempt to add Narrower Term string for non-Preferred Term string

Cause: only a PT can have NTs

Action: attach the NT to the preferred term

DRG-11717: attempt to add Related Term string to non-Preferred Term string

Cause: only a PT can have RTs

Action: attach the RT

DRG-11718: multiple Preferred Terms for term string

Action: Correct thesaurus

DRG-11719: Broader Term hierarchy too deep

Cause: The broader term hierarchy in this thesaurus is too deep

Action: flatten the hierarchy for best results

DRG-11720: too many synonyms per synonym ring

Cause: too many synonyms for a single preferred term

Action: introduce further distinctions to deepen the hierarchy

DRG-11721: thesaurus string is empty

Cause: no entries in thesaurus

Action: add some entries or drop the thesaurus

DRG-11722: invalid language specification

Cause: language specification cannot be more than 10 characters

Action: reduce language specification to less or equal to 10 char

DRG-11723: phrase cannot be NULL

Cause: you tried to add a NULL phrase to the thesaurus

Action: specify a valid phrase

DRG-11724: phrase string already exists

Cause: phrase with same name exists

Action: use another name

DRG-11725: phrase does not have any synonyms

Cause: you tried to nominate a phrase with no synonyms to be the preferred term, or you tried to drop SYN from a phrase with no synonyms

Action: None

DRG-11726: phrase is not a preferred term

Cause: you tried to remove the preferred term relation from a phrase which is not a preferred term.

Action: None

DRG-11727: phrase does not have any related terms

Cause: you tried to drop a relation which does not exist

Action: None

DRG-11728: phrase does not have any broader terms of this type

Cause: you tried to drop a relation which does not exist

Action: None

DRG-11729: phrase does not have any narrower terms of this type

Cause: you tried to drop a relation which does not exist

Action: None

DRG-11730: relation does not exist

Cause: you tried to drop a relation which does not exist

Action: None

DRG-11731: translation does not exist

Cause: you tried to drop a translation which does not exist

Action: None

DRG-11732: phrase does not have any translations

Cause: you tried to drop translations which does not exists

Action: None

DRG-11733: more than one translation for the term in the specified language

Cause: the term has more than one translation in the specified language

Action: specified a translation

DRG-11734: missing homograph

Cause: A term of the form 'homograph(disambiguation)' is missing the the homograph.

Action: None

DRG-11735: missing disambiguation

Cause: A term of the form 'homograph(disambiguation)' is missing the the disambiguation (i.e., homograph()).

Action: None

DRG-11736: illegal text after disambiguated homograph

Cause: A term of the form 'homograph(disambiguation)' has text after the disambiguation (e.g, homograph(disambiguation) extra text".

Action: None

DRG-11801: Continue

Cause: Enquire user to decide if continue is necessary HTTP\_ERROR = 100

Action: Upon positive response, continue the original operation

DRG-11802: Switching Protocols

Cause: Telling client a protocol switching just happened HTTP\_ERROR = 101

Action: The user agent takes proper actions

DRG-11803: OK

Cause: Telling client things are ok HTTP\_ERROR = 200

Action: The user agent takes proper actions

DRG-11804: Created

Cause: Telling client things are created HTTP\_ERROR = 201

Action: The user agent takes proper actions

DRG-11805: Accepted

Cause: Telling client things are accepted but not commited HTTP\_ERROR = 202

Action: The user agent takes proper actions

DRG-11806: Non-authoritative Information

Cause: The returned metainformation is not the definitive set HTTP\_ERROR = 203

Action: The user agent knows the information is Non-authoritative

DRG-11807: No Content

Cause: request has been fulfilled but no new information found HTTP\_ERROR = 204

Action: The user agent takes proper actions

DRG-11808: Reset Content

Cause: Telling client to reset the document view HTTP\_ERROR = 205

Action: The user agent takes proper actions

DRG-11809: Partial Content

Cause: Telling client document content is a patial content HTTP\_ERROR = 206

Action: The user agent takes proper actions

DRG-11810: Partial Update OK

Cause: Telling client document is partially updated HTTP\_ERROR = 207

Action: The user agent takes proper actions

DRG-11811: Multiple Choices

Cause: Telling client multiple choices of resources is possible HTTP\_ERROR = 300

Action: The user agent takes proper actions

DRG-11812: Moved Permanently

Cause: The URI has been assigned a new permanent URI HTTP\_ERROR = 301

Action: The user agent takes proper actions

DRG-11813: Moved Temporarily

Cause: The URI resides temporarily under a different URI. HTTP\_ERROR = 302

Action: The user agent takes proper actions

DRG-11814: See Other

Cause: The URI can be found using GET METHOD under a different URI HTTP\_ERROR = 303

Action: The user agent takes proper actions

DRG-11815: Not Modified

Cause: Response to conditional GET, indicating document not modified. HTTP\_ERROR = 304

Action: The user agent takes proper actions

DRG-11816: Use Proxy

Cause: The client should use specified proxy to repeat the request HTTP\_ERROR = 305

Action: The user agent takes proper actions

DRG-11817: Proxy Redirect

Cause: Proxy redirection. Not used HTTP\_ERROR = 306

Action: Outdated due to HTTP evolution

DRG-11818: Temporary Redirect

Cause: The resource is temporarily under a different URI. HTTP\_ERROR = 307

Action: The takes proper actions

DRG-11819: Bad Request

Cause: The URL syntax is incorrect. Request rejected by server. HTTP\_ERROR = 400

Action: The user agent takes proper actions

DRG-11820: Unauthorized

Cause: The request requires further authentication. HTTP\_ERROR = 401

Action: The user agent takes proper actions

DRG-11821: Payment Required

Cause: Reserved for future use. HTTP\_ERROR = 402

Action: The user agent takes proper actions

DRG-11822: Forbidden

Cause: The server refuses to fulfil the request from client HTTP\_ERROR = 403

Action: The user agent takes proper actions

DRG-11823: Not Found

Cause: The server can not find the requested URI HTTP\_ERROR = 404

Action: The user agent takes proper actions

DRG-11824: Method Not Allowed

Cause: The user agent specified method not allowed HTTP\_ERROR = 405

Action: The user agent reads allow header to decide alternatives.

DRG-11825: Not Acceptable

Action: The user agent should query the user for the next action.

DRG-11826: Proxy Authentication Required

Cause: The client must authenticate itself with the proxy. HTTP\_ERROR = 407

Action: The user agent takes proper actions

DRG-11827: Request Timeout

Cause: The server is tired of waiting for the requst HTTP\_ERROR = 408

Action: The user agent repeat the request

DRG-11828: Conflict

Cause: The request conflicts with the current state of the URI HTTP\_ERROR = 409

Action: The user agent takes proper actions

DRG-11829: Gone

Cause: The resource is no longer available and no forwarding address. HTTP\_ERROR = 410

Action: The user agent takes proper actions

DRG-11830: Length Required

Cause: The server must receive a content-length header. HTTP\_ERROR = 411

Action: The user agent takes proper actions

DRG-11831: Precondition Failed

Cause: Telling the user agent that the resource failed preconditions HTTP\_ERROR = 412

Action: The user agent takes proper actions

DRG-11832: Request Entity Too Large

Cause: Request rejected because request entity is too large. HTTP\_ERROR = 413

Action: If Retry-After header found, the user agent should retry.

DRG-11833: Request-URI Too Big

Cause: The server is refusing to accept the URI which is too big. HTTP\_ERROR = 414

Action: The user agent takes proper actions

DRG-11834: Unsupported Media Type

Cause: The server is refusing the request because of media type HTTP\_ERROR = 415

Action: The user agent takes proper actions

DRG-11835: Requested Range Not Satisfiable

Cause: The byte range request can not be satisfied by the resource extent. HTTP\_ERROR = 416

Action: The user agent reads content-range header in the response.

DRG-11836: Expectation Failed

Cause: Server can not meet the user agent's expectation. HTTP\_ERROR = 417

Action: The user agent takes pro

DRG-11837: Reauthorization Required

Cause: Reserved HTTP\_ERROR = 418

Action: Reserverd

DRG-11838: Proxy Reauthentication Required

Cause: Reserved HTTP\_ERROR = 419

Action: Reserved

DRG-11839: Internal Server Error

Cause: The server encountered internal error in fulfilling the request. HTTP\_ERROR = 500

Action: The user agent takes proper actions

DRG-11840: Not Implemented

Cause: The server can't support a request feature which has yet to be implemented. HTTP\_ERROR = 501

Action: The user agent takes proper actions

DRG-11841: Bad Gateway

Cause: In serving the request, the server received invalid response from gateway. HTTP\_ERROR = 502

Action: The user agent takes proper actions

DRG-11842: Service Unavailable

Cause: Server overloaded or in maintenance mode. HTTP\_ERROR = 503

Action: If retry-after header is in the response, retry the request.

DRG-11843: Gateway Timeout

Cause: Upstream server did not timely respond to the gateway server. HTTP\_ERROR = 504

Action: The user agent takes proper actions

DRG-11844: HTTP Version Not Supported

Cause: The HTTP version in the request header is rejected by the server. HTTP\_ERROR = 505

Action: The user agent takes proper actions

DRG-11845: No Partial Update

Cause: Reserved HTTP\_ERROR = 506

Action: Reserved

DRG-11846: Response Is Stale

Cause: The the user agent knows the returned reponse is stale. HTTP\_CACHE\_ERROR = 10

Action: The user agent client takes proper actions.

DRG-11847: Revalidation Failed

Cause: User agent's attempt to revalidate a stale response failed. HTTP\_CACHE\_ERROR = 11

Action: The user agent client takes proper actions

DRG-11848: Disconnected Operation

Cause: The cache is intentionally disconnected for a time period. HTTP\_CACHE\_ERROR = 12

Action: The user agent client takes proper actions

DRG-11849: Heuristic Expiration

Cause: Cache freshness lifetime and response age both greater than 24 hours. HTTP\_CACHE\_ERROR = 13

Action: The user agent client takes proper actions

DRG-11850: Transformation Applied

Cause: Telling cache manager, content encoding/media type has been changed in cache. HTTP\_CACHE\_ERROR = 14

Action: The user agent takes proper actions

DRG-11851: Cache Related Warning

Cause: Arbitrary information about cache to be presented to logger. HTTP\_CACHE\_ERROR = 99

Action: The user agent client must not take any automated action.

DRG-11852: Can't Locate Remote Host

Cause: connection to remote host failed USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11853: No Host Name Found

Cause: The host name is not specicied in URI. USER\_AGENT\_ERROR

Action: The user agent client takes proper action.

DRG-11854: No File Name Found Or File Not Accessible

Cause: Unable to open the file specified USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11855: FTP Server Replies

Cause: FTP server responds to the agent request USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11856: FTP Server Doesn't Reply

Cause: No response from FTP server during operation. USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11857: Server Timed Out

Cause: Server operation timed out USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11858: Gopher Server Replies

Cause: Gopher server responds to the agent request. USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11859: Data Transfer Interrupted

Cause: Processing of URL request was interrupted USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11860: Connection Establishment Interrupted

Cause: Connection operation was interupped USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11861: CSO-server Replies

Cause: Telling client things are ok USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11862: This Is Probaly A HTTP Server 0.9 Or Less

Cause: A very old web server USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11863: Bad, Incomplete, Or Unknown Response

Cause: The server is mumbering something not understandable USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11864: Unknown Access Authentication Scheme

Cause: The server is using an unkown access authentication scheme USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11865: News Server Replies

Cause: News Server is responding USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11866: Please Try \`ftp://' Instead Of \`file://'

Cause: wrong access scheme is used. USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11867: Method Not Suited For Automatic Redirection

Cause: Telling client things are ok USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11868: Too Many Redirections

Cause: The web server setup configured too many redirections USER\_AGENT\_ERROR

Action: The user agent client should take proper actions

DRG-11869: Premature End Of File Detected

Cause: Detected end of file is unexpected USER\_AGENT\_ERROR

Action: The user agent client takes proper actions

DRG-11870: Response From WAIS Server Too Large -- Extra Lines Ignored

Cause: Response from WAIS caused buffer overflow USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11871: WAIS Server Doesn't Return Any Data

Cause: Bad WAIS Server USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11872: Can't Connect To WAIS Server

Cause: Connect to WAIS server failed USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11873: System Call Replies

Action: The user agent takes proper actions

DRG-11874: Wrong Or Unknown Access Scheme

Cause: Protocol class is wrongfully connected to ther server USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11875: Access Scheme Is Not Allowed

Cause: Telling client things are ok USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11876: When Your Are Connected, You Can Log In

Cause: Pass information to telnet agent USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11877: This Cache Version Has Expired And Will Be Automatically Reloaded

Cause: Need to tell user that cache entry has been reloaded USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11878: Loading New Rules Must Be Explicitly Acknowledged

Cause: Let user agent client be aware of new rule loading USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-11879: Automatic Proxy Redirection Msut Be Explicitly Acknowledged

Cause: Let user agent client be aware of proxy redirection USER\_AGENT\_ERROR

Action: The user agent takes proper actions

DRG-12001: Please enter username:

Cause: Prompt user for name W3CLIB\_MSG = 0

Action: The user agent client takes proper actions

DRG-12002: Please enter username for proxy authentication:

Cause: Prompt user for name W3CLIB\_MSG = 1

Action: The user agent client takes proper actions

DRG-12003: Please enter username for this FTP server:

Cause: Prompt user for name W3CLIB\_MSG = 2

Action: The user agent client takes proper actions

DRG-12004: Password:

Cause: Prompt user for password W3CLIB\_MSG = 3

Action: The user agent client takes proper actions

DRG-12005: Please give name of file to save in:

Cause: Prompt user for file name W3CLIB\_MSG = 4

Action: The user agent client takes proper actions

DRG-12006: Plase enter account:

Cause: Prompt user for account W3CLIB\_MSG = 5

Action: The user agent client takes proper actions

DRG-12007: You might not be allowed to use this method here, continue?

Cause: Warn user of deny of service. W3CLIB\_MSG = 6

Action: The user agent client takes proper actions

DRG-12008: Location has moved, continue?

Cause: Warn user of location changes. W3CLIB\_MSG = 7

Action: The user agent client takes proper actions

DRG-12009: A new set of rules is requested to be added to your setup - continue?

Cause: Warn user of rule changes. W3CLIB\_MSG = 8

Action: The user agent client takes proper actions

DRG-12010: This file already exists - replace existing file?

Cause: Warn user of pending replacement W3CLIB\_MSG = 9

Action: The user agent client takes proper actions

DRG-12011: Authentication failed - retry?

Cause: Warn user of authentication failure W3CLIB\_MSG = 10

Action: The user agent client takes proper actions

DRG-12012: Proxy authentication failed - retry?

Cause: Warn user of proxy authentication failure W3CLIB\_MSG = 11

Action: The user agent client takes proper actions

DRG-12013: This method has already been performed - repeat operation?

Cause: Warn user the repetition of previous method used W3CLIB\_MSG = 12

Action: The user agent client takes proper actions

DRG-12014: This document is very big - continue operation?

Cause: Warn user of big document processing W3CLIB\_MSG = 13

Action: The user agent client takes proper actions

DRG-12015: The source document for this operation has moved - continue?

Cause: Warn user of location changes W3CLIB\_MSG = 14

Action: The user agent client takes proper actions

DRG-12016: The target document for this operation has moved - continue?

Cause: Warn user of destination document changes W3CLIB\_MSG = 15

Action: The user agent client takes proper actions

DRG-12017: A redirection may change the behavior of this method - proceed anyway?

Cause: Warn user of redirection effects on method W3CLIB\_MSG = 16

Action: The user agent client takes proper actions

DRG-12018: Encountered an automatic request for changing proxy - continue?

Cause: Warn user of automatic proxy change W3CLIB\_MSG = 17

Action: The user agent client takes proper actions

DRG-12201: section group string already exists

Cause: Section group with the same name already exists

Action: Use another name or delete the existing one first

DRG-12202: error while creating section group

Cause: detect an Oracle error while creating section group

Action: see the accompanying Oracle error and take appropriate action

DRG-12203: section group string does not exist

Cause: section group provided does not exist

Action: provide an existing section group

DRG-12204: error while dropping section group string

Cause: detect an Oracle error while dropping a section group

Action: see the accompanying Oracle error and take appropriate action

DRG-12206: tag string already exists in section group string

Cause: the start tag provided already exists in the same Section

Action: provide another start tag

DRG-12210: error while adding section string

Cause: detect an Oracle error while adding a section

Action: see the accompanying Oracle error and take appropriate action

DRG-12211: section or section id string does not exist

Cause: Section name or Section id to be dropped does not exist

Action: provide an existing Section name or Section id

DRG-12212: error while dropping section string

Cause: detect an Oracle error while dropping a Section

Action: see the accompanying Oracle error and take appropriate action

DRG-12213: cannot create/drop section group or sections for other user

Cause: You can only create/drop section group objects of your own

Action: have the other user create/drop his/her own objects

DRG-12217: tags cannot be more than 64 bytes

Cause: max limit of start and end tag is 64 bytes

Action: provide a shorter start and end tag

DRG-12218: section group name missing

Cause: must provide section group name

Action: provide a section group name when creating Section or section group

DRG-12219: section name missing

Cause: must provide Section name when creating a Section

Action: provide a Section name

DRG-12220: a valid tag must be provided

Cause: must provide tag when adding a section to a section group

Action: provide a tag

DRG-12223: section name string is a reserved name

Cause: you tried to name a section a reserved name

Action: Specify a different name for the section

DRG-12224: use ctx\_ddl.create\_section\_group to create section groups

Cause: you tried to use ctx\_ddl.create\_preference to create a section group

Action: use ctx\_ddl.create\_section\_group

DRG-12225: this type of section cannot be added to this section group

Cause: You tried to add sections to the null section group, add a stop section to a non-auto section group, or add a zone or field section to the auto section group

Action: Do not add this type of section to this section group

DRG-12226: a field section named string already exists in this section group

Cause: you tried to name an attribute or zone section the same name as an existing field section

Action: use another name

DRG-12227: a zone section named string already exists in this section group

Cause: you tried to name an attribute or field section the same name as an existing zone section

Action: use another name

DRG-12228: maximum number of field sections (string) exceeded

Cause: a section group has more than the maximum number of unique field sections

Action: no action required

DRG-12229: special section string already exists in this section group

Cause: you tried to add a special section which already exists

Action: no action required

DRG-12230: special section name must be one of string

Cause: you tried to add an invalid special section

Action: specify a valid special section

DRG-12231: an attr section named string already exists in this section group

Cause: you tried to name a field or zone section the same name as an existing attribute section

Action: use another name

DRG-12232: invalid attribute tag format

Cause: you specified a tag for use as an attribute tag which did not have the correct format. An attribute tag must have the form TAG@ATTR

Action: use correct format

DRG-12233: xml sections cannot co-exist with other section types

Cause: you tried to add an xml section to a section group or index which already has zone, field, attr, or special sections, or you tried to add a zone, field, attr, or special section to a section group or index which already has xml sections

Action: None

DRG-12234: column string already mapped in section group string

Cause: you tried to add a column section which already exists

Action: use correct format

DRG-12235: an sdata section named string already exists in this section group

Cause: you tried to name a non-sdata section the same name as an existing sdata section

Action: use another name

DRG-12236: an mdata section named string already exists in this section group

Cause: you tried to name a non-mdata section the same name as an existing mdata section

Action: use another name

DRG-12237: a section named string already exists in this section group

Cause: you tried to map a column but the section name is already being used by another section

Action: use another name

DRG-12238: maximum number of mdata sections (string) exceeded

Cause: a section group has more than the maximum number of unique mdata sections

Action: no action required

DRG-12239: maximum number of sdata sections (string) exceeded

Cause: a section group has more than the maximum number of unique sdata sections

Action: no action required

DRG-12240: ORDER BY column string must be indexed as an SDATA section

Cause: an order by column has been mapped to an MDATA section

Action: adjust section group

DRG-12241: column name string is not a valid section name

Cause: an order by or filter by column cannot be implicitly mapped to an SDATA section because the name is not valid as a section name

Action: adjust section group to map column name to a valid section name

DRG-12242: value of string is too large for section string

Cause: the value of a filter by or order by column is too large to be indexed

Action: update the row

DRG-12243: invalid datatype

Cause: the datatype specified for a sdata or mdata section is invalid

Action: specify a supported datatype

DRG-12244: data conversion error for sdata section string

Cause: failed to convert data

Action: check the format of the data

DRG-12245: SDATA operator not compatible with the sdata section string

Cause: failed to convert data

Action: check the format of the data

DRG-12246: SDATA operand not compatible with the sdata section string

Cause: failed to convert data

Action: check the format of the data

DRG-12247: maximum number of NDATA sections (string) exceeded

Cause: a section group has more than the maximum number of unique NDATA sections

Action: no action required

DRG-12248: a NDATA section named string already exists in this section group

Cause: you tried to name a non-NDATA section the same name as an existing NDATA section

Action: use another name

DRG-12249: a MVDATA section named string already exists in this section group

Cause: you tried to name a non-MVDATA section the same name as an existing MVDATA section

Action: use another name

DRG-12250: maximum number of mvdata sections (string) exceeded

Cause: a section group has more than the maximum number of unique mvdata sections

Action: no action required

DRG-12300: an index with this column list already exists in the index set

Cause: You tried to add an index to an index set, but an index with the specified column list already exists

Action: None

DRG-12301: index does not exist in index set

Cause: You tried to remove an index from an index set, but the specified index was not found

Action: None

DRG-12302: invalid column list

Cause: You specified an invalid column list -- it may have a syntax error, duplicate columns, or invalid column names

Action: None

DRG-12303: cannot add more than 99 indexes to an index set

Cause: You tried to add too many indexes to the index set

Action: None

DRG-12304: index set string does not exist

Cause: You specified an invalid index set name

Action: None

DRG-12305: column string data type is not supported for index set columns

Cause: You specified a column in the column list of an index of an index set which does not have a valid datatype

Action: use only DATE, NUMBER, CHAR, or VARCHAR2 columns in index column lists

DRG-12306: column string is too long for index set columns

Cause: You specified a column in the column list of an index of an index set which is too long

Action: CHAR and VARCHAR2 columns must be 30 bytes or less max length

DRG-12307: column string is NULL and cannot be indexed

Cause: You tried to index a row where at least one of the meta columns was NULL.

Action: provide a value for the meta column and reindex the row

DRG-12308: use ctx\_ddl.create\_index\_set to create index sets

Cause: you tried to use ctx\_ddl.create\_preference to create an index set

Action: use ctx\_ddl.create\_index\_set

DRG-12400: template string is empty

Cause: The template is empty.

Action: Check the template was installed successfully.

DRG-12401: invalid template: query within a loop

Cause: A CTX EXEC tag cannot occur within a CTX REPEAT tag.

Action: Remove the CTX EXEC tag.

DRG-12402: error processing template string, line string

Cause: An error occurred when processing a template.

Action: See other errors on the stack and take the appropriate action.

DRG-12403: template string was not found

Cause: The template does not exist.

Action: Check the name of the template and check that it is installed.

DRG-12404: more than one template string found

Cause: More than one template with the same name was found.

Action: Remove templates as appropriate.

DRG-12405: error occurred processing CTX REDIRECT or CTX LABEL tag

Cause: Error in syntax of a tag.

Action: Correct the syntax of the tag.

DRG-12406: invalid CTX EXEC tag attribute (string)

Cause: The specified attribute is incorrectly specified.

Action: Check the sytax of the specified attribute.

DRG-12407: invalid CTX REPEAT tag attribute (string)

Cause: The specified attribute is incorrectly specified.

Action: Check the sytax of the specified attribute.

DRG-12408: invalid variable reference: string.string

Cause: The variable referenced does not exist.

Action: Check the label and column name.

DRG-12409: syntax error for label in string

Cause: The SQL in a CTX EXEC tag has incorrect syntax for a label or label type.

Action: Check the SQL attribute of the CTX EXEC tag.

DRG-12410: could not process CTX EXEC tag

Cause: An error occurred when processing the SQL attribute of a CTX EXEC tag.

Action: See other errors on the stack and take the appropriate action.

DRG-12411: SQL processing error: string

Cause: Error executing SQL from SQL attribute of CTX EXEC tag.

Action: Check the SQL in the SQL attribute.

DRG-12412: missing or invalid Template Processor attribute (string)

Cause: The specified attribute was missing or invalid in a HTML input field.

Action: Check the Template Processor-specific attributes in the INPUT, SELECT, RADIO and CHECKBOX tags of the template.

DRG-12422: write to client failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12430: mandatory argument missing: string

Cause: This argument is mandatory.

Action: Re-submit the URL with this argument supplied.

DRG-12431: configuration section string not found

Cause: Specified conf argument is invalid.

Action: Re-submit the URL with this argument corrected.

DRG-12432: configuration file string not found or unreadable

Cause: An error occurred when processing the configuration file.

Action: Contact the administrator.

DRG-12433: load of string JDBC driver class failed

Cause: Driver class is invalid.

Action: Contact the administrator to modify configuration.

DRG-12434: connection failed using configuration string information

Cause: Configuration information is not correct.

Action: Contact the administrator to modify configuration.

DRG-12435: highlight table allocation failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12436: document table allocation failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12437: highlight table release failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12438: document table release failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12439: highlight table read failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12440: document table read failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12441: counting the number of highlights failed

Cause: See the following messages.

Action: Contact the administrator.

DRG-12500: stoplist string already exists

Cause: the specified stop list already exists

Action: must remove the duplicate stop list if you want to re-create it.

DRG-12501: null stoplist is not allowed

Cause: the specified stop list is null

Action: mustspecify a valid stop list

DRG-12502: cannot modify stoplists owned by other users

Cause: You can only create/drop Stop List or Stop Word objects of your own

Action: have the other user create/drop his/her own objects

DRG-12503: error while creating or dropping stoplist

Cause: detect an Oracle error while creating Stop List

Action: see the accompanying Oracle error and take appropriate action

DRG-12504: stoplist string does not exist

Cause: the specified stop list does not exist

Action: check that the Stop List is valid

DRG-12505: error while adding or removing a stop word

Cause: detect an Oracle error while adding or removing Stop Word

Action: see the accompanying Oracle error and take appropriate action

DRG-12506: stop word string does not exist in stoplist string

Cause: the specified Stop Sord does not exist

Action: check that the Stop Word is valid

DRG-12507: stop word string already exists in this stoplist

Cause: the specified stop word already exists

Action: must remove the duplicate word if you want to re-create it.

DRG-12508: null stop words are not allowed

Cause: the specified stop word is null

Action: must remove the null stop word if you want to re-create it.

DRG-12509: length of the stop word string exceeded the limit of string bytes

Cause: A stop list entry has exceeded the maximun length

Action: Reduce the length of the stop list entry

DRG-12511: use ctx\_ddl.create\_stoplist to create stoplists

Cause: you tried to use ctx\_ddl.create\_preference to create a stoplist

Action: use ctx\_ddl.create\_stoplist

DRG-12512: invalid stop class string

Cause: you specified an invalid stop class

Action: specify a valid stop class

DRG-12513: valid stop classes are: string

Cause: You specified an invalid stop class

Action: Specify a valid stop class

DRG-12514: languages must be specified for stopwords in a MULTI\_STOPLIST

Cause: You tried to add a stopword to a multi\_stoplist without specifying the language of the stopword

Action: Specify the language of the stopword

DRG-12515: cannot specify language for stopwords in a BASIC\_STOPLIST

Cause: You tried to add a language-specific stopword to a basic stoplist.

Action: Do not specify language for the stopword

DRG-12516: language column must be specified when using the multi stoplist

Cause: you tried to create an index using a multi stoplist but you did not specify a language column

Action: specify a language column

DRG-12517: cannot add stopthemes to a MULTI\_STOPLIST

Cause: you tried to add a stoptheme to a MULTI\_STOPLIST. This is not supported in this version.

Action: None

DRG-12518: cannot use this option with MULTI\_STOPLIST

Cause: index already has multi\_stoplist

Action: can only be used to migrate from basic to multi stoplist

DRG-12519: LANGUAGE COLUMN missing

Cause: index does not have a language column

Action: specify language column value

DRG-12520: LANGUAGE COLUMN mismatch

Cause: LANGUAGE COLUMN does not match language column of the Index

Action: index language column should match specified one

DRG-12521: cannot add STOP PATTERN to NUMBERS stopclass

Cause: NUMBERS is a predefined stopclass to specify numeric values

Action: use any other alphanumeric word

DRG-12600: user datastore procedure name contains a semicolon

Cause: the procedure name specified had a semicolon

Action: remove semicolon or rename procedure name. The correct format is PACKAGENAME.PROCEDURE\_NAME

DRG-12601: invalid user datastore procedure name: string

Cause: the format of the procedure name is invalid. It should be in the form PACKAGENAME.PROCEDURENAME or PROCEDURENAME

Action: make sure PROCEDURE attr has the format PACKAGENAME.PROCEDURENAME or PROCEDURENAME

DRG-12602: index owner does not have access to user datastore procedure: string

Cause: the index owner does not have execute privilege of the procedure

Action: CTXSYS to grant execute privilege of the procedure to index owner

DRG-12603: CTXSYS does not own user datastore procedure: string

Cause: CTXSYS does not have execute privilege to the user datastore procedure

Action: make sure the package is owned by CTXSYS and the procedure exist

DRG-12604: execution of user datastore procedure has failed

Cause: an error occur while executing the user datastore procedure

Action: check or debug the datastore procedure

DRG-12605: datatype of column number in COLUMNS list is not supported

Cause: one or more of the columns in the column list of the multi datastore are of a type which the multi datastore is unable to process

Action: change the column list of the multi datastore to contain only supported types. PL/SQL functions can be used in the comlumn list to convert unsupported types to supported types.

DRG-12606: error encountered while parsing COLUMNS list

Cause: An oracle error was encountered while parsing the columns list of the multi datastore.

Action: See next error on stack and take appropriate action

DRG-12607: only ctxsys can create MULTI\_COLUMN preferences

Cause: In order to create a multi column datastore preference, the effective user must be ctxsys.

Action: contact your DBA to create the preference as ctxsys

DRG-12700: seed word must be a single word

Cause: seed word is not a single word

Action: use a single-word seed word

DRG-12800: Attribute NESTED\_TYPE must have owner name as prefix

Cause: the attribute NESTED\_TYPE does not have an owner name prefix

Action: reset the attribute NESTED\_TYPE to include owner name prefix

DRG-12801: invalid type: string

Cause: invalid nested\_type or

Action: check the owner and the type attribute names

DRG-12802: invalid type column: string

Cause: column specified does not exist in the type table

Action: check the type table

DRG-12803: invalid text datatype

Cause: LONG and LONG RAW are not supported in nested table

Action: change text column to a supported data type

DRG-12900: Operation:string for index: string has already been started

Cause: the specified operation has been started

Action: None

DRG-13000: error while adding or removing a sub lexer

Cause: see next error

Action: None

DRG-13001: sub lexer and multi lexer must have the same owner

Cause: you specified a sub lexer which is not owned by the owner of the enclosing multi-lingual lexer preference

Action: specify a sub lexer owned by the owner of the multi-lexer preference

DRG-13002: preference string is not a MULTI\_LEXER

Cause: you tried to add a sub lexer to a lexer preference which cannot accept sub lexers. Only multi-lingual lexers can accept sub lexers.

Action: specify a multi lingual lexer

DRG-13003: preference string cannot be used as a sub lexer

Cause: you specified a preference for sub lexer which is not a lexer, or is a multi-lingual lexer

Action: specify a sub lexer which is not a multi-lingual lexer

DRG-13004: language is invalid

Cause: you specified an invalid language for the sub lexer or stopword

Action: specify a valid language -- see NLS Support Guide for a list of valid languages

DRG-13005: alt\_value cannot be an NLS language name

Cause: you specified an NLS language name as the alt value

Action: specify a non-NLS value

DRG-13006: sub lexer for this language is not defined

Cause: you tried to remove a sub lexer for a language, but no sub lexer was defined for that language

Action: None

DRG-13007: cannot define an alternate value for the DEFAULT sub lexer

Cause: you tried to define an alternate value for the DEFAULT sub lexer

Action: None

DRG-13008: cannot remove the DEFAULT sub lexer

Cause: you tried to remove the DEFAULT sub lexer

Action: None

DRG-13009: multi lexer preference does not have a DEFAULT sub lexer

Cause: you tried to use a multi lexer preference which does not have a DEFAULT sub lexer defined

Action: add a DEFAULT sub lexer to the multi lexer preference and retry

DRG-13010: alt\_value is already used by another sub lexer

Cause: you tried to specify an alt value which is already in use by another sub lexer in the lexer preference

Action: specify a different alt value

DRG-13011: language column must be specified when using the multi lexer

Cause: you tried to create an index using a multi lexer preference, but you did not specify a language column

Action: specify a language column

DRG-13012: language column must be a char, varchar, or varchar2 type

Cause: you specified a language column which is not a char, varchar, or varchar2 type.

Action: specify a language column of correct type

DRG-13013: cannot have language independent DEFAULT sub lexer

Cause: you tried to define a language independent DEFAULT sub lexer

Action: DEFAULT sub lexer can only be language dependent

DRG-13014: base table has rows with language column value string

Cause: there are documents in the base table with language column value set to symbol for sublexer or stopword being removed

Action: base table should not have such rows

DRG-13015: sublexer string already exists in the index

Cause: cannot add a sub\_lexer more than once

Action: if you want to update sub\_lexer preferences, use update sub\_lexer parameter or remove currently used sub\_lexer

DRG-13100: index is not partitioned

Cause: you attempted to invoke a partition-level operation on an index which is not partitioned

Action: invoke appropriate index-level operation

DRG-13101: partition string does not exist in this index

Cause: you specified a partition name which does not exist

Action: specify correct partition name

DRG-13102: index partition name must be specified

Cause: you attempted to invoke a partition-level operation on a partitioned index but did not specify the partition name

Action: None

DRG-13103: index table string is partitioned

Cause: you attempted to perform an exchange partition including indexes, but one or more of the internal index tables are partitioned.

Action: specify EXCLUDING INDEXES on the exchange partition, then manually rebuild the indexes.

DRG-13104: indexes do not have equivalent settings for string

Cause: you attempted to perform an exchange partition including indexes, but the specified metadata setting is not equivalent across the two indexes, so the data cannot be exchanged

Action: specify EXCLUDING INDEXES on the exchange partition, then manually rebuild the indexes.

DRG-13200: failed to load dictionary file string

Cause: failed to load a dictionary file

Action: check whether the dictionary file exists in $ORACE\_HOME/ctx/data/kolx or access permission is available

DRG-13201: KOREAN\_LEXER is desupported

Cause: Using lexer type KOREAN\_LEXER which is desupported.

Action: Use lexer type KOREAN\_MORPH\_LEXER instead.

DRG-13300: document size bigger than string bytes

Cause: size of the document being indexed is larger than the maximum supported size for the VARCHAR2 interface of stored procedure

Action: use the CLOB interface for the stored procedure

DRG-13301: syntax error in token data when expecting string, at line string

Cause: token data returned by the user-defined lexer procedure is incorrect

Action: modify user-defined lexer procedure to return expected data

DRG-13302: number of wildcard offsets must be in the range string..string, at line string

Cause: number of wildcard offsets specified as value for the wildcard attribute does not meet the supported range

Action: modify user-defined lexer query procedure to return valid number of wildcard offsets

DRG-13303: value of wildcard offset must be in the range string..string, at line string

Cause: value of pre-normalized wildcard offset or post-normalized wildcard offset specified as value for the wildcard attribute does not meet the supported range

Action: modify user-defined lexer query procedure to return valid value for wildcard offset

DRG-13304: character referenced by wildcard attribute is not a wildcard character, at line string

Cause: The wildcard attribute value specified the offset of a wildcard character. The character at the specified offset is neither the '%' character nor the '\_' character.

Action: Modify user-defined lexer query procedure.

DRG-13305: 'off' attribute value must be in the range string..string, at line string

Cause: value of 'off' attribute does not meet the supported range

Action: modify user-defined lexer index procedure to return valid value for 'off' attribute

DRG-13306: 'len' attribute value must be in the range string..string, at line string

Cause: value of 'len' attribute does not meet the supported range

Action: modify user-defined lexer index procedure to return valid value for 'len' attribute

DRG-13307: 'off'=string and 'len'=string references character past end-of-file of string character document, at line string

Cause: value of 'off' attribute plus value of 'len' attribute is greater than the number of characters in the document

Action: modify user-defined lexer index procedure to return valid values for 'off' and 'len' attributes

DRG-13308: query operator ABOUT not supported by USER\_LEXER

Cause: the query contains an ABOUT operator while using USER\_LEXER lexer type

Action: remove ABOUT operator from query or use lexer type other than USER\_LEXER

DRG-13309: operation not supported by USER\_LEXER

Cause: USER\_LEXER does not support this operation

Action: stop the operation or use alternate lexer type

DRG-13310: index owner does not have EXECUTE privilege on USER\_LEXER stored procedure string

Cause: user CTXSYS did not grant EXECUTE privilege on USER\_LEXER stored procedure to the index owner

Action: user CTXSYS grant EXECUTE privilege on USER\_LEXER stored procedure to index owner

DRG-13311: USER\_LEXER stored procedure name contains a semicolon

Cause: the procedure name contains a semicolon character

Action: remove semicolon from procedure name or rename stored procedure

DRG-13312: user CTXSYS does not own USER\_LEXER stored procedure string

Cause: CTXSYS does not have EXECUTE privilege on the USER\_LEXER stored procedure

Action: make sure the stored procedure exists and is owned by CTXSYS

DRG-13400: Oracle Data Mining was not installed

Cause: The function you used depends on Oracle Data Mining, which has not been installed yet.

Action: make sure the Oracle Data Mining is installed

DRG-13401: the preference string type is not supported in this API

Cause: the type you have specified is not supported

Action: use a different type

DRG-13500: Parameter\_string must start with string

Cause: Wrong syntax for parameter\_string.

Action: Make sure the parameter\_string has the correct syntax

DRG-13501: Shadow Index Already Exists

Cause: A shadow index was previously created already

Action: Drop the shadow index and try again

DRG-13502: NOPOPULATE is not allowed in recreate\_index\_online

Cause: Specify NOPOPULATE in parameter\_string in recreate\_index\_online

Action: Don't specify NOPOPULATE.

DRG-13503: POPULATE is not allowed for a local index in create\_shadow\_index

Cause: Specify POPULATE for a local index during create\_shadow\_index

Action: Don't specify POPULATE.

DRG-13504: string has no shadow index

Cause: Tried to perform exchange shadow without creating shadow index first

Action: create a shadow index before doing exchanges\_shadow\_index

DRG-13505: Keyword string is not allowed here in parameter\_string

Cause: Wrong syntax for parameter\_string

Action: Make sure the parameter\_string has the correct syntax

DRG-13506: string has no shadow part

Cause: Tried to perform exchange shadow part without creating shadow part first

Action: create a shadow part before doing exchanges\_shadow\_index on the partition.

DRG-13507: SWAP and NOPOPULATE is incompatible

Cause: Specified SWAP and NOPOUPLATE in parameter string

Action: Correct the parameter string setting

DRG-13508: Not all partitions for index string are swapped

Cause: try to swap an local partitioned index when not all partitions are swapped

Action: Swap all partitions first, then swap the (local) index.

DRG-13509: error while swapping shadow index

Cause: an error occurred during the shadow index swap

Action: check error message stack for the actual error

DRG-13510: shadow index does not exist

Cause: Tried to perform exchange shadow without creating shadow index first

Action: create a shadow index before doing exchanges\_shadow\_index

DRG-13600: Syntax error in the result set descriptor at string

Cause: The result set descriptor has a syntax error

Action: check the syntax of the result set descriptor

DRG-13601: Syntax error in the order attribute

Cause: The order attibute has a syntax error

Action: check the syntax of the order attibute

DRG-13602: Number parsing error in string

Cause: The number string is malformed

Action: check the syntax of the number string

DRG-13603: To many sort keys

Cause: Too many sort keys are specified

Action: reduce the number of sort keys

DRG-13604: To many items to select

Cause: Too many select items are specified

Action: reduce the number of select items

DRG-13605: Too many group tags

Cause: Too many group tags are specified

Action: reduce the number of group tags

DRG-13606: start\_hit\_num is not specified or out of valid range number..number

Cause: start\_hit\_num is not specified or out of valid range

Action: set a correct start\_hit\_num value

DRG-13607: end\_hit\_num is not specified or out of valid range number..number

Cause: end\_hit\_num is not specified or out of valid range

Action: set a correct end\_hit\_num value

DRG-13608: Temporary lob not created for ctx\_query.result\_set\_document

Cause: Temporary lob is not allocated for ctx\_query.result\_set\_document

Action: Create a temporary lob for ctx\_query.result\_set\_document

DRG-13609: Result set Interface should only have group mvdata element in absence of a query

Cause: No query is specified and result set descriptor has invalid elements

Action: either specify query or change result set descriptor

DRG-13610: Missing group\_values in the result set interface

Cause: MVDATA group values not specified in RSI

Action: add group\_values element for group counting

DRG-13611: Missing value id for MVDATA group counting in the result set interface

Cause: MVDATA group values not specified in RSI

Action: add value id element for group counting

DRG-13612: Missing path element in the result set interface

Cause: Path element not specified for the ctx\_tree element

Action: add path element for the ctx\_tree element

DRG-13613: Missing index name

Cause: index name not specified in the API

Action: specify an index name

DRG-13614: result\_set\_inteface not supported with security policy

Cause: result set interface not supported with security policies

Action: s: cannot use result set interface on table with security policy

DRG-13700: Syntax error in the Extraction Rule Descriptor

Cause: The Extraction Rule descriptor has a syntax error

Action: check the syntax of the Extraction rule descriptor

DRG-13701: Invalid rule\_id

Cause: rule\_id is NULL or rule\_id <= 0

Action: rule\_id must be number > 0

DRG-13702: Rule not found

Cause: No rule for given rule\_id

Action: Specify a valid rule\_id

DRG-13703: Invalid Type Specified: string

Cause: An invalid entity type was specified

Action: Specify a valid entity type

DRG-13704: Invalid Entity Type List

Cause: An invalid entity type list was specified

Action: Check format and types on entity type list

DRG-13705: Must use an Extract Policy

Cause: Using a non-extraction policy

Action: Use a policy created with ctx\_entity.create\_extract\_policy

DRG-13706: Cannot use Entity Extraction Policy here

Cause: Using an entity extraction policy

Action: Use a policy created with ctx\_ddl.create\_policy

DRG-13707: Rule Engine Loading Failed

Cause: A user rule has an error

Action: Fix the user rule with the error

DRG-13708: Dictionary Loading Failed

Cause: The user dictionary has an error

Action: Fix the user dictionary

DRG-13709: Unsupported Language Specified: string

Cause: Unsupported Language Specified

Action: Specify a supported language

DRG-13710: Syntax Error in Dictionary

Cause: Syntax error in dictionary

Action: Correct syntax error in dictionary

DRG-13711: Stop Entity Not Found

Cause: Tried to remove a non-existent stop entity

Action: Cannot remove non-existent stop entity

DRG-13712: User Dictionary already loaded

Cause: Tried to load a 2nd user dictionary to a policy

Action: Drop the dictionary, and then load

DRG-13713: No User Dictionary loaded

Cause: No user dictionary loaded for this policy

Action: Cannot drop non-existent dictionary

DRG-13714: Duplicate Stop Entity

Cause: Trying to load a duplicate uncompiled stop entity

Action: Stop entity is already present

DRG-13715: Null name and type for Stop entity

Cause: Trying to load a stop entity with null name and type

Action: Stop entity must have at least one parameter non-null

DRG-13716: Entity Extraction not enabled

Cause: Haven't loaded correct event

Action: Must load correct event and level

DRG-13717: Null entry or alternate form in user dict

Cause: A entry or alternate form has null value

Action: Entries or alternate forms must be non-null

DRG-13718: No entity type given in user dict

Cause: An entry was not given an entity type

Action: All entries must have an entity type

DRG-13719: File and Drop are mutually exclusive

Cause: Tried to run ctxload with file and drop

Action: file and drop are mutually exclusive

DRG-13720: Stop entity already marked for deletion

Cause: Tried to re-drop a stop entity

Action: Only drop this stop entity once

DRG-13721: Duplicate Type on Typelist

Cause: Duplicate type on typelist

Action: Typelist must be unique

DRG-13722: Invalid Backreference

Cause: Backreference not between 1 and 10

Action: Backreferences must be between 1 and 10

DRG-13723: Invalid Attribute: string

Cause: Unsupported Attribute

Action: Follow correct syntax for rule or dictionary

DRG-13724: Invalid Attribute Value: string

Cause: Unsupported attribute value

Action: Follow correct syntax for rule or dictionary

DRG-13725: Type Name Too Long

Cause: Type name more than 30 bytes

Action: Type must be less than 30 bytes

DRG-13726: Invalid Tag: string

Cause: Unsupported Tag

Action: Follow correct syntax for rule or dictionary

DRG-13727: Missing Tag: string

Cause: Missing Necessary Tag

Action: Add tag for rule or dictionary

DRG-13728: Missing Attribute: string

Cause: Missing Necessary Attribute

Action: Add attribute for rule or dictionary

DRG-13800: MVDATA section string does not exist

Cause: The given MVDATA section name does not exist in USER\_SECTIONS

Action: Rewrite query with valid MVDATA section name

DRG-13801: literal is not compatible with the data type of the MVDATA section

Cause: The given literal is not compatible with the data type of the specified MVDATA section.

Action: Rewrite query with a compatible literal

DRG-13802: MVDATA operand not compatible with the mvdata section string

Cause: failed to convert data

Action: check the format of the data

DRG-13803: Illegal MVDATA value

Cause: failed to convert data

Action: check the format of the data

DRG-13804: ctx\_tree.register\_index() not run for index string and mvdata section string

Cause: failed to create data

Action: create the data (trees) first

DRG-13805: Invalid character in node name string

Cause: failed to create data

Action: check the format of the data

DRG-13806: Duplicate path 'string' in CTX\_TREE.ADD\_NODE()

Cause: The path specified in ctx\_tree.add\_node() adds the node with the same name in the same tree at the same level

Action: change path

DRG-13807: Node string does not exist or is deleted

Cause: failed to lookup input node

Action: check if the path exists

DRG-13808: Empty path passed into string

Cause: path is empty

Action: pass in a non-empty and valid path

DRG-13809: Index with MVDATA sections must have big\_io turned on

Cause: Big\_io option not specified for MVDATA index

Action: turn on big\_io for the index

DRG-13810: Index with support\_ctx\_tree must have atleast one MVDATA section

Cause: MVDATA section not specified for ctx\_tree usage

Action: add one MVDATA section for the index

DRG-13811: Invalid path 'string' in CTX\_TREE.ADD\_NODE()

Cause: The path specified in ctx\_tree.add\_node() is invalid.

Action: change path

DRG-13900: Auto\_Optimize Process is already started

Cause: Auto\_Optimize Process is already started

Action: Can't start auto\_optimize when it's already running

DRG-13901: Index must have stage\_itab

Cause: Auto\_Optimize works on indexes with stage\_itab

Action: Use an index with stage\_itab for auto\_optimize

DRG-13902: Index/Partition already added to auto\_optimize list

Cause: Index/Partition already added to auto\_optimize list

Action: Can't add index/partition to list twice

DRG-50000: requested size larger than pagesize

Cause: The requested memoery size is larger than page size,

Action: Contact support

DRG-50100: CORE LSF error: string

Cause: detect a CORE LSF error

Action: look up the core error and take appropriate action

DRG-50101: CORE LEM error: string

Cause: detect a CORE LEM error while reading the error stack

Action: Contact support

DRG-50200: Third-party filter internal error

Cause: Third-party filter could not filter this document because of an internal error.

Action: Contact Oracle Support.

DRG-50300: error sending message from server to client

Cause: internal database error or internal Text error

Action: Call customer support

DRG-50301: server error reading request queue

Cause: database error or internal Text error

Action: Call customer support

DRG-50302: server error reading OOB break queue; cannot detect interrupts

Cause: database error or internal Text error

Action: Call customer support

DRG-50303: error in bufout

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50304: error in execute()

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50305: getcmd() called when one of the queue names is NULL

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50400: maximum number of fuzzy match candidates exceeded: string

Cause: Internal error, probably result of large number of indexed words

Action: Contact Oracle support

DRG-50401: failed to retrieve fuzzy match candidates from db: string

Cause: Internal error

Action: Contact Oracle support

DRG-50402: Index validation failed for one or more tokens

Cause: Index validation generated an error for one or more tokens

Action: Check the ctx log for the detailed errors

DRG-50403: Invalid MVDATA entries exist in the index

Cause: Index validation generated an error for one or more tokens

Action: Check the ctx log for the detailed errors

DRG-50500: only RULE\_CLASSIFIER is accepted in this API

Cause: you specified an illegal classifier

Action: use RULE\_CLASSIFIER

DRG-50501: classifier preference not specified

Cause: the classifier preference is not specified

Action: specify a classifier preference

DRG-50502: cannot use RULE\_CLASSIFIER in this API

Cause: you specified RULE\_CLASSIFIER

Action: use a different classifier

DRG-50503: unsupported classification method

Cause: you spcified an unsupported classification method

Action: use a different classifier

DRG-50504: invalid column datatype for string table

Cause: the column datatype is invalid

Action: specify a different datatype

DRG-50600: assertion failed

Cause: An internal check-condition has been violated

Action: Contact Oracle support for assistance

DRG-50601: fatal error

Cause: A fatal error has occurred

Action: Contact Oracle support for assistance

DRG-50603: unrecognized operation code string

Cause: Bad operation code was encountered (reached switch default:)

Action: check.h files versions

DRG-50607: failed to obtain column info for cid string

Cause: internal error, probably a bug

Action: call customer support

DRG-50608: unexpected end of data

Cause: internal error, probably a bug

Action: call customer support

DRG-50609: pipe internal error

Cause: internal error, probably a bug

Action: call customer support

DRG-50610: internal error: string

Cause: internal error, probably a bug

Action: call customer support

DRG-50611: Third party lexer internal error: string

Cause: internal error from inxight lexer

Action: call customer support

DRG-50612: internal error: you need to call bind first for this insertion mode

Cause: internal error

Action: call customer support

DRG-50613: internal error: model type is not supported in drctrwpf

Cause: internal error

Action: call customer support

DRG-50614: library loading error in string

Cause: internal error

Action: call customer support

DRG-50615: Third party lexer timed out

Cause: Third-party auto lexer could not complete tokenization because the lexer timed out.

Action: Increase the value of the TIMEOUT attribute of the auto\_lexer and reindex the document. If TIMEOUT is set to 0 and the lexer still hangs context Oracle Support.

DRG-50616: Stop-Optimize List not found

Cause: internal error

Action: calll customer support

DRG-50700: unknown command (args=queue, command)

Cause: this is an internal error

Action: Contact Oracle support to report a bug

DRG-50701: error in listener.get\_cmd()

Cause: this is an internal error

Action: Contact Oracle support to report a bug

DRG-50702: error in drtlsleep()

Cause: this is an internal error in a testing function

Action: Contact Oracle Support

DRG-50703: listener startup error

Cause: this is an internal error

Action: Contact Oracle support to report a bug

DRG-50704: Net8 listener is not running or cannot start external procedures

Cause: Oracle Text needs to call external code to complete your request, and could not start the extproc agent process.

Action: Start listener if it is configured for external procedures and is not running. If your listener is running, configure it for starting external procedures and restart it. Consult Oracle documentation for details.

DRG-50800: failed to open cursor

Cause: Too many cursors open for internal queries

Action: implement cursor cleanup routine

DRG-50801: failed to parse cursor

Cause: parse error on an internal query

Action: check versions of code

DRG-50802: failed to bind input

Cause: bind error on an internal query

Action: check versions of code

DRG-50803: failed to define output

Cause: define error on an internal query

Action: check versions of code

DRG-50804: failed to exec cursor

Cause: exec error on an internal query

Action: debug code

DRG-50805: failed to close cursor

Cause: cursor close error on an internal query

Action: check versions of code

DRG-50806: failed to rollback

Cause: transaction rollback error

Action: contact support

DRG-50807: failed to commit

Cause: internal error

Action: contact support

DRG-50850: string

Cause: This is an oracle error

Action: See RDBMS documentation

DRG-50851: SQL execute failed

Cause: failed to execute a sql statement

Action: please report this as a bug

DRG-50852: failed to turn SQL trace on

Cause: internal error,

Action: Please contact Oracle support

DRG-50853: fetch error

Cause: fetch error on an internal query

Action: check versions of code

DRG-50855: logoff fail

Cause: Fail to logoff from the database

Action: check versions of code

DRG-50857: oracle error in string

Cause: this is an informational message

Action: See error

DRG-50858: OCI error: string

Cause: a generic OCI error occurred

Action: Please contact Oracle support

DRG-50859: failed to allocate statement handle

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50860: failed to prepare statement

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50861: failed to obtain type descriptor

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50862: failed to create new Oracle object

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50863: string assignment failed

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50864: number assignment failed

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50865: failed to append to collection

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50866: failed to resize string

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50867: failed to free Oracle object

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50868: failed to free statement handle

Cause: This is an internal error

Action: Contact Oracle Support

DRG-50900: text query parser error on line string, column string

Cause: bad query

Action: fix query

DRG-50901: text query parser syntax error on line string, column string

Cause: bad query

Action: fix query

DRG-50902: unexpected character string

Cause: bad query

Action: fix query

DRG-50903: invalid weight string

Cause: invalid weight

Action: fix query

DRG-50904: weight string outside valid range 0.1 to 10.0

Cause: invalid weight

Action: fix query

DRG-50905: invalid score threshold string

Cause: invalid score threshold

Action: fix query

DRG-50906: score threshold string is not an integer

Cause: invalid score threshold

Action: fix query

DRG-50907: score threshold string outside valid range 1 to 100

Cause: invalid score threshold

Action: fix query

DRG-50908: invalid maximum number of documents string

Cause: invalid maximum number of documents

Action: fix query

DRG-50909: maximum number of documents string is not an integer

Cause: invalid maximum number of documents

Action: fix query

DRG-50910: max documents requested string outside valid range 1 to 65535

Cause: invalid maximum number of documents

Action: fix query

DRG-50911: invalid first document number string

Cause: invalid first document number

Action: fix query

DRG-50912: first document number string is not an integer

Cause: invalid first document number

Action: fix query

DRG-50913: first document requested string is not a positive number

Cause: invalid first document number

Action: fix query

DRG-50914: invalid last document number string

Cause: invalid last document number

Action: fix query

DRG-50915: last document number string is not an integer

Cause: invalid last document number

Action: fix query

DRG-50916: last document string is less than first document

Cause: invalid last document number

Action: fix query

DRG-50917: escape on at end of text query string

Cause: unbalanced escape characters

Action: turn escape off

DRG-50918: mismatched close escape character

Cause: no matching open escape character for close escape

Action: match open and close escapes

DRG-50919: NEAR operand not a phrase, equivalence or another NEAR expression

Cause: invalid operand type for NEAR operator

Action: correct operand type

DRG-50920: part of phrase not itself a phrase or equivalence

Cause: invalid type of expression which is part of phrase

Action: fix query

DRG-50921: EQUIV operand not a word or another EQUIV expression

Cause: invalid operand type for EQUIV operator

Action: correct operand type

DRG-50922: PL/SQL execution failed for string

Cause: PL/SQL function may not exist or is returning bad value

Action: PL/SQL may not exist or is returning bad value

DRG-50923: could not rewrite PL/SQL for execution

Cause: parser internal

Action: call support

DRG-50924: PL/SQL inside PL/SQL not supported

Cause: PL/SQL function call returned another PL/SQL call

Action: remove recursive PL/SQL

DRG-50925: could not parse return value of PL/SQL

Cause: string returned by PL/SQL function could not be parsed

Action: fix PL/SQL function being called

DRG-50926: invalid text query string

Cause: query string empty or made up of invalid characters

Action: fix query

DRG-50927: parser failed on line string on column string

Cause: bug

Action: call support

DRG-50928: reserved failure on line string on column string

Cause: bug

Action: call support

DRG-50929: parser internal on line string on column string

Cause: bug

Action: call support

DRG-50930: parser memory failure on line string on column string

Cause: memory allocation or freeing error

Action: call support

DRG-50931: parser not opened

Cause: bug

Action: call support

DRG-50932: parser preference initialization failed

Cause: bug

Action: call support

DRG-50933: parser hash insert failure

Cause: bug

Action: call support

DRG-50934: parser hash create failure

Cause: bug

Action: call support

DRG-50935: parser component failure

Cause: bug

Action: look for other errors

DRG-50936: query word string is too complex for index

Cause: bug

Action: look for other errors

DRG-50937: query too complex

Cause: query is too complex for our query evaluator

Action: make query smaller

DRG-50938: parser already bound

Cause: internal coding mistake

Action: call support

DRG-50939: parser not set

Cause: bug

Action: call support

DRG-50940: parser not parsed

Cause: bug

Action: call support

DRG-50941: PL/SQL function string cannot be executed

Cause: PL/SQL function may not exist or cannot be executed by user

Action: rewrite PL/SQL function specified in query

DRG-50942: errors: stringstring

Cause: PL/SQL function encountered error -- this is the error message

Action: See error message

DRG-50943: query token too long on line string on column string

Cause: A query token is longer than 256 bytes

Action: Rewrite query

DRG-50944: NEAR operator not supported for theme index

Cause: NEAR operator used in theme index query

Action: Rewrite query without NEAR operator

DRG-50945: Illegal phrase in query for theme index

Cause: Phrase incorrectly defined in theme index query

Action: Rewrite query

DRG-50946: Invalid unary operator for theme index

Cause: Stemming, fuzzy match and soundex not allowed for theme index

Action: Rewrite query

DRG-50947: ABOUT clause not allowed without a theme index

Cause: The query contains an ABOUT clause, but there is no theme index to support it

Action: Rewrite query

DRG-50948: ABOUT clause required in the absence of a text index

Cause: There is no text index, but the query does not contain any about clause. With only a theme index present, each query term must belong to an ABOUT clause

Action: Rewrite query

DRG-50949: too many SQEs

Cause: Too many SQEs to expand

Action: Rewrite query or SQE

DRG-50950: circular SQE found

Cause: Circular SQE reference is found.

Action: Rewrite query or SQE

DRG-50951: Unable to resolve element name for attribute string

Cause: XPATH expression such as A/\*/@B or A//@B is not supported.

Action: Rewrite query

DRG-50952: Section is not PATH section group

Cause: XPATH expression has section which is not created using PATH section group.

Action: Rewrite query not to use XPATH expression or create the index with PATH section group

DRG-50953: Unable to determine section name

Cause: XPATH expression should not end with. or \*

Action: Rewrite the path expression not to use. or \* at the end

DRG-50954: Theme index is required for CTXCAT about queries

Cause: There is no theme index, but the catsearch query contains about clause. You must create a theme index before using ABOUT query against CTXCAT index

Action: create theme index

DRG-50955: Missing comma in transform clause string

Cause: A transform clause in a query template is missing a comma

Action: Add the comma in the appropriate position

DRG-50956: Theme index is required for THEMES transform queries

Cause: There is no theme index, but the operator TRANSFORM is used with THEMES as its parameter. You must create a theme index before using THEMES in TRASNFORM operator.

Action: create theme index

DRG-50957: Missing \<textquery> element in query template string

Cause: The \<textquery> tag is missing or misspelled in a query template

Action: Correct the missing tag

DRG-50958: Missing quote in transform clause string

Cause: A transform clause in a query template is missing a quote

Action: Add the quote in the appropriate position

DRG-50959: Query length exceeds string bytes

Cause: the query length exceeds the maximum allowed length

Action: reduce the length of the query

DRG-50960: Mild not operand not a term or phrase

Cause: invalid operand type for MNOT operator

Action: correct operand type

DRG-50961: Missing string for string clause

Cause: the specified tag is missing from the specified complex query clause

Action: Add missing clause

DRG-50962: Query operators are not allowed in transform input string

Cause: You specified an operator (such as wildcard) in the input string for the transform operator

Action: Remove or escape the query operator

DRG-51002: unexpected component failure

Cause: Internal error

Action: Contact Oracle support

DRG-51017: unable to open storage buffer for fuzzy match candidates

Cause: Internal error, probably insufficient memory

Action: Contact Oracle support

DRG-51019: unable to open or illegal format for fuzzy match data file: string

Cause: Unable to open OS file containing fuzzy matching information or the file was not of the correct format

Action: Consult the documentation for correct location of the fuzzy match information files and check for file damage

DRG-51020: out of memory in fuzzy matcher

Cause: Cannot allocate more memory

Action: Contact your system adminstrator

DRG-51021: undefined error in fuzzy matcher

Cause: Internal error

Action: Contact Oracle support

DRG-51022: undefined error in stemmer

Cause: Internal error

Action: Contact Oracle support

DRG-51023: stemmer file cannot be opened

Cause: Unable to open OS file containing stemmer lexicon, or the file contents were not correct

Action: Consult documentation for for correct location of the stemmer lexicons and check for file damage

DRG-51024: out of memory in stemmer

Cause: Cannot allocate more memory

Action: Contact your system administrator

DRG-51025: an invalid character was passed to the stemmer

Cause: Invalid character in word input to the stemmer

Action: Remove invalid character from word to be stemmed

DRG-51028: unexpected error in fuzzy match expansion: %(1)

Cause: Internal error

Action: Contact Oracle support

DRG-51029: unexpected error in stemmer expansion: %(1)

Cause: Internal error

Action: Contact Oracle support

DRG-51030: wildcard query expansion resulted in too many terms

Cause: User error

Action: Make wildcard query narrower

DRG-51100: invalid program argument index

Cause: This is an internal error

Action: Contact Oracle Support to report a bug

DRG-51101: argument processing callback failed

Cause: this is an internal error

Action: Contact Oracle support to report a bug

DRG-51200: open keymap failed for index id = string

Cause: Failed to initialize the keymap for the column id specified.

Action: Check index ID. Contact support if caused by internal errors

DRG-51201: failed to perform DDL operation: database object string

Cause: Textkey mapping service failed on DDL operation

Action: Check Oracle error and take corrective action

DRG-51202: invalid key mapping operation mode: string

Cause: invalid keymap mode value found. This is an internal error

Action: Contact Oracle support

DRG-51203: found doc ids without mappings during get maps

Cause: found doc ids without mappings during get mapping by doc ids, the index data and keymap service are out of synch.

Action: Contact Oracle support

DRG-51300: error getting dml Queue lock

Cause: a server must have hung while processing the dml Queue, leaving it locked

Action: Contact Oracle support

DRG-51301: error releasing dml Queue lock

Cause: internal database error, or perhaps someone dropped the lock while we were using it

Action: Contact Oracle support

DRG-51311: DML lock handle previously allocated

Cause: internal error

Action: Contact Oracle support

DRG-51312: DML lock internal error string

Cause: internal error

Action: Contact Oracle support

DRG-51313: timeout while waiting for lock

Cause: most likely an internal error

Action: Contact Oracle support

DRG-51314: index is not empty

Cause: you attempted to invoke populate\_pending against an index which already has or has had indexed documents.

Action: populate pending manually, or recreate the index NOPOPULATE

DRG-51403: New index name not provided by kernel

Cause: this is an internal error

Action: Contact Oracle support

DRG-51801: failed to seek in file: %(1)

Cause: this is an internal error

Action: Contact Oracle support

DRG-51802: failed to read from file: %(1)

Cause: this is an internal error

Action: Contact Oracle support

DRG-51803: failed to open file: %(1)

Cause: this is an internal error

Action: Contact Oracle support

DRG-51804: failed to write to file: %(1)

Cause: this is an internal error

Action: Contact Oracle support

DRG-52100: string returned internal error code string

Cause: this is an internal error

Action: Contact Oracle support

DRG-52101: an invalid session handle was passed to Oracle Text

Cause: this is an internal error

Action: Contact Oracle support

DRG-52102: an invalid transaction handle was passed to Oracle Text

Cause: this is an internal error

Action: Contact Oracle support

DRG-52103: the Oracle Text environment could not reset

Cause: this is an internal error

Action: Contact Oracle support

DRG-52104: the Oracle Text environment could not initialize

Cause: this is an internal error

Action: Contact Oracle support

DRG-52105: no delete function found

Cause: this is an internal error

Action: Contact Oracle support

DRG-52106: Oracle Text service results could not be committed

Cause: this is an internal error

Action: Contact Oracle support

DRG-52107: ctxkbtc internal error

Cause: this is an internal error

Action: Contact Oracle support

DRG-52108: failed to delete knowledge base user extension

Cause: this is an internal error

Action: check file permissions or contact Oracle support

DRG-52109: error in reading thesaurus

Cause: this is an internal error

Action: Contact Oracle support

DRG-52110: error in writing extended knowledge base

Cause: this is an internal error

Action: Contact Oracle support

DRG-52111: error in knowledge base cache

Cause: this is an internal error

Action: Contact Oracle support

DRG-52112: improper Chinese string string of length number

Cause: this is an internal error

Action: None

DRG-52113: improper Japanese string string of length number

Cause: this is an internal error

Action: None

DRG-52200: invalid state during export

Cause: this is an internal error

Action: Contact Oracle support

DRG-52201: imcompatible Oracle Text versions

Cause: attempting to import an incompatible version of Oracle Text data

Action: make sure source and target Oracle Text versions are compatible

DRG-52202: invalid class name: string

Cause: the specified class name is not valid

Action: Contact Oracle Support

DRG-52203: invalid object name: string

Cause: the specified object name is not valid

Action: Contact Oracle Support

DRG-52204: error while registering index

Cause: this is an internal error

Action: Contact Oracle support

DRG-52205: class string and object string already exists for this index

Cause: duplicate entry of class and object

Action: Contact Oracle support

DRG-52206: error while registering index object

Cause: this is an internal error

Action: Contact Oracle support

DRG-52207: the specified attribute does not exist: string

Cause: This is an internal error

Action: Contact Oracle Support

DRG-52208: the specified attribute already exist: string

Cause: This is an internal error

Action: Contact Oracle Support

DRG-52210: error while registering value for attribute: string

Cause: This is an internal error

Action: Contact Oracle Support

DRG-52211: error while registering partition

Cause: this is an internal error

Action: Contact Oracle support

DRG-52212: error while registering cdi columns

Cause: this is an internal error

Action: Contact Oracle support

DRG-52300: Index string.string does not exist

Cause: The given index does not exist for the current user

Action: Give a valid index name

DRG-52301: Query Stats is already enabled for this index

Cause: attempting to enable the query stats for an index for which it is already enabled

Action: None. No need to enable again

DRG-52302: Query Stats is not enabled for this index

Cause: attempting to disable the query stats for an index for which it is not enabled

Action: None. No need to disable if it is not already enabled

DRG-52304: This operation requires Query Stats to be enabled for the index

Cause: attempting to do an operation which required query stats option for the index to be enabled

Action: Enable query stats option for the index using ctx\_output.enable\_query\_stats()

DRG-52305: Unknown value, string, passed in to stat\_type

Cause: An invalid value is passed in to the parameter stat\_type

Action: Give a valid value