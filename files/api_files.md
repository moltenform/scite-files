

* [back](../README.md)
* [how to install a .api or .properties file from the list below](api_files_howto.md) (to enable calltips + completion)
* [how to create a .api file for your own code](api_files_howto_create_api.md)
* [how to add highlighting/folding for a new language](api_files_howto_create_lexer.md)

### Languages

<!-- website refers to these, but I don't see them in properties: Clarion, Progress, Asymptote, TADS3, Gui4Cli, PL/M, PowerBasic -->
<!-- these lexers are available, but not referred to, set(['', 'SML', 'mysql', 'powerbasic','', 'kvirc', '', 'cppnocase', '', 'a68k', 'po', 'DMIS', '', 'bib', '', 'clarionnocase', 'tcmd', 'DMAP', 'PL/M', 'mssql', 'phpscript', 'clarion', 'fcST', 'magiksf', 'gui4cli', '']) -->
<!-- these lexers are available and just need to be turned on manually, as described below: markdown, visualprolog, tads3, progress , asy, literatehaskell, apdl -->

* HTML, CSS, and JavaScript

    * HTML, CSS, and JavaScript have highlighting and folding already enabled by default
    * [JavaScript API file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/javascript.api)
    * [JavaScript JQuery API file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/javascript_jquery.api) and [properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/javascript.properties)
    * [css api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/css.api)
    * [html api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/html.api)

* Abaqus

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `abaqus`, then save and restart SciTE

* ActionScript (Flash)

    * highlighting and folding is already enabled by default
    * [actionscript api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/actionscript.api)

* Ada

    * highlighting and folding is already enabled by default

* AMPL

    * [Properties file, api file, tools and setup instructions.](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/ampl.zip)

* APDL

    * highlighting and folding is enabled after the properties file below is installed
    * [APDL properties and API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/apdl.zip)

* Assembler (NASM/MASM)

    * highlighting and folding is already enabled by default
    
* Asl (ACPI Source)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `asl`, then save and restart SciTE

* ASN.1 MIB

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `asn1`, then save and restart SciTE
    
* ASP

    * highlighting and folding is already enabled by default
    * [ASP API methods](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/asp.api)
    * Edit html.properties to set the language of scripts in ASP code
        * If asp.default.language=1, script in an ASP code block is JavaScript
        * If asp.default.language=2, script in an ASP code block is VBScript
        * If asp.default.language=3, script in an ASP code block is Python

* Asymptote

    * highlighting and folding is enabled after the properties file below is installed
    * [Properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/asymptote.properties)
    
* Auto It3 

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `au3`, then save and restart SciTE
    * [SciTE4AutoIt3 Website containing Auto It3 related properties and API files.](https://www.autoitscript.com/site/autoit-script-editor/)
    * [au3 API file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/au3.api)

* AutoHotkey (AHK)

    * [AutoHotkey properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/ahk.properties)
    * [SciTE4AutoHotkey](https://github.com/fincs/SciTE4AutoHotkey) custom SciTE build for ahk
    * [ahk API file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/ahk.api)

* AutoCAD Dialog Box components

    * [DCL properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/adcl.properties)

* Avenue (Ave)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `ave`, then save and restart SciTE

* AviSynth (avs)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `avs`, then save and restart SciTE

* baan

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `baan`, then save and restart SciTE

* Batch files (MS-DOS)

    * highlighting and folding is already enabled by default
    * [API Files for Batch](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/batch.api.zip) (API files for NT, XP/2003, GNUWin32 UnixUtils and SysInternals commands)

* Bash

    * highlighting and folding is already enabled by default

* BlitzBasic

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `blitzbasic`, then save and restart SciTE

* Bullant

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `bullant`, then save and restart SciTE
    
* C/C++

    * highlighting and folding is already enabled by default
    * [C standard library](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/c_withdoc.api) with short doc strings
    * [C standard library](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/c.api)
    * [C++ standard library, incl C++11](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/cpp.api)
    * [cpp_more.properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/cpp_more.properties) adds highlighting for c99, c11, cpp98, cpp11, Objective C, idl, Doxygen, Arduino, go, Actionscript, vala, pike, swift
    * [Windows API, cpp](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/cpp_win32.api)
    * [OpenGL 1.2 API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/opengl.api)
    * [OpenGL 4.4 API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/glext.api)
    * [Glut API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/glut.api)
    * [SDL API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/sdl.api)

* C#

    * highlighting and folding is already enabled by default
    * [C# csharp api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/c_sharp.api)

* CIL 

    * [Properties for CIL/MSIL](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/il.properties)

* Clojure

    * [a lisp.properties including support for Scheme and Clojure](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lisp_and_closure.properties)
    * [api file for Clojure](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/clojure.api)

* CMake

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `cmake`, then save and restart SciTE
    * [CMake API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/cmake.api)

* COBOL

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `cobol`, then save and restart SciTE

* Cobra

    * [Properties for Cobra and Cobraproj](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/cobra.zip)

* coffeescript

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `coffeescript`, then save and restart SciTE

* conf (Apache)

    * highlighting and folding is already enabled by default

* csound

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `csound`, then save and restart SciTE

* D

    * highlighting and folding is already enabled by default

* Delphi

    * highlighting and folding is already enabled by default
    * [Delphi api files and abbrevs](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/delphi_extras.zip) 

* diff files

    * highlighting and folding is already enabled by default

* ecl

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `ecl`, then save and restart SciTE

* Eiffel

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `eiffel`, then save and restart SciTE

* Erlang

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `erlang`, then save and restart SciTE

* E-Script (escript)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `escript`, then save and restart SciTE

* Flagship

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `flagship`, then save and restart SciTE
    
* Forth

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `forth`, then save and restart SciTE
    * [api file for Forth](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/forth.api)
    
* Fortran

    * highlighting and folding is already enabled by default
    * [Standard FORTRAN API functions](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/fortran.api)

* Freebasic

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `freebasic`, then save and restart SciTE
    * [properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/freebasic.properties) that highlights more keywords
    * [api file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/freebasic.api)
    
* GAP

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `gap`, then save and restart SciTE

* Gettext

    * highlighting and folding is already enabled by default
    
* GLPK/GMPL (MathProg)

    * a LP/MILP IDE based on SciTE can be found [here](https://sourceforge.net/projects/gusek/?source=directory)

* Go

    * highlighting and folding is already enabled by default

* Haml

    * [properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/haml.properties)

* Haskell

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `haskell`, then save and restart SciTE
    * literatehaskell support can be enabled by copying `haskell.properties` to `lhaskell.properties`, changing all references to .hs to .lhs, and changing the line `lexer.*.lhs=haskell` to `lexer.*.lhs=literatehaskell`

* Intel HEX (hex)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `hex`, then save and restart SciTE

* InnoSetup (inno)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `inno`, then save and restart SciTE

* IDL/MSIDL/XPIDL

    * highlighting and folding is already enabled by default

* indent

    * a lexer for plain text docs that supports folding on indentation levels
    * highlighting and folding is already enabled by default

* INI

    * highlighting and folding is already enabled by default

* Java <!-- used to link to https://www.burgaud.com/scite-java-api/ , but put this info in instructions instead -->
    
    * highlighting and folding is already enabled by default
    * [Java properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/java.properties), including Java 1.8 keywords
    * [Java API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/java.api)
    * [Java API, other versions incl 1.5 and 1.6](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/javaversions.api.zip)
    
* json and json-ld

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `json`, then save and restart SciTE

* KiXtart (kix)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `kix`, then save and restart SciTE

* LaTeX / TeX

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `latex`, then save and restart SciTE
    * a [description](http://www.pragma-ade.com/general/manuals/scite-context-readme.pdf) and [Windows package](http://wiki.contextgarden.net/Windows_Installation:_ConTeXt_Suite_with_SciTe) of how to add highlighting, spellcheck, and extensions for using ConTeXt and SciTe
    
* LISP, Scheme (scm smd)

    * highlighting and folding is already enabled by default
    
* LOT

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `lot`, then save and restart SciTE

* Lout

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `lout`, then save and restart SciTE
    
* Lua  <!--  https://github.com/arjunae/myScite has a lua.properties with a few more keywords to highlight  -->

    * highlighting and folding is already enabled by default
    * [Lua standard library](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lua.api)
    * [Api for SciTE extension scripts](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lua_scite_extension.api)
    * [Lua 5.1, 5.2, 5.3 C API and luajit](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lua_c_api.zip)
    * [Lua 5.0 C API and standard library](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lua_5.0_api.zip)
    * [scite-for-lua](https://code.google.com/archive/p/scite-for-lua/), extensive support for Lua programming, including debugging and a lint-based highlighter
    * [lua-inspect](https://github.com/davidm/lua-inspect), plugin for SciTE that does Lua code analysis and adds features like rename-occurrences and autocomplete
    * [Api for wxLua](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lua_wx.api)
    * [Api for WoW lua](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/lua_wow.api)

* Make / makefile

    * highlighting and folding is already enabled by default

* markdown

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `markdown`, then save and restart SciTE
    * an alternate [properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/markdown_alt.properties) for markdown

* Matlab

    * highlighting and folding is already enabled by default

* maxima

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `maxima`, then save and restart SciTE

* Metapost

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `metapost`, then save and restart SciTE

* MetaQuotes language (MQL4, MQL5, MT4)

    * [properties for MQL4, MQL5](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/mql.properties)
    * The [scite-mql](https://github.com/ylw633/scite-mql) project adds syntax highlighting, autocomplete, parameter hints, and more for MT4 based code

* Microsoft SQL / MSSQL

    * highlighting and folding is already enabled by default
    * [Replace sql.properties with this, for better MSSQL support](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/mssql.properties)

* MMIXAL

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `mmixal`, then save and restart SciTE

* Modula 3 (modula3)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `modula3`, then save and restart SciTE

* moonscript

    * [properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/moonscript.properties)
    * a package containing SciTE, scintillua, and moonscript highlighting can be found [here](http://leafo.net/posts/getting_started_with_moonscript.html)

* Nimrod

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `nimrod`, then save and restart SciTE

* nncron / nncrontab

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `nncrontab`, then save and restart SciTE
    * [nncron api file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/nncron.api) 

* NSIS (nullsoft install)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `nsis`, then save and restart SciTE
    * [nsis api file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/nsis.api) 

* Objective C

    * highlighting and folding is already enabled by default

* OCaml and mli/sml

    * highlighting and folding is already enabled by default

* Octave

    * highlighting and folding is already enabled by default
    * [octave.api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/octave.api)

* Opal

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `opal`, then save and restart SciTE

* Oracle 

    * [Extended properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/sql_more.properties) with additional keywords and standard package names
    * [sql plsql](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/sql_plsql.api.zip) properties file

* OScript

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `oscript`, then save and restart SciTE
    * [oscript.api.zip](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/oscript.api.zip)

* Pascal

    * highlighting and folding is already enabled by default
    * Pascal [API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/pascal.api) 
    * Pascal [Abbreviations](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/pascal.abbrev) 

* Perl

    * highlighting and folding is already enabled by default
    * [Perl API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/perl.api)
    * [Parrot properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/parrot_properties.zip)

* PHP

    * highlighting and folding is already enabled by default
    * [php.api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/php.api) and [phpfunctions.properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/phpfunctions.properties) (without PECL extensions)
    * [php-all.api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/php-all.api) and [phpfunctions-all.properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/phpfunctions-all.properties) (all extensions)
    * [php.api in Spanish, PHP 5](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/php-es.api)

* PostScript

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `ps`, then save and restart SciTE

* POV-Ray 

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `pov`, then save and restart SciTE
    * [POV-Ray API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/pov.api)

* PowerPro

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `powerpro`, then save and restart SciTE

* PowerShell (ps1/ps2)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `powershell`, then save and restart SciTE

* Progress

    * highlighting and folding is enabled after the properties file below is installed
    * [Progress properties](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/progress.properties)

* PureBasic

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `purebasic`, then save and restart SciTE

* Python

    * highlighting and folding is already enabled by default
    * api files and keywords files for [Python 3.11](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/python311.api.zip), [Python 3.8](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/python38.api.zip), [Python 3.7](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/python37.api.zip)
    * [Automatically print the contents of local variables on unhandled exceptions](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/python_print_vars.zip)
    * api file for [numpy](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/py_numpy.zip)
    * api file for [scipy](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/py_scipy.zip)
    * older [Python API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/python.api) including PIL, psycho

* R

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `r`, then save and restart SciTE
    * a [properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/r.properties) with additional keyword highlighting

* Rebol

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `rebol`, then save and restart SciTE

* Registry

    * highlighting and folding is already enabled by default

* Ruby

    * highlighting and folding is already enabled by default
    * [Ruby API](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/ruby.api)

* Rust

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `rust`, then save and restart SciTE
    
* Scheme

    * highlighting and folding is already enabled by default

* scriptol

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `scriptol`, then save and restart SciTE
    
* Smalltalk

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `smalltalk`, then save and restart SciTE

* SORCUS Installation (sorcins)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `sorcins`, then save and restart SciTE

* Specman E (specman)

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `specman`, then save and restart SciTE

* Spice

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `spice`, then save and restart SciTE

* SQL and PLSQL <!--  https://github.com/arjunae/myScite has a sql.properties with a few more keywords to highlight  -->

    * highlighting and folding is already enabled by default

* S-Record

    * highlighting and folding is already enabled by default

* Swift

    * highlighting and folding is already enabled by default

* TACL

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `tacl`, then save and restart SciTE

* TADS3 

    * highlighting and folding is enabled after the properties file below is installed
    * [TADS3 property file and explanation](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/tads3.zip)

* TAL

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `tal`, then save and restart SciTE
    
* Tcl/Tk

    * highlighting and folding is already enabled by default

* txt2tags

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `txt2tags`, then save and restart SciTE

* Vala

    * highlighting and folding is already enabled by default

* Verilog

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `verilog`, then save and restart SciTE

* VHDL

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `vhdl`, then save and restart SciTE

* Visual Basic

    * highlighting and folding is already enabled by default
    * vb [properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/vb.properties) with more keywords

* VBScript

    * highlighting and folding is already enabled by default
    * [vbscript api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/vbscript.api)
    * vbscript [properties file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/vbscript.properties)
    * [vba api file](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/vba.api)

* visualprolog

    * to enable highlighting and folding, open `SciTEGlobal.properties`, look for `imports.exclude=`, delete `visualprolog`, then save and restart SciTE

* Windows Scripting 

    * [Properties files](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/windows_scripting.zip)
    * [More files and scripts](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/windows_scripting_scripts.zip), refer to readme.txt
    * [wsh.api](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/wsh.api) for vbscript calling into ActiveX objects like Scripting.FileSystemObject

* XML

    * highlighting and folding is already enabled by default

* YAML

    * highlighting and folding is already enabled by default

The scintillua project adds highlighting and folding for more than 120 languages, but it requires configuration to install. scintillua can be downloaded from [here](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/api_files/scintillua.zip), and see doc/manual.md. A .properties file is still needed to map the file extension to the lexer, more information [here](https://foicica.com/scintillua/README.html).

To contribute a file to this list, send an e-mail to scitewiki at gmail dot com or submit a pull request. 

How to install a file downloaded above? Refer to the links at the top of this page for instructions.
