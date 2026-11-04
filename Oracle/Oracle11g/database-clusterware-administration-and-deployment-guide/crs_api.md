---
title: Oracle Clusterware C Application Program Interfaces
book: Database Clusterware Administration and Deployment Guide
doc_id: E41959-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41959/crs_api.htm
tags:
  - oracle
  - 11g
  - database-clusterware-administration-and-deployment-guide
---

## F Oracle Clusterware C Application Program Interfaces

This appendix describes the Oracle Clusterware C application program interfaces (APIs). This appendix contains the following topics:

See Also:

[Chapter 6, "Making Applications Highly Available Using Oracle Clusterware"](crschp.md) for detailed information about using Oracle Clusterware to make applications highly available

## About the Programming Interface (C API) to Oracle Clusterware

This section contains information about using the programming interface (C API) to Oracle Clusterware (CLSCRS.

Overview

CLSCRS is a set of C-based APIs for Oracle Clusterware. The CLSCRS APIs enable you to manage the operation of entities that are managed by Oracle Clusterware. These entities include resources, resource types, servers, and server pools. You use the APIs to register user applications with Oracle Clusterware so that the clusterware can manage them and maintain high availability. Once an application is registered, you can manage it and query the application's status. If you no longer need the application, then you can stop it and unregister it from Oracle Clusterware.

Oracle Clusterware services are provided by Cluster Ready Services that runs as part of Oracle Clusterware. The CLSCRS API uses a context that is explicitly named in all function calls. The API does not store anything at the process or thread level. You can use the callbacks for diagnostic logging.

Note:

You can install the Oracle Clusterware high availability API from the Oracle Database client installation media.

Operational Notes

This section includes the following topics:

- Context Initialization and Persistence
- Threading Support
- CLSCRS API Data Structures
- Memory Management
- Error Handling and Tracing
- Callback Mechanism
- Filters
- Script Agent Usage
- Help Interface

Context Initialization and Persistence

To use the CLSCRS APIs, you must first initialize the `clscrs` context. The calls to create and terminate this context are:

- `clscrs_init_crs`: Initializes the `clscrs` context
- `clscrs_term_crs`: Terminates the `clscrs` context

The caller is responsible for terminating the context when it is no longer needed.

Threading Support

If initialized with the `CLSCRS_FLAG_USETHREADS` flag, then the CLSCRS API may spawn threads internally. Every API function executes in the context of the calling thread. The API context object may not be used concurrently by multiple threads. However, no thread-affinity on the part of the client is required. A process may create multiple API contexts and use those on different threads, subject to the one-thread-per-one-context-at-a-time rule.

CLSCRS API Data Structures

The following entities are passed into the API calls and contain return values from the API call:

- `clscrs_sp`: A stringpair (`sp`) contains a name and a value string. The value can be NULL. It is created and destroyed, and its contents can be examined and the value replaced. A stringpair can be a member of exactly one stringpair list (`splist`).
- `clscrs_splist`: A stringpair list (`splist`) is a list of zero or more stringpairs used in various contexts. An API can add stringpairs to or remove them from a stringpair list, or the API can iterate stringpairs.
- `clscrs_res`: A resource instance (`res`) represents an Oracle Clusterware entity, which contains the name and additional data appropriate to the context in which the Oracle Clusterware entity is used. Sometimes a resource instance contains Oracle Clusterware entity attribute data and other times it carries status and return messages about an operation. A single resource instance can be a member of exactly one `clscrs_reslist`.
- `clscrs_reslist`: A resource list (`reslist`) is a data structure that contains zero or more instances of `clscrs_res`. An API can add resources to or remove them from a resource list, or the API can iterate resources.

Memory Management

The CLSCRS APIs work on elements and lists. The elements are added to lists. The memory for both elements and lists is allocated and released through explicit API calls. It is the caller's responsibility to release the memory that they allocate. However, when elements are added to lists, only the list must be destroyed: the destruction of the list destroys its elements implicitly. The elements must be destroyed when they are not added to any list. For recursive lists, destroying the parent list also destroys any lists contained within it. The `clscrs_sp` and `clscrs_res` elements must be destroyed by the caller. If they are part of a `clscrs_splist` or `clscrs_reslist`, destroying the list destroys the respective `clscrs_sp` and `clscrs_res` entities.

For example, when a resource is created and added to a resource list, only the resource list must be destroyed, but not the individual resource. Destroying the resource list releases the memory for the individual resource, too.

Memory is allocated by the API through the following calls:

```
clscrs_sp_create()
clscrs_res_create()
clscrs_serverpool_create()
clscrs_type_create()
clscrs_splist_create()
clscrs_reslist_create()
clscrs_entity_id_create()
```

Each of the calls in the preceding list has a corresponding `clscrs_*_destroy()` call.

Error Handling and Tracing

Interactive and non-interactive CLSCRS APIs each use a different error-handling mechanism.

For non-interactive CLSCRS APIs, the error code is returned as the return value of the function call. For example:

```
clscrsret clscrs_sp_get_value(clscrs_sp *sp, oratext **value);
```

The error code is returned as a `clscrsret` value.

For interactive CLSCRS APIs, the output result is represented, as follows:

1. The return value of the function call provides a high-level output of the request. Did the request reach the server? Was it completely successful, or completely or only partially unsuccessful? A successful return value means the request was received, processed, and the outcome was successful for all entities requested.
2. For each entity on which the request operated, there is a programmatic completion code stored in the `op_status` list. If the value is not `success`, it indicates the high-level type of the problem specific to processing the request for the particular object.
3. Optionally, the API might indicate that it wants to receive localized, human-readable error, warning, or status messages by using the callback mechanism. Each invocation of the callback provides the message, message type (severity), and the ID of the object to which the callback invocation pertains.

For example:

```
CLSCRS_STAT clscrs_register_resource2(clscrs_reslist *in_reslist, uword flags,
                                       clscrs_msgf2 msgf, void *msgarg,
                                       clscrs_reslist *op_status);
```
1. The function returns an error code of value `CLSCRS_STAT`.
2. The `crsd` sends error messages, warning messages, and progress messages back to the client through the `clscrs_msgf2` callback. The client must implement the callback to process these messages returned by the `crsd`.
3. In previous Oracle Clusterware releases, the API also contained results of each operation on the Oracle Clusterware entities as part of the `op_status` list. You can access that information using the following API:
	```
	clscrsret clscrs_res_get_op_status(clscrs_res *res, CLSCRS_STAT *status,
	                                    oratext **msg);
	```
	The `status` argument contains a status code about the `crsd` operation on the Oracle Clusterware entity. Additionally, the `msg` argument contains a message from the `crsd` about the result of the operation. Though the `op_status` list continues to contain the results of the `crsd` operation for each Oracle Clusterware entity in the `msg` argument, usage of the `msg` argument to get the error codes and messages has now been deprecated and is not supported for any use of the API on a new entity. Only pre-existing use cases (for acting on resources, specifically) are supported. Use the callback function to process any messages returned by the `crsd`.

Callback Mechanism

Interactive CLSCRS APIs provide a callback mechanism that the clients can use to process error messages, warning messages, and progress messages sent by the `crsd`.

The signature of the callback mechanism is:

```
typedef  void (*clscrs_msgf2)(void *usrp, const oratext *id, const oratext *msg,
                clscrs_msgtype msgtype);
```

In the preceding syntax:

- `usrp`: Is a user-supplied pointer that probably contains the context of the call
- `id`: Is the identifier of the entity to which the message corresponds
- `msg`: Is the output text
- `msgtype`: Is the type of the message; either error, warning, or progress

Example F-1 describes an example of the callback mechanism.

Example F-1 Callback Mechanism

```
void myCallback(void *arg, const oratext *pId, const oratext *pMsg,
                clscrs_msgtype msgType)
{
    if (pMsg != NULL)
   {
       cout << pMsg << endl;
    }
}
```

Example F-2 describes how to use the callback mechanism in an interactive API.

Example F-2 Using the Callback Mechanism In an Interactive API

```
clscrs_start_resource2(pResIdList, NULL,
                       env, myCallback, NULL,
                       0, pOpStatus);
```

You can also print debug trace messages for the API, itself by passing the `CLSCRS_FLAG_TRACE` flag when creating the context. The signature for context creation is:

```
CLSCRS_STAT clscrs_init_crs(clscrs_ctx **ctx, clscrs_msgf2 errf, void *errCtx,
                             ub4 flags);
```

For the trace messages to work, you must specify both the `CLSCRS_FLAG_TRACE` flag and a `clscrs_msgf2` callback mechanism in the `clscrs_init_crs` API.

The `clscrs_msgf2` callback mechanism has the following signature:

```
typedef  void (*clscrs_msgf)(void *usrp, const oratext *msg, sword msglen);
```

Filters

You can use filters to narrow down Oracle Clusterware entities upon which a CLSCRS API operates. Simple filters are attribute-value pairs with an operator. Operators must be surrounded by spaces, as shown in the examples. You can combine simple filters into expressions called expression filters using Boolean operators.

Supported filter operators are:

  
`=`  
`>`  
`<`  
`!=`  
`co`: Contains  
`st`: Starts with  
`en`: Ends with  

Supported Boolean operators are `AND` and `OR`.

Examples of filters are:

- `TYPE = type1`
- `((TYPE = type1) AND (CHECK_INTERVAL > 50))`
- `(TYPE = type1) AND ((CHECK_INTERVAL > 30) OR (AUTO_START co never))`
- `NAME en network.res`
- `TYPE st ora.db`

See Also:

Use the `clscrs_comparator enum` and the `clscrs_operator enum` located in the `$ORA_CRS_HOME/crs/demo/clscrsx.h` file to get the correct type for the above comparators and operators, respectively, in the API calls

There are two types of filters and CLSCRS has a set of APIs to create these filters:

- Comparison filter: A simple filter that compares two values. For example:
	```
	TYPE = ora.db.type
	```
	Use the `clscrs_compfilter_create` API to create a comparison filter. For example, to create the `(TYPE = ora.db.type)` comparison filter:
	```
	clscrs_compfilter_create(ctx, clscrs_TYPE,
	                    clscrs_comparator_eq, (const oratext *)"ora.db.type",
	                    &myCompFilter);
	```
- Expression filter: A filter that is created from either a set of comparison filters or expression filters, or both. For example:
	```
	((TYPE = ora.db.type) AND (CHECK_INTERVAL > 50))
	```
	Use the `clscrs_expfilter_create` API to create a comparison filter. For example, to create an expression filter:
	```
	clscrs_exprfilter_create(myCompFilter1, clscrs_operator_or,
	                          myCompFilter2, &myExprFilter);
	```

See Also:

The `$ORA_CRS_HOME/crs/demo/clscrsx.h` file for usage information for the `clscrs_compfilter_create` and `clscrs_expfilter_create` APIs

Note:

Both the `clscrs_compfilter_create` and `clscrs_expfilter_create` APIs allocate memory that must be freed by calling `clscrs_filter_destroy()`.

You can use filters in the following interactive CLSCRS APIs in place of an entity list:

  
`clscrs_start_resource2`  
`clscrs_stat2`  
`clscrs_stop_resource2`  
`clscrs_check_resource2`  
`clscrs_relocate_resource2`  

Example F-3 describes using filters in an interactive CLSCRS API.

Example F-3 Filters In an Interactive CLSCRS API

```
clscrs_start_resource2(myCompFilter, NULL,
                       env, msgf2, NULL,
                       0, pOpStatus);
```

Script Agent Usage

When you use CLSCRS APIs inside script agent entry points, keep the following in mind:

1. Some actions, such as start, stop, and clean, are executed under a lock on the resource instance. Thus, issuing a request to the server to act on the resource directly or by extension of a relation results in a dead-lock.
2. Issuing read-only (`clscrs_stat2`) is generally safe unless it is an initial check, where the script agent must not call back on the server, because that results in a dead-lock, as well. Use the `clsagfw` APIs to query the check entry point.

See Also:

[Appendix B, "Oracle Clusterware Resource Reference"](resatt.md) for examples of script agents

Help Interface

You can find the entire list of CLSCRS APIs, including usage information for each, in the `$ORA_CRS_HOME/crs/demo/clscrsx.h` file, along with a demo called `crsapp.c`.

Deprecated CLSCRS APIs

Table F-1 lists the deprecated CLSCRS APIs and the corresponding new APIs for Oracle Clusterware 11g release 2 (11.2).

Table F-1 Deprecated CLSCRS APIs

| Deprecated Command | Replacement |
| --- | --- |
| ``` clscrs_register_resource ``` | ``` clscrs_register_resource2 ``` |
| ``` clscrs_start_resource ``` | ``` clscrs_start_resource2 ``` |
| ``` clscrs_stat ``` | ``` clscrs_stat2 ``` |
| ``` clscrs_stop_resource ``` | ``` clscrs_stop_resource2 ``` |
| ``` clscrs_check_resource ``` | ``` clscrs_check_resource2 ``` |
| ``` clscrs_relocate_resource ``` | ``` clscrs_relocate_resource2 ``` |
| ``` clscrs_unregister_resource ``` | ``` clscrs_unregister_resource2 ``` |
| ``` clscrs_msgf ``` | ``` clscrs_msgf2 ``` |
| ``` clscrs_fail_resource ``` | No replacement. |

## Interactive CLSCRS APIs

The APIs listed in Table F-2 make calls to the Cluster Ready Services daemon (`crsd`) to run commands. The `crsd` must be up and running for these APIs to function.

Table F-2 Summary of Interactive CLSCRS APIs for Oracle Clusterware

| C API | Description |
| --- | --- |
| ``` clscrs_register_type ``` | Registers the resource types in the input resource list. |
| ``` clscrs_register_serverpool ``` | Registers a server pool for the input list of servers. |
| ``` clscrs_register_resource2 ``` | Registers the resources in the input resource list. |
| ``` clscrs_start_resource2 ``` | Notifies Oracle Clusterware to start a named set of resources. |
| ``` clscrs_stat2 ``` | Obtains information about the entities identified in rqlist. |
| ``` clscrs_stop_resource2 ``` | Notifies Oracle Clusterware to stop a named set of resources. |
| ``` clscrs_check_resource2 ``` | Notifies Oracle Clusterware to run the check entry points for the identified resources. |
| ``` clscrs_relocate_resource2 ``` | Relocates the list of resource identifiers. |
| ``` clscrs_unregister_resource2 ``` | Unregisters the resources in the input list of resource names. |
| ``` clscrs_unregister_type ``` | Unregisters the resource types in the input list. |
| ``` clscrs_unregister_serverpool ``` | Unregisters the given server pool. |
| ``` clscrs_relocate_server ``` | Relocates a list of servers. |

## Non-Interactive CLSCRS APIs

You can use non-interactive CLSCRS APIs for functions such as context initialization, preparing request payloads for interactive APIs, and post-processing output of the interactive APIs. The non-interactive CLSCRS APIs do not call `crsd`.

A callback error reporting mechanism is not available for the non-interactive CLSCRS APIs. All interactive CLSCRS APIs, except, `clscrs_stat2`, use this callback mechanism. Clients of these APIs also use the callback mechanism to receive error, warning, and progress messages from the `crsd`.

You can also use filters to reduce the list of CRS entities. You can also use filters in the interactive APIs to reduce the list of CRS entities.

Thread Safety

The routines provided to manage API data structures cannot be used with the same API context in multiple threads concurrently; however, no thread-affinity on the part of the client is required. A process may invoke these routines on multiple threads provided that a separate API context is used in each instance.

See Also:

"Error Handling and Tracing", "Callback Mechanism", and "Filters" for more information

Table F-3 describes the non-interactive CLSCRS APIs.

Table F-3 Non-Interactive CLSCRS APIs

| C API | Description |
| --- | --- |
| ``` clscrs_entity_id_destroy ``` | Frees the memory associated with an entity identifier created from `clscrs_entity_id_create()`. |
| ``` clscrs_exprfilter_create ``` | Constructs an expression filter from comparison and/or expression filters. |
| ``` clscrs_filter_destroy ``` | Frees the memory for a filter. |
| ``` clscrs_get_entity_type ``` | Obtains the entity type corresponding to the entity identifier provided. |
| ``` clscrs_get_fixed_attrlist ``` | Obtains the list of attributes that correspond to an attribute group identifier. |
| ``` clscrs_get_resource_instance_details ``` | Obtains the resource instance details, such as resource name, cardinality, and degree, from the resource instance identifier that is used. |
| ``` clscrs_getnodename ``` | Obtains the node name. |
| ``` clscrs_init_crs ``` | Initializes a context for communications with Oracle Clusterware. |
| ``` clscrs_is_crs_admin ``` | Checks whether the user is an Oracle Clusterware administrator. |
| ``` clscrs_res_attr_count ``` | Obtains the number of attributes for a resource. |
| ``` clscrs_res_create ``` | Creates a new resource. |
| ``` clscrs_res_destroy ``` | Frees the memory for a resource. |
| ``` clscrs_res_get_attr ``` | Obtains a resource attribute for a resource. |
| ``` clscrs_res_get_attr_list ``` | Obtains the attribute list for a resource. |
| ``` clscrs_res_get_name ``` | Obtains the name of a resource. |
| ``` clscrs_res_get_op_status ``` | Obtains the status of an operation for an entity. |
| ``` clscrs_res_get_registered ``` | Obtains the registration status of a resource. |
| ``` clscrs_res_get_reslist ``` | Obtains the resource list for a resource. |
| ``` clscrs_res_set_attr_list ``` | Sets the attribute list for a resource. |
| ``` clscrs_res_set_reslist ``` | Sets the resource list for a resource. |
| ``` clscrs_reslist_append ``` | Adds a resource to a resource list. |
| ``` clscrs_reslist_count ``` | Counts the number of resources in a resource list. |
| ``` clscrs_reslist_create ``` | Creates a new resource list. |
| ``` clscrs_reslist_delete_res ``` | Deletes a resource from a resource list. |
| ``` clscrs_reslist_destroy ``` | Frees the memory for a resource list. |
| ``` clscrs_reslist_find ``` | Finds a resource in a resource list. |
| ``` clscrs_reslist_first ``` | Obtains the first resource on a resource list. |
| ``` clscrs_reslist_next ``` | Obtains the current next resource from the resource list. |
| ``` clscrs_sp_get ``` | Obtains the name and value components of a stringpair. |
| ``` clscrs_sp_set ``` | Changes the value part of a stringpair. |
| ``` clscrs_splist_append ``` | Adds a new stringpair (sp) to a stringpair list (splist). |
| ``` clscrs_splist_create ``` | Creates a new stringpair list. |
| ``` clscrs_splist_delete_sp ``` | Deletes a stringpair (sp) from a stringpair list (splist). |
| ``` clscrs_splist_first ``` | Obtains the first stringpair (sp) from a stringpair list (splist). |
| ``` clscrs_splist_replace ``` | Replaces the value for a stringpair (sp) in a stringpair list (splist). |
| ``` clscrs_term_crs ``` | Releases a context for communications with CRS. |
| ``` clscrs_type_create ``` | Creates a new resource type. |
| ``` clscrs_type_get_attr ``` | Obtains the value/properties of a resource type attribute. |
| ``` clscrs_type_set_attr ``` | Adds an attribute to a resource type. |
| ``` clscrs_compfilter_create ``` | Constructs a simple filter that compares two values. |
| ``` clscrs_entity_id_create ``` | Creates an entity identifier that identifies a CRS entity such as a resource, resource type, server group, and so on. |
| ``` clscrs_register_serverpool ``` | Registers a server pool for the input list of servers. |
| ``` clscrs_register_type ``` | Registers the resource types in the input resource list. |
| ``` clscrs_relocate_server ``` | Relocates a list of servers. |
| ``` clscrs_res_get_node_list ``` | Obtains the nodelist currently hosting the resource. |
| ``` clscrs_res_set_attr ``` | Sets a resource attribute for a resource. |
| ``` clscrs_sp_get_value ``` | Obtains the value component of a stringpair. |
| ``` clscrs_splist_count ``` | Counts the number of stringpairs (sp) in a stringpair list (splist). |
| ``` clscrs_splist_create_and_set ``` | Creates a new stringpair list (splist) and set the name and value for the first stringpair in the list. |
| ``` clscrs_splist_destroy ``` | Frees the memory for a stringpair list (splist). |
| ``` clscrs_splist_find ``` | Finds the value for a stringpair (sp) in a stringpair list (splist). |
| ``` clscrs_splist_next ``` | Obtains the current next stringpair (sp) from a stringpair list (splist). Current next SP is effectively the next SP in the SPLIST. The list iterator is stored within the API and is not exposed. |
| ``` clscrs_stat2 ``` | Obtains information about the entities identified in rqlist. |