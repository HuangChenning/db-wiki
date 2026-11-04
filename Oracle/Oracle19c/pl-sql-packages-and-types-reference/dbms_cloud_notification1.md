---
title: DBMS_CLOUD_NOTIFICATION
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/dbms_cloud_notification1.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_CLOUD_NOTIFICATION` package allows you to send messages or the output of a SQL query to a provider.

### DBMS\_CLOUD\_NOTIFICATION Overview

This scenario describes setup and use of the `DBMS_CLOUD_NOTIFICATION` package.

The supported providers are: Email, Microsoft Teams, and Slack.

### Installing DBMS\_CLOUD Packages

The `DBMS_CLOUD` family of packages is not pre-installed or configured with Oracle database. You need to manually install the `DBMS_CLOUD` packages and also configure users or roles to use this package.

For information on installation and configuration with Oracle Database 19c, Release 19.30 and above, see [Using the DBMS\_CLOUD Family of Packages](https://docs.oracle.com/en/database/oracle/oracle-database/26/sutil/using-dbms_cloud-family-packages.html#SUTIL-GUID-0F94EA7F-1BD0-41BF-90FA-25F5B89DC87B).

For installing the `DBMS_CLOUD` packages and configuring users or roles for Oracle Database 19c, Releases prior to 19.30, see the MOS-NOTE with Doc ID [2748362.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=213651872530310&id=2748362.1&_afrWindowMode=0&_adf.ctrl-state=dz5ua14hn_4). Note that earlier releases provide limited `DBMS_CLOUD` functionality only.

### Summary of DBMS\_CLOUD\_NOTIFICATION Subprograms

This table summarizes the subprograms included in the package.

| Subprogram | Description |
| --- | --- |
| SEND\_DATA Procedure | Send SQL query output to a provider. |
| SEND\_MESSAGE Procedure | Send a text message to a provider. |

### SEND\_DATA Procedure

The `SEND_DATA` procedure sends the results of the specified query to a provider.

**Syntax**

```sql
DBMS_CLOUD_NOTIFICATION.SEND_DATA(
       provider           IN  VARCHAR2,
       credential_name    IN  VARCHAR2,
       query              IN  CLOB,
       params             IN  CLOB
 );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `provider` | Specifies the provider.  Valid values are: ' `email` ', ' `msteams` ', and ' `slack` '  This parameter is mandatory. |
| `credential_name` | The name of the credential object to access the provider.  For the email provider, the credential is the name of the credential of the SMTP approved sender that contains its username and password.  For the msteams provider, the credential is the name of the credential.  For the Slack provider, the credential's username must be `"SLACK_TOKEN"` and the `password` is the Slack Bot Token.  This parameter is mandatory. |
| `query` | Specifies the SQL query to run. Results are sent to the provider.  This parameter is mandatory. |
| `params` | Specifies specific parameters for the `provider` in JSON format.  For the provider type `email`, the valid parameters are:  - `sender`. This specifies the Email ID of the approved sender in a `String` value. - `smtp_host`. This specifies the SMTP host name in a `String` value. - `subject`. This specifies the subject of the email in a `String` value The maximum size is 100 characters. - `recipient`. This specifies the email IDs of recipients in a `String` value. Use a comma between email IDs when there are multiple recipients. - `to_cc`. This specifies the email IDs that are receiving a CC of the email. It is a `String` value. Use a comma between email IDs when there are multiple CC recipients. - `to_bcc`. This specifies the email IDs that are receiving a BCC of the email. It is a `String` value. Use a comma between email IDs when there are multiple BCC recipients. - `message`. This specifies the message text in a `String` value. - `type`. This specifies the output format in a `String` value as either CSV or JSON. - `title`. This specifies the title of the attachment of SQL output in a `String` value. The title should only contain letters, digits, underscores, hyphens, or dots as characters in its value due to it being used to generate a file name.  For the provider type `msteams`, the valid parameters are:  - `tenant`. This specifies the tenant ID in a `String` format. - `team`. This specifies the team ID in a `String` format. - `channel`. This specifies the channel ID in a `String` format. - `title`. This specifies the title of the file in a `String` format. The maximum size is 50 characters. - `type`. This specifies the output format in a `String` value. Valid values are CSV or JSON.  For the provider type `slack`, the valid parameters are:  - `channel`. This specifies the Channel ID in a `String` value. The Channel ID is a unique ID for a channel and is different from the channel name. In Slack, when you view channel details you can find the Channel ID on the "About" tab. - `type`. This specifies the output format in a `String` value. Valid values are CSV or JSON.  This parameter is mandatory. |

**Usage Notes**

- Use the procedure `DBMS_CLOUD.CREATE_CREDENTIAL` `(credential_name`, `username`, `password)` to create the credential object.
	See [CREATE\_CREDENTIAL Procedure](dbms_cloud.md) for more information.
- For the `email` provider, note the following:
	- The user requires an SMTP connection endpoint for the Email Delivery server to obtain `smtp_host`. The user also requires an SMTP approved sender and its credentials to authenticate with the Email Delivery server to obtain the `credential_name`. The SMTP connection must be configured and the SMTP credentials must be generated and approved.
		- The maximum message size supported when using `DBMS_CLOUD_NOTIFICATION.SEND_DATA` with the `email` provider is 32k bytes.
- For the `msteams` provider, the user requires the Microsoft Teams App and a bot configured in it. The app needs to be published to the org and installed after obtaining approval from the admin from the admin center. The user also requires access for `Files.ReadWrite.All` and `ChannelSettings.Read.All` permission for Graph API from their Azure Portal. To generate the required token, the user requires `bot_id` in the username and `bot_secret` in the password.
	The maximum file size supported when using `DBMS_CLOUD_NOTIFICATION.SEND_DATA` for Microsoft Teams is 4MB.
- For the `slack` provider, the `username` value can be any valid string and the `password` is the Slack bot token.

**Examples**

Send SQL output with the `email` provider:

```sql
BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(
    credential_name => 'EMAIL_CRED',
    username        => 'username',
    password        => 'password');
END;
/

BEGIN
   DBMS_CLOUD_NOTIFICATION.SEND_DATA(
        provider        => 'email',
        credential_name => 'EMAIL_CRED',
        query           => 'SELECT tablespace_name FROM dba_tablespaces',
        params          => json_object('recipient' value  'mark@oracle.com, suresh@oracle.com',
                                       'to_cc'  value 'nicole@oracle.com1, jordan@oracle.com',
                                       'to_bcc' value 'manisha@oracle.com',
                                       'subject' value 'Test subject',
                                       'type' value 'json',
                                       'title' value 'mytitle',
                                       'message' value 'This is the message',
                                       'smtp_host' value 'smtp.email.example.com',
                                       'sender'    value  'approver_sender@oracle.com' )
   );
   END;
/
```

Send SQL output with the `msteams` provider:

```sql
BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(credential_name => 'TEAMS_CRED',
        username        => 'bot_id',
        password        => 'bot_secret');
END;
/

BEGIN
     DBMS_CLOUD_NOTIFICATION.SEND_DATA(provider => 'msteams',
        credential_name => 'TEAMS_CRED',
        query           => 'SELECT tablespace_name FROM dba_tablespaces',
        params          => json_object('tenant'value '5b743bc******c0286',
                                       'team'value '0ae401*********5d2bd',
                                       'channel'value '19%3a94be023*****%40thread.tacv2',
                                       'title'value 'today',
                                       'type'value 'csv'));
END;
/
```

Send SQL output with the `slack` provider:

```sql
BEGIN
   DBMS_CLOUD.CREATE_CREDENTIAL(
     credential_name => 'SLACK_CRED',
     username        => 'SLACK_TOKEN',
     password        => 'password');
END;
/
BEGIN
  DBMS_CLOUD_NOTIFICATION.SEND_DATA(
      provider        => 'slack',
      credential_name => 'SLACK_CRED',
      query           => 'SELECT username, account_status, expiry_date FROM USER_USERS WHERE rownum < 5',
      params          => json_object('channel' value 'C0....08','type' value 'csv'));
END;
/
```

### SEND\_MESSAGE Procedure

The procedure sends a text message to a provider.

**Syntax**

```sql
DBMS_CLOUD_NOTIFICATION.SEND_MESSAGE(
       provider           IN  VARCHAR2,
       credential_name    IN  VARCHAR2,
       message            IN  CLOB,
       params             IN  CLOB
 );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `provider` | Specifies the provider.  Valid values are: ' `email` ', ' `msteams` ', and ' `slack` '  This parameter is mandatory. |
| `credential_name` | The name of the credential object to access the provider.  For the email provider, the credential is the name of the credential of the SMTP approved sender that contains its username and password.  For the msteams provider, the credential must contain the `bot_id` and the `bot_secret` key in both the username and the password.  For the Slack provider, the credential's username must be `"SLACK_TOKEN"` and the `password` is the Slack Bot Token.  This parameter is mandatory. |
| `message` | Specifies the message text.  This parameter is mandatory. |
| `params` | Specifies specific parameters for the `provider` in JSON format.  For the provider type `email`, the valid parameters are:  - `sender`. This specifies the Email ID of the approved sender in a `String` value. - `smtp_host`. This specifies the SMTP host name in a `String` value. - `subject`. This specifies the subject of the email in a `String` value. The maximum size is 100 characters. - `recipient`. This specifies the email IDs of recipients in a `String` value. Use a comma between email IDs when there are multiple recipients. - `to_cc`. This specifies the email IDs that are receiving a CC of the email. Use a comma between email IDs when there are multiple CC recipients. - `to_bcc`. This specifies the email IDs that are receiving a BCC of the email. Use a comma between email IDs when there are multiple BCC recipients.  For the provider type `msteams`, the valid parameter is:  - `channel`. This specifies the Channel ID in a `String` value.  For the provider type `slack`, the valid parameter is:  - `channel`. This specifies the Channel ID in a `String` value.  The Channel ID is a unique ID for a channel and is different from the channel name. In Slack, when you view channel details you can find the Channel ID on the "About" tab.  This parameter is mandatory. |

**Usage Notes**

Use the procedure `DBMS_CLOUD.CREATE_CREDENTIAL` `(credential_name`, `username`, `password)` to create the credential object. See [CREATE\_CREDENTIAL Procedure](dbms_cloud.md) for more information.

- For the `email` provider, the user requires an SMTP connection endpoint for the Email Delivery server to obtain `smtp_host`. The user also requires an SMTP approved sender and its credentials to authenticate with the Email Delivery server to obtain the `credential_name`. SMTP connection must be configured, and SMTP credentials must be generated and approved.
- For the `msteams` provider, the user requires the Microsoft Teams App and a bot configured in it. The app needs to be published to the org and installed after obtaining approval from the admin from the admin center. The user also requires access for `Files.ReadWrite.All` and `ChannelSettings.Read.All` permission for Graph API from their Azure Portal. To generate the required token, the user requires `bot_id` in the username and `bot_secret` in the password.
- For the `slack` provider, the `username` value can be any valid string and the `password` is the Slack bot token.

**Examples**

Send a text message with the `email` provider:

```sql
BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(
    credential_name => 'EMAIL_CRED',
    username        => 'username',
    password        => 'password');
END;
/

BEGIN
   DBMS_CLOUD_NOTIFICATION.SEND_MESSAGE(
        provider        => 'email',
        credential_name => 'EMAIL_CRED',
        message         => 'Subject content',
        params          => json_object('recipient' value  'mark@oracle.com, suresh@oracle.com',
                                       'to_cc'  value 'nicole@oracle.com, jordan@oracle.com',
                                       'to_bcc' value 'manisha@oracle.com',
                                       'subject' value 'Test subject',
                                       'smtp_host' value 'smtp.email.example.com',
                                       'sender'    value  'approver_sender@oracle.com' )
   );
   END;
/
```

Send a text message with the `msteams` provider:

```sql
BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(credential_name => 'TEAMS_CRED',
        username        => 'bot_id',
        password        => 'bot_secret');
END;
/

BEGIN
     DBMS_CLOUD_NOTIFICATION.SEND_MESSAGE(
        provider        => 'msteams',
        credential_name => 'TEAMS_CRED',
        message         => 'text from new teams api',
        params          => json_object('channel'value 'C0....08'),'region'value 'india');
END;
/
```

Send a text message with the `slack` provider:

```sql
BEGIN
   DBMS_CLOUD.CREATE_CREDENTIAL(
     credential_name => 'SLACK_CRED',
     username        => 'SLACK_TOKEN',
     password        => 'password');
END;
/
BEGIN
   DBMS_CLOUD_NOTIFICATION.SEND_MESSAGE(
      provider          => 'slack',
      credential_name   => 'SLACK_CRED',
      message           => 'Send text from Autonomous Database.',
      params            => json_object('channel' value 'C0....08'));
END;
/
```