

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

<!-- I don't see this in properties files: Clarion, Progress,Asymptote, TADS3, Gui4Cli, PL/M -->

These languages are recognized by SciTE but are not enabled by default:

Abaqus, Baan, BlitzBasic, Bullant, Avenue (Ave), Asl (ACPI Source), ASN.1 MIB, AutoIt, AviSynth, cmake, COBOL, Coffeescript, CSound, Ecl, Eiffel, Erlang, E-Script, Flagship (Clipper / XBase), Forth, Freebasic, GAP, Haskell, Intel HEX, InnoSetup, JSON and JSON-LD, KiXtart, TeX and LaTeX, LOT, Lout, Metapost, MMIXAL,, Modula 3, Nimrod, nnCron, NSIS, Opal, OScript, POV-Ray, PowerBasic, PowerShell, PowerPro, , PostScript, PureBasic, R, Rebol, Rust, scriptol, Smalltalk, SORCUS Installation, Spice, Specman E, TACL, TAL, txt2tags, Verilog, VHDL

To enable one of these languages,

* Select "Open Global Options File" from the Options menu

* Scroll to the end of this file and look for the line that begins with `imports.exclude=`

* Delete a word in this list. For example, to enable Haskell, delete the word "haskell".

* Save this file and restart SciTE (may require sudo privileges on Unix systems)

<a name="api_files_and_properties"></a>
### API Files and properties

* C, C++

    * [C standard library](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c.api)
    * [C standard library](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/c_withdoc.zip) with short doc strings
    * [Windows API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/cpp.api.zip)
    * [OpenGL API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/opengl.zip)
    * [Glut API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/glut.zip)
    * [SDL API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/sdl.api)

* JavaScript, CSS, web

    * [Customization_BetterCssProperties A better CSS properties file]
    * [CSS, JavaScript, and JQuery api](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/css,js,jquery.zip)
    * [PHP, abbreviations, CSS, JavaScript, and JQuery](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/css,js,jquery,php.zip)

* APDL

    * [APDL properties and API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/apdl.zip)

* ASP

    * [ASP API methods](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/asp.api)
    * Set asp.default.language in html.properties to choose between VbScript or JScript in asp block.

* Auto Hotkey 

    * [AutoHotkey properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/ahk.properties)
    * [SciTE4AutoHotkey](http://www.autohotkey.net/~fincs/SciTE4AutoHotkey_3/web/) custom SciTE build for ahk.

* Auto It3 

    * [SciTE4AutoIt3 Website containing Auto It3 related properties and API files.](http://www.autoitscript.com/autoit3/scite)

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

* Go

    * [Properties for Go Programming](http://go-lang.cat-v.org/text-editors/scite/)

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

    * [Extended properties file](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/sql.properties_ext) with additional keywords and standard package names
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

    * [html.properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/html.properties)
    * [php.api, latest PHP 5](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/php.api)
    * [php.api in Spanish, PHP 5](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/php-es.api)
    * [PHP properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/php.properties)
    * [PHP functions](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/phpfunctions.properties)

* POV-Ray 

    * [POV-Ray API](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/pov.api)

* Progress

    * [Progress properties](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/progress.properties)
    * Please see [http://www.yuvcom.com/progress4gl](http://www.yuvcom.com/progress4gl) for more information.

* TADS3 

    * [TADS3 property file] and explanation(https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/tads3.zip)
    
* Windows Scripting 

    * [Properties files](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files/windows_scripting.zip)
    * [More files and scripts](Customization_SciteForWindowsScripters.md)

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



<a name="how_to_make_api"></a>
### How to make an api file

