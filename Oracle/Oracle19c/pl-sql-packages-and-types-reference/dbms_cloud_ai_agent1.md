---
title: DBMS_CLOUD_AI_AGENT
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/dbms_cloud_ai_agent1.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_CLOUD_AI_AGENT` package defines and manages Select AI agents, tasks, tools, and orchestration.

### Installing DBMS\_CLOUD Packages

The `DBMS_CLOUD` family of packages is not pre-installed or configured with Oracle database. You need to manually install the `DBMS_CLOUD` packages and also configure users or roles to use this package.

For information on installation and configuration with Oracle Database 19c, Release 19.30 and above, see [Using the DBMS\_CLOUD Family of Packages](https://docs.oracle.com/en/database/oracle/oracle-database/26/sutil/using-dbms_cloud-family-packages.html#SUTIL-GUID-0F94EA7F-1BD0-41BF-90FA-25F5B89DC87B).

For installing the `DBMS_CLOUD` packages and configuring users or roles for Oracle Database 19c, Releases prior to 19.30, see the MOS-NOTE with Doc ID [2748362.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=213651872530310&id=2748362.1&_afrWindowMode=0&_adf.ctrl-state=dz5ua14hn_4). Note that earlier releases provide limited `DBMS_CLOUD` functionality only.

### Summary of DBMS\_CLOUD\_AI\_AGENT Subprograms

This section covers the Select AI Agent’s `DBMS_CLOUD_AI_AGENT` subprograms provided with Oracle Database.

| Subprogram | Description |
| --- | --- |
| CREATE\_AGENT Procedure | This procedure creates an agent. |
| CREATE\_AGENT Attributes | Provides attributes for creating an agent. |
| ENABLE\_AGENT Procedure | This procedure enables an agent. |
| DISABLE\_AGENT Procedure | This procedure disables an agent. |
| DROP\_AGENT Procedure | This procedure drops an existing agent. |
| CREATE\_TASK Procedure | This procedure creates a task that an agent and agent team can include. |
| CREATE\_TASK Attributes | Provides attributes for creating an agent task. |
| ENABLE\_TASK Procedure | This procedure enables an agent task. |
| DISABLE\_TASK Procedure | This procedure disables an agent task. |
| DROP\_TASK Procedure | This procedure drops an existing agent task. |
| CREATE\_TOOL Procedure | This procedure creates custom tools that an agent can include. |
| CREATE\_TOOL Attributes | Provides attributes for creating tools. |
| ENABLE\_TOOL Procedure | This procedure enables a registered tool. |
| DISABLE\_TOOL Procedure | This procedure disables a registered tool. |
| DROP\_TOOL Procedure | This procedure drops an existing tool. |
| CREATE\_TEAM Procedure | This procedure creates an agent team and includes agents and tasks. |
| CREATE\_TEAM Attributes | Provides attributes for creating an agent team. |
| SET\_TEAM Function | This procedure sets the agent team in the current session. |
| GET\_TEAM Function | This procedure returns the agent team set in the current session. |
| CLEAR\_TEAM Function | This procedure clears the agent team set in the current session. |
| RUN\_TEAM Function | This procedure creates a new agent or runs a paused one. |
| ENABLE\_TEAM Procedure | This procedure enables an agent team. |
| DISABLE\_TEAM Procedure | This procedure disables an agent team. |
| DROP\_TEAM Procedure | This procedure drops an existing agent team. |

### CREATE\_AGENT Procedure

Use the `DBMS_CLOUD_AI_AGENT.CREATE_AGENT` procedure to register a new AI agent in the Select AI Agent framework. Define the agent’s identity using `agent_name`, configure its behavior with the attributes parameter, and optionally provide a description.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.CREATE_AGENT(
     agent_name          IN  VARCHAR2,
     attributes          IN  CLOB,
     status              IN  VARCHAR2  DEFAULT NULL,
     description         IN  CLOB      DEFAULT NULL
  );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `agent_name` | A name for the AI agent. The agent name must follow the naming rules of Oracle SQL identifier. Maximum length of name is 125 characters.  This is a mandatory parameter. |
| `attributes` | Custom attributes for the AI agent. See CREATE\_AGENT Attributes for more details. |
| `status` | Status of the agent.  The default value is `enabled`. |
| `description` | User-specified description for the AI agent.  The default value is NULL. |

**Example**

The following example creates an agent to process customer product returns. For a complete example, see [Example: Create a Product Return Agent](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-82F6F7DF-5011-4CCD-944D-CB25E7D8A9E5).

```sql
BEGIN
  DBMS_CLOUD_AI_AGENT.CREATE_AGENT(
    agent_name => 'CustomerAgent',
    attributes => '{
       "profile_name": "GOOGLE",
                       "role": "You are an experienced customer agent who deals with customers return request."
     }'
  );
END;
/

PL/SQL procedure successfully completed.
```

### CREATE\_AGENT Attributes

**Attributes**

| Attribute Name | Default Value | Description |
| --- | --- | --- |
| `profile_name` | \- | The AI profile that the agent is using to send request to LLM.  This is a mandatory parameter. |
| `role` | \<p>-\</p> | Define the agent's function and provide context to the agent. This is sent to LLM.  This is a mandatory parameter. |
| `enable_human_tool` | `True` | Enable agent to ask questions to the user for information or clarification. |

The following example shows you how you can customize agent attributes in the procedure.

```md
BEGIN
  DBMS_CLOUD_AI_AGENT.CREATE_AGENT(
    agent_name => 'Customer_Return_Agent',
    attributes => '{
       "profile_name": "GOOGLE",
                       "role": "You are an experienced customer agent who deals with customers return request.",
               "enable_human_tool": "False"
     }'
  );
END;
/

PL/SQL procedure successfully completed
```

### ENABLE\_AGENT Procedure

This procedure enables the AI agent that the user specifies. The procedure changes the status of the AI agent to `ENABLED`.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.ENABLE_AGENT(
   agent_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `agent_name` | Name for the AI agent to enable.  This parameter is mandatory. |

**Example to Enable AI Profile**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.ENABLE_AGENT(
         agent_name    => 'Customer_Return_Agent'
     );
END;
/
```

### DISABLE\_AGENT Procedure

This procedure disables the AI agent in the current database. The status of the AI agent is changed to `DISABLED` by this procedure.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DISABLE_AGENT(
   agent_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `agent_name` | Name for the AI agent.  This parameter is mandatory. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DISABLE_AGENT(
         agent_name    => 'Customer_Return_Agent'
     );
END;
/
```

### DROP\_AGENT Procedure

The procedure drops an existing AI agent. If the agent does not exist, then the procedure throws an error.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DROP_AGENT(
    agent_name          IN  VARCHAR2,
    force               IN  BOOLEAN DEFAULT FALSE
 );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `agent_name` | Name of the AI agent.  This is a mandatory parameter. |
| `force` | If `TRUE`, then the procedure ignores errors if AI agent does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DROP_AGENT(agent_name => 'Customer_Return_Agent');
END;
/
```

**Usage Notes**

Use `force` to drop an agent and ignore errors if AI agent does not exist.

### CREATE\_TASK Procedure

Use the `DBMS_CLOUD_AI_AGENT.CREATE_TASK` procedure to define a task that a Select AI agent can include in its reasoning process. Each task has a unique name and a set of attributes that specify the agent’s behavior when planning and performing the task.

You can define dependencies between tasks using the `input` attribute, allowing Select AI to pass the output of one task into another. This supports chained reasoning and multi-step workflows.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.CREATE_TASK(
     task_name           IN  VARCHAR2,
     attributes          IN  CLOB,
     status              IN  VARCHAR2  DEFAULT NULL,
     description         IN  CLOB      DEFAULT NULL
  );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `task_name` | A unique name for the task.  This is a mandatory parameter. |
| `attributes` | JSON object containing task-specific attributes. See CREATE\_TASK Attributes. |
| `status` | Status of the task.  The default value is `ENABLED`. |
| \<p> `description` \</p> | User-defined description to help identify the task. This value is stored in the database but not sent to the LLM.  The default value is NULL. |

**Example**

The following example creates a task to process a product return from a customer.

```sql
BEGIN
  DBMS_CLOUD_AI_AGENT.CREATE_TASK(
    task_name => 'Return_And_Price_Match',
    attributes => '{"instruction": "Process a product return request from a customer:{query}' ||
                    '1. Ask customer the reason for return (price match or defective)' ||
                    '2. If price match:' ||
                    '   a. Request customer to provide a price match link' ||
                    '   b. Use websearch tool to get the price for that price match link' ||
                    '   c. Ask customer if they want a refund.' ||
                    '   d. Send email notification only if customer accept the refund.' ||
                    '3. If defective:' ||
                     '   a. Process the defective return",
                    "tools": ["WebSearch", "Email"]}'
  );
END;
/
```

### CREATE\_TASK Attributes

**Attributes**

| Attribute Name | Default Value | Description |
| --- | --- | --- |
| `instruction` | \- | A clear, concise statement that describes what the task should accomplish. This text is included in the prompt sent to the LLM. You can include a `{query}` placeholder to represent the your natural language input. For example:  ```md SELECT AI AGENT ```  This is a mandatory parameter. |
| `tools` | \- | A JSON array of tool names that the agent can use to complete the task. For example: `"tools": ["SQL", "WEBSEARCH", "NOTIFICATION"]`.  This is a mandatory parameter. |
| `input` | \- | Identifies other tasks whose outputs should be used as input for this task. Select AI automatically provides these outputs to the LLM. |
| \<p> `enable_human_tool` \</p> | \- | Enable agent to ask questions to user when it requires information or clarification during a task.  Default value is true.  Note:  Task `enable_human_tool` overwrites the agent `enable_human_tool` attribute. If agent `enable_human_tool` is set to `false` and task `enable_human_tool` is set to `true`, during the task run, the LLM is expected to ask questions. |

### ENABLE\_TASK Procedure

Use the `DBMS_CLOUD_AI_AGENT.ENABLE_TASK` procedure to enable a previously defined task. This changes the task’s status to `ENABLED`, allowing the agent to use it during processing.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.ENABLE_TASK(
   task_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `task_name` | Name for the task to enable.  This parameter is mandatory. |

**Usage Notes**

The task must already exist in the system. This procedure updates the task status, making it available for agent process during reasoning workflows.

**Example to Enable a Task**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.ENABLE_TASK(
         task_name    => 'Return_And_Price_Match'
     );
END;
/
```

### DISABLE\_TASK Procedure

Use the `DBMS_CLOUD_AI_AGENT.DISABLE_TASK` procedure to disable a task in the current database. This changes the task’s status to `DISABLED`, preventing the agent from using it during processing.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DISABLE_TASK(
   task_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task to disable.  This parameter is mandatory. |

**Usage Notes**

Disabling a task does not delete it; you can re-enable it later using `DBMS_CLOUD_AI_AGENT.ENABLE_TASK`. Once disabled, the task becomes inactive and the agent no longer considers it during task selection.

**Example**

The following example disables an existing task.

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DISABLE_TASK(
         task_name    => 'Return_And_Price_Match'
     );
END;
/
```

### DROP\_TASK Procedure

Use the `DBMS_CLOUD_AI_AGENT.DROP_TASK` procedure to remove a previously defined task from the database. If the task does not exist, you can suppress the error by setting the `force` parameter to `TRUE`.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DROP_TASK(
   task_name IN  VARCHAR2,
   force     IN  BOOLEAN DEFAULT FALSE
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `task_name` | Name of the task to drop.  This is a mandatory parameter. |
| `force` | If `TRUE`, then the procedure ignores errors if the task does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DROP_TASK(task_name => 'Return_And_Price_Match');
END;
/
```

**Usage Notes**

Use `force` to drop a task and ignore errors if the task does not exist.

### CREATE\_TOOL Procedure

Use the `DBMS_CLOUD_AI_AGENT.CREATE_TOOL` procedure to register a custom tool that an agent can use during task processing. Each tool is identified by a unique `tool_name` and includes attributes that define its purpose, implementation logic, and metadata.

The tools can be custom PL/SQL procedures or functions, or built-in tool types such as SQL, WEBSEARCH, or NOTIFICATION.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.CREATE_TOOL(
     tool_name          IN  VARCHAR2,
     attributes          IN  CLOB,
     status              IN  VARCHAR2  DEFAULT NULL,
     description         IN  CLOB      DEFAULT NULL
  );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `tool_name` | A unique name to identify the tool.  This is a mandatory parameter. |
| `attributes` | Tool attributes in JSON format. See CREATE\_TOOL Attributes.  This is a mandatory parameter. |
| `status` | Status of the tool.  The default value is `ENABLED`. |
| `description` | User-defined description to help identify the tool. This value is stored in the database but not sent to the LLM.  The default value is NULL. |

**Example**

The following example creates a tool for to generate an email to the recipient.

```sql
BEGIN
  DBMS_CLOUD_AI_AGENT.CREATE_TOOL(
    tool_name  => 'NOTIFICATION',
    attributes => '{"tool_type": "EMAIL"}'
  );
END;
/
```

### CREATE\_TOOL Attributes

**Attributes**

| Attribute Name | Default Value | Description |
| --- | --- | --- |
| `instruction` | \- | A clear, concise statement that describes what the tool should accomplish and how to do it. This text is included in the prompt sent to the LLM.  This is a mandatory parameter. |
| `function` | \- | Specifies the PL/SQL procedure or function to call when the tool is used.  This is a mandatory parameter for custom tools. |
| `tool_type` | \- | Specifies a built-in tool type. If set, `instruction` and `function` are not required.  The possible values are:  - `SQL` - `WEBSEARCH` - `NOTIFICATION`  You can create built-in tools with customized names and parameters. You can also create multiple built-in tools with same `tool_type` but different `tool_params`. |
| `tool_params` | \- | Specifies parameters for registering built-in tools. |
| `tool_inputs` | \- | Describes input arguments. Similar to column comments in a table. For example:  ```md "tool_inputs": [ { "name": "data_guard", "description": "Only supported values are "Enabled" and "Disabled"" } ] ``` |

**Prerequisites for Built-In Tool**

Perform these steps before you use built-in tools:

**NOTIFICATION Tool**

The following are supported: `SLACK` and `EMAIL`.

**SLACK Tool**:

1. Set up a Slack application to receive messages from Autonomous Database.
2. Create a credential using `DBMS_CLOUD_NOTIFICATION` to send Slack notifications from Autonomous Database. See [Send Slack Notifications from Autonomous Database](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-CEE3933E-2542-401D-B65A-AAFA288BA847) for more details.

**EMAIL Tool**:

**Note:** The email tool sends email notification from OCI.

1. Identify your SMTP endpoint. For example, select one of the SMTP endpoints:
	```md
	smtp.us-phoenix-1.oraclecloud.com
	smtp.us-ashburn-1.oraclecloud.com
	smtp.email.uk-london-1.oci.oraclecloud.com
	smtp.email.eu-frankfurt-1.oci.oraclecloud.com
	```
2. Grant SMTP access using an ACL. See [Configuring SMTP Connection](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Configure_the_SMTP_connection.htm).
3. Generate SMTP credentials for email delivery. The `UTL_SMTP` package uses credentials to authenticate with email delivery servers when you send an email. See [Generate SMTP Credentials for a User](https://docs.oracle.com/iaas/Content/Email/Reference/gettingstarted_topic-create-smtp-credentials.htm#top) for more information.
4. Create approved senders. Complete this step for all email addresses you use as the `From` address with `UTL_SMTP.MAIL` subprogram. See [Managing Approved Senders](https://docs.oracle.com/iaas/Content/Email/Tasks/managingapprovedsenders.htm) for more information.
5. Grant SMTP access to the user by adding Access Control Entry (ACE). For more details, see [Send Email from Autonomous Database Using DBMS\_CLOUD\_NOTIFICATION](https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/smtp-send-mail.html#GUID-931E5FC9-627D-499B-92E7-26D0E84311AC).

**Built-In Tool Types in DBMS\_CLOUD\_AI\_AGENT Package**

You can register built-in tools using the `tool_type` and `tool_params` attributes.

| Tool Type | Description | Mandatory Parameters |
| --- | --- | --- |
| `SQL` | Translates natural language into SQL queries. | `profile_name` |
| `NOTIFICATION` | Sends messages to a Slack channel or sends emails using SMTP. Available options:  - `slack` - `email` | `notification_type`.  When `notification_type` is `slack` then `credential_name` and `channel` are mandatory.  When `notification_type` is `email` then `credential_name`, `recipient`, `sender`, and `smtp_host` are mandatory. |
| `WEBSEARCH` | Searches information from the web. | `credential_name` |

### ENABLE\_TOOL Procedure

Use the `DBMS_CLOUD_AI_AGENT.ENABLE_TOOL` procedure to enable a previously registered tool. This changes the tool’s status to `ENABLED`, allowing the agent to use it tasks.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.ENABLE_TOOL(
   tool_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `tool_name` | Name for the tool to enable.  This parameter is mandatory. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.ENABLE_TOOL(
         tool_name    => 'SQL'
     );
END;
/
```

### DISABLE\_TOOL Procedure

Use the `DBMS_CLOUD_AI_AGENT.DISABLE_TOOL` procedure to disable a registered tool. This changes the tool’s status to `DISABLED`, preventing the agent from using it in tasks.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DISABLE_TOOL(
   tool_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `tool_name` | Name of the tool to disable.  This parameter is mandatory. |

**Example**

The following example disables an existing tool.

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DISABLE_TOOL(
         tool_name    => 'SQL'
     );
END;
/
```

### DROP\_TOOL Procedure

Use the `DBMS_CLOUD_AI_AGENT.DROP_TOOL` procedure to remove a previously registered tool with the agent. If the task does not exist, you can suppress the error by setting the `force` parameter to `TRUE`.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DROP_TOOL(
   tool_name IN  VARCHAR2,
   force     IN  BOOLEAN DEFAULT FALSE
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `tool_name` | Name of the tool to drop.  This is a mandatory parameter. |
| `force` | If `TRUE`, then the procedure ignores errors if tool does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DROP_TOOL(tool_name => 'SQL');
END;
/
```

**Usage Notes**

Use `force` to drop a tool and ignore errors if the tool does not exist.

### CREATE\_TEAM Procedure

Use the `DBMS_CLOUD_AI_AGENT.CREATE_TEAM` procedure to define a team of AI agents that work together to accomplish tasks. You specify agents and their associated tasks, along with how the tasks should be processed.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.CREATE_TEAM(
   team_name    IN VARCHAR2,
   attributes   IN CLOB,
   status       IN VARCHAR2 DEFAULT NULL,
   description  IN CLOB     DEFAULT NULL
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `team_name` | A unique name to identify the AI agent team.  This is a mandatory parameter. |
| `attributes` | JSON-formatted string defining team attributes such as agents and process. See CREATE\_TEAM Attributes.  This is a mandatory parameter. |
| `status` | Status of the team.  The default value is `ENABLED`. |
| `description` | User-defined description to identify the team's purpose. This value is stored in the database but not sent to the LLM.  The default value is NULL. |

**Example**

The following example creates an agent team to process a customer’s product return.

```sql
BEGIN
  DBMS_CLOUD_AI_AGENT.CREATE_TEAM(
    team_name  => 'ReturnAgency',
    attributes => '{"agents": [{"name":"Customer_Return_Agent","task" : "Return_And_Price_Match"}],
                    "process": "sequential"}');
END;
/
```

### CREATE\_TEAM Attributes

**Attributes**

| Attribute Name | Default Value | Description |
| --- | --- | --- |
| `agents` | \- | Specifies JSON array listing agents and their corresponding tasks. An agent can be assigned to multiple tasks using the same name.  This is a mandatory parameter.  Example:  ```md [ {"name": "", "task": ""} ] ``` |
| `process` | \- | Specifies how tasks are run. Use `"sequential"` for tasks to run one after another in order. |

### SET\_TEAM Function

Use `DBMS_CLOUD_AI_AGENT.SET_TEAM` to specify the AI agent team for the current session.

Once a team is set, only the `select ai agent` action is enabled, the system does not support other Select AI actions.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.SET_TEAM(
    team_name      IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `team_name` | Specifies the name of the AI Agent team to use in the current session. The team must already exist in the system.  This parameter is mandatory. |

**Example**

The following example sets the user-specified AI agent team in the current session.

```sql
EXEC DBMS_CLOUD_AI_AGENT.SET_TEAM('ReturnAgency');
```

### GET\_TEAM Function

Use `DBMS_CLOUD_AI_AGENT.GET_TEAM` to return the AI agent team for the current session.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.GET_TEAM RETURN VARCHAR2;
```

**Example**

The following example returns the AI agent team in the current session.

```sql
SELECT DBMS_CLOUD_AI_AGENT.GET_TEAM from DUAL;
```

### CLEAR\_TEAM Function

Use `DBMS_CLOUD_AI_AGENT.CLEAR_TEAM` to clear the AI agent team set in the current session. This procedure does not drop the team.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.CLEAR_TEAM;
```

**Example**

The following example clears the AI agent team in the current session.

```sql
BEGIN
  DBMS_CLOUD_AI_AGENT.CLEAR_TEAM;
END;
/
```

### RUN\_TEAM Function

Use `DBMS_CLOUD_AI_AGENT.RUN_TEAM` to start a new AI agent team or resume a paused one that is waiting for human input. If you provide an existing process ID and the associated team process is in the `WAITING_FOR_HUMAN` state, the function resumes the workflow using the input you provide as the human response.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.RUN_TEAM(
     team_name               IN  VARCHAR2,
     user_prompt             IN  CLOB DEFAULT NULL,
     params                  IN  CLOB DEFAULT NULL
  );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `team_name` | Specifies the name of the AI Agent team to use in the current session. The team must already exist in the system.  This parameter is mandatory. |
| `user_prompt` | Specifies the user query or response provided to the task.  If the task is in the `RUNNING` state, the input acts as a placeholder for the `{query}` in the task instruction.  If the task is in the `WAITING_FOR_HUMAN` state, the input serves as the human response. |
| `params` | Specifies customized parameters used during AI agent team process. Supported parameters include:  - `conversation_id`: Identifies the conversation session associated with the agent team. Use this parameter for stateless application integrations (for example, APEX) to distinguish between different user connections. - `variables`: Define key-value pairs that provide additional input to the agent team. These variables help customize the team's behavior during the process. |

**Example**

The following example runs the user-specified AI agent team in the current session.

```sql
l_final_answer := DBMS_CLOUD_AI_AGENT.RUN_TEAM(
  team_name => 'ReturnAgency',
  user_prompt => 'I want to return computer desk chair',
  params => '{"conversation_id": "' ||l_conversation_id || '"}'
);
```

### ENABLE\_TEAM Procedure

Use the `DBMS_CLOUD_AI_AGENT.ENABLE_TEAM` procedure to enable a user-specified AI agent team. This changes the team’s status to `ENABLED`.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.ENABLE_TEAM(
   team_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `team_name` | Name for the AI agent team to enable.  This parameter is mandatory. |

**Example**

The following example enables a user-specified AI agent team.

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.ENABLE_TEAM(
         team_name    => 'ReturnAgency'
     );
END;
/
```

### DISABLE\_TEAM Procedure

Use the `DBMS_CLOUD_AI_AGENT.DISABLE_TEAM` procedure to disable an existing AI agent team. This changes the team’s status to `DISABLED`.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DISABLE_TEAM(
   team_name           IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `team_name` | Name of the AI agent team to disable.  This parameter is mandatory. |

**Example**

The following example disables an existing AI agent team.

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DISABLE_TEAM(
         team_name    => 'ReturnAgency'
     );
END;
/
```

### DROP\_TEAM Procedure

Use the `DBMS_CLOUD_AI_AGENT.DROP_TEAM` procedure to remove a previously created AI agent team.

**Syntax**

```sql
DBMS_CLOUD_AI_AGENT.DROP_TEAM(
   team_name IN  VARCHAR2,
   force     IN  BOOLEAN DEFAULT FALSE
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `team_name` | Name of the team to drop.  This is a mandatory parameter. |
| `force` | If `TRUE`, then the procedure ignores errors if team does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI_AGENT.DROP_TEAM(team_name => 'ReturnAgency');
END;
/
```

**Usage Notes**

Use `force` to drop a team and ignore errors if the team does not exist.