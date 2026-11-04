---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/UTL_MAIL.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 273 UTL\_MAIL

The `UTL_MAIL` package is a utility for managing email which includes commonly used email features, such as attachments, CC, and BCC.

This chapter contains the following topics:

### 273.1 UTL\_MAIL Security Model

`UTL_MAIL` is not installed by default because of the `SMTP_OUT_SERVER` configuration requirement and the security exposure this involves. In installing `UTL_MAIL`, you should take steps to prevent the port defined by `SMTP_OUT_SERVER` being swamped by data transmissions`.`

This package is now an invoker's rights package and the invoking user will need the connect privilege granted in the access control list assigned to the remote network host to which he wants to connect.

Note:

For more information about managing fine-grained access, see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG-GUID-B7DB516A-3245-417F-BB89-8E8212A97542).

### 273.2 UTL\_MAIL Operational Notes

You must both install `UTL_MAIL` and define the `SMTP_OUT_SERVER.`

- To install UTL\_MAIL:
	```
	sqlplus sys/<pwd>
	SQL> @$ORACLE_HOME/rdbms/admin/utlmail.sql
	SQL> @$ORACLE_HOME/rdbms/admin/prvtmail.plb
	```
- You define the `SMTP_OUT_SERVER` parameter in the `init`.`ora` `rdbms` initialization file. However, if `SMTP_OUT_SERVER` is not defined, this invokes a default of `DB_DOMAIN` which is guaranteed to be defined to perform appropriately.

### 273.3 UTL\_MAIL Rules and Limits

Use `UTL_MAIL` only within the context of the ASCII (American Standard Code for Information Interchange) and EBCDIC (Extended Binary-Coded Decimal Interchange Code) codes.

### 273.4 Summary of UTL\_MAIL Subprograms

This table lists the `UTL_MAIL` subprograms and briefly describes them.

Table 273-1 UTL\_MAIL Package Subprograms

| Subprogram | Description |
| --- | --- |
| SEND Procedure | Packages an email message into the appropriate format, locates SMTP information, and delivers the message to the SMTP server for forwarding to the recipients |
| SEND\_ATTACH\_RAW Procedure | Represents the `SEND` Procedure overloaded for `RAW` attachments |
| SEND\_ATTACH\_VARCHAR2 Procedure | Represents the `SEND` Procedure overloaded for `VARCHAR2` attachments |

#### 273.4.1 SEND Procedure

This procedure packages an email message into the appropriate format, locates SMTP information, and delivers the message to the SMTP server for forwarding to the recipients.

It hides the SMTP API and exposes a one-line email facility for ease of use.

Syntax

```
UTL_MAIL.SEND (
   sender      IN    VARCHAR2 CHARACTER SET ANY_CS,
   recipients  IN    VARCHAR2 CHARACTER SET ANY_CS,
   cc          IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   bcc         IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   subject     IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   message     IN    VARCHAR2 CHARACTER SET ANY_CS,
   mime_type   IN    VARCHAR2 DEFAULT 'text/plain; charset=us-ascii',
   priority    IN    PLS_INTEGER DEFAULT 3,
   replyto     IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL);
```

Parameters

Table 273-2 SEND Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sender` | Email address of the sender |
| `recipients` | Email addresses of the recipient(s), separated by commas |
| `cc` | Email addresses of the CC recipient(s), separated by commas, default is `NULL` |
| `bcc` | Email addresses of the BCC recipient(s), separated by commas, default is `NULL` |
| `subject` | String to be included as email subject string, default is `NULL` |
| `message` | Text message body |
| `mime_type` | Mime type of the message, default is `'text/plain; charset=us-ascii'` |
| `priority` | Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. |
| `replyto` | Defines to whom the reply email is to be sent |

#### 273.4.2 SEND\_ATTACH\_RAW Procedure

This procedure is the `SEND` Procedure overloaded for `RAW` attachments.

Syntax

```
UTL_MAIL.SEND_ATTACH_RAW (
   sender           IN    VARCHAR2 CHARACTER SET ANY_CS,
   recipients       IN    VARCHAR2 CHARACTER SET ANY_CS,
   cc               IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   bcc              IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   subject          IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   message          IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   mime_type        IN    VARCHAR2 DEFAULT CHARACTER SET ANY_CS
                              DEFAULT 'text/plain; charset=us-ascii',
   priority         IN    PLS_INTEGER DEFAULT 3,
   attachment       IN    RAW,
   att_inline       IN    BOOLEAN DEFAULT TRUE,
   att_mime_type    IN    VARCHAR2 CHARACTER SET ANY_CS 
                                           DEFAULT 'text/plain; charset=us-ascii',
   att_filename     IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   replyto          IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL);
```

Parameters

Table 273-3 SEND\_ATTACH\_RAW Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sender` | Email address of the sender |
| `recipients` | Email addresses of the recipient(s), separated by commas |
| `cc` | Email addresses of the CC recipient(s), separated by commas, default is `NULL` |
| `bcc` | Email addresses of the BCC recipient(s), separated by commas, default is `NULL` |
| `subject` | String to be included as email subject string, default is `NULL` |
| `message` | Text message body |
| `mime_type` | Mime type of the message, default is `'text/plain; charset=us-ascii'` |
| `priority` | Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. |
| `attachment` | `RAW` attachment |
| `att_inline` | Specifies whether the attachment is viewable inline with the message body, default is `TRUE` |
| `att_mime_type` | Mime type of the attachment, default is 'application/octet' |
| `att_filename` | String specifying a filename containing the attachment, default is `NULL` |
| `replyto` | Defines to whom the reply email is to be sent |

#### 273.4.3 SEND\_ATTACH\_VARCHAR2 Procedure

This procedure is the `SEND` Procedure overloaded for `VARCHAR2` attachments.

Syntax

```
UTL_MAIL.SEND_ATTACH_VARCHAR2 (
   sender            IN    VARCHAR2 CHARACTER SET ANY_CS,
   recipients        IN    VARCHAR2 CHARACTER SET ANY_CS,
   cc                IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   bcc               IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   subject           IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   message           IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
   mime_type         IN    VARCHAR2 CHARACTER SET ANY_CS 
                                           DEFAULT 'text/plain; charset=us-ascii',
   priority          IN    PLS_INTEGER DEFAULT 3,
   attachment        IN    VARCHAR2 CHARACTER SET ANY_CS, ,
   att_inline        IN    BOOLEAN DEFAULT TRUE,
   att_mime_type     IN    VARCHAR2 CHARACTER SET ANY_CS 
                                           DEFAULT 'text/plain; charset=us-ascii,
   att_filename      IN    VARCHAR2CHARACTER SET ANY_CS DEFAULT NULL,
   replyto           IN    VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL);
```

Parameters

Table 273-4 SEND\_ATTACH\_VARCHAR2 Procedure Parameters

| Parameter | Description |
| --- | --- |
| `sender` | Email address of the sender |
| `recipients` | Email addresses of the recipient(s), separated by commas |
| `cc` | Email addresses of the CC recipient(s), separated by commas, default is `NULL` |
| `bcc` | Email addresses of the BCC recipient(s), separated by commas, default is `NULL` |
| `subject` | String to be included as email subject string, default is `NULL` |
| `message` | Text message body |
| `mime_type` | Mime type of the message, default is `'text/plain; charset=us-ascii` |
| `priority` | Message priority, which maps to the X-priority field. 1 is the highest priority and 5 the lowest. The default is 3. |
| `attachment` | Text attachment |
| `att_inline` | Specifies whether the attachment is inline, default `TRUE` |
| `att_mime_type` | Mime type of the attachment, default is `'text/plain; charset=us-ascii'` |
| `att_filename` | String specifying a filename containing the attachment, default is `NULL` |
| `replyto` | Defines to whom the reply email is to be sent |