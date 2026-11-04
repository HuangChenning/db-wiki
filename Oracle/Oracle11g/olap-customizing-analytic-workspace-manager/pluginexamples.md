---
title: Examples of Analytic Workspace Manager Plug-ins
book: OLAP Customizing Analytic Workspace Manager
doc_id: E17237-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/olap.112/e17237/pluginexamples.htm
tags:
  - oracle
  - 11g
  - olap-customizing-analytic-workspace-manager
---

## 3 Examples of Analytic Workspace Manager Plug-ins

This chapter contains examples of the Java classes that implement the `AWMPlugin`, `ViewerPlugin`, and `EditorPlugin` interfaces. It also contains the example XML documents that specify the plug-ins.

This chapter contains the following topics:

## Availability of Example Classes and XML Documents

The examples of Java classes and XML documents in this chapter and in [Chapter 1](olawxml.md) contain the complete code for the class or document. The complete code is also available in a compressed file that you can download from the Oracle Technology Network (OTN) Web site. The download includes the compiled `class` files for the plug-ins, as well. The OTN Web site is at

`http://www.oracle.com/technology/products/bi/olap/index.html`

To get the examples, in the Download section of the Web page, select Sample Code and Schemas. On the Oracle OLAP Downloads page, in the Sample Schemas and Code section, under Oracle OLAP 11g, in the AWM Java Plug-ins and XML Documents for 11.2.0.2 line, click examples.

The compressed file `customizingAWM_examples11202.zip` contains the following files.

| Filename | Description |
| --- | --- |
| `readme.txt` | Briefly describes the contents of the `zip` file. |
| `awmcalcs.xml` | Contains the XML for [Example 1-9, "Sample AWMCalcs Document"](olawxml.md). |
| `awmtree.xml` | Contains the XML for [Example 1-3, "Passing the Name of a View to a SELECT Statement"](olawxml.md). |
| `plugin11202.jar` | Contains a directory named `plugin11202`, which is the package containing the examples. In the directory are the `xml`, `java`, and `class` files for the examples in Chapter 3. |

You put the `awmcalcs.xml` and `awmtree.xml` files in the same directory as the Analytic Workspace Manager executable file. You put the `plugin11202.jar` file in the directory that you specify for plug-ins, as described in ["Enabling Analytic Workspace Manager Plug-ins"](pluginintro.md).

## Examples of AWMPlugin

The examples of an `AWMPlugin` are in the following topics.

- ViewXMLPlugin Example
- DeleteDimPlugin Example

The examples do not include the documentation comments of the methods of the `AWMPlugin` interface or the input parameters and return values of those methods. Those methods and parameters are described in ["Describing the AWMPlugin Interface"](pluginintro.md).

### ViewXMLPlugin Example

The `ViewXMLPlugin` class displays an XML representation of a measure or a custom measure of a cube in the Cubes folder in the Analytic Workspace Manager navigation tree. Example 3-1 contains the code for the class. The plug-in applies to `oracle.olap.metadata.mdm.MdmBaseMeasure` and `oracle.olap.metadata.mdm.MdmDerivedMeasure` objects, which correspond to the Measure and Calculated Measure objects, respectively, of a cube.

The plug-in gets and displays an XML representation of a measure. [Figure 2-3](pluginintro.md) shows the menu that Analytic Manager Workspace displays for `ViewXMLPlugin` when a user right-clicks a measure. For an example of the dialog box that `ViewXMLPlugin` displays, see Figure 3-1, "Dialog Box Displayed by ViewXMLPlugin".

Example 3-1 The ViewXMLPlugin Class

```
import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.sql.Connection;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

import oracle.AWXML.AW;
import oracle.olap.awm.plugin.AWMPlugin;
import oracle.olapi.metadata.mdm.MdmBaseMeasure;
import oracle.olapi.metadata.mdm.MdmDerivedMeasure;
import oracle.olapi.metadata.mdm.MdmMetadataProvider;
import oracle.olapi.metadata.mdm.MdmObject;

/**
 * An implementation of the AWMPlugin interface that displays the XML
 * representation of an Oracle OLAP measure object.
 */
public class ViewXMLPlugin implements AWMPlugin
{
  public boolean isSupported(Connection conn, String type, Object obj, 
                             AW aw, Map params)
  {
    // Support MdmBaseMeasure and MdmDerivedMeasure objects.
    if (obj instanceof MdmBaseMeasure || obj instanceof MdmDerivedMeasure)
    {
      return true;
    }
    return false;
  }

  public String getMenu(Connection conn, String type, Object obj, AW aw, 
                        Map params)
  {
    // Text to display on the right-click menu.
    String menu = "View XML Example Plug-in";
    return menu;
  }

  public void handle(Frame parent, Connection conn, String type, Object obj,
                     AW aw, Map params)
  {
    if (obj instanceof MdmObject)
    {
      // Get the MdmMetadataProvider to use in exporting the XML.
      Object objdp = params.get("DATAPROVIDER");
      if (objdp != null)
      {
        MdmObject mobj = (MdmObject)obj;
        MdmMetadataProvider mdp = (MdmMetadataProvider)objdp;
 
        // Get the XML representation of the MdmObject.
        List objects = new ArrayList();
        objects.add(mobj);
        Map renameMap = null;
        boolean includeOwnerString = true;
        String title = "XML for " + mobj.getName();
        try
        {
          String xml =
            mdp.exportFullXML(objects, renameMap, includeOwnerString);
          // Create a dialog box and display the XML.
          DisplayXMLDialog dxd = new DisplayXMLDialog(parent, title, true,
                                                      xml);
        }
        catch (IOException ie)
        {
          // Ignore error.
        }
      }
    }
  }

  public boolean refreshTree(Connection conn, String type, Object obj, AW aw,
                             Map params)
  {
    // This example does not create new metadata objects, so return false.
    return false;
  }

  /**
   * An inner class that creates a dialog box that displays the XML.
   */
  class DisplayXMLDialog extends JDialog implements ActionListener
  {
    /**
     * Creates a DisplayXMLDialog for displaying the contents of the xml
     * parameter.
     * 
     * @param parent A Frame that is provided by Analytic Workspace Manager.
     * @param title A String that contains text to use as the title for the
     *              dialog box.
     * @param modal A boolean that specifies whether the dialog box is modal.
     * @param xml A String that contains the XML to display.
     */
    public DisplayXMLDialog(Frame parent, String title, boolean modal,
                            String xml)
    {
      super(parent);
      setLocation(200, 200);
      setTitle(title);
      setModal(modal);
      
      try
      {
        displayXML(xml);
      }
      catch (Exception e)
      {
        e.printStackTrace();
      }
    }
 
    /**
     * Creates a dialog box and displays the contents of a String.
     * 
     * @param xml A String that contains the XML to display.
     */
    private void displayXML(String xml)
    {
      JTextArea ta = new JTextArea(xml);
      ta.setEditable(false);
      Font of = ta.getFont();
      Font f = new Font("Courier New", of.getStyle(), of.getSize());
      ta.setFont(f);

      JScrollPane p = new JScrollPane();
      p.getViewport().add(ta);

      JPanel buttonPane = new JPanel();
      JButton button = new JButton("Close");
      buttonPane.add(button);
      button.addActionListener(this);
      getContentPane().add(buttonPane, BorderLayout.SOUTH);
      
      getContentPane().add(p, BorderLayout.NORTH);
      setDefaultCloseOperation(DISPOSE_ON_CLOSE);
      pack();
      setVisible(true);
    }

    /**
     * Performs an action for the Close button.
     * 
     * @param e An ActionEvent for the Close button.
     */
    public void actionPerformed(ActionEvent e)
    {
      setVisible(false);
      dispose();
    }
  }
}
```

Figure 3-1 illustrates the dialog box that `ViewXMLPlugin` displays for the `PROFIT` calculated measure in the `UNITS_CUBE` folder.

Figure 3-1 Dialog Box Displayed by ViewXMLPlugin

![Description of Figure 3-1 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/xmlprofit.gif "Description of Figure 3-1 follows")  
[Description of "Figure 3-1 Dialog Box Displayed by ViewXMLPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/xmlprofit.htm)  

### DeleteDimPlugin Example

The `DeleteDimPlugin` class deletes the dimension that the user has selected in the navigation tree. The plug-in only applies to dimension objects that are in a custom folder and that have `dimobj` as the value of the `TYPE` key of the `params` `Map`. The `DeleteDimPlugin` plug-in is specified by the `aw.xml` document in Example 3-7.

Example 3-2 contains the code for the `DeleteDimPlugin` class.

Example 3-2 The DeleteDimPlugin Class

```
package plugin11202;
 
import java.awt.Frame;
import java.sql.Connection;
import java.util.Map;
import javax.swing.JOptionPane;
import oracle.AWXML.AW;
import oracle.olap.awm.plugin.AWMPlugin;
import oracle.olapi.metadata.mdm.MdmMetadataProvider;
import oracle.olapi.metadata.mdm.MdmObject;
import oracle.olapi.metadata.mdm.MdmPrimaryDimension;
import oracle.olapi.metadata.mdm.MdmSchema;

/**
 * An implementation of the AWMPlugin interface that can delete
 * an Oracle OLAP dimension object in a custom folder.
 */
public class DeleteDimPlugin implements AWMPlugin
{
  // This plug-in applies to dimension objects in a custom folder.
  public boolean isSupported(Connection conn, String type, Object obj, AW aw,
                             Map params)
  {
    if (params != null)
    {
      // Get the value of the type attribute of the AWMNode that specifies this
      // plug-in.
      Object nodeType = params.get("TYPE");
      if (nodeType != null && ((String)nodeType).equalsIgnoreCase("dimobj"))
        return true;
    }
    return false;
  }
 
  public String getMenu(Connection conn, String type, Object obj, AW aw,
                        Map params)
  {
    Object dimName = null;
    if (obj != null && obj instanceof String)
    {
      dimName = (String) obj;
    }
    // Text to display on the right-click menu.
    return "Example Plug-in: Delete Dimension " + dimName;
  }
 
  public void handle(Frame parent, Connection conn, String type, Object obj,
                     AW aw, Map params)
  {
    String dimName = "";
    // The obj parameter should be the name of the currently selected dimension.
    if (obj != null && obj instanceof String)
    {
      dimName = (String) obj;
      String title = "Delete Dimension";
      if (JOptionPane.showConfirmDialog(parent, "Delete " + dimName + "?",
                                        title, JOptionPane.YES_NO_OPTION) ==
                                        JOptionPane.NO_OPTION)
        return;
    }

    if (params != null)
    {
      Map bindMap = (Map)params.get("BIND_MAP");
      if (bindMap != null)
      {
        // Get the name of the owner, which is also the name of the schema.
        String owner = (String)bindMap.get("owner");
        // Get the currently selected dimension.
        MdmPrimaryDimension dim = getDimension(dimName, owner, params);

        if (dim != null)
        {
          // Get the schema object that contains the dimension.
          MdmSchema schema = dim.getOwner();
          schema.removeDimension(dim);
          MdmMetadataProvider mdp = getMetadataProvider(params);
          // Get the TransactionProvider and commit the current Transaction.
          try
          {
            mdp.getDataProvider()
               .getTransactionProvider()
               .commitCurrentTransaction();
            JOptionPane.showMessageDialog(parent,
                                          owner + "." + dimName +
                                          " dimension has been deleted.");
          }
          catch (Exception e)
          {
            JOptionPane.showMessageDialog(parent, e.getMessage(), "Error",
                                          JOptionPane.ERROR_MESSAGE);
            // Roll back the current Transaction.
            try
            {
              mdp.getDataProvider()
                 .getTransactionProvider()
                 .rollbackCurrentTransaction();
            }
            catch (Exception e2)
            {
              // Ignore the exception.
            }
          }
        }
      }
      else
      {
        return;
      }
    }
  }
 
  public boolean refreshTree(Connection conn, String type, Object obj, AW aw,
                             Map params)
  {
    return true;
  }
 
  // Get the MdmMetadataProvider.
  private MdmMetadataProvider getMetadataProvider(Map params)
  {
    Object dp = params.get("DATAPROVIDER");
    if (dp instanceof MdmMetadataProvider)
    {
      MdmMetadataProvider mdp = (MdmMetadataProvider)dp;
      return mdp;
    }
    return null;
  }
 
  // Get the currently selected dimension.
  private MdmPrimaryDimension getDimension(String dimName, String schema,
                                           Map params)
  {
    if (params != null)
    {
      MdmMetadataProvider mdp = getMetadataProvider(params);
      if (mdp != null)
      {
        // Get the dimension from the MdmMetadataProvider.
        MdmObject mobj = mdp.getMetadataObject(schema + "." + dimName);
        if (mobj != null && mobj instanceof MdmPrimaryDimension)
        {
          MdmPrimaryDimension dim = (MdmPrimaryDimension)mobj;
          return dim;
        }
      }
    }
    return null;
  }
}
```

Figure 3-2 shows the menu that Analytic Manager Workspace displays for `DeleteDimPlugin`. The figure shows the menu that appears when a user right-clicks the CUSTOMER dimension in the MyDims folder. The MyDims folder is created by the `aw.xml` document in Example 3-7.

Figure 3-2 Right-click Menu Displayed by DeleteDimPlugin

![Description of Figure 3-2 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/deltdim2.gif "Description of Figure 3-2 follows")  
[Description of "Figure 3-2 Right-click Menu Displayed by DeleteDimPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/deltdim2.htm)  

If the user clicks Example Plug-in: Delete Dimension CUSTOMER, then `DeleteDimPlugin` displays the dialog box shown in Figure 3-3.

Figure 3-3 Dialog Box Displayed by DeleteDimPlugin

![Description of Figure 3-3 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/deltcust.gif "Description of Figure 3-3 follows")  
[Description of "Figure 3-3 Dialog Box Displayed by DeleteDimPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/deltcust.htm)  

## Examples of ViewerPlugin and EditorPlugin

The example `ViewerPlugin` and `EditorPlugin` implementations are in the following topics:

- LevelViewerPlugin Example
- MeasureViewerPlugin Example
- CubeViewerPlugin Example
- DimEditorPlugin Example

The topics include the XML documents that specify the plug-ins.

The methods of the `ViewerPlugin` and `EditorPlugin` interfaces are described in ["Describing the ViewerPlugin and EditorPlugin Interfaces"](pluginintro.md).

### LevelViewerPlugin Example

The `dimension.xml` document in Example 3-3 has an `<AWMNode>` that specifies a folder named MyLevels and a SQL statement that selects the names of the levels of the currently selected dimension from the USER\_CUBE\_DIM\_LEVELS table. An unnamed child `<AWMNode>` specifies the `LevelViewerPlugin`. Figure 3-4 shows the navigation tree folder and the display in the property inspector for the document.

Example 3-3 Creating a dimension.xml Document

```
<?xml version="1.0" encoding="US-ASCII" ?>
<AWMTree>
  <AWMNode name="MyLevels"
           type="levelobj"
           sql="select level_name from user_cube_dim_levels where dimension_name = {dimension_name} ">
    <AWMNode type="levelview"
             viewClass="plugin11202.LevelViewerPlugin"/>  
  </AWMNode>
</AWMTree>
```

Example 3-4 contains the `LevelViewerPlugin` class. The class displays the name of the currently selected level, as shown in Figure 3-5.

Example 3-4 The LevelViewerPlugin Class

```
package plugin11202;
 
import java.awt.FlowLayout;
import java.sql.Connection;
import java.util.Map;
import javax.swing.JLabel;
import javax.swing.JPanel;
import oracle.olap.awm.plugin.ViewerPlugin;
 
public class LevelViewerPlugin implements ViewerPlugin
{
  public boolean isViewerForType(Connection conn, String name)
    throws Exception
  {
    return true;
  }
 
  public JPanel getPanel(Connection conn, String name, Map params)
    throws Exception
  {
    JPanel panel = new JPanel();
    panel.setLayout(new FlowLayout());
    // Get the name of the current level.
    Object obj = params.get("levelobj");
    if (obj instanceof String)
    {
      String levelName = (String)obj;
      panel.add(new JLabel(levelName));
    }
    return panel;
  }
  
  public void cleanup(String name)
  {     
  }
}
```

Figure 3-4 shows the results of the `MyLevels` `<AWMNode>` in the `dimension.xml` document. A MyLevels folder appears in each dimension folder of the analytic workspace. The user has selected the MyLevels folder in the PRODUCT folder. The result of the SQL statement of the `<AWMNode>` appears in the MyLevels folder. The property inspector displays the same SQL statement and the result of it, which is a list of the levels of the dimension.

Figure 3-4 Results of the MyLevels \<AWMNode> in dimension.xml

![Description of Figure 3-4 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/mylevels.gif "Description of Figure 3-4 follows")  
[Description of "Figure 3-4 Results of the MyLevels \<AWMNode> in dimension.xml"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/mylevels.htm)  

Figure 3-5 shows the results of the unnamed child `<AWMNode>` of the `MyLevels` `<AWMNode>` in the `dimension.xml` document. The user has selected the FAMILY level in the MyLevels folder. The property inspector displays the user interface specified by `LevelViewerPlugin`. The plug-in displays the name of the level.

Figure 3-5 Results of LevelViewerPlugin

![Description of Figure 3-5 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/family.gif "Description of Figure 3-5 follows")  
[Description of "Figure 3-5 Results of LevelViewerPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/family.htm)  

### MeasureViewerPlugin Example

The `cube.xml` document in Example 3-5 has an `<AWMNode>` that specifies a folder named MyMeasures and a SQL statement that selects the names of the measures of the currently selected cube from the USER\_CUBE\_MEASURES table. An unnamed child `<AWMNode>` specifies the `MeasureViewerPlugin` plug-in. Figure 3-6 shows the navigation tree folder and the display in the property inspector for the document.

Example 3-5 Creating a cube.xml Document

```
<?xml version="1.0" encoding="US-ASCII" ?>
<AWMTree>
  <AWMNode name="MyMeasures"
           type="measureobj" 
           sql="select measure_name from user_cube_measures where cube_name = {cube_name}">
    <AWMNode type="measureview"
             viewClass="plugin11202.MeasureViewerPlugin"/>
  </AWMNode>
</AWMTree>
```

Example 3-6 contains the `MeasureViewerPlugin` class. The class displays the name of the currently selected measure, as shown in Figure 3-7.

Example 3-6 The MeasureViewerPlugin Class

```
package plugin11202;
 
import java.awt.FlowLayout;
import java.sql.Connection;
import java.util.Map;
import javax.swing.JLabel;
import javax.swing.JPanel;
import oracle.olap.awm.plugin.ViewerPlugin;
 
public class MeasureViewerPlugin implements ViewerPlugin
{
  public boolean isViewerForType(Connection conn, String name)
    throws Exception
  {
    return true;
  }   
 
  public JPanel getPanel(Connection conn, String name, Map params)
    throws Exception
  {
    JPanel panel = new JPanel();
    panel.setLayout(new FlowLayout());

    // Get the name of the current measure.
    Object measureobj = null;
    if (params != null)
      measureobj = params.get("measureobj");

    if (measureobj instanceof String)
    {
      String measureName = (String)measureobj;
      panel.add(new JLabel(measureName));
    }
    return panel;
  }
 
  public void cleanup(String name)
  {   
  }
}
```

Figure 3-6 shows the results of the `MyMeasures` `<AWMNode>` in the `cube.xml` document. A MyMeasures folder appears in each cube folder of the analytic workspace. The user has selected the MyMeasures folder in the UNITS\_CUBE folder. The result of the SQL statement of the `<AWMNode>` appears in the MyMeasures folder. The property inspector displays the same SQL statement and the result of it, which is a list of the measures and calculated measures of the cube.

Figure 3-6 Results of the MyMeasures \<AWMNode> in cube.xml

![Description of Figure 3-6 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/mymeasrs.gif "Description of Figure 3-6 follows")  
[Description of "Figure 3-6 Results of the MyMeasures \<AWMNode> in cube.xml"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/mymeasrs.htm)  

Figure 3-7 shows the results of the unnamed child `<AWMNode>` of the `MyMeasures` `<AWMNode>` in the `cube.xml` document. The user has selected the UNITS measure in the MyMeasures folder. The property inspector displays the user interface specified by `MeasureViewerPlugin`. The plug-in displays the name of the measure.

Figure 3-7 Results of MeasureViewerPlugin

![Description of Figure 3-7 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/measview.gif "Description of Figure 3-7 follows")  
[Description of "Figure 3-7 Results of MeasureViewerPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/measview.htm)  

### CubeViewerPlugin Example

The `aw.xml` document in Example 3-7 has an `<AWMNode>` that specifies a folder named MyDims. For a description of the `MyDims` `<AWMNode>`, see "DimEditorPlugin Example".

The `aw.xml` document also has an `<AWMNode>` that specifies a folder named MyCubes and a SQL statement that selects the names of the cubes of the current analytic workspace from the USER\_CUBES table. An unnamed child `<AWMNode>` specifies the `CubeViewerPlugin`. Figure 3-8 shows the navigation tree folder and the display in the property inspector for the `MyCubes` `<AWMNode>`.

Example 3-7 Creating an aw.xml Document

```
<?xml version="1.0" encoding="US-ASCII" ?>
<AWMTree>
  <AWMNode name="MyDims"
           type="mydimfolder"
           viewSql="select dimension_name, dimension_type from user_cube_dimensions where aw_name = {aw_name}">
    <AWMNode type="dimobj"
             sql="select dimension_name from user_cube_dimensions where aw_name = {aw_name}"
             viewClass="plugin11202.DimEditorPlugin">
    </AWMNode>
      <AWMNode name="MyLevels"
               type="levelobj"
               sql="select level_name from user_cube_dim_levels where dimension_name = {dimobj}">
        <AWMNode sql="select * from user_cube_dim_levels where dimension_name = {dimobj} and level_name = {levelobj}"/>
      </AWMNode>
  </AWMNode>
  <AWMNode name="MyCubes"
           type="cubeobj"
           sql="select cube_name from user_cubes where aw_name = {aw_name}">
    <AWMNode type="mycubeview"
             viewClass="plugin11202.CubeViewerPlugin"/>
  </AWMNode>
</AWMTree>
```

Example 3-8 contains the `CubeViewerPlugin` class. The class displays the name of the currently selected cube, as shown in Figure 3-9.

Example 3-8 The CubeViewerPlugin Class

```
package plugin11202;
 
import java.awt.FlowLayout;
import java.sql.Connection;
import java.util.Map;
import javax.swing.JLabel;
import javax.swing.JPanel;
import oracle.olap.awm.plugin.ViewerPlugin;
 
public class CubeViewerPlugin implements ViewerPlugin
{
  public boolean isViewerForType(Connection conn, String name)
    throws Exception
  {
    return true;
  }
  
  public JPanel getPanel(Connection conn, String name, Map params)
    throws Exception
  {
    JPanel panel = new JPanel();
    panel.setLayout(new FlowLayout());
    // Get the name of the current cube.
    Object cubeobj = null;
    if (params != null)
      cubeobj = params.get("cubeobj");
    if (cubeobj instanceof String)
    {
      String cubeName = (String)cubeobj;
      panel.add(new JLabel(cubeName));
    }
    return panel;
  }
 
  public void cleanup(String name)
  {
  }
}
```

Figure 3-8 shows the results of the `MyCubes` `<AWMNode>` in the `aw.xml` document. A MyCubes folder appears in the GLOBAL analytic workspace folder. The user has selected the MyCubes folder. The result of the SQL statement of the `<AWMNode>` appears in the folder. The property inspector displays the same SQL statement and the result of it, which is a list of the cubes of the analytic workspace.

Figure 3-8 Results of the MyCubes \<AWMNode> in aw.xml

![Description of Figure 3-8 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/mycubes.gif "Description of Figure 3-8 follows")  
[Description of "Figure 3-8 Results of the MyCubes \<AWMNode> in aw.xml"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/mycubes.htm)  

Figure 3-9 shows the results of the unnamed child `<AWMNode>` of the `MyCubes` `<AWMNode>` in the `aw.xml` document. The user has selected the `UNITS_CUBE` cube in the MyCubes folder. The property inspector displays the user interface specified by `CubeViewerPlugin`. The plug-in displays the name of the cube.

Figure 3-9 Results of the CubeViewerPlugin

![Description of Figure 3-9 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/unitscube.gif "Description of Figure 3-9 follows")  
[Description of "Figure 3-9 Results of the CubeViewerPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/unitscube.htm)  

### DimEditorPlugin Example

The `aw.xml` document in Example 3-7 has an `<AWMNode>` that specifies a folder named MyDims and a SQL statement that selects the names and types of the dimensions of the current analytic workspace from the USER\_CUBE\_DIMENSIONS table. Figure 3-10 shows the navigation tree folder and the display in the property inspector for the `MyDims` `<AWMNode>`.

An unnamed child `<AWMNode>` specifies a SQL statement that selects the names of the dimensions and also specifies the `DimEditorPlugin`. Figure 3-11 shows the navigation tree folder and the display in the property inspector for the `MyDims` `<AWMNode>`.

The `<AWMNode>` named `MyLevels`, nested in the unnamed `<AWMNode>`, selects the names of the levels from the USER\_CUBE\_DIM\_LEVELS table for the currently selected dimension. The `MyLevels` `<AWMNode>` has an unnamed nested `<AWMNode>` that selects all columns from the USER\_CUBE\_DIM\_LEVELS table for the currently selected dimension and level.

Example 3-9 contains the `DimEditorPlugin` class. The class displays the name and the short description of the currently selected dimension, as shown in Figure 3-11. The user can change the value of the short description.

Example 3-9 The DimEditorPlugin Class

```
package plugin11202;
 
import java.awt.Component;
import java.awt.GridLayout;
import java.sql.Connection;
import java.util.Map;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import oracle.olap.awm.plugin.EditorPlugin;
import oracle.olap.awm.plugin.PanelChanged;
import oracle.olapi.metadata.mdm.MdmDescriptionType;
import oracle.olapi.metadata.mdm.MdmMetadataProvider;
import oracle.olapi.metadata.mdm.MdmObject;
import oracle.olapi.metadata.mdm.MdmPrimaryDimension;
 
public class DimEditorPlugin implements EditorPlugin
{
  private JTextField shortDescTextField;
  private PanelChanged parentPanelChanged;
  private JPanel panel;
  private JLabel dimNameLabel;
  private MdmDescriptionType mdmShortDescrDescrType;

  public DimEditorPlugin()
  {
    panel = new JPanel();
    panel.setLayout(new GridLayout(3, 1));
    dimNameLabel = new JLabel();
    panel.add(dimNameLabel);
    shortDescTextField = new JTextField();
    panel.add(new JLabel("Short Description:"));
    panel.add(shortDescTextField);
    shortDescTextField.getDocument().addDocumentListener(new DocumentListener()
        {
          public void insertUpdate(DocumentEvent e)
          {
            changed();
          }
 
          public void removeUpdate(DocumentEvent e)
          {
            changed();
          }
 
          public void changedUpdate(DocumentEvent e)
          {
            changed();
          }
        });
  }
 
  public boolean isViewerForType(Connection conn, String name)
    throws Exception
  {
    return true;
  }
 
  // Get the MdmMetadataProvider of the session.
  private MdmMetadataProvider getMetadataProvider(Map params)
  {
    Object dp = params.get("DATAPROVIDER");
    if (dp instanceof MdmMetadataProvider)
    {
      MdmMetadataProvider mdp = (MdmMetadataProvider)dp;
      return mdp;
    }
    return null;
  }
  
  // Get the currently selected dimension and the schema from the params Map.
  // Get the MdmMetadataProvider and get the MdmPrimaryDimension for the
  // dimension.
  private MdmPrimaryDimension getDimension(Map params)
  {
    Object obj = null;
    String schema = "";
    if (params != null)
    {
      obj = params.get("dimobj");
      schema = (String)params.get("schema");
    }
    if (obj instanceof String)
    {
      String dimName = (String)obj;
      MdmMetadataProvider mdp = getMetadataProvider(params);
      if (mdp != null)
      {
        MdmObject mobj = mdp.getMetadataObject(schema + "." + dimName);
        if (mobj != null && mobj instanceof MdmPrimaryDimension)
        {
          MdmPrimaryDimension dim = (MdmPrimaryDimension)mobj;
          return dim;
        }
        else
          System.out.println("Cannot get the " + dimName + " dimension.");
      }
    }
    return null;
  }
 
  // Get the dimension and the short description of it. 
  // Display the short description.
  private void read(Map params)
  {
    MdmPrimaryDimension dim = getDimension(params);
    if (dim != null)
    {
      dimNameLabel.setText(dim.getName());
      mdmShortDescrDescrType =
        MdmDescriptionType.getShortDescriptionDescriptionType();
      String shortDesc = dim.getDescription(mdmShortDescrDescrType);
      shortDescTextField.setText(shortDesc);
    }
  }
 
  public JPanel getPanel(Connection conn, String name, Map params)
    throws Exception
  {
    read(params);
    return panel;
  }
 
  public void cleanup(String name)
  {  
  }
 
  public boolean validate(Connection conn, Component parent, String name,
                          Map params)
    throws Exception
  {
    String invalidDescr = "foo";
    if (shortDescTextField.getText().equals(invalidDescr))
    {
      JOptionPane.showMessageDialog(parent, "Description cannot be " +
                                    invalidDescr + ".");
      return false;
    }
    return true;
  }
 
  public void revert(Connection conn, Component parent, String name,
                     Map params)
    throws Exception
  {
    read(params);
  }
 
  public void showHelp(Connection conn, Component parent, String name,
                       Map params)
    throws Exception
  {
    JOptionPane.showMessageDialog(parent, "In Help.");
  }
 
  public boolean save(Connection conn, Component parent, String name,
                      Map params)
    throws Exception
  {
    // Get the currently selected dimension and set the short description for 
    // it.
    MdmPrimaryDimension dim = getDimension(params);
    dim.setDescription(mdmShortDescrDescrType, shortDescTextField.getText());
    // Get the MdmMetadataProvider.
    MdmMetadataProvider mdp = getMetadataProvider(params);
    if (mdp == null)
      return false;
    // Get the DataProvider and the TransactionProvider and commit the current
    // Transaction. If the Transaction is not committable, roll it back.
    try
    {
      mdp.getDataProvider().getTransactionProvider().commitCurrentTransaction();
    }
    catch (Exception e)
    {
      JOptionPane.showMessageDialog(parent, e.getMessage(), "Error",
                                    JOptionPane.ERROR_MESSAGE);
      try
      {
        mdp.getDataProvider()
           .getTransactionProvider()
           .rollbackCurrentTransaction();
      }
      catch (Exception e2)
      {
        // Ignore the exception.
      }
    }
    return true;
  }
 
  public void setValueChanged(Connection conn, String name, Map params,
                              PanelChanged parentPanelChanged)
  {
    this.parentPanelChanged = parentPanelChanged;
  }
 
  
  // Calls the changed() method of the PanelChanged object supplied by
  // Analytic Workspace Manager when it calls the setValueChanged method.
  public void changed()
  {
    if (parentPanelChanged != null)
      parentPanelChanged.changed();
  }  
}
```

Figure 3-10 shows the results of the `MyDims` `<AWMNode>` in the `aw.xml` document. A MyDims folder appears in the GLOBAL analytic workspace folder. The user has selected the MyDims folder. The property inspector displays the SQL statement of the `MyDims` `<AWMNode>` and the result of it, which is a table that has columns headed DIMENSION\_NAME and DIMENSION\_TYPE. The rows of the columns contains the names of the dimensions of the analytic workspace and the types of the dimensions.

The `MyDims` `<AWMNode>` has an unnamed child `<AWMNode>` that has a SQL statement that retrieves the names of the dimensions. Those names appear in the MyDims folder in the navigation tree. The unnamed `<AWMNode>` also specifies the `DimEditorPlugin` plug-in.

Figure 3-10 Results of the MyDims \<AWMNode> in aw.xml

![Description of Figure 3-10 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/mydims.gif "Description of Figure 3-10 follows")  
[Description of "Figure 3-10 Results of the MyDims \<AWMNode> in aw.xml"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/mydims.htm)  

Figure 3-11 shows the Analytic Workspace Manager user interface after a user has selected the CHANNEL dimension in the MyDims folder in the navigation tree. The property inspector displays the user interface specified by `DimEditorPlugin`. The user interface includes a text field in which the user can change the value of the short description attribute.

Figure 3-11 Results of DimEditorPlugin

![Description of Figure 3-11 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/dimeditr.gif "Description of Figure 3-11 follows")  
[Description of "Figure 3-11 Results of DimEditorPlugin"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/dimeditr.htm)  

Figure 3-12 shows the result of the `MyLevels` `<AWMNODE>` that is the child of the `MyDims` `<AWMNODE>` in the `aw.xml` document. The SQL statement of the `MyLevels` `<AWMNode>` selects the LEVEL\_NAME column from the USER\_CUBE\_DIM\_LEVELS table for the currently selected dimension. Figure 3-12 shows the navigation tree folder with the MyLevels folder selected in the CHANNEL folder. In the property inspector is the result of the query.

Figure 3-12 Result of MyLevels \<AWMNode> Under MyDims in aw.xml

![Description of Figure 3-12 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/mydims_mylevels.gif "Description of Figure 3-12 follows")  
[Description of "Figure 3-12 Result of MyLevels \<AWMNode> Under MyDims in aw.xml"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/mydims_mylevels.htm)  

Figure 3-13 shows the result of the unnamed `<AWMNODE>` that is the child of the `MyLevels` `<AWMNODE>` in the `aw.xml` document. The SQL statement of the unnamed `<AWMNode>` selects all columns from the USER\_CUBE\_DIM\_LEVELS table for the currently selected dimension and level. Figure 3-13 shows the navigation tree folder with the TOTAL level selected in the MyLevels folder in the CHANNEL folder. The property inspector displays the result of the query.

Figure 3-13 Results of the Nested \<AWMNode> in the MyLevels \<AWMNode> in aw.xml

![Description of Figure 3-13 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/total_level.gif "Description of Figure 3-13 follows")  
[Description of "Figure 3-13 Results of the Nested \<AWMNode> in the MyLevels \<AWMNode> in aw.xml"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/total_level.htm)  

## Example of Plug-in Descriptions

As discussed in ["Describing the Available Plug-ins"](pluginintro.md), the `awmplugin.xml` file contains descriptions of Java plug-ins that Analytic Workspace Manager displays. Figure 3-14 shows the Plugins tab of the About dialog box with the information that is specified by the `awmplugin.xml` document in Example 3-10.

Figure 3-14 Plugins Tab in the About Dialog Box

![Description of Figure 3-14 follows](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img/awmplugin.gif "Description of Figure 3-14 follows")  
[Description of "Figure 3-14 Plugins Tab in the About Dialog Box"](https://docs.oracle.com/cd/E11882_01/olap.112/e17237/img_text/awmplugin.htm)  

Example 3-10 shows the `awmplugin.xml` document that produces the result shown in Figure 3-14.

Example 3-10 Creating an awmplugins.xml Document

```
<?xml version="1.0" encoding="utf-8" ?>
<AWMPlugins>
  <Plugin name="Cube Viewer Plug-in" version="1.0"
          class="plugin11202.CubeViewerPlugin">
    <Description>Displays the name of a cube.</Description>
  </Plugin>
  <Plugin name="Level Viewer Plug-in" version="1.0"
          class="plugin11202.LevelViewerPlugin">
    <Description>Displays the name of a level.</Description>
  </Plugin>
  <Plugin name="Measure Viewer Plug-in" version="1.0"
          class="plugin11202.MeasureViewerPlugin">
    <Description>Displays the name of a measure.</Description>
  </Plugin>
  <Plugin name="Delete Dimension Plug-in" version="2.0"
          class="plugin11202.DeleteDimPlugin">
    <Description>Deletes a dimension in the MyDims folder.</Description>
  </Plugin>
  <Plugin name="Edit Dimension Plug-in" version="2.0"
          class="plugin11202.DimEditorPlugin">
    <Description>Edits the short description of a dimension.</Description>
  </Plugin>
  <Plugin name="View XML Plug-in" version="1.0" class="plugin11202.ViewXMLPlugin">
    <Description>Displays the XML for an OLAP measure.</Description>
  </Plugin>
</AWMPlugins>
```