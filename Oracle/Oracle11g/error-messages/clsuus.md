---
title: CLSU-00100 to CLSU-00912
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/clsuus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 62 CLSU-00100 to CLSU-00912

CLSU-00100: Operating System function: string failed with error data: string

Cause: A call to an Operating System dependent service or function returned an error indication. The message includes the name of the function and the returned error data. The latter varies by platform but typically is numeric; on most platforms it is the value of C "errno" after the failing call.

Action: This error normally is accompanied by other (higher-level) messages describing the operation that is affected by the failure. It may also include one or more of messages 101, 103, and 104 providing additional error details. All of the messages should be examined to assess the error, which may have a very ordinary cause and correction, such as an input file failing to open because the supplied name was misspelled.

CLSU-00101: Operating System error message: string

Cause: This message accompanies message 100 above when the Operating System dependent error data can be converted into a text message. On most Oracle platforms the message is a text representation of the C "errno" value reported in message 100.

Action: See message 100.

CLSU-00102: Operating System interface detected an error

Cause: This message is issued instead of messages 100-101 when a "logical" error condition (rather than failure of an Operating System function call) is detected at an Operating System specific interface. The error condition is further described by accompanying message(s), including 103 and 104.

Action: This error normally is accompanied by other (higher-level) messages describing the operation that is affected by the failure. In most cases it will also include messages 103 and 104, providing additional details about the error. All of the messages should be examined to assess the error, which may have a very ordinary cause and correction, such as a missing required environment variable.

CLSU-00103: error location: string

Cause: This message accompanies message 100, 102, or 105 and identifies a location in Oracle program code that encountered the error.

Action: See message 100, 102, or 105. This information normally is useful only when reporting the error condition to Oracle as a potential code bug.

CLSU-00104: additional error information: string

Cause: This message accompanies message 100, 102, or 105 and supplies additional information related to the error condition. A single error may include multiple lines of additional information.

Action: See message 100, 102, or 105.

CLSU-00105: Operating System interface has reported an internal failure

Cause: This message indicates that an Operating System dependent interface within Oracle code has detected internal corruption or some other evidence of internal program failure.

Action: This message may be accompanied by other (higher-level) messages indicating the product operation that was affected by the failure. It may also be accompanied by either or both of messages 103 and 104. All situations reporting this condition should be referred to Oracle Support for resolution.

CLSU-00106: An improper Operating System error display was attempted

Cause: During processing of an error condition, an attempt was made to format/display Operating System dependent error data, but the error data structure was found to indicate "no error".

Action: This error should be reported to Oracle Support for resolution.

CLSU-00200: \*\*\*\* Error stack contains number records, newest first:

Cause: The collection of errors about to be presented contains this many following records.

Action: This and the following data should be reported to Oracle Support for resolution.

CLSU-00201: \*\*\*\* Error stack end \*\*\*\*

Cause: This marks the end of a collection of errors

Action: The preceding data should be reported to Oracle Support for resolution.

CLSU-00210: CLSUUS test msg 0

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00211: CLSUUS test msg 1:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00212: CLSUUS test msg 2:string 2:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00213: CLSUUS test msg 3:string 2:string 3:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00214: CLSUUS test msg 4:string 2:string 3:string 4:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00215: CLSUUS test msg 5:string 2:string 3:string 4:string 5:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00216: CLSUUS test msg 6:string 2:string 3:string 4:string 5:string 6:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00217: CLSUUS test msg 7:string 2:string 3:string 4:string 5:string 6:string 7:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00218: CLSUUS test msg 8:string 2:string 3:string 4:string 5:string 6:string 7:string 8:string

Cause: A message for testing, should never be seen in the field.

Action: Report to Oracle Support.

CLSU-00220: clsem FATAL exception: string

Cause: Something unrecoverable happened in CLSEM.

Action: Report to Oracle Support.

CLSU-00221: ERROR printed by clsecho: string

Cause: An error printed by clsecho

Action: Report to Oracle Support.

CLSU-00222: WARNING printed by clsecho: string

Cause: A warning

Action: Note the text

CLSU-00223: Info printed by clsecho: string

Cause: Information printed by clsecho

Action: Report to Oracle Support.

CLSU-00910: Named exception string string string string

Cause: Program raised an exception that does not have its own message

Action: Report to Oracle Support.

CLSU-00911: Signal string received

Cause: Program received on OS signal reported as an exception

Action: Report to Oracle Support

CLSU-00912: OSE: string string

Cause: An operating specific error was noticed

Action: Examine the message in context.