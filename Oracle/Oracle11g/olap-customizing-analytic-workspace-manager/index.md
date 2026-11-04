---
title: Index
book: OLAP Customizing Analytic Workspace Manager
doc_id: E17237-01
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/olap.112/e17237/index.htm
tags:
  - oracle
  - 11g
  - olap-customizing-analytic-workspace-manager
---

A B C D E F G H I J L M N O P R S T U V X

---

## Symbols

`$`

`{}`

---

## A

Analytic Workspace Manager

`aw` parameter

`AWMCalcs` element

`awmcalcs.xml` document

`AWMNode` element

of an `AWMTree` element, [1.1.6.2](olawxml.md)

`AWMPlugin` interface

examples of, [3.2.1](pluginexamples.md), [3.2.2](pluginexamples.md)

implementations loaded on startup, [2.1.2](pluginintro.md)

specification, [2.2](pluginintro.md)

`AWMPlugins` element

root of a plug-in description, [2.5.2.1](pluginintro.md)

`awmplugin.xml` document

description, [2.5](pluginintro.md)

example of, [3.4](pluginexamples.md)

`AWMTree` element

root of a SQL report, [1.1.6.1](olawxml.md)

`AWMTree` prefix

for `type` parameter values, [2.2.1](pluginintro.md)

`awmtree.xml` document

example of, [1.1.2](olawxml.md), [1.1.3](olawxml.md), [1.1.4](olawxml.md)

in downloadable examples, [3.1](pluginexamples.md)

location in directory, [1.1.1](olawxml.md)

location in navigation tree, [1.1.5](olawxml.md)

`aw.xml` document

example of, [3.3.3](pluginexamples.md)

location in navigation tree, [1.1.5](olawxml.md)

---

## B

bind variables

enclosed by braces, [1.1.4](olawxml.md), [1.2.5.2](olawxml.md)

for an `AWMPlugin`, [2.2.2.2](pluginintro.md)

in calculation templates, [1.2.2](olawxml.md), [1.2.5.2](olawxml.md)

in custom reports, [1.1.4](olawxml.md)

referencing using lower case, [2.2.2.2](pluginintro.md)

replacing values in a `WHERE` clause, [1.1.1](olawxml.md)

replacing values in a `WHERE` clause, example of, [1.1.4](olawxml.md)

`BIND_MAP` `Map`

for an `AWMPlugin`, [2.2.2.2](pluginintro.md)

keys and values, examples of, [2.2.3](pluginintro.md)

braces

enclosing bind variable, [1.1.4](olawxml.md), [1.2.5.2](olawxml.md)

enclosing hypertext parameters, [1.2.5.2](olawxml.md)

---

## C

`Calc` element

of an `AWMCalcs` element, [1.2.5.2](olawxml.md)

`CalcOptional` element

of a `Calc` or a `CalcOptionalDefinitions` element, [1.2.5.3](olawxml.md)

supporting calculation options, [1.2.3](olawxml.md)

`CalcOptionalDefinitions` element

applying options to all calculations, [1.2.3](olawxml.md)

of a `AWMCalcs` element, [1.2.5.4](olawxml.md)

calculation templates

adding options, [1.2.3](olawxml.md)

description, [1.2](olawxml.md)

example of, [1.2.2](olawxml.md)

`Category` element

of an `AWMCalcs` element, [1.2.5.5](olawxml.md)

`changed` method, [2.3.2](pluginintro.md), [2.4](pluginintro.md)

`class` attribute

of a `Plugin` element, [2.5.2.2](pluginintro.md)

`cleanup` method, [2.3.1](pluginintro.md), [2.4](pluginintro.md)

configuring Analytic Workspace Manager for plug-ins, [2.1.1](pluginintro.md)

`conn` parameter

of `AWMPlugin` methods, [2.2](pluginintro.md)

of `ViewerPlugin` methods, [2.3.1](pluginintro.md)

`Connection` object, [2.1.2](pluginintro.md)

`CubeViewerPlugin` class, [3.3.3](pluginexamples.md)

`cube.xml` document

example of, [3.3.2](pluginexamples.md)

location in navigation tree, [1.1.5](olawxml.md)

custom calculations, [1.2](olawxml.md)

custom SQL reports

adding to navigation tree, [1.1](olawxml.md)

example, [1.1.2](olawxml.md), [1.1.3](olawxml.md), [1.1.3](olawxml.md), [1.1.4](olawxml.md)

`customizingAWM_examples11202.zip` file

containing example code, [3.1](pluginexamples.md)

---

## D

`default` attribute

of a `Param` element, [1.2.5.7](olawxml.md)

`DeleteDimPlugin` class, [3.2.2](pluginexamples.md)

`description` attribute

of a `Calc` element, [1.2.5.2](olawxml.md)

of a `Category` element, [1.2.5.5](olawxml.md)

`Description` element

of an `AWMPlugins` element, [2.5.2.3](pluginintro.md)

`DimEditorPlugin` class, [3.3.4](pluginexamples.md)

`dimension.xml`

example of, [3.3.1](pluginexamples.md)

location in navigation tree, [1.1.5](olawxml.md)

dollar sign

---

## E

`EditorPlugin` interface

examples of, [3.3.4](pluginexamples.md)

specification, [2.3.2](pluginintro.md)

enabling plug-ins, [2.1.1](pluginintro.md)

examples

downloadable, [3.1](pluginexamples.md)

of `awmcalcs.xml`, [1.2.2](olawxml.md), [1.2.3](olawxml.md), [1.2.4](olawxml.md)

of `AWMPlugin`, [3.2.1](pluginexamples.md), [3.2.2](pluginexamples.md)

of `awmplugin.xml`, [3.4](pluginexamples.md)

of `awmtree.xml`, [1.1.2](olawxml.md), [1.1.3](olawxml.md), [1.1.4](olawxml.md)

of `aw.xml`, [3.3.3](pluginexamples.md)

of `cube.xml` document, [3.3.2](pluginexamples.md)

of `dimension.xml`, [3.3.1](pluginexamples.md)

of `EditorPlugin`, [3.3.4](pluginexamples.md)

of `schema.xml`, [1.1.5](olawxml.md)

of `ViewerPlugin`, [3.3.1](pluginexamples.md), [3.3.2](pluginexamples.md), [3.3.3](pluginexamples.md)

`expression` attribute

of a `Calc` element, [1.2.5.2](olawxml.md)

of a `CalcOptional` element, [1.2.5.3](olawxml.md)

of an `Item` element, [1.2.5.6](olawxml.md)

expression syntax, [1.2.1](olawxml.md)

---

## F

folders

creating in navigation tree, [1.1.3](olawxml.md)

---

## G

`getMenu` method, [2.1.2.1](pluginintro.md), [2.2](pluginintro.md), [2.4](pluginintro.md)

`getPanel` method, [2.3.1](pluginintro.md), [2.3.2](pluginintro.md), [2.4](pluginintro.md)

---

## H

`handle` method, [2.1.2.1](pluginintro.md), [2.2](pluginintro.md), [2.4](pluginintro.md)

headings

for XML documents, [1.1.1](olawxml.md), [1.2.1](olawxml.md), [2.5.1](pluginintro.md)

hypertext parameters

creating links by using, [1.2.2](olawxml.md)

enclosed by braces, [1.2.5.2](olawxml.md)

referencing two or more, [1.2.5.2](olawxml.md)

---

## I

`icon` attribute

example of, [1.1.5](olawxml.md)

of an `AWMNode` element, [1.1.6.2](olawxml.md)

icons

in JAR file, [1.1.5](olawxml.md)

in JAR file, example of, [1.1.5](olawxml.md)

`isSupported` method, [2.1.2.1](pluginintro.md), [2.2](pluginintro.md), [2.4](pluginintro.md)

`isViewerForType` method, [2.3.1](pluginintro.md), [2.3.2](pluginintro.md), [2.4](pluginintro.md)

`Item` element

of a `Param` element, [1.2.5.6](olawxml.md)

---

## J

JAR files

containing multiple XML documents and plug-ins, [2.4](pluginintro.md)

directory structure of, [1.1.5](olawxml.md)

files for icons included in, [1.1.5](olawxml.md)

loaded on startup, [2.4](pluginintro.md)

location for, [2.4](pluginintro.md)

required by plug-ins, [2.4](pluginintro.md)

---

## L

leaf element

defined, [1.1.4](olawxml.md)

`LevelViewerPlugin` class, [3.3.1](pluginexamples.md)

---

## M

`MeasureViewerPlugin` class, [3.3.2](pluginexamples.md)

---

## N

`name` attribute

of a `Calc` element, [1.2.5.2](olawxml.md)

of a `CalcOptional` element, [1.2.5.3](olawxml.md)

of a `Category` element, [1.2.5.5](olawxml.md)

of a `Param` element, [1.2.5.7](olawxml.md)

of a `Plugin` element, [2.5.2.2](pluginintro.md)

of an `AWMNode` element, [1.1.6.2](olawxml.md)

`name` parameter

of `ViewerPlugin` methods, [2.3.1](pluginintro.md)

---

## O

`obj` parameter

of `AWMPlugin` methods, [2.2](pluginintro.md), [2.2.1](pluginintro.md)

OLAP expression syntax, [1.2.1](olawxml.md)

options

adding to calculation templates, [1.2.3](olawxml.md)

Oracle Technology Network (OTN), [3.1](pluginexamples.md), [3.1](pluginexamples.md)

---

## P

`Param` element

of a `Calc` or a `Params` element, [1.2.5.7](olawxml.md)

`Params` element

of an `AWMCalcs` element, [1.2.5.8](olawxml.md)

`params` parameter

keys and values for a `ViewerPlugin` and `EditorPlugin`, [2.3.3](pluginintro.md)

keys and values for a `ViewerPlugin`, examples of, [2.3.4.1](pluginintro.md)

keys and values for an `AWMPlugin`, [2.2.2](pluginintro.md)

keys and values for an `AWMPlugin`, examples of, [2.2.3](pluginintro.md)

keys and values for an `EditorPlugin`, examples of, [2.3.4.2](pluginintro.md)

of `AWMPlugin` methods, [2.2](pluginintro.md)

of `ViewerPlugin` methods, [2.3.1](pluginintro.md)

`parent` parameter

of `AWMPlugin` methods, [2.2](pluginintro.md)

of `EditorPlugin` methods, [2.3.2](pluginintro.md)

plug-in descriptions

creating, [2.5.1](pluginintro.md)

example of, [3.4](pluginexamples.md)

plug-in directory

specifying, [2.1.1](pluginintro.md)

`Plugin` element

of an `AWMPlugins` element, [2.5.2.2](pluginintro.md)

`plugin11202` package, [1.1.5](olawxml.md)

`plugin11202.jar` file

containing example plug-ins, [3.1](pluginexamples.md)

plug-ins

descriptions of, [2.5.1](pluginintro.md)

enabling, [2.1.1](pluginintro.md)

examples of, [3.2.1](pluginexamples.md), [3.2.2](pluginexamples.md), [3.3.1](pluginexamples.md), [3.3.2](pluginexamples.md), [3.3.3](pluginexamples.md), [3.3.4](pluginexamples.md)

including package when specifying, [1.1.5](olawxml.md)

prerequisites for creating, [2.4](pluginintro.md)

providing descriptions of, [2.5](pluginintro.md)

---

## R

refreshing the navigation tree, [2.1.2.1](pluginintro.md)

`refreshTree` method, [2.1.2.1](pluginintro.md), [2.2](pluginintro.md), [2.4](pluginintro.md)

reports

See SQL reports

`revert` method, [2.3.2](pluginintro.md), [2.4](pluginintro.md)

root element

of a calculation template, [1.2.5.1](olawxml.md)

of a plug-in description, [2.5.2.1](pluginintro.md)

of a SQL report, [1.1.6.1](olawxml.md)

run-time selections

stored by `type` parameter of `AWMNode`, [1.1.4](olawxml.md)

---

## S

`save` method, [2.3.2](pluginintro.md), [2.4](pluginintro.md)

`schema.xml` document

example of, [1.1.5](olawxml.md)

location in navigation tree, [1.1.5](olawxml.md)

`setValueChanged` method, [2.3.2](pluginintro.md), [2.4](pluginintro.md)

`showHelp` method, [2.3.2](pluginintro.md)

`ShowIfQueryTrue` element

of an `AWMNode` element, [1.1.6.3](olawxml.md)

`sql` attribute

of a `ShowIfQueryTrue` element, [1.1.6.3](olawxml.md)

of an `AWMNode` element, [1.1.6.2](olawxml.md)

SQL reports

adding to navigation tree, [1.1](olawxml.md)

creating in object folders, [1.1.5](olawxml.md), [1.1.5](olawxml.md)

creating XML documents for, [1.1.1](olawxml.md)

examples, [1.1.2](olawxml.md), [1.1.3](olawxml.md), [1.1.3](olawxml.md), [1.1.4](olawxml.md)

XML document structure, [1.1.6](olawxml.md)

syntax for expressions, [1.2.1](olawxml.md)

---

## T

`text` attribute

of a `CalcOptional` element, [1.2.5.3](olawxml.md)

of an `Item` element, [1.2.5.6](olawxml.md)

`type` attribute

of a `CalcOptional` element, [1.2.5.3](olawxml.md)

of a `Param` element, [1.2.5.7](olawxml.md)

of an `AWMNode` element, [1.1.6.2](olawxml.md)

`type` parameter

of an `AWMNode`, storing run-time selection, [1.1.4](olawxml.md)

of `AWMPlugin` methods, [2.2](pluginintro.md), [2.2.1](pluginintro.md)

---

## U

`ui` attribute

of a `Calc` element, [1.2.5.2](olawxml.md)

---

## V

`validate` method, [2.3.2](pluginintro.md), [2.4](pluginintro.md)

`version` attribute

of a `Plugin` element, [2.5.2.2](pluginintro.md)

`ViewerPlugin` interface

`viewSql` attribute

of an `AWMNode` element, [1.1.6.2](olawxml.md)

`ViewXMLPlugin` class, [3.2.1](pluginexamples.md)

---

## X

XML documents

XML formats