---
title: DBMS_CLOUD_AI
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/dbms_cloud_ai1.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_CLOUD_AI` package with Select AI facilitates and configures the generation of SQL queries from natural language prompts to generate, run, and explain SQL statements. It also enables synthetic data generation, text summarization and translation, along with direct LLM chat.

### Installing DBMS\_CLOUD Packages

The `DBMS_CLOUD` family of packages is not pre-installed or configured with Oracle database. You need to manually install the `DBMS_CLOUD` packages and also configure users or roles to use this package.

For information on installation and configuration with Oracle Database 19c, Release 19.30 and above, see [Using the DBMS\_CLOUD Family of Packages](https://docs.oracle.com/en/database/oracle/oracle-database/26/sutil/using-dbms_cloud-family-packages.html#SUTIL-GUID-0F94EA7F-1BD0-41BF-90FA-25F5B89DC87B).

For installing the `DBMS_CLOUD` packages and configuring users or roles for Oracle Database 19c, Releases prior to 19.30, see the MOS-NOTE with Doc ID [2748362.1](https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=213651872530310&id=2748362.1&_afrWindowMode=0&_adf.ctrl-state=dz5ua14hn_4). Note that earlier releases provide limited `DBMS_CLOUD` functionality only.

### DBMS\_CLOUD\_AI Overview

Learn how you can use the `DBMS_CLOUD_AI` package.

Use the `DBMS_CLOUD_AI` package to create AI profiles and configure them for access to a Large Language Model (LLM). Set the AI profile in the current database user session to perform tasks, such as generating, running, and explaining SQL. In addition, you can use this package for natural language-based interactions including chatting with LLMs.

To learn more about supported platforms and LLMs, see: [About Select AI](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SELAI-GUID-D3FFFC75-0BC6-4D17-9FB0-C60E1FEC2E46).

### Summary of DBMS\_CLOUD\_AI Subprograms

This section covers the `DBMS_CLOUD_AI` subprograms and supporting parameter or attribute references provided with Oracle Database.

| Subprogram | Description |
| --- | --- |
| CREATE\_PROFILE Procedure | This procedure creates a new AI profile for translating natural language prompts to SQL statements. |
| Profile Attributes | Provides AI profile attributes that you can configure. |
| CLEAR\_PROFILE Procedure | This procedure clears an active AI profile in the current session. |
| DISABLE\_PROFILE Procedure | This procedure disables an AI profile in the current database. |
| DROP\_PROFILE Procedure | This procedure drops an existing AI profile. |
| ENABLE\_PROFILE Procedure | This procedure enables an AI profile to use in the current database. |
| GENERATE Function | This function enables you to use Select AI in a stateless manner with your existing profile. |
| GENERATE\_SYNTHETIC\_DATA Function | This function generates synthetic data. |
| GET\_PROFILE Function | This function returns the profile name used in the current session. |
| SET\_ATTRIBUTE Procedure | This procedure sets AI profile attributes. |
| SET\_ATTRIBUTES Procedure | This procedure enables you to set one or more AI profile attributes by accepting attribute name and value pairs in JSON format. |
| SET\_PROFILE Procedure | This procedure sets AI profile for the current database. |
| ENABLE\_DATA\_ACCESS Procedure | Use this procedure to enable sending data to your LLM. |
| DISABLE\_DATA\_ACCESS Procedure | Use this procedure to disable sending data to your LLM. |
| CREATE\_CONVERSATION Procedure | This procedure helps you to create a conversation. |
| CREATE\_CONVERSATION Function | This function helps you to create a conversation and use the conversation ID in other procedures. |
| CREATE\_CONVERSATION Attributes | Use the conversation attributes to customize your conversations. |
| UPDATE\_CONVERSATION Procedure | This procedure updates an existing procedure with user-specified parameters. |
| SET\_CONVERSATION\_ID Procedure | This procedure sets conversation support in the current session. |
| GET\_CONVERSATION\_ID Function | This procedure helps you to get the `conversation_id` parameter. |
| CLEAR\_CONVERSATION\_ID Procedure | This procedure helps you to clear any `conversation_id` set in the current session. |
| DELETE\_CONVERSATION\_PROMPT Procedure | This procedure deletes a particular prompt. |
| DROP\_CONVERSATION Procedure | This procedure deletes an entire conversation and its metadata. |
| SUMMARIZE Function | This function summarizes your content based on the parameters. |
| SUMMARIZE Parameters | Use the summarize attributes to customize summary generation. |
| TRANSLATE Function | This function enables you to translate your text into the specified `target_language`. |

### CREATE\_PROFILE Procedure

The procedure creates a new AI profile for translating natural language prompts to SQL statement.

**Syntax**

```sql
DBMS_CLOUD_AI.CREATE_PROFILE(
   profile_name        IN  VARCHAR2,
   attributes          IN  CLOB      DEFAULT NULL,
   status              IN  VARCHAR2  DEFAULT NULL,
   description         IN  CLOB      DEFAULT NULL
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `profile_name` | A name for the AI profile. The profile name must follow the naming rules of Oracle SQL identifier. Maximum length of profile name is 125 characters.  This is a mandatory parameter. |
| `attributes` | Profile attributes in JSON format. See AI Profile Attributes for more details.  The default value is NULL. |
| `status` | Status of the profile.  The default value is enabled. |
| `description` | Description for the AI profile.  The default value is NULL. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI.CREATE_PROFILE(
          profile_name    => 'OpenAI',
          attributes      => JSON_OBJECT('provider' value 'openai',
                                         'credential_name' value 'openai_cred'),
        status     => 'enabled',
          description     => 'AI profile to use OpenAI for SQL translation'
     );
END;
/
```

To view profile attributes, see

- [DBA\_CLOUD\_AI\_PROFILE\_ATTRIBUTES View](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-CEEE312D-E618-4701-A17C-323096D8F5CE)
- [USER\_CLOUD\_AI\_PROFILE\_ATTRIBUTES View](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-1CF66036-DCD2-40D1-9539-A1E2E879A6A1)

### Profile Attributes

**Attributes**

| Attribute Name | Description |
| --- | --- |
| `azure_deployment_name` | Name of the Azure OpenAI Service deployed model. The name can only include alphanumeric characters, underscore character (*) and a hyphen (-) character. The name cannot end with an underscore (*) or a hyphen (-). To know how to get the `azure_deployment_name`, see [Create and deploy an Azure OpenAI Service resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal). |
| `azure_embedding_deployment_name` | Name of the Azure OpenAI deployed embedding model.  The name can only include alphanumeric characters, underscore, and hyphen. The name can't start or end with a hyphen or underscore. |
| `azure_resource_name` | Name of the Azure OpenAI Service resource. The resource name can only include alphanumeric characters and hyphens, and can’t start or end with a hyphen. To know how to get the `azure_resource_name`, see [Create and deploy an Azure OpenAI Service resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal). |
| `case_sensitive_values` | Specifies whether Select AI should instruct the LLM to generate case-insensitive SQL for columns containing string or text values.  The supported values are:  - `true`: Indicates the LLM to generate SQL queries with case-sensitive string values. - `false`: Indicates the LLM to generate SQL queries that ignore case for string values.  The default value is `false`. |
| `comments` | Includes table and column comments in the metadata used for translating natural language prompts using AI. `BOOLEAN` data type is supported. The valid values are `TRUE` or `FALSE` for a string with `VARCHAR2` data type. The values are not case sensitive. |
| `constraints` | Manages whether to include referential integrity constraints such as primary and foreign keys in the metadata sent to the LLM.  The valid values are `TRUE` or `FALSE`. The default value is `FALSE`. The values are not case sensitive.  `TRUE`: Includes referential constraints in the augmented prompt metadata that is sent to the LLM.  `FALSE`: Does not include referential integrity constraints. |
| `conversation` | A `VARCHAR2` attribute that indicates if conversation history is enabled for a profile. Valid values are `true` or `false`. The default value is `false`. The values are not case sensitive. |
| `conversation_length` | You can specify `conversation_length`. You can change the existing value to a suitable value for your use case. This is not a mandatory parameter. See CREATE\_CONVERSATION Attributes for details. |
| `credential_name` | The name of the credential to access the AI provider APIs.  Credential using bearer tokens can be created by using the provider name as the user name and bearer token as the password.  Vault Secret credentials are also supported.  Principal authentication, for example, Azure service principal, is also supported. For more information on how to configure it, see [Use Azure Service Principal to Access Azure Resources](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-29ED76DB-8202-44B3-9ADF-D5352334D7B4).  This is a mandatory attribute. See [CREATE\_CREDENTIAL Procedure](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-742FC365-AA09-48A8-922C-1987795CF36A#GUID-742FC365-AA09-48A8-922C-1987795CF36A). |
| `enforce_object_list` | Specifies whether to restrict the LLM to generate SQL that uses only tables covered by the object list.  The supported values are:  - `true`: Enforces the use of only the tables specified in the object list. - `false`: Allows the LLM to use tables accessible to the user.  The values are not case sensitive. The default value is `false`. |
| `max_tokens` | Denotes the number of tokens to predict per generation. Default is 1024. See [Tokens and Tokenizers](https://docs.cohere.com/docs/tokens-and-tokenizers) for more details. |
| `model` | The name of the AI model being used to generate responses.  See [Select Your AI Provider and LLMs](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-FDAEF22A-5DDF-4BAE-A465-C1D568C75812) and specify the model name.  Note:  - Cohere: Smaller, "light" models are faster, while larger models perform better.[Custom models](https://docs.cohere.com/docs/creating-custom-models#what-are-custom-models) can also be supplied with their full ID. - OCI Generative AI: The Chat Models are supported for all Select AI actions such as `runsql`, `showsql`, `explainsql`, `narrate`, and `chat`. 	Select AI supports pretrained models for OCI Generative AI. Custom models can also be supplied with their full OCIDs. If you are supplying OCID or `oci_endpoint_id`, be sure to provide either `oci_runtimetype` or `oci_apiformat` depending on the OCI Chat models. 	To know more about supported models in OCI Generative AI, see [Pretrained Foundational Models in Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm). - This parameter is not used for Azure as the model is determined when you create your deployment in the Azure OpenAI Service portal. - AWS: Amazon Bedrock foundation models require access permissions through the Amazon Bedrock console. See the AWS documentation to get the modelID. - OpenAI compatible: See the AI provider documentation for the supported model names. |
| `object_list` | Array of JSON objects specifying the owner and object names that are eligible for natural language translation to SQL. To include all objects of a given user, omit the "name" and only specify the "owner" key in the JSON object.  The following types of objects can be used:  - tables - views - materialized views - global temporary tables - external tables - synonyms on the above object types  For translation natural language to SQL, the object name, object owner, object columns and comments are sent to the AI provider using HTTPS requests. Avoid specifying objects with sensitive object name, column names or comments in the object list.  AI providers may have limit on the size of metadata allowed in translation requests. Consider limiting the list of objects suitable for the natural language prompts by your application users.  Format:  ```md [ {"owner": "SH", "name": "SALES", {"owner": "TEST_USER"} } ] ```  External tables created using sync of [OCI Data Catalog or AWS Glue](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-480FAF23-453D-4B15-BF92-8435805EB8A5) can also be used the object list. This helps in managing metadata in central Data Catalogs and use the metadata directly for translating natural language prompts using AI. |
| `oci_apiformat` | Specifies the format in which the API expects data to be sent and received. Use this attribute to generate text responses. This attribute applies to OCI Generative AI Chat Models in a dedicated AI cluster. Specify this attribute when you specify a model OCID in the `model` attribute or provide an endpoint in the `oci_endpoint_id` attribute.  Supported values are:  - `COHERE` - `GENERIC`  Note:  Use this attribute for [OCI Generative AI Chat Models](https://docs.oracle.com/en-us/iaas/Content/generative-ai/chat-models.htm) |
| `oci_compartment_id` | Specifies the OCID of the compartment you are permitted to access when calling the OCI Generative AI service. The compartment ID can contain alphanumeric characters, hyphens and dots.  The default is the compartment ID of the PDB. |
| `oci_endpoint_id` | This attributes indicates the endpoint OCID of the Oracle dedicated AI hosting cluster. The endpoint ID can contain alphanumeric characters, hyphens and dots. To find the endpoint OCID, see [Getting an Endpoint's Details in Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/get-endpoint.htm).  When you want to use the Oracle dedicated AI cluster, you must provide the endpoint OCID of the hosting cluster.  By default, the endpoint ID is empty and the model is on-demand on a shared infrastructure. |
| `oci_runtimetype` | This attribute indicates the runtime type of the provided model. This attribute is applicable to OCI Generate Text models in a dedicated AI cluster. Specify this attribute when you specify a model OCID in the `model` attribute or provide an endpoint in the `oci_endpoint_id` attribute.  All permitted values can be found in OCI Generative AI runtimeType. See [LlmInferenceRequest Reference](https://docs.oracle.com/en-us/iaas/api/#/en/generative-ai-inference/20231130/datatypes/LlmInferenceRequest).  The supported values are:  - `COHERE` - `LLAMA`  Note:  This attribute is deprecated. Use `oci_apiformat`. |
| `provider` | AI provider for the AI profile.  Supported providers:  - openai - cohere - azure - database - oci - google - anthropic - huggingface - aws  This is a mandatory attribute. |
| `provider_endpoint` | Specifies the API endpoint for OpenAI-compatible providers. This attribute is specific only to OpenAI-compatible providers. Specify `provider_endpoint` as an attribute in the `DBMS_CLOUD_AI.CREATE_PROFILE` procedure instead of the `provider` attribute. See [Use OpenAI Compatible Providers](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-F8EAAF29-9750-4DFD-AE2B-DBFC509AD436) to learn how to obtain the parameter.  Example: `api.fireworks.ai/inference` |
| `region` | This attribute indicates the location of the Generative AI cluster that you want to use. The region can contain alphanumeric characters and hyphen characters.  Note:  The Oracle Generative AI cluster is available in Chicago, Frankfurt, London, and other selected regions. See [Regions with Generative AI](https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm#regions) to learn more.  The default region for AWS is `us-east-1`.  The default region is `us-chicago-1`. |
| `stop_tokens` | The generated text will be terminated at the beginning of the earliest stop sequence. Sequence will be incorporated into the text. The attribute value must be a valid array of string values in JSON format. `stop_tokens` takes a JSON array as input. To learn more about stop tokens or stop sequences, see [OpenAI](https://help.openai.com/en/articles/5072263-how-do-i-use-stop-sequences) or [Cohere](https://docs.cohere.com/v2/docs/tokens-and-tokenizers) documentation. |
| `temperature` | Sampling from Generate Text models incorporates randomness, so that the same prompt may yield different outputs each time you hit “generate”. Temperature is a non-negative float number used to tune the degree of randomness. Lower temperatures mean less random generations. See [Temperature](https://docs.cohere.com/docs/temperature) for more details. This parameter is applicable to all the supported service providers. |
| \<p> `vector_index_name` \</p> | Name of the vector index. The vector index name must follow the naming rules of Oracle SQL identifier. Maximum length of the vector store name is 125 characters. |
| `source_language` | The language of the input text sent to the provider for translation. Accepts either the full language name or the language code (`language_code`) supported by providers. The values are not case sensitive. |
| `target_language` | The language into which the provider translates the text. Accepts either the full language name or the language code (`language_code`) supported by providers. The values are not case sensitive. |

The following example is using Cohere as the provider and displays custom profile attributes:

```md
BEGIN
  DBMS_CLOUD_AI.CREATE_PROFILE(
     profile_name => 'COHERE',
     attributes =>
      '{"provider": "cohere",
        "credential_name": "COHERE_CRED",
        "object_list": [{"owner": "ADB_USER"}],
        "max_tokens":512,
        "stop_tokens": [";"],
        "model": "command-nightly",
        "temperature": 0.5,
        "comments": true,
     "source_language": "en",
     "target_language": "french"
       }');
END;
/
```

The following example shows custom profile attributes using OCI Generative AI:

```md
BEGIN
  DBMS_CLOUD_AI.CREATE_PROFILE(
      profile_name => 'GENAI',
      attributes => '{"provider": "oci",
        "credential_name": "GENAI_CRED",
        "object_list": [{"owner": "SH", "name": "customers"},
                        {"owner": "SH", "name": "countries"},
                        {"owner": "SH", "name": "supplementary_demographics"},
                        {"owner": "SH", "name": "profits"},
                        {"owner": "SH", "name": "promotions"},
                        {"owner": "SH", "name": "products"}],
        "oci_compartment_id": "ocid1.compartment.oc1...",
    "oci_endpoint_id": "ocid1.generativeaiendpoint.oc1.us-chicago-1....",
    "region": "us-chicago-1",
    "model": "cohere.command-light",
    "oci_apiformat": "COHERE"
       }');
END;
/
```

### CLEAR\_PROFILE Procedure

This procedure clears any active AI profile set in the current session. Once you clear an active profile, you can no longer use `SELECT AI` on the SQL command line or use the set AI profile when calling `DBMS_CLOUD_AI.GENERATE`. This procedure does not drop the profile.

**Syntax**

```sql
DBMS_CLOUD_AI.CLEAR_PROFILE;
```

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI.CLEAR_PROFILE;
END;
/
```

### DROP\_PROFILE Procedure

The procedure drops an existing AI profile. If the profile does not exist, then the procedure throws an error.

**Syntax**

```sql
DBMS_CLOUD_AI.DROP_PROFILE(
       profile_name        IN   VARCHAR2,
       force               IN   BOOLEAN DEFAULT FALSE
 );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `profile_name` | Name of the AI profile |
| `force` | If `TRUE`, then the procedure ignores errors if AI profile does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI.DROP_PROFILE(profile_name => 'OPENAI');
END;
/
```

**Usage Notes**

Use `force` to drop a profile and ignore errors if AI profile does not exist.

### ENABLE\_PROFILE Procedure

This procedure enables the AI profile that the user specifies. The procedure changes the status of the AI profile to `ENABLED`.

**Syntax**

```sql
DBMS_CLOUD_AI.ENABLE_PROFILE(
     profile_name         IN   VARCHAR2
 );
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `profile_name` | Name for the AI profile to enable  This parameter is mandatory. |

**Example to Enable AI Profile**

```sql
BEGIN
     DBMS_CLOUD_AI.ENABLE_PROFILE(
         profile_name    => 'OPENAI'
     );
END;
/
```

### DISABLE\_PROFILE Procedure

This procedure disables the AI profile in the current database. The status of the AI profile is changed to `DISABLED` by this procedure.

**Syntax**

```sql
DBMS_CLOUD_AI.DISABLE_PROFILE(
      profile_name  IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `profile_name` | Name for the AI profile.  This parameter is mandatory. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI.DISABLE_PROFILE(
         profile_name    => 'OPENAI'
     );
END;
/
```

### GET\_PROFILE Function

This function returns the AI profile name set in the current session.

**Syntax**

```sql
DBMS_CLOUD_AI.GET_PROFILE
;
```

**Example**

This example shows how you can display the name of the profile in the current session.

```sql
SELECT DBMS_CLOUD_AI.GET_PROFILE
from DUAL;
```

### SET\_ATTRIBUTE Procedure

This procedure enables you to set AI profile attributes. It is overloaded to accept attribute values of various types.

**Syntax**

```sql
<!--Draft comment: <br/>ADBS-97824 Bundle of Select AI usability-related features for 2025Q1: boolean|varchar added-->DBMS_CLOUD_AI.SET_ATTRIBUTE(
      profile_name         IN   VARCHAR2,
      attribute_name       IN   VARCHAR2,
      attribute_value      IN   {BOOLEAN|VARCHAR2}
);

DBMS_CLOUD_AI.SET_ATTRIBUTE(
      profile_name         IN   VARCHAR2,
      attribute_name       IN   VARCHAR2,
      attribute_value      IN   CLOB DEFAULT NULL
);
```

**Parameters**

Only the owner can set or modify the attributes of the AI profile. For a list of supported attributes, see Profile Attributes.

| Parameter | Description |
| --- | --- |
| `profile_name` | Name of the AI profile for which you want to set the attributes.  This parameter is mandatory. |
| `attribute_name` | Name of the AI profile attribute  This parameter is mandatory. |
| `attribute_value` | Value of the profile attribute. Value can be `BOOLEAN`, `CLOB`, `NUMBER` or `VARCHAR2` type.  The default value is NULL. |

**Examples**

```sql
BEGIN
 DBMS_CLOUD_AI.SET_ATTRIBUTE(
   profile_name    => 'OPENAI',
   attribute_name  => 'credential_name',
   attribute_value => 'OPENAI_CRED_NEW'
 );
END;
/
```

The following example accepts `NUMBER` type as the `attribute_value`.

```md
BEGIN
 DBMS_CLOUD_AI.SET_ATTRIBUTE(
   profile_name    => 'OCI_PROFILE',
   attribute_name  => 'temperature',
   attribute_value => 0.5
 );
END;
/
```

The following example accepts `BOOLEAN` type as the `attribute_value`.

```md
BEGIN
 DBMS_CLOUD_AI.SET_ATTRIBUTE(
   profile_name    => 'OCI_PROFILE',
   attribute_name  => 'comments',
   attribute_value => 'true'
 );
END;
/
```

The following example accepts `VARCHAR2` type as the `attribute_value`.

```md
BEGIN
 DBMS_CLOUD_AI.SET_ATTRIBUTE(
   profile_name    => 'OCI_PROFILE',
   attribute_name  => 'model',
   attribute_value => 'meta.llama-3.3-70b-instruct'
 );
END;
/
```

### SET\_ATTRIBUTES Procedure

This procedure enables you to set one or more AI profile attributes. The attribute name and value pairs are provided as a JSON document.

**Syntax**

```sql
DBMS_CLOUD_AI.SET_ATTRIBUTES(
        profile_name        IN   VARCHAR2,
        attributes          IN   CLOB
);
```

**Parameters**

Only the owner can set or modify the attributes of the AI profile. For a list of supported attributes, see Profile Attributes.

| Parameter | Description |
| --- | --- |
| `profile_name` | Name of the AI profile for which you want to set the attributes.  This parameter is mandatory. |
| `attributes` | AI profile attributes in JSON format.  This parameter is mandatory. |

**Example**

The following example accepts attributes in JSON format.

```sql
BEGIN
  DBMS_CLOUD_AI.SET_ATTRIBUTES(
    profile_name => 'OCI_PROFILE',
    attributes   => '{"temperature": 0.2,
                     "max_tokens": 3000}'
  );
END;
/
```

### GENERATE Function

Overriding some or all of the profile attributes is also possible using this function.

**Syntax**

```sql
DBMS_CLOUD_AI.GENERATE(
    prompt            IN  CLOB,
    profile_name      IN  VARCHAR2 DEFAULT NULL,
    action            IN  VARCHAR2 DEFAULT NULL,
    attributes        IN  CLOB     DEFAULT NULL,
    params            IN  CLOB
) RETURN CLOB;
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `prompt` | Natural language prompt to translate using AI.  The prompt can include `SELECT AI ` as the prefix. The action can also be supplied separately as an "action" parameter. The action supplied in the prompt overrides the `action` parameter. Default action is `showsql`.  This parameter is mandatory. |
| `profile_name` | Name of the AI profile. This parameter is optional if an AI profile is already set in the session using `DBMS_CLOUD_AI.SET_PROFILE`.  The default value is NULL.  The following conditions apply:  - If a profile is set in the current session, the user may omit `profile_name` argument in the `DBMS_CLOUD_AI.GENERATE` function. - If the `profile_name` argument is supplied in the `DBMS_CLOUD_AI.GENERATE` function, it overrides any value set in the session using the `DBMS_CLOUD_AI.SET_PROFILE` procedure. - If there is no profile set in the session using the `DBMS_CLOUD_AI.SET_PROFILE` procedure, the `profile_name` argument must be supplied in the `DBMS_CLOUD_AI.GENERATE` function.  Note:  For Database Actions, you can either specify `profile_name` argument in `DBMS_CLOUD_AI.GENERATE` or you can run two steps as a PL/SQL script: `DBMS_CLOUD_AI.SET_PROFILE` and `DBMS_CLOUD_AI.GENERATE`. ```md EXEC DBMS_CLOUD_AI.set_profile('OPENAI');  ----------------------------------------------- SELECT DBMS_CLOUD_AI.GENERATE(prompt => 'how many customers', profile_name => 'OPENAI', action => 'runsql') FROM dual; -----------------------------------------------  SELECT DBMS_CLOUD_AI.GENERATE(prompt => 'how many customers', profile_name => 'OPENAI', action => 'showsql') FROM dual; ----------------------------------------------- SELECT DBMS_CLOUD_AI.GENERATE(prompt => 'how many customers', profile_name => 'OPENAI', action => 'explainsql') FROM dual; ------------------------------------------------ SELECT DBMS_CLOUD_AI.GENERATE(prompt => 'how many customers', profile_name => 'OPENAI', action => 'narrate') FROM dual; ------------------------------------------- SELECT DBMS_CLOUD_AI.GENERATE(prompt => 'what is oracle autonomous database', profile_name => 'OPENAI', action => 'chat') FROM dual; ``` See [Executing SQL Statements in the Code Editor](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SDWAD-GUID-1BE36B0F-4D2B-4CC2-B705-4D8794D8FC8C#GUID-1BE36B0F-4D2B-4CC2-B705-4D8794D8FC8C) for more information. |
| `action` | Action for translating natural prompt using AI. The supported actions include:  - `runsql` (default) - `showsql` - `explainsql` - `narrate` - `summarize` - `translate` - `chat`  Descriptions of actions are included in [Use AI Keyword to Enter Prompts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-B3E0EE68-3B4C-4002-9B45-BBE258A2F15A). |
| `attributes` | Override specific AI profile attributes by supplying attributes in JSON format. See Profile Attributes for more details. |
| `params` | Specify conversation parameter. See CREATE\_CONVERSATION Attributes. You can specify only the following parameter:  `conversation_id`: The default value is the conversation id set in the current session. This is not a mandatory parameter. |

**Examples**

**Example: Using the GENERATE Function for Select AI Actions**

The following examples illustrate `runsql`, `showsql`, `explainsql`, `narrate`, `summarize`, `translate`, and `chat` actions that can be used with the `DBMS_CLOUD_AI.GENERATE` function.

See also [Use AI Keyword to Enter Prompts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-B3E0EE68-3B4C-4002-9B45-BBE258A2F15A) for more details.

An example with `runsql` action is as follows:

```md
SELECT DBMS_CLOUD_AI.GENERATE(prompt       => 'how many customers',
                              profile_name => 'OPENAI',
                              action       => 'runsql')
FROM dual;
```

An example with `showsql` action is as follows:

```md
SELECT DBMS_CLOUD_AI.GENERATE(prompt       => 'how many customers',
                              profile_name => 'OPENAI',
                              action       => 'showsql')
FROM dual;
```

An example with `explainsql` action is as follows:

```md
SELECT DBMS_CLOUD_AI.GENERATE(prompt       => 'how many customers',
                              profile_name => 'OPENAI',
                              action       => 'explainsql')
FROM dual;
```

An example with `narrate` action is as follows:

```md
SELECT DBMS_CLOUD_AI.GENERATE(prompt       => 'how many customers',
                              profile_name => 'OPENAI',
                              action       => 'narrate')
FROM dual;
```

An example with `chat` action is as follows:

```md
SELECT DBMS_CLOUD_AI.GENERATE(prompt       => 'what is oracle autonomous database',
                              profile_name => 'OPENAI',
                              action       => 'chat')
FROM dual;
```

An example with `summarize` action is as follows:

```sql
SELECT DBMS_CLOUD_AI.GENERATE(
                prompt => TO_CLOB(
                            DBMS_CLOUD.GET_OBJECT(
                             credential_name => 'STORE_CRED',
                             object_uri => 'https://objectstorage.ca-toronto-1.oraclecloud.com' ||
                                '/n/namespace-string/b/bucketname/o/data_folder/' ||
                                'summary/test_4000_words.txt')),
                profile_name => 'GENAI_LLAMA',
                action => 'SUMMARIZE')
from DUAL;
```

Result:

```md
The music streaming industry, led by Spotify, has revolutionized the way
people consume music, with streaming accounting for 80% of the American
recording industry's revenue. However, this shift has also complicated the
lives of artists trying to survive in an on-demand, hyper-abundant present.
Spotify's business model, which pays royalties based on an artist's
popularity, has led to concerns about the fairness of the system, with some
artists earning little to no royalties. The company's dominance has also
changed the way people listen to music, with a focus on convenience and
personalized playlists. Liz Pelly's book, "Mood Machine: The Rise of Spotify
and the Costs of the Perfect Playlist," explores the impact of Spotify's rise
on the music industry and listeners, arguing that the platform's emphasis on
affect and mood has led to a homogenization of music and a loss of autonomy
for listeners. As the music industry continues to evolve, questions remain
about the future of music creation and consumption, and whether artists will
be able to thrive in a system that prioritizes convenience and profit over
artistic expression.
```

These examples show `translate` action:

The following examples shows using `translate` action in the prompt.

**Note:** Your AI profile must specify target language.

```md
SELECT DBMS_CLOUD_AI.GENERATE('select ai translate text to be translated')
          FROM dual;
```

The following example shows `translate` action supplied in the `DBMS_CLOUD_AI.GENERATE` function along with `target_language` and `source_language`. This example uses generative AI translation. The input text `this is a document` in English (`source_language: "en"`) is translated into French (`target_language: "fr"`).

```md
DECLARE
         l_attributes  clob := '{"target_language": "fr", "source_language": "en"}';
         output clob;
      BEGIN
         output := DBMS_CLOUD_AI.GENERATE(
                        prompt            => 'this is a document',
                        profile_name      => 'oci_translate',
                        action            => 'translate',
                        attributes        => l_attributes
                     );
      END;
      /
```

**Using the GENERATE Function in a Procedure**

You can use `DBMS_CLOUD_AI.GENERATE` in a procedure and run the function. The following example takes an `ai_prompt`, `profile_name`, and `action` as input parameters and calls `DBMS_CLOUD_AI.GENERATE`

```sql
create or replace FUNCTION call_select_ai (ai_prompt  IN VARCHAR2,
                                           ai_profile IN VARCHAR2,
                                           ai_action  IN VARCHAR2) -- valid for 'chat', 'narrate', 'showsql'
                                           RETURN CLOB AS sai_resp clob;
BEGIN
  sai_resp := DBMS_CLOUD_AI.GENERATE(prompt       => ai_prompt,
                                     profile_name => ai_profile,
                                     action       => ai_action);
  return(sai_resp);
END call_select_ai;
```

**Example: Using the GENERATE Function for Conversations**

The following example shows how to use `DBMS_CLOUD_AI.GENERATE` function in a conversation setting. This example assumes that a conversation has already been created.

```sql
SELECT DBMS_CLOUD_AI.GENERATE(
        prompt       =>  'What is the difference in weather between Seattle and San Francisco?',
        profile_name =>  'GENAI',
        action       =>  'CHAT',
        params       =>  '{"conversation_id":"30C9DB6E-EA4D-AFBA-E063-9C6D46644B92"}') AS RESPONSE;
```

Result:

```md
RESPONSE
--------------------------------------------------------------------------------
Seattle and San Francisco, both located in the Pacific Northwest and Northern
California respectively, experience a mild oceanic climate. However, there are
some notable differences in their weather patterns:

1. **Temperature**: San Francisco tends to be slightly warmer than Seattle,
especially during the summer months. San Francisco's average temperature ranges
from 45?F (7?C) in winter to 67?F (19?C) in summer, while Seattle's average
temperature ranges from 38?F (3?C) in winter to 64?F (18?C) in summer.

2. **Rainfall**: Seattle is known for its rainy reputation, with an average
annual rainfall of around 37 inches (94 cm). San Francisco receives less rainfall,
with an average of around 20 inches (51 cm) per year. However, San Francisco's
rainfall is more concentrated during the winter months, while Seattle's rainfall
is more evenly distributed throughout the year.

......
```

### SET\_PROFILE Procedure

This procedure sets AI profile for current session.

After setting an AI profile for the database session, any SQL statement with the prefix `SELECT AI` is considered a natural language prompt. Depending on the action the you specify with the `AI` prefix, a response is generated using AI. To use the `AI` prefix, see [Examples of Using Select AI](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-8BEF8CA8-D98D-41FB-A819-6C2F862099DC) and [Use AI Keyword to Enter Prompts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-B3E0EE68-3B4C-4002-9B45-BBE258A2F15A). Optionally, it is possible to override the profile attributes or modify attributes by specifying them in JSON format. See SET\_ATTRIBUTE Procedure for setting the attributes.

The AI profile can only be set for current session if the owner of the AI profile is the session user.

To set an AI profile for all sessions of a specific database user or all user sessions in the database, consider using a database event trigger for `AFTER LOGON` event on the specific user or the entire database. See [CREATE TRIGGER Statement](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=LNPLS-GUID-AF9E33F1-64D1-4382-A6A4-EC33C36F237B) for more details.

**Syntax**

```sql
DBMS_CLOUD_AI.SET_PROFILE(
    profile_name      IN  VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `profile_name` | A name for the AI profile in the current session.  This parameter is mandatory. |

**Example**

```sql
BEGIN
     DBMS_CLOUD_AI.SET_PROFILE(
       profile_name    => 'OPENAI'
     );
END;
/
```

### CREATE\_CONVERSATION Procedure

This procedure enables you to create a conversation and automatically set the `conversation_id` within the procedure.

**Note:** If you are using `DBMS_CLOUD_AI.CREATE_CONVERSATION` procedure, you can skip setting the `conversation_id` as the procedure automatically sets it.

**Syntax**

```sql
DBMS_CLOUD_AI.CREATE_CONVERSATION(
  attributes            IN CLOB DEFAULT NULL
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `attributes` | Attributes for conversation in JSON format. See CREATE\_CONVERSATION Attributes for more details.  The default value is NULL. |

**Example**

**Example: Create Conversation**

The following example shows creating a conversation without any customization.

```sql
EXEC DBMS_CLOUD_AI.CREATE_CONVERSATION;
```

Result:

```md
PL/SQL procedure successfully completed.
```

**Example: Create Conversation with Custom Attributes**

The following example shows creating a conversation with custom parameters such as `title`, `description`, `retention_days` and `conversation_length`.

```md
-- Create conversation with custom attributes
SELECT DBMS_CLOUD_AI.CREATE_CONVERSATION(
               attributes => '{"title":"Conversation 1",
                               "description":"this is a description",
                               "retention_days":5,
                               "conversation_length":5}')
     AS conversation_id FROM dual;
```

### CREATE\_CONVERSATION Function

This function creates a conversation and returns its `conversation_id` that can be used in other procedures or functions such as `DBMS_CLOUD_AI.SET_CONVERSATION_ID` and `DBMS_CLOUD_AI.GENERATE`.

Oracle recommends setting `conversation_id` to enable conversation. Alternately, you can set `conversation_id` in the `DBMS_CLOUD_AI.GENERATE` function.

**Note:** If you are using `DBMS_CLOUD_AI.CREATE_CONVERSATION` procedure, you can skip setting the `conversation_id` as the procedure automatically sets it.

**Syntax**

```sql
DBMS_CLOUD_AI.CREATE_CONVERSATION(
  attributes            IN CLOB DEFAULT NULL
) RETURN VARCHAR2;
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `attributes` | Attributes for conversation in JSON format. See CREATE\_CONVERSATION Attributes for more details.  The default value is NULL. |

**Example**

**Example: Create Conversation**

The following example shows using `DBMS_CLOUD_AI.CREATE_CONVERSATION` function to create a conversation without any customization.

```sql
SELECT DBMS_CLOUD_AI.CREATE_CONVERSATION FROM DUAL;
```

Result:

```md
CREATE_CONVERSATION
------------------------------------
30C9DB6E-EA4D-AFBA-E063-9C6D46644B92
```

**Example: Create Conversation with Custom Attributes**

The following example shows using `DBMS_CLOUD_AI.CREATE_CONVERSATION` function to specify attributes such as `title`, `retention_days` and `conversation_length`.

```md
SELECT DBMS_CLOUD_AI.CREATE_CONVERSATION(
                attributes => '{"title":"This is a test conversation",
                               "retention_days":7,
                               "conversation_length":20}')
FROM DUAL;
```

### CREATE\_CONVERSATION Attributes

**Attributes**

| Attribute Name | Default Value | Description |
| --- | --- | --- |
| `title` | New Conversation | The user-assigned name for the conversation. If not provided, Select AI will have the LLM generate one when the conversation is first used with a prompt. |
| `description` | NULL | Provides a user-defined description summarizing the purpose or context of the conversation. If it’s not provided, the LLM generates one when the conversation is first used with a prompt and update it again on the 5th use to include more accurate and relevant information. |
| `retention_days` | 7 | Specify the number of days to retain the conversation history. This is stored in the database from its creation date. If you omit the value, the systems sets it to default value of 7. If you set it to 0, the system retains the conversation until you manually delete it using the `DBMS_CLOUD_AI.DROP_CONVERSATION` procedure or `DBMS_CLOUD.DELETE_ALL_OPERATIONS('CONVERSATION')`. |
| `conversation_length` | NULL | Specify the number of recent prompts and responses to include with the current prompt. The maximum allowed value is 999. You can override this value by specifying the `conversation_length` parameter in the `DBMS_CLOUD_AI.GENERATE` function or by setting it in the AI profile using `SELECT AI `. Apply the following precedence rules for `conversation_length`:  1. Value from the attributes argument in `DBMS_CLOUD_AI.GENERATE` 2. Value set in the conversation takes the next priority 3. Value defined in the AI profile takes the last priority  If none of them specify the `conversation_length`, then the default value is 10. |

The following example shows you how you can customize conversation attributes in the `DBMS_CLOUD_AI.CREATE_CONVERSATION` procedure.

```md
-- Create conversation with custom attributes
SELECT DBMS_CLOUD_AI.CREATE_CONVERSATION(
               attributes => '{"title":"Conversation 1",
                               "description":"this is a description",
                               "retention_days":5,
                               "conversation_length":5}')
     AS conversation_id FROM dual;
```

### UPDATE\_CONVERSATION Procedure

This procedure updates an existing conversation with a specified value of the conversation attributes.

**Syntax**

```md
DBMS_CLOUD_AI.UPDATE_CONVERSATION(
    conversation_id    IN VARCHAR2,
    attributes         IN CLOB
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `conversation_id` | Unique number assigned to a conversation.  This is a mandatory parameter. |
| `attributes` | Attributes for conversation in JSON format. See CREATE\_CONVERSATION Attributes for more details. |

**Example**

```sql
EXEC DBMS_CLOUD_AI.UPDATE_CONVERSATION(
conversation_id => '30C9DB6E-EA4E-AFBA-E063-9C6D46644B92',
attributes => '{"retention_days":20,
        "description":"This a sample description",
        "title":"Sample title",
        "conversation_length":20}');
```

Result:

```md
PL/SQL procedure successfully completed.
```

### SET\_CONVERSATION\_ID Procedure

This procedure sets the current conversation to the specified ID. Subsequent prompts include existing conversation prompts based on the conversation’s configured attributes.

**Syntax**

```sql
DBMS_CLOUD_AI.SET_CONVERSATION_ID(
    conversation_id   IN VARCHAR2
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `conversation_id` | Unique number assigned to a conversation in the current session.  This parameter is mandatory. |

**Example**

```sql
EXEC DBMS_CLOUD_AI.SET_CONVERSATION_ID('30C9DB6E-EA4D-AFBA-E063-9C6D46644B92');
```

Result:

```md
PL/SQL procedure successfully completed.
```

### GET\_CONVERSATION\_ID Function

See CLEAR\_CONVERSATION\_ID Procedure.

**Syntax**

```sql
DBMS_CLOUD_AI.GET_CONVERSATION_ID
RETURN VARCHAR2;
```

**Example**

This example displays the conversation ID set in the current session.

```sql
SELECT DBMS_CLOUD_AI.GET_CONVERSATION_ID FROM DUAL;
```

Result:

```md
--------------------------------------------------------------------------------
30C9DB6E-EA4F-AFBA-E063-9C6D46644B92
```

### CLEAR\_CONVERSATION\_ID Procedure

This procedure clears a conversation ID set in the session to disable the conversation feature for `SELECT AI <ACTION> <PROMPT>`. If you did not set a conversation, the system does not raise any error.

**Syntax**

```sql
DBMS_CLOUD_AI.CLEAR_CONVERSATION_ID;
```

**Example**

This example demonstrates displaying the current conversation ID in the session, clearing the ID, and verifying the change.

```md
-- A conversation id is set in the session
SELECT DBMS_CLOUD_AI.GET_CONVERSATION_ID FROM dual;

GET_CONVERSATION_ID
--------------------------------------------------------------------------------
3A88BFF0-1D7E-B3B8-E063-9C6D46640ECD

-- Clear the conversation id
EXEC DBMS_CLOUD_AI.CLEAR_CONVERSATION_ID;

PL/SQL procedure successfully completed.

-- The conversation id is removed from the session
SELECT DBMS_CLOUD_AI.GET_CONVERSATION_ID FROM dual;

GET_CONVERSATION_ID
--------------------------------------------------------------------------------
```

### DELETE\_CONVERSATION\_PROMPT Procedure

The procedure removes a certain prompt from the conversation.

**Syntax**

```sql
DBMS_CLOUD_AI.DELETE_CONVERSATION_PROMPT(
    conversation_prompt_id  IN VARCHAR2,
    force                   IN BOOLEAN DEFAULT FALSE
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `conversation_prompt_id` | Unique number assigned to a prompt in a conversation. You can find the prompt ID by querying `DBA/USER_CLOUD_AI_CONVERSATION_PROMPTS` view. See [DBMS\_CLOUD\_AI Views](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-5C826A3E-E60B-4D1C-AD0B-E385F6ECEBA5).  This is a mandatory parameter. |
| `force` | If `TRUE`, then the procedure ignores errors if the `conversation_prompt_id` does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
EXEC DBMS_CLOUD_AI.DELETE_CONVERSATION_PROMPT('30C9DB6E-EA61-AFBA-E063-9C6D46644B92');
```

Result:

```md
PL/SQL procedure successfully completed.
```

### DROP\_CONVERSATION Procedure

The procedure removes the conversation and all its associated prompts and the associated responses. Once dropped, the `conversation_id` becomes invalid. If a conversation is dropped while it’s set in the session, it is cleared automatically.

**Syntax**

```sql
DBMS_CLOUD_AI.DROP_CONVERSATION(
    conversation_id  IN VARCHAR2,
    force            IN BOOLEAN  DEFAULT FALSE
);
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `conversation_id` | Unique number assigned to a conversation.  This is a mandatory parameter. |
| `force` | If `TRUE`, then the procedure ignores errors if the `conversation_id` does not exist.  The default value for this parameter is `FALSE`. |

**Example**

```sql
EXEC DBMS_CLOUD_AI.DROP_CONVERSATION('30C9DB6E-EA4D-AFBA-E063-9C6D46644B92');
```

Result:

```md
PL/SQL procedure successfully completed.
```

### SUMMARIZE Function

**Syntax**

```sql
DBMS_CLOUD_AI.SUMMARIZE(
  content         IN  CLOB     DEFAULT NULL,
  credential_name IN  VARCHAR2 DEFAULT NULL,
  location_uri    IN  VARCHAR2 DEFAULT NULL,
  profile_name    IN  VARCHAR2 DEFAULT NULL,
  user_prompt     IN  CLOB     DEFAULT NULL,
  params          IN  CLOB     DEFAULT NULL
) RETURN CLOB;
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `content` | Specifies the text you want to summarize. Either `content` or `location_uri` must be specified.  This is not a mandatory parameter. |
| `credential_name` | Identifies the credential object used to authenticate with the object store. You must create this credential using \`DBMS\_CLOUD.CREATE\_CREDENTIAL\`.  Note:  Use this parameter only when you provide \`location\_uri\`. |
| `location_uri` | Provides the URI where the text is stored or the path to a local file. Either `content` or `location_uri` must be specified.  For example:  Object storage: `https://objectstorage.ca-toronto-1.oraclecloud.com/n/namespace-string/b/bucketname/o/data_folder/summary/test_file.txt`  Local file: `summary_gobject:test_file.txt` |
| `profile_name` | Specifies the AI profile to use. If you do not provide a `profile_name`, Select AI uses the default profile set in the session. If no default profile is set, it returns the error: ORA-20046: AI profile is not enabled in the session.  The default value is NULL. |
| `user_prompt` | Supplies a natural language prompt to guide or customize the summary. You can include additional instructions beyond summary parameters.  For example, The summary should start with ''The summary of the article is: '''  This parameter is not mandatory. |
| `params` | Defines summarization parameters. See SUMMARIZE Parameters. |

**Example**

See [Example: Select AI Summarize](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-22D738E1-BC06-47F0-9684-CD698DD8C492) to explore.

### SUMMARIZE Parameters

**Attributes**

| Attribute Name | Default Value | Description |
| --- | --- | --- |
| `min_words` | 0 | Specifies the approximate minimum number of words the generated summary is expected to contain.  Note:  This parameter acts as a guideline rather than a strict limit: the actual length of the summary may vary depending on the content provided and the model's interpretation. |
| `max_words` | 200 | Specifies the approximate maximum number of words the generated summary is expected to contain.  Note:  This parameter acts as a guideline rather than a strict limit, the actual length of the summary may vary depending on the content provided and the model's interpretation. |
| `summary_style` | Paragraph | Specifies the format style for the summary. The following are the available summary format options:  - `paragraph`: the summary is presented in one or more paragraphs. - `list`: the summary is a list of key points from the text. |
| `chunk_processing_method` | `map_reduce` | When the text exceeds the token limit that the LLM can process, it must be split into manageable chunks. This parameter enables you to choose the method for processing these chunks. The following options are provided:  - `iterative_refinement`. See [Iterative Refinement](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-CCBDA0E8-3B91-4264-9A2B-8690CA10B95A) for more details. - `map_reduce`. See [Map Reduce](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-95DC8B91-DE34-4434-9A2C-D1B4901C6D50) for more details. |
| `extractiveness_level` | `low` | Determines how closely the summary follows the original wording of the input. It controls the degree to which the model extracts versus rephrases it. The following are the options: - `High`: The summary stays close to the original phrasing, reusing sentences and expressions where possible. - `Medium`: A balanced mix of extraction and paraphrasing. - `Low`: Allows more freedom to reword, restructure, or simplify the input, focusing on meaning rather than exact phrasing.  Note:  This setting serves as guidance for the model's summarization behavior, it does not enforce a strict rule. The actual style and wording of the summary may vary based on the input content and model decisions. |

### TRANSLATE Function

You can supply the `source_language` and the `target_language` parameters in the function or they can be taken from the user’s AI profile. If your AI profile does not include a `source_language` attribute, the generative AI provider automatically detects the input language. If the `target_language` attribute is missing, Select AI returns an error.

**Syntax**

```sql
DBMS_CLOUD_AI.TRANSLATE(
   profile_name      IN VARCHAR2,
   text              IN CLOB,
   source_language   IN VARCHAR2 DEFAULT NULL,
   target_language   IN VARCHAR2 DEFAULT NULL
) RETURN CLOB;
```

**Parameters**

| Parameter | Description |
| --- | --- |
| `profile_name` | Specifies the AI profile to use.  This is not a mandatory parameter. |
| `text` | Specifies the text you want to translate.  This is a mandatory parameter. |
| `source_language` | Language of the input text |
| `target_language` | Language into which the text is translated. |

**Example**

See [Example: Select AI Translate](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-8EA7C9C8-E449-4961-9746-D537E00547F2) to explore.

### GENERATE\_SYNTHETIC\_DATA Function

The following is the syntax to generate synthetic data for a single table.

**Syntax**

```sql
DBMS_CLOUD_AI.GENERATE_SYNTHETIC_DATA(
  profile_name        IN  VARCHAR2,
  object_name         IN  DBMS_ID,
  owner_name          IN  DBMS_ID,
  record_count        IN  NUMBER,
  user_prompt         IN  CLOB DEFAULT NULL,
  params              IN  CLOB DEFAULT NULL
);
```

The following is the syntax to generate synthetic data for multiple tables.

```md
DBMS_CLOUD_AI.GENERATE_SYNTHETIC_DATA(
  profile_name        IN  VARCHAR2,
  object_list         IN  CLOB,
  params              IN  CLOB DEFAULT NULL
);
```

If you do not want table data or vector search documents to be sent to an LLM, a user with administrator privileges can disable such access for all users of the given database. This, in effect, disables the `narrate` action.

**Parameters** {#GUID-AA65C99D-600E-4216-AFAE-26AE9DE972F1}

| Parameter | Mandatory | Description |
| --- | --- | --- |
| `profile_name` | Yes | The AI profile containing necessary LLM service information. This can be created by CREATE\_PROFILE Procedure. |
| `object_name` | Yes | Specify a table name to populate synthetic data. - `SELECT` and `INSERT` privilege on the table objects are needed for the user using it. - The table is either empty or have records in it. |
| `owner_name` | No | Specify the database user who owns the referenced object. If no specific owner is provided, the procedure defaults to using the schema of the user running it. |
| `record_count` | No | The number of records to be synthetically generated. |
| `user_prompt` | No | Additional information that a user can mention to generate synthetic data. For example, to generate a record for a table called `MOVIE` with a `release_date` column, the `user_prompt` can be: *the release date for the movies should be in 2019* |
| `params` | No | Optional attributes provided in JSON object string format to modify the behavior of an API. See Optional Parameters. |
| `object_list` | Yes | Use this parameter for generating synthetic data on multiple tables. This parameter takes in table object information along with it’s arguments and contains the same arguments provided in the single table. See object\_list Parameters. |

**Optional Parameters** {#GUID-6663C43D-AC55-4B5B-A6AE-529012A63A9A}

| Parameter | Value Datatype | Value | Description |
| --- | --- | --- | --- |
| `sample_rows` | Number | `0 <= sample_rows <= 100` | Specify the number of rows from the table to use as a sample to guide the LLM in data generation.  A value of 0 means no sample rows will be used. The default value is `0`. |
| `table_statistics` | Boolean | - `True` - `False` | Enable or disable the use of table statistics information.  The default value is `False`. |
| `priority` | String | Valid values:  - `HIGH` - `MEDIUM` - `LOW` | Assign a priority value that defines the number of parallel requests sent to the LLM for generating synthetic data. Tasks with a higher priority will consume more database resources and complete faster.  The default value is `HIGH`  - `HIGH`: Specifies the number of parallel LLM requests based on the database's ECPU count (or OCPU count if your database uses OCPUs). - `MEDIUM`: Sets the number of concurrent processes according to the concurrency limit for Medium service. The default value is 4. - `LOW`: Runs the pipeline job in a serial order, without parallel processing.  The maximum number of concurrent parallel processes used for synthetic data generation is limited to 64. |
| `comments` | Boolean | - `True` - `False` | Enable or disable sending comments to the LLM to guide data generation.  The default value is `False`. |

**object\_list Parameters** {#GUID-4CEDCBD1-8116-4307-93C1-DD15CAC92275}

| Parameter | Value Datatype | Mandatory | Description |
| --- | --- | --- | --- |
| `owner` | String | Yes | Specifies the database user who owns the object being referenced. If no specific owner is provided, the procedure will default to using the schema of the user running it. |
| `name` | String | No | Specify a table name to populate synthetic data. `SELECT` and `INSERT` privilege on the table objects are needed for the user using it.The table is either empty or have records in it. |
| `record_count` | Number | No | The number of records to be synthetically generated. Provide a number greater than 0.  Supply `record_count` or `record_count_percentage`. |
| `record_count_percentage` | Number | No | The percentage of number of records to be synthetically generated. Provide a number greater than 0.  For a Metadata Clone database, where the table metadata including statistics is preserved, the `record_count_percentage` parameter is supported.  Supply `record_count` or `record_count_percentage`.  When using the `record_count_percentage` parameter, the final record count in the table is calculated as:  ```md Original_Num_Rows * record_count_percentage ``` |
| `user_prompt` | String | No | Same as `user_prompt` in Parameters. The `user_prompt` is associated with a specific table object. |

**Examples**

The following examples show the `DBMS_CLOUD_AI.GENERATE_SYNTHETIC_DATA` function for generating synthetic data for a single table and multiple tables. For a complete example and to view more examples, see [Example: Generate Synthetic Data](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=ADBSB-GUID-9990ACE7-BCEF-4597-8FA6-CFD6D834B510).

```sql
BEGIN
    DBMS_CLOUD_AI.GENERATE_SYNTHETIC_DATA(
        profile_name => 'GENAI',
        object_name  => 'Director',
        owner_name   => 'ADB_USER',
        record_count => 5
    );
END;
/
PL/SQL procedure successfully completed.
```
```sql
BEGIN
    DBMS_CLOUD_AI.GENERATE_SYNTHETIC_DATA(
        profile_name => 'GENAI',
        object_list => '[{"owner": "ADB_USER", "name": "Director","record_count":5},
                         {"owner": "ADB_USER", "name": "Movie_Actor","record_count":5},
                         {"owner": "ADB_USER", "name": "Actor","record_count":10},
                         {"owner": "ADB_USER", "name": "Movie","record_count":5,"user_prompt":"all movies are released in 2009"}]'
    );
END;
/
PL/SQL procedure successfully completed.
```

### ENABLE\_DATA\_ACCESS Procedure

This procedure enables sending data to LLM for applicable Select AI features, which is the default behavior. Only an administrator can run this procedure.

This procedure controls data access for the following Select AI capabilities:

- `narrate` action
- Retrieval Augmented Generation (RAG)
- Synthetic Data Generation

**Syntax**

```sql
DBMS_CLOUD_AI.ENABLE_DATA_ACCESS();
```

**Parameters**

This procedure does not require any parameters.

**Example to Enable Data Access**

```sql
BEGIN
  DBMS_CLOUD_AI.ENABLE_DATA_ACCESS();
END;
/
```

### DISABLE\_DATA\_ACCESS Procedure

This procedure disables sending data to LLM for applicable Select AI features. Only an administrator can run this procedure.

This procedure limits the following Select AI capabilities:

- `narrate` action
- Retrieval Augmented Generation (RAG)
- Synthetic Data Generation

**Syntax**

```sql
DBMS_CLOUD_AI.DISABLE_DATA_ACCESS();
```

**Parameters**

This procedure does not require any parameters.

**Example to Disable Data Access**

```sql
BEGIN
  DBMS_CLOUD_AI.DISABLE_DATA_ACCESS();
END;
/
```