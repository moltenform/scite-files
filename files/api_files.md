
[Back to scite-files home](../README.md)

[Built-in languages](#built_in_languages)

[API Files and properties](#api_files_and_properties)

[How to install a properties file](#how_to_install_properties)

[How to install an api file and enable calltips](#how_to_install_api)

[How to make an api file](#how_to_make_api)

<a name="built_in_languages"></a>
### Built-in languages

These languages are recognized by SciTE and enabled by default:

Ada, Assembler (NASM, MASM), AutoIt, Batch files (MS-DOS), Bash, C/C++/C#, conf (Apache), CSS, D, diff files, Flash (ActionScript), Fortran, Gettext, Go, HTML, HTML with embedded JavaScript, VBScript, PHP and ASP, IDL, MSIDL, XPIDL, INI, Java, JavaScript, LISP, Lua, Make, Matlab, MSSQL, Objective C, Objective Caml, Octave, Pascal/Delphi, Perl, PostScript, Python, Registry, Ruby, Scheme, SQL and PLSQL, S-Record, Swift, Tcl/Tk, Vala, VB and VBScript, XML, and YAML

<!-- I don't see this in properties files: Clarion, Progress, Asymptote, TADS3, Gui4Cli, PL/M -->

These languages are recognized by SciTE but are not enabled by default:

Abaqus, Baan, BlitzBasic, Bullant, Avenue (Ave), Asl (ACPI Source), ASN.1 MIB, AutoIt, AviSynth, cmake, COBOL, Coffeescript, CSound, Ecl, Eiffel, Erlang, E-Script, Flagship (Clipper / XBase), Forth, Freebasic, GAP, Haskell, Intel HEX, InnoSetup, JSON and JSON-LD, KiXtart, TeX and LaTeX, LOT, Lout, Metapost, MMIXAL,, Modula 3, Nimrod, nnCron, NSIS, Opal, OScript, POV-Ray, PowerBasic, PowerShell, PowerPro, , PostScript, PureBasic, R, Rebol, Rust, scriptol, Smalltalk, SORCUS Installation, Spice, Specman E, TACL, TAL, txt2tags, Verilog, VHDL

To enable one of these languages,

* Select "Open Global Options File" from the Options menu

* Scroll to the end of this file and look for the line that begins with `imports.exclude=`

* Delete a word in this list. For example, to enable Haskell, delete the word "haskell"

* Save this file and restart SciTE (may require sudo privileges on Unix systems)

<a name="api_files_and_properties"></a>
### API Files and properties

* C, C++

    * [C standard library](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c.api)
    * [C standard library](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c_withdoc.zip) with short doc strings
    * [Windows API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/cpp.api.zip)
    * [OpenGL API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/opengl.zip)
    * [OpenGL 4.4 API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/opengl4.4.zip)
    * [Glut API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/glut.zip)
    * [SDL API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/sdl.api)

* JavaScript, CSS, web

    * [CSS, JavaScript, and JQuery api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/css,js,jquery.zip)
    * [PHP, abbreviations, CSS, JavaScript, and JQuery](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/css,js,jquery,php.zip)

* APDL

    * [APDL properties and API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/apdl.zip)

* ASP

    * [ASP API methods](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/asp.api)
    * Edit html.properties to set the language of scripts in ASP code
        * If asp.default.language=1, script in an ASP code block is JavaScript
        * If asp.default.language=2, script in an ASP code block is VBScript
        * If asp.default.language=3, script in an ASP code block is Python

* Auto Hotkey 

    * [AutoHotkey properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/ahk.properties)
    * [SciTE4AutoHotkey](https://github.com/fincs/SciTE4AutoHotkey) custom SciTE build for ahk

* Auto It3 

    * [SciTE4AutoIt3 Website containing Auto It3 related properties and API files.](https://www.autoitscript.com/site/autoit-script-editor/)

* Batch Scripting (Windows)

    * [Batch API Files](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/batch.api.zip) (API files for NT, XP/2003, GNUWin32 and SysInternals commands)

* C# 

    * [C# api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c_sharp.api.zip)

* CIL 

    * [Properties for CIL/MSIL](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/il.properties)

* Clojure

    * [Properties for Clojure](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/clojure.api)

* CMake

    * [CMake API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/cmake.api)

* FORTRAN 

    * [Standard FORTRAN API functions](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/fortran.api)

* Java 

    * [Java API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/java.api.zip)
    * [Java API, complete 1.5 and 1.6 api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/javaversions.api.zip)
    * [Java API and Java Help](http://www.burgaud.com/scite.php)

* Lua 

    * [Lua 5.0 C API and Lua functions](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/lua5.api.zip)
    * [Api for SciTE extension scripts](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/lua_scite_extension.api)

* Microsoft SQL 

    * [Replaces sql.properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/mssql.properties)

* nncron

    * [nncron.api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/nncron.api) 

* Octave

    * [octave.api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/octave.api)

* Oracle 

    * [Extended properties file](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/sql_more.properties) with additional keywords and standard package names
    * [sql plsql](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/sql_plsql.api.zip) properties file
    
* OScript

    * [oscript.api.zip](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/oscript.api.zip)

* Pascal / Delphi[API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/pascal.api) 

    * [Abbreviations](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/pascal.abbrev) 
    * [Delphi api files and abbrevs](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/delphi_extras.zip) 

* Perl 

    * [Perl API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/perl.api)
    * [Parrot properties file](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/parrot_properties.zip)

* PHP 

    * [php.api, latest PHP 5](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/php.api)
    * [php.api in Spanish, PHP 5](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/php-es.api)
    * [PHP properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/php.properties)
    * [PHP functions](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/phpfunctions.properties)

* POV-Ray 

    * [POV-Ray API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/pov.api)

* Progress

    * [Progress properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/progress.properties)

* Python

    * [Python script to print variables on exception or breakpoint](api_files_py_debug.md)

* TADS3 

    * [TADS3 property file and explanation](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/tads3.zip)
    
* Windows Scripting 

    * [Properties files](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/windows_scripting.zip)
    * [More files and scripts](api_files_win_scripting.md)

* AMPL

    * [Properties file, api file, tools and setup instructions.](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/ampl.zip)

* Asymptote

    * [Properties file](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/asymptote.properties)

To contribute a file to this list, send an e-mail to scitewiki at gmail dot com or submit a pull request. 

<a name="how_to_install_properties"></a>
### How to install a properties file

* Properties files can change colors and fonts, specify lists of keywords, define what action to take on "Compile" and "Go", map file extensions to a programming language, and more

* In Windows, move the .properties file into the directory that contains SciTE.exe

* In Linux, move the .properties file into the directory that contains SciTEGlobal.properties. This is typically either /usr/bin/scite or /usr/local/bin/scite.

<a name="how_to_install_api"></a>
### How to install an api file and enable calltips

* As an example, let's set up the api file for C

* Download and uncompress [c_withdoc.zip](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c_withdoc.zip)

* In Windows, move c_withdoc.api into the directory that contains SciTE.exe

* In Linux, move c_withdoc.api into the directory that contains SciTEGlobal.properties. This is typically either /usr/bin/scite or /usr/local/bin/scite.

* Open SciTE

* From the Options menu, select Open User Options File

* Add the line `api.$(file.patterns.cpp)=$(SciteDefaultHome)/c_withdoc.api`

* Save this file and restart SciTE

* In SciTE, create and open a new file "test.c"

* Calltips

    * Type the text "fputs("
    
    * As soon as you press (, a calltip appears, showing a description of fputs
    
* Completion

    * On an empty line, type the text "fp" and press Ctrl+Space
    
    * A listbox appears allowing you to choose between fprintf, fputc, and fputs
    
    * You can use the arrow keys can navigate this box and Enter to choose an item from this box

<a name="how_to_make_api"></a>
### How to make an api file

An api file is a plain text file with one entry per line.

You can generate api files for your own source code, one of these tools may be helpful:

* For C/C++ headers, an API file can be generated using [ctags](http://ctags.sourceforge.net/) and then the [tags2api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/tags2api.py) Python script (which assumes C/C++ source) on the tags file to grab complete multiple line function prototypes. Some common headers surround parameter lists with a __P macro and may have comments. The [cleanapi](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/cleanapi.cc) utility may be used on these files
* For Python modules, there is a [gen_python](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_python_api.py) script
* For Python 3, there is a [gen_python_3](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_python_3_api.py) script
* For Java classes, there is a [ApiBuilder.java](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/java_ApiBuilder.java) program
* For C# classes, use [genapi.cs](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_csgenapi.zip)
* For PHP, use [php-api-generator](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/gen_php-api-generator.zip) or [phpapi.php](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_gen/phpapi.php.txt)

Search for "calltip" in the [SciTE Documentation](http://www.scintilla.org/SciTEDoc.html) for more information.


