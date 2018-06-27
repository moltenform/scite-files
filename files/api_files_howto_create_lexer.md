
[back](api_files.md)

### Add highlighting/folding for a new language

If the language is similar enough to a language already supported by SciTE, you might be able to copy the properties file for that language and change to it to match your new language.

If this does not work, you can write a piece of code that SciTE calls a "lexer".

* a lexer defines how to add syntax highlighting and/or folding

* it's less complex than actually parsing the file that the user is editing

* in recent versions of SciTE, a lexer can be written in the Lua language (simpler and doesn't require a C++ compiler)

* documentation on [Writing a lexer in the Lua language](https://www.scintilla.org/ScriptLexer.html) 

* Andreas Tscharner's tutorial for adding [Syntax Highlighting & Code Folding](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_new_lexer/newlexertutorial.pdf), and [example code](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/api_files_new_lexer/newlexertutorialcode.tar.bz2) in C++

