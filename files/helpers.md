[Back](../README.md)

### Information

* An [introduction to adding features to SciTE with Lua scripts](./files/helpers/adding_scite_features_with_lua.md), read this to learn how to install a .lua script in the list below

### Scripts for SciTE

* [extman](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/extman.zip) 

    * dispatches scite events so that many lua scripts can be installed at the same time without conflict. For example, you might have several different scripts that each need to respond to the OnOpen event.

* [Mitchell's SciTE Tools](https://github.com/btakita/scite-tools), powerful text-editing utilities including snippets.lua

* [swapheader](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/swapheader/swapheader.html) move from a .c to a .h, with installation tips

* [autoblock.zip](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/autoblock.zip) lua scripts for block completion, by Mario Ray M.

* [move selection up/down](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/move_or_copy_selection_up_or_down.lua), lua script from the scite-ru project

* [SciTE Windows Context menu](https://github.com/andreburgaud/wscitecm), by andre burgaud

* [scitecmd](http://www.frykholm.se/scitecmd.html) open files in SciTE from the Windows command line

* [Orthospell](http://tools.diorama.ch/orthospell.html), spellcheck for SciTE, based on [luahunspell](https://code.google.com/p/luahunspell/)

* [Serge Baranov's scripts](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/perlformatters.txt) using Perl to reformat/clean up whitespace in a document

* [live markdown preview from SciTE](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/markdown.txt)

* yipf's [SciTEStartup.lua](https://github.com/yipf/scite-files/blob/master/SciTEStartup.lua) has some useful scripts for automatically closing braces, expanding snippets when Tab is pressed, spell check, word counting, moving to the beginning/end of a sentence, and more

* adding features to scite with lua scripts, I've [archived the content of lua-users SciTE scripts](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/lua-users-scite-scripts.zip) using wayback machine to recover most of the missing content. containing many lua scripts for SciTE, including scripts for AsciiTable, AutoCompleteAnyLanguage, AutoExpansion, BackupFile, BufferSwitch, Calculator, CleanDocWhitespace, CleanWhiteLines, ColouriseDemo, CommentBox, ConvertDecHex, CustomFolding, Debug, DeleteBlankLines, DisplayFunctions, EditWithVim, ElizaClassic, ExternalFileBrowser, ExtMan, Favs, FileBrowser, FuncList, HexEdit, Hexify, HtmlEntities, Indentation, InplaceCalculator, InsertDate, JavadocComment, Latex, LineBreak, ListAllOccurances, LuaDll, LuaPrompt, MacroExpander, MakeMonospace, ManPages, MarkWord, MergeOnChange, MiscScripts, NumberedBookmarks, OpenFilename, OpenPhpLocalhost, OpenToLine, OpenUrl, Other, ProcessString, Programmers, ProgrammingUtils, QuickStartXhtml, ReadTags, RunOneScript, ScriptManager, Scripts, SimpleTemplate, SortSelection, StripTrailings, TabsToSpacesObserveTabstop, Tags, TextFolding, TicTacToe, TitleCase, UnicodeInput, UsingUnicode, WordSelect, WordSubstitution, and XmlAutocompletion. The original wiki was [here](http://lua-users.org/wiki/SciteScripts)

* adding features to scite with lua scripts, here are [some lua scripts from the scite-ru project](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite-ru-scripts.zip) including abbrevlist, ascii_table, auto_backup, auto_complete_object, change_comment_char, codepage, code_poster2, code_poster_html, color_set, copymarkedlines, css_formatter, event_manager, exec, find_text, fold_text, font_changer, goto_line, highlighting_identical_text, highlighting_text, highlight_links, html_tags_autoclose, indent_tab_to_space, insertspecialchar, lexer_name, luainspect_install, macro_support, make_abbrev, move_lines, movemenuitem, new_file, open_selected_filename, open_find_files, paired_tags, readonly, recode, rename, restore_recent, rocheck, rowrite, save_settings, set_html, showcalltip, sidebar, smartbraces, smartcomment, sort_text, style_changer, svn_menu, translit, url_detect, value, xcomment, and zoom


### Lua utilities

Building blocks for SciTE lua scripts

* [scite_msg](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_msg.zip) 

    * a command-line tool that can send messages to a scite window, by Ben Fisher (uses some code from scite_other)

* [SciTE.Helper](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/SciTE.Helper.zip) 

    * an ActiveX control that can send messages to scite, can be used by jscript/vbscript and probably a hta UI

* [scite_other](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_other.zip) 

   * example code that finds a SciTE instance and sends it a message, or starts a new SciTE instance if none found, by Steve Donovan
   
* [lua_shell_dll](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/lua_shell_dll.zip)

    * this lua extension library, place in the same directory as scite, allows scite lua scripts to call:
    * `shell.msgbox` Showing text message with buttons.
    * `shell.inputbox` Display dialog box for input some text value.
    * `shell.getfileattr`, `shell.setfileattr`, `shell.fileexists
    * `shell.exec` a prettier 'exec' (to start a process) that doesn't show a window
    * `shell.findfiles` Searches for files and folders with mask and returned result as the table.

* [scite_other](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_lua_startprocess.zip) 

    * the basis for `scite_lua_extensions`. this lua extension library, place in the same directory as scite, allows scite lua scripts to call:
    * `shell.exec` a prettier 'exec' (to start a process) that doesn't show a window

### Gui addons

* [sciteproj](https://savannah.nongnu.org/projects/sciteproj/), project manager for SciTE 

* [hilfer](https://rubygems.org/gems/hilfer/), keyboard-rich directory browser using ruby-gtk that talks to SciTE

* [SciTE sidebar extension](http://valentin.dasdeck.com/projects/scite_sidebar/), adds tabs for opening files, ftp, functions, and more

* [Steve D's SciTE-GUI](https://groups.google.com/forum/#!topic/scite-interest/yZubpejP-bM) extension for SciTE Lua to add lists, file and colour dialogs, floating toolbar, and more

* [scite-gui](https://github.com/frank-w/scite-gui) GTK tool for changing SciTE settings, last updated 2010

### Add to this page

You can add to this page by submitting a pull request, or sending an e-mail to scitewiki at gmail dot com






