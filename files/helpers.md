[Back](../README.md)n

### Scripts/addons

Helper scripts and addons for SciTE, including lua scripts and lua tips

* [Mitchell's SciTE Tools](https://github.com/btakita/scite-tools), powerful text-editing utilities (including snippets.lua)

* [lua-users SciTE Scripts](http://lua-users.org/wiki/SciteScripts) contains many lua scripts for SciTE

* [swapheader](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/swapheader/swapheader.html) move from a .c to a .h, also describes how to set up a lua script in SciTE

* [autoblock.zip](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/autoblock.zip) lua scripts for block completion, by Mario Ray M.

* [SciTE Windows Context menu](https://github.com/andreburgaud/wscitecm), by andre burgaud

  * [scitecmd](http://www.frykholm.se/scitecmd.html) open files in SciTE from the Windows command line

* [sciteproj](https://savannah.nongnu.org/projects/sciteproj/), project manager for SciTE 

* [scite-gui](https://github.com/frank-w/scite-gui) GTK tool for changing SciTE settings, last updated 2010

* [Hilfer](https://rubygems.org/gems/hilfer/), keyboard-rich directory browser using ruby-gtk that talks to SciTE

* [extman](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/extman.zip) 

    * dispatches scite events so that lua scripts can be installed at the same time without conflict

    * addresses this: SciTE Lua interface is very powerful, but presently there is no way to make non-trivial scripts 'play nice' with each other. Consider SciteBufferSwitch; the handlers OnOpen,OnSwitchFile and OnUserListSelection are all overriden to keep track of buffer changes and present a drop-down list of buffers. Such a script would interfere with any other script that had a need to watch these events.

    * editor's note: I've gathered what appears to be the latest version(s) of extman, send an e-mail scitewiki@gmail.com if you know of a more recent version

* [Orthospell](http://tools.diorama.ch/orthospell.html), spellcheck for SciTE, based on [luahunspell](https://code.google.com/p/luahunspell/)

### SciTE process communication

these might be useful for building your own tools

* [scite_msg](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_msg.zip) 

    * a command-line tool that can send messages to a scite window, by Ben Fisher/Steve Donovan

* [SciTE.Helper](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/SciTE.Helper.zip) 

    * an ActiveX control that can send messages to scite, can be used by jscript/vbscript and probably a hta UI

* [scite_other](https://raw.githubusercontent.com/downpoured/scite-files/master/files/files/helpers/scite_other.zip) 

   * lua scripts can use this to have a prettier process 'exec' that doesn't show a window, by Steve Donovan

Add to this page by submitting a pull request, or sending an e-mail to [scite-wiki@gmail.com](scite-wiki@gmail.com)









