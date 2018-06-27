[Back](../README.md)

### Scripts/addons

Helper scripts and addons for SciTE, including lua scripts and lua tips

* [Mitchell's SciTE Tools](https://github.com/btakita/scite-tools), powerful text-editing utilities (including snippets.lua)

* [lua-users SciTE Scripts](http://lua-users.org/wiki/SciteScripts) contains many lua scripts for SciTE

* [swapheader](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/swapheader/swapheader.html) move from a .c to a .h, also describes how to set up a lua script in SciTE

* [autoblock.zip](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/autoblock.zip) lua scripts for block completion, by Mario Ray M.

* [move selection up/down](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/move_or_copy_selection_up_or_down.lua), lua script from the scite-ru project

* [SciTE Windows Context menu](https://github.com/andreburgaud/wscitecm), by andre burgaud

* [scitecmd](http://www.frykholm.se/scitecmd.html) open files in SciTE from the Windows command line

* [sciteproj](https://savannah.nongnu.org/projects/sciteproj/), project manager for SciTE 

* [hilfer](https://rubygems.org/gems/hilfer/), keyboard-rich directory browser using ruby-gtk that talks to SciTE

* [extman](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/extman.zip) 

    * dispatches scite events so that many lua scripts can be installed at the same time without conflict. For example, you might have a few different scripts that each want to respond to the OnOpen event.

    * I've gathered what appears to be the latest version(s) of extman, send an e-mail scitewiki at gmail dot com if you have a more recent version

* [Orthospell](http://tools.diorama.ch/orthospell.html), spellcheck for SciTE, based on [luahunspell](https://code.google.com/p/luahunspell/)

* [Serge Baranov's scripts](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/perlformatters.txt) using Perl to reformat/clean up whitespace in a document

* [live markdown preview from SciTE](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/markdown.txt)

* [SciTE sidebar extension](http://valentin.dasdeck.com/projects/scite_sidebar/), adds tabs for opening files, ftp, functions, and more

* [Steve D's SciTE-GUI](https://groups.google.com/forum/#!topic/scite-interest/yZubpejP-bM) extension for SciTE Lua to add lists, file and colour dialogs, floating toolbar, and more

* [scite-gui](https://github.com/frank-w/scite-gui) GTK tool for changing SciTE settings, last updated 2010

### SciTE process communication

These might be useful for building your own tools

* [scite_msg](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_msg.zip) 

    * a command-line tool that can send messages to a scite window, by Ben Fisher (uses some code from scite_other)

* [SciTE.Helper](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/SciTE.Helper.zip) 

    * an ActiveX control that can send messages to scite, can be used by jscript/vbscript and probably a hta UI

* [scite_other](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_other.zip) 

   * example code that finds a SciTE instance and sends it a message, or starts a new SciTE instance if none found, by Steve Donovan
   
* [scite_lua_extensions](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_lua_extensions.zip)

    * this lua extension library, place in the same directory as scite, allows scite lua scripts to call:
    * `shell.msgbox` Showing text message with buttons.
    * `shell.inputbox` Display dialog box for input some text value.
    * `shell.getfileattr`, `shell.setfileattr`, `shell.fileexists
    * `shell.exec` a prettier 'exec' (to start a process) that doesn't show a window
    * `shell.findfiles` Searches for files and folders with mask and returned result as the table.

* [scite_other](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_lua_startprocess.zip) 

    * the basis for `scite_lua_extensions`. this lua extension library, place in the same directory as scite, allows scite lua scripts to call:
    * `shell.exec` a prettier 'exec' (to start a process) that doesn't show a window

### Add to this page

You can add to this page by submitting a pull request, or sending an e-mail to scitewiki at gmail dot com






