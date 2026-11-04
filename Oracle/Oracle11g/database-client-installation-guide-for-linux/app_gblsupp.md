---
title: Configuring Oracle Database Globalization Support
book: Database Client Installation Guide for  Linux
doc_id: E24322-14
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e24322/app_gblsupp.htm
tags:
  - oracle
  - 11g
  - database-client-installation-guide-for-linux
---

## B Configuring Oracle Database Globalization Support

This appendix describes the following Globalization Support topics:

- Installing and Using Oracle Components in Different Languages
- Running Oracle Universal Installer in Different Languages

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch1overview.htm#NLSPG001) for an overview of globalization support for Oracle Database

## B.1 Installing and Using Oracle Components in Different Languages

This section describes the following procedures:

- Configuring Oracle Components to Run in Different Languages
- Installing Translation Resources

### B.1.1 Configuring Oracle Components to Run in Different Languages

You can specify the language and the territory, or locale, in which you want to use Oracle components. The locale setting of a component determines the language of the user interface of the component and the globalization behavior, such as date and number formatting. Depending on the Oracle component, the locale of the component is either inherited from the operating system session that started the component, or is defined by the `NLS_LANG` environment variable.

The operating system locale usually influences Oracle components that are based on Java technology. The `NLS_LANG` environment variable usually influences Oracle components that use Oracle Database Client libraries such as OCI.

Note:

The user interface of an Oracle component is displayed in a selected language only if the appropriate translation is available and has been installed. Else, the user interface is be displayed in English.

#### B.1.1.1 Determining the Operating System Locale by Using the LANG Environment Variable

The locale setting of your operating system session determines the language of the user interface and the globalization behavior for components such as Oracle Universal Installer, Oracle Net Configuration Assistant, and Oracle Database Configuration Assistant. It also determines the globalization behavior of Oracle Database sessions created by a user application through Oracle JDBC driver, unless overridden by the application.

The operating system locale is determined by the value of the `LANG` environment variable. Depending on your desktop environment, such as KDE, GNOME, or telnet, you can select a default session locale on a login screen, in a configuration panel, or in a configuration file.

Note:

Refer to the operating system documentation on how to select a locale for the operating system session in your desktop environment.

You can modify the `LANG` variable in the environment of your shell to start an Oracle component in a selected language. For example, to start Oracle Database Configuration Assistant in German, enter one of the following commands:

- Bourne shell (sh), or Korn shell (ksh), or Bash shell (bash):
	```
	$ LANG=de_DE.iso88591 dbca
	```
- C shell (csh):
	```
	% (setenv LANG de_DE.iso88591; dbca)
	```

To modify the operating system locale for all Oracle components started from now on by the given shell, modify the `LANG` variable using one of the following commands:

- Bourne shell (sh), or Korn shell (ksh), or Bash shell (bash):
	```
	$ LANG=de_DE.iso88591; export LANG
	$ ...
	```
- C shell (csh):
	```
	$ setenv LANG de_DE.iso88591
	$ ...
	```

The value of the `LANG` environment variable must be a valid operating system locale. To see the list of valid locales, enter the following command:

```
$ locale -a
```

Note:

Refer to the operating system documentation for a mapping between values of the `LANG` environment variable and the languages and territories that they represent.

#### B.1.1.2 Configuring Locale and Character Sets Using NLS\_LANG

The `NLS_LANG` environment variable determines the language of the user interface and the globalization behavior for components such as SQL\*Plus, exp, and imp. It sets the language and territory used by the client application and the database user session. It also declares the character set for entering and displaying data by the client application.

The `NLS_LANG` environment variable uses the following format:

```
NLS_LANG=language_territory.characterset
```

In this format:

- `language` specifies the language used for displaying Oracle messages, sorting, day names, and month names
- `territory` specifies the conventions for default date, monetary and numeric formats
- `characterset` specifies the encoding used by the client application
	In most cases, this is the Oracle character set that corresponds to the character set of the user terminal or the operating system.

Note:

To install additional languages for a component, you must reinstall this component.

The `NLS_LANG` environment variable is set as a local environment variable for the shell on all UNIX-based platforms. For example, if the operating system locale setting is `en_US.UTF-8`, then the corresponding value of `NLS_LANG` environment variable is `AMERICAN_AMERICA.AL32UTF8`.

See Also:

Oracle Database Globalization Support Guide for information about the `NLS_LANG` parameter and Globalization Support initialization parameters

The following examples illustrate some valid values for the `NLS_LANG` environment variable.

Note:

Refer to the operating system documentation on how to determine the operating system locale environment setting.

| Operating System Locale | `NLS_LANG` Values |
| --- | --- |
| French (France) | FRENCH\_FRANCE.WE8ISO8859P15   FRENCH\_FRANCE.WE8ISO8859P1   FRENCH\_FRANCE.WE8MSWIN1252   FRENCH\_FRANCE.AL32UTF8 |
| Japanese (Japan) | JAPANESE\_JAPAN.JA16EUC   JAPANESE\_JAPAN.JA16SJIS   JAPANESE\_JAPAN.AL32UTF8 |

### B.1.2 Installing Translation Resources

To view the user interface of Oracle components in different languages, you must install the appropriate language translations along with the component.

To install the translation resources:

1. Start Oracle Universal Installer.
2. In the Configure Security Updates screen enter the relevant information and click Next.
3. In the Download Software Updates and Apply Software Updates screens, enter the relevant information and click Next.
4. In the Select Installation Option screen, select the installation option and click Next.
5. In the System Class screen, select the type of system class for installing the database, and click Next.
6. In the Grid Installation Options screen, select the type of database installation you want to perform, and click Next.
7. In the Select Product Languages screen, select the language in which you want to use Oracle components from the Available Languages field.
	Note:
	The Available Languages field lists all languages supported by Oracle globalization libraries. The set of languages for which a translation is actually available is usually smaller and depends on a particular component. The scope of translation for a given component may differ between languages. For example, some translations may include all user interface text, while others may include only error messages and no help files.
8. Use the > arrow to move the selected language to the Selected Languages field, and then click Next.
	Note:
	Oracle Universal Installer ignores languages in the Selected Languages field for which translation is not available.

## B.2 Running Oracle Universal Installer in Different Languages

Your operating system locale determines the language in which Oracle Universal Installer runs. Oracle Universal Installer may run in one of the following languages:

- Brazilian Portuguese (`pt_BR`)
- French (`fr`)
- German (`de`)
- Italian (`it`)
- Japanese (`ja`)
- Korean (`ko`)
- Simplified Chinese (`zh_CN`)
- Spanish (`es`)
- Traditional Chinese (`zh_TW`)

To run Oracle Universal Installer in one of the available languages, change the locale in which your operating system session is running before you start Oracle Universal Installer with the.`/runInstaller` command. If the selected language is not one of the listed earlier, then Oracle Universal Installer runs in English.

You must ensure that the selected value for the `LANG` environment variable starts with the appropriate language abbreviation. In the aforementioned list of languages, in which Oracle Universal Installer can run, the required abbreviation appears in parentheses beside the language name. For example, fr\_FR and fr\_CA are valid values to run the Oracle Universal Installer in French.