[Back](../README.md)

### Information

* An [introduction to adding features to SciTE with Lua scripts](./files/helpers/adding_scite_features_with_lua.md), read this to learn how to install a .lua script in the list below

### Scripts for SciTE

* [swapheader](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/swapheader.lua) move from a .c to a .h. Read the "Installing someone else's Lua script" section in [this guide](./files/helpers/adding_scite_features_with_lua.md) for installation instructions.

* [autoblock.zip](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/autoblock.zip) lua scripts for block completion, by Mario Ray M.

* [See ascii codes in selection](./files/helpers/see_ascii_selection.md)

* [smartpaste](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/smartpaste.lua), lua script to correctly indent pasted code

* [scitecmd](http://www.frykholm.se/scitecmd.html) open files in SciTE from the Windows command line

* [SciTE Windows Context menu](https://github.com/andreburgaud/wscitecm), by andre burgaud

* [Orthospell](http://tools.diorama.ch/orthospell.html), spellcheck for SciTE, based on [luahunspell](https://code.google.com/p/luahunspell/)

* [extman](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/extman.zip) 

    * dispatches scite events so that many lua scripts can be installed at the same time without conflict. You might have several different scripts that each need to respond to the OnOpen event, and extman lets each script coexist.

* [live markdown preview from SciTE](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/markdown.txt)

* [Mitchell's SciTE Tools](https://github.com/btakita/scite-tools), text-editing utilities including snippets.lua

* [Serge Baranov's scripts](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/perlformatters.txt) using Perl to reformat/clean up whitespace in a document

* yipf's [SciTEStartup.lua](https://github.com/yipf/scite-files/blob/master/SciTEStartup.lua) has some useful scripts for automatically closing braces, expanding snippets when Tab is pressed, spell check, word counting, moving to the beginning/end of a sentence, and more

* I've [archived the content of lua-users SciTE scripts](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/lua-users-scite-scripts.zip) using wayback machine to recover most of the missing content. containing many lua scripts for SciTE, including scripts for AsciiTable, AutoCompleteAnyLanguage, AutoExpansion, BackupFile, BufferSwitch, Calculator, CleanDocWhitespace, CleanWhiteLines, ColouriseDemo, CommentBox, ConvertDecHex, CustomFolding, Debug, DeleteBlankLines, DisplayFunctions, EditWithVim, ElizaClassic, ExternalFileBrowser, ExtMan, Favs, FileBrowser, FuncList, HexEdit, Hexify, HtmlEntities, Indentation, InplaceCalculator, InsertDate, JavadocComment, Latex, LineBreak, ListAllOccurances, LuaDll, LuaPrompt, MacroExpander, MakeMonospace, ManPages, MarkWord, MergeOnChange, MiscScripts, NumberedBookmarks, OpenFilename, OpenPhpLocalhost, OpenToLine, OpenUrl, Other, ProcessString, Programmers, ProgrammingUtils, QuickStartXhtml, ReadTags, RunOneScript, ScriptManager, Scripts, SimpleTemplate, SortSelection, StripTrailings, TabsToSpacesObserveTabstop, Tags, TextFolding, TicTacToe, TitleCase, UnicodeInput, UsingUnicode, WordSelect, WordSubstitution, and XmlAutocompletion. The original wiki was [here](http://lua-users.org/wiki/SciteScripts)

* here are [some lua scripts from the my-scite project](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/my_scite_scripts.zip) including AutoComplete, Calculator, HexEdit, Socket, and sortText. myScite also includes completing snippets, the orthospell spell-checker, custom language parsers via scintillua, debugging/stepping capabilities, and a sidebar for lua ui. see more at the [myScite project](https://github.com/arjunae/myScite). 

* here are [some lua scripts from the scite-ru project](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/scite-ru-scripts.zip) including move_lines, abbrevlist, ascii_table, auto_backup, auto_complete_object, change_comment_char, codepage, code_poster2, code_poster_html, color_set, copymarkedlines, css_formatter, event_manager, exec, find_text, fold_text, font_changer, goto_line, highlighting_identical_text, highlighting_text, highlight_links, html_tags_autoclose, indent_tab_to_space, insertspecialchar, lexer_name, luainspect_install, macro_support, make_abbrev, movemenuitem, new_file, open_selected_filename, open_find_files, paired_tags, readonly, recode, rename, restore_recent, rocheck, rowrite, save_settings, set_html, showcalltip, sidebar, smartbraces, smartcomment, sort_text, style_changer, svn_menu, translit, url_detect, value, xcomment, and zoom

* here are [some lua scripts from the scite_scripts project](https://github.com/mkottman/scite_scripts) including gitdiff, mark_word, and xml_close_tag

* [Lua Exporters](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/SciTELuaExporters-0.9.11.zip)  includes an enhanced PDF exporter (with line wrapping and kerning), an OpenOffice.org format exporter, an AbiWord format exporter, and an ODT (Open Document) exporter.

* Kein-Hong Man has developed a [calculator script](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/scite_calculator.zip) and [hex editor script](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/scite_hexedit.zip) that run within SciTE

### Lua utilities

Building blocks for SciTE lua scripts

* [moltenform_scite_utils.lua](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/moltenform_scite_utils.lua) and its [API documentation](./files/helpers/moltenform_scite_utils_api.md)

* [extman](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/extman.zip)

* [some lua utilities from the myscite project](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/my_scite_lua.zip) including running COM from lua, listing lua definitions, parsing CTags, and adding per-project CTags support, and snippets. also, lua utilities for bit manipulation, classes, md5, regular expresions, and the "serpent" pretty printer.

* [scite_msg](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/scite_msg.zip) 

    * a command-line tool that can send messages to a scite window, by Ben Fisher (uses some code from scite_other)

* [scite_other](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/scite_other.zip) 

   * example code that finds a SciTE instance and sends it a message, or starts a new SciTE instance if none found, by Steve Donovan
   
* [lua_shell_dll](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/lua_shell_dll.zip)

    * this lua extension library, place in the same directory as scite, allows scite lua scripts to call:
    * `shell.msgbox` Showing text message with buttons.
    * `shell.inputbox` Display dialog box for input some text value.
    * `shell.getfileattr`, `shell.setfileattr`, `shell.fileexists
    * `shell.exec` a prettier 'exec' (to start a process) that doesn't show a window
    * `shell.findfiles` Searches for files and folders with mask and returned result as the table.

* [scite_lua_startprocess](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/scite_lua_startprocess.zip) 

    * this lua extension library, place in the same directory as scite, allows scite lua scripts to call:
    * `shell.exec` a prettier 'exec' (to start a process) that doesn't show a window
    
* [SciTE.Helper](https://raw.githubusercontent.com/moltenform/scite-files/master/files/files/helpers/SciTE.Helper.zip) 

    * an ActiveX control that can send messages to scite, can be used by jscript/vbscript and probably a hta UI
    
* [scite-strip-wrapper](https://github.com/klonuo/scite-strip-wrapper) shows how to add strip dialog in SciTE so that your lua scripts can show UI

### Gui addons / patches

* [sciteproj](https://savannah.nongnu.org/projects/sciteproj/), project manager for SciTE 

* [SciTE sidebar extension](http://valentin.dasdeck.com/projects/scite_sidebar/), adds tabs for opening files, ftp, functions, and more

* [hilfer](https://rubygems.org/gems/hilfer/), keyboard-rich directory browser using ruby-gtk that talks to SciTE

* [Steve D's SciTE-GUI](https://groups.google.com/forum/#!topic/scite-interest/yZubpejP-bM) extension for SciTE Lua to add lists, file and colour dialogs, floating toolbar, and more

* [scite-gui](https://github.com/frank-w/scite-gui) GTK tool for changing SciTE settings, last updated 2010

* [Example Ruby extension](https://groups.google.com/forum/#!topic/scite-interest/cl6DogvZz2k)

### Add to this page

You can add to this page by submitting a pull request, or sending an e-mail to scitewiki at gmail dot com

