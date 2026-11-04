---
title: Introducing Analytic Workspace Manager Plug-ins
book: OLAP Customizing Analytic Workspace Manager
doc_id: E17237-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/olap.112/e17237/pluginintro.htm
tags:
  - oracle
  - 11g
  - olap-customizing-analytic-workspace-manager
---

## 2 Introducing Analytic Workspace Manager Plug-ins

An Analytic Workspace Manager plug-in enables you to run Java code in the context of Analytic Workspace Manager. With an implementation of a Java plug-in interface that is supported by Oracle Analytic Workspace Manager, Version 11.2, you can extend the functionality of Analytic Workspace Manager in Oracle Database 11g Release 2 (11.2) with the OLAP option.

This chapter has the following topics.

## Describing Analytic Workspace Manager Plug-ins

Analytic Workspace Manager has the following Java plug-in interfaces.

- `AWMPlugin`, which you can use to add selections to the right-click menu of a navigation tree object.
- `ViewerPlugin`, which you can use to display information in the property inspector about the current navigation tree object.
- `EditorPlugin`, which extends `ViewerPlugin` and adds the ability to edit properties of the object.

With an Analytic Workspace Manager plug-in, you can implement programs that perform actions such as the following:

- Create new types of calculations.
- Create forecasts.
- Create custom OLAP metadata objects, such as an enterprise-specific time dimension.
- Control the display in the property inspector of the information associated with a custom navigation tree object.
- Edit the properties of an object in the property inspector.

In an Analytic Workspace Manager plug-in, you can use the following Java APIs:

- Oracle OLAP Java API
- JDBC API
- Swing API

You can invoke OLAP DML or SQL procedures by using JDBC classes.

### Enabling Analytic Workspace Manager Plug-ins

Analytic Workspace Manager has a configuration option that specifies whether it uses plug-ins. To enable plug-ins, from the Analytic Workspace Manager Tools menu, select Configuration, as shown in Figure 2-1. In the Configuration dialog box, select Enable Plugins and specify the directory that contains your plug-ins, as shown in Figure 2-2. Click OK and then exit and restart Analytic Workspace Manager.

Figure 2-1 Configuration Item on the Tools Menu

![Description of Figure 2-1 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/awmtools.gif "Description of Figure 2-1 follows")  
[Description of "Figure 2-1 Configuration Item on the Tools Menu"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/awmtools.htm)  

Figure 2-2 shows the Configuration dialog box with Enable plugins selected and with `plugin` as the value for Plugin directory. The value should include the full path to the plug-in directory unless the directory is a subdirectory of the `Oracle_home` `/olap/awm` directory, which is the case for the `plugin` directory shown in the figure.

Figure 2-2 Configuration Dialog Box with Enable Plugins Selected

![Description of Figure 2-2 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/awmconfig.gif "Description of Figure 2-2 follows")  
[Description of "Figure 2-2 Configuration Dialog Box with Enable Plugins Selected"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/awmconfig.htm)  

### How Analytic Workspace Manager Calls a Plug-in

If Analytic Workspace Manager has plug-ins enabled, then on startup Analytic Workspace Manager dynamically loads Java code from JAR files located in the plug-ins directory. After loading the contents of the JAR files, Analytic Workspace Manager looks for classes that implement the `AWMPlugin`, `ViewerPlugin`, or `EditorPlugin` interfaces. It also looks for `aw.xml`, `cube.xml`, `dimension.xml`, and `schema.xml` files to add objects to the navigation tree.

Note:

You can include multiple plug-ins and XML documents in a single JAR file.

When Analytic Workspace Manager calls most methods of a plug-in, it passes the method a `java.sql.Connection` object as the `conn` parameter. The `Connection` represents the current connection to the Oracle Database instance.

Analytic Workspace Manager does not pass any user identification or password to the plug-in. It only passes the connection object. An Analytic Workspace Manager plug-in does not allow you to do anything that you cannot do by writing a standalone Java program. For information on the parameters that Analytic Workspace Manager passes to the methods of plug-ins, see "Describing the AWMPlugin Interface" and "Describing the ViewerPlugin and EditorPlugin Interfaces".

#### Calling an AWMPlugin

When a user right-clicks an object in the Analytic Workspace Manager navigation tree, a menu appears that presents the actions available for the object. The menu also displays options supplied by the `AWMPlugin` plug-ins that apply to the object. An `AWMPlugin` uses the `isSupported` method to indicate whether it applies to an object in the tree. Because Analytic Workspace Manager calls the `isSupported` method of each plug-in whenever the user right-clicks a navigation tree object, an `isSupported` method should return quickly.

The menu displays the text returned by the `getMenu` method of the plug-in. Figure 2-3 shows the menu that Analytic Workspace Manager displays when a user right-clicks a calculated measure in the tree. The menu includes the `ViewXMLPlugin` example plug-in. For the code of the plug-in example, see [Example 3-1](pluginexamples.md).

Figure 2-3 Right-click Menu of the Navigation Tree for a Calculated Measure

![Description of Figure 2-3 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/navtree.gif "Description of Figure 2-3 follows")  
[Description of "Figure 2-3 Right-click Menu of the Navigation Tree for a Calculated Measure"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/navtree.htm)  

If the user selects the plug-in, then Analytic Workspace Manager calls the `handle` method of the plug-in. The `handle` method specifies the actions that the plug-in performs. The `refreshTree` method of the plug-in indicates whether Analytic Workspace Manager refreshes the navigation tree to include any new objects created by the plug-in or to remove objects deleted by the plug-in.

#### Calling a ViewerPlugin or EditorPlugin

As described in ["Creating Reports in Object Folders"](olawxml.md), with certain XML documents you can add objects to the Schemas, Analytic Workspaces, Dimensions, and Cubes folders in the Analytic Workspace Manager navigation tree. You add objects to the navigation tree by adding `<AWMNode>` elements to the XML document. If an `<AWMNode>` specifies a `ViewerPlugin` or an `EditorPlugin`, then Analytic Workspace Manager calls the plug-in when the user selects the navigation tree object that corresponds to the `<AWMNode>`.

With the `sql` attribute of an `<AWMNode>` element, you can specify a SQL `SELECT` statement. Analytic Workspace Manager displays the result of the statement either in the folder in the navigation tree or in the property inspector, or in both places. For more information about creating the XML documents and the SQL statements, see ["Creating Reports in Object Folders"](olawxml.md).

To control the display of the information in the property inspector or to enable the user to edit properties of the selected navigation tree object, you can use a `ViewerPlugin` or `EditorPlugin`. You use the `viewClass` attribute of an `<AWMNode>` element to specify the plug-in. In the plug-in you can use the Oracle OLAP Java API to retrieve OLAP objects or alter characteristics of them. You can also specify user interface elements for the display in the property inspector.

## Describing the AWMPlugin Interface

The following is the `oracle.olap.awm.plugin.AWMPlugin` interface.

```
package oracle.olap.awm.plugin

import java.awt.Frame;
import java.sql.Connection;
import java.util.Map;
import oracle.AWXML.AW;

public interface AWMPlugin
{
  boolean isSupported(Connection conn, String type, Object obj, AW aw,
                      Map params);

  String getMenu(Connection conn, String type, Object obj, AW aw, 
                 Map params);

  void handle(Frame parent, Connection conn, String type, Object obj, 
              AW aw, Map params);

  boolean refreshTree(Connection conn, String type, Object obj, AW aw,
                      Map params);
}
```

When a user right-clicks an object in the navigation tree, Analytic Workspace Manager calls the methods of classes that implement the `AWMPlugin` interface in the sequence illustrated in Figure 2-4.

Figure 2-4 Sequence of Calls to an AWMPlugin

![Description of Figure 2-4 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/awmpluginseq.gif "Description of Figure 2-4 follows")  
[Description of "Figure 2-4 Sequence of Calls to an AWMPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/awmpluginseq.htm)  

Analytic Workspace Manager first calls the `isSupported` method. If that method returns `true`, then Analytic Workspace Manager calls `getMenu` and displays on the right-click menu the value that `getMenu` returns. If a user selects the menu item, then Analytic Workspace Manager calls the `handle` and `refreshTree` methods. The input parameters that Analytic Workspace Manager passes to the `AWMPlugin` methods are the following:

- `conn`, which is a `java.sql.Connection` object that represents the current connection to the Oracle Database instance.
- `type`, which is a `java.lang.String` that is a type designation that Analytic Workspace Manager assigns to the object. For a description of `type` parameter values, see "Values for the type and obj Parameters".
- `obj`, which is a `java.lang.Object` that Analytic Workspace Manager associates with the object selected in the Analytic Workspace Manager navigation tree. The `Object` can be a `String` or an object from the Oracle OLAP Java API. For more information on the `obj` parameter values, see "Values for the type and obj Parameters".
- `aw`, which is `null`. This parameter exists for compatibility with 10g plug-ins, for which `aw` was an `oracle.AWXML.AW` object.
- `params`, which is a `java.util.Map` that contains objects and information that the plug-in can use. For a description of the `Map` keys and values, see "Elements in the params Map for an AWMPlugin".
- `parent`, which is a `java.awt.Frame` object that Analytic Workspace Manager passes to the `handle` method. The plug-in can use this object as the parent frame for user interface components.

### Values for the type and obj Parameters

For the `type` parameter of the methods of an `AWMPlugin` implementation, Analytic Workspace Manager passes to the plug-in a label that identifies the type of the navigation tree object for which the plug-in is invoked. For the `obj` parameter of the methods, Analytic Workspace Manager passes an `Object`, which is a `java.lang.String` or an OLAP metadata object.

A plug-in can use the `type` value to distinguish between the navigation tree objects that are associated with the same metadata object. For example, for all of the folder objects in a Dimensions folder, such as Levels and Hierarchies, Analytic Workspace Manager passes as the `obj` parameter the same `MdmPrimaryDimension` object, but it passes a different `type` label for each folder object.

Custom objects that you add with an XML document appear in the navigation tree at the level specified by the XML document. For example, a top-level `<AWMNode>` in a `dimension.xml` document appears in the Dimensions folder of an analytic workspace. For an `AWMPlugin` implementation specified by an `<AWMNode>` element, the `type` parameter value has the prefix `AWMTree_` followed by the value of the `name` attribute of the parent `<AWMNode>`. The `obj` parameter value is the run-time value of the `type` attribute of the `<AWMNode>`.

Table 2-1 shows the `type` parameter values and `obj` parameter objects that Analytic Workspace Manager passes to the plug-in for the selected navigation tree object. The indentation of objects in the Navigation Tree Object column indicates the hierarchy of the tree. Text in italics indicates a variable object name. The `obj` parameter objects are `String` objects or OLAP metadata objects. The `AW` object is an `oracle.olapi.metadata.deployment.AW` object. The other metadata objects, such as `MdmStandardDimension` and `MdmCube`, are classes in the `oracle.olapi.metadata.mdm` package. The Reports object and all of the objects under it have the same type.

Table 2-1 Type Values and Objects for Navigation Tree Objects

| Navigation Tree Object | type Parameter Value | obj Parameter Object |
| --- | --- | --- |
| Databases | `Databases` | `Databases` |
| Database name | `DATABASE` | Database identifier |
| Schemas | `SCHEMA_FOLDER` | Database identifier |
| Schema name | `SCHEMA` | Schema name |
| Analytic Workspaces | `WORKSPACE_FOLDER` | Schema name |
| Analytic workspace name | `WORKSPACE` | `AW` |
| Dimensions | `DIMENSION_FOLDER` | `AW` |
| Dimension name | `DIMENSION` | `MdmStandardDimension` or `MdmTimeDimension` |
| Levels | `DIMENSION_LEVEL_FOLDER` | `MdmStandardDimension` or `MdmTimeDimension` |
| Level name | `DIMENSION_LEVEL` | `MdmDimensionLevel` |
| Hierarchies | `DIMENSION_HIERARCHY_FOLDER` | `MdmStandardDimension` or `MdmTimeDimension` |
| Hierarchy name | `DIMENSION_HIERARCHY` | `MdmLevelHierarchy` or `MdmValueHierarchy` |
| Attributes | `DIMENSION_ATTRIBUTE_FOLDER` | `MdmStandardDimension` or `MdmTimeDimension` |
| Attribute name | `DIMENSION_ATTRIBUTE` | `MdmBaseAttribute` |
| Mappings | `DIMENSION_MAP` | `MdmStandardDimension` or `MdmTimeDimension` |
| Views | `DIMENSION_VIEW_FOLDER` | `MdmStandardDimension` or `MdmTimeDimension` |
| View name | `DIMENSION_VIEW` | `MdmStandardDimension` or `MdmTimeDimension` |
| Data Security | `DATA_SECURITY` | `MdmStandardDimension` or `MdmTimeDimension` |
| dimension.xml object | `AWMTree_` parent\_node\_name | For a folder, the name of the `<AWMNode>`. For a value returned by the SQL query, the run-time object name. |
| Cubes | `CUBE_FOLDER` | `AW` |
| Cube name | `CUBE` | `MdmCube` |
| Measures | `CUBE_MEASURE_FOLDER` | `MdmCube` |
| Measure name | `CUBE_MEASURE` | `MdmBaseMeasure` |
| Calculated Measures | `CUBE_DERIVED_MEASURE_FOLDER` | `MdmCube` |
| Calculated measure name | `CUBE_DERIVED_MEASURE` | `MdmDerivedMeasure` |
| Mappings | `CUBE_MAP` | `MdmCube` |
| Views | `CUBE_VIEW_FOLDER` | `MdmCube` |
| View name | `CUBE_VIEW` | `MdmCube` |
| Cube Scripts | `CUBE_SCRIPT_FOLDER` | `MdmCube` |
| Cube script name | `CUBE_SCRIPT` | Script\_name |
| Data Security | `DATA_SECURITY` | `MdmCube` |
| cube.xml object | `AWMTree_` parent\_node\_name | For a folder, the name of the `<AWMNode>`. For a value returned by the SQL query, the run-time object name. |
| Measure Folders | `MEASURE_FOLDER_FOLDER` | `AW` |
| Measure folder name | Measure\_folder\_name | `MdmOrganizationalSchema` |
| Languages | `LANGUAGE` | `Languages` |
| aw.xml object | `AWMTree_` parent\_node\_name | For a folder, the name of the `<AWMNode>`. For a value returned by the SQL query, the run-time object name. |
| OLAP DML Programs | `AWMTREE_OLAP DML Programs` | `OLAP DML Programs` |
| Program name | `AWMTREE_OLAP DML Programs` | Program\_name |
| Maintenance Scripts | `MAINTENANCE_SCRIPT_FOLDER` | Schema name |
| Script name | `MAINTENANCE_SCRIPT` | Script name |
| Maintenance Reports | `AWMTREE_Maintenance Reports` | Maintenance Reports |
| Maintenance\_report\_name | `AWMTREE_` maintenance\_report\_name | Maintenance\_report\_name |
| schema.xml object | `AWMTree_` parent\_node\_name | For a folder, the name of the `<AWMNode>`. For a value returned by the SQL query, the run-time object name. |
| Data Security Roles | `ACL_DOCUMENT_FOLDER` | Data Security Roles |
| Security role name | Security role name | Security role name |
| Reports | `AWMTREE_Reports` | Reports |
| Report name | `AWMTREE_` report\_name | Report name |

### Elements in the params Map for an AWMPlugin

The `params` `Map` contains information about the navigation tree object that is currently selected. Table 2-2, "Keys and Values of the params Map for a Non-custom Object" and Table 2-3, "Keys and Values of the params Map for a Custom Object" contain descriptions of the keys and values of the elements of the `Map` for an `AWMPlugin` The keys are `String` objects.

The `params` `Map` for the Database folder does not have a `DATASOURCE`, `DATAPROVIDER`, or `GETDATAPROVIDER` key. The `params` `Map` objects for the higher level navigation tree objects, those above the individual analytic workspaces, have a null value for the `DATAPROVIDER` key until the user selects a tree object that requires OLAP metadata. Other than for those exceptions, the `params` `Map` for a navigation tree object has the keys and values listed in the tables.

#### Params Map Elements for Non-custom Objects

Table 2-2 lists the keys and values of the elements of the `params` `Map` for non-custom navigation tree objects. Custom navigation tree objects are specified by an `<AWMNode>` element in a SQL Report XML document and have a type that begins with the prefix AWMTree.

Table 2-2 Keys and Values of the params Map for a Non-custom Object

| Key | Value |
| --- | --- |
| `AWM_VERSION` | A `String` that is the version number of Analytic Workspace Manager. |
| `DATAPROVIDER` | An `oracle.olapi.metadata.mdm.MdmMetadataProvider` that is the metadata provider for the session. |
| `BIND_MAP` | An empty `Map`. |
| `DATASOURCE` | A `java.sql.DataSource`. |
| `GETDATAPROVIDER` | An implementation of the `oracle.olap.awm.plugin.OLAPDataProvider` interface. The interface specifies a method that gets an `MdmMetadataProvider`. |

#### Params Map Elements for Custom Objects

Table 2-3 lists the keys and values of the elements of the `params` `Map` for custom navigation tree objects. A custom object is specified by an `<AWMNode>` element in a SQL Report XML document.

Table 2-3 Keys and Values of the params Map for a Custom Object

| Key | Value |
| --- | --- |
| `AWM_VERSION` | A `String` that is the version number of Analytic Workspace Manager. |
| `DATAPROVIDER` | An `oracle.olapi.metadata.mdm.MdmMetadataProvider` that is the metadata provider for the session. |
| `BIND_MAP` | A `java.util.Map` that contains bind variables from the `<AWMNode>` element and from the parent of the element, and from Analytic Workspace Manager. |
| `DATASOURCE` | A `java.sql.DataSource` object. |
| `GETDATAPROVIDER` | An implementation of the `oracle.olap.awm.plugin.OLAPDataProvider` interface. The interface specifies a method that gets an `MdmMetadataProvider`. |
| `ISFOLDER` | A `String` that is `TRUE` if the `<AWMNode>` that specifies the plugin-in is a folder or `FALSE` if it is not. |
| `NODE_TYPE` | For a nested `<AWMNode>`, a `String` that is the name of the parent `<AWMNode>`. For an `<AWMNode>` that is a folder, the name of the node. |
| `TYPE` | A `String` that is the value of the `type` attribute of the `<AWMNode>` that specifies the plug-in. |

The `BIND_MAP` `Map` contains bind variables that are associated with the navigation tree object that is currently selected. Table 2-4 contains descriptions of the keys and values in the `BIND_MAP` `Map`.

This `Map` includes the bind variables that appear in the SQL statements of the `<AWMNode>` and the parent `<AWMNode>`. It also includes other bind variables for the currently selected object in the navigation tree.

The keys are `String` objects. A bind variable is specified by the `type` attribute of an `<AWMNODE>` element of a custom navigation tree object or is set internally by Analytic Workspace Manager. A plug-in gets the run-time value of the bind variable from the `BIND_MAP` `Map`. For examples of bind map `Map` keys and values, see Table 2-6.

Note:

When you reference the key for a bind variable in your plug-in, be sure to use lowercase, as in `{owner}` or `{measureobj}` or `{dimension_name}`.

Table 2-4 Keys and Values of the BIND\_MAP Map

| Key | Value |
| --- | --- |
| `aw_name` | A `String` that contains the name of the currently selected analytic workspace. |
| `owner` | A `String` that contains the name of the owner of the currently selected analytic workspace. |
| `schema` | A `String` that contains the name of the owner of the currently selected schema. |
| `user` | A `String` that contains the name of the user who is connected to the database. |
| Other bind variables | One or more elements, each of which has a bind variable as a key and has the run-time value of the bind variable as the value.  Examples of other bind variable keys are `dimension_name` and `cube_name`. For examples of other bind variables that can be in the `Map` see the "Example params Map Elements for an AWMPlugin" and the examples in [Chapter 3, "Examples of Analytic Workspace Manager Plug-ins"](pluginexamples.md). |

### Example params Map Elements for an AWMPlugin

Examples of the keys and values of a `params` `Map` for a custom object are in Table 2-5 and in Table 2-6. All of the values are `String` objects except those for the `DATAPROVIDER` and `DATASOURCE` keys.

Table 2-6 has the elements of the `params` `Map` that Analytic Workspace Manager passes to the methods of `DeleteDimPlugin` when the user right-clicks the CUSTOMER dimension in the MyDims folder, as shown in [Figure 3-2](pluginexamples.md). The MyDims folder is created by the aw.xml document in [Example 3-7](pluginexamples.md).

The figure shows the menu that `DeleteDimPlugin` displays. The property inspector in the figure has the output of `DimEditorPlugin`, because that plug-in is also activated when the user selects a dimension in the MyDims folder.

An example of getting a value from the `params` `Map` is the following line from the `isSupported` method in the `DeleteDimPlugin` class in [Example 3-2](pluginexamples.md).

```
Object nodeType = params.get("TYPE");
```

Table 2-5 Keys and Values of the params Map for DeleteDimPlugin

| Key | Value | Description |
| --- | --- | --- |
| AW | An `AW` | The current analytic workspace object. |
| `AWM_VERSION` | `11.2.0.2.0` | The version number of Analytic Workspace Manager. |
| `BIND_MAP` | A `Map` | A container for bind variables related to the current object. |
| `DATAPROVIDER` | An `MdmMetadataProvider` | The metadata provider for the session. |
| `DATASOURCE` | A `DataSource` | The current data source. |
| `GETDATAPROVIDER` | An `OLAPDataProvider` | An implementation of the `OLAPDataProvider` interface. |
| `ISFOLDER` | `FALSE` | Specifies that the `<AWMNode>` is not a folder. |
| `NODE_TYPE` | `MyDims` | The name of the parent `<AWMNode>`. |
| `TYPE` | `dimobj` | The type of the `<AWMNode>` that specifies the plug-in. |

Table 2-6 has the elements of the `Map` that is the value of the `BIND_MAP` key in the `params` `Map`. An example of getting a value from the `BIND_MAP` `Map` is the following lines from the `handle` method in the `DeleteDimPlugin` class in [Example 3-2](pluginexamples.md).

```
Map bindMap = (Map)params.get("BIND_MAP");
...
String owner = (String)bindMap.get("owner");
```

Table 2-6 Keys and Values of the BIND\_MAP Map for DeleteDimPlugin

| Key | Value | Description |
| --- | --- | --- |
| `aw_name` | `GLOBAL` | The name of the current analytic workspace. |
| `dimobj` | `CUSTOMER` | The run-time value of the dimension currently selected in the MyDims folder. |
| `owner` | `GLOBAL` | The name of the owner of the analytic workspace. |
| `schema` | `GLOBAL` | The name of the current schema. |
| `user` | `global` | The name of the current user. |

## Describing the ViewerPlugin and EditorPlugin Interfaces

As described in ["Creating Reports in Object Folders"](olawxml.md), with certain XML documents you can add objects to the Schemas, Analytic Workspaces, Dimensions, and Cubes folders in the Analytic Workspace Manager navigation tree. You add objects to the navigation tree by adding `<AWMNode>` elements to an XML document.

With the `sql` attribute of an `<AWMNode>` element, you can specify a SQL `SELECT` statement. Analytic Workspace Manager displays the result of the statement either in the folder in the navigation tree or in the property inspector, or in both places. For more information about creating the XML documents and the SQL statements, see ["Creating Reports in Object Folders"](olawxml.md).

With the `viewClass` attribute of an `<AWMNode>` element, you can specify a Java plug-in for viewing or editing database objects. You can add a viewer or an editor for relational objects or OLAP objects. Relational objects include tables, materialized views, and so on, and OLAP objects include dimensions, cubes, and so on. To add a viewer, have the `viewClass` attribute specify an implementation of the `ViewerPlugin` interface. To add an editor, have the `viewClass` attribute specify an implementation of the `EditorPlugin` interface. The viewer or editor plug-in displays in the property inspector.

### Describing the ViewerPlugin Interface

The following is the `oracle.olap.awm.plugin.ViewerPlugin` interface.

```
package oracle.olap.awm.plugin

import java.sql.Connection;
import java.util.Map;
import javax.swing.JPanel;

public interface ViewerPlugin
{
  public boolean isViewerForType(Connection conn, String name) 
    throws Exception;

  public JPanel getPanel(Connection conn, String name, Map params)
    throws Exception;

  public void cleanup(String name);
}
```

When the Analytic Workspace Manager user selects the navigation tree object that is associated with the `ViewerPlugin`, Analytic Workspace Manager calls the methods of a `ViewerPlugin` in the sequence illustrated in Figure 2-5.

Figure 2-5 Sequence of Calls to a ViewerPlugin

![Description of Figure 2-5 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/viewseq.gif "Description of Figure 2-5 follows")  
[Description of "Figure 2-5 Sequence of Calls to a ViewerPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/viewseq.htm)  

Analytic Workspace Manager first calls the `isViewerForType` method and passes it the following parameters:

- `conn`, which is a `java.sql.Connection` object that represents the current connection to the Oracle Database instance.
- `name`, which is a `String` that contains the name of the `<AWMNode>` that is the parent of the `<AWMNode>` that has the `viewClass` attribute.

If the plug-in returns `true`, Analytic Workspace Manager calls the `getPanel` method and passes it the same `conn` and `name` parameters plus the following parameter.

- `params`, which is a `java.util.Map` object that contains information about the currently selected navigation tree object. The information includes the run-time values for attributes of the `<AWMNode>` element that has the `viewClass` attribute and from the parent `<AWMNode>`. The plug-in can use this information in specifying data to display or to retrieve from the database. The keys and values of the `Map` are described in Table 2-7. For a description of the `Map` keys and values, see "Elements in the params Map for a ViewerPlugin or EditorPlugin".

When the user selects a different navigation tree object, Analytic Workspace Manager calls the `cleanup` method of the plug-in. It passes the method the same `name` parameter. In this method you can perform any cleanup that your plug-in requires.

### Describing the EditorPlugin Interface

The `EditorPlugin` interface extends the `ViewerPlugin` interface. The following is the `oracle.olap.awm.plugin.EditorPlugin` interface.

```
package oracle.olap.awm.plugin

import java.awt.Component;
import java.sql.Connection;
import java.util.Map;

public interface EditorPlugin extends ViewerPlugin
{
  public void setValueChanged(Connection conn, String name, Map params,
    PanelChanged parent);

  public boolean validate(Connection conn, Component parent, String name, 
    Map params) throws Exception;

  public boolean save(Connection conn, Component parent, String name,
    Map params) throws Exception;

  public void revert(Connection conn, Component parent, String name, 
    Map params) throws Exception;

  public void showHelp(Connection conn, Component parent, String name,
    Map params) throws Exception;
}
```

For an `EditorPlugin`, Analytic Workspace Manager initially calls the `isViewerForType`, `setValueChanged`, and `getPanel` methods, as shown in Figure 2-6, "Sequence of Calls to an EditorPlugin". For an example of the display of an `EditorPlugin`, see [Figure 3-11](pluginexamples.md).

If the user makes a change in the property inspector, then the Apply and Revert buttons become active. If the user clicks Apply, then Analytic Workspace Manager calls the `validate` method of the `EditorPlugin`. If the value is valid, then Analytic Workspace Manager calls the `save` method. If the user clicks Revert, then Analytic Workspace Manager calls `revert`. If the user clicks the Help button, then Analytic Workspace Manager calls `showHelp`.

All of the methods of an `EditorPlugin` have the same `conn`, `name`, and `param` parameters as the `getPanel` method. Those parameters are described in "Describing the ViewerPlugin and EditorPlugin Interfaces". The methods also have the following additional parameter.

- `parent`, which for the `setValueChanged` method is an implementation of the `oracle.olap.awm.plugin.PanelChanged` interface. That interface specifies a single method, `public void changed();`. Whenever the user interacts with the editing field of your `EditorPlugin`, the `EditorPlugin` should call the `changed` method of the `PanelChanged` object. For the other `EditorPlugin` methods, the `parent` parameter is the parent component.

Figure 2-6 Sequence of Calls to an EditorPlugin

![Description of Figure 2-6 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/editseq.gif "Description of Figure 2-6 follows")  
[Description of "Figure 2-6 Sequence of Calls to an EditorPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/editseq.htm)  

### Elements in the params Map for a ViewerPlugin or EditorPlugin

The `params` `Map` for a `ViewerPlugin` or an `EditorPlugin` does not contain a `BIND_MAP` `Map`. Instead, the bind variables are keys in the `params` `Map`. Table 2-7 contains descriptions of the keys and values of the elements of the `Map` for a `ViewerPlugin` or an `EditorPlugin`.

Table 2-7 Keys and Values of the params Map for a ViewerPlugin or EditorPlugin

| Key | Value |
| --- | --- |
| `AW` | An `oracle.olapi.metadata.deployment.AW`. |
| `aw_name` | A `String` that contains the name of the currently selected analytic workspace. |
| `DATAPROVIDER` | An `oracle.olapi.metadata.mdm.MdmMetadataProvider` object that is the metadata provider for the session. |
| `DATASOURCE` | A `java.sql.DataSource` object. |
| `ISFOLDER` | A `String` that is `TRUE` if the `<AWMNode>` that specifies the plugin-in is a folder or `FALSE` if it is not. |
| `owner` | A `String` that contains the name of the owner of the currently selected analytic workspace. |
| `schema` | A `String` that contains the name of the owner of the currently selected schema. |
| `TYPE` | A `String` that is the value of the `type` attribute of the `<AWMNode>` that specifies the plug-in. |
| `user` | A `String` that contains the name of the user who is connected to the database. |
| Other bind variables | One or more elements, each of which has a bind variable as a key and has the run-time value of the bind variable as the value. For a plug-in that is specified by the `viewClass` attribute of an `<AWMNode>` in an XML document, the number of bind variables depends upon how many bind variables are in the SQL statement of the `<AWMNode>` and the parent `<AWMNode>`.  Examples of other bind variable keys are `dimension_name` and `cube_name`. For examples of other bind variables that can be in the `Map` see the "Example params Map Elements for a ViewerPlugin and an EditorPlugin" and the examples in [Chapter 3, "Examples of Analytic Workspace Manager Plug-ins"](pluginexamples.md). |

### Example params Map Elements for a ViewerPlugin and an EditorPlugin

Examples of the keys and values of a `params` `Map` for a `ViewerPlugin` or `EditorPlugin` are in Table 2-8. All of the values are `String` objects except those for the `DATAPROVIDER` and `DATASOURCE` keys.

#### Example params Map Elements for a ViewerPlugin

The `cube.xml` document in [Example 3-5](pluginexamples.md) has a parent `<AWMNode>` that has the name `MyMeasures`, a type of `measureobj`, and a SQL statement that references the bind variable `cube_name`. The child `<AWMNode>` has the type `measureview` and has a `viewClass` attribute that specifies the plug-in `MeasureViewerPlugin`.

Table 2-8 has the elements of the `params` `Map` that Analytic Workspace Manager passes to the methods of the `MeasureViewerPlugin` when the user selects the UNITS measure in the MyMeasures folder, as shown in [Figure 3-7](pluginexamples.md). The property inspector has the output of the plug-in, which is simply the name of the measure.

The `MeasureViewerPlugin` class in [Example 3-6](pluginexamples.md) gets the value of a bind variable in the following line in the `getPanel` method.

```
measureobj = params.get("measureobj");
```

Table 2-8 Keys and Values of the params Map for MeasureViewerPlugin

| Key | Value | Description |
| --- | --- | --- |
| `AW` | An `AW`. | The current analytic workspace object. |
| `aw_name` | `GLOBAL` | The name of the current analytic workspace. |
| `cube_name` | `UNITS_CUBE` | The name of the current cube. |
| `DATAPROVIDER` | An `MdmMetadataProvider` | The metadata provider for the session. |
| `DATASOURCE` | A `DataSource` | The current data source. |
| `ISFOLDER` | `FALSE` | Indicates that the navigation tree object is not a folder. |
| `measureobj` | `UNITS` | The name of the current measure. |
| `NODE_TYPE` | `MyMeasures` | The name of the parent `<AWMNode>`. |
| `owner` | `GLOBAL` | The name of the owner of the analytic workspace. |
| `schema` | `GLOBAL` | The name of the current schema. |
| `TYPE` | `measureview` | The type of the `<AWMNode>`. |
| `user` | `global` | The name of the current user. |

#### Example params Map Elements for an EditorPlugin

Table 2-9 has the elements of the `params` `Map` that Analytic Workspace Manager passes to the methods of the `DimEditorPlugin` when the user selects the CHANNEL dimension in the MyDims folder, as shown in [Figure 3-11](pluginexamples.md). The property inspector in the figure has the output of the `DimEditorPlugin`.

An example of getting a value from the `params` `Map` is the following line from the `getMetadataProvider` method in the `DimEditorPlugin` class in [Example 3-9](pluginexamples.md).

```
Object dp = params.get("DATAPROVIDER");
```

Another example of getting a value from the `params` `Map` is the following lines from the `getDimension` method in the `DimEditorPlugin` class.

```
Object obj = null;
...
obj = params.get("dimobj");
```

Table 2-9 Keys and Values of the params Map for DimEditorPlugin

| Key | Value | Description |
| --- | --- | --- |
| `AW` | An `AW`. | The current analytic workspace object. |
| `aw_name` | `GLOBAL` | The name of the current analytic workspace. |
| `DATAPROVIDER` | An `MdmMetadataProvider` | The metadata provider for the session. |
| `DATASOURCE` | A `DataSource` | The current data source. |
| `dimobj` | `CHANNEL` | The run-time value of the dimension currently selected in the MyDims folder. |
| `ISFOLDER` | `TRUE` | Indicates that the navigation tree object is a folder. |
| `NODE_TYPE` | `MyDims` | The name of the parent `<AWMNode>`. |
| `owner` | `GLOBAL` | The name of the owner of the analytic workspace. |
| `schema` | `GLOBAL` | The name of the current schema. |
| `TYPE` | `dimobj` | The type of the `<AWMNode>`. |
| `user` | `global` | The name of the current user. |

## Steps in Creating a Plug-in

The prerequisites for creating an Analytic Workspace Manager plug-in are the following:

- For the Analytic Workspace Manager that is part of an Oracle Database Enterprise Edition distribution, include the following files in your development environment. These JAR files are located in the `Oracle_home` `/olap/api/lib` directory in the Oracle Database installation.
	- `awm.jar`, which contains the plug-in interfaces.
		- `olap_api.jar`, which contains the classes in the Oracle OLAP Java API.
		- `awxml.jar`, which contains the `oracle.AWXML.AW` class, which the `AWMPlugin` interface includes for compatibility with the 10g release of Analytic Workspace Manager.
- For an Analytic Workspace Manager that you have downloaded from Oracle Technology Network, include the `awm11.2.0.1.0.jar` file in your development environment.
- Compile the code with JDK 1.5.

Note:

Only plug-ins compiled with JDK 1.5 are compatible with Analytic Workspace Manager in 11g Release 2 (11.2).

To create an Analytic Workspace Manager plug-in, do the following:

1. Create a class that implements a plug-in interface.
	- For an `AWMPlugin`, do the following.
		- In the `isSupported` method, specify the objects in the navigation tree to which the plug-in applies. Be sure to have this method return quickly.
				- Have the `getMenu` method return the text to display on the right-click menu for navigation tree objects that the plug-in supports.
				- In the `handle` method, include the code for the operations that the plug-in performs.
				- Have the refreshTree method return a boolean that specifies whether to refresh the navigation tree.
		- For `ViewerPlugin`, do the following.
		- In the `isViewerForType` method, specify the type of navigation tree objects to which the plug-in applies.
				- Have the `getPanel` method create the user interface elements for Analytic Workspace to display and specify the actions for them.
				- In the `cleanup` method, perform any cleaning up that your plug-in requires.
		- For an `EditorPlugin`, do the steps for a `ViewerPlugin` and add the following.
		- In the `setValueChanged` method, store the `PanelChanged` object from Analytic Workspace Manager. Call the `changed` method of the `PanelChanged` whenever you want to update the display in the property inspector.
				- In the `validate` method, validate any change that the user has made.
				- In the `save` method, perform the actions required to make the changes and then commit the current `Transaction` to save the changes.
				- In the `revert` method, display the object as it was before the changes.
2. Using JDK 1.5, compile the plug-in and any other classes that it uses.
3. Deploy the plug-in, XML documents, and other classes to a JAR file. You can include multiple plug-ins in the same JAR file.
4. Put the JAR file in the plug-ins directory.
5. Start Analytic Workspace Manager.

Note:

Analytic Workspace Manager only loads the contents of the JAR files upon startup, so if you put a new or updated version of a JAR file in the plug-ins directory, then you must restart Analytic Workspace Manager.

To use a `ViewerPlugin` or `EditorPlugin`, you generally do the following steps.

- Create an XML document that has the name `schema.xml`, `aw.xml`, `cube.xml`, or `dimension.xml`, depending on where in the navigation tree you want the custom objects to appear. In the XML document, you can have multiple `<AWMNode>` elements at the same level. You can also nest one or more `<AWMNode>` elements in a parent `<AWMNode>` element.
- Develop the SQL statements to specify with `<AWMNode>` elements.
- Implement the `ViewerPlugin` or `EditorPlugin` interface.
- Specify the SQL statement for an `<AWMNode>` with the `sql` attribute. Specify a plug-in with the `viewClass` attribute.
- Deploy the XML document and plug-in implementation in a JAR file. You can have multiple XML documents and plug-ins in the same JAR file. You can put the XML documents in the same JAR file as the plug-ins.
- Put the JAR file in the Analytic Workspace Manager directory for plug-ins.
- Start Analytic Workspace Manager.

## Describing the Available Plug-ins

You can provide information about the plug-ins that you add to Analytic Workspace Manager by creating an `awmplugin.xml` document. In that XML document, you can provide a name, a version number, and a description for each plug-in. Analytic Workspace Manager displays that information, along with the status of the plug-in, when a user selects the Plugins tab after selecting About on the Help menu.

### Creating an XML Document for Descriptions of Plug-ins

1. Create a text file named `awmplugin.xml`.
2. Begin the file with an XML declaration like this one:
	```
	<?xml version="1.0" encoding="utf-8"?>
	```
	Specify the appropriate encoding for your site.
3. Enter the XML for the plug-in descriptions, as described in "Reference: Elements for Plug-in Descriptions".
4. For the `name` attribute of the `<Plugin>` element, enter a name for the plug-in. For the `version` attribute, enter the version number of the plug-in. For the `class` attribute, enter the class that contains the plug-in. For the `<Description>` element, enter a description of the plug-in.
5. In the plug-directory, create a JAR file that contains the `awmplugin.xml` document. Alternatively, you could add the `awmplugin.xml` document to a JAR file that contains the XML documents described in ["Creating Reports in Object Folders"](olawxml.md) or the plug-ins.

For a sample `awmplugin.xml` file, see ["Example of Plug-in Descriptions"](pluginexamples.md).

### Reference: Elements for Plug-in Descriptions

An XML document for describing the available plug-ins has the format shown in Example 2-1.

Example 2-1 XML Structure for Descriptions of Plug-ins

```
<AWMPlugins>
  <Plugin>
    <Description>
         .
         .
         .
```

#### \<AWMPlugins>

The root element that identifies this document as containing information about the Java plug-ins that are available to Analytic Workspace Manager.

Contains

`<Plugin>`

Attributes

None

#### \<Plugin>

Contains information about a plug-in.

Contains

`<Description>`

Attributes

`<Plugin>` has the following attributes:

- name: A name for the plug-in.
- version: A version number for the plug-in.
- class: The Java class that implements the plug-in.

#### \<Description>

Contains a description of the plug-in.

Contains

None

Attributes

None